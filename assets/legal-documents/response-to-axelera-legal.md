# Response to Proposed Employment Addendum

**From:** Abhilash Chadhar
**To:** Axelera AI B.V., Legal Department (via Bram)
**Date:** 4 March 2026
**Re:** Proposed Addendum to Employment Agreement, Sections 1.1–1.19
**Classification:** Confidential

---

Dear Counsel,

Thank you for preparing the proposed addendum regarding the Wingman application. I appreciate legal's work in protecting Axelera's interests, and I want to help scope this correctly so we can reach a clean agreement quickly. I am fully committed to delivering Wingman v1.0.0 to Axelera under fair and legally compliant terms.

Before addressing the specific clauses, I think it would be helpful to clarify the factual and technical background, as the proposed addendum may have been drafted on the understanding that Wingman and ChipOS are closely linked. In practice, they are independent products serving different purposes, though Wingman does draw on general patterns and structural approaches from ChipOS (as detailed in Section 1.3 below). Wingman uses patterns and structural approaches from my independently-developed ChipOS platform, but it is an application built specifically for Axelera's needs. I want to set out this distinction below so legal can scope the addendum precisely to the Wingman delivery.

---

## 1. Background: ChipOS and Wingman

### 1.1 What is ChipOS?

**ChipOS** is a vendor-neutral agentic orchestration platform for semiconductor design workflows. I conceived, designed, and developed ChipOS independently, on my own time, using my own equipment and resources, through my registered sole proprietorship **FutureAtoms** (eenmanszaak, KvK: 99153289). ChipOS was not created as part of my employment duties at Axelera, was not developed using Axelera equipment or resources, and was not created under Axelera's direction or instruction.

ChipOS is a substantial, mature platform:
- **An extensive independent commit history** of development
- **11 application modules** ("App Packs") covering verification, physical design, and other semiconductor workflows
- **Own database infrastructure** (separate Supabase project)
- **Vendor-neutral:** designed to work with any semiconductor vendor's toolchain, not specific to Axelera

### 1.2 What is Wingman?

**Wingman** (formally "Voyager Wingman") is an application I built specifically for the purpose of programming Axelera AI accelerator cards using the Voyager SDK. Wingman was developed as a **derivative application** that applies general patterns and structural approaches from my independently-developed ChipOS platform, tailored specifically for the Voyager SDK use case.

Wingman's profile:
- **Separate git repository** from ChipOS
- **Purpose:** narrowly focused on Axelera's Voyager SDK
- **Own database infrastructure** (separate Supabase project, distinct from ChipOS)
- **Distinct scope:** while Wingman shares some structural elements with ChipOS, it was built and scoped for Axelera's specific needs

### 1.3 The Relationship Between ChipOS and Wingman

To be transparent: Wingman builds on patterns, structural approaches, and general techniques that I developed through my work on ChipOS. This is a common arrangement in software: a developer builds a general platform (ChipOS) and then creates a tailored application (Wingman) for a specific client's needs.

Both products incorporate general software engineering patterns (workflow automation, API integration, configuration management) that are standard industry techniques used by developers worldwide. Under **EU Directive 2009/24/EC Art. 1(2)** (the Software Directive, applied in Dutch law via directive-conforming interpretation; confirmed by CJEU C-406/10, *SAS Institute v. WPL*), the ideas and principles underlying a computer program are not protectable by copyright. The fact that both products use similar structural approaches reflects common professional practice, not a proprietary connection between the codebases.

The key distinction is:
- **ChipOS** is the broader platform: 11 App Packs, vendor-neutral, serving multiple use cases across semiconductor design
- **Wingman** is a focused application designed for a single purpose: programming Axelera AI accelerator cards

The **delivered version (Wingman v1.0.0)** will be a standalone, self-contained codebase that Axelera can operate independently. Prior to delivery, I will ensure all non-Wingman components are removed and the codebase operates as a standalone application.

### 1.4 The Pilot

During an approximately three-month pilot, Axelera evaluated Wingman as an internal tool for assisting with Voyager SDK programming. The pilot confirmed Wingman's value for Axelera's specific use case. It is this product, Wingman v1.0.0, that I have agreed to deliver to Axelera.

