---
name: dutch-case-law-research
description: "Search, retrieve, and analyze Dutch case law using ECLI identifiers and Rechtspraak.nl. Use this skill whenever the user asks about Dutch court decisions, jurisprudentie, rechtspraak, case law, ECLI numbers, Hoge Raad rulings, or wants to find legal precedents under Dutch law."
---

# Dutch Case Law Research

## When to Use
- User asks for relevant case law on a Dutch legal issue
- User provides an ECLI identifier and wants the case analyzed
- User needs to understand how courts have interpreted specific statutory provisions
- User wants to find precedents for a particular legal argument
- User asks about the current judicial interpretation of Dutch law

## Process
1. **Clarify the legal question** - Determine the specific legal issue, relevant area of law, and desired outcome
2. **Identify search parameters** - Determine relevant:
   - Area of law (rechtsgebied)
   - Time period
   - Court level (Rechtbank, Gerechtshof, Hoge Raad)
   - Specific statutory provisions
   - Key legal concepts (rechtstermen)
3. **Execute search** - Use `search_case_law` with Dutch legal terminology for best results
4. **Validate ECLI identifiers** - Ensure ECLI format is correct (ECLI:NL:COURT:YEAR:ID)
5. **Retrieve and analyze** - For each relevant case:
   a. Retrieve full text via `get_case_law`
   b. Identify the legal issue (rechtsvraag)
   c. Extract the court's reasoning (overwegingen)
   d. Note the decision (beslissing/dictum)
   e. Assess precedential value based on court level
6. **Synthesize findings** - Organize results by relevance and authority
7. **Append disclaimer**

## Key Legal Framework
- **Wet op de rechterlijke organisatie (Wet RO)** - Organization of the judiciary
- **Wetboek van Burgerlijke Rechtsvordering (Rv)** - Code of Civil Procedure
- **Algemene wet bestuursrecht (Awb)** - General Administrative Law Act (for administrative case law)
- **Court hierarchy**:
  - Hoge Raad der Nederlanden (Supreme Court - cassation only)
  - Gerechtshoven (Courts of Appeal - 4 districts)
  - Rechtbanken (District Courts - 11 districts)
  - Specialized courts: CBb, CRvB, ABRvS (administrative)
- **ECLI system**: European Case Law Identifier - standardized citation format
- **Rechtspraak.nl**: Official publication platform for Dutch case law

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer that this is not legal advice
- **Citation accuracy**: Only cite cases that have been actually retrieved and verified; never fabricate ECLI numbers
- **Precedential value**: Always note the court level and explain the weight of the decision (Hoge Raad decisions are binding precedent; lower court decisions are persuasive only)
- **Publication bias**: Note that not all decisions are published on Rechtspraak.nl; absence of case law does not mean absence of judicial practice
- **Currency**: Flag if case law may be outdated due to subsequent legislative changes
- **Anonymization**: Respect that published Dutch case law is anonymized; do not attempt to identify parties

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
- `search_case_law` - Search Rechtspraak.nl by keywords, legal area, court, date range
- `get_case_law` - Retrieve full case text by ECLI identifier
- `search_legislation` - Find statutory provisions referenced in cases
- `get_legislation` - Retrieve legislative text for cross-reference

## Related Skills
- **All other skills** - Case law research is cross-cutting and supports every legal domain. Consider which substantive skill is most relevant to the user's legal question and cross-reference accordingly.

## Output Format
```
## Case Law Research Results

**Legal Question**: [Formulated legal question]
**Search Terms**: [Dutch terms used]
**Scope**: [Courts, time period, legal area]

## Key Findings

### Leading Case(s)
#### [Case Title / Short Description]
- **ECLI**: [ECLI:NL:COURT:YEAR:ID]
- **Court**: [Full court name]
- **Date**: [Decision date]
- **Legal Issue**: [Core legal question addressed]
- **Key Holding**: [Court's main conclusion]
- **Relevant Paragraphs**: [r.o. numbers]
- **Precedential Value**: [Binding/Persuasive]

### Supporting Cases
[Same format, briefer analysis]

## Legal Analysis
[Synthesis of case law findings answering the user's question]

## Trend / Development
[Any observable trend in judicial interpretation]

## Limitations
[Publication bias, pending cases, legislative changes]

---
[Disclaimer]
```

## Escalation Triggers
- Conflicting case law from same or different court levels with no Hoge Raad resolution
- Pending prejudicial questions (prejudiciele vragen) to the Hoge Raad or CJEU on the relevant issue
- Case involves fundamental rights (ECHR implications) requiring specialized constitutional analysis
- User needs to file an actual court procedure based on the research
- Legal question involves very recent legislative changes not yet interpreted by courts
- Criminal case law research where the user may be a suspect or defendant

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
