#!/usr/bin/env python3
"""Fill fillable PDF form fields with provided values."""
import sys
import json

def fill_form(input_pdf, values_json, output_pdf):
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        print("Error: pypdf not installed. Run: pip install pypdf")
        sys.exit(1)

    with open(values_json, 'r', encoding='utf-8') as f:
        field_values = json.load(f)

    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    writer.append(reader)

    # Build a map of field_id -> value
    value_map = {fv['field_id']: fv['value'] for fv in field_values}

    # Get available fields
    available_fields = reader.get_fields() or {}
    available_names = set(available_fields.keys())

    # Validate field IDs
    errors = []
    for fv in field_values:
        if fv['field_id'] not in available_names:
            errors.append(f"Field '{fv['field_id']}' not found in PDF. "
                         f"Available: {', '.join(sorted(available_names)[:10])}...")

    if errors:
        print("ERRORS - fix these before retrying:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)

    # Fill fields
    writer.update_page_form_field_values(writer.pages[0], value_map)

    # Try to fill on all pages
    for page_num in range(len(writer.pages)):
        try:
            writer.update_page_form_field_values(writer.pages[page_num], value_map)
        except Exception:
            pass

    with open(output_pdf, 'wb') as f:
        writer.write(f)

    print(f"Filled {len(field_values)} fields. Output: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input.pdf> <field_values.json> <output.pdf>")
        sys.exit(1)
    fill_form(sys.argv[1], sys.argv[2], sys.argv[3])
