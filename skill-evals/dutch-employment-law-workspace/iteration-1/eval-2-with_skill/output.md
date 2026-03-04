## Employment Law Analysis

**Topic**: Hiring a Kennismigrant (Highly Skilled Migrant) and Non-Compete Clause in Fixed-Term Contract
**Perspective**: Employer
**Applicable CAO**: Not specified -- employer should verify whether the CAO ICT or another sector/company CAO applies, as this may affect employment terms

---

## Legal Framework

This question involves two distinct areas of Dutch law:

### A. Kennismigrant (Highly Skilled Migrant) Scheme
- **Besluit uitvoering Wet arbeid vreemdelingen (BuWav)** -- exemption from regular work permit (TWV) for highly skilled migrants
- **Wet arbeid vreemdelingen (Wav)** -- Work Permits for Foreign Nationals Act
- **IND (Immigratie- en Naturalisatiedienst)** regulations and salary criteria
- **Recognized Sponsor (Erkend Referent)** requirements

### B. Non-Compete Clause in Fixed-Term Contract
- **Art. 7:653 BW** -- concurrentiebeding (non-compete clause)
- **WWZ (2015) reforms** -- specific restrictions on non-compete clauses in fixed-term contracts
- **Art. 7:653 lid 2 BW** -- requirement for written justification of zwaarwegende bedrijfs- of dienstbelangen (substantial business interests)

---

## Analysis

### Part 1: Kennismigrant Salary Threshold

#### What is the Kennismigrant Scheme?

The kennismigrant (highly skilled migrant) scheme allows Dutch employers who are recognized as a sponsor (erkend referent) by the IND to hire non-EU/EEA nationals without a separate work permit (TWV), provided the employee meets the applicable salary threshold.

#### Salary Thresholds (IND Criteria)

The IND sets salary thresholds annually, adjusted each January. The thresholds for 2024 are:

| Category | Monthly Gross Salary (excl. 8% vakantiegeld) |
|----------|-----------------------------------------------|
| Highly skilled migrant, aged 30 and over | EUR 5,008 per month |
| Highly skilled migrant, under 30 | EUR 3,672 per month |
| Graduates (zoekjaar / orientation year) | EUR 2,631 per month |
| European Blue Card | EUR 6,245 per month |

**Important notes**:
- These amounts are **exclusive of 8% vacation allowance (vakantiebijslag)**; when the vacation allowance is included in monthly salary, the effective threshold is slightly lower per month
- The salary must be paid in accordance with the applicable **CAO** or, absent a CAO, must be in line with market conditions
- The salary threshold is a **minimum**; for a senior developer from India, the actual salary would typically be well above the threshold
- Thresholds are adjusted annually in January -- the employer must verify the current figures with the IND at the time of application
- The 30% ruling (30%-regeling) for tax benefit eligibility is a separate matter (handled by Belastingdienst, not IND), but many kennismigranten also qualify

#### Recognized Sponsor (Erkend Referent) Requirement

The employer must be registered as a recognized sponsor with the IND before applying for the kennismigrant residence permit. Key requirements:
- Application to IND with company documentation
- Compliance with duty of care (zorgplicht), administrative obligation (administratieplicht), and information obligation (informatieplicht)
- Sponsor is responsible for monitoring compliance with residence permit conditions
- Annual fee and periodic inspections by IND

#### Application Process
1. Employer applies to IND for combined residence and work permit (GVVA) or separate residence permit
2. IND assesses the salary criterion, employer's recognized sponsor status, and other requirements
3. Processing time: typically 2-4 weeks for recognized sponsors (fast track)
4. The employee then obtains an MVV (entry visa) at the Dutch embassy/consulate in India
5. Upon arrival: registration at municipality (gemeente), collect residence permit (verblijfsdocument)

#### References
- **IND website**: ind.nl -- current salary thresholds and application procedures
- **Salary criterion updates**: published annually by IND in the Staatscourant

---

### Part 2: Concurrentiebeding (Non-Compete Clause) in a Fixed-Term Contract

#### General Rule Since WWZ (2015)

