## IP Law Analysis

**IP Right(s)**: Copyright (Auteursrecht) on software / training code
**Territorial Scope**: Netherlands (NL)
**Legal Question**: Who owns the copyright on an AI model's training code created by an employee during working hours using company resources, where the developer claims personal copyright?

## Applicable Legal Framework

The principal legislation governing this question is the **Auteurswet (Aw)** -- the Dutch Copyright Act (1912, as amended). The following provisions are directly relevant:

- **Art. 1 Aw** -- Defines copyright as the exclusive right of the maker (author) to reproduce and make public a work of literature, science, or art.
- **Art. 7 Aw** -- The employer ownership rule: if labor performed in the service of another (in dienst van een ander) consists of the making of certain works, the **employer** is deemed the maker of those works, unless otherwise agreed between the parties.
- **Art. 45h Aw** -- Computer programs are protected as literary works under the Auteurswet, implementing EU Software Directive 2009/24/EC.
- **Art. 6 Aw** -- Works made under direction and supervision of another (relevant as a contrasting provision for commissioned works, not employment).
- **Art. 2 Aw** -- Transfer of copyright requires an akte (written deed).

Additionally, regarding the AI model itself as a potentially patentable invention, the **Rijksoctrooiwet 1995 (ROW)**, specifically **Art. 12 ROW**, addresses employer ownership of employee inventions. However, the question focuses on the training code (a copyrightable software work), so the Auteurswet is the primary framework.

## Analysis

### 1. Software as a Protected Work

Under **Art. 45h Aw**, computer programs -- including source code, object code, and preparatory design materials -- are protected as literary works. Training code for an AI model unambiguously qualifies as a computer program within the meaning of the Auteurswet and the EU Software Directive (2009/24/EC). This means the general copyright rules of the Auteurswet apply.

### 2. The Employer Ownership Rule (Art. 7 Aw)

**Art. 7 Aw** provides that where an employee, in the course of employment (in dienst), creates a work as part of the tasks for which they are employed, the **employer is deemed the maker** (and therefore the initial copyright holder). Two cumulative requirements must be met:

1. **Employment relationship** (arbeidsovereenkomst): There must be a formal employment relationship within the meaning of Dutch labor law. The developer must be an employee, not an independent contractor (ZZP'er). Based on the facts stated -- the developer is part of the "software development team" and works "during working hours using company resources" -- this strongly indicates an employment relationship.

2. **Creating the work falls within the scope of the employee's duties**: The making of the specific type of work (here, software/training code) must be part of what the employee is employed to do. A software developer employed to build AI models and write code is clearly creating works within the scope of their employment duties.

If both conditions are met -- as appears to be the case here -- the **employer is the initial copyright holder** by operation of law. The developer is not the "maker" within the meaning of Art. 1 Aw, and therefore cannot claim copyright ownership.

### 3. The Developer's Claim

The individual developer's claim to copyright on the training code would fail under Art. 7 Aw, provided:
- They are indeed an employee (not an independent contractor);
- Writing this type of code falls within their employment duties.

The fact that the developer personally wrote the code is irrelevant under Art. 7 Aw. The provision is a legal fiction (fictief makerschap) that assigns authorship to the employer, overriding the general rule that the natural person who creates the work is the author.

### 4. Exceptions and Caveats

- **"Unless otherwise agreed"** (tenzij anders is overeengekomen): Art. 7 Aw is a default rule (regelend recht). If the employment contract or a separate agreement provides that the employee retains copyright, that agreement prevails. Review the employment contract, any IP assignment clauses, and the company's IP policy.
- **Moral rights (Art. 25 Aw)**: Even though the employer owns the economic copyright, the developer retains certain moral rights (persoonlijkheidsrechten), including the right of attribution and the right to object to distortion that harms reputation. However, moral rights in software are of limited practical significance under Dutch law.
- **Works created outside employment duties**: If the developer created the code purely in their own time, on their own initiative, and the work falls outside their employment duties, Art. 7 Aw would not apply. The facts here (working hours, company resources, team context) weigh heavily against the developer's position.

### 5. The AI Model Itself

If the AI model constitutes a patentable invention (meeting novelty, inventive step, and industrial applicability requirements under Art. 2 ROW), **Art. 12 ROW** assigns patent ownership to the employer for inventions made by employees in the context of their employment. The employee may be entitled to a fair compensation (billijke vergoeding) if the invention's significance exceeds what could reasonably be expected given their salary. However, "AI models as such" may face patentability challenges under Art. 2 lid 2 ROW (computer programs as such are excluded, though technical effects may be patentable).

## Protection Status

The training code is protected by copyright as a literary work under Art. 45h Aw. Protection arises automatically upon creation -- no registration is required under Dutch law.

## Ownership

Under **Art. 7 Aw**, the **employer** is deemed the maker and initial copyright holder of the training code, provided:
1. The developer is employed under an employment contract (arbeidsovereenkomst); and
2. Creating such software falls within the scope of the developer's employment duties.

The individual developer does **not** own the copyright, despite being the person who physically wrote the code.

## Practical Recommendations

1. **Review the employment contract**: Verify that the contract does not contain any clauses derogating from Art. 7 Aw (e.g., clauses granting IP rights to the employee). Also check for any applicable collective labor agreement (CAO) provisions.
2. **Implement or review an IP policy**: If the company does not already have a clear IP assignment policy, it should implement one that explicitly confirms the application of Art. 7 Aw to all software and IP created during employment.
3. **Document the relationship**: Maintain clear records that the developer was employed (not freelancing) and that AI model development was part of their job description. This is critical evidence if the developer later disputes ownership.
4. **Address the developer's claim directly**: Inform the developer that under Art. 7 Aw, copyright vests in the employer by operation of law. If the developer persists, seek formal legal advice from a Dutch IP lawyer (advocaat) to resolve the dispute, potentially through mediation or legal proceedings.
5. **Consider patent protection**: If the AI model has technical features that may be patentable, consult a patent attorney (octrooigemachtigde) about filing a patent application under the ROW or EPC. Remember: any public disclosure before filing destroys novelty (there is no grace period under Dutch/European patent law).
6. **Open source audit**: If the training code incorporates open source components, ensure compliance with the relevant open source licenses, as this is a copyright matter under Dutch law (Art. 45h-45n Aw).

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
