---
name: eu-law-integration
description: "EU law supremacy in the Netherlands, directives implementation, CJEU preliminary rulings, and interaction between EU and Dutch legal orders. Use this skill whenever the user asks about EU law in the Netherlands, direct effect, directives implementation, CJEU, preliminary rulings, or EU-Dutch legal relationship."
---

# EU Law Integration in the Netherlands

## When to Use
- User asks about the relationship between EU law and Dutch national law
- User asks whether an EU regulation or directive applies in the Netherlands
- User asks about direct effect of EU law provisions
- User asks about challenging Dutch legislation on EU law grounds
- User asks about preliminary references to the CJEU (prejudiciele verwijzing)
- User asks about implementation of EU directives in Dutch law
- User asks about state liability for breach of EU law (Francovich)
- User asks about the role of Art. 93/94 Grondwet in applying international/EU law
- User asks about specific EU regulations and their Dutch application

## Process
1. **Identify the EU law source** - Determine which EU instrument is relevant (Treaty provision, regulation, directive, decision, or general principle)
2. **Determine the nature of the provision** - Is it directly effective? Does it have horizontal or only vertical direct effect?
3. **Check Dutch implementation** - If a directive: has it been properly transposed? What is the implementing legislation?
4. **Analyze the interaction** - Apply the hierarchy: primacy, direct effect, consistent interpretation, or state liability as appropriate
5. **Search relevant CJEU case law** - Find preliminary rulings and Dutch court applications
6. **Check Dutch court practice** - How have Dutch courts (Hoge Raad, ABRvS, CRvB, CBb) applied the EU provision?
7. **Provide practical guidance** - Explain consequences for the user's situation
8. **Append disclaimer**

## Key Legal Framework

### EU Treaties
- **TEU (Treaty on European Union)** - Institutional framework, fundamental values (Art. 2), objectives (Art. 3), principles of conferral, subsidiarity, proportionality (Art. 5)
- **TFEU (Treaty on the Functioning of the European Union)** - Substantive rules: free movement (Arts. 28-66), competition (Arts. 101-109), state aid (Arts. 107-109), approximation of laws (Arts. 114-118)
- **EU Charter of Fundamental Rights** - Binding since Lisbon Treaty; applies when Member States implement EU law (Art. 51 Charter)

### EU Legal Instruments (Art. 288 TFEU)
- **Regulations (Verordeningen)** - Directly applicable in all Member States; no implementation required; create rights and obligations for individuals
- **Directives (Richtlijnen)** - Binding as to result; Member States choose form and methods of implementation; transposition deadline applies
- **Decisions (Besluiten)** - Binding on those to whom addressed; may be addressed to Member States, companies, or individuals
- **Recommendations and Opinions** - Not binding but may have interpretive value

### Foundational CJEU Case Law
- **Van Gend en Loos (C-26/62)** - Direct effect: EU law creates rights for individuals enforceable in national courts
- **Costa v ENEL (C-6/64)** - Primacy/supremacy: EU law prevails over conflicting national law, including later national legislation
- **Internationale Handelsgesellschaft (C-11/70)** - EU law prevails even over national constitutional provisions
- **Simmenthal (C-106/77)** - National courts must set aside conflicting national law of their own motion
- **Von Colson (C-14/83)** - Duty of consistent interpretation (richtlijnconforme interpretatie)
- **Marleasing (C-106/89)** - Consistent interpretation applies to all national law, not just implementing measures
- **Francovich (C-6/90 and C-9/90)** - State liability for failure to implement a directive
- **Brasserie du Pecheur/Factortame III (C-46/93 and C-48/93)** - Conditions for state liability: sufficiently serious breach
- **Mangold (C-144/04)** - General principles of EU law may have horizontal direct effect

### Dutch Constitutional Framework
- **Art. 90 Grondwet** - Government promotes development of international legal order
- **Art. 91 Grondwet** - Treaties require parliamentary approval
- **Art. 93 Grondwet** - Provisions of treaties and decisions of international organizations which may be binding on all persons (een ieder verbindend) have binding force after publication
- **Art. 94 Grondwet** - Statutory regulations in force within the Kingdom shall not be applied if such application is in conflict with provisions of treaties or decisions binding on all persons (een ieder verbindende bepalingen)
- Note: The Netherlands has a **monist** tradition - international law does not require separate transformation into national law

### Dutch Implementation Practice
- Directives typically implemented via: formal legislation (wet), governmental decree (AMvB), or ministerial regulation (ministeriele regeling)
- Transposition tracked by the Ministry responsible for the subject matter
- Late or incorrect implementation: individuals may invoke the directive directly against the state (vertical direct effect after transposition deadline)
- **Richtlijnconforme interpretatie**: Dutch courts are obliged to interpret national law in conformity with EU directives, insofar as possible

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## MCP Tools to Use
- `eurlex_search_regulations` - Search EUR-Lex for EU legislation by keyword, subject, date
- `eurlex_get_act` - Retrieve the full text of a specific EU regulation, directive, or decision by CELEX number
- `legislation_search` - Search Dutch legislation for implementing measures
- `legislation_get_article` - Retrieve specific articles of Dutch implementing legislation
- `caselaw_search_rechtspraak` - Search Dutch case law for application of EU law principles
- `caselaw_get_decision` - Retrieve specific Dutch court decisions applying EU law

## Related Skills
- **dutch-privacy-gdpr** - For AVG (GDPR) as directly applicable EU regulation
- **dutch-ip-law** - For EU IP directives and their Dutch implementation
- **dutch-tax-law** - For EU tax directives (Parent-Subsidiary, ATAD, DAC6)

## Output Format
```
## EU Law Analysis

**EU Instrument**: [Regulation/Directive/Treaty Article number]
**Subject Matter**: [Brief description]
**Dutch Implementation**: [Implementing legislation if applicable]

## Applicable EU Law
[Relevant provisions and their effect]

## Interaction with Dutch Law
[How the EU provision relates to Dutch national law]

## Direct Effect Analysis
[Whether the provision has direct effect; vertical/horizontal]

## Relevant Case Law
- **CJEU**: [Key preliminary rulings]
- **Dutch courts**: [Key national decisions]

## Practical Consequences
[What this means for the user's situation]

---
[Disclaimer]
```

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **EU law complexity**: Emphasize that EU law questions often require specialized expertise; general guidance only
- **Implementation accuracy**: Verify that Dutch implementing legislation cited is current and correctly transposed

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

## Escalation Triggers
- State aid questions requiring European Commission notification (Art. 108 TFEU)
- Pending infringement proceedings against the Netherlands (Art. 258 TFEU)
- Questions requiring a preliminary reference to the CJEU (Art. 267 TFEU)
- Complex interaction between EU law and Dutch constitutional law
- EU competition law matters involving market-dominant undertakings
- Cross-border enforcement of EU judgments
- EU sanctions law and restrictive measures
- Complex EU public procurement disputes (above EU thresholds)
- EU data protection issues requiring coordination with European Data Protection Board

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
