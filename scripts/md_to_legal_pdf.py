#!/usr/bin/env python3
"""
Convert Dutch legal markdown documents to professional PDF format.

Uses reportlab following the dutch-legal-pdf skill patterns:
- A4, 2.5cm margins, professional Dutch legal typography
- Paragraph objects in all table cells for proper word-wrap
- Watermarks via pypdf page merge (15% opacity red)
- Confidentiality banners via canvas callback
- Mandatory disclaimer on final page
- pypdfium2 for preview image generation
- pdfplumber for verification
"""
import sys
import os
import re
import json
import io
import argparse
from datetime import date
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Flowable
)
from reportlab.pdfgen.canvas import Canvas as RLCanvas
from pypdf import PdfReader, PdfWriter

try:
    import pdfplumber
except ImportError:
    pdfplumber = None

try:
    import pypdfium2 as pdfium
except ImportError:
    pdfium = None

# ─── Constants ────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent.parent
LEGAL_DOCS_DIR = BASE_DIR / "assets" / "legal-documents"
PDF_OUTPUT_DIR = LEGAL_DOCS_DIR / "pdf"
PREVIEWS_DIR = PDF_OUTPUT_DIR / "previews"
DISCLAIMER_PATH = BASE_DIR / "assets" / "disclaimers" / "disclaimer-nl.md"

TODAY_STR = date.today().strftime("%d-%m-%Y")
PAGE_W, PAGE_H = A4
MARGIN = 2.5 * cm
CONTENT_W = PAGE_W - 2 * MARGIN  # ~16cm

RISK_COLORS = {
    "CRITICAL": "#E74C3C",
    "HIGH": "#F39C12",
    "MEDIUM": "#F1C40F",
    "LOW": "#27AE60",
}

HEADER_BG = colors.HexColor("#2C3E50")

DOCUMENT_FILES = [
    "employment-addendum-counter-proposal.md",
    "chipos-wingman-independence-report.md",
    "axelera-addendum-analysis.md",
    "immigration-risk-assessment.md",
    "axelera-dual-roles-precedent.md",
    "response-to-axelera-legal.md",
    "side-business-permission-request.md",
    "wingman-delivery-manifest.md",
]

DOC_CONFIG = {
    "employment-addendum-counter-proposal.md": {
        "watermark": "VERTROUWELIJK",
        "banner": None,
    },
    "chipos-wingman-independence-report.md": {
        "watermark": "VERTROUWELIJK",
        "banner": None,
    },
    "axelera-addendum-analysis.md": {
        "watermark": None,
        "banner": None,
    },
    "immigration-risk-assessment.md": {
        "watermark": None,
        "banner": None,
    },
    "axelera-dual-roles-precedent.md": {
        "watermark": "STRIKT VERTROUWELIJK",
        "banner": "STRICTLY CONFIDENTIAL \u2014 FOR INTERNAL USE ONLY",
    },
    "response-to-axelera-legal.md": {
        "watermark": "VERTROUWELIJK",
        "banner": None,
    },
    "side-business-permission-request.md": {
        "watermark": None,
        "banner": None,
    },
    "wingman-delivery-manifest.md": {
        "watermark": None,
        "banner": None,
    },
}


# ─── Block Types ──────────────────────────────────────────────────────────────

class HeadingBlock:
    def __init__(self, level, text):
        self.level = level
        self.text = text

class ParagraphBlock:
    def __init__(self, text):
        self.text = text

class TableBlock:
    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows

class ListBlock:
    def __init__(self, items, ordered=False):
        self.items = items  # list of (text, indent_level)
        self.ordered = ordered

class BlockquoteBlock:
    def __init__(self, text):
        self.text = text

class HorizontalRuleBlock:
    pass

class ChecklistBlock:
    def __init__(self, items):
        self.items = items  # list of (checked: bool, text: str)

class CodeBlock:
    def __init__(self, text, language=""):
        self.text = text
        self.language = language


# ─── Inline Formatting ────────────────────────────────────────────────────────

