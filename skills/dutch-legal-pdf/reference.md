# PDF Processing Advanced Reference

Advanced PDF processing features, JavaScript libraries, and detailed examples beyond the main skill instructions.

## Table of Contents

1. [pypdfium2 Library](#pypdfium2-library)
2. [JavaScript Libraries (pdf-lib, pdfjs-dist)](#javascript-libraries)
3. [Advanced Command-Line Operations](#advanced-command-line-operations)
4. [Advanced Python Techniques](#advanced-python-techniques)
5. [Complex Legal Workflows](#complex-legal-workflows)
6. [Performance Optimization](#performance-optimization)
7. [Troubleshooting](#troubleshooting)

---

## pypdfium2 Library (Apache/BSD License)

Fast PDF rendering and image generation — excellent for converting legal documents to images for review or OCR.

### Render PDF to Images
```python
import pypdfium2 as pdfium
from PIL import Image

pdf = pdfium.PdfDocument("vonnis.pdf")

# High-resolution render for legal review
page = pdf[0]
bitmap = page.render(scale=3.0, rotation=0)
img = bitmap.to_pil()
img.save("pagina_1.png", "PNG")

# Batch render all pages
for i, page in enumerate(pdf):
    bitmap = page.render(scale=2.0)
    img = bitmap.to_pil()
    img.save(f"pagina_{i+1}.jpg", "JPEG", quality=90)
```

### Extract Text
```python
import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("contract.pdf")
for i, page in enumerate(pdf):
    text = page.get_text()
    print(f"Pagina {i+1}: {len(text)} tekens")
```

---

## JavaScript Libraries

### pdf-lib (MIT License)

Works in any JavaScript environment for PDF creation and modification.

#### Load and Modify Existing PDF
```javascript
import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

async function addPageToContract() {
    const existingPdfBytes = fs.readFileSync('contract.pdf');
    const pdfDoc = await PDFDocument.load(existingPdfBytes);

    const newPage = pdfDoc.addPage([595, 842]); // A4
    newPage.drawText('Bijlage A - Aanvullende Voorwaarden', {
        x: 50, y: 792, size: 16
    });

    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync('contract-met-bijlage.pdf', pdfBytes);
}
```

#### Create PDF from Scratch
```javascript
import { PDFDocument, rgb, StandardFonts } from 'pdf-lib';
import fs from 'fs';

async function createLegalDocument() {
    const pdfDoc = await PDFDocument.create();
    const helvetica = await pdfDoc.embedFont(StandardFonts.Helvetica);
    const helveticaBold = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

    const page = pdfDoc.addPage([595, 842]); // A4
    const { width, height } = page.getSize();

    // Title
    page.drawText('GEHEIMHOUDINGSOVEREENKOMST', {
        x: 50, y: height - 60,
        size: 18, font: helveticaBold,
        color: rgb(0.17, 0.24, 0.31)
    });

    // Horizontal rule
    page.drawLine({
        start: { x: 50, y: height - 75 },
        end: { x: width - 50, y: height - 75 },
        thickness: 1, color: rgb(0.17, 0.24, 0.31)
    });

    const pdfBytes = await pdfDoc.save();
    fs.writeFileSync('nda.pdf', pdfBytes);
}
```

#### Merge and Split
```javascript
import { PDFDocument } from 'pdf-lib';
import fs from 'fs';

async function mergeLegalDossier() {
    const merged = await PDFDocument.create();

    const files = ['hoofdovereenkomst.pdf', 'bijlage-1.pdf', 'bijlage-2.pdf'];
    for (const file of files) {
        const pdf = await PDFDocument.load(fs.readFileSync(file));
        const pages = await merged.copyPages(pdf, pdf.getPageIndices());
        pages.forEach(page => merged.addPage(page));
    }

    fs.writeFileSync('compleet-dossier.pdf', await merged.save());
}
```

### pdfjs-dist (Apache License)

Mozilla's library for rendering and text extraction in browser environments.

```javascript
import * as pdfjsLib from 'pdfjs-dist';

async function extractText() {
    const pdf = await pdfjsLib.getDocument('uitspraak.pdf').promise;
    let fullText = '';

    for (let i = 1; i <= pdf.numPages; i++) {
        const page = await pdf.getPage(i);
        const content = await page.getTextContent();
        fullText += content.items.map(item => item.str).join(' ') + '\n';
    }
    return fullText;
}
```

---

## Advanced Command-Line Operations

### poppler-utils

```bash
# Extract text with bounding box coordinates (for structured extraction)
pdftotext -bbox-layout document.pdf output.xml

# High-resolution image conversion
pdftoppm -png -r 300 vonnis.pdf vonnis_pagina

# Extract embedded images
pdfimages -j -p bewijsstuk.pdf bewijs_images

# List image info without extracting
pdfimages -list document.pdf
```

### qpdf Advanced

```bash
# Split into groups of pages
qpdf --split-pages=3 groot-dossier.pdf deel_%02d.pdf

# Complex page ranges from multiple sources
qpdf --empty --pages contract.pdf 1-3 bijlage.pdf 5-7 -- selectie.pdf

# Linearize for web streaming
qpdf --linearize dossier.pdf web-optimized.pdf

# Repair corrupted PDF
qpdf --check beschadigd.pdf
qpdf --fix-qdf beschadigd.pdf gerepareerd.pdf

# Encryption with specific permissions
qpdf --encrypt lezer_pw eigenaar_pw 256 \
  --print=none --modify=none -- \
  vertrouwelijk.pdf beschermd.pdf
```

---

## Advanced Python Techniques

### pdfplumber — Coordinate-Based Extraction

```python
import pdfplumber

with pdfplumber.open("contract.pdf") as pdf:
    page = pdf.pages[0]

    # Character-level extraction with coordinates
    chars = page.chars
    for char in chars[:20]:
        print(f"'{char['text']}' at ({char['x0']:.1f}, {char['y0']:.1f})")

    # Extract text from specific region (e.g., signature block)
    bbox_text = page.within_bbox((50, 700, 400, 780)).extract_text()

    # Advanced table settings for complex layouts
    table_settings = {
        "vertical_strategy": "lines",
        "horizontal_strategy": "lines",
        "snap_tolerance": 3,
        "intersection_tolerance": 15
    }
    tables = page.extract_tables(table_settings)
```

### reportlab — Professional Tables

```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

data = [
    ['Artikel', 'Bepaling', 'Risico'],
    ['Art. 3.1', 'Geheimhouding 5 jaar', 'Laag'],
    ['Art. 7.1', 'Boete EUR 50.000', 'Gemiddeld'],
    ['Art. 8.2', 'Forum Rotterdam', 'Laag'],
]

doc = SimpleDocTemplate("clausetabel.pdf", pagesize=A4)
styles = getSampleStyleSheet()

table = Table(data, colWidths=[3*cm, 8*cm, 3*cm])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')]),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
]))

doc.build([table])
```

---

## Complex Legal Workflows

### Batch Process Legal Documents

```python
import os
import glob
from pypdf import PdfReader, PdfWriter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def batch_merge_dossier(input_dir, output_file):
    """Merge all PDFs in a directory into a single dossier."""
    pdf_files = sorted(glob.glob(os.path.join(input_dir, "*.pdf")))
    writer = PdfWriter()

    for pdf_file in pdf_files:
        try:
            reader = PdfReader(pdf_file)
            for page in reader.pages:
                writer.add_page(page)
            logger.info(f"Toegevoegd: {os.path.basename(pdf_file)}")
        except Exception as e:
            logger.error(f"Fout bij verwerking {pdf_file}: {e}")
            continue

    with open(output_file, "wb") as f:
        writer.write(f)
    logger.info(f"Dossier opgeslagen: {output_file}")
```

### Extract Figures and Evidence from PDFs

```bash
# Method 1: pdfimages (fastest, original quality)
pdfimages -all bewijsstuk.pdf bewijs/img

# Method 2: pypdfium2 for page renders
```

```python
import pypdfium2 as pdfium

def extract_page_images(pdf_path, output_dir, scale=3.0):
    """Render each page as high-res image for evidence review."""
    os.makedirs(output_dir, exist_ok=True)
    pdf = pdfium.PdfDocument(pdf_path)
    for i, page in enumerate(pdf):
        bitmap = page.render(scale=scale)
        img = bitmap.to_pil()
        img.save(os.path.join(output_dir, f"pagina_{i+1}.png"), "PNG")
```

### Crop Specific Regions

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("vonnis.pdf")
writer = PdfWriter()

page = reader.pages[0]
# Crop to just the dictum area (in points: 1pt = 1/72 inch)
page.mediabox.left = 50
page.mediabox.bottom = 50
page.mediabox.right = 550
page.mediabox.top = 400

writer.add_page(page)
with open("dictum-uitsnede.pdf", "wb") as f:
    writer.write(f)
```

---

## Performance Optimization

1. **Large dossiers**: Use `qpdf --split-pages` for splitting, process pages individually
2. **Text extraction**: `pdftotext` (CLI) is fastest for plain text; pdfplumber for structured data
3. **Image extraction**: `pdfimages` is much faster than page rendering
4. **Memory management**: Process large PDFs in chunks

```python
def process_large_pdf(pdf_path, chunk_size=10):
    reader = PdfReader(pdf_path)
    total = len(reader.pages)
    for start in range(0, total, chunk_size):
        end = min(start + chunk_size, total)
        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])
        with open(f"deel_{start//chunk_size + 1}.pdf", "wb") as f:
            writer.write(f)
```

---

## Troubleshooting

### Encrypted PDFs
```python
from pypdf import PdfReader
reader = PdfReader("versleuteld.pdf")
if reader.is_encrypted:
    reader.decrypt("wachtwoord")
```

### Corrupted PDFs
```bash
qpdf --check beschadigd.pdf
qpdf --replace-input beschadigd.pdf
```

### Text Extraction Returns Empty
```python
# Likely a scanned PDF — fall back to OCR
import pytesseract
from pdf2image import convert_from_path

images = convert_from_path('scan.pdf')
text = ""
for img in images:
    text += pytesseract.image_to_string(img, lang='nld')
```

## License Information

| Library | License |
|---|---|
| pypdf | BSD |
| pdfplumber | MIT |
| pypdfium2 | Apache/BSD |
| reportlab | BSD |
| poppler-utils | GPL-2 |
| qpdf | Apache |
| pdf-lib | MIT |
| pdfjs-dist | Apache |
