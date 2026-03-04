---
name: triage-nda
description: "Quick screen an NDA or confidentiality agreement under Dutch law with traffic-light risk triage"
arguments:
  - name: nda
    description: NDA text or file path
    required: true
  - name: type
    description: mutual or unilateral
    required: false
---

# NDA / Geheimhoudingsovereenkomst Triage

Perform a rapid pre-screening of a Dutch NDA (geheimhoudingsovereenkomst) using traffic-light risk flags.

## Skill and Tools

Use skill: **nda-triage-nl**

Use MCP tools where applicable:
- `legislation_search` to verify relevant BW provisions on confidentiality and penalty clauses
- `caselaw_search_rechtspraak` to find relevant case law on boetebedingen and confidentiality disputes

## Workflow

### Step 1: NDA Classification

- Determine if the NDA is **mutual** (wederzijds) or **unilateral** (eenzijdig)
- If the `type` argument is provided, verify it matches the document; flag discrepancies
- Identify the disclosing and receiving parties
- Note the governing law and jurisdiction

### Step 2: Rapid Clause Screening

Screen each of the following key areas and assign a traffic-light flag:

#### A. Definition of Confidential Information (Vertrouwelijke Informatie)
- **GREEN**: Clear, reasonably scoped definition with appropriate inclusions and exclusions
- **YELLOW**: Overly broad or vague definition; missing standard carve-outs
- **RED**: Catch-all definition with no limits; or definition so narrow it provides no real protection

#### B. Standard Carve-outs (Uitzonderingen)
Check for presence and adequacy of standard exclusions:
- Already publicly known information
- Independently developed information
- Information received from third party without breach
- Information required to be disclosed by law or court order
- **GREEN**: All standard carve-outs present
- **YELLOW**: Some carve-outs missing
- **RED**: No carve-outs or carve-outs severely restricted

#### C. Term and Duration (Looptijd)
- **GREEN**: Reasonable term (typically 2-5 years) with clear start/end
- **YELLOW**: Extended term (5-10 years) or perpetual for some categories
- **RED**: Perpetual/indefinite with no termination right; or unreasonably short

#### D. Return / Destruction Obligations (Teruggave/Vernietiging)
- **GREEN**: Clear obligations to return or destroy upon request or expiry, with certification
- **YELLOW**: Vague obligations or no timeline specified
- **RED**: No return/destruction clause; or receiving party retains copies indefinitely

#### E. Penalty Clause (Boetebeding)
- **GREEN**: No penalty clause, or reasonable fixed penalty with cap (proportional to the agreement)
- **YELLOW**: Penalty present but amount is high relative to contract value; partially cumulative with damages
- **RED**: Excessive penalty (e.g., per-breach + per-day + cumulative with full damages); potentially voidable under art. 6:94 BW (matiging)

#### F. Permitted Disclosures
- **GREEN**: Clear carve-outs for employees, advisors, affiliates on need-to-know basis
- **YELLOW**: Limited or unclear permitted disclosure scope
- **RED**: No permitted disclosures; or disclosure limited to named individuals only

#### G. Remedies and Enforcement
- **GREEN**: Balanced remedies, acknowledgment of injunctive relief possibility
- **YELLOW**: Aggressive remedies but within Dutch law norms
- **RED**: One-sided remedies, waiver of defenses, or provisions inconsistent with Dutch procedural law

#### H. Governing Law and Jurisdiction (Toepasselijk recht en bevoegde rechter)
- **GREEN**: Dutch law, competent Dutch court (or agreed arbitration such as NAI)
- **YELLOW**: Foreign law but EU jurisdiction
- **RED**: Non-EU governing law; inconvenient or unusual forum selection

### Step 3: Overall Risk Assessment

Produce a summary triage:

```
## NDA Triage Report

**Type:** [Mutual/Unilateral]
**Parties:** [names]
**Governing Law:** [law]

### Quick Scan Results

| Area | Flag | Key Finding |
|------|------|-------------|
| Definition of Confidential Info | [GREEN/YELLOW/RED] | [one-line finding] |
| Standard Carve-outs | [GREEN/YELLOW/RED] | [one-line finding] |
| Term and Duration | [GREEN/YELLOW/RED] | [one-line finding] |
| Return/Destruction | [GREEN/YELLOW/RED] | [one-line finding] |
| Penalty Clause | [GREEN/YELLOW/RED] | [one-line finding] |
| Permitted Disclosures | [GREEN/YELLOW/RED] | [one-line finding] |
| Remedies | [GREEN/YELLOW/RED] | [one-line finding] |
| Governing Law/Jurisdiction | [GREEN/YELLOW/RED] | [one-line finding] |

### Overall Assessment: [GREEN / YELLOW / RED]

### Priority Actions
1. [Most critical issue to address]
2. [Second priority]
3. [Third priority]

### Negotiation Points
[Specific suggested changes if YELLOW or RED flags found]
```

### Step 4: Boetebeding Deep Dive

If a penalty clause is present, provide additional analysis:
- Calculate effective penalty exposure
- Assess enforceability under Dutch law (art. 6:91-94 BW)
- Note the court's power to mitigate (matiging) under art. 6:94 BW
- Reference relevant case law on penalty clause reasonableness

### Step 5: Disclaimer

Always append the following disclaimer at the end:

---

**Disclaimer / Juridische kennisgeving**

This NDA triage is generated by an AI legal assistant and does not constitute legal advice within the meaning of the Advocatenwet. This analysis is for informational purposes only. No attorney-client relationship (advocaat-client relatie) is created by this review. You should consult a qualified Dutch advocaat before making any legal decisions or signing any NDA. AI-generated analysis may contain errors or miss context-specific nuances. Laws and regulations may have changed since the AI's training data.

*Deze NDA-beoordeling is gegenereerd door een AI-juridisch assistent en vormt geen juridisch advies in de zin van de Advocatenwet. Deze analyse is uitsluitend bedoeld ter informatie. U dient een gekwalificeerde Nederlandse advocaat te raadplegen voordat u juridische beslissingen neemt of een geheimhoudingsovereenkomst ondertekent.*