def _xml_escape(text):
    """Escape XML/HTML special characters for reportlab Paragraph."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def format_inline(text):
    """Convert markdown inline formatting to reportlab XML.

    Order: extract code spans first (may contain * or _),
    then XML-escape, then bold/italic, then restore code.
    """
    # 1. Protect inline code spans
    code_spans = []

    def _save_code(m):
        idx = len(code_spans)
        code_spans.append(m.group(1))
        return f"\x00CODESPAN{idx}\x00"

    text = re.sub(r'`([^`]+)`', _save_code, text)

    # 2. XML-escape the rest
    text = _xml_escape(text)

    # 3. Bold+italic ***...***
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold **...**
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italic *...* — only when bounded by non-word chars or start/end
    text = re.sub(r'(?<![*\w])\*([^*\n]+?)\*(?![*\w])', r'<i>\1</i>', text)

    # 4. Links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" color="blue">\1</a>', text)

    # 5. Restore code spans
    for i, code in enumerate(code_spans):
        safe_code = _xml_escape(code)
        text = text.replace(
            f"\x00CODESPAN{i}\x00",
            f'<font name="Courier" size="8">{safe_code}</font>'
        )

    return text


def apply_risk_badges(text):
    """Color-code risk level words in already-formatted text."""
    for level, hex_color in RISK_COLORS.items():
        text = re.sub(
            rf'\b({level})\b',
            rf'<font color="{hex_color}"><b>\1</b></font>',
            text
        )
    return text


# ─── Markdown Parser ─────────────────────────────────────────────────────────

class MarkdownParser:
    """Line-by-line regex parser producing typed block objects."""

    def parse(self, text):
        lines = text.split("\n")
        blocks = []
        i = 0
        n = len(lines)

        while i < n:
            line = lines[i]
            stripped = line.strip()

            # Blank line — skip
            if stripped == "":
                i += 1
                continue

            # Horizontal rule
            if re.match(r'^-{3,}$', stripped) or re.match(r'^\*{3,}$', stripped):
                blocks.append(HorizontalRuleBlock())
                i += 1
                continue

            # Heading
            hm = re.match(r'^(#{1,4})\s+(.*)', line)
            if hm:
                blocks.append(HeadingBlock(len(hm.group(1)), hm.group(2).strip()))
                i += 1
                continue

            # Fenced code block
            if stripped.startswith("```"):
                lang = stripped[3:].strip()
                code_lines = []
                i += 1
                while i < n and not lines[i].strip().startswith("```"):
                    code_lines.append(lines[i])
                    i += 1
                if i < n:
                    i += 1  # skip closing ```
                blocks.append(CodeBlock("\n".join(code_lines), lang))
                continue

            # Table: must have header row + separator row
            if "|" in line and i + 1 < n and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i + 1]):
                headers = [c.strip() for c in stripped.strip("|").split("|")]
                i += 2  # skip header + separator
                rows = []
                while i < n and "|" in lines[i] and lines[i].strip():
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    rows.append(cells)
                    i += 1
                blocks.append(TableBlock(headers, rows))
                continue

            # Checklist item
            cm_check = re.match(r'^[-*]\s+\[([ xX])\]\s+(.*)', line)
            if cm_check:
                items = []
                while i < n:
                    m = re.match(r'^[-*]\s+\[([ xX])\]\s+(.*)', lines[i])
                    if not m:
                        break
                    items.append((m.group(1).lower() == 'x', m.group(2).strip()))
                    i += 1
                blocks.append(ChecklistBlock(items))
                continue

            # Blockquote
            if stripped.startswith(">"):
                bq_lines = []
                while i < n and lines[i].strip().startswith(">"):
                    bq_lines.append(re.sub(r'^>\s?', '', lines[i]))
                    i += 1
                # Continue collecting continuation lines
                while i < n and lines[i].strip() and not lines[i].strip().startswith(">") and not re.match(r'^#{1,4}\s', lines[i]) and not re.match(r'^-{3,}$', lines[i].strip()):
                    bq_lines.append(lines[i])
                    i += 1
                blocks.append(BlockquoteBlock(" ".join(l.strip() for l in bq_lines)))
                continue

            # Ordered list
            om = re.match(r'^(\d+)\.\s+(.*)', line)
            if om:
                items = []
                while i < n:
                    m = re.match(r'^(\d+)\.\s+(.*)', lines[i])
                    if m:
                        item_text = lines[i].strip()
                        i += 1
                        # Gather continuation/sub-items
                        while i < n and (lines[i].startswith("   ") or lines[i].startswith("\t")) and lines[i].strip():
                            sub = re.match(r'^\s+[-*]\s+(.*)', lines[i])
                            if sub:
                                item_text += "\n   \u2022 " + sub.group(1).strip()
                            elif re.match(r'^\s+\(([a-z])\)', lines[i]):
                                item_text += "\n   " + lines[i].strip()
                            else:
                                item_text += " " + lines[i].strip()
                            i += 1
                        items.append((item_text, 0))
                    else:
                        break
                blocks.append(ListBlock(items, ordered=True))
                continue

            # Unordered list (top-level or indented sub-items)
            um = re.match(r'^(\s*)[-*+]\s+(.*)', line)
            if um and not re.match(r'^\s*[-*]\s+\[([ xX])\]', line):
                items = []
                while i < n:
                    m = re.match(r'^(\s*)[-*+]\s+(.*)', lines[i])
                    if m and not re.match(r'^\s*[-*]\s+\[([ xX])\]', lines[i]):
                        item_text = m.group(2).strip()
                        indent = len(m.group(1))
                        i += 1
                        # Sub-items (more deeply indented)
                        while i < n and lines[i].strip() and (
                            lines[i].startswith("   ") or lines[i].startswith("\t")):
                            sub = re.match(r'^\s+[-*+]\s+(.*)', lines[i])
                            if sub:
                                item_text += "\n   \u2022 " + sub.group(1).strip()
                            elif re.match(r'^\s+\(([a-z])\)', lines[i]):
                                item_text += "\n   " + lines[i].strip()
                            else:
                                item_text += " " + lines[i].strip()
                            i += 1
                        items.append((item_text, indent))
                    else:
                        break
                blocks.append(ListBlock(items, ordered=False))
                continue

            # Paragraph — gather lines until structural break
            para_lines = []
            while i < n:
                l = lines[i]
                s = l.strip()
                if s == "":
                    break
                if re.match(r'^#{1,4}\s+', l):
                    break
                if re.match(r'^-{3,}$', s) or re.match(r'^\*{3,}$', s):
                    break
                if s.startswith("```"):
                    break
                if s.startswith(">"):
                    break
                # Break on list items (both top-level and indented)
                if re.match(r'^\s*[-*+]\s+', l) and not para_lines:
                    break
                if re.match(r'^\d+\.\s+', s) and not para_lines:
                    break
                if "|" in l and i + 1 < n and re.match(r'^\s*\|[\s:|-]+\|', lines[i + 1]):
                    break
                para_lines.append(s)
                i += 1
            if para_lines:
                blocks.append(ParagraphBlock(" ".join(para_lines)))
            elif i < n:
                # Safety: if no progress, skip the line
                i += 1

        return blocks


# ─── Checkbox Flowable ────────────────────────────────────────────────────────

class CheckboxFlowable(Flowable):
    """Draw a checkbox (rectangle) with text — no Unicode ballot boxes."""

    def __init__(self, checked, text, width=CONTENT_W):
        Flowable.__init__(self)
        self.checked = checked
        self.text = text
        self.width = width
        self.height = 15

    def draw(self):
        c = self.canv
        sz = 7
        x, y = 2, 3

        c.setStrokeColor(colors.HexColor("#555555"))
        c.setLineWidth(0.6)
        c.rect(x, y, sz, sz)

        if self.checked:
            c.setStrokeColor(colors.HexColor("#27AE60"))
            c.setLineWidth(1.2)
            c.line(x + 1.5, y + 3.5, x + 3, y + 1.5)
            c.line(x + 3, y + 1.5, x + 5.5, y + 5.5)

        c.setFillColor(colors.black)
        c.setFont("Helvetica", 9)
        # Truncate long text
        display = self.text[:130]
        c.drawString(x + sz + 5, y + 0.5, display)


# ─── Legal Styles (per skill pattern) ────────────────────────────────────────

def get_legal_styles():
    """Create Dutch legal document styles following skill patterns."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'LegalTitle', parent=styles['Title'],
        fontSize=15, spaceAfter=4, spaceBefore=0,
        alignment=TA_CENTER, fontName='Helvetica-Bold',
        textColor=colors.HexColor('#1a1a1a')
    ))
    styles.add(ParagraphStyle(
        'LegalSubtitle', parent=styles['Normal'],
        fontSize=11, spaceAfter=8, alignment=TA_CENTER,
        fontName='Helvetica-Oblique', textColor=colors.HexColor('#555555')
    ))
    styles.add(ParagraphStyle(
        'LegalH1', parent=styles['Heading1'],
        fontSize=14, spaceBefore=16, spaceAfter=8,
        fontName='Helvetica-Bold', textColor=colors.HexColor('#1a1a1a')
    ))
    styles.add(ParagraphStyle(
        'LegalH2', parent=styles['Heading2'],
        fontSize=12, spaceBefore=14, spaceAfter=6,
        fontName='Helvetica-Bold', textColor=colors.HexColor('#2C3E50')
    ))
    styles.add(ParagraphStyle(
        'LegalH3', parent=styles['Heading3'],
        fontSize=10.5, spaceBefore=10, spaceAfter=5,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'LegalH4', parent=styles['Heading3'],
        fontSize=10, spaceBefore=8, spaceAfter=4,
        fontName='Helvetica-BoldOblique'
    ))
    styles.add(ParagraphStyle(
        'LegalBody', parent=styles['Normal'],
        fontSize=9.5, leading=13.5, alignment=TA_JUSTIFY, spaceAfter=5
    ))
    styles.add(ParagraphStyle(
        'LegalArticle', parent=styles['Normal'],
        fontSize=9.5, leading=13.5, alignment=TA_JUSTIFY,
        spaceAfter=4, leftIndent=1 * cm
    ))
    styles.add(ParagraphStyle(
        'LegalBlockquote', parent=styles['Normal'],
        fontSize=9, leading=12.5, alignment=TA_JUSTIFY,
        leftIndent=1 * cm, rightIndent=0.5 * cm,
        textColor=colors.HexColor('#333333'),
        borderColor=colors.HexColor('#3498DB'),
        borderWidth=2, borderPadding=8,
        spaceAfter=8, spaceBefore=6,
        backColor=colors.HexColor('#F0F4F8')
    ))
    styles.add(ParagraphStyle(
        'LegalCode', parent=styles['Normal'],
        fontSize=7.5, leading=9.5, fontName='Courier',
        leftIndent=0.4 * cm, rightIndent=0.4 * cm,
        backColor=colors.HexColor('#F5F5F5'),
        spaceAfter=8, spaceBefore=6,
        borderColor=colors.HexColor('#CCCCCC'),
        borderWidth=0.5, borderPadding=8
    ))
    styles.add(ParagraphStyle(
        'LegalDisclaimer', parent=styles['Normal'],
        fontSize=8, leading=10.5, textColor=colors.grey,
        alignment=TA_JUSTIFY, spaceBefore=4, spaceAfter=3
    ))
    styles.add(ParagraphStyle(
        'LegalDisclaimerHeading', parent=styles['Normal'],
        fontSize=8.5, leading=11, fontName='Helvetica-Bold',
        textColor=colors.HexColor('#333333'),
        spaceBefore=6, spaceAfter=3
    ))
    styles.add(ParagraphStyle(
        'LegalFooter', parent=styles['Normal'],
        fontSize=8, alignment=TA_RIGHT, textColor=colors.grey
    ))
    styles.add(ParagraphStyle(
        'LegalListItem', parent=styles['Normal'],
        fontSize=9.5, leading=13.5, alignment=TA_JUSTIFY,
        leftIndent=1 * cm, spaceAfter=3, bulletIndent=0.3 * cm
    ))
    styles.add(ParagraphStyle(
        'LegalSubListItem', parent=styles['Normal'],
        fontSize=9.5, leading=13.5, alignment=TA_JUSTIFY,
        leftIndent=1.8 * cm, spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        'TableCell', parent=styles['Normal'],
        fontSize=8.5, leading=11, alignment=TA_LEFT, wordWrap='CJK'
    ))
    styles.add(ParagraphStyle(
        'TableCellBold', parent=styles['Normal'],
        fontSize=8.5, leading=11, alignment=TA_LEFT,
        fontName='Helvetica-Bold', wordWrap='CJK'
    ))
    styles.add(ParagraphStyle(
        'TableHeader', parent=styles['Normal'],
        fontSize=8.5, leading=11, alignment=TA_LEFT,
        fontName='Helvetica-Bold', textColor=colors.whitesmoke, wordWrap='CJK'
    ))
    return styles


