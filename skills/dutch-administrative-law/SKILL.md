---
name: dutch-administrative-law
description: "AWB procedures, objection and appeal against government decisions, government liability. Use this skill whenever the user asks about Dutch administrative law, bezwaar, beroep, omgevingsvergunning, building permits, government decisions, bestuursrecht, or Awb procedures."
---

# Dutch Administrative Law

## When to Use
- User receives a government decision (besluit) and wants to challenge it
- User asks about the objection (bezwaar) or appeal (beroep) procedure
- User asks about government liability for unlawful decisions
- User asks about permits, subsidies, or other administrative decisions
- User asks about enforcement actions by administrative bodies (handhaving)
- User asks about the Algemene wet bestuursrecht (AWB) framework
- User asks about specific administrative law areas (spatial planning, environmental law, social security)

## Process
1. **Identify the administrative body** - Which government body issued the decision
2. **Identify the decision type** - Is it a besluit in the sense of Art. 1:3 Awb?
3. **Determine standing** - Is the user an interested party (belanghebbende, Art. 1:2 Awb)?
4. **Check time limits** - Is the user still within the 6-week bezwaar/beroep period?
5. **Analyze the legal basis** - Which law authorizes the decision?
6. **Assess grounds for challenge** - Procedural defects, factual errors, legal errors, proportionality
7. **Advise on procedure** - Bezwaar, beroep, hoger beroep, or voorlopige voorziening
8. **Append disclaimer**

## Key Legal Framework
- **Algemene wet bestuursrecht (Awb)** - General Administrative Law Act:
  - Chapter 1: Definitions
  - Chapter 2: Relations between citizens and administrative bodies
  - Chapter 3: General provisions on decisions (besluiten)
  - Chapter 4: Special provisions (subsidies, administrative fines)
  - Chapter 6: General provisions on objection and appeal
  - Chapter 7: Bezwaar (objection) procedure
  - Chapter 8: Beroep (appeal to court) procedure
- **Wet openbaarheid van bestuur (Wob) / Wet open overheid (Woo)** - Government Transparency Act
- **Omgevingswet** (2024) - Environmental and Planning Act
- **Vreemdelingenwet 2000** - Aliens Act (immigration decisions)
- **Participatiewet** - Social assistance
- **Courts**: Rechtbank (bestuursrechter), ABRvS, CRvB, CBb (see court-hierarchy.md)
- **General principles of good governance** (Algemene beginselen van behoorlijk bestuur - ABBB)

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **Time limits are fatal**: Emphasize that missing the 6-week deadline is almost always fatal; recommend immediate action if deadline is approaching
- **Complexity warning**: Administrative law intersects with many specialized fields; flag when sector-specific expertise is needed
- **Voorlopige voorziening**: If the decision has immediate irreversible effects, flag the option for provisional measures
- **No drafting**: Do not draft bezwaarschriften or beroepschriften; provide analysis only
- **Legal aid**: Mention possible eligibility for government-funded legal aid (gesubsidieerde rechtsbijstand / toevoeging)

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
- `search_legislation` - Look up Awb and specific administrative legislation
- `get_legislation` - Retrieve specific statutory text
- `search_case_law` - Find administrative case law (ABRvS, CRvB, CBb)
- `get_case_law` - Retrieve specific administrative decisions

## Related Skills
- **dutch-real-estate-law** - For environmental permits (omgevingsvergunning) and spatial planning decisions
- **dutch-criminal-law** - For administrative vs. criminal enforcement (bestuursrechtelijke vs strafrechtelijke handhaving)

## Output Format
```
## Administrative Law Analysis

**Decision**: [Description of the challenged decision]
**Administrative Body**: [Which body issued it]
**Legal Basis**: [Statutory provision authorizing the decision]
**Date of Decision**: [If known]
**Deadline**: [6-week bezwaar/beroep deadline]

## Standing Analysis
[Is the user an interested party?]

## Grounds for Challenge
[Procedural, factual, and legal grounds]

## Procedure
[Which procedure to follow and key steps]

## Practical Steps
1. [Immediate actions]
2. [Preparation steps]
3. [What to include in bezwaar/beroep]

## Provisional Measures
[Whether voorlopige voorziening is advisable]

---
[Disclaimer]
```

## Escalation Triggers
- Bezwaar/beroep deadline is within days (urgent)
- Government enforcement action (bestuursdwang, last onder dwangsom) with immediate effect
- Decisions with irreversible consequences requiring voorlopige voorziening
- Criminal prosecution by administrative body (bestuurlijke boete vs. strafrechtelijke vervolging)
- Expropriation (onteigening) or compulsory acquisition
- Large financial impact (subsidy recovery, administrative fines > EUR 100,000)
- Systemic government misconduct (institutionele bias) requiring political/ombudsman route
- Cross-border administrative decisions (EU mutual recognition)

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