The Wet Werk en Zekerheid (WWZ, effective 1 January 2015) fundamentally changed the rules for non-compete clauses in fixed-term contracts. Under Art. 7:653 BW:

**In a fixed-term contract (bepaalde tijd), a non-compete clause (concurrentiebeding) is in principle NOT permitted**, unless the employer provides a **written justification** of **zwaarwegende bedrijfs- of dienstbelangen** (substantial business or service interests) that make the non-compete clause necessary.

#### Requirements for a Valid Non-Compete in a Fixed-Term Contract

To include a valid concurrentiebeding in a fixed-term contract, the employer must satisfy ALL of the following:

1. **In writing** (schriftelijk) -- must be included in the employment contract itself
2. **Employee must be 18 or older** (meerderjarig)
3. **Written justification in the clause itself** -- the employer must explain, in the text of the non-compete clause, which specific substantial business interests necessitate the restriction. This justification must be:
   - **Specific and concrete** (not generic boilerplate)
   - **Related to the specific employee and function** -- e.g., access to proprietary technology, client databases, trade secrets, strategic business information
   - **Proportionate** to the restriction imposed

4. **The justification must still be valid at the time the clause is invoked** -- if circumstances change, the employer must be able to demonstrate that the interest persists

#### Case Law Guidance

Dutch courts (kantonrechters) have been **strict** in applying this requirement. In practice:

