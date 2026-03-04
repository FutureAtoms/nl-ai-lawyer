---
name: dutch-legal-pdf
description: >
  Create, manipulate, fill, merge, split, and process PDF documents for Dutch legal practice. Use this skill whenever the user wants to generate a legal PDF (contract, NDA, memorandum, dagvaarding, legal opinion), extract text/tables from legal PDFs, fill Dutch legal forms (KVK forms, court filings, notarial deeds), combine or split legal documents, add watermarks or confidentiality stamps, OCR scanned legal documents, or convert legal analysis into professional PDF output. Triggers on any mention of .pdf files in a Dutch legal context, requests to "generate a document", "create a contract PDF", "fill out a form", "make this into a PDF", or any legal document production task. Also use when the user asks to extract clauses, tables, or structured data from existing legal PDFs.
---

# Dutch Legal PDF Processing

Generate, manipulate, and process PDF documents for Netherlands legal practice. This skill combines robust PDF tooling with Dutch legal formatting standards, mandatory disclaimers, and integration with the Netherlands AI Lawyer system.

## When You Need More Detail

- **Advanced PDF techniques** (pypdfium2, pdf-lib, complex operations): Read `reference.md`
- **Filling PDF forms** (KVK, court filings, government forms): Read `forms.md`
- **Dutch legal document types and formatting**: Read `dutch-legal-docs.md`

## Quick Decision Tree

```
User wants to...
├── CREATE a new legal PDF from scratch
│   → Use reportlab (Python) — see "Creating Legal PDFs" below
│   → Read dutch-legal-docs.md for document type templates
│
├── FILL an existing PDF form (KVK, court, government)
│   → Read forms.md and follow its step-by-step instructions
│
├── EXTRACT text/tables from a legal PDF
│   → Use pdfplumber for tables, pypdf for text
│
├── MERGE multiple legal documents
│   → Use pypdf or qpdf
│
├── SPLIT a legal document
│   → Use pypdf or qpdf
│
├── OCR a scanned legal document
│   → Use pytesseract + pdf2image
│
├── ADD watermark/confidentiality stamp
│   → Use pypdf page merging
│
└── CONVERT legal analysis to PDF
    → Use reportlab with legal templates below
```

## Ethical Requirements

Every legal PDF produced by this system must include:

1. **Disclaimer** — append the appropriate disclaimer from `assets/disclaimers/` (Dutch: `disclaimer-nl.md`, English: `disclaimer-en.md`). The disclaimer goes on the final page.
2. **Source citations** — every legal statement must reference its source (article number, ECLI, BWB-ID).
3. **Date stamp** — include the date of generation and the date of last legislation verification.
4. **AI disclosure** — clearly state the document was generated with AI assistance.

These are non-negotiable. A legal PDF without a disclaimer is incomplete.

## Python Libraries

### pypdf — Merge, Split, Metadata, Rotate

```python
from pypdf import PdfReader, PdfWriter

# Read and extract text
reader = PdfReader("contract.pdf")
for page in reader.pages:
    text = page.extract_text()

# Merge legal documents (e.g., contract + annexes)
writer = PdfWriter()
for pdf_file in ["hoofdovereenkomst.pdf", "bijlage-1.pdf", "bijlage-2.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)
with open("compleet-dossier.pdf", "wb") as f:
    writer.write(f)

# Split: extract specific pages
reader = PdfReader("vonnis.pdf")
writer = PdfWriter()
writer.add_page(reader.pages[0])  # Just the first page (dictum)
with open("dictum.pdf", "wb") as f:
    writer.write(f)

# Rotate
page = reader.pages[0]
page.rotate(90)
```

### pdfplumber — Extract Text and Tables from Legal Documents

Particularly useful for extracting clause tables, fee schedules, and structured data from contracts or court rulings.

```python
import pdfplumber

with pdfplumber.open("jaarrekening.pdf") as pdf:
    for page in pdf.pages:
        # Extract text preserving layout
        text = page.extract_text()

        # Extract tables (fee schedules, financial statements)
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)
```

#### Extract Tables to Excel

```python
import pdfplumber
import pandas as pd

with pdfplumber.open("financieel-overzicht.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)
    if all_tables:
        combined = pd.concat(all_tables, ignore_index=True)
        combined.to_excel("extracted_tables.xlsx", index=False)
```

### reportlab — Create Professional Legal PDFs