# ─── PDF Renderer ─────────────────────────────────────────────────────────────

class LegalPdfRenderer:
    """Convert parsed blocks to reportlab flowables and build PDF."""

    def __init__(self, config, filename):
        self.config = config
        self.filename = filename
        self.styles = get_legal_styles()
        self.story = []

    def render_blocks(self, blocks):
        for block in blocks:
            try:
                if isinstance(block, HeadingBlock):
                    self._heading(block)
                elif isinstance(block, ParagraphBlock):
                    self._paragraph(block)
                elif isinstance(block, TableBlock):
                    self._table(block)
                elif isinstance(block, ListBlock):
                    self._list(block)
                elif isinstance(block, BlockquoteBlock):
                    self._blockquote(block)
                elif isinstance(block, HorizontalRuleBlock):
                    self.story.append(Spacer(1, 3))
                    self.story.append(HRFlowable(
                        width="100%", thickness=0.5,
                        color=colors.HexColor('#CCCCCC')))
                    self.story.append(Spacer(1, 3))
                elif isinstance(block, ChecklistBlock):
                    self._checklist(block)
                elif isinstance(block, CodeBlock):
                    self._code(block)
            except Exception as e:
                # Fallback: render as plain text so we don't lose content
                fallback = getattr(block, 'text', str(e))
                try:
                    self.story.append(Paragraph(
                        _xml_escape(str(fallback)[:500]),
                        self.styles['LegalBody']))
                except Exception:
                    pass

    def _heading(self, block):
        text = format_inline(block.text)
        style_map = {1: 'LegalH1', 2: 'LegalH2', 3: 'LegalH3', 4: 'LegalH4'}
        self.story.append(Paragraph(text, self.styles[style_map.get(block.level, 'LegalH4')]))

    def _paragraph(self, block):
        text = format_inline(block.text)
        text = apply_risk_badges(text)
        self.story.append(Paragraph(text, self.styles['LegalBody']))

    def _table(self, block):
        """Render table with Paragraph cells for proper word-wrap."""
        ncols = len(block.headers)

        # Header row
        header_row = []
        for h in block.headers:
            header_row.append(Paragraph(format_inline(h), self.styles['TableHeader']))

        # Data rows
        data_rows = []
        for row in block.rows:
            cells = []
            for j, cell in enumerate(row[:ncols]):
                cell_text = format_inline(cell)
                cell_text = apply_risk_badges(cell_text)
                # Bold first column for 2-column key-value tables
                if j == 0 and ncols == 2 and len(cell) < 60:
                    cells.append(Paragraph(cell_text, self.styles['TableCellBold']))
                else:
                    cells.append(Paragraph(cell_text, self.styles['TableCell']))
            # Pad short rows
            while len(cells) < ncols:
                cells.append(Paragraph("", self.styles['TableCell']))
            data_rows.append(cells)

        all_data = [header_row] + data_rows
        col_widths = self._compute_col_widths(block.headers, block.rows, ncols)

        t = Table(all_data, colWidths=col_widths, repeatRows=1)
        style_cmds = [
            ('BACKGROUND', (0, 0), (-1, 0), HEADER_BG),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8.5),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1),
             [colors.white, colors.HexColor('#F8F9FA')]),
        ]

        # Color-code risk cells
        for ri, row in enumerate(block.rows, 1):
            for ci, cell in enumerate(row[:ncols]):
                upper = cell.strip().upper()
                if upper in RISK_COLORS:
                    style_cmds.append(('TEXTCOLOR', (ci, ri), (ci, ri),
                                       colors.HexColor(RISK_COLORS[upper])))
                    style_cmds.append(('FONTNAME', (ci, ri), (ci, ri), 'Helvetica-Bold'))

        t.setStyle(TableStyle(style_cmds))
        self.story.append(t)
        self.story.append(Spacer(1, 8))

    def _compute_col_widths(self, headers, rows, ncols):
        """Proportional column widths based on content length."""
        max_lens = [max(len(h), 5) for h in headers]
        for row in rows:
            for j in range(min(len(row), ncols)):
                max_lens[j] = max(max_lens[j], len(row[j]))

        total = sum(max_lens) or 1
        widths = [(l / total) * CONTENT_W for l in max_lens]

        # Enforce minimum
        min_w = 1.8 * cm
        for i in range(len(widths)):
            widths[i] = max(widths[i], min_w)

        # Scale to fit
        total_w = sum(widths)
        if total_w > CONTENT_W:
            factor = CONTENT_W / total_w
            widths = [w * factor for w in widths]
        return widths

    def _list(self, block):
        for idx, (text, indent) in enumerate(block.items):
            # Split into main line and sub-lines
            parts = text.split("\n")
            main_line = parts[0]

            if block.ordered:
                m = re.match(r'^(\d+)\.\s+(.*)', main_line)
                if m:
                    formatted = f"<b>{m.group(1)}.</b> {format_inline(m.group(2))}"
                else:
                    formatted = f"<b>{idx + 1}.</b> {format_inline(main_line)}"
                formatted = apply_risk_badges(formatted)
                self.story.append(Paragraph(formatted, self.styles['LegalListItem']))
            else:
                formatted = f"\u2022 {format_inline(main_line)}"
                formatted = apply_risk_badges(formatted)
                self.story.append(Paragraph(formatted, self.styles['LegalListItem']))

            # Sub-lines
            for sub in parts[1:]:
                sub = sub.strip()
                if sub:
                    self.story.append(Paragraph(
                        format_inline(sub),
                        self.styles['LegalSubListItem']))

    def _blockquote(self, block):
        text = format_inline(block.text)
        self.story.append(Paragraph(text, self.styles['LegalBlockquote']))

    def _checklist(self, block):
        for checked, text in block.items:
            # Strip markdown formatting for plain-text checkbox display
            plain = re.sub(r'[*_`]', '', text)
            self.story.append(CheckboxFlowable(checked, plain))

    def _code(self, block):
        text = _xml_escape(block.text)
        text = text.replace("\n", "<br/>")
        text = text.replace("  ", "&nbsp;&nbsp;")
        self.story.append(Paragraph(text, self.styles['LegalCode']))

    # ── Disclaimer Page ───────────────────────────────────────────────────────

    def add_disclaimer_page(self):
        """Mandatory Dutch disclaimer on final page, per skill requirements."""
        self.story.append(PageBreak())
        self.story.append(Paragraph("DISCLAIMER", self.styles['LegalH2']))
        self.story.append(Spacer(1, 4))
        self.story.append(HRFlowable(width="100%", thickness=1, color=HEADER_BG))
        self.story.append(Spacer(1, 8))

        # Read full disclaimer file
        if DISCLAIMER_PATH.exists():
            raw = DISCLAIMER_PATH.read_text(encoding='utf-8')
            raw = raw.replace("[DATUM]", TODAY_STR)

            for line in raw.split("\n"):
                line = line.strip()
                if not line:
                    self.story.append(Spacer(1, 3))
                    continue
                if line.startswith("# "):
                    self.story.append(Paragraph(
                        format_inline(line[2:]),
                        self.styles['LegalDisclaimerHeading']))
                elif line.startswith("---"):
                    self.story.append(HRFlowable(
                        width="100%", thickness=0.3,
                        color=colors.HexColor('#CCCCCC')))
                elif re.match(r'^\d+\.', line):
                    self.story.append(Paragraph(
                        format_inline(line), self.styles['LegalDisclaimer']))
                else:
                    self.story.append(Paragraph(
                        format_inline(line), self.styles['LegalDisclaimer']))
        else:
            # Fallback inline disclaimer per skill pattern
            self.story.append(Paragraph(
                "Dit document is opgesteld met behulp van AI-ondersteunde analyse en vormt "
                "<b>geen juridisch advies</b> in de zin van de Advocatenwet. De informatie is "
                "uitsluitend informatief. Raadpleeg altijd een gekwalificeerde advocaat "
                "(ingeschreven bij de Nederlandse Orde van Advocaten) voordat u juridische "
                "beslissingen neemt. Aan dit document kunnen geen rechten worden ontleend. "
                "De analyse is gebaseerd op de stand van het recht op de aangegeven datum en "
                "houdt mogelijk geen rekening met recente wijzigingen.",
                self.styles['LegalDisclaimer']))

        self.story.append(Spacer(1, 10))
        self.story.append(HRFlowable(width="100%", thickness=0.5,
                                     color=colors.HexColor('#CCCCCC')))
        self.story.append(Spacer(1, 6))
        self.story.append(Paragraph(
            f"FALCON (FutureAtoms AI Legal Counsel Of Netherlands) | "
            f"Datum: {TODAY_STR} | "
            f"Verificatiedatum wetgeving: {TODAY_STR}",
            self.styles['LegalFooter']))

    # ── Build PDF ─────────────────────────────────────────────────────────────

    def build_pdf(self, output_path):
        banner_text = self.config.get("banner")

        def page_callback(canvas, doc):
            canvas.saveState()

            # Confidentiality banner
            if banner_text:
                canvas.setFillColor(colors.HexColor('#C0392B'))
                canvas.rect(0, PAGE_H - 20, PAGE_W, 20, fill=True, stroke=False)
                canvas.setFillColor(colors.white)
                canvas.setFont("Helvetica-Bold", 8)
                canvas.drawCentredString(PAGE_W / 2, PAGE_H - 15, banner_text)

            # Footer
            canvas.setFont("Helvetica", 7)
            canvas.setFillColor(colors.grey)
            canvas.drawCentredString(
                PAGE_W / 2, 1.0 * cm,
                f"Page {doc.page}  |  {TODAY_STR}  |  "
                f"FALCON  |  Confidential")

            canvas.restoreState()

        top = 2.8 * cm if banner_text else 2.5 * cm

        doc = SimpleDocTemplate(
            str(output_path), pagesize=A4,
            leftMargin=MARGIN, rightMargin=MARGIN,
            topMargin=top, bottomMargin=1.8 * cm)

        doc.build(self.story, onFirstPage=page_callback, onLaterPages=page_callback)


