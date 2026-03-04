---
name: gdpr-check
description: AVG/GDPR compliance assessment
arguments:
  - name: processing
    description: Description of data processing activity
    required: true
  - name: scope
    description: quick or full assessment
    required: false
---

# AVG/GDPR Compliance Assessment

Assess a data processing activity against the Dutch implementation of the GDPR (AVG -- Algemene Verordening Gegevensbescherming) and UAVG (Uitvoeringswet AVG).

## Skill and Tools

Use skill: **dutch-privacy-gdpr**

Use MCP tools:
- `legislation_search` -- to look up AVG/UAVG provisions
- `caselaw_search_rechtspraak` -- to find relevant AP (Autoriteit Persoonsgegevens) decisions and court rulings
- `legislation_fetch` -- to retrieve specific articles of the AVG/UAVG

## Workflow

### Step 1: Scope Determination

- If `scope` is "quick": perform a rapid assessment focusing on the most critical compliance areas
- If `scope` is "full" or not specified: perform a comprehensive assessment covering all areas below
- Parse the `processing` description to identify: what data, whose data, why, how, where, who has access

### Step 2: Data Processing Inventory

Establish the facts:

```
### Processing Activity Overview

| Element | Details |
|---------|---------|
| **Data Controller (Verwerkingsverantwoordelijke)** | [identified or to be confirmed] |
| **Data Processor (Verwerker)** | [if applicable] |
| **Categories of Data Subjects** | [e.g., customers, employees, website visitors] |
| **Categories of Personal Data** | [list all data types] |
| **Special Categories (Bijzondere persoonsgegevens)** | [health, biometric, genetic, racial/ethnic, political, religious, trade union, sexual orientation, criminal records] |
| **Purpose(s) of Processing** | [specific, explicit, legitimate purposes] |
| **Processing Operations** | [collection, storage, use, sharing, deletion, etc.] |
| **Recipients** | [who receives the data] |
| **International Transfers** | [any transfers outside EEA] |
| **Retention Period** | [how long data is kept] |
| **Automated Decision-Making** | [any profiling or automated decisions under art. 22 AVG] |
```

### Step 3: Legal Basis Assessment (Art. 6 AVG)

Evaluate which legal basis applies:

1. **Consent (Toestemming)** -- art. 6(1)(a) AVG
   - Is consent freely given, specific, informed, and unambiguous?
   - Can it be withdrawn as easily as given?
   - Is there a power imbalance (e.g., employer-employee)?

2. **Contract Performance (Uitvoering overeenkomst)** -- art. 6(1)(b) AVG
   - Is processing necessary for contract performance?
   - Is processing necessary for pre-contractual steps?

3. **Legal Obligation (Wettelijke verplichting)** -- art. 6(1)(c) AVG
   - Which specific Dutch law requires this processing?

4. **Vital Interests (Vitale belangen)** -- art. 6(1)(d) AVG
   - Only applicable in life-or-death situations

5. **Public Task (Algemeen belang / openbaar gezag)** -- art. 6(1)(e) AVG
   - Is there a basis in Dutch law for this public task?

6. **Legitimate Interest (Gerechtvaardigd belang)** -- art. 6(1)(f) AVG
   - Three-part test: (1) legitimate interest, (2) necessity, (3) balancing test
   - Note: not available for public authorities in their core tasks

For special categories (art. 9 AVG), assess the additional legal basis required.
For criminal data (art. 10 AVG / art. 31-32 UAVG), check Dutch-specific requirements.

### Step 4: Key Compliance Areas

Assess each area and flag as COMPLIANT / NEEDS ATTENTION / NON-COMPLIANT:

#### A. Data Minimization (art. 5(1)(c) AVG)
- Is only necessary data collected?
- Could the purpose be achieved with less data?

#### B. Purpose Limitation (art. 5(1)(b) AVG)
- Are purposes specific, explicit, and legitimate?
- Any risk of function creep?

#### C. Storage Limitation (art. 5(1)(e) AVG)
- Is a retention period defined?
- Is it justified and documented?
- Are there deletion procedures?

#### D. Transparency and Information Obligations (art. 13-14 AVG)
- Is a privacy notice provided?
- Does it contain all required elements?
- Is it in clear, plain language?

#### E. Data Subject Rights (art. 15-22 AVG)
- Access (inzage) -- art. 15
- Rectification (rectificatie) -- art. 16
- Erasure (wissen / recht op vergetelheid) -- art. 17
- Restriction (beperking) -- art. 18
- Data portability (overdraagbaarheid) -- art. 20
- Objection (bezwaar) -- art. 21
- Automated decision-making rights -- art. 22
- Are procedures in place to handle these requests within 1 month?

