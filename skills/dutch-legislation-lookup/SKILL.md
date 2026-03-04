---
name: dutch-legislation-lookup
description: "Retrieve, explain, and contextualize Dutch legislation from BWB/CVDR databases. Use this skill whenever the user asks about Dutch laws, BW articles, wetgeving, statutes, Burgerlijk Wetboek provisions, or wants to look up specific articles of Dutch law."
---

# Dutch Legislation Lookup

## When to Use
- User asks about a specific Dutch law, article, or regulation
- User needs the text of a statutory provision
- User wants to understand how a Dutch law works or applies to their situation
- User asks about recent legislative changes
- User needs to compare current and previous versions of legislation
- User asks about municipal or provincial regulations (CVDR)

## Process
1. **Identify the legislation** - Determine which law/regulation the user is asking about
   - Map common names to formal titles (e.g., "Dutch GDPR" = Uitvoeringswet AVG; "employment law" = BW Boek 7 Titel 10)
   - Identify whether national (BWB) or local (CVDR) legislation
2. **Retrieve the text** - Use `search_legislation` or `get_legislation` with BWB identifier
3. **Identify the relevant articles** - Narrow down to specific provisions
4. **Explain in context**:
   a. Plain language explanation of the provision
   b. How it fits within the broader legislative framework
   c. Whether the provision is mandatory (dwingend recht) or default (regelend recht)
   d. Key case law interpreting the provision
   e. Any recent amendments or pending changes
5. **Cross-reference** - Check related provisions, implementing regulations, and EU source directives
6. **Append disclaimer**

## Key Legal Framework
- **Grondwet** - Dutch Constitution
- **Burgerlijk Wetboek (BW)** - Civil Code (Books 1-10)
- **Wetboek van Strafrecht (Sr)** - Criminal Code
- **Wetboek van Strafvordering (Sv)** - Code of Criminal Procedure
- **Wetboek van Burgerlijke Rechtsvordering (Rv)** - Code of Civil Procedure
- **Algemene wet bestuursrecht (Awb)** - General Administrative Law Act
- **Hierarchy of legislation**:
  1. EU law (treaties, regulations, directives)
  2. Grondwet (Constitution) - but note: no constitutional review of Acts of Parliament (Art. 120 Grondwet / toetsingsverbod)
  3. Wet in formele zin (Act of Parliament / Rijkswet)
  4. Algemene Maatregel van Bestuur (AMvB - Government Decree)
  5. Ministeriele regeling (Ministerial Regulation)
  6. Provinciale verordening (Provincial regulation)
  7. Gemeentelijke verordening (Municipal regulation)
- **Databases**:
  - wetten.overheid.nl (BWB - Basiswettenbestand)
  - lokaleregelgeving.overheid.nl (CVDR - Centrale Voorziening Decentrale Regelgeving)

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **Version accuracy**: Always specify which version of the law is being cited (geldend op datum)
- **No interpretation as advice**: Explain what the law says, but clarify that application to specific situations requires professional legal advice
- **Transitional law**: Flag when transitional provisions (overgangsrecht) may affect the application
- **Pending amendments**: Note any known pending legislative changes (wetsvoorstellen in behandeling bij Tweede/Eerste Kamer)
- **EU dimension**: Note when Dutch legislation implements EU directives and how this affects interpretation

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
- `search_legislation` - Search for legislation by keyword, title, or subject matter
- `get_legislation` - Retrieve specific legislation by BWB identifier
- `search_case_law` - Find judicial interpretation of specific provisions
- `search_eu_legislation` - Check underlying EU directives or regulations
- `get_eu_legislation` - Retrieve EU legislative text

## Related Skills
- **All other skills** - Legislation lookup is cross-cutting and supports every legal domain. Consider which substantive skill is most relevant to the user's legal question and cross-reference accordingly.

## Output Format
```
## Legislation Lookup

**Requested**: [What the user asked for]
**Legislation**: [Full formal title]
**BWB Identifier**: [BWBR/BWBV number if available]
**Status**: [In force / Amended / Repealed]
**Effective Date**: [Date of entry into force]

## Relevant Provisions

### Article [X]
**Text (Dutch)**:
> [Original Dutch text of the article]

**Translation/Explanation (English)**:
[Plain language explanation]

**Legal Context**:
- Type: [Dwingend recht / Regelend recht / Semi-dwingend recht]
- Part of: [Book/Title/Section within the broader law]
- Related provisions: [Cross-references]
- EU basis: [Implementing directive/regulation if applicable]

### Article [Y]
[Same format]

## Practical Application
[How this legislation typically applies in practice]

## Key Case Law
[Brief reference to leading judicial interpretations]

## Recent / Pending Changes
[Any amendments or proposals]

---
[Disclaimer]
```

## Escalation Triggers
- Legislation is ambiguous and there is no clear case law interpretation
- Multiple overlapping laws apply and the interaction is complex
- The user's situation involves conflict between Dutch and EU law
- Legislation has been recently amended and transitional provisions create uncertainty
- The question involves constitutional law or fundamental rights
- Local regulations (verordeningen) may conflict with national law
- The user needs to comply with legislation and faces regulatory enforcement risk

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
