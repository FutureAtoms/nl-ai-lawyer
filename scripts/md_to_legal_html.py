#!/usr/bin/env python3
"""
Convert Dutch legal markdown documents to professional HTML.

Typography follows Dutch government (Rijksoverheid) style:
- Serif body text (Georgia → Times New Roman fallback)
- Sans-serif headings (Arial/Helvetica)
- A4 print layout with 25mm margins
- Clean bullet/numbered lists, proper spacing
- Watermarks, confidentiality banners, risk badges
- Mandatory disclaimer on final page

Output: standalone HTML files that can be opened in a browser
and saved/printed as PDF via Ctrl+P / Cmd+P.
"""
import sys
import os
import re
import json
import argparse
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LEGAL_DOCS_DIR = BASE_DIR / "assets" / "legal-documents"
OUTPUT_DIR = LEGAL_DOCS_DIR / "pdf"
DISCLAIMER_PATH = BASE_DIR / "assets" / "disclaimers" / "disclaimer-nl.md"

TODAY = date.today().strftime("%d-%m-%Y")
TODAY_LONG = date.today().strftime("%-d %B %Y")  # e.g. "5 March 2026"

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

RISK_COLORS = {
    "CRITICAL": "#C0392B",
    "HIGH": "#E67E22",
    "MEDIUM": "#F39C12",
    "LOW": "#27AE60",
}

# ─── CSS ──────────────────────────────────────────────────────────────────────