- **Generic justifications** (e.g., "the employee has access to confidential information") are typically rejected
- The employer must explain **what specific knowledge** the employee will acquire and **why** a non-compete clause (rather than just a confidentiality clause / geheimhoudingsbeding) is necessary
- Courts weigh the **double disadvantage** of a fixed-term employee: the contract already has a limited duration, and the non-compete further restricts their position after it ends
- Many non-compete clauses in fixed-term contracts are **partially or fully set aside** by courts under Art. 7:653 lid 3 BW (unreasonable disadvantage to the employee relative to the employer's interest)

#### Practical Considerations for the Senior Developer Role

For a senior developer position, the employer should consider:

| Factor | Assessment |
|--------|-----------|
| Access to proprietary source code | Strong argument for non-compete |
| Access to client data or business strategy | Strong argument |
| General programming skills | NOT sufficient -- these are the employee's own professional skills |
| Knowledge of general technology stacks | NOT sufficient |
| Specific access to trade secrets or patents | Strong argument |

**Recommendation**: If the employer has a legitimate need to protect specific business interests (e.g., proprietary algorithms, client-specific implementations, strategic product roadmaps), include a non-compete clause WITH a detailed written justification in the contract. However:

- Keep the **scope narrow** (geographic area, duration, specific competitors)
- Keep the **duration reasonable** (6-12 months maximum; longer periods are more likely to be set aside)
- Consider whether a **geheimhoudingsbeding (confidentiality clause)** and **relatiebeding (non-solicitation clause)** might suffice instead -- these are often easier to enforce and less burdensome to the employee
- The relatiebeding is treated as a form of concurrentiebeding by case law and is subject to the same requirements under Art. 7:653 BW

#### Alternative: Indefinite Contract

If the employer converts the employment to an **indefinite contract (onbepaalde tijd)**, the standard rules apply:
- Non-compete clause requires only written form and adult employee
- No written justification of substantial business interests required
- Court can still set aside or limit the non-compete if disproportionate

This may be an additional reason to offer an indefinite contract from the start.

---

## Employee Rights / Employer Obligations

### Kennismigrant-Specific Obligations
- Maintain salary at or above the IND threshold throughout the employment -- if salary drops below the threshold, the residence permit may be revoked
- Notify IND of changes in employment (termination, change of function, salary reduction)
- Ensure proper registration and compliance with sponsor obligations
- The employee's right to reside in the Netherlands is tied to the employment -- upon termination, the kennismigrant has a 3-month search period (zoekperiode) to find new employment

### Non-Compete Clause Obligations
- If the non-compete is upheld and the employee is restricted: the court may award compensation (vergoeding) to the employee under Art. 7:653 lid 5 BW
- The employee may challenge the non-compete clause at any time, including before the contract ends

---

## Practical Steps

### For the Kennismigrant Hiring Process
1. **Verify or obtain erkend referent status** with the IND
2. **Confirm the current salary threshold** on the IND website (ind.nl) -- the figures are updated annually in January
3. **Ensure the offered salary meets or exceeds the applicable threshold** (check whether the employee is under or over 30 years of age)
4. **Prepare the employment contract** in compliance with Art. 7:655 BW (written statement obligations)
5. **Submit the residence permit application** to IND
6. **Consider the 30% ruling application** with the Belastingdienst for tax advantages
7. **Arrange practical matters**: BSN (burgerservicenummer), housing, healthcare insurance

### For the Non-Compete Clause
1. **Assess whether a non-compete is truly necessary** -- or whether a confidentiality clause suffices
2. **If necessary**: draft a specific, detailed written justification of substantial business interests, tailored to this specific role and employee
3. **Limit the scope**: geographic area, duration (6-12 months), specific activities or competitors
4. **Consider offering an indefinite contract** -- this simplifies the non-compete requirements and may also be more attractive to the kennismigrant (providing more job security and a stronger position for the residence permit)
5. **Have the contract reviewed by a Dutch employment lawyer** -- especially given the combination of immigration law and employment law considerations

---

## Timeline / Deadlines

| Phase | Timeframe | Key Actions |
|-------|-----------|-------------|
| Erkend referent check/application | 2-4 weeks (if not yet registered) | IND application |
| Employment contract preparation | 1-2 weeks | Draft contract with non-compete justification |
| IND residence permit application | 2-4 weeks (recognized sponsor fast track) | Submit via IND portal |
| MVV issuance (India) | 1-2 weeks | Employee visits Dutch embassy/consulate |
| Arrival and registration | 1-2 weeks | Gemeente registration, BSN, residence permit pickup |
| 30% ruling application | Within 4 months of start | Belastingdienst application |
| **Total estimated timeline** | **6-12 weeks** | From contract signing to start date |

---

## Financial Implications

| Component | Details |
|-----------|---------|
| IND application fee | Approx. EUR 345 (kennismigrant permit) |
| Erkend referent application | Approx. EUR 4,744 (one-time, if not yet registered) |
| Salary (minimum threshold, 30+) | EUR 5,008/month excl. vakantiegeld (2024) |
| Salary (minimum threshold, under 30) | EUR 3,672/month excl. vakantiegeld (2024) |
| 30% ruling (if applicable) | 30% of gross salary tax-free (max 5 years) |
| Legal costs for contract review | EUR 1,000-3,000 |
| Relocation allowance | Market practice varies; often EUR 2,000-5,000 |

---

### Note on CAO Applicability

If a CAO applies (e.g., CAO ICT for approximately 80,000 employees in the Dutch ICT sector), it may affect:
- Salary scales (loonschalen) -- the salary must also comply with the applicable CAO scale for the function
- Notice periods
- Non-compete clause provisions
- Additional leave or benefits
- Training obligations

Verify whether a sector or company CAO is applicable and whether it has been declared generally binding (algemeen verbindend verklaard).

---

**IMPORTANT - READ THIS DISCLAIMER CAREFULLY**

This is an AI-generated legal analysis and does **NOT constitute legal advice** within the meaning of the Dutch Advocates Act (Advocatenwet). The information in this analysis:

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) registered with the Netherlands Bar Association (Nederlandse Orde van Advocaten).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a lawyer.** For legal decisions, proceedings, contracts, or disputes, you must always consult a qualified lawyer authorized to practice law in the Netherlands.

4. **Does not guarantee confidentiality.** Information shared with this AI system is not protected by attorney-client privilege (verschoningsrecht). Do not share confidential or privileged information.

5. **May not reflect current law.** Dutch legislation and case law change continuously. This analysis is based on the state of the law as of the indicated date and may not account for recent amendments.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

7. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal advisor.**

---

*Generated by the Netherlands AI Lawyer System -- an AI tool for legal analysis.*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2026-03-04*
