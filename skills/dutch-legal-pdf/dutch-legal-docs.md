# Dutch Legal Document Types and Templates

Reference for generating specific types of Dutch legal documents as PDFs. Each section describes the document type, its required structure, and a reportlab implementation pattern.

## Table of Contents

1. [Juridisch Memorandum (Legal Memorandum)](#juridisch-memorandum)
2. [Geheimhoudingsovereenkomst (NDA)](#geheimhoudingsovereenkomst)
3. [Contract Review Report](#contract-review-report)
4. [Verwerkersovereenkomst (Data Processing Agreement)](#verwerkersovereenkomst)
5. [Arbeidsovereenkomst (Employment Contract)](#arbeidsovereenkomst)
6. [Dagvaarding (Summons)](#dagvaarding)
7. [Juridisch Advies (Legal Opinion)](#juridisch-advies)
8. [Bezwaarschrift (Administrative Objection)](#bezwaarschrift)
9. [Common Building Blocks](#common-building-blocks)

---

## Juridisch Memorandum

Standard Dutch legal memorandum structure. Use when the user asks for a legal analysis, memo, or opinion on a specific legal question.

### Required Sections
1. **Header** — To/From/Date/Subject/Reference/Confidentiality
2. **Rechtsvraag** (Issue Presented) — Primary and subsidiary legal questions
3. **Kort Antwoord** (Brief Answer) — Summary conclusion
4. **Feiten** (Statement of Facts) — Numbered relevant facts
5. **Analyse** (Discussion) — Applicable law, case law, application to facts
6. **Conclusie** (Conclusion) — Answer to each legal question, risk assessment
7. **Aanbevelingen** (Recommendations) — Concrete action items with timeline
8. **Bronnen** (Sources) — Legislation, jurisprudentie, literatuur tables
9. **Disclaimer** — Mandatory AI disclaimer

### Template Reference
Full template at: `assets/templates/legal-memorandum.md`

### reportlab Pattern
```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)

def create_memorandum(filename, memo_data):
    doc = SimpleDocTemplate(filename, pagesize=A4,
        leftMargin=2.5*cm, rightMargin=2.5*cm,
        topMargin=2.5*cm, bottomMargin=2.5*cm)

    styles = getSampleStyleSheet()
    # Add legal styles as in main SKILL.md

    story = []

    # Header block
    story.append(Paragraph("MEMORANDUM", styles['LegalTitle']))
    story.append(HRFlowable(width="100%", thickness=1))
    story.append(Spacer(1, 8))

    header_data = [
        ['Aan:', memo_data['to']],
        ['Van:', memo_data['from']],
        ['Datum:', memo_data['date']],
        ['Betreft:', memo_data['subject']],
        ['Referentie:', memo_data['reference']],
    ]
    header_table = Table(header_data, colWidths=[3*cm, 12*cm])
    header_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(header_table)
    story.append(HRFlowable(width="100%", thickness=1))
    story.append(Spacer(1, 16))

    # I. Rechtsvraag
    story.append(Paragraph("I. Rechtsvraag", styles['LegalHeading']))
    for q in memo_data['questions']:
        story.append(Paragraph(q, styles['LegalBody']))

    # II. Kort Antwoord
    story.append(Paragraph("II. Kort Antwoord", styles['LegalHeading']))
    story.append(Paragraph(memo_data['brief_answer'], styles['LegalBody']))

    # III. Feiten
    story.append(Paragraph("III. Feiten", styles['LegalHeading']))
    for i, fact in enumerate(memo_data['facts'], 1):
        story.append(Paragraph(f"{i}. {fact}", styles['LegalBody']))

    # IV. Analyse (multiple subsections)
    story.append(Paragraph("IV. Analyse", styles['LegalHeading']))
    for section in memo_data['analysis_sections']:
        story.append(Paragraph(section['title'], styles['Heading3']))
        story.append(Paragraph(section['content'], styles['LegalBody']))

    # V. Conclusie
    story.append(Paragraph("V. Conclusie", styles['LegalHeading']))
    story.append(Paragraph(memo_data['conclusion'], styles['LegalBody']))

    # VI. Aanbevelingen
    story.append(Paragraph("VI. Aanbevelingen", styles['LegalHeading']))
    for i, rec in enumerate(memo_data['recommendations'], 1):
        story.append(Paragraph(f"{i}. {rec}", styles['LegalBody']))

    # Sources + Disclaimer
    # ... (add source tables and disclaimer as in main SKILL.md)

    doc.build(story)
```

---

## Geheimhoudingsovereenkomst

Dutch NDA / confidentiality agreement. Use when user asks for NDA, geheimhoudingsovereenkomst, or confidentiality agreement under Dutch law.

### Required Sections
1. **Partijen** — Full party identification with KVK numbers
2. **Overwegingen** — Recitals (A, B, C, D)
3. **Artikel 1: Definities** — Vertrouwelijke Informatie, Doel, Verbonden Personen
4. **Artikel 2: Vertrouwelijke Informatie** — Scope and limitations
5. **Artikel 3: Verplichtingen** — Confidentiality obligations (a through f)
6. **Artikel 4: Uitzonderingen** — Standard carve-outs (a through e)
7. **Artikel 5: Duur en Beeindiging** — Term and survival
8. **Artikel 6: Teruggave** — Return/destruction of information
9. **Artikel 7: Boetebeding** — Penalty clause
10. **Artikel 8: Toepasselijk Recht** — Dutch law, forum selection
11. **Overige bepalingen** — Amendments, entirety, assignment, severability
12. **Ondertekening** — Signature blocks

### Template Reference
Full template at: `assets/templates/nda-template-nl.md`

### Key Legal Considerations
- Boetebeding (penalty clause): Must be proportionate under Dutch law (BW 6:91-94)
- Survival period: Typically 2-5 years after termination
- Forum selection: Name specific rechtbank
- AVG compliance: If personal data is involved, reference the verwerkersovereenkomst

---

## Contract Review Report

Structured analysis of a contract with risk flagging. Use when user asks to review, analyze, or assess a contract.

### Required Sections
1. **Executive Summary** — Document type, parties, key terms, overall risk level
2. **Risk Dashboard** — GREEN/YELLOW/RED per clause category
3. **Clause-by-Clause Analysis** — For each clause: text, applicable law, risk level, recommendation
4. **Missing Clauses** — Standard clauses not present
5. **Recommendations** — Priority-ordered action items
6. **Sources** — Legislation and case law references

### Template Reference
Full template at: `assets/templates/contract-review-report.md`

### Risk Color Coding
- **GREEN**: Standard market terms, compliant with mandatory law
- **YELLOW**: Non-standard but enforceable, potential issues
- **RED**: Potentially unenforceable, violates mandatory law, significant risk

---

## Verwerkersovereenkomst

Data Processing Agreement per AVG/GDPR Art. 28. Use when user needs a DPA, verwerkersovereenkomst, or data processing agreement.

### Required Sections
1. **Partijen** — Verwerkingsverantwoordelijke (controller) and Verwerker (processor)
2. **Artikel 1: Definities** — AVG-aligned definitions
3. **Artikel 2: Voorwerp en Duur** — Subject, duration, types of personal data
4. **Artikel 3: Verplichtingen Verwerker** — Art. 28(3) requirements
5. **Artikel 4: Subverwerkers** — Sub-processor requirements
6. **Artikel 5: Doorgifte** — International transfers (adequacy, SCCs)
7. **Artikel 6: Beveiliging** — Technical and organizational measures (Art. 32)
8. **Artikel 7: Meldplicht** — Data breach notification (Art. 33/34)
9. **Artikel 8: DPIA** — Data Protection Impact Assessment support
10. **Artikel 9: Rechten Betrokkenen** — Data subject rights support
11. **Artikel 10: Audit** — Audit rights
12. **Artikel 11: Aansprakelijkheid** — Liability and indemnification
13. **Bijlage 1: Verwerkingen** — Processing activities table
14. **Bijlage 2: Beveiligingsmaatregelen** — TOM details

### Template Reference
Full template at: `assets/templates/verwerkersovereenkomst.md`

---

## Arbeidsovereenkomst

Dutch employment contract. Use when user needs an employment agreement, arbeidsovereenkomst, or work contract under Dutch law.

### Required Sections
1. **Partijen** — Werkgever (employer) and Werknemer (employee)
2. **Artikel 1: Indiensttreding** — Start date, function, location
3. **Artikel 2: Duur** — Fixed term (bepaalde tijd) or indefinite (onbepaalde tijd)
4. **Artikel 3: Proeftijd** — Probationary period (max per BW 7:652)
5. **Artikel 4: Werktijden** — Hours, schedule, overtime
6. **Artikel 5: Salaris** — Gross salary, holiday allowance (8%), 13th month
7. **Artikel 6: Vakantie** — Vacation days (minimum 4x weekly hours per BW 7:634)
8. **Artikel 7: Pensioen** — Pension arrangement
9. **Artikel 8: Ziekte** — Sick leave (70% pay for 104 weeks per BW 7:629)
10. **Artikel 9: Opzegtermijn** — Notice period
11. **Artikel 10: Geheimhouding** — Confidentiality
12. **Artikel 11: Concurrentiebeding** — Non-compete (must be written, specific per BW 7:653)
13. **Artikel 12: Toepasselijk Recht** — Dutch law
14. **Bijlage: CAO** — Applicable collective labor agreement

### Template Reference
Full template at: `assets/templates/arbeidsovereenkomst.md`

### Key Legal Constraints
- Proeftijd: Max 1 month for contracts ≤2 years, max 2 months otherwise
- Concurrentiebeding: Must be in writing; for fixed-term requires specific motivation
- Ketenregeling: Max 3 consecutive fixed-term contracts / 36 months total (BW 7:668a)
- Transitievergoeding: Due upon employer-initiated termination (BW 7:673)

---

## Dagvaarding

Court summons under Dutch civil procedure. Use when user needs a dagvaarding, summons, or wants to initiate court proceedings.

### Required Sections
1. **Kop** — "DAGVAARDING" + court identification
2. **Partijen** — Eiser (plaintiff) identification with address, advocate
3. **Gedaagde** — Defendant identification, service details
4. **Aanzegging** — Formal notice to appear (verschijntermijn)
5. **Feitelijke Grondslag** — Statement of facts (numbered)
6. **Juridische Grondslag** — Legal basis (specific articles)
7. **Middelen** — Legal arguments and reasoning
8. **Vordering** (Petitum) — What plaintiff demands (primair/subsidiair)
9. **Bewijsaanbod** — Offer of proof
10. **Proceskosten** — Claim for legal costs
11. **Betekening** — Service details

### Formatting Notes
- Court-specific requirements vary; check local rules (procesreglement)
- Dagvaarding must be served by deurwaarder (bailiff)
- Verschijntermijn: typically 4 weeks (binnenhof) or 6 weeks (buitenland)
- Number all paragraphs consecutively

---

## Juridisch Advies

Legal opinion / advice letter. Use when user asks for legal advice, opinion, or counsel on a Dutch law matter.

### Required Sections
1. **Briefhoofd** — Addressee, date, reference, subject
2. **Inleiding** — Context and scope of advice
3. **Feiten** — Facts as understood
4. **Juridisch Kader** — Applicable legal framework
5. **Analyse** — Application of law to facts
6. **Conclusie en Advies** — Concrete recommendations
7. **Voorbehoud** — Reservations and limitations
8. **Disclaimer** — AI disclaimer

---

## Bezwaarschrift

Administrative objection against a government decision (beschikking). Use when user needs to object to a government decision under the Awb.

### Required Sections
1. **Geadresseerde** — Administrative body (bestuursorgaan)
2. **Betreft** — Decision being objected to (beschikking)
3. **Bezwaarmaker** — Objector identification
4. **Inleiding** — Statement that this is a bezwaar under Awb Art. 6:4
5. **Ontvankelijkheid** — Timeliness (6-week deadline per Awb 6:7), standing
6. **Feiten** — Relevant facts
7. **Gronden** — Grounds for objection (specific legal arguments)
8. **Verzoek** — What the objector requests (herroeping, wijziging)
9. **Bijlagen** — List of appendices (copy of beschikking, evidence)

### Key Legal Requirements
- Must be filed within 6 weeks of the beschikking (Awb 6:7)
- Must contain name, address, date, description of beschikking, grounds (Awb 6:5)
- Consider requesting voorlopige voorziening (interim relief) if urgent

---

## Common Building Blocks

### Party Identification Block

Standard Dutch legal party identification. Use for any contract or legal document.

```python
def create_party_block(party_data):
    """Generate party identification paragraph."""
    return (
        f"<b>{party_data['name']}</b>, een {party_data['legal_form']} naar Nederlands recht, "
        f"statutair gevestigd te {party_data['city']}, "
        f"kantoorhoudende te ({party_data['postal_code']}) {party_data['address']}, "
        f"ingeschreven in het Handelsregister van de Kamer van Koophandel "
        f"onder nummer {party_data['kvk_number']}, "
        f"rechtsgeldig vertegenwoordigd door {party_data['representative']}, "
        f"in de functie van {party_data['function']},"
    )
```

### Source Citation Table

```python
def create_source_table(legislation, jurisprudentie):
    """Create standardized source citation tables."""
    # Legislation table
    leg_data = [['#', 'Bron', 'Artikelen']]
    for i, src in enumerate(legislation, 1):
        leg_data.append([str(i), src['law'], src['articles']])

    # Case law table
    case_data = [['#', 'ECLI', 'Instantie', 'Datum']]
    for i, case in enumerate(jurisprudentie, 1):
        case_data.append([str(i), case['ecli'], case['court'], case['date']])

    return leg_data, case_data
```

### Disclaimer Block

Always include at the end of every legal PDF:

```python
from datetime import date

def create_disclaimer_block(styles, language='nl'):
    """Generate mandatory disclaimer block."""
    elements = []
    elements.append(PageBreak())
    elements.append(Paragraph("DISCLAIMER", styles['LegalHeading']))

    if language == 'nl':
        text = (
            "Dit document is opgesteld met behulp van AI-ondersteunde analyse en vormt "
            "<b>geen juridisch advies</b> in de zin van de Advocatenwet. De informatie is "
            "uitsluitend informatief. Raadpleeg altijd een gekwalificeerde advocaat "
            "(ingeschreven bij de Nederlandse Orde van Advocaten) voordat u juridische "
            "beslissingen neemt. Aan dit document kunnen geen rechten worden ontleend. "
            "De analyse is gebaseerd op de stand van het recht op de aangegeven datum en "
            "houdt mogelijk geen rekening met recente wijzigingen."
        )
    else:
        text = (
            "This document was prepared with the assistance of AI-powered analysis and "
            "does <b>not constitute legal advice</b> within the meaning of the Dutch "
            "Advocates Act (Advocatenwet). The information is for informational purposes only. "
            "Always consult a qualified lawyer registered with the Netherlands Bar Association "
            "before making legal decisions. No rights may be derived from this document."
        )

    elements.append(Paragraph(text, styles['LegalDisclaimer']))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph(
        f"FALCON (FutureAtoms AI Legal Counsel Of Netherlands) | "
        f"Datum: {date.today().strftime('%d-%m-%Y')} | "
        f"Verificatiedatum wetgeving: {date.today().strftime('%d-%m-%Y')}",
        styles['LegalFooter']
    ))
    return elements
```

### Risk Badge (for Contract Review)

```python
from reportlab.platypus import Paragraph
from reportlab.lib import colors

def risk_badge(level, styles):
    """Create colored risk indicator."""
    color_map = {
        'GREEN': '#27AE60',
        'YELLOW': '#F39C12',
        'RED': '#E74C3C',
    }
    hex_color = color_map.get(level, '#95A5A6')
    return Paragraph(
        f'<font color="{hex_color}"><b>[{level}]</b></font>',
        styles['Normal']
    )
```
