---
name: dutch-privacy-gdpr
description: "AVG/UAVG compliance, DPIAs, data processing agreements, and Autoriteit Persoonsgegevens enforcement under Dutch law (Netherlands jurisdiction only). Use this skill whenever the user asks about Dutch GDPR, AVG, privacy compliance, data protection, verwerkersovereenkomst, data subject rights, cookie consent, or AP enforcement in the Netherlands. Do not use for GDPR questions about other EU countries."
---

# Dutch Privacy and GDPR

## When to Use
- User asks about GDPR compliance in the Netherlands (AVG/UAVG)
- User needs to assess whether a data processing activity is lawful
- User asks about data processing agreements (verwerkersovereenkomst)
- User needs guidance on conducting a DPIA (Data Protection Impact Assessment / Gegevensbeschermingseffectbeoordeling)
- User asks about data subject rights under Dutch law
- User asks about the Autoriteit Persoonsgegevens (AP) enforcement practice
- User asks about data breach notification obligations
- User asks about international data transfers (post-Schrems II)
- User asks about employee data processing, cookie compliance, or direct marketing

## Process
1. **Identify the processing activity** - What personal data, whose data, for what purpose
2. **Determine applicable framework** - AVG (GDPR), UAVG, sector-specific rules (e.g., Telecommunicatiewet for cookies/direct marketing)
3. **Assess lawfulness** - Identify the legal basis (Art. 6 AVG); for special categories (Art. 9 AVG) and criminal data (Art. 10 AVG/UAVG)
4. **Analyze compliance**:
   a. Legal basis adequacy
   b. Purpose limitation and data minimization
   c. Data subject rights implementation
   d. Security measures (Art. 32 AVG)
   e. Data processing agreements (Art. 28 AVG)
   f. International transfers (Chapter V AVG)
   g. DPIA requirement (Art. 35 AVG)
   h. Records of processing (Art. 30 AVG)
   i. DPO requirement (Art. 37 AVG)
5. **Provide recommendation** with specific article references
6. **Append disclaimer**

## Key Legal Framework
- **AVG** (Algemene Verordening Gegevensbescherming) - GDPR (Regulation (EU) 2016/679)
- **UAVG** (Uitvoeringswet AVG) - Dutch GDPR Implementation Act
- **Telecommunicatiewet (Tw)** - Art. 11.7a (cookie consent), Art. 11.7 (direct marketing)
- **Wet politiegegevens (Wpg)** - Processing of police data
- **Wet justitiele en strafvorderlijke gegevens (Wjsg)** - Criminal record data
- **EDPB Guidelines** - European Data Protection Board guidance (binding on AP)
- **AP Beleidsregels** - AP policy rules and guidance documents
- **Autoriteit Persoonsgegevens (AP)** - Dutch Data Protection Authority (supervisory authority under Art. 51 AVG)

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **No DPO replacement**: This tool does not replace a Data Protection Officer; recommend DPO consultation for complex processing
- **No legal basis selection**: Present options for legal basis but do not definitively select one - this requires factual assessment by the controller
- **Enforcement risk**: When AP enforcement risk is high, explicitly flag this
- **Data breach response**: If user describes an active data breach, emphasize the 72-hour notification deadline and recommend immediate action
- **International transfers**: Post-Schrems II transfers to third countries require careful assessment; flag complexity
- **Sector-specific rules**: Note when sector-specific data protection rules may apply (healthcare, finance, telecom)

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
- `search_legislation` - Look up AVG, UAVG, Telecommunicatiewet provisions
- `get_legislation` - Retrieve specific statutory text
- `search_case_law` - Find AP enforcement decisions and court rulings on privacy
- `get_case_law` - Retrieve specific decisions
- `search_eu_legislation` - Access GDPR text and related EU instruments
- `get_eu_legislation` - Retrieve specific EU legislative provisions

## Related Skills
- **dutch-employment-law** - For employee personal data processing and workplace monitoring
- **eu-law-integration** - For GDPR as an EU regulation and its direct applicability
- **dutch-criminal-law** - For Wwft (anti-money laundering) data processing obligations

## Output Format
```
## Privacy / GDPR Analysis

**Processing Activity**: [Description]
**Data Controller**: [Identified controller]
**Data Subjects**: [Categories of individuals]
**Personal Data**: [Types of data processed]

## Legal Basis Assessment
[Analysis of applicable legal basis under Art. 6 AVG]

## Compliance Analysis
### Lawfulness
[Legal basis, special categories, criminal data]

### Purpose and Data Minimization
[Assessment]

### Data Subject Rights
[Which rights apply, how to facilitate]

### Security
[Art. 32 requirements]

### Data Processing Agreements
[Whether Art. 28 agreements needed]

### International Transfers
[Transfer mechanisms if applicable]

### DPIA
[Whether required and key findings]

## Risk Assessment
[AP enforcement risk, key compliance gaps]

## Recommendations
1. [Prioritized action items]

---
[Disclaimer]
```

## Escalation Triggers
- Active data breach requiring 72-hour AP notification
- Large-scale systematic processing of sensitive data
- AP investigation or enforcement action underway
- Cross-border processing requiring lead supervisory authority determination
- Processing of children's data
- Profiling or automated decision-making with legal effects (Art. 22 AVG)
- Processing involving new technologies with high privacy risk
- Employee monitoring or surveillance questions
- International data transfer to countries without adequacy decision
- Whistleblower data or journalistic exemption questions

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
