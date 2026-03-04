## IP Law Analysis

**IP Right(s)**: Copyright (Auteursrecht) — primarily software copyright; potentially also database rights (Databankenwet) if training data is involved
**Territorial Scope**: Netherlands (Dutch law)
**Legal Question**: Who owns the copyright in a custom AI model and its training code created by employees during working hours using company resources?

---

## Applicable Legal Framework

- **Auteurswet (Aw)**, in particular:
  - Art. 1 — Definition and scope of copyright
  - Art. 7 — Werkgeversauteursrecht (employer copyright / works made in employment)
  - Art. 45h–45n — Specific provisions for software (implementing EU Software Directive 2009/24/EC)
- **EU Software Directive 2009/24/EC** — Harmonizes software copyright across EU member states, including the employer-ownership rule for employee-created software
- **Databankenwet** — May apply to the training dataset if it constitutes a database meeting the relevant thresholds
- **HR 1 June 1990, ECLI:NL:HR:1990:ZC8537 (Kluwer Academic Publishers)** — Leading Dutch Supreme Court case on the scope of employer copyright under Art. 7 Aw

---

## Analysis

### 1. Is the Training Code Protected by Copyright?

The training code written by the developer is a computer program (software), which is protected as a literary work under **Art. 45h Auteurswet** (implementing Art. 1 of the EU Software Directive 2009/24/EC). Software is protected by copyright provided it meets the originality threshold: it must be the *eigen intellectuele schepping van de maker* (the author's own intellectual creation), as established by the Hoge Raad in the **Endstra Tapes** case (HR 30 May 2008, ECLI:NL:HR:2008:BC2153) and harmonized at EU level by the CJEU in **Infopaq** (C-5/08). Code that reflects creative programming choices will generally meet this threshold.

Note: As confirmed by the CJEU in **SAS Institute** (C-406/10), the *functionality* of the software, the programming language used, and the underlying algorithms are not protectable by copyright — only the specific code expression is protected. This is particularly relevant when considering what exactly is protected in AI model training code.

### 2. Who Owns the Copyright? — Art. 7 Auteurswet (Werkgeversauteursrecht)

Under **Art. 7 Auteurswet**, when an employee creates a work as part of their employment duties, the **employer** is deemed the maker (maker) of the work — and therefore the initial copyright holder — unless otherwise contractually agreed.

The key requirements for Art. 7 Aw to apply are:

1. **Employment relationship (dienstverband)**: There must be a valid employment contract (arbeidsovereenkomst) between the developer and the company. This appears to be the case here, as the work was performed "during working hours."

2. **The work falls within the scope of employment duties**: The creation of the work must be part of what the employee was hired to do, or specifically instructed to do. A software developer employed by a company to build software and AI tools will almost certainly satisfy this requirement when writing training code for a company AI model.

3. **No contrary agreement**: If the employment contract or any separate IP agreement specifically assigns copyright to the employee, Art. 7 Aw can be modified. However, absent such an agreement, the employer is automatically the rights holder — **no formal assignment is needed**.

The **Kluwer Academic Publishers** case (HR 1 June 1990, ECLI:NL:HR:1990:ZC8537) confirmed that Art. 7 Aw requires the creation to fall within the employee's normal duties or specific instructions. Works created outside the scope of employment (e.g., purely personal or hobby projects) remain with the employee, even if created during working hours. However, given that the developer created training code as part of a company software development team using company resources and during working hours, the work is almost certainly within the scope of the employment duties.

### 3. The Software Directive — Art. 45h Auteurswet

**Art. 45h Auteurswet** (implementing Art. 2(3) of the EU Software Directive 2009/24/EC) specifically addresses software created by employees: the employer is the author of software created by an employee in the course of their duties or following the employer's instructions, unless otherwise agreed.

This rule for software mirrors and reinforces the general Art. 7 Aw rule, providing a double statutory basis for employer ownership of employee-created software under Dutch law.

### 4. The Developer's Claim

The developer's claim that he holds copyright in the training code he wrote is legally unfounded under Dutch law, provided the following conditions are met (which appear satisfied based on the facts):

- The developer had an employment contract (dienstverband) with the company.
- Writing training code for the company's AI model was within his employment duties.
- No employment contract clause or separate agreement specifically reserved copyright to the developer.

Under Art. 7 Aw, the employer is deemed the maker by operation of law. The copyright arises in the employer's name from the moment of creation — there is no need for an assignment, and no assignment back to the employer is required.

### 5. What About the AI Model Itself?

The AI model (the trained neural network or machine learning model, distinct from the training code) raises separate IP questions:

- **The model weights and architecture** may also be protected as software or as a database under the **Databankenwet** (Database Act), depending on the nature of the model and the investment made in compiling it.
- **AI-generated outputs** are an evolving area of Dutch and EU law. If the AI model generates content autonomously, that content may not meet the originality threshold under current Dutch copyright law, as there is no natural person making creative choices (see the notes in the key case law reference on AI-generated works).
- For the purposes of this analysis, the model as a technical artifact created by employees as part of their duties would also fall under the employer's IP rights via Art. 7 Aw and/or the Databankenwet.

### 6. Moral Rights (Persoonlijkheidsrechten)

Even where the employer owns the copyright under Art. 7 Aw, the developer as the natural person who actually created the work retains certain **moral rights** under Art. 25 Auteurswet (recht op naamsvermelding, recht op integriteit). However, Art. 7 Aw overrides the economic copyright — the moral rights remain with the natural author but are of limited practical relevance in a commercial employment context, and many employment contracts include waivers of moral rights (to the extent permitted by law).

---

## Protection Status

The training code and related software created by the development team are protected as computer programs under **Art. 45h Auteurswet**, meeting the originality threshold as the developers' own intellectual creation. The AI model itself may be protected as software and/or under the Databankenwet.

---

## Ownership

**The company (employer) owns the copyright** in the training code and any other software created by its employees in the course of their employment duties, by operation of **Art. 7 Auteurswet** (werkgeversauteursrecht), read in conjunction with **Art. 45h Auteurswet** (software copyright in employment).

The individual developer's copyright claim is not valid under Dutch law, provided the standard requirements of Art. 7 Aw are satisfied: there is an employment relationship (dienstverband) and the code was written as part of the developer's job duties.

---

## Practical Recommendations

1. **Review employment contracts**: Ensure all employment contracts include an explicit IP clause confirming that IP created in the course of employment belongs to the employer. While Art. 7 Aw achieves this automatically, an express contractual provision adds legal clarity and avoids disputes.

2. **Contractor/freelancer distinction**: Art. 7 Aw applies only to employees. If any part of the AI model or training code was developed by freelancers (ZZP'ers) or external contractors under a commissioning agreement (opdracht), the copyright will remain with those individuals unless explicitly transferred by written akte (Art. 2 Aw). Conduct an audit of who contributed to the project and in what capacity.

3. **Open source compliance**: If any open source code was used in training or building the model, check the applicable open source licenses (e.g., GPL, MIT, Apache). Open source license obligations are copyright obligations under Dutch law and must be complied with.

4. **Document the scope of duties**: To protect against future claims by employees, document (in job descriptions, project specifications, or written instructions) that AI development and training code writing is within the scope of each developer's employment duties.

5. **Protect the AI model**: Consider whether the AI model and training data meet the requirements for database right protection under the Databankenwet. If significant investment was made in obtaining, verifying, or presenting the training data, a sui generis database right may apply.

6. **AI-specific IP strategy**: Given the rapidly evolving legal landscape around AI-generated works, consider seeking legal advice from a specialist IP attorney (IE-advocaat) on a comprehensive AI IP strategy, including protection of model weights, training data, and model outputs.

7. **No patent registration concerns here**, but note that the AI model's underlying algorithms or methods may not be patentable as such under Dutch/European patent law (Art. 2 lid 2 ROW — computer programs as such are not patentable; however, technical effects of software-implemented inventions may be).

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
