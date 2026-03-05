# Analysis of Axelera AI's Proposed Employment Addendum

## Executive Summary

The proposed addendum (Sections 1.1-1.19) contains **8 scope alignment issues** that require revision before it can be finalized. While the addendum is presented as a Wingman delivery agreement, in its current form the scope extends to the entire ChipOS platform, including all future derivatives and related technologies, which goes beyond the agreed Wingman arrangement.

**Key facts:**
- Abhilash Chadhar has been a permanent employee at Axelera AI since December 2022.
- ChipOS was independently developed by Abhilash through FutureAtoms (eenmanszaak, KvK: 99153289), an independently operated business. Note: an eenmanszaak does not have separate legal personality under Dutch law (FutureAtoms is a trade name of Abhilash), but it is a distinct commercial activity with its own KvK registration, administration, and IP portfolio.
- Wingman is a narrow application built for the Axelera Voyager SDK; it is architecturally and technically independent from ChipOS.
- The proposed addendum does not distinguish between ChipOS and Wingman, captures virtually all future work, and requires suspension of FutureAtoms. This scope extends beyond the agreed Wingman arrangement.

The addendum **requires significant revision** in its current form and should be replaced with a properly scoped counter-proposal that separates the Wingman delivery from ChipOS ownership.

> **Note:** The scope refinement in each section below represents the *minimum acceptable* position for each clause. The full counter-proposal document (`employment-addendum-counter-proposal.md`) contains the complete negotiating position, which may differ in specific details (e.g., exclusive vs. non-exclusive license scope) as part of the overall negotiation strategy.

---

## Clause-by-Clause Analysis

---

### Issue 1: ChipOS Definition Too Broad (Section 1.2)

**Axelera's Clause:**
Section 1.2 defines ChipOS to include "any successor, derivative, fork, update, extension, architectural variation or related technology" of the ChipOS platform.

**Problem:**
This definition is broad enough to capture virtually any future work that FutureAtoms could undertake. Any software Abhilash develops, even entirely new products unrelated to ChipOS, could be argued to fall within this definition as an "extension," "architectural variation," or "related technology." This may unintentionally capture future work in unrelated domains (healthcare, music, wellness, etc.).

**Legal Basis:**
- **Art. 7:653a BW** (effective 1 August 2022): protection of ancillary activities. An employer may not prohibit an employee from performing work for others outside working hours unless objectively justified. A definition broader than necessary that captures all future independent work lacks such justification.
- **Art. 7:611 BW** (goed werkgeverschap): an employer must act reasonably and fairly. Defining an employee's pre-existing independent IP so broadly as to swallow all future entrepreneurial activity is unreasonable.

**Risk Assessment:** **CRITICAL**

**Suggested Scope Refinement:**
> "ChipOS" means the vendor-neutral agentic orchestration platform for semiconductor design workflows, as existing at the date of this Agreement, version 1.0 (as at the signing date), as documented in the FutureAtoms repository at the signing date. This definition expressly excludes any future developments, derivatives, forks, updates, extensions, or new products created by FutureAtoms independently of this Agreement.

---

### Issue 2: Non-Exclusive License to ALL of ChipOS (Section 1.3a)

**Axelera's Clause:**
Section 1.3a grants Axelera a "perpetual, irrevocable, transferable, sublicensable" non-exclusive license to the entire ChipOS platform.

**Problem:**
The scope of this license extends beyond the Wingman delivery arrangement. Axelera evaluated and agreed to receive Wingman, a narrow application for programming the Voyager SDK. There is no contractual or factual basis for a license to ChipOS itself, which is a separate, pre-existing platform developed independently by FutureAtoms. This license scope would encompass an extensive independent commit history, 11 App Packs, and the entire VS Code IDE extension architecture, none of which relate to the agreed Wingman delivery.

**Legal Basis:**
- No contractual basis exists in the employment agreement for requiring license rights to pre-existing, independently developed IP.
- The scope of the license exceeds the employment relationship entirely; ChipOS was not created in the course of employment duties.

**Risk Assessment:** **CRITICAL**

**Proposed Narrowing:**
> Axelera receives a non-exclusive, non-transferable license limited exclusively to Wingman v1.0.0 (the Voyager SDK programming assistant), for internal use only. No license of any kind is granted to the ChipOS platform.

---

### Issue 3: Exclusive License in Overly Broad Fields (Section 1.3b)

**Axelera's Clause:**
Section 1.3b defines "Defined Fields" as "any and all fields of developing software for AI applications on CPUs, GPUs, AIPUs, accelerators, and any other compute processors."