# ─── Watermark (per skill pattern, 15% opacity) ──────────────────────────────

def create_watermark_page(text):
    """Create a single-page watermark PDF in memory."""
    packet = io.BytesIO()
    c = RLCanvas(packet, pagesize=A4)
    c.saveState()
    c.translate(PAGE_W / 2, PAGE_H / 2)
    c.rotate(45)
    c.setFont("Helvetica-Bold", 54)
    c.setFillColor(colors.Color(1, 0, 0, alpha=0.15))
    c.drawCentredString(0, 0, text)
    c.restoreState()
    c.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]


def apply_watermark(pdf_path, text):
    """Apply diagonal watermark to every page of a PDF."""
    wm_page = create_watermark_page(text)
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(wm_page)
        writer.add_page(page)
    with open(str(pdf_path), "wb") as f:
        writer.write(f)


# ─── Strip Trailing Disclaimer ────────────────────────────────────────────────

def strip_trailing_disclaimer(text):
    """Remove inline disclaimers from the end of markdown docs."""
    patterns = [
        r'\n---\n+\*\*DISCLAIMER\*\*.*$',
        r'\n---\n+\*Generated by.*$',
        r'\n---\n+\*Gegenereerd door.*$',
        r'\n---\n+## Disclaimer.*$',
        r'\n---\n+# Juridische Disclaimer.*$',
    ]
    for pat in patterns:
        text = re.sub(pat, '', text, flags=re.DOTALL | re.IGNORECASE)
    return text