def get_css(config):
    """Generate CSS following Rijksoverheid typography standards."""
    watermark = config.get("watermark", "")
    banner = config.get("banner", "")

    watermark_css = ""
    if watermark:
        watermark_css = f"""
        @media print {{
            .page-content::before {{
                content: "{watermark}";
                position: fixed;
                top: 45%;
                left: 50%;
                transform: translate(-50%, -50%) rotate(-45deg);
                font-size: 72pt;
                font-family: Arial, Helvetica, sans-serif;
                font-weight: 700;
                color: rgba(200, 0, 0, 0.07);
                z-index: -1;
                pointer-events: none;
                white-space: nowrap;
            }}
        }}
        @media screen {{
            .page-content::before {{
                content: "{watermark}";
                position: fixed;
                top: 45%;
                left: 50%;
                transform: translate(-50%, -50%) rotate(-45deg);
                font-size: 72pt;
                font-family: Arial, Helvetica, sans-serif;
                font-weight: 700;
                color: rgba(200, 0, 0, 0.07);
                z-index: -1;
                pointer-events: none;
                white-space: nowrap;
            }}
        }}
        """

    banner_css = ""
    if banner:
        banner_css = f"""
        .conf-banner {{
            background-color: #C0392B;
            color: white;
            text-align: center;
            padding: 6px 0;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 9pt;
            font-weight: 700;
            letter-spacing: 0.5px;
            position: running(banner);
        }}
        @page {{
            @top-center {{
                content: element(banner);
            }}
        }}
        """

    return f"""
    /* ─── Rijksoverheid-style Typography ─────────────────────── */
    @page {{
        size: A4;
        margin: 25mm 25mm 20mm 25mm;
        @bottom-center {{
            content: counter(page);
            font-family: Arial, Helvetica, sans-serif;
            font-size: 8pt;
            color: #999;
        }}
    }}

    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}

    html {{
        font-size: 10.5pt;
    }}

    body {{
        font-family: Georgia, "Times New Roman", "Rijksoverheid Serif", serif;
        font-size: 10.5pt;
        line-height: 1.55;
        color: #1a1a1a;
        max-width: 160mm;
        margin: 0 auto;
        padding: 25mm;
        background: #fff;
    }}

    @media print {{
        body {{
            padding: 0;
            max-width: none;
        }}
    }}

    .page-content {{
        position: relative;
    }}

    {watermark_css}
    {banner_css}

    /* ─── Headings (Sans-serif, Rijksoverheid Sans style) ──── */

    h1, h2, h3, h4 {{
        font-family: Arial, Helvetica, "Rijksoverheid Sans", sans-serif;
        color: #1a1a1a;
        page-break-after: avoid;
        orphans: 3;
        widows: 3;
    }}

    h1 {{
        font-size: 16pt;
        font-weight: 700;
        margin-top: 28pt;
        margin-bottom: 10pt;
        padding-bottom: 4pt;
        border-bottom: 2px solid #154273;
        color: #154273;
        letter-spacing: -0.3px;
    }}

    h1:first-of-type {{
        margin-top: 0;
    }}

    h2 {{
        font-size: 13pt;
        font-weight: 700;
        margin-top: 22pt;
        margin-bottom: 8pt;
        color: #154273;
        padding-bottom: 2pt;
        border-bottom: 1px solid #d0d0d0;
    }}

    h3 {{
        font-size: 11pt;
        font-weight: 700;
        margin-top: 16pt;
        margin-bottom: 6pt;
        color: #2c3e50;
    }}

    h4 {{
        font-size: 10.5pt;
        font-weight: 700;
        font-style: italic;
        margin-top: 12pt;
        margin-bottom: 4pt;
        color: #34495e;
    }}

    /* ─── Body Text ────────────────────────────────────────── */

    p {{
        margin-bottom: 8pt;
        text-align: justify;
        hyphens: auto;
        -webkit-hyphens: auto;
        orphans: 2;
        widows: 2;
    }}

    strong {{
        font-weight: 700;
    }}

    em {{
        font-style: italic;
    }}

    a {{
        color: #154273;
        text-decoration: underline;
    }}

    code {{
        font-family: "Courier New", Courier, monospace;
        font-size: 9pt;
        background: #f4f4f4;
        border: 1px solid #e0e0e0;
        border-radius: 2px;
        padding: 1px 4px;
    }}

    /* ─── Lists (proper bullet points & numbering) ─────────── */

    ul, ol {{
        margin: 6pt 0 10pt 0;
        padding-left: 22pt;
    }}

    ul {{
        list-style-type: disc;
    }}

    ul ul {{
        list-style-type: circle;
        margin-top: 3pt;
        margin-bottom: 3pt;
    }}

    ol {{
        list-style-type: decimal;
    }}

    ol ol {{
        list-style-type: lower-alpha;
    }}

    li {{
        margin-bottom: 4pt;
        text-align: justify;
        line-height: 1.5;
    }}

    li > ul, li > ol {{
        margin-top: 3pt;
    }}

    /* ─── Tables ───────────────────────────────────────────── */

    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 10pt 0 14pt 0;
        font-size: 9.5pt;
        line-height: 1.4;
        page-break-inside: auto;
    }}

    thead {{
        display: table-header-group;
    }}

    tr {{
        page-break-inside: avoid;
    }}

    th {{
        background-color: #154273;
        color: #fff;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: 700;
        font-size: 9pt;
        text-align: left;
        padding: 7pt 8pt;
        border: 1px solid #154273;
    }}

    td {{
        padding: 6pt 8pt;
        border: 1px solid #d0d0d0;
        vertical-align: top;
    }}

    tbody tr:nth-child(even) {{
        background-color: #f8f9fa;
    }}

    tbody tr:nth-child(odd) {{
        background-color: #ffffff;
    }}

    /* Bold first column for key-value tables */
    table.kv-table td:first-child {{
        font-weight: 700;
        white-space: nowrap;
        width: 1%;
    }}

    /* ─── Blockquotes ──────────────────────────────────────── */

    blockquote {{
        margin: 10pt 0;
        padding: 10pt 14pt;
        border-left: 3px solid #154273;
        background: #f0f4f8;
        color: #333;
        font-size: 10pt;
        line-height: 1.5;
    }}

    blockquote p {{
        margin-bottom: 4pt;
    }}

    blockquote p:last-child {{
        margin-bottom: 0;
    }}

    /* ─── Code blocks ──────────────────────────────────────── */

    pre {{
        background: #f5f5f5;
        border: 1px solid #ddd;
        border-radius: 2px;
        padding: 10pt 12pt;
        font-family: "Courier New", Courier, monospace;
        font-size: 8.5pt;
        line-height: 1.4;
        overflow-x: auto;
        margin: 8pt 0 12pt 0;
        white-space: pre-wrap;
        word-wrap: break-word;
    }}

    /* ─── Horizontal rules ─────────────────────────────────── */

    hr {{
        border: none;
        border-top: 1px solid #d0d0d0;
        margin: 14pt 0;
    }}

    /* ─── Checklists ───────────────────────────────────────── */

    .checklist {{
        list-style: none;
        padding-left: 0;
        margin: 6pt 0 10pt 0;
    }}

    .checklist li {{
        padding-left: 24pt;
        position: relative;
        margin-bottom: 4pt;
    }}

    .checklist li::before {{
        content: "";
        position: absolute;
        left: 0;
        top: 3pt;
        width: 11pt;
        height: 11pt;
        border: 1.5px solid #555;
        border-radius: 2px;
        background: #fff;
    }}

    .checklist li.checked::before {{
        background: #27AE60;
        border-color: #27AE60;
    }}

    .checklist li.checked::after {{
        content: "\\2713";
        position: absolute;
        left: 2pt;
        top: 1pt;
        color: #fff;
        font-size: 9pt;
        font-weight: 700;
    }}

    /* ─── Risk badges ──────────────────────────────────────── */

    .risk-critical {{ color: #C0392B; font-weight: 700; }}
    .risk-high {{ color: #E67E22; font-weight: 700; }}
    .risk-medium {{ color: #F39C12; font-weight: 700; }}
    .risk-low {{ color: #27AE60; font-weight: 700; }}

    /* ─── Disclaimer section ───────────────────────────────── */

    .disclaimer {{
        page-break-before: always;
        margin-top: 0;
    }}

    .disclaimer h2 {{
        font-size: 13pt;
        color: #154273;
    }}

    .disclaimer p, .disclaimer li {{
        font-size: 8.5pt;
        line-height: 1.45;
        color: #555;
    }}

    .disclaimer strong {{
        color: #333;
    }}

    .footer-meta {{
        margin-top: 16pt;
        padding-top: 8pt;
        border-top: 1px solid #d0d0d0;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 7.5pt;
        color: #999;
        text-align: right;
    }}

    /* ─── Confidentiality banner (screen) ──────────────────── */

    .top-banner {{
        background-color: #C0392B;
        color: white;
        text-align: center;
        padding: 5pt 0;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 8.5pt;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin: -25mm -25mm 14pt -25mm;
        width: calc(100% + 50mm);
    }}

    @media print {{
        .top-banner {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            margin: 0;
            width: 100%;
        }}
    }}

    /* ─── Page break helpers ───────────────────────────────── */

    .page-break {{
        page-break-before: always;
    }}
    """


