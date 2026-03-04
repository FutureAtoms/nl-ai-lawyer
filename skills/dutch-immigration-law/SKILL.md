---
name: dutch-immigration-law
description: Residence permits, knowledge migrant scheme, IND procedures, and work permits under Dutch immigration law
---

# Dutch Immigration Law

## When to Use
- User asks about obtaining a residence permit (verblijfsvergunning) in the Netherlands
- User asks about the highly skilled migrant scheme (kennismigrantenregeling)
- User asks about work permits (TWV - tewerkstellingsvergunning)
- User asks about IND (Immigration and Naturalisation Service) procedures
- User asks about Dutch citizenship or naturalization
- User asks about the 30% ruling for expat employees
- User asks about family reunification (gezinshereniging) or family formation
- User asks about asylum or refugee status
- User asks about EU/EEA nationals' rights in the Netherlands

## Process
1. **Identify nationality** - EU/EEA/Swiss or third-country national (determines applicable framework)
2. **Identify purpose of stay** - Work, study, family, asylum, other
3. **Determine applicable scheme** - Which residence permit type or regulation applies
4. **Analyze requirements** - Check specific conditions for the relevant permit type
5. **Outline procedure** - IND application process, timelines, costs
6. **Flag conditions and obligations** - Reporting, civic integration, etc.
7. **Append disclaimer**

## Key Legal Framework
- **Vreemdelingenwet 2000 (Vw)** - Aliens Act 2000
- **Vreemdelingenbesluit 2000 (Vb)** - Aliens Decree 2000
- **Voorschrift Vreemdelingen 2000 (VV)** - Aliens Regulation 2000
- **Vreemdelingencirculaire (Vc)** - Aliens Circular (policy rules)
- **Wet arbeid vreemdelingen (Wav)** - Foreign Nationals Employment Act
- **Besluit uitvoering Wav (BuWav)** - Wav Implementation Decree
- **Rijkswet op het Nederlanderschap (RWN)** - Nationality Act
- **Wet inburgering 2021 (Wi)** - Civic Integration Act
- **EU Free Movement Directive 2004/38/EC**
- **EU Blue Card Directive**
- **Wet modern migratiebeleid** - Modern Migration Policy Act
- **IND** (Immigratie- en Naturalisatiedienst) - Immigration and Naturalisation Service
- **Courts**: Rechtbank Den Haag (all locations) for immigration cases; ABRvS for higher appeal

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

**Note:** Monetary thresholds, tax rates, and salary requirements are subject to annual adjustment. Reference files include date stamps - always verify current values.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **No application filing**: Do not file or prepare IND applications
- **Asylum sensitivity**: Asylum cases require specialized legal counsel; never provide substantive asylum advice
- **Deadline awareness**: Immigration deadlines are strict; emphasize timeliness
- **Criminal background**: Flag that criminal records can affect immigration status
- **Unauthorized stay**: Do not advise on circumventing immigration rules
- **Family impact**: Immigration decisions affect entire families; approach with sensitivity
- **Data sensitivity**: Immigration status is highly sensitive personal information
- **Recognized sponsor**: Emphasize that many schemes require a recognized sponsor (erkend referent)

### Disclaimer Language Selection
- Use **Dutch disclaimer** (`assets/disclaimers/disclaimer-nl.md`) when:
  - The query is in Dutch
  - The output document is in Dutch
  - The user's organization config specifies Dutch as primary language
- Use **English disclaimer** (`assets/disclaimers/disclaimer-en.md`) when:
  - The query is in English
  - The output document is in English
  - Default when language is unclear
- Use **both disclaimers** when:
  - The output is bilingual
  - The user requests both languages

## MCP Tools to Use
- `search_legislation` - Look up immigration legislation
- `get_legislation` - Retrieve specific statutory text
- `search_case_law` - Find immigration case law (ABRvS)
- `get_case_law` - Retrieve specific immigration decisions

## Related Skills
- **dutch-employment-law** - For employment contracts (arbeidsovereenkomst) linked to work permits
- **dutch-tax-law** - For the 30% ruling and tax implications for expats

## Output Format
```
## Immigration Law Analysis

**Nationality**: [If relevant]
**Purpose of Stay**: [Work/Study/Family/Other]
**Applicable Scheme**: [Specific permit type]

## Requirements
[Specific conditions to be met]

## Application Procedure
- **Where to apply**: [IND / Embassy / Online]
- **Who applies**: [Applicant / Sponsor]
- **Required documents**: [List]
- **Processing time**: [Standard timeframe]
- **Costs**: [Application fees]

## Rights and Obligations
[What the permit allows and requires]

## Duration and Renewal
[Validity period and renewal process]

## Path to Permanent Residence / Citizenship
[If applicable]

---
[Disclaimer]
```

## Escalation Triggers
- Asylum application or refugee status determination
- Deportation or removal order (uitzetting)
- Criminal record affecting immigration status
- Revocation of residence permit
- Family separation across borders
- Unaccompanied minors
- Statelessness (staatloosheid) issues
- Detention of foreign nationals (vreemdelingenbewaring)
- Complex multi-country immigration history
- EU long-term resident or EU Blue Card cross-border transfers

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