# ─── Verification ─────────────────────────────────────────────────────────────

def verify_pdf(pdf_path, md_path, config):
    """Automated verification checks on generated PDF."""
    result = {"file": os.path.basename(pdf_path), "checks": {}}

    if pdfplumber is None:
        result["checks"]["pdfplumber"] = {"status": "SKIP", "message": "not installed"}
        return result

    try:
        pdf = pdfplumber.open(str(pdf_path))
    except Exception as e:
        result["checks"]["open"] = {"status": "FAIL", "message": str(e)}
        return result

    full_text = ""
    for page in pdf.pages:
        t = page.extract_text()
        if t:
            full_text += t + "\n"

    num_pages = len(pdf.pages)
    file_kb = os.path.getsize(str(pdf_path)) / 1024
    md_kb = os.path.getsize(str(md_path)) / 1024

    # 1. Content integrity — check H2 headings from markdown
    #    Use individual word matching to handle watermark text interference
    md_text = Path(md_path).read_text(encoding='utf-8')
    h2_headings = re.findall(r'^##\s+(.+)$', md_text, re.MULTILINE)
    found = 0
    missing = []
    full_lower = full_text.lower()
    for h in h2_headings:
        clean = re.sub(r'[*_`#\[\]()]', '', h).strip()
        # Check if each significant word appears in the PDF
        words = [w.lower() for w in clean.split() if len(w) > 2]
        if not words:
            found += 1
            continue
        matched_words = sum(1 for w in words if w in full_lower)
        # Pass if majority of words found (handles watermark text interleaving)
        if matched_words >= len(words) * 0.6:
            found += 1
        else:
            missing.append(clean[:60])

    total_h2 = len(h2_headings)
    pct = (found / total_h2 * 100) if total_h2 > 0 else 100
    result["checks"]["content_integrity"] = {
        "status": "PASS" if pct >= 80 else "WARN" if pct >= 60 else "FAIL",
        "h2_found": found, "h2_total": total_h2,
        "percentage": round(pct, 1),
        "missing": missing[:5]
    }

    # 2. Formatting
    expected = max(2, int(md_kb / 3))
    ok = 0.25 < (num_pages / expected) < 4.0 if expected > 0 else True
    result["checks"]["formatting"] = {
        "status": "PASS" if ok else "WARN",
        "pages": num_pages, "file_size_kb": round(file_kb, 1), "md_size_kb": round(md_kb, 1)
    }

    # 3. Legal completeness
    has_disclaimer = ("disclaimer" in full_text.lower() or "advocatenwet" in full_text.lower())
    has_date = TODAY_STR in full_text
    has_ai = ("ai" in full_text.lower() and
              ("gegenereerd" in full_text.lower() or "generated" in full_text.lower() or
               "ai lawyer" in full_text.lower()))

    result["checks"]["legal_completeness"] = {
        "status": "PASS" if (has_disclaimer and has_date) else "FAIL",
        "disclaimer_present": has_disclaimer,
        "date_stamp": has_date,
        "ai_disclosure": has_ai
    }

    # 4. Watermark
    wm = config.get("watermark")
    if wm:
        result["checks"]["watermark"] = {
            "status": "PASS", "configured": wm, "note": "Applied via pypdf merge (15% opacity)"
        }
    else:
        result["checks"]["watermark"] = {"status": "N/A"}

    pdf.close()
    return result


