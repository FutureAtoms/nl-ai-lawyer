#!/usr/bin/env python3
"""Check if a PDF has fillable form fields."""
import sys

def check_fillable_fields(pdf_path):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("Error: pypdf not installed. Run: pip install pypdf")
        sys.exit(1)

    reader = PdfReader(pdf_path)
    fields = reader.get_fields()

    if fields:
        print(f"FILLABLE: {pdf_path} has {len(fields)} fillable form fields.")
        print("\nFields found:")
        for name, field in fields.items():
            field_type = field.get('/FT', 'Unknown')
            print(f"  - {name} (type: {field_type})")
        return True
    else:
        print(f"NOT FILLABLE: {pdf_path} has no fillable form fields.")
        print("Use the non-fillable fields approach (text annotations).")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pdf_file>")
        sys.exit(1)
    check_fillable_fields(sys.argv[1])
