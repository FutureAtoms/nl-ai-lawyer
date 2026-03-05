#!/usr/bin/env python3
"""
Create professional Dutch legal PDFs from structured data.
Supports: memoranda, NDAs, contract reviews, legal opinions.
"""
import sys
import json
from datetime import date

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm, mm
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, HRFlowable, KeepTogether
    )
except ImportError:
    print("Error: reportlab not installed. Run: pip install reportlab")
    sys.exit(1)


def get_legal_styles():
    """Create Dutch legal document styles."""
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        'LegalTitle', parent=styles['Title'],
        fontSize=16, spaceAfter=20, alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'LegalSubtitle', parent=styles['Normal'],
        fontSize=12, spaceAfter=12, alignment=TA_CENTER,
        fontName='Helvetica-Oblique', textColor=colors.HexColor('#555555')
    ))
    styles.add(ParagraphStyle(
        'LegalHeading', parent=styles['Heading2'],
        fontSize=12, spaceBefore=16, spaceAfter=8,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'LegalSubHeading', parent=styles['Heading3'],
        fontSize=10, spaceBefore=10, spaceAfter=6,
        fontName='Helvetica-Bold'
    ))
    styles.add(ParagraphStyle(
        'LegalBody', parent=styles['Normal'],
        fontSize=10, leading=14, alignment=TA_JUSTIFY, spaceAfter=6
    ))
    styles.add(ParagraphStyle(
        'LegalArticle', parent=styles['Normal'],
        fontSize=10, leading=14, alignment=TA_JUSTIFY,
        spaceAfter=4, leftIndent=1*cm
    ))
    styles.add(ParagraphStyle(
        'LegalDisclaimer', parent=styles['Normal'],
        fontSize=8, leading=10, textColor=colors.grey,
        alignment=TA_JUSTIFY, spaceBefore=20
    ))
    styles.add(ParagraphStyle(
        'LegalFooter', parent=styles['Normal'],
        fontSize=8, alignment=TA_RIGHT, textColor=colors.grey
    ))
    return styles


def add_disclaimer(story, styles, language='nl'):
    """Add mandatory AI disclaimer to document."""
    story.append(PageBreak())
    story.append(Paragraph("DISCLAIMER", styles['LegalHeading']))

    if language == 'nl':
        text = (
            "Dit document is opgesteld met behulp van AI-ondersteunde analyse en vormt "
            "<b>geen juridisch advies</b> in de zin van de Advocatenwet. De informatie is "
            "uitsluitend informatief. Raadpleeg altijd een gekwalificeerde advocaat "
            "(ingeschreven bij de Nederlandse Orde van Advocaten) voordat u juridische "
            "beslissingen neemt. Aan dit document kunnen geen rechten worden ontleend. "
            "De analyse is gebaseerd op de stand van het recht op de aangegeven datum."
        )
    else:
        text = (
            "This document was prepared with the assistance of AI-powered analysis and "
            "does <b>not constitute legal advice</b> within the meaning of the Dutch "
            "Advocates Act (Advocatenwet). Always consult a qualified lawyer registered "
            "with the Netherlands Bar Association before making legal decisions. "
            "No rights may be derived from this document."
        )

    story.append(Paragraph(text, styles['LegalDisclaimer']))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        f"FALCON (FutureAtoms AI Legal Counsel Of Netherlands) | "
        f"Datum: {date.today().strftime('%d-%m-%Y')} | "
        f"Verificatiedatum wetgeving: {date.today().strftime('%d-%m-%Y')}",
        styles['LegalFooter']
    ))


