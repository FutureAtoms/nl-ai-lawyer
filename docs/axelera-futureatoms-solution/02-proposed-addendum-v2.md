# Proposed Addendum v2 (Counsel Negotiation Draft)

Purpose: replace Axelera counsel draft clauses 1.1-1.19 with language that gives Axelera autonomous Wingman rights while preserving FutureAtoms ChipOS ownership.

## A. Replace/Delete Instructions for Axelera Draft

Delete and replace clauses `1.2` through `1.19` entirely.

Reason:

- Current draft grants overbroad perpetual rights over all ChipOS and successors.
- Current draft captures future inventions created outside working hours.
- Current draft effectively forces suspension of all external AI/software business activities.
- Current draft creates high structural conflict with BW 7:653a (outside work restrictions require objective reason).

## B. Clean Replacement Text

### Recitals (Overwegingen)

**WHEREAS:**

A. Employee has been employed by Employer since 1 December 2022 under a permanent employment contract (arbeidsovereenkomst voor onbepaalde tijd), currently holding the position of Senior Verification Engineer;

B. Employee independently owns and operates **FutureAtoms**, a sole proprietorship (eenmanszaak) registered with the Dutch Chamber of Commerce (Kamer van Koophandel) under number **KvK: 99153289**, through which Employee has developed **ChipOS**, a vendor-neutral agentic orchestration platform for semiconductor design workflows, and operates across nine diverse technology domains;

C. ChipOS was conceived, designed, and developed by Employee on his own time, using his own equipment and resources, independently of and prior to any instruction or assignment by Employer, and does not fall within Employee's employment duties (taakomschrijving) with Employer;

D. Employee developed an application called **Wingman** (Voyager Wingman v1.0.0), a product for programming Axelera AI accelerator cards using the Voyager SDK, which is maintained in a separate git repository with zero code imports from ChipOS, a separate database, and a separate Docker network;

E. Employer has expressed interest in acquiring rights to the Wingman application for use in connection with its hardware products;

F. Employer's initial proposed addendum contains clauses (1.2 through 1.19) that, in Employee's assessment, are broader than necessary for the Wingman delivery and may unintentionally capture intellectual property rights to ChipOS and other FutureAtoms assets that fall outside the scope of the employment relationship;

G. This Addendum seeks to establish a fair and legally compliant arrangement that (i) properly delineates the boundaries between Employee's employment duties and FutureAtoms' independent business activities, (ii) grants Employer appropriate rights to the Wingman application, and (iii) preserves Employee's pre-existing intellectual property rights in ChipOS and FutureAtoms, all in accordance with Dutch law including Book 7 of the Dutch Civil Code (Burgerlijk Wetboek, "BW"), the Dutch Copyright Act (Auteurswet, "Aw"), and the Dutch Patent Act (Rijksoctrooiwet 1995);

H. Parties wish to record their agreements in accordance with the principle of good employment practices (goed werkgeverschap en goed werknemerschap) as set forth in **Article 7:611 BW**;

**NOW, THEREFORE, the Parties agree as follows:**

### 1. Definitions

1.1 `Pre-Existing FutureAtoms IP` means all intellectual property, source code, architecture, data models, tooling, documentation, and know-how owned or controlled by FutureAtoms before the Effective Date, including ChipOS and all unrelated modules, whether or not publicly available.

1.2 `Wingman Deliverable` means the standalone codebase and related artifacts delivered by Employee to Employer as `Wingman v1.0.0`, limited to the components listed in Schedule 1.

1.3 `Embedded FutureAtoms Components` means those specific portions of Pre-Existing FutureAtoms IP, if any, that are technically included in Wingman v1.0.0 and listed exhaustively in Schedule 2. Both products are developed by the same person and may reflect similar design approaches. Pursuant to EU Directive 2009/24/EC Art. 1(2) (CJEU C-406/10, ECLI:EU:C:2012:259), ideas and principles underlying software are not protectable by copyright.

1.4 `Axelera Confidential Information` means non-public information disclosed by Employer and marked or reasonably understood as confidential, excluding information that is public, independently developed without use of Axelera confidential information, or lawfully received from third parties.

### 2. Side Business Approval and Conflict Controls

2.1 Employer grants written approval for Employee to own and operate FutureAtoms and to continue development of ChipOS outside Employee working time, subject to this Article.

2.2 Employee shall not use Employer equipment, accounts, confidential information, or paid working time for FutureAtoms activities.

2.3 Employee shall not provide, through FutureAtoms, direct services that are materially competitive with Employer's card-specific software products in the defined restricted field in Schedule 3.

2.4 Any limitation under this Article must be objectively justified and proportionate to legitimate business interests.

2.5 The parties shall review conflict boundaries at least every 6 months and document any updates in writing.

### 3. Ownership of Work Product and IP Boundary

3.1 All IP created by Employee in the course of Employee's Axelera employment duties and specifically for Wingman v1.0.0 is owned by Employer.

3.2 All Pre-Existing FutureAtoms IP remains exclusively owned by FutureAtoms.

3.3 No assignment or license under this Agreement transfers ownership of:

a) ChipOS platform outside the Wingman Deliverable;  
b) unrelated FutureAtoms modules, applications, or future releases;  
c) independent developments made outside Axelera duties, on non-Axelera resources, without Axelera confidential information.

3.4 Any transfer of rights is limited to rights strictly necessary for Employer to use, maintain, modify, and support Wingman v1.0.0.

### 4. License for Embedded FutureAtoms Components (If Any)