# ─── HTML Escaping ────────────────────────────────────────────────────────────

def html_escape(text):
    """Escape HTML special characters."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    return text


def format_inline(text):
    """Convert markdown inline formatting to HTML."""
    # Protect inline code spans first
    code_spans = []

    def _save(m):
        idx = len(code_spans)
        code_spans.append(m.group(1))
        return f"\x00CODE{idx}\x00"

    text = re.sub(r'`([^`]+)`', _save, text)

    # HTML-escape
    text = html_escape(text)

    # Bold+italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'(?<![*\w])\*([^*\n]+?)\*(?![*\w])', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

    # Restore code spans
    for i, code in enumerate(code_spans):
        text = text.replace(f"\x00CODE{i}\x00",
                           f'<code>{html_escape(code)}</code>')

    # Risk badges
    for level, color in RISK_COLORS.items():
        text = re.sub(
            rf'\b({level})\b',
            rf'<span class="risk-{level.lower()}">\1</span>',
            text
        )

    return text


# ─── Markdown to HTML Converter ───────────────────────────────────────────────

class MarkdownToHtml:
    """Convert markdown text to HTML body content."""

    def convert(self, text):
        lines = text.split("\n")
        html_parts = []
        i = 0
        n = len(lines)

        while i < n:
            line = lines[i]
            stripped = line.strip()

            # Blank line
            if stripped == "":
                i += 1
                continue

            # Horizontal rule
            if re.match(r'^-{3,}$', stripped) or re.match(r'^\*{3,}$', stripped):
                html_parts.append("<hr>")
                i += 1
                continue

            # Heading
            hm = re.match(r'^(#{1,4})\s+(.*)', line)
            if hm:
                level = len(hm.group(1))
                text = format_inline(hm.group(2).strip())
                html_parts.append(f"<h{level}>{text}</h{level}>")
                i += 1
                continue

            # Fenced code block
            if stripped.startswith("```"):
                lang = stripped[3:].strip()
                code_lines = []
                i += 1
                while i < n and not lines[i].strip().startswith("```"):
                    code_lines.append(html_escape(lines[i]))
                    i += 1
                if i < n:
                    i += 1
                code_text = "\n".join(code_lines)
                html_parts.append(f'<pre><code>{code_text}</code></pre>')
                continue

            # Table
            if "|" in line and i + 1 < n and re.match(r'^\s*\|[\s:|-]+\|\s*$', lines[i + 1]):
                headers = [c.strip() for c in stripped.strip("|").split("|")]
                i += 2
                rows = []
                while i < n and "|" in lines[i] and lines[i].strip():
                    cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                    rows.append(cells)
                    i += 1

                # Detect key-value table (2 columns)
                is_kv = len(headers) == 2
                kv_class = ' class="kv-table"' if is_kv else ''

                table_html = f"<table{kv_class}>\n<thead><tr>"
                for h in headers:
                    table_html += f"<th>{format_inline(h)}</th>"
                table_html += "</tr></thead>\n<tbody>\n"
                for row in rows:
                    table_html += "<tr>"
                    for j, cell in enumerate(row):
                        cell_html = format_inline(cell)
                        if j < len(headers):
                            table_html += f"<td>{cell_html}</td>"
                    # Pad missing cells
                    for _ in range(len(headers) - len(row)):
                        table_html += "<td></td>"
                    table_html += "</tr>\n"
                table_html += "</tbody></table>"
                html_parts.append(table_html)
                continue

            # Checklist
            cm = re.match(r'^\s*[-*]\s+\[([ xX])\]\s+(.*)', line)
            if cm:
                html_parts.append('<ul class="checklist">')
                while i < n:
                    m = re.match(r'^\s*[-*]\s+\[([ xX])\]\s+(.*)', lines[i])
                    if not m:
                        break
                    checked = ' checked' if m.group(1).lower() == 'x' else ''
                    text = format_inline(m.group(2).strip())
                    html_parts.append(f'<li class="{checked.strip()}">{text}</li>')
                    i += 1
                html_parts.append('</ul>')
                continue

            # Blockquote
            if stripped.startswith(">"):
                bq_lines = []
                while i < n and lines[i].strip().startswith(">"):
                    content = re.sub(r'^>\s?', '', lines[i]).strip()
                    bq_lines.append(content)
                    i += 1
                # Continuation lines
                while i < n and lines[i].strip() and not lines[i].strip().startswith(">") \
                        and not re.match(r'^#{1,4}\s', lines[i]) \
                        and not re.match(r'^-{3,}$', lines[i].strip()):
                    bq_lines.append(lines[i].strip())
                    i += 1

                # Split into paragraphs on blank lines within blockquote
                bq_html = "<blockquote>"
                current_para = []
                for bl in bq_lines:
                    if bl == "":
                        if current_para:
                            bq_html += f"<p>{format_inline(' '.join(current_para))}</p>"
                            current_para = []
                    else:
                        current_para.append(bl)
                if current_para:
                    bq_html += f"<p>{format_inline(' '.join(current_para))}</p>"
                bq_html += "</blockquote>"
                html_parts.append(bq_html)
                continue

            # Ordered list
            om = re.match(r'^(\d+)\.\s+(.*)', line)
            if om:
                html_parts.append("<ol>")
                while i < n:
                    m = re.match(r'^(\d+)\.\s+(.*)', lines[i])
                    if not m:
                        break
                    item_text = m.group(2).strip()
                    i += 1
                    # Sub-items
                    sub_items = []
                    while i < n and (lines[i].startswith("   ") or lines[i].startswith("\t")) and lines[i].strip():
                        sub = re.match(r'^\s+[-*+]\s+(.*)', lines[i])
                        sub_letter = re.match(r'^\s+\(([a-z])\)\s*(.*)', lines[i])
                        if sub:
                            sub_items.append(sub.group(1).strip())
                        elif sub_letter:
                            sub_items.append(f"({sub_letter.group(1)}) {sub_letter.group(2).strip()}")
                        else:
                            item_text += " " + lines[i].strip()
                        i += 1

                    li_html = format_inline(item_text)
                    if sub_items:
                        li_html += "\n<ul>"
                        for si in sub_items:
                            li_html += f"\n<li>{format_inline(si)}</li>"
                        li_html += "\n</ul>"
                    html_parts.append(f"<li>{li_html}</li>")
                html_parts.append("</ol>")
                continue

            # Unordered list (including indented)
            um = re.match(r'^(\s*)[-*+]\s+(.*)', line)
            if um and not re.match(r'^\s*[-*]\s+\[([ xX])\]', line):
                html_parts.append("<ul>")
                while i < n:
                    m = re.match(r'^(\s*)[-*+]\s+(.*)', lines[i])
                    if m and not re.match(r'^\s*[-*]\s+\[([ xX])\]', lines[i]):
                        item_text = m.group(2).strip()
                        i += 1
                        # Sub-items (more deeply indented)
                        sub_items = []
                        while i < n and lines[i].strip() and \
                                (lines[i].startswith("   ") or lines[i].startswith("\t")):
                            sub = re.match(r'^\s+[-*+]\s+(.*)', lines[i])
                            sub_letter = re.match(r'^\s+\(([a-z])\)\s*(.*)', lines[i])
                            if sub:
                                sub_items.append(sub.group(1).strip())
                            elif sub_letter:
                                sub_items.append(f"({sub_letter.group(1)}) {sub_letter.group(2).strip()}")
                            else:
                                item_text += " " + lines[i].strip()
                            i += 1

                        li_html = format_inline(item_text)
                        if sub_items:
                            li_html += "\n<ul>"
                            for si in sub_items:
                                li_html += f"\n<li>{format_inline(si)}</li>"
                            li_html += "\n</ul>"
                        html_parts.append(f"<li>{li_html}</li>")
                    else:
                        break
                html_parts.append("</ul>")
                continue

            # Paragraph
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
                if re.match(r'^\s*[-*+]\s+', l) and not para_lines:
                    break
                if re.match(r'^\d+\.\s+', s) and not para_lines:
                    break
                if "|" in l and i + 1 < n and re.match(r'^\s*\|[\s:|-]+\|', lines[i + 1]):
                    break
                para_lines.append(s)
                i += 1
            if para_lines:
                text = format_inline(" ".join(para_lines))
                html_parts.append(f"<p>{text}</p>")
            elif i < n:
                i += 1  # safety: skip unprocessable line

        return "\n".join(html_parts)


# ─── Disclaimer ───────────────────────────────────────────────────────────────

def render_disclaimer():
    """Render the mandatory Dutch disclaimer section."""
    parts = ['<div class="disclaimer">', '<h2>DISCLAIMER</h2>', '<hr>']

    if DISCLAIMER_PATH.exists():
        raw = DISCLAIMER_PATH.read_text(encoding='utf-8')
        raw = raw.replace("[DATUM]", TODAY)
        converter = MarkdownToHtml()
        parts.append(converter.convert(raw))
    else:
        parts.append(
            '<p>Dit document is opgesteld met behulp van AI-ondersteunde analyse en vormt '
            '<strong>geen juridisch advies</strong> in de zin van de Advocatenwet.</p>')

    parts.append(f'''
    <div class="footer-meta">
        FALCON (FutureAtoms AI Legal Counsel Of Netherlands) &nbsp;|&nbsp;
        Datum: {TODAY} &nbsp;|&nbsp;
        Verificatiedatum wetgeving: {TODAY} &nbsp;|&nbsp;
        AI-gegenereerd document
    </div>''')
    parts.append('</div>')
    return "\n".join(parts)


# ─── Strip trailing disclaimer from markdown ──────────────────────────────────

def strip_trailing_disclaimer(text):
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


# ─── Build Full HTML Document ─────────────────────────────────────────────────

def build_html(md_filename):
    """Convert a markdown file to a complete standalone HTML document."""
    md_path = LEGAL_DOCS_DIR / md_filename
    config = DOC_CONFIG.get(md_filename, {})

    md_text = md_path.read_text(encoding="utf-8")
    md_text = strip_trailing_disclaimer(md_text)

    # Extract title from first H1
    title_match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else md_filename.replace(".md", "")
    title_clean = re.sub(r'[*_`]', '', title)

    # Convert body
    converter = MarkdownToHtml()
    body_html = converter.convert(md_text)

    # Disclaimer
    disclaimer_html = render_disclaimer()

    # Banner
    banner_html = ""
    if config.get("banner"):
        banner_html = f'<div class="top-banner">{html_escape(config["banner"])}</div>'

    css = get_css(config)

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html_escape(title_clean)}</title>
    <style>{css}</style>
</head>
<body>
<div class="page-content">
{banner_html}
{body_html}
{disclaimer_html}
</div>
</body>
</html>"""

    return html