**Problem:**
This definition covers **all of computing**. Every modern software application runs on CPUs, GPUs, or accelerators. An exclusive license in these "Defined Fields" would prevent FutureAtoms from operating in any AI software field whatsoever, which is broader than necessary for the Wingman delivery scope. This breadth may unintentionally capture FutureAtoms projects in entirely unrelated domains (healthcare, music, wellness, etc.).

**Legal Basis:**
- **Art. 7:653a BW**: a restriction this broad cannot be objectively justified; it would be void as an unreasonable restraint on ancillary activities.
- General Dutch contract law principles of **reasonableness and fairness (redelijkheid en billijkheid, Art. 6:248 BW)**: a clause that prevents an employee from working in any computing field is manifestly unreasonable and potentially unenforceable.

**Risk Assessment:** **CRITICAL**

**Recommended Revision:**
> Exclusive license limited to: "programming and developing software applications specifically for Axelera AI accelerator cards (Metis and successor Axelera-branded products)." All other fields remain unrestricted for FutureAtoms.

---

### Issue 4: All Future ChipOS Development Belongs to Axelera (Section 1.8)

**Axelera's Clause:**
Section 1.8 provides that ALL developments related to ChipOS "whether during or outside working hours and whether at the workplace or elsewhere" shall vest in Axelera.

**Problem:**
This clause is difficult to reconcile with Dutch law. It claims ownership over work performed entirely outside the employment relationship, on the employee's own time, using the employee's own resources, through a separately registered business. Combined with the broad definition in Section 1.2, this would mean that any software Abhilash writes at home, on weekends, for FutureAtoms clients, would automatically become Axelera's property. This scope extends well beyond the Wingman delivery and would undermine the viability of FutureAtoms as an independent business.

**Legal Basis:**
- **Art. 7:653a BW** (effective 1 August 2022): employers cannot restrict ancillary activities without objective justification. Claiming ownership of all output from those activities goes far beyond mere restriction.
- **Art. 7 Auteurswet (Copyright Act)**: employer copyright is limited to works created within the scope of the employee's duties. Work done independently outside employment scope does not fall under this provision.
- **Art. 6:248 lid 2 BW** (*derogerende werking van redelijkheid en billijkheid*): a contractual provision is not binding insofar as it would be unacceptable according to standards of reasonableness and fairness. Claiming ownership of all independent output is disproportionate and unreasonable.

**Risk Assessment:** **CRITICAL**

**Counter-Position:**
> Clear IP boundary clause:
> - Work performed within the scope of employment duties during working hours = employer IP (Axelera).
> - Work performed independently outside employment duties, outside working hours, through FutureAtoms = employee IP (Abhilash/FutureAtoms).
> - Wingman v1.0.0, as delivered, constitutes the complete scope of work-for-hire under this agreement.

---

### Issue 5: Mandatory Suspension of FutureAtoms (Section 1.13-1.14)

**Axelera's Clause:**
Sections 1.13 and 1.14 prohibit ALL AI/software business activities by the employee and require the suspension of existing business activities, including FutureAtoms.

**Problem:**
This is difficult to reconcile with both Dutch law and the original employment agreement. The original employment contract (Clause 13) expressly permits side activities with employer approval, which "shall not be unreasonably withheld." The addendum attempts to override this with a blanket prohibition, which:
1. Violates the statutory protection of ancillary activities under Art. 7:653a BW.
2. Contradicts the agreed terms of the original employment contract.
3. Would require Abhilash to abandon a registered business (KvK: 99153289) with its own clients and independent value.

**Legal Basis:**
- **Art. 7:653a BW**: a clause prohibiting ancillary activities is void unless the employer can demonstrate an objective justification (e.g., health and safety, avoiding conflicts of interest, protecting trade secrets). A blanket prohibition fails this test.
- **Original employment agreement, Clause 13**: side activities are permitted with approval not to be unreasonably withheld. The addendum cannot unilaterally override this without meeting the requirements of Art. 6:248 BW (redelijkheid en billijkheid) and the Stoof/Mammoet test (HR 11 July 2008, ECLI:NL:HR:2008:BD1847), which requires that any proposed change to employment terms be (i) based on changed circumstances, (ii) a reasonable proposal by the employer, and (iii) one that the employee cannot reasonably refuse.

**Risk Assessment:** **CRITICAL**