4.1 For Embedded FutureAtoms Components listed in Schedule 2 only, FutureAtoms grants Employer a perpetual, irrevocable, worldwide, royalty-free license to use, reproduce, modify, and internally sublicense solely as part of or for operation/support of Wingman v1.0.0 and Employer-derived internal versions.

4.2 Employer may not use Embedded FutureAtoms Components as a standalone platform product separate from Wingman.

4.3 No rights are granted by implication to other ChipOS components not listed in Schedule 2.

### 5. No Capture of Future FutureAtoms Developments

5.1 Employer acknowledges that FutureAtoms may continue to develop ChipOS and related technology after the Effective Date.

5.2 Employer has no ownership, option, right of first refusal, or automatic license to such future developments unless separately agreed in a new written agreement.

### 6. Wingman Delivery and Autonomy

6.1 Employee shall deliver Wingman v1.0.0 by the agreed delivery date with source code, build instructions, deployment/runbook documentation, dependency manifest, and security handover artifacts as listed in Schedule 1.

6.2 Delivery excludes full ChipOS history and excludes modules not required for Wingman autonomy.

6.3 Employer is responsible for operation and maintenance of Wingman after acceptance.

### 7. Confidentiality and Data Separation

7.1 Both parties remain bound by confidentiality obligations under the Employment Agreement.

7.2 Each party shall implement technical and organizational measures to prevent cross-contamination of confidential information and credentials.

### 8. Marketing and Reference Rights

8.1 Subject to prior written approval (not unreasonably withheld or delayed), FutureAtoms may state factually that it developed/delivered Wingman for Axelera.

8.2 Logo use, quotes, and case-study publication require prior written approval for each publication.

### 9. Compensation and Consideration

9.1 The agreed bonus/equity consideration for Wingman delivery is as set out in Employer compensation documentation and is separate from ownership of Pre-Existing FutureAtoms IP.

9.2 No clause in this Article shall be interpreted as requiring Employee to suspend lawful outside activities that comply with this Article.

### 10. Precedence and Conflict

10.1 If there is conflict between this Addendum and prior draft Article 1.1-1.19 language regarding ChipOS, this Addendum prevails.

10.2 Any amendment to this Article must be in writing signed by both parties.

### 11. Severability (Partiele Nietigheid)

11.1 If any provision of this Addendum is held to be invalid, illegal, or unenforceable by a court of competent jurisdiction, the remaining provisions shall continue in full force and effect.

11.2 The Parties shall negotiate in good faith to replace any invalid provision with a valid provision that most closely reflects the Parties' original intent and the economic effect of the invalid provision.

11.3 The invalidity of any provision shall not affect the validity of the remainder of this Addendum, which shall be interpreted as if the invalid provision had not been included, except to the extent that such interpretation would be unreasonable (onredelijk) within the meaning of Article 6:248 BW.

## C. Schedules to Attach

- [Schedule 1: Wingman v1.0.0 Deliverables](schedule-1-wingman-deliverables.md) -- acceptance criteria and handover artifacts.
- [Schedule 2: Embedded FutureAtoms Components](schedule-2-embedded-components.md) -- None (Wingman contains no embedded ChipOS components).
- [Schedule 3: Restricted Competitive Field](schedule-3-restricted-field.md) -- narrow and objective definition.
- [Schedule 4: Resource Separation Protocol](schedule-4-separation-protocol.md) -- time, equipment, network, data, git, and database separation.

## D. Negotiation Notes

- If Axelera requests "exclusive" rights, limit exclusivity to defined Wingman deliverables and the restricted field, not all ChipOS derivatives.
- Reject language that claims rights to "any successor, derivative, fork, update, extension" of ChipOS generally.
- Reject language assigning all developments made outside working hours by default.
- Keep the boundary test factual: duties + resources + confidential information + defined deliverable scope.

## E. Signature Blocks (Ondertekening)

This Addendum has been executed in two (2) counterparts on the date first written above. Employee signs twice: once in his capacity as employee, and once in his capacity as sole proprietor of FutureAtoms, to confirm his commitment with respect to both the employment-related and the commercial/IP-related provisions of this Addendum.

&nbsp;

**FOR AND ON BEHALF OF EMPLOYER (NAMENS WERKGEVER):**

**Axelera AI B.V.**

&nbsp;

| | |
|---|---|
| Name (Naam): | _________________________________ |
| Title (Functie): | _________________________________ |
| Date (Datum): | _________________________________ |
| Signature (Handtekening): | _________________________________ |

&nbsp;

**EMPLOYEE (WERKNEMER):**

&nbsp;

| | |
|---|---|
| Name (Naam): | Abhilash Chadhar |
| Date (Datum): | _________________________________ |
| Signature (Handtekening): | _________________________________ |

&nbsp;

**FOR AND ON BEHALF OF FUTUREATOMS (NAMENS FUTUREATOMS):**

*(in Employee's capacity as sole proprietor of FutureAtoms, KvK: 99153289)*

&nbsp;

| | |
|---|---|
| Name (Naam): | Abhilash Chadhar |
| Capacity (Hoedanigheid): | Sole Proprietor (Eigenaar Eenmanszaak) |
| Date (Datum): | _________________________________ |
| Signature (Handtekening): | _________________________________ |

---

## Legal Disclaimer

This is a negotiation draft for qualified Dutch counsel review, not legal advice.

**DISCLAIMER:** This is an AI-generated document and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and should be reviewed by a qualified Dutch lawyer (advocaat) before use. References to legal provisions should be independently verified.

*Generated by FALCON (FutureAtoms AI Legal Counsel Of Netherlands)*