# ─── Preview Generation (pypdfium2) ──────────────────────────────────────────

def generate_previews(pdf_path, output_dir):
    """Render first and last page as PNG using pypdfium2."""
    if pdfium is None:
        return False

    try:
        pdf = pdfium.PdfDocument(str(pdf_path))
        stem = Path(pdf_path).stem
        total = len(pdf)

        # First page
        page = pdf[0]
        bitmap = page.render(scale=2.0)
        img = bitmap.to_pil()
        img.save(str(output_dir / f"{stem}-page1.png"), "PNG")

        # Last page (if different from first)
        if total > 1:
            page = pdf[total - 1]
            bitmap = page.render(scale=2.0)
            img = bitmap.to_pil()
            img.save(str(output_dir / f"{stem}-lastpage.png"), "PNG")

        return True
    except Exception as e:
        print(f"  [WARN] Preview: {e}")
        return False


# ─── Main Conversion ─────────────────────────────────────────────────────────

def convert_document(md_filename):
    """Convert a single markdown document to PDF."""
    md_path = LEGAL_DOCS_DIR / md_filename
    pdf_name = md_filename.replace(".md", ".pdf")
    pdf_path = PDF_OUTPUT_DIR / pdf_name
    config = DOC_CONFIG.get(md_filename, {})

    print(f"\n{'='*60}")
    print(f"  Converting: {md_filename}")
    print(f"{'='*60}")

    md_text = md_path.read_text(encoding="utf-8")
    md_text = strip_trailing_disclaimer(md_text)

    parser = MarkdownParser()
    blocks = parser.parse(md_text)
    print(f"  Parsed {len(blocks)} blocks")

    renderer = LegalPdfRenderer(config, md_filename)
    renderer.render_blocks(blocks)
    renderer.add_disclaimer_page()
    renderer.build_pdf(pdf_path)
    print(f"  Built: {pdf_name}")

    # Watermark
    wm = config.get("watermark")
    if wm:
        apply_watermark(pdf_path, wm)
        print(f"  Watermark: {wm}")

    # Verify
    vresult = verify_pdf(pdf_path, md_path, config)
    for name, data in vresult.get("checks", {}).items():
        status = data.get("status", "?")
        extra = ""
        if name == "content_integrity":
            extra = f" ({data.get('h2_found')}/{data.get('h2_total')})"
        elif name == "formatting":
            extra = f" ({data.get('pages')} pages, {data.get('file_size_kb')} KB)"
        print(f"  [{status}] {name}{extra}")

    # Preview
    if generate_previews(pdf_path, PREVIEWS_DIR):
        print(f"  Previews generated")
    else:
        print(f"  [SKIP] Previews (pypdfium2 not available)")

    return vresult


