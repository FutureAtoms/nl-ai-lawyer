# Dutch Legal PDF Form Filling

Complete guide for filling PDF forms commonly used in Dutch legal practice: KVK forms, court filings, IND applications, notarial documents, and government submissions.

## Decision Tree

Complete these steps in order. Do not skip ahead to writing code.

**Step 1**: Determine if the PDF has fillable form fields:
```bash
python scripts/check_fillable_fields.py <file.pdf>
```

- **Has fillable fields** → go to "Fillable Fields" section
- **No fillable fields** (scanned/image-based) → go to "Non-Fillable Fields" section

---

## Fillable Fields

If the PDF has native form fields (common for official KVK, Belastingdienst, and IND forms):

### 1. Extract Field Information

```bash
python scripts/extract_form_field_info.py <input.pdf> <field_info.json>
```

This creates JSON with field details:
```json
[
  {
    "field_id": "unique_field_name",
    "page": 1,
    "rect": [left, bottom, right, top],
    "type": "text"
  },
  {
    "field_id": "checkbox_field",
    "page": 1,
    "type": "checkbox",
    "checked_value": "/On",
    "unchecked_value": "/Off"
  },
  {
    "field_id": "radio_group",
    "page": 1,
    "type": "radio_group",
    "radio_options": [
      {"value": "/Option1", "rect": [...]},
      {"value": "/Option2", "rect": [...]}
    ]
  },
  {
    "field_id": "dropdown",
    "page": 1,
    "type": "choice",
    "choice_options": [
      {"value": "NL", "text": "Nederland"},
      {"value": "BE", "text": "Belgie"}
    ]
  }
]
```

### 2. Convert to Images for Visual Reference

```bash
python scripts/convert_pdf_to_images.py <file.pdf> <output_directory>
```

Examine the images to understand what each field is for. Match field IDs from the JSON to visible form labels. Convert bounding box PDF coordinates to image coordinates for verification.

### 3. Create Field Values

Create `field_values.json`:
```json
[
  {
    "field_id": "bedrijfsnaam",
    "description": "Company name (handelsnaam)",
    "page": 1,
    "value": "TechCorp B.V."
  },
  {
    "field_id": "kvk_nummer",
    "description": "KVK registration number",
    "page": 1,
    "value": "12345678"
  },
  {
    "field_id": "rechtsvorm_bv",
    "description": "Legal form: BV checkbox",
    "page": 1,
    "value": "/On"
  }
]
```

### 4. Fill the Form

```bash
python scripts/fill_fillable_fields.py <input.pdf> <field_values.json> <output.pdf>
```

The script validates field IDs and values. Fix any reported errors and retry.

---

## Non-Fillable Fields

For scanned forms or PDFs without native form fields (common for older court forms, notarial templates). Text annotations are placed at calculated coordinates.

### Approach A: Structure-Based (Preferred)

Use when the PDF has selectable text (not purely image-based).

#### A.1: Extract Structure

```bash
python scripts/extract_form_structure.py <input.pdf> form_structure.json
```

This extracts:
- **labels**: Text elements with exact coordinates (x0, top, x1, bottom in PDF points)
- **lines**: Horizontal lines defining row boundaries
- **checkboxes**: Small square rectangles (with center coordinates)
- **row_boundaries**: Row positions from horizontal lines

#### A.2: Analyze and Map Fields

Read `form_structure.json`. Identify:
1. **Label groups**: Adjacent text forming one label (e.g., "Naam" + "bedrijf")
2. **Row structure**: Labels with similar `top` values share a row
3. **Entry positions**: Entry areas start after label ends (x0 = label.x1 + gap)
4. **Checkboxes**: Use detected coordinates directly

Coordinate system: PDF coordinates where y=0 is at TOP of page, y increases downward.

#### A.3: Create fields.json

```json
{
  "pages": [
    {"page_number": 1, "pdf_width": 595, "pdf_height": 842}
  ],
  "form_fields": [
    {
      "page_number": 1,
      "description": "Company name entry",
      "field_label": "Naam onderneming",
      "label_bounding_box": [43, 63, 130, 73],
      "entry_bounding_box": [135, 63, 400, 79],
      "entry_text": {"text": "TechCorp B.V.", "font_size": 10}
    },
    {
      "page_number": 1,
      "description": "BV checkbox",
      "field_label": "BV",
      "label_bounding_box": [260, 200, 275, 210],
      "entry_bounding_box": [285, 197, 292, 205],
      "entry_text": {"text": "X"}
    }
  ]
}
```

Use `pdf_width`/`pdf_height` with coordinates from `form_structure.json`.

### Approach B: Visual Estimation (Fallback)

Use when the PDF is scanned/image-based and structure extraction finds no usable text.

#### B.1: Convert to Images

```bash
python scripts/convert_pdf_to_images.py <input.pdf> <images_dir/>
```

#### B.2: Identify Fields

Examine page images. Note approximate pixel coordinates for each form field.

#### B.3: Zoom Refinement

For each field, crop a region to refine coordinates:

```bash
magick <page_image> -crop <width>x<height>+<x>+<y> +repage <crop_output.png>
```

Examine the crop, determine precise coordinates, then convert back to full image coordinates:
- full_x = crop_x + crop_offset_x
- full_y = crop_y + crop_offset_y

#### B.4: Create fields.json

Use `image_width`/`image_height` (signals image coordinates):
```json
{
  "pages": [
    {"page_number": 1, "image_width": 1700, "image_height": 2200}
  ],
  "form_fields": [...]
}
```

### Hybrid Approach

When structure extraction works for most fields but misses some:

1. Use Approach A for detected fields (PDF coordinates)
2. Use Approach B zoom refinement for missed fields (image coordinates)
3. Convert image coordinates to PDF coordinates:
   - pdf_x = image_x * (pdf_width / image_width)
   - pdf_y = image_y * (pdf_height / image_height)
4. Use a single coordinate system in fields.json

---

## Validation and Filling

### Validate Before Filling

```bash
python scripts/check_bounding_boxes.py fields.json
```

Checks for:
- Intersecting bounding boxes (would cause overlapping text)
- Entry boxes too small for the specified font size

Fix errors before proceeding.

### Fill the Form

```bash
python scripts/fill_pdf_form_with_annotations.py <input.pdf> fields.json <output.pdf>
```

The script auto-detects the coordinate system and handles conversion.

### Verify Output

```bash
python scripts/convert_pdf_to_images.py <output.pdf> <verify_images/>
```

If text is mispositioned:
- **Approach A**: Verify PDF coordinates match `form_structure.json`
- **Approach B**: Verify image dimensions and pixel coordinates
- **Hybrid**: Check coordinate conversions

---

## Common Dutch Legal Forms

### KVK (Kamer van Koophandel)
- BV registration (inschrijving)
- Trade name changes (handelsnaamwijziging)
- Director changes (bestuurswisseling)
- Address changes (adreswijziging)

### Court Forms (Rechtspraak)
- Verzoekschrift (petition)
- Dagvaarding attachments
- Proceskostenstaat (cost statement)

### IND (Immigration)
- MVV application
- Verblijfsvergunning (residence permit)
- Kennismigrant (knowledge migrant) forms

### Belastingdienst (Tax Authority)
- Voorlopige aanslag (provisional assessment)
- Bezwaarschrift (objection) forms
- BTW aangifte (VAT return)

### Tips for Dutch Forms
- KVK numbers are always 8 digits
- BSN (Burgerservicenummer) is 9 digits
- Dates in DD-MM-YYYY format
- Phone numbers: +31 (0)XX XXXXXXX
- Postal codes: 4 digits + 2 letters (e.g., 1234 AB)
