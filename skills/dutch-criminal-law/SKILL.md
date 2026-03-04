---
name: dutch-criminal-law
description: "Criminal code, economic criminal law, corporate criminal liability, and criminal procedure under Dutch law. Use this skill whenever the user asks about Dutch criminal law, strafrecht, FIOD, corporate criminal liability, environmental crimes, valsheid in geschrift, or WED offenses."
---

# Dutch Criminal Law

## When to Use
- User asks about criminal offenses under Dutch law
- User asks about criminal procedure (arrest, investigation, trial)
- User asks about economic or financial crimes (WED, fraud, money laundering)
- User asks about corporate criminal liability
- User asks about rights of suspects/defendants (verdachten)
- User asks about penalties, sentencing, or criminal records
- User asks about the intersection of criminal and administrative enforcement

## Process
1. **Identify the offense category** - Misdrijf (felony) or overtreding (misdemeanor)
2. **Determine applicable law** - Wetboek van Strafrecht, WED, Opiumwet, or special legislation
3. **Assess elements of the offense** - Objective elements (bestanddelen) and subjective elements (opzet/schuld)
4. **Consider defenses** - Justification (rechtvaardigingsgronden) and excuses (schulduitsluitingsgronden)
5. **Identify procedural aspects** - Investigation powers, rights of the suspect, trial procedure
6. **Provide general information** - Always note this is general information, not defense strategy
7. **Append disclaimer**

## Key Legal Framework
- **Wetboek van Strafrecht (Sr)** - Criminal Code
  - Boek 1: Algemene bepalingen (General provisions)
  - Boek 2: Misdrijven (Felonies)
  - Boek 3: Overtredingen (Misdemeanors)
- **Wetboek van Strafvordering (Sv)** - Code of Criminal Procedure
- **Wet op de Economische Delicten (WED)** - Economic Offenses Act
- **Opiumwet** - Drugs Act
- **Wet wapens en munitie (WWM)** - Weapons and Ammunition Act
- **Wegenverkeerswet 1994 (WVW)** - Road Traffic Act
- **Wet witwassen** - Money laundering (Art. 420bis-420quater Sr)
- **Wwft** - Anti-Money Laundering and Terrorist Financing Act (administrative/preventive)
- **EU Directives** - Framework decisions and directives on criminal law
- **ECHR** - European Convention on Human Rights (fair trial rights)
- **Courts**: Rechtbank (politierechter/meervoudige strafkamer), Gerechtshof, Hoge Raad

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **Not a defense lawyer**: This system does NOT provide criminal defense advice; always recommend engaging a strafrechtadvocaat
- **Right to counsel**: Emphasize the suspect's right to a lawyer before police questioning (Salduz rights)
- **Presumption of innocence**: Respect the presumption of innocence in all analysis
- **No confession advice**: Never advise to confess, deny, or adopt any specific defense strategy
- **Victim sensitivity**: If the query relates to victimization, provide information on victim rights (Slachtofferhulp Nederland)
- **Minors**: Flag special procedures for juvenile criminal law (jeugdstrafrecht)
- **Self-incrimination**: Do not assist in concealing criminal activity

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
- `search_legislation` - Look up criminal legislation
- `get_legislation` - Retrieve specific criminal provisions
- `search_case_law` - Find criminal case law (Hoge Raad strafkamer)
- `get_case_law` - Retrieve specific criminal decisions

## Related Skills
- **dutch-corporate-law** - For corporate criminal liability (rechtspersoon als dader)
- **dutch-administrative-law** - For administrative enforcement and una via principle
- **dutch-privacy-gdpr** - For Wwft (anti-money laundering) obligations and data processing

## Output Format
```
## Criminal Law Analysis

**Topic**: [Offense/Procedure/Rights]
**Applicable Law**: [Sr/WED/Special legislation]

## Legal Framework
[Relevant provisions and their application]

## Elements of the Offense (if applicable)
- Objective elements (bestanddelen)
- Subjective element (opzet/schuld)
- Possible defenses

## Procedure
[Relevant procedural information]

## Rights of the Suspect
[Key rights to be aware of]

## Penalties (if applicable)
[Maximum penalties and sentencing guidelines]

## IMPORTANT: Legal Representation
[Strong recommendation to engage a criminal defense lawyer]

---
[Disclaimer]
```

## Escalation Triggers
- User is a suspect or has been arrested (immediate lawyer referral)
- Criminal investigation is ongoing (recommend silence and lawyer)
- Corporate criminal liability for the user's company
- Cross-border criminal matters (EAW, mutual legal assistance)
- Serious offenses (life imprisonment eligible, organized crime, terrorism)
- Juvenile criminal law (minors involved)
- Intersection of criminal and regulatory enforcement (ne bis in idem / una via issues)
- Victim of crime seeking damages (voegen als benadeelde partij)
- Extradition or international cooperation requests

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