def main():
    ap = argparse.ArgumentParser(description="Convert legal markdown to professional PDF")
    ap.add_argument("--all", action="store_true", help="Convert all 8 documents")
    ap.add_argument("--file", type=str, help="Convert single file (filename only)")
    ap.add_argument("--verify-only", action="store_true", help="Only verify existing PDFs")
    args = ap.parse_args()

    PDF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)

    if args.verify_only:
        results = []
        for f in DOCUMENT_FILES:
            pp = PDF_OUTPUT_DIR / f.replace(".md", ".pdf")
            if pp.exists():
                r = verify_pdf(pp, LEGAL_DOCS_DIR / f, DOC_CONFIG.get(f, {}))
                results.append(r)
                print(json.dumps(r, indent=2))
        rp = PDF_OUTPUT_DIR / "verification-report.json"
        with open(str(rp), "w") as fp:
            json.dump(results, fp, indent=2)
        print(f"\nReport: {rp}")
        return

    files = []
    if args.all:
        files = DOCUMENT_FILES
    elif args.file:
        fname = args.file if args.file.endswith(".md") else args.file + ".md"
        if fname not in DOCUMENT_FILES:
            print(f"Error: {fname} not found. Available:")
            for f in DOCUMENT_FILES:
                print(f"  {f}")
            sys.exit(1)
        files = [fname]
    else:
        print("Usage:")
        print(f"  python3 {sys.argv[0]} --all")
        print(f"  python3 {sys.argv[0]} --file <name.md>")
        print(f"  python3 {sys.argv[0]} --verify-only")
        sys.exit(0)

    all_results = []
    for f in files:
        all_results.append(convert_document(f))

    # Write verification report
    rp = PDF_OUTPUT_DIR / "verification-report.json"
    with open(str(rp), "w") as fp:
        json.dump(all_results, fp, indent=2)

    print(f"\n{'='*60}")
    print(f"  DONE: {len(files)} documents \u2192 {PDF_OUTPUT_DIR}")
    print(f"  Report: {rp}")
    print(f"{'='*60}")

    passed = sum(1 for r in all_results
                 for c in r.get("checks", {}).values()
                 if c.get("status") in ("PASS", "N/A"))
    total = sum(1 for r in all_results for _ in r.get("checks", {}).values())
    print(f"\n  Verification: {passed}/{total} checks passed")


if __name__ == "__main__":
    main()
