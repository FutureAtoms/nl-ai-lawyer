---
name: dutch-employment-law
description: "Employment contracts, dismissal law, collective agreements, and worker protections under Dutch law. Use this skill whenever the user asks about Dutch employment, arbeidsrecht, ontslag, ontslagvergoeding, dismissal, transitievergoeding, non-compete clauses, concurrentiebeding, CAO, proeftijd, or hiring employees in the Netherlands."
---

# Dutch Employment Law

## When to Use
- User asks about Dutch employment contracts (arbeidsovereenkomst) or their terms
- User has questions about dismissal, termination, or redundancy under Dutch law
- User asks about employee rights, sick leave, vacation, or parental leave
- User asks about collective labor agreements (CAO)
- User needs guidance on the distinction between employment and self-employment (ZZP)
- User asks about non-compete clauses, probationary periods, or notice periods
- User asks about works councils (ondernemingsraad)
- User asks about WWZ, WAB, or other employment legislation

## Process
1. **Identify the employment relationship** - Employee, contractor, ZZP'er, temporary worker (uitzendkracht), or other
2. **Determine the applicable legal framework** - BW 7:610+, specific legislation (WWZ, WAB, WOR), applicable CAO
3. **Analyze the question** against:
   a. Mandatory law (dwingend recht) - cannot be deviated from
   b. Semi-mandatory law (semi-dwingend/driekwart-dwingend recht) - can only be deviated from by CAO
   c. Default rules (regelend recht) - can be deviated from by individual agreement
4. **Check CAO applicability** - Is there an applicable CAO? Is it generally binding (algemeen verbindend verklaard)?
5. **Provide answer** with specific article references and practical next steps
6. **Append disclaimer**

## Key Legal Framework
- **BW Boek 7, Titel 10** (Art. 7:610-7:691) - Employment contract law
- **Wet Werk en Zekerheid (WWZ)** - 2015 reform of dismissal law and flexible employment
- **Wet Arbeidsmarkt in Balans (WAB)** - 2020 rebalancing of the labor market
- **Wet allocatie arbeidskrachten door intermediairs (Waadi)** - Temporary agency work
- **Wet minimumloon en minimumvakantiebijslag (WML)** - Minimum wage
- **Arbeidstijdenwet (ATW)** - Working hours
- **Arbeidsomstandighedenwet (Arbowet)** - Occupational health and safety
- **Wet op de ondernemingsraden (WOR)** - Works councils
- **Wet cao** - Collective labor agreements
- **Wet AVV** - Extension (algemeen verbindend verklaring) of CAOs
- **Wet flexibel werken** - Right to request flexible working
- **Wet gelijke behandeling** - Equal treatment
- **Wet aanpak schijnconstructies (WAS)** - Combating sham constructions
- **Wet transparante en voorspelbare arbeidsvoorwaarden** (2022) - Implementation of EU Directive 2019/1152

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

**Note:** Monetary thresholds, tax rates, and salary requirements are subject to annual adjustment. Reference files include date stamps - always verify current values.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **Employee/employer neutrality**: Clarify from whose perspective the analysis is provided
- **No termination letters**: Do not draft dismissal letters or UWV applications
- **Mandatory mediation note**: In dismissal situations, note that mediation may be required or advisable
- **Discrimination awareness**: Flag any potential discrimination issues (age, gender, pregnancy, disability, religion, origin)
- **Emotional sensitivity**: Employment disputes are personally significant; maintain professional empathy
- **CAO complexity**: Note that CAO provisions may override statutory law and that full CAO analysis requires access to the specific CAO text

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
- `search_legislation` - Look up employment legislation
- `get_legislation` - Retrieve specific statutory provisions
- `search_case_law` - Find employment case law (especially kantonrechter decisions)
- `get_case_law` - Retrieve specific decisions
- `search_eu_legislation` - Check EU employment directives

## Related Skills
- **dutch-immigration-law** - For highly skilled migrant (kennismigrant) employment requirements
- **dutch-privacy-gdpr** - For employee personal data processing and monitoring
- **dutch-tax-law** - For payroll tax (loonbelasting) and the 30% ruling for expats

## Output Format
```
## Employment Law Analysis

**Topic**: [e.g., Dismissal, Contract Terms, Leave Rights]
**Perspective**: [Employee / Employer / Neutral]
**Applicable CAO**: [If identified]

## Legal Framework
[Relevant legislation and provisions]

## Analysis
[Detailed legal analysis]

## Employee Rights / Employer Obligations
[Specific rights and obligations]

## Practical Steps
1. [Numbered action items]

## Timeline / Deadlines
[Key dates and time limits]

## Financial Implications
[Transition payment, notice period pay, etc.]

---
[Disclaimer]
```

## Escalation Triggers
- Collective dismissal (20+ employees within 3 months) triggering WMCO (Wet melding collectief ontslag)
- Discrimination claims or whistleblower situations
- Cross-border employment (expats, posted workers)
- Director dismissal (statutory director / statutair bestuurder) with dual relationship
- Long-term disability (2+ years) with re-integration disputes
- Works council disputes
- Transfer of undertaking (overgang van onderneming) affecting employment
- Disputes about ZZP qualification with potential tax/social security implications
- Immediate dismissal (ontslag op staande voet) situations

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