This is the primary tool for generating legal documents from scratch.

#### Legal Document with Dutch Formatting

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether
)
from datetime import date

def create_legal_document(filename, title, content_blocks):
    """Create a professional Dutch legal PDF."""
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=2.5*cm,
        rightMargin=2.5*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm
    )

    styles = getSampleStyleSheet()

    # Dutch legal document styles
    styles.add(ParagraphStyle(
        'LegalTitle',
        parent=styles['Title'],
        fontSize=16,
        spaceAfter=20,
        alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        'LegalHeading',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=16,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'LegalBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        'LegalDisclaimer',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        textColor=colors.grey,
        alignment=TA_JUSTIFY,
        spaceBefore=20
    ))
    styles.add(ParagraphStyle(
        'LegalFooter',
        parent=styles['Normal'],
        fontSize=8,
        alignment=TA_RIGHT,
        textColor=colors.grey
    ))

    story = []

    # Title
    story.append(Paragraph(title, styles['LegalTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 12))

    # Content blocks
    for block in content_blocks:
        if block['type'] == 'heading':
            story.append(Paragraph(block['text'], styles['LegalHeading']))
        elif block['type'] == 'body':
            story.append(Paragraph(block['text'], styles['LegalBody']))
        elif block['type'] == 'table':
            t = Table(block['data'], colWidths=block.get('colWidths'))
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
            ]))
            story.append(t)
            story.append(Spacer(1, 12))
        elif block['type'] == 'pagebreak':
            story.append(PageBreak())

    # Disclaimer (always last page)
    story.append(PageBreak())
    story.append(Paragraph("DISCLAIMER", styles['LegalHeading']))
    story.append(Paragraph(
        "Dit document is opgesteld met behulp van AI-ondersteunde analyse en vormt "
        "<b>geen juridisch advies</b> in de zin van de Advocatenwet. De informatie is "
        "uitsluitend informatief. Raadpleeg altijd een gekwalificeerde advocaat "
        "(ingeschreven bij de Nederlandse Orde van Advocaten) voordat u juridische "
        "beslissingen neemt. Aan dit document kunnen geen rechten worden ontleend.",
        styles['LegalDisclaimer']
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        f"Gegenereerd door Netherlands AI Lawyer System | "
        f"Datum: {date.today().strftime('%d-%m-%Y')} | "
        f"Verificatiedatum wetgeving: {date.today().strftime('%d-%m-%Y')}",
        styles['LegalFooter']
    ))

    doc.build(story)
    return filename
```

#### Subscripts and Superscripts

Never use Unicode subscript/superscript characters in ReportLab PDFs — they render as black boxes. Use XML markup tags instead:

```python
from reportlab.platypus import Paragraph
styles = getSampleStyleSheet()

# Subscripts: <sub> tag
chemical = Paragraph("H<sub>2</sub>O", styles['Normal'])

# Superscripts: <super> tag
squared = Paragraph("x<super>2</super>", styles['Normal'])
```

## Command-Line Tools

### pdftotext (poppler-utils)
```bash
# Extract text preserving layout
pdftotext -layout vonnis.pdf vonnis.txt

# Extract specific pages
pdftotext -f 1 -l 5 contract.pdf first-five-pages.txt
```

### qpdf
```bash
# Merge legal documents with annexes
qpdf --empty --pages hoofdovereenkomst.pdf bijlage-1.pdf bijlage-2.pdf -- dossier.pdf

# Split: extract pages 1-5
qpdf contract.pdf --pages . 1-5 -- samenvatting.pdf

# Decrypt password-protected document
qpdf --password=geheim --decrypt versleuteld.pdf ontsleuteld.pdf

# Encrypt with permissions (no printing, no copying)
qpdf --encrypt user_pw owner_pw 256 --print=none --modify=none -- input.pdf beschermd.pdf
```

## Common Legal Tasks

### OCR Scanned Legal Documents
```python
import pytesseract
from pdf2image import convert_from_path

# Convert scanned PDF to searchable text
images = convert_from_path('gescand-vonnis.pdf')
text = ""
for i, image in enumerate(images):
    # Use Dutch language model for better accuracy
    text += f"--- Pagina {i+1} ---\n"
    text += pytesseract.image_to_string(image, lang='nld')
    text += "\n\n"
```

For Dutch legal documents, install the Dutch Tesseract language pack (`nld`) for significantly better OCR accuracy on Dutch text.

### Add Confidentiality Watermark
```python
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import io

