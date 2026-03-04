#!/usr/bin/env python3
"""Extract form structure (labels, lines, checkboxes) from a PDF."""
import sys
import json

def extract_form_structure(pdf_path, output_json):
    try:
        import pdfplumber
    except ImportError:
        print("Error: pdfplumber not installed. Run: pip install pdfplumber")
        sys.exit(1)

    result = {'pages': []}

    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            page_data = {
                'page_number': page_num,
                'width': float(page.width),
                'height': float(page.height),
                'labels': [],
                'lines': [],
                'checkboxes': [],
                'row_boundaries': [],
            }

            # Extract text labels with coordinates
            for char_group in (page.extract_words() or []):
                page_data['labels'].append({
                    'text': char_group['text'],
                    'x0': float(char_group['x0']),
                    'top': float(char_group['top']),
                    'x1': float(char_group['x1']),
                    'bottom': float(char_group['bottom']),
                })

            # Extract lines
            for line in (page.lines or []):
                x0, y0 = float(line['x0']), float(line['top'])
                x1, y1 = float(line['x1']), float(line['bottom'])
                # Horizontal lines (row boundaries)
                if abs(y0 - y1) < 2 and abs(x1 - x0) > 50:
                    page_data['lines'].append({
                        'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1,
                        'orientation': 'horizontal'
                    })

            # Extract rectangles (potential checkboxes)
            for rect in (page.rects or []):
                w = float(rect['x1']) - float(rect['x0'])
                h = float(rect['bottom']) - float(rect['top'])
                # Small squares are likely checkboxes
                if 5 < w < 20 and 5 < h < 20 and abs(w - h) < 5:
                    page_data['checkboxes'].append({
                        'x0': float(rect['x0']),
                        'top': float(rect['top']),
                        'x1': float(rect['x1']),
                        'bottom': float(rect['bottom']),
                        'center_x': (float(rect['x0']) + float(rect['x1'])) / 2,
                        'center_y': (float(rect['top']) + float(rect['bottom'])) / 2,
                    })

            # Calculate row boundaries from horizontal lines
            h_lines = sorted(
                [l for l in page_data['lines'] if l['orientation'] == 'horizontal'],
                key=lambda l: l['y0']
            )
            for i in range(len(h_lines) - 1):
                page_data['row_boundaries'].append({
                    'top': h_lines[i]['y0'],
                    'bottom': h_lines[i + 1]['y0'],
                })

            result['pages'].append(page_data)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    total_labels = sum(len(p['labels']) for p in result['pages'])
    total_checkboxes = sum(len(p['checkboxes']) for p in result['pages'])
    print(f"Extracted structure from {len(result['pages'])} pages:")
    print(f"  Labels: {total_labels}")
    print(f"  Checkboxes: {total_checkboxes}")
    print(f"  Saved to: {output_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.pdf> <output.json>")
        sys.exit(1)
    extract_form_structure(sys.argv[1], sys.argv[2])