# ─── Verification ─────────────────────────────────────────────────────────────

def verify_html(html_path, md_path, config):
    """Basic verification checks on generated HTML."""
    html_text = Path(html_path).read_text(encoding='utf-8')
    md_text = Path(md_path).read_text(encoding='utf-8')

    result = {"file": os.path.basename(html_path), "checks": {}}

    # Strip HTML tags for text comparison
    plain = re.sub(r'<[^>]+>', ' ', html_text)
    plain = re.sub(r'\s+', ' ', plain).lower()

    # 1. Content integrity
    h2_headings = re.findall(r'^##\s+(.+)$', md_text, re.MULTILINE)
    found = 0
    missing = []
    for h in h2_headings:
        clean = re.sub(r'[*_`#\[\]()]', '', h).strip()
        words = [w.lower() for w in clean.split() if len(w) > 2]
        if not words:
            found += 1
            continue
        matched = sum(1 for w in words if w in plain)
        if matched >= len(words) * 0.6:
            found += 1
        else:
            missing.append(clean[:60])

    total_h2 = len(h2_headings)
    pct = (found / total_h2 * 100) if total_h2 > 0 else 100
    result["checks"]["content_integrity"] = {
        "status": "PASS" if pct >= 80 else "WARN",
        "h2_found": found, "h2_total": total_h2,
        "percentage": round(pct, 1),
        "missing": missing[:5]
    }

    # 2. Legal completeness
    has_disclaimer = "disclaimer" in plain or "advocatenwet" in plain
    has_date = TODAY in html_text
    has_ai = "ai" in plain and ("gegenereerd" in plain or "generated" in plain)
    result["checks"]["legal_completeness"] = {
        "status": "PASS" if (has_disclaimer and has_date) else "FAIL",
        "disclaimer_present": has_disclaimer,
        "date_stamp": has_date,
        "ai_disclosure": has_ai
    }

    # 3. Formatting
    file_kb = os.path.getsize(str(html_path)) / 1024
    md_kb = os.path.getsize(str(md_path)) / 1024

    # Check for proper HTML structure
    has_lists = "<ul>" in html_text or "<ol>" in html_text
    has_tables = "<table" in html_text
    md_has_lists = bool(re.search(r'^[-*+]\s+', md_text, re.MULTILINE))
    md_has_tables = bool(re.search(r'^\|', md_text, re.MULTILINE))

    lists_ok = has_lists == md_has_lists
    tables_ok = has_tables == md_has_tables

    result["checks"]["formatting"] = {
        "status": "PASS" if lists_ok and tables_ok else "WARN",
        "file_size_kb": round(file_kb, 1),
        "lists_rendered": has_lists,
        "tables_rendered": has_tables
    }

    # 4. Watermark
    wm = config.get("watermark")
    if wm:
        has_wm = wm in html_text
        result["checks"]["watermark"] = {
            "status": "PASS" if has_wm else "FAIL",
            "configured": wm
        }
    else:
        result["checks"]["watermark"] = {"status": "N/A"}

    return result