def create_confidentiality_watermark():
    """Create a VERTROUWELIJK (CONFIDENTIAL) watermark."""
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.saveState()
    c.translate(A4[0]/2, A4[1]/2)
    c.rotate(45)
    c.setFont("Helvetica-Bold", 60)
    c.setFillColor(colors.Color(1, 0, 0, alpha=0.15))
    c.drawCentredString(0, 0, "VERTROUWELIJK")
    c.restoreState()
    c.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

def apply_watermark(input_pdf, output_pdf):
    watermark = create_confidentiality_watermark()
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark)
        writer.add_page(page)
    with open(output_pdf, "wb") as f:
        writer.write(f)
```

### Password Protection for Legal Documents
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("vertrouwelijk-advies.pdf")
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

# Encrypt: user password to open, owner password for full access
writer.encrypt("lezer-wachtwoord", "eigenaar-wachtwoord")
with open("beschermd-advies.pdf", "wb") as f:
    writer.write(f)
```

### Extract Images from Legal Documents
```bash
# Using pdfimages (poppler-utils)
pdfimages -j bewijsstuk.pdf images/bewijs
# Extracts as bewijs-000.jpg, bewijs-001.jpg, etc.
```

## Integration with Netherlands AI Lawyer System

When generating legal PDFs, leverage the existing legal domain skills:

| Document Type | Template Source | Legal Skill |
|---|---|---|
| Contract Review Report | `assets/templates/contract-review-report.md` | `dutch-contract-review` |
| Legal Memorandum | `assets/templates/legal-memorandum.md` | Multiple (domain-specific) |
| NDA / Geheimhoudingsovereenkomst | `assets/templates/nda-template-nl.md` | `nda-triage-nl` |
| Verwerkersovereenkomst (DPA) | `assets/templates/verwerkersovereenkomst.md` | `dutch-privacy-gdpr` |
| Arbeidsovereenkomst | `assets/templates/arbeidsovereenkomst.md` | `dutch-employment-law` |

Use the MCP tools to pull live legal data into documents:
- **dutch-legal-mcp**: `legislation_get_article` for exact statutory text, `caselaw_search_rechtspraak` for case law citations
- **cerebra-legal-mcp**: `legal_think` for structured legal reasoning in document analysis sections
- **opentk**: Parliamentary data for legislative context

## Dutch Legal Formatting Standards

### Paper and Margins
- **Paper size**: A4 (210 x 297 mm) — standard for all Dutch legal documents
- **Margins**: 2.5 cm all sides (minimum for court filings)
- **Font**: proportional serif or sans-serif, 10-12pt body text
- **Line spacing**: 1.2-1.5 for body text

### Numbering Convention
Dutch legal documents use hierarchical numbering:
- Articles: `Artikel 1`, `Artikel 2`
- Sub-articles: `1.1`, `1.2`, `1.3`
- Sub-sub: `1.1.1` or `a.`, `b.`, `c.`

### Mandatory Elements for Court Filings
- Party identification with KVK numbers
- Procureur/advocaat details
- Court identification
- Case number (zaaknummer/rolnummer)
- Date of filing

### Date Format
Always use Dutch format: `4 maart 2026` or `04-03-2026` (DD-MM-YYYY), never MM-DD-YYYY.

## Quick Reference

| Task | Best Tool | Notes |
|---|---|---|
| Create legal PDF | reportlab | Use A4, Dutch formatting |
| Merge documents + annexes | pypdf or qpdf | Maintain page numbering |
| Extract text from rulings | pdfplumber | Preserves layout |
| Extract tables | pdfplumber | Fee schedules, financial data |
| Fill government forms | See forms.md | KVK, court, IND forms |
| OCR scanned documents | pytesseract (lang=nld) | Use Dutch language model |
| Add VERTROUWELIJK stamp | pypdf merge | See watermark example above |
| Password protect | pypdf encrypt | Or qpdf for CLI |
| Extract images/evidence | pdfimages | poppler-utils |
| Convert to searchable PDF | pytesseract + reportlab | OCR then rebuild |

## Next Steps

- For advanced PDF techniques (pypdfium2, pdf-lib, batch processing): Read `reference.md`
- For filling PDF forms (government, court, KVK): Read `forms.md`
- For Dutch legal document types with full templates: Read `dutch-legal-docs.md`
