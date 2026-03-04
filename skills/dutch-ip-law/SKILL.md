---
name: dutch-ip-law
description: "Copyright, patents, Benelux trademarks, trade secrets, and other IP rights under Dutch and Benelux law. Use this skill whenever the user asks about Dutch intellectual property, auteursrecht, copyright ownership, trademark registration, BOIP, patent law, trade secrets, or Wet bescherming bedrijfsgeheimen."
---

# Dutch Intellectual Property Law

## When to Use
- User asks about copyright protection or ownership in the Netherlands (Auteurswet)
- User asks about patent rights or applications (Rijksoctrooiwet)
- User asks about Benelux or EU trademark registration or infringement (BVIE)
- User asks about trade name protection (Handelsnaamwet)
- User asks about trade secrets (Wet bescherming bedrijfsgeheimen)
- User asks about IP ownership in employment or contractor relationships
- User asks about IP licensing or assignment
- User asks about IP enforcement or infringement proceedings

## Process
1. **Identify the IP right(s) involved** - Copyright, patent, trademark, design, trade name, trade secret, or database right
2. **Determine the territorial scope** - Dutch, Benelux, EU, or international
3. **Analyze the legal question**:
   a. For creation/registration: check requirements for protection
   b. For ownership: apply the relevant ownership rules (employee, contractor, commissioner)
   c. For infringement: assess the scope of protection and alleged infringement
   d. For licensing/assignment: check formal requirements (akte for copyright, registration for patents/trademarks)
4. **Research relevant case law** - Dutch IP case law is extensive and fact-specific
5. **Provide practical guidance** - Registration options, enforcement strategies, risk assessment
6. **Append disclaimer**

## Key Legal Framework
- **Auteurswet (Aw)** - Copyright Act (1912, frequently amended)
- **Rijksoctrooiwet 1995 (ROW)** - Patent Act
- **Benelux-Verdrag inzake de Intellectuele Eigendom (BVIE)** - Benelux Convention on Intellectual Property (trademarks and designs)
- **EU Trademarks Regulation** (Regulation (EU) 2017/1001) - EUTM via EUIPO
- **Handelsnaamwet (Hw)** - Trade Name Act
- **Wet bescherming bedrijfsgeheimen (Wbb)** - Trade Secrets Act (implementing EU Directive 2016/943)
- **Databankenwet** - Database Act (implementing EU Directive 96/9/EC)
- **Wet op de naburige rechten (WNR)** - Neighboring Rights Act (performers, producers)
- **Chipswet** - Semiconductor Topography Act
- **European Patent Convention (EPC)** - European patent applications via EPO
- **Courts**: Rechtbank Den Haag has exclusive jurisdiction for patent and EU trademark cases; all Rechtbanken for copyright

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **No registration filing**: Do not file or prepare patent, trademark, or design applications; recommend a patent/trademark attorney (octrooigemachtigde/merkengemachtigde)
- **Prior art caveat**: Patent analysis is limited; a freedom-to-operate or patentability analysis requires professional search
- **Enforcement complexity**: IP infringement cases are fact-intensive; provide general analysis only
- **Confidentiality**: Remind users that sharing unpublished inventions may affect patentability (novelty requirement)
- **International scope**: Flag when protection extends beyond NL/Benelux/EU jurisdictions

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
- `search_legislation` - Look up IP legislation provisions
- `get_legislation` - Retrieve specific statutory text
- `search_case_law` - Find IP case law
- `get_case_law` - Retrieve specific IP decisions
- `search_eu_legislation` - Check EU IP regulations and directives

## Related Skills
- **dutch-contract-review** - For IP clauses in commercial agreements
- **dutch-employment-law** - For employer IP ownership and employee inventions
- **eu-law-integration** - For EU IP directives and their Dutch implementation

## Output Format
```
## IP Law Analysis

**IP Right(s)**: [Copyright/Patent/Trademark/etc.]
**Territorial Scope**: [NL/Benelux/EU/International]
**Legal Question**: [Formulated question]

## Applicable Legal Framework
[Relevant legislation and provisions]

## Analysis
[Detailed legal analysis with article references]

## Protection Status
[Whether/how the IP is protected]

## Ownership
[Who owns the IP right]

## Practical Recommendations
1. [Registration steps if applicable]
2. [Enforcement options if applicable]
3. [Risk mitigation]

---
[Disclaimer]
```

## Escalation Triggers
- Patent infringement or freedom-to-operate analysis requiring professional patent search
- Trademark opposition or cancellation proceedings at BOIP or EUIPO
- Cross-border IP enforcement requiring multi-jurisdiction coordination
- IP valuation for transactions or financial reporting
- Standard-essential patents (SEP) and FRAND licensing disputes
- Software patent or AI-generated works questions (rapidly evolving law)
- IP in bankruptcy (how IP rights are treated in insolvency)
- Compulsory licensing questions
- IP disputes involving preliminary injunctions (kort geding)

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
