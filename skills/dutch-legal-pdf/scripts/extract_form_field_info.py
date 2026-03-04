#!/usr/bin/env python3
"""Extract form field information from a fillable PDF."""
import sys
import json

def extract_form_fields(pdf_path, output_json):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("Error: pypdf not installed. Run: pip install pypdf")
        sys.exit(1)

    reader = PdfReader(pdf_path)
    fields_info = []

    if not reader.get_fields():
        print("No fillable fields found in this PDF.")
        sys.exit(1)

    for page_num, page in enumerate(reader.pages, 1):
        if '/Annots' not in page:
            continue
        for annot in page['/Annots']:
            annot_obj = annot.get_object()
            if annot_obj.get('/Subtype') != '/Widget':
                continue

            field_info = {
                'field_id': str(annot_obj.get('/T', '')),
                'page': page_num,
                'type': 'text',
            }

            # Get bounding box
            rect = annot_obj.get('/Rect')
            if rect:
                field_info['rect'] = [float(r) for r in rect]

            # Determine field type
            ft = annot_obj.get('/FT')
            if ft == '/Btn':
                # Check if checkbox or radio
                if '/Ff' in annot_obj and (int(annot_obj['/Ff']) & (1 << 15)):
                    field_info['type'] = 'radio_group'
                    # Extract radio options
                    kids = annot_obj.get('/Kids', [])
                    options = []
                    for kid in kids:
                        kid_obj = kid.get_object()
                        ap = kid_obj.get('/AP', {})
                        if '/N' in ap:
                            values = [k for k in ap['/N'].keys() if k != '/Off']
                            for v in values:
                                options.append({
                                    'value': v,
                                    'rect': [float(r) for r in kid_obj.get('/Rect', [])]
                                })
                    field_info['radio_options'] = options
                else:
                    field_info['type'] = 'checkbox'
                    ap = annot_obj.get('/AP', {})
                    if '/N' in ap:
                        normal_ap = ap['/N']
                        checked_values = [k for k in normal_ap.keys() if k != '/Off']
                        field_info['checked_value'] = checked_values[0] if checked_values else '/Yes'
                        field_info['unchecked_value'] = '/Off'
            elif ft == '/Ch':
                field_info['type'] = 'choice'
                options = annot_obj.get('/Opt', [])
                field_info['choice_options'] = []
                for opt in options:
                    if isinstance(opt, list):
                        field_info['choice_options'].append({
                            'value': str(opt[0]),
                            'text': str(opt[1]) if len(opt) > 1 else str(opt[0])
                        })
                    else:
                        field_info['choice_options'].append({
                            'value': str(opt),
                            'text': str(opt)
                        })
            elif ft == '/Tx':
                field_info['type'] = 'text'

            fields_info.append(field_info)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(fields_info, f, indent=2, ensure_ascii=False)

    print(f"Extracted {len(fields_info)} fields to {output_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.pdf> <output.json>")
        sys.exit(1)
    extract_form_fields(sys.argv[1], sys.argv[2])
