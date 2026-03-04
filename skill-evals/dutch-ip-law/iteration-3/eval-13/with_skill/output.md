## IP Law Analysis

**IP Right(s)**: Copyright (Auteursrecht) — Software / Training Code; potentially also Database Rights (Databankenwet) for the AI model
**Territorial Scope**: Netherlands (Dutch law governs employment relationship and IP ownership)
**Legal Question**: Who owns the copyright in a custom AI model (specifically the training code) created by an employed developer during working hours using company resources?

---

## Applicable Legal Framework

- **Auteurswet (Aw)**, specifically:
  - **Art. 7 Aw** — Werkgeversauteursrecht (employer copyright / works made in employment)
  - **Art. 8 Aw** — Legal entity as deemed author
  - **Art. 45h–45n Aw** — Special provisions for computer programs (implementing EU Software Directive 2009/24/EC)
  - **Art. 2 Aw** — Transfer of copyright (requires written akte)
  - **Art. 1 Aw** — Definition of copyright
- **Databankenwet** — Database rights (potentially relevant for the AI model's training dataset)
- **CJEU, 2 May 2012, C-406/10 (SAS Institute v. World Programming Ltd)** — Scope of software copyright (expression protected, not ideas/algorithms)
- **HR 1 June 1990, ECLI:NL:HR:1990:ZC8537 (Kluwer Academic Publishers)** — Scope of Art. 7 Aw in employment context
- **HR 30 May 2008, ECLI:NL:HR:2008:BC2153 (Endstra Tapes)** — Originality requirement (eigen intellectuele schepping)
- **CJEU 16 July 2009, C-5/08 (Infopaq)** — EU-harmonized originality standard

---

## Analysis

### 1. Does the Training Code Qualify for Copyright Protection?

For the developer's training code to be protectable by copyright, it must meet the **originality threshold** under Art. 1 Aw:
- The work must be the **eigen intellectuele schepping** (own intellectual creation) of the author — the harmonized EU standard established by the Hoge Raad in **Endstra Tapes** (ECLI:NL:HR:2008:BC2153) and confirmed by the CJEU in **Infopaq** (C-5/08)
- The work must bear the **persoonlijk stempel van de maker** (personal stamp of the author) — reflecting creative choices
- Mere labor, skill, or investment ("sweat of the brow") is insufficient

**For training code specifically**: Source code written by a developer to train a custom AI model typically involves significant creative choices — architecture selection, hyperparameter configurations, data pipeline design, custom loss functions, preprocessing logic, etc. Such code will ordinarily meet the originality threshold and qualify for copyright protection as a literary work (Art. 45h Aw).

**What is NOT protected**: Per **SAS Institute (CJEU C-406/10)**, the following elements of the AI model/code are **not** copyright-protected:
- The underlying **algorithm or mathematical method** (these are ideas, not expressions)
- The **AI model's functionality** or behavior
- The **programming language** used
- The **training methodology** as an abstract concept
- Data formats and interfaces, unless specifically expressed in original form

Only the **specific expression** — the actual source code as written — is protected.

### 2. The Central Legal Issue: Art. 7 Auteurswet — Werkgeversauteursrecht

**Art. 7 Auteurswet** provides:

> *If the labor performed in the service of another consists of the making of certain works of literature, science, or art, the employer is deemed to be the author of those works, unless otherwise agreed between the parties.*

This is the **werkgeversauteursrecht** (employer copyright rule). Under Art. 7 Aw, the **employer is automatically deemed the author** — and thus the copyright owner — of works created by an employee in the course of their employment duties, **without any need for a separate written assignment** (akte van overdracht).

This is a fundamental distinction from commissioned works by independent contractors (ZZP'ers), where copyright stays with the creator unless explicitly transferred by a written assignment deed (Art. 2 Aw).

**Software-specific provision**: The same rule applies explicitly to computer programs under **Art. 45h Aw**: the employer is deemed the author of software created by an employee in the course of their duties. This was implemented to reflect the EU Software Directive (2009/24/EC, Art. 2 lid 3).

### 3. Conditions for Art. 7 Aw to Apply

For the employer to be deemed the author under Art. 7 Aw, the following conditions must be met:

**Condition 1: Employment relationship (dienstverband)**
- There must be an employment contract (arbeidsovereenkomst) between the developer and the company
- Art. 7 does NOT apply to freelancers, contractors (ZZP'ers), or consultants, even if they work on company premises or use company resources
- Based on the question, the developer is a member of "our software development team" — this implies an employment relationship, so Art. 7 Aw applies

**Condition 2: The work was made "in the service of another" as part of job duties**
- The creation of the work must fall within the scope of the employee's normal duties or specific instructions
- Per **HR 1 June 1990, ECLI:NL:HR:1990:ZC8537 (Kluwer Academic Publishers)**: Art. 7 Aw requires that the creation of the work falls within the employee's **normal duties** or was done pursuant to **specific instructions from the employer**
- Works created **outside the scope of employment** (e.g., personal side projects, open-source contributions during personal time) remain with the employee even if created during working hours or using employer resources — though use of employer resources and working hours is a strong indicator

**Application to this case**:
- The code was created **during working hours** — strong indicator that it falls within job duties
- Company **resources were used** — further indicator of employment context
- The developer is a member of a **software development team** — implying that creating software is their core function
- A **custom AI model** created by a software development team is very likely within the scope of their job duties

**Conclusion**: All three Art. 7 Aw conditions appear to be met. The **employer (the company) is the deemed author and copyright owner** of the training code — the developer's claim to copyright is very likely without legal foundation under Art. 7 Aw.

### 4. What About the Developer's Moral Rights?

Even where the employer is the deemed author under Art. 7 Aw, the question arises about **persoonlijkheidsrechten (moral rights)** under Art. 25 Aw.

**Important**: When Art. 7 Aw applies (employer deemed author), **the employee retains no moral rights** in respect of the employer's exploitation of the work. This is because Art. 7 Aw deems the employer to be the author — not merely the owner of a transferred copyright. Moral rights belong to the **maker** (author), and the employer is the deemed maker.

This is a key distinction from copyright assignment (Art. 2 Aw): in a transfer scenario, the natural person retains moral rights. Under Art. 7 Aw, the employer is the maker ab initio.

### 5. "Unless Otherwise Agreed" — Can the Parties Contract Around Art. 7?

Art. 7 Aw applies **"unless otherwise agreed between the parties"** (tenzij anders is overeengekomen). This means:
- The parties could contractually agree that the employee retains copyright in works created in the course of employment
- Such an agreement would need to be **clear and explicit** — a general employment contract without specific IP provisions does not displace Art. 7
- In practice, most employment contracts either rely on Art. 7 Aw (employer is deemed author) or include an explicit IP assignment clause as a belt-and-suspenders provision

If there is **no explicit agreement** to the contrary, Art. 7 Aw operates automatically. The developer's claim is based on the general principle that creators own their work — but this is overridden by Art. 7 Aw in the employment context.

### 6. Database Rights (Databankenwet) — AI Model Training Data

Separately from copyright in the training code, the **trained AI model itself** and the **training dataset** may be subject to additional IP protection:

**Databankenwet (Sui Generis Database Right)**:
- If the company made a **substantial investment** (substantiële investering) in obtaining, verifying, or presenting the contents of the training dataset, the company may hold a **sui generis database right** over the training dataset under the Databankenwet (implementing EU Directive 96/9/EC)
- This right prevents extraction and re-utilization of the dataset without permission
- Duration: 15 years from completion of the database (renewable if a new substantial investment is made)

**Copyright in the AI model weights**: The legal status of trained AI model weights under Dutch copyright law is currently evolving. The weights are mathematical values determined through the training process. Whether they constitute an "original work" meeting the eigen intellectuele schepping threshold is uncertain — this is an area of legal development. The Endstra Tapes standard (personal stamp of the author from creative choices) is difficult to apply to machine-generated weights. This is flagged as an escalation trigger requiring specialist AI law advice.

### 7. Patent Considerations

If the AI model or its training method constitutes a **technical invention** (not just software "as such"), a **patent application** under the Rijksoctrooiwet 1995 (ROW) may be possible. Under Art. 12 ROW, inventions made by an employee in the context of their employment belong to the **employer**. Patent advice from a specialized octrooigemachtigde should be sought if patentability is considered.

---

## Protection Status

| IP Right | Protected? | Owner |
|----------|-----------|-------|
| Training code (source code) | YES — copyright under Art. 45h Aw | Employer (Art. 7 Aw) |
| Algorithm / mathematical method | NO — not copyright-protectable (SAS Institute) | N/A |
| AI model weights | Uncertain — evolving law | Unclear; likely employer if protectable |
| Training dataset (if substantial investment) | YES — sui generis database right (Databankenwet) | Employer |
| Training methodology (as idea) | NO — ideas not protected | N/A |

---

## Ownership

**The employer owns the copyright** in the training code by operation of **Art. 7 Auteurswet** (and Art. 45h Aw for software). This applies:
- Automatically — no assignment deed needed
- From the moment of creation
- Regardless of the developer's personal effort or creative contribution

The **developer's claim to copyright** is legally unfounded for work performed in the course of their employment duties. The developer was employed to create software; the AI model and training code fall squarely within their job scope.

**Exception**: If the developer created code **outside of working hours, without using company resources, and for purposes unrelated to their employment**, that specific code would remain with the developer. However, on the facts presented (working hours, company resources, team context), this exception does not appear to apply.

---

## Practical Recommendations

1. **Confirm the employment status** of the developer — verify that an employment contract (arbeidsovereenkomst) exists and that creating software/AI systems is within their job description (functieomschrijving). This is the legal foundation for Art. 7 Aw.

2. **Review the employment contract** — check whether it contains an IP clause. If it does, verify it is consistent with Art. 7 Aw and does not inadvertently assign rights to the employee. Consider adding an explicit IP ownership clause for clarity.

3. **Document the work attribution** — maintain records showing that the training code was developed during working hours, using company resources, as part of the team's assigned project. This documentation strengthens the Art. 7 Aw position.

4. **Do not accept the developer's claim without legal review** — the claim is likely without legal basis but should be formally assessed by an IP lawyer specializing in software and employment IP.

5. **Assess trade secret protection** — in addition to copyright, consider whether the training code and model architecture qualify as **bedrijfsgeheimen (trade secrets)** under the Wet bescherming bedrijfsgeheimen (Wbb), which provides protection against unauthorized disclosure or use of confidential business information.

6. **Consider patent protection** — if the AI model or training method represents a novel technical solution (not software "as such"), consult an octrooigemachtigde (patent attorney) about patent protection under the ROW or European Patent Convention.

7. **Assess database rights** — if the company made substantial investments in the training dataset, register or document the sui generis database right position.

8. **Seek specialist advice on AI model weights** — given the evolving nature of AI copyright law, consult an IP lawyer with AI expertise regarding the ownership and protection of the trained model weights themselves.

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

*Generated by the Netherlands AI Lawyer System - an AI tool for legal analysis.*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2026-03-04*