#### F. Data Protection Impact Assessment (DPIA / Gegevensbeschermingseffectbeoordeling)
- Is a DPIA required? Check against:
  - AP's list of processing activities requiring DPIA
  - Art. 35 AVG criteria (systematic monitoring, large-scale special categories, etc.)
  - WP29/EDPB guidelines
- If required, has it been conducted?

#### G. International Transfers (art. 44-49 AVG)
- Are there transfers outside the EEA?
- What transfer mechanism is used? (adequacy decision, SCCs, BCRs, derogations)
- Post-Schrems II considerations for US transfers
- EU-US Data Privacy Framework applicability

#### H. Verwerkersovereenkomst (Data Processing Agreement) -- art. 28 AVG
- If a processor is involved, is there a written verwerkersovereenkomst?
- Does it contain all mandatory elements of art. 28(3) AVG?
  - Subject-matter and duration
  - Nature and purpose of processing
  - Types of personal data and categories of data subjects
  - Controller's obligations and rights
  - Processor's confidentiality obligations
  - Security measures
  - Sub-processor approval and flow-down requirements
  - Assistance with data subject rights
  - Deletion/return obligations
  - Audit rights

#### I. Security (art. 32 AVG)
- Are appropriate technical and organizational measures in place?
- Consider: pseudonymization, encryption, access controls, backup, testing

#### J. Data Breach Procedures (art. 33-34 AVG)
- Is there a procedure for detecting and reporting breaches?
- Notification to AP within 72 hours
- Notification to data subjects when high risk
- Is the AP notification portal known?

### Step 5: Dutch-Specific Requirements (UAVG)

Check requirements specific to the Dutch implementation:
- BSN (Burgerservicenummer) processing restrictions (art. 46 UAVG)
- National identification number usage
- Healthcare data processing (art. 30 UAVG)
- Employment context processing (art. 29-30 UAVG)
- Exemptions for journalistic, academic, artistic, literary purposes
- Age of consent for children: 16 years in the Netherlands (art. 8 AVG, art. 5 UAVG)

### Step 6: Assessment Summary

```
## AVG/GDPR Compliance Assessment

**Processing Activity:** [description]
**Assessment Type:** [Quick / Full]
**Assessment Date:** [date]

### Compliance Dashboard

| Area | Status | Priority |
|------|--------|----------|
| Legal Basis | [COMPLIANT/NEEDS ATTENTION/NON-COMPLIANT] | [High/Medium/Low] |
| Data Minimization | [status] | [priority] |
| Purpose Limitation | [status] | [priority] |
| Storage Limitation | [status] | [priority] |
| Transparency | [status] | [priority] |
| Data Subject Rights | [status] | [priority] |
| DPIA | [status] | [priority] |
| International Transfers | [status] | [priority] |
| Verwerkersovereenkomst | [status] | [priority] |
| Security | [status] | [priority] |
| Breach Procedures | [status] | [priority] |
| UAVG-Specific | [status] | [priority] |

### Overall Assessment: [COMPLIANT / PARTIALLY COMPLIANT / NON-COMPLIANT]

### Critical Actions Required
1. [Most urgent action]
2. [Second priority]
3. [Third priority]

### Recommendations
[Detailed recommendations for achieving or maintaining compliance]

### Relevant Legislation
- AVG (GDPR) -- [specific articles]
- UAVG -- [specific articles]
- [Other relevant Dutch laws]

### Relevant AP Guidance
- [Reference to relevant Autoriteit Persoonsgegevens guidelines or decisions]
```

### Step 7: Disclaimer

Always append the following disclaimer at the end:

---

**Disclaimer / Juridische kennisgeving**

This AVG/GDPR compliance assessment is generated by an AI legal assistant and does not constitute legal advice within the meaning of the Advocatenwet. This assessment is for informational purposes only. Data protection law is complex and context-dependent. You should consult a qualified Dutch privacy lawyer or Functionaris Gegevensbescherming (Data Protection Officer) for a formal compliance assessment. No attorney-client relationship is created by this assessment. The Autoriteit Persoonsgegevens (AP) is the competent supervisory authority for data protection in the Netherlands.

*Deze AVG/GDPR-compliancebeoordeling is gegenereerd door een AI-juridisch assistent en vormt geen juridisch advies in de zin van de Advocatenwet. Deze beoordeling is uitsluitend bedoeld ter informatie. U dient een gekwalificeerde Nederlandse privacyadvocaat of Functionaris Gegevensbescherming te raadplegen voor een formele compliancebeoordeling.*
