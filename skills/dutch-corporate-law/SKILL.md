---
name: dutch-corporate-law
description: BV/NV formation, corporate governance, M&A, KVK registration, and BW Book 2 analysis
---

# Dutch Corporate Law

## When to Use
- User asks about forming a Dutch BV or NV
- User has questions about corporate governance, board duties, or shareholder rights
- User asks about M&A transactions (mergers, acquisitions, demergers) under Dutch law
- User needs guidance on KVK (Chamber of Commerce) registration
- User asks about director liability (bestuurdersaansprakelijkheid)
- User has questions about the Dutch Corporate Governance Code
- User asks about foundation (stichting) or association (vereniging) law

## Process
1. **Identify the entity type** - BV, NV, stichting, vereniging, cooperatie, VOF, CV, maatschap, or other
2. **Determine the legal question** - Formation, governance, transactions, liability, dissolution
3. **Research applicable provisions** - BW Boek 2 and any sector-specific regulation
4. **Analyze** - Apply the law to the user's question:
   a. Identify mandatory vs. optional provisions
   b. Check articles of association (statuten) requirements
   c. Consider corporate governance code applicability
   d. Review case law on the specific issue
5. **Provide practical guidance** - Next steps, filing requirements, timelines
6. **Append disclaimer**

## Key Legal Framework
- **BW Boek 2** - Rechtspersonen (Legal Persons):
  - Titel 1: Algemene bepalingen (General provisions)
  - Titel 3: Verenigingen (Associations)
  - Titel 4: Cooperaties (Cooperatives)
  - Titel 5: Naamloze vennootschappen (NV - Public Limited Companies)
  - Titel 6: Besloten vennootschappen (BV - Private Limited Companies)
  - Titel 6A: Stichtingen (Foundations)
- **Handelsregisterwet 2007** - Trade Register Act (KVK registration)
- **Wet op het notarisambt** - Notarial Act (notarial deeds for incorporation)
- **SER Fusiegedragsregels 2015** - Merger code of conduct
- **Wet op de ondernemingsraden (WOR)** - Works Council Act
- **Dutch Corporate Governance Code** (updated 2022)
- **Wet giraal effectenverkeer (Wge)** - Securities transactions
- **Wet toezicht financiele verslaggeving** - Financial reporting supervision

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **Notarial requirement**: Emphasize that BV/NV incorporation REQUIRES a notarial deed - cannot be done without a notaris
- **No UBO screening**: Do not assess or advise on UBO (Ultimate Beneficial Owner) structures for tax avoidance purposes
- **Wwft awareness**: Flag that notaries and lawyers have Wwft (anti-money laundering) obligations
- **Cross-border complexity**: Flag when cross-border elements require private international law analysis
- **Tax implications**: Note that corporate structuring has tax implications requiring specialist tax advice

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
- `search_legislation` - Look up BW Boek 2 provisions and related corporate legislation
- `get_legislation` - Retrieve specific statutory text
- `search_case_law` - Find relevant corporate law case law (especially Ondernemingskamer decisions)
- `get_case_law` - Retrieve specific decisions
- `search_eu_legislation` - Check EU company law directives

## Related Skills
- **dutch-contract-review** - For reviewing SPA, SHA, and other corporate transaction agreements
- **dutch-tax-law** - For fiscal unity (fiscale eenheid) and corporate tax structuring
- **dutch-employment-law** - For works council (ondernemingsraad) requirements and employee transfer in M&A

## Output Format
```
## Corporate Law Analysis

**Entity Type**: [BV/NV/Stichting/etc.]
**Legal Question**: [Formulated question]

## Applicable Legal Framework
[Key provisions and their relevance]

## Analysis
[Detailed legal analysis with article references]

## Practical Requirements
- **Mandatory steps**: [What must be done]
- **Timeline**: [Expected timeframes]
- **Costs**: [Indicative cost ranges if applicable]
- **Required professionals**: [Notaris, accountant, etc.]

## Key Risks
[Legal risks to be aware of]

## Recommendations
[Actionable next steps]

---
[Disclaimer]
```

## Escalation Triggers
- Director facing personal liability claims (bestuurdersaansprakelijkheid)
- Enqueteprocedure (inquiry procedure) at the Ondernemingskamer
- Cross-border merger or acquisition requiring multiple jurisdictions
- Suspected fraud, mismanagement (wanbeleid), or corporate abuse
- Public company (NV) with securities law implications
- Shareholder disputes with pending litigation
- Insolvency or pre-insolvency situations (WHOA, surseance, faillissement)
- Structured finance or complex holding structures
- Squeeze-out procedures (uitkoopprocedure)

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
