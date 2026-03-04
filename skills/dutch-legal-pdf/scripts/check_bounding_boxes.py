#!/usr/bin/env python3
"""Validate bounding boxes in fields.json for form filling."""
import sys
import json

def boxes_overlap(box1, box2):
    """Check if two bounding boxes overlap."""
    return not (box1[2] <= box2[0] or box2[2] <= box1[0] or
                box1[3] <= box2[1] or box2[3] <= box1[1])

def check_bounding_boxes(fields_json_path):
    with open(fields_json_path, 'r') as f:
        data = json.load(f)

    errors = []
    warnings = []

    fields = data.get('form_fields', [])

    for i, field in enumerate(fields):
        entry_box = field.get('entry_bounding_box', [])
        if len(entry_box) != 4:
            errors.append(f"Field {i} '{field.get('field_label', '?')}': "
                         f"entry_bounding_box must have 4 values [left, top, right, bottom]")
            continue

        # Check box dimensions
        width = entry_box[2] - entry_box[0]
        height = entry_box[3] - entry_box[1]

        if width <= 0 or height <= 0:
            errors.append(f"Field {i} '{field.get('field_label', '?')}': "
                         f"entry box has zero or negative dimensions ({width}x{height})")

        # Check if box is too small for font size
        font_size = field.get('entry_text', {}).get('font_size', 10)
        if height < font_size * 0.8:
            warnings.append(f"Field {i} '{field.get('field_label', '?')}': "
                           f"entry box height ({height:.1f}) may be too small for "
                           f"font size {font_size}")

        # Check for overlaps with other fields
        for j in range(i + 1, len(fields)):
            other = fields[j]
            other_box = other.get('entry_bounding_box', [])
            if len(other_box) == 4 and field.get('page_number') == other.get('page_number'):
                if boxes_overlap(entry_box, other_box):
                    errors.append(
                        f"Fields {i} '{field.get('field_label', '?')}' and "
                        f"{j} '{other.get('field_label', '?')}' have overlapping entry boxes")

    if errors:
        print("ERRORS (must fix before filling):")
        for e in errors:
            print(f"  [ERROR] {e}")
    if warnings:
        print("\nWARNINGS (may cause issues):")
        for w in warnings:
            print(f"  [WARN] {w}")
    if not errors and not warnings:
        print("All bounding boxes look good!")

    return len(errors) == 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <fields.json>")
        sys.exit(1)
    ok = check_bounding_boxes(sys.argv[1])
    sys.exit(0 if ok else 1)