### 1.5 Key Differences

| Aspect | ChipOS | Wingman |
|--------|--------|---------|
| **Purpose** | Vendor-neutral semiconductor orchestration platform | Axelera Voyager SDK programming tool |
| **Scope** | 11 App Packs, multiple workflows | Single application, single use case |
| **Target users** | Any semiconductor engineer | Axelera developers only |
| **Business context** | FutureAtoms independent product | Developed for Axelera's specific needs |
| **Git repository** | Separate repo (extensive independent commit history) | Separate repo |
| **Database** | Own Supabase project | Separate Supabase project |
| **Branding** | FutureAtoms / ChipOS | Voyager Wingman |
| **Licensing** | FutureAtoms proprietary | Licensed to Axelera per this addendum |

### 1.6 FutureAtoms' Broader Scope

It is worth noting that FutureAtoms operates across nine diverse project domains that extend far beyond semiconductors. In addition to ChipOS, FutureAtoms encompasses: **Swaastik** (healthcare platform targeting 150K+ facilities, per FutureAtoms project specifications), **BevyBeats** (music generation), **Zaphy** (LinkedIn networking AI), **Agentic Control** (workflow automation), **SystemVerilogGPT** (RTL generation), **Yuj** (AI wellness/yoga), **Savitri** (mental health CBT/DBT companion), and **AdaptiveVision** (computer vision deployment). The breadth of these projects, spanning healthcare, music, wellness, networking, and automation, underscores that FutureAtoms is not a competitor to Axelera. Scoping the addendum specifically to the Wingman deliverable avoids unintentionally capturing these unrelated activities.

### 1.7 What This Means for the Addendum

The agreed arrangement is the delivery of **Wingman v1.0.0**, an application built for Axelera, with an exclusive license for Axelera to use it with its hardware products. This is a standard software licensing arrangement: the client (Axelera) receives an exclusive license to the deliverable application (Wingman), while the developer (FutureAtoms) retains ownership of the underlying platform (ChipOS) from which it was derived.

The addendum should therefore be scoped to the Wingman deliverable. The proposed draft references **ChipOS** in several places, which I believe was unintentional. The Wingman delivery is what we discussed and agreed upon. The suggestions below are intended to help align the addendum's scope with the actual deliverable.

---

## 2. Suggested Scope Refinements

I am happy to give Axelera very strong Wingman rights, including exclusive use, full source code delivery, and even future development during my employment. The only thing I need is clear separation for my independent projects (ChipOS and FutureAtoms). With that framing, here are some areas where I believe the scope can be refined to capture the intent more precisely:

### 2.1 ChipOS Definition: Scope Alignment (Section 1.2)

The definition includes "any successor, derivative, fork, update, extension, architectural variation or **related technology**." This is broader than necessary for the Wingman delivery and may unintentionally capture future software I develop through FutureAtoms in unrelated domains (healthcare, music, wellness, etc.). I would suggest scoping this to the Wingman v1.0.0 deliverable as defined in the delivery manifest.

### 2.2 License Scope: Wingman vs. ChipOS (Section 1.3a)

Section 1.3a grants Axelera a perpetual, irrevocable, transferable, sublicensable license to the **entire ChipOS platform** rather than the Wingman deliverable. I would suggest scoping this to the Wingman application, which is what Axelera evaluated during the pilot and what we agreed to deliver. ChipOS is a broader, independently developed platform with 11 App Packs serving multiple use cases beyond Axelera. To ensure compliance with **Article 7 of the Auteurswet** (*werkgeversauteursrecht*), it is worth noting that employer copyright arises only where there is a functional connection (*functioneel verband*) between the employment duties and the creative work (see e.g. HR 19 januari 1951, NJ 1952/37, *Van der Laan/Schoonderbeek*). Article 7 Aw applies to software as well as other works and requires that the employee's work "consists of" creating such works and that the works are created "in the service of" the employer. Scoping the license to Wingman ensures the addendum aligns with these statutory requirements.

### 2.3 "Defined Fields": Precision of Scope (Section 1.3b)

