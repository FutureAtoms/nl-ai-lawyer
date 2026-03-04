#!/usr/bin/env python3
"""Convert PDF pages to PNG images for visual inspection."""
import sys
import os

def convert_pdf_to_images(pdf_path, output_dir, dpi=200):
    os.makedirs(output_dir, exist_ok=True)

    try:
        from pdf2image import convert_from_path
        images = convert_from_path(pdf_path, dpi=dpi)
        for i, image in enumerate(images):
            output_path = os.path.join(output_dir, f"page_{i+1}.png")
            image.save(output_path, "PNG")
            print(f"Saved: {output_path} ({image.size[0]}x{image.size[1]})")
        print(f"\nConverted {len(images)} pages to {output_dir}")
    except ImportError:
        print("Error: pdf2image not installed. Run: pip install pdf2image")
        print("Also requires poppler: brew install poppler (macOS) or apt install poppler-utils (Linux)")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <pdf_file> <output_directory> [dpi]")
        sys.exit(1)
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    convert_pdf_to_images(sys.argv[1], sys.argv[2], dpi)