# ─── Main ─────────────────────────────────────────────────────────────────────

def convert_document(md_filename):
    html_name = md_filename.replace(".md", ".html")
    html_path = OUTPUT_DIR / html_name
    config = DOC_CONFIG.get(md_filename, {})

    print(f"\n{'='*60}")
    print(f"  Converting: {md_filename}")
    print(f"{'='*60}")

    html = build_html(md_filename)
    html_path.write_text(html, encoding='utf-8')

    size_kb = os.path.getsize(str(html_path)) / 1024
    print(f"  Output: {html_name} ({size_kb:.1f} KB)")

    if config.get("watermark"):
        print(f"  Watermark: {config['watermark']}")
    if config.get("banner"):
        print(f"  Banner: {config['banner']}")

    # Verify
    vresult = verify_html(html_path, LEGAL_DOCS_DIR / md_filename, config)
    for name, data in vresult.get("checks", {}).items():
        status = data.get("status", "?")
        extra = ""
        if name == "content_integrity":
            extra = f" ({data.get('h2_found')}/{data.get('h2_total')})"
        print(f"  [{status}] {name}{extra}")

    return vresult


def main():
    ap = argparse.ArgumentParser(description="Convert legal markdown to Dutch government-style HTML")
    ap.add_argument("--all", action="store_true", help="Convert all 8 documents")
    ap.add_argument("--file", type=str, help="Convert single file")
    args = ap.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    files = []
    if args.all:
        files = DOCUMENT_FILES
    elif args.file:
        fname = args.file if args.file.endswith(".md") else args.file + ".md"
        if fname not in DOCUMENT_FILES:
            print(f"Error: {fname} not found")
            sys.exit(1)
        files = [fname]
    else:
        print("Usage:")
        print(f"  python3 {sys.argv[0]} --all")
        print(f"  python3 {sys.argv[0]} --file <name.md>")
        sys.exit(0)

    all_results = []
    for f in files:
        all_results.append(convert_document(f))

    rp = OUTPUT_DIR / "verification-report.json"
    with open(str(rp), "w") as fp:
        json.dump(all_results, fp, indent=2)

    print(f"\n{'='*60}")
    print(f"  DONE: {len(files)} HTML documents")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Report: {rp}")
    print(f"{'='*60}")

    passed = sum(1 for r in all_results
                 for c in r.get("checks", {}).values()
                 if c.get("status") in ("PASS", "N/A"))
    total = sum(1 for r in all_results for _ in r.get("checks", {}).values())
    print(f"\n  Verification: {passed}/{total} checks passed")
    print(f"\n  To save as PDF: open each .html in a browser, then Cmd+P / Ctrl+P → Save as PDF")


if __name__ == "__main__":
    main()