The exclusive license scope ("any and all fields of developing software for AI applications on CPUs, GPUs, AIPUs, accelerators, and **any other compute processors**") is broader than necessary for the Wingman delivery scope. As drafted, this may unintentionally capture FutureAtoms projects in entirely unrelated domains (healthcare, music, wellness). I would suggest scoping this to programming Axelera AI accelerator cards, which is what Wingman was built for. This more precise scope also helps ensure compliance with **Article 6:248 lid 2 BW** (*derogerende werking van redelijkheid en billijkheid*), which requires proportionality in contractual terms.

### 2.4 Future Development Scope (Section 1.8)

Section 1.8 claims all developments "whether during or outside working hours and whether at the workplace or elsewhere." I understand the intent is to ensure Axelera captures Wingman-related work, which I fully support. However, to ensure this provision sits on solid legal footing under **Article 7:653a BW** (effective 1 August 2022, implementing EU Directive 2019/1152), which requires objective justification for restricting an employee's activities outside working hours, I would suggest scoping this to Wingman-related developments. This achieves the same protective intent while ensuring compliance.

### 2.5 FutureAtoms Side Activities (Sections 1.13-1.14)

I understand these sections aim to prevent competitive activity, which is a reasonable concern. However, a blanket prohibition on all AI/software business activities is broader than necessary for the Wingman delivery scope and may conflict with:
- **Article 7:653a BW**, which requires objective justification for restricting outside activities; and
- **Clause 13 of my employment agreement**, which permits side activities with consent "not unreasonably withheld on objective grounds."

FutureAtoms generates no revenue, has no external clients, and operates across nine diverse domains (healthcare, music, wellness, etc.) that do not compete with Axelera. I would suggest scoping any restrictions to developing programming tools that directly compete with Wingman for Axelera AI accelerator cards, which achieves the protective intent without affecting unrelated FutureAtoms projects (healthcare, music, wellness, computer vision, etc.) or vendor-neutral semiconductor tooling.

### 2.6 Delivery Scope Clarification (Sections 1.5-1.6c)

The delivery obligation references the "full source code repository for **ChipOS** and Voyager Wingman." Since these are separate repositories (as outlined in the comparison table above), I would suggest updating this to reference the Wingman v1.0.0 repository specifically. This aligns the delivery clause with the actual deliverable and avoids any ambiguity.

### 2.7 Enforcement Rights: Scope Alignment (Section 1.15)

This provision would grant Axelera enforcement rights over ChipOS intellectual property. I would suggest scoping this to the Wingman deliverable IP, which is the subject of the license. Axelera should absolutely have strong enforcement rights over Wingman; I just want to ensure the scope matches the deliverable.

### 2.8 Termination Provisions (Section 1.17)

I understand the desire for license stability, which I fully support. To ensure the provision aligns with the principle of good employer practices (*goed werkgeverschap*) under **Article 7:611 BW**, and noting that Dutch employment termination law is governed by the semi-mandatory regime of **Article 7:669 ff. BW**, I would suggest including standard mutual termination-for-material-breach provisions that operate within this statutory framework, which is common in licensing arrangements and protects both parties.

---

## 3. Counter-Proposal

I have prepared a counter-proposal (attached as **Annex A**) that gives Axelera strong rights to the Wingman deliverable while properly scoping the arrangement to Wingman rather than the broader ChipOS platform. The key terms:

### What Axelera receives:

- **Perpetual, irrevocable, worldwide, exclusive** license to Wingman v1.0.0
- Scope: programming Axelera AI accelerator cards (Metis and successor products)
- Right to use, modify, reproduce, and distribute Wingman to customers **in connection with Axelera hardware**
- Full source code delivery (git archive, tag v1.0.0), Docker images, deployment docs, API docs, SBOM, SHA-256 checksums
- Delivery by **15 April 2026**, with a 30-calendar-day verification period

### What remains with Employee / FutureAtoms:

- FutureAtoms continues operating under clear separation conditions (outside working hours, no Axelera resources, no solicitation, prompt conflict disclosure)
- Clear IP boundary: work within employment scope = Axelera's IP; independent FutureAtoms work = Employee's IP
- ChipOS acknowledged as exclusive FutureAtoms property
- Right to develop similar technology for non-Axelera hardware platforms
- No ongoing maintenance obligation; future versions by separate agreement
- Mutual marketing rights (with prior written approval)