**Suggested Scope Refinement:**
> Employee is permitted to continue operating FutureAtoms (KvK: 99153289) subject to the following conditions:
> - Employee shall not develop programming tools that directly compete with Wingman for the specific purpose of programming Axelera AI accelerator cards.
> - FutureAtoms shall not use Axelera confidential information.
> - All other FutureAtoms activities (including healthcare, music, wellness, computer vision, networking, and vendor-neutral semiconductor tooling such as ChipOS) remain unrestricted.

---

### Issue 6: Delivery Includes Full ChipOS Source (Section 1.5-1.6c)

**Axelera's Clause:**
Sections 1.5 and 1.6c require delivery of the "full source code repository for ChipOS and Voyager Wingman."

**Problem:**
The delivery obligation captures the entire ChipOS codebase: an extensive independent commit history of developed work, including 11 App Packs, the VS Code IDE architecture, and all supporting infrastructure. The only deliverable that should be in scope is Wingman, which consists of 3 commits and a separate FastAPI + React application with zero imports from ChipOS. Including the full ChipOS source code in the delivery scope would effectively encompass the entire FutureAtoms product portfolio.

**Legal Basis:**
- There is no contractual basis in the employment agreement for requiring delivery of pre-existing, independently developed IP.
- The delivery obligation exceeds the scope of the agreed Wingman work product and would be disproportionate without adequate compensation for the independently developed IP.

**Risk Assessment:** **HIGH**

**Proposed Limitation:**
> Delivery limited to:
> - Wingman v1.0.0 git archive (separate repository).
> - Wingman technical documentation.
> - Wingman deployment instructions for Axelera's infrastructure.
> No ChipOS source code, repositories, or documentation shall be included in the delivery.

---

### Issue 7: Axelera Gets Enforcement Rights Over ChipOS (Section 1.15)

**Axelera's Clause:**
Section 1.15 grants Axelera the power to bring legal proceedings against third parties for infringement of ChipOS intellectual property.

**Problem:**
This clause grants Axelera enforcement rights over intellectual property that belongs to FutureAtoms. Granting enforcement rights to a licensee (especially one whose license should be limited to Wingman) would allow Axelera to influence how ChipOS is used and by whom, which is broader than necessary for the Wingman delivery arrangement.

**Legal Basis:**
- Enforcement rights generally follow ownership; they cannot be granted without an explicit ownership transfer or a carefully scoped exclusive license.
- Granting enforcement rights without ownership transfer creates legal confusion and potential liability for FutureAtoms.

**Risk Assessment:** **HIGH**

**Recommended Revision:**
> Remove Section 1.15 entirely. Alternatively, if Axelera requires enforcement capability for Wingman-specific IP only:
> - Enforcement rights limited to Wingman v1.0.0 IP only.
> - Any enforcement action requires prior written consent of FutureAtoms.
> - FutureAtoms retains all enforcement rights over ChipOS.

---

### Issue 8: Irrevocable Waiver (Section 1.17)

**Axelera's Clause:**
Section 1.17 requires the employee to waive "any right to terminate, rescind, dissolve or set aside the licence."

**Problem:**
This provision removes all contractual remedies for the licensor (FutureAtoms/Abhilash) in the event of breach by Axelera. Under Dutch law, irrevocable waivers of this nature are disfavored, particularly in employment contexts where there is an inherent power imbalance. If Axelera were to breach the agreement (for example, by sublicensing beyond the agreed scope or failing to pay), Abhilash would have no ability to terminate the license. Standard licensing practice provides balanced termination rights for both parties.

**Legal Basis:**
- **Art. 7:611 BW**: good employer practices require balanced contractual terms; a unilateral irrevocable waiver in an employment context is unreasonable.
- **Art. 6:248 lid 2 BW**: a contractual provision is not binding insofar as it would be unacceptable according to standards of reasonableness and fairness (derogerende werking van redelijkheid en billijkheid).
- General Dutch contract law principles require that both parties retain remedies for material breach.

**Risk Assessment:** **HIGH**

**Counter-Position:**
> Standard termination provisions:
> - Either party may terminate the license upon material breach, subject to a 30-day cure period.
> - License terminates automatically upon termination of the employment relationship, with a 12-month wind-down period for Axelera to transition away from Wingman.
> - Axelera retains a perpetual license only if all financial obligations have been met in full.

---

## Summary Comparison Table