def create_memorandum(data, output_path):
    """Create a Dutch legal memorandum PDF."""
    doc = SimpleDocTemplate(output_path, pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.5*cm,
        topMargin=2.5*cm, bottomMargin=2.5*cm)
    styles = get_legal_styles()
    story = []

    # Title
    story.append(Paragraph("MEMORANDUM", styles['LegalTitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
    story.append(Spacer(1, 8))

    # Header table
    header_data = [
        ['Aan:', data.get('to', '[ONTVANGER]')],
        ['Van:', data.get('from', '[AFZENDER]')],
        ['Datum:', data.get('date', date.today().strftime('%d-%m-%Y'))],
        ['Betreft:', data.get('subject', '[ONDERWERP]')],
        ['Referentie:', data.get('reference', '[REF]')],
    ]
    if data.get('confidential'):
        header_data.append(['Vertrouwelijkheid:', 'VERTROUWELIJK'])

    ht = Table(header_data, colWidths=[3*cm, 12*cm])
    ht.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(ht)
    story.append(HRFlowable(width="100%", thickness=1))
    story.append(Spacer(1, 16))

    # Sections
    sections = [
        ('I. Rechtsvraag', data.get('questions', [])),
        ('II. Kort Antwoord', data.get('brief_answer', '')),
        ('III. Feiten', data.get('facts', [])),
        ('IV. Analyse', data.get('analysis', '')),
        ('V. Conclusie', data.get('conclusion', '')),
        ('VI. Aanbevelingen', data.get('recommendations', [])),
    ]

    for title, content in sections:
        story.append(Paragraph(title, styles['LegalHeading']))
        if isinstance(content, list):
            for i, item in enumerate(content, 1):
                story.append(Paragraph(f"{i}. {item}", styles['LegalBody']))
        elif isinstance(content, str):
            story.append(Paragraph(content, styles['LegalBody']))

    # Sources
    if data.get('sources'):
        story.append(Paragraph("Bronnen", styles['LegalHeading']))
        src_data = [['#', 'Bron', 'Referentie']]
        for i, src in enumerate(data['sources'], 1):
            src_data.append([str(i), src.get('source', ''), src.get('reference', '')])
        st = Table(src_data, colWidths=[1*cm, 7*cm, 7*cm])
        st.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(st)

    add_disclaimer(story, styles, data.get('language', 'nl'))
    doc.build(story)
    print(f"Memorandum saved to: {output_path}")


def create_contract_review(data, output_path):
    """Create a contract review report PDF with risk flagging."""
    doc = SimpleDocTemplate(output_path, pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.5*cm,
        topMargin=2.5*cm, bottomMargin=2.5*cm)
    styles = get_legal_styles()
    story = []

    # Title
    story.append(Paragraph("CONTRACT REVIEW REPORT", styles['LegalTitle']))
    story.append(Paragraph(
        f"Beoordeling van: {data.get('contract_name', '[CONTRACT]')}",
        styles['LegalSubtitle']
    ))
    story.append(HRFlowable(width="100%", thickness=1))
    story.append(Spacer(1, 16))

    # Executive Summary
    story.append(Paragraph("Executive Summary", styles['LegalHeading']))
    story.append(Paragraph(data.get('summary', ''), styles['LegalBody']))

    # Risk Dashboard
    if data.get('risk_items'):
        story.append(Paragraph("Risk Dashboard", styles['LegalHeading']))
        risk_colors = {
            'GREEN': colors.HexColor('#27AE60'),
            'YELLOW': colors.HexColor('#F39C12'),
            'RED': colors.HexColor('#E74C3C'),
        }
        risk_data = [['Clausule', 'Risico', 'Samenvatting']]
        for item in data['risk_items']:
            risk_data.append([
                item.get('clause', ''),
                item.get('risk_level', 'GREEN'),
                item.get('summary', ''),
            ])
        rt = Table(risk_data, colWidths=[4*cm, 2.5*cm, 8.5*cm])
        style_commands = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]
        # Color-code risk column
        for i, item in enumerate(data['risk_items'], 1):
            level = item.get('risk_level', 'GREEN')
            if level in risk_colors:
                style_commands.append(
                    ('TEXTCOLOR', (1, i), (1, i), risk_colors[level])
                )
                style_commands.append(
                    ('FONTNAME', (1, i), (1, i), 'Helvetica-Bold')
                )
        rt.setStyle(TableStyle(style_commands))
        story.append(rt)
        story.append(Spacer(1, 12))

    # Clause Analysis
    if data.get('clauses'):
        story.append(Paragraph("Clause Analysis", styles['LegalHeading']))
        for clause in data['clauses']:
            story.append(Paragraph(
                f"<b>{clause.get('name', '')}</b> [{clause.get('risk_level', 'GREEN')}]",
                styles['LegalSubHeading']
            ))
            story.append(Paragraph(clause.get('analysis', ''), styles['LegalBody']))
            if clause.get('recommendation'):
                story.append(Paragraph(
                    f"<i>Aanbeveling: {clause['recommendation']}</i>",
                    styles['LegalArticle']
                ))

    add_disclaimer(story, styles, data.get('language', 'nl'))
    doc.build(story)
    print(f"Contract review saved to: {output_path}")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print(f"  {sys.argv[0]} memorandum <data.json> [output.pdf]")
        print(f"  {sys.argv[0]} contract-review <data.json> [output.pdf]")
        sys.exit(1)

    doc_type = sys.argv[1]
    data_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else f"{doc_type}.pdf"

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if doc_type == 'memorandum':
        create_memorandum(data, output_path)
    elif doc_type == 'contract-review':
        create_contract_review(data, output_path)
    else:
        print(f"Unknown document type: {doc_type}")
        print("Supported: memorandum, contract-review")
        sys.exit(1)


if __name__ == "__main__":
    main()
