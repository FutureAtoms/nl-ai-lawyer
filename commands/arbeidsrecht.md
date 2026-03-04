---
name: arbeidsrecht
description: Employment law query
arguments:
  - name: question
    description: Employment law question
    required: true
  - name: context
    description: employer or employee perspective
    required: false
---

# Dutch Employment Law (Arbeidsrecht) Query

Answer employment law questions under Dutch law, covering the full spectrum of arbeidsrecht.

## Skill and Tools

Use skill: **dutch-employment-law**

Use MCP tools:
- `legislation_search` -- to look up BW Boek 7 Titel 10 and other employment legislation
- `legislation_fetch` -- to retrieve specific articles
- `caselaw_search_rechtspraak` -- to find relevant employment law case law
- `caselaw_fetch_uitspraak` -- to retrieve full text of key decisions

## Workflow

### Step 1: Question Classification

Classify the employment law question into one or more of these categories:

1. **Contract Formation (Totstandkoming):** arbeidsovereenkomst vs. opdracht, schijnzelfstandigheid, qualification of the relationship
2. **Terms and Conditions (Arbeidsvoorwaarden):** salary, working hours, holidays, benefits
3. **During Employment (Tijdens dienstverband):** sick leave, performance, disciplinary measures, modification of terms
4. **Termination (Beeindiging):** dismissal, resignation, mutual termination, UWV/kantonrechter procedures
5. **Post-Employment (Na dienstverband):** non-compete, pension, references, transitievergoeding
6. **Collective Labor Law (Collectief arbeidsrecht):** CAO, ondernemingsraad, restructuring
7. **Special Categories:** pregnant employees, disabled employees, agency workers, fixed-term contracts
8. **New Work Forms:** platform work, WAB implications, DBA/VBAR

### Step 2: Perspective Framing

If `context` is provided:
- **Employer perspective:** Focus on obligations, risks, procedures, and protective measures for the employer
- **Employee perspective:** Focus on rights, protections, remedies, and entitlements for the employee
- If not specified, present both perspectives in a balanced way

### Step 3: Legal Framework Analysis

Present the applicable legal framework:

```
### Applicable Legislation

| Law | Relevant Provisions | Topic |
|-----|---------------------|-------|
| BW Boek 7, Titel 10 | art. 7:610-691 | Core employment law |
| WWZ | Various | Work and Security Act |
| WAB | Various | Balanced Labour Market Act |
| WML | | Minimum Wage Act |
| ATW | | Working Hours Act |
| Waadi | | Allocation of Workers by Intermediaries Act |
| WOR | | Works Councils Act |
| WGBL | | Equal Treatment (Age) Act |
| AWGB | | General Equal Treatment Act |
| Wet flexibel werken | | Flexible Working Act |
| [Applicable CAO] | | Collective labour agreement |
```

### Step 4: Detailed Analysis by Topic

#### For Termination Questions:

Present the eight grounds for dismissal under art. 7:669 BW:

| Ground | Description | Route |
|--------|-------------|-------|
| a. Bedrijfseconomisch | Business economic reasons (redundancy) | UWV |
| b. Langdurige ziekte | Long-term illness (>2 years) | UWV |
| c. Frequent verzuim | Frequent absenteeism | Kantonrechter |
| d. Disfunctioneren | Poor performance | Kantonrechter |
| e. Verwijtbaar handelen | Culpable conduct | Kantonrechter |
| f. Gewetensbezwaar | Conscientious objection | Kantonrechter |
| g. Verstoorde relatie | Disrupted working relationship | Kantonrechter |
| h. Andere omstandigheden | Other circumstances | Kantonrechter |
| i. Cumulatie | Combination of grounds (WAB) | Kantonrechter |

Analyze:
- Which ground(s) apply
- Required documentation and evidence
- Procedural requirements (UWV vs. kantonrechter)
- Herplaatsingsplicht (obligation to reassign)
- Transitievergoeding calculation
- Billijke vergoeding (fair compensation) if applicable
- Notice periods (opzegtermijn) per art. 7:672 BW

#### For Contract Questions:

- Fixed-term vs. indefinite (bepaalde/onbepaalde tijd)
- Ketenregeling (chain provision) -- art. 7:668a BW: max 3 contracts in 36 months
- Probationary period (proeftijd) -- art. 7:652 BW
- Non-compete clause (concurrentiebeding) -- art. 7:653 BW
- Schriftelijkheidsvereiste (written form requirement) for specific clauses

#### For Sick Leave Questions:

- Employer's obligations during illness:
  - 104 weeks salary continuation (70% first year, 70% second year, minimum WML first year)
  - Re-integration obligations (Wet verbetering poortwachter)
  - Plan of approach and re-integration report
  - Second opinion rights
- Opzegverbod tijdens ziekte (prohibition of dismissal during illness)
- WIA assessment after 104 weeks

#### For CAO Questions:

- Determine applicable CAO
- Distinguish between standard-CAO (normaal) and minimum-CAO
- AVV (algemeen verbindend verklaring) -- extension to entire sector
- Relationship between CAO and individual contract

### Step 5: Transitievergoeding Calculation

If relevant, calculate the transitievergoeding:

```
### Transitievergoeding Calculation

**Formula (since 1 January 2020 -- WAB):**
1/3 monthly salary per year of service (pro rata for partial years)

**Monthly Salary Basis:**
- Bruto maandsalaris (gross monthly salary)
- + 1/12 vakantietoeslag (holiday allowance)
- + 1/12 13th month (if applicable)
- + 1/36 variable components (average over 3 years)

**Calculation:**
- Years of service: [X]
- Monthly salary basis: EUR [Y]
- Transitievergoeding: [X] x (1/3 x [Y]) = EUR [result]

**Maximum (2024/2025):** EUR [current cap] or one annual salary if higher
```

### Step 6: Practical Guidance

Provide actionable guidance:

```
### Practical Steps

**If Employer:**
1. [Step 1 -- specific action with timeline]
2. [Step 2]
3. [Step 3]
**Risks to consider:**
- [Risk 1]
- [Risk 2]

**If Employee:**
1. [Step 1 -- specific action with timeline]
2. [Step 2]
3. [Step 3]
**Rights to exercise:**
- [Right 1]
- [Right 2]

### Important Deadlines
- [Deadline 1: e.g., vervaltermijn for requesting billijke vergoeding -- 2 months after end of employment]
- [Deadline 2: e.g., UWV application timeline]
```

### Step 7: Disclaimer

Always append the following disclaimer at the end:

---

**Disclaimer / Juridische kennisgeving**

This employment law analysis is generated by an AI legal assistant and does not constitute legal advice within the meaning of the Advocatenwet. Employment law matters often involve strict deadlines (vervaltermijnen) that, if missed, result in loss of rights. You should consult a qualified Dutch employment lawyer (arbeidsrechtadvocaat) promptly, especially in termination situations. No attorney-client relationship is created by this analysis. This information may not reflect the most recent legislative changes or CAO updates.

*Deze arbeidsrechtelijke analyse is gegenereerd door een AI-juridisch assistent en vormt geen juridisch advies in de zin van de Advocatenwet. Arbeidsrechtelijke kwesties kennen vaak strikte vervaltermijnen. U dient onmiddellijk een gekwalificeerde arbeidsrechtadvocaat te raadplegen, met name bij ontslagkwesties. Er ontstaat geen advocaat-client relatie door deze analyse.*