### Compensation (as agreed with Accounts):

- EUR 14,000 gross bonus
- EUR 10,000 in SARs/stock options
- Reimbursement of pilot expenses (~USD 1,400)

A delivery manifest (attached as **Annex B**) specifies exactly what is included in and excluded from the deliverable.

---

## 4. Items Not Included in the Delivery

For absolute clarity, the following are **expressly excluded** from the Wingman delivery and are not covered by this arrangement:

| Excluded Item | Reason |
|---------------|--------|
| ChipOS platform source code | Separate product, FutureAtoms IP (extensive independent commit history, 11 App Packs, vendor-neutral platform) |
| ChipOS git history | Separate repository |
| Non-Wingman App Packs | 11 modules unrelated to Wingman |
| FutureAtoms branding / logos | FutureAtoms proprietary |
| Future Wingman versions (v1.1+) | Not covered; future work by separate agreement |
| ChipOS database / infrastructure | Separate Supabase project |

---

## 5. Conclusion

I believe we are very close to a good agreement. The core of what I am proposing is simple: Axelera gets everything on Wingman (exclusive rights, full source code, the ability to modify and extend it) and my independently operated side business (FutureAtoms) stays separate. Given that FutureAtoms spans nine diverse domains from healthcare to music to wellness, none of which compete with Axelera, I am confident this is a clean separation that works well for both sides.

I am available to discuss the counter-proposal at your convenience and welcome the opportunity to finalise this quickly.

Kind regards,

**Abhilash Chadhar**
Senior Verification Engineer
Axelera AI B.V.

---

## Attachments

- **Annex A:** Counter-Proposal, Addendum to Employment Agreement (Ref: FTA-AXL-2026-CP-001)
- **Annex B:** Wingman v1.0.0 Delivery Manifest

---

## Legal References Cited (for Ensuring Compliance)

| Reference | Subject |
|-----------|---------|
| Art. 7 Auteurswet | Employer copyright (*werkgeversauteursrecht*); requires that the work "consists of" creating such works and that works are created "in the service of" the employer, i.e., a functional connection (*functioneel verband*) between employment duties and the work (see e.g. HR 19 januari 1951, NJ 1952/37, *Van der Laan/Schoonderbeek*). Art. 7 Aw applies to all works including software. |
| Art. 45h Auteurswet | Part of the software chapter (Arts. 45h–45n Aw) implementing EU Directive 2009/24/EC; Art. 45h concerns rental rights (*verhuurrechten*) for software, not employer copyright. Employer copyright for software is governed by Art. 7 Aw (general provision). |
| EU Directive 2009/24/EC Art. 1(2) | Ideas and principles underlying a computer program are not protectable by copyright (CJEU C-406/10, *SAS Institute v. WPL*; applied via *richtlijnconforme interpretatie*) |
| Art. 7:653a BW | Ancillary activities clause (*nevenwerkzaamhedenbeding*); void without objective justification. Effective 1 August 2022, implementing EU Directive 2019/1152. Includes anti-retaliation protection. |
| Art. 7:611 BW | Good employer practices (*goed werkgeverschap*); applies alongside the semi-mandatory termination regime of Art. 7:669 ff. BW |
| Art. 6:248 lid 2 BW | Limitation based on reasonableness and fairness (*derogerende werking van redelijkheid en billijkheid*); a contractual provision is not binding insofar as its application would be unacceptable (*onaanvaardbaar*) per standards of reasonableness and fairness (HR 25 februari 2000, NJ 2000/471) |
| EU Directive 2019/1152 | Transparent and predictable working conditions |
| Clause 13, Employment Agreement | Side activities permitted with consent "not unreasonably withheld on objective grounds" |

---

*This letter and its attachments are confidential and intended solely for the addressee. This communication does not constitute a waiver of any rights or claims.*

---

**DISCLAIMER:** This is an AI-generated document and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and should be reviewed by a qualified Dutch lawyer (advocaat) before use. References to legal provisions should be independently verified.

*Generated by the Netherlands AI Lawyer System*
*Date of analysis: 2026-03-04*
