#!/usr/bin/env python3
"""Fill non-fillable PDF forms by adding text annotations at specified coordinates."""
import sys
import json

def fill_with_annotations(input_pdf, fields_json, output_pdf):
    try:
        from pypdf import PdfReader, PdfWriter
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4
        import io
    except ImportError as e:
        print(f"Error: Missing dependency. Run: pip install pypdf reportlab")
        print(f"Details: {e}")
        sys.exit(1)

    with open(fields_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Determine coordinate system
    pages_info = {p['page_number']: p for p in data.get('pages', [])}
    form_fields = data.get('form_fields', [])

    # Group fields by page
    fields_by_page = {}
    for field in form_fields:
        pg = field.get('page_number', 1)
        fields_by_page.setdefault(pg, []).append(field)

    for page_num, page in enumerate(reader.pages, 1):
        page_fields = fields_by_page.get(page_num, [])

        if page_fields:
            # Get page dimensions
            page_width = float(page.mediabox.width)
            page_height = float(page.mediabox.height)

            page_info = pages_info.get(page_num, {})

            # Determine if we need coordinate conversion
            if 'image_width' in page_info:
                # Image coordinates -> PDF coordinates
                scale_x = page_width / page_info['image_width']
                scale_y = page_height / page_info['image_height']
            else:
                scale_x = 1.0
                scale_y = 1.0

            # Create overlay with text
            packet = io.BytesIO()
            c = canvas.Canvas(packet, pagesize=(page_width, page_height))

            for field in page_fields:
                entry_box = field.get('entry_bounding_box', [0, 0, 100, 20])
                entry_text = field.get('entry_text', {})
                text = entry_text.get('text', '')
                font_size = entry_text.get('font_size', 10)

                if not text:
                    continue

                # Convert coordinates
                x0 = entry_box[0] * scale_x
                y_top = entry_box[1] * scale_y
                x1 = entry_box[2] * scale_x
                y_bottom = entry_box[3] * scale_y

                # PDF coordinate system: y=0 at bottom
                # If using image coordinates (y=0 at top), flip
                if 'image_width' in page_info:
                    y_pos = page_height - y_bottom + (font_size * 0.3)
                else:
                    # PDF coordinates: y increases downward from top
                    y_pos = page_height - y_bottom + (font_size * 0.3)

                c.setFont("Helvetica", font_size)
                c.drawString(x0 + 2, y_pos, text)

            c.save()
            packet.seek(0)

            # Merge overlay onto page
            overlay_reader = PdfReader(packet)
            if len(overlay_reader.pages) > 0:
                page.merge_page(overlay_reader.pages[0])

        writer.add_page(page)

    with open(output_pdf, 'wb') as f:
        writer.write(f)

    print(f"Filled {len(form_fields)} fields with annotations. Output: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input.pdf> <fields.json> <output.pdf>")
        sys.exit(1)
    fill_with_annotations(sys.argv[1], sys.argv[2], sys.argv[3])