| Section | Axelera Proposes | Risk | Counter-Proposal |
|---------|-----------------|------|-----------------|
| **1.2** Definition | ALL of ChipOS + all derivatives, forks, extensions, related technology | **CRITICAL** | Wingman v1.0.0 only, with fixed version and date |
| **1.3a** License | Perpetual, irrevocable, transferable, sublicensable non-exclusive license to ALL ChipOS | **CRITICAL** | No ChipOS license; Wingman v1.0.0 non-exclusive license only |
| **1.3b** Fields | ALL computing fields (CPUs, GPUs, AIPUs, accelerators, all processors) | **CRITICAL** | Axelera hardware products only (Metis and successors) |
| **1.8** Future IP | ALL work, all hours, all locations vest in Axelera | **CRITICAL** | Employment scope only; FutureAtoms work remains with FutureAtoms |
| **1.13-14** FutureAtoms | Must suspend all AI/software business activities | **CRITICAL** | May continue operating; only restriction: no competing Wingman-like tools for Axelera cards |
| **1.5-6c** Delivery | Full ChipOS + Wingman source code repository | **HIGH** | Wingman v1.0.0 git archive only |
| **1.15** Enforcement | Axelera can sue third parties over ChipOS IP | **HIGH** | Remove entirely; or Wingman-only with consent requirement |
| **1.17** Waiver | Irrevocable waiver of all termination rights | **HIGH** | Standard termination provisions with cure periods |

---

## Technical Evidence of Separation

The following technical evidence, verified by codebase analysis on 4 March 2026, confirms that ChipOS and Wingman are architecturally independent products with no code-level dependency:

| Aspect | ChipOS | Wingman |
|--------|--------|---------|
| **Repository** | github.com/FutureAtoms/ChipOS.git | github.com/FutureAtoms/voyager-wingman.git |
| **Git commits** | Extensive (predominantly FutureAtoms) | 3 (all by FutureAtoms) |
| **First commit** | 15 September 2025 | February 2026 |
| **Architecture** | Custom VS Code distribution + FastAPI + MCP | 8-service Docker microservices platform |
| **Purpose** | Vendor-neutral semiconductor design orchestration (11 App Packs) | Axelera Metis NPU programming (Voyager SDK) |
| **Frontend** | VS Code native UI + embedded webviews | React 18 + Vite SPA (standalone) |
| **Docker network** | chipos-network | wingman-network |
| **Port range** | 3737, 8181, 8051 | 4080, 4737, 5433, 7800, 9051, 9181, 28017 |
| **Direct runtime imports from ChipOS** | N/A | **None** (no runtime module imports) |
| **Database** | Own Supabase project | Separate Supabase project (mandatory) |
| **Target users** | Any semiconductor engineer (vendor-neutral) | Axelera Voyager SDK developers only |
| **License** | FutureAtoms proprietary (December 2025) | Voyager Wingman License Agreement v1.0 (January 2026) |
| **Shared git history** | None | None |
| **Independence verification** | N/A | Independence verified through technical analysis (see chipos-wingman-independence-report.md for full methodology) |

This separation is critical: Wingman has no runtime dependency on ChipOS and operates as a standalone product. While Wingman draws on general development patterns and structural approaches from ChipOS (as transparently acknowledged in the counter-proposal's "Shared Development Patterns" provision), the two products have entirely different architectures, different purposes, different technology stacks, separate databases, and separate Docker networks. A comprehensive technical-legal independence report is available as a separate annex (`chipos-wingman-independence-report.md`).

---

## Conclusion

The proposed addendum **requires significant revision** in its current form. The 8 identified scope alignment issues reveal that the addendum is broader than necessary for the Wingman delivery scope and would benefit from refinement to accurately reflect the agreed arrangement.

A proper counter-proposal should:

1. **Limit scope to Wingman v1.0.0**, the only deliverable with a legitimate connection to the employment relationship.
2. **Preserve FutureAtoms' independence** in compliance with Art. 7:653a BW and the original employment contract.
3. **Maintain clear IP boundaries**: employment work belongs to Axelera; independent FutureAtoms work belongs to Abhilash.
4. **Include balanced termination rights** so that both parties retain remedies for breach.
5. **Provide fair compensation.** If Axelera wants broader rights, they must negotiate a separate commercial license at market rates.

> **Note:** We are prepared to be generous on Wingman rights, including future Wingman development during employment vesting in Axelera, in exchange for clear separation of FutureAtoms' independent projects.

---

**DISCLAIMER:** This is an AI-generated legal analysis and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and must be reviewed and finalized by a licensed attorney admitted to the Dutch bar. All legal citations should be independently verified.

*Generated by the Netherlands AI Lawyer System*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2026-03-04*
