# Technical and Legal Independence Report: ChipOS vs. Wingman

## (Technisch en Juridisch Onafhankelijkheidsrapport: ChipOS versus Wingman)

**Prepared for:** Abhilash Chadhar / FutureAtoms
**Date:** 4 March 2026
**Classification:** Confidential. Legal Strategy Document
**Purpose:** Establishing clarity for both parties regarding the independent development, distinct architecture, and separate IP status of ChipOS and Wingman, to support accurate scoping of the employment addendum

---

## 1. Executive Summary

This report presents the combined technical and legal evidence demonstrating that **ChipOS** and **Wingman** are two independent products with no runtime dependencies, separate architectures, and distinct ownership status under Dutch law. While Wingman applies general patterns and structural approaches from ChipOS (see Section 6.3), the products are technically and legally separable. The evidence is drawn from:

- **Codebase analysis** of both repositories (git history, source code, architecture, dependencies)
- **Statutory framework** under Dutch copyright law (Auteurswet), patent law (Rijksoctrooiwet 1995), employment law (BW Boek 7), and the EU Software Directive (2009/24/EC)
- **Case law** from the Hoge Raad establishing the functional connection requirement and strict interpretation of employer copyright

**Core finding:** ChipOS is an independently developed, vendor-neutral semiconductor design platform owned by FutureAtoms. FutureAtoms operates across nine diverse domains: semiconductor design (ChipOS), healthcare (Swaastik, targeting 150K+ facilities per FutureAtoms project specifications), music generation (BevyBeats), professional networking AI (Zaphy), workflow automation (Agentic Control), RTL generation (SystemVerilogGPT), wellness (Yuj), mental health (Savitri), and computer vision (AdaptiveVision). This demonstrates that it is a broad technology platform, not a competitor to Axelera's hardware business. Wingman is an application built specifically for Axelera's Voyager SDK, delivered under a separate license. Wingman uses general development patterns and structural approaches from ChipOS (as acknowledged in the counter-proposal's "Shared Development Patterns" provision), but the two products are **independent of each other**: separate repositories, separate databases, separate Docker networks, no runtime imports, and entirely different architectures. The shared developer and shared design patterns do not create employer IP claims over ChipOS, as any attempt to claim employer ownership through the employment relationship fails the cumulative test of Article 7 Auteurswet, as conditions (2) and (3) are not met (condition (1), the existence of an employment relationship, is conceded).

---

## 2. Product Definitions

### 2.1 ChipOS

| Attribute | Details |
|-----------|---------|
| **Full name** | ChipOS: AI Operating System for Semiconductor Design |
| **Repository** | https://github.com/FutureAtoms/ChipOS.git |
| **Owner** | FutureAtoms (eenmanszaak, KvK: 99153289) |
| **First commit** | 15 September 2025 (ad59af6, by FutureAtoms) |
| **Total commits** | Extensive (predominantly FutureAtoms) |
| **Contributors** | FutureAtoms (vast majority); minor contributions from CI automation and AI-assisted commits |
| **Version** | v1.0.1 (released 5 February 2026) |
| **License** | FutureAtoms proprietary license (v1.0, December 2025) |
| **Architecture** | Custom VS Code distribution + FastAPI backend + MCP server |
| **Purpose** | Vendor-neutral agentic orchestration for semiconductor design workflows |
| **Target users** | Any semiconductor engineer (vendor-neutral, not tied to any specific hardware) |

### 2.2 Wingman

| Attribute | Details |
|-----------|---------|
| **Full name** | Voyager Wingman v1.0.0 |
| **Repository** | https://github.com/FutureAtoms/voyager-wingman.git |
| **Owner** | FutureAtoms (delivered to Axelera AI under license) |
| **Total commits** | 3 |
| **Contributors** | FutureAtoms: 3 commits |
| **Version** | v1.0.0 (delivered February 2026) |
| **License** | Voyager Wingman Software License Agreement v1.0 (January 2026) |
| **Architecture** | Full-stack microservices platform (8 Docker services) |
| **Purpose** | AI-powered developer platform for Axelera Metis NPU programming |
| **Target users** | Axelera Voyager SDK developers only |

---

## 3. Technical Independence Evidence

### 3.1 Architectural Separation

ChipOS and Wingman have distinct architectures:

| Aspect | ChipOS | Wingman |
|--------|--------|---------|
| **Type** | Custom VS Code distribution | Full-stack microservices platform |
| **Frontend** | VS Code native UI + embedded webviews | React 18 + Vite SPA (port 4737) |
| **Backend** | FastAPI (port 8181) + VS Code extension host | FastAPI (port 9181) + 7 additional services |
| **Chat** | ChipChat (Continue.dev fork, integrated in VS Code) | LibreChat fork (standalone, port 4080) |
| **MCP server** | Extension IPC-based | HTTP-based (port 9051) |
| **Database** | Supabase (own project) | Supabase (separate project, mandatory) |
| **Authentication** | Supabase OAuth + VS Code auth | Supabase JWT + OAuth + JWKS |
| **Docker services** | VS Code app + backend + MCP | 8 independent containers |
| **Port range** | 3737, 8181, 8051 | 4080, 4737, 5433, 7800, 9051, 9181, 28017 |
| **Network** | chipos-network | wingman-network |

### 3.2 Code Independence

**No runtime cross-imports between the two codebases:**

A search of the Wingman repository for runtime imports from ChipOS modules yields **zero results**:

```
grep -r "from.*chipos\|import.*chipos" backend/ --include="*.py"
→ Returns only database table name references (configuration, not code imports)
```

**Important context:** While Wingman has no runtime dependency on ChipOS, the two products share a developer and Wingman was built using general patterns, structural approaches, and design techniques from ChipOS (see Section 6.3 and the counter-proposal's "Shared Development Patterns" provision). This is analogous to a developer building a general platform and then creating a tailored application for a specific client. The application draws on the developer's experience and patterns but operates as a standalone product.

The two codebases:
- Live in **separate git repositories** with no shared history
- Maintain **separate dependency manifests** (`pyproject.toml`, `package.json`)
- Share **no utility libraries** or runtime modules
- Include **no git submodules** pointing to each other
- Run from **separate Docker Compose configurations** with no cross-references
- Carry **separate VS Code extension IDs** and bundle identifiers

### 3.3 Git Repository Evidence

| Metric | ChipOS | Wingman |
|--------|--------|---------|
| **Remote** | github.com/FutureAtoms/ChipOS.git | github.com/FutureAtoms/voyager-wingman.git |
| **Upstream remotes** | None (origin only) | None (origin only) |
| **Commits** | Extensive (predominantly FutureAtoms) | 3 |
| **Authors** | FutureAtoms (vast majority), minor CI bot and AI-assisted commits | FutureAtoms (3) |
| **First commit date** | 15 September 2025 | February 2026 |
| **Shared git history** | None | None |
| **Shared branches** | None | None |

### 3.4 Database Separation

Each product requires a **separate Supabase project** (separate PostgreSQL instance, separate authentication domain, separate API keys):

| Database aspect | ChipOS | Wingman |
|-----------------|--------|---------|
| **Supabase project** | Own instance | Separate instance (mandatory) |
| **Tables** | chipos_* prefix (15+ tables) | chipos_* prefix (15 tables, renamed from wingman_*) |
| **RLS policies** | Organization-scoped | Organization-scoped (26 policies) |
| **Connection strings** | CHIPOS_SUPABASE_URL | WINGMAN_SUPABASE_URL |
| **API keys** | CHIPOS_SUPABASE_KEY | WINGMAN_SUPABASE_KEY |
| **Data sharing** | None | None |

**Note:** Wingman database tables currently use a `chipos_` prefix due to an earlier naming convention. These tables will be renamed to `wingman_*` before delivery to ensure clear separation. This is a naming convention only, not evidence of code sharing. The tables are in a completely separate database instance. Backward-compatibility views (`wingman_*` → `chipos_*`) exist for migration purposes.

### 3.5 Technology Stack Differences

| Layer | ChipOS | Wingman |
|-------|--------|---------|
| **Core platform** | Electron / Code-OSS (VS Code) | Docker Compose (8 microservices) |
| **Extensions** | 9+ custom VS Code extensions | 3 VS Code extensions (optional) |
| **Chat integration** | Continue.dev fork ("Chip AI") | LibreChat fork ("ChipChat") |
| **Search** | Built-in VS Code search + RAG | MeiliSearch (dedicated container) |
| **Document store** | MongoDB (embedded) | MongoDB (separate container, port 28017) |
| **Vector search** | pgvector (via Supabase) | pgvector (separate container, port 5433) |
| **Customer support** | Zendesk MCP | Zendesk MCP (separate instance) |
| **Build system** | Custom Electron builder + multi-arch scripts | Standard Docker build |

### 3.6 Feature Independence

**ChipOS has 11 AI-native App Packs for chip design:**

1. CPU Development (RISC-V ISA, micro-architecture)
2. RTL Verification (UVM testbenches, SystemVerilog assertions)
3. RTL Debug (waveform analysis, signal tracing)
4. Physical Design (floorplanning, placement, CTS, routing)
5. PD Verification (DRC/LVS/ERC, static timing, IR/EM analysis)
6. Spec Developer (architecture specifications)
7. Hardware Programmer (FPGA workflows, firmware)
8. Axelera Voyager SDK (AI acceleration on Metis APUs)
9. Raspberry Pi (embedded Linux, GPIO)
10. Web Development (React/FastAPI)
11. Documentation (technical writing)

**Wingman has a focused feature set for Axelera:**

1. Voyager SDK pipeline builder (Axelera Metis NPU-specific)
2. RAG knowledge base (documentation search)
3. Multi-model AI chat (14 models, 5 providers)
4. Project/task management
5. Zendesk customer support integration
6. MCP tool integration for Claude Code/Cursor

**Key observation:** While App Pack #8 in ChipOS provides Voyager SDK support within the ChipOS VS Code environment, Wingman implements Voyager SDK support through a separate architecture (8-service Docker microservices vs. VS Code extension). They share a *purpose* (Voyager SDK support) and *general development patterns* from the same developer, but run independently with no runtime dependencies between them.

### 3.7 Independence Verification

Wingman includes a **formal independence verification methodology** that programmatically confirms:
- Docker network is `wingman-network` (not shared with ChipOS)
- All volumes are prefixed with `wingman-`
- Product identity in `product.overrides.json` is correct
- No ChipOS runtime dependencies

### 3.8 Deployment Independence

| Aspect | ChipOS | Wingman |
|--------|--------|---------|
| **Deployment target** | Desktop application (Electron) + GCP Cloud Run (backend) | GCP Cloud Run (all services) |
| **Domain** | futureatoms.com (planned: chipos.ai) | Axelera infrastructure |
| **Docker Compose project** | chipos | voyager-wingman |
| **Can run simultaneously** | Yes | Yes |
| **Requires the other** | No | No |

---

## 4. Legal Framework for IP Independence

### 4.1 The Creator Principle (Makersbeginsel): Art. 1 Auteurswet

The fundamental principle of Dutch copyright law is that **the natural person who creates a work is its author** (maker). This is the starting point. All exceptions, including employer copyright under Art. 7 Aw, must be **strictly interpreted** (*restrictieve interpretatie*).

This principle was reaffirmed by the Hoge Raad in **HR 12 April 2013, ECLI:NL:HR:2013:BY1532 (Stokke/Fikszo, Tripp Trapp)**, which confirmed that the creator principle is the foundation of Dutch copyright law, consistent with the EU requirement of "een eigen intellectuele schepping van de auteur" (an own intellectual creation of the author) per **HvJEU C-5/08 (Infopaq I)**.

### 4.2 Article 7 Auteurswet: Employer Copyright

Article 7 Aw provides an exception to the creator principle for works created in employment. It requires **three cumulative conditions**:

> *"Indien de arbeid, in dienst van een ander verricht, **bestaat in** het vervaardigen van bepaalde werken van letterkunde, wetenschap of kunst, dan wordt, tenzij tusschen partijen anders is overeengekomen, als de maker van die werken aangemerkt degene, **in wiens dienst** de werken zijn vervaardigd."*

1. **Employment relationship** exists
2. **The work consists of** creating such works (must be part of employee's duties)
3. Works were created **in the service of** the employer

Hoge Raad jurisprudence establishes that Art. 7 Aw requires a **functional connection** (*functioneel verband*) between the employment relationship and the creative work (see e.g. **HR 19 januari 1951, NJ 1952/37**, *Van der Laan/Schoonderbeek*). The mere existence of an employment relationship is insufficient.

**Application to ChipOS:** Only one of the three conditions is met, and the remaining two — which are each necessary for Art. 7 Aw to apply — are not:
- (1) Employment exists (conceded)
- (2) ChipOS development was not part of Employee's duties as Senior Verification Engineer: **not satisfied**
- (3) ChipOS was not created "in the service of" Axelera (outside hours, own equipment, own initiative): **not satisfied**

### 4.3 Article 7 Auteurswet: Application to Software

Art. 7 Aw is the **general employer copyright provision** that applies to all works, including computer programs. The EU Software Directive 2009/24/EC Art. 2(3), which provides that the employer is deemed author of computer programs created by an employee "in the execution of his duties" or "following the instructions given by his employer", is implemented in Dutch law through **Art. 7 Aw** (the general employer copyright article), not through Art. 45h Aw. Art. 45h Aw is part of the software chapter (Arts. 45h–45n) and concerns rental rights (*verhuurrechten*) for software, not employer copyright.

Art. 7 Aw requires, as set out in Section 4.2 above, that the employee's work "consists of" creating such works and that the works are created "in the service of" the employer, i.e., there must be a **functional connection** (*functioneel verband*) between employment duties and the creative work.

**EU Directive 2009/24/EC Art. 2(3)** requires that the software was created:
- "in the execution of his duties" **OR**
- "following the instructions given by his employer"

For ChipOS, **neither condition is met**: it was not created in execution of employment duties, and no instructions were given by Axelera for its development.

Under the **richtlijnconforme interpretatie** (directive-conforming interpretation) obligation established in **HR 19 June 2009, ECLI:NL:HR:2009:BH7602 (Buma/Chellomedia)**, Dutch courts must interpret national copyright provisions in conformity with EU directives. This means Art. 7 Aw must be read through the lens of Directive 2009/24/EC when applied to software.

### 4.4 Article 12 Rijksoctrooiwet 1995: Patent Law Analogy

Even patent law, which provides a broader basis for employer claims, **defaults to employee ownership**:

> *"[The employee] has a claim to the patent, UNLESS the nature of the position entails using their special knowledge to make inventions of the same type."*

If patent law protects employee-inventors who develop inventions related to the employer's field, **a fortiori** copyright law, which starts from the creator principle, should offer at least equivalent protection.

**Application:** The "nature" of Employee's position as Senior Verification Engineer does not "entail" developing AI orchestration platforms. Even under the more employer-friendly patent standard, ChipOS would remain Employee's IP.

### 4.5 Article 7:653a BW: Side Activities Freedom

Since 1 August 2022 (implementing EU Directive 2019/1152), employers **may not restrict** employees from performing work outside working hours unless justified by an objective reason. This statutory protection further supports the legal permissibility of Employee's independent ChipOS development through FutureAtoms.

### 4.6 The Task-Based Test (*Taakcriterium*)

The decisive legal test under Dutch law is whether creating the specific type of work was part of the employee's **assigned tasks**, not whether the employer and employee operate in the same general field.

**Key distinction:** Abhilash Chadhar was hired as a **Senior Verification Engineer**. His employment duties involve hardware verification tasks for Axelera's chip products. Developing an AI-powered orchestration platform for semiconductor design is an entirely different activity that falls outside the scope of his employment duties.

The fact that both activities relate to the semiconductor field is **legally irrelevant** under the task-based test. Field relatedness alone does not create employer copyright.

### 4.7 Burden of Proof

The **employer bears the burden** of proving that the conditions of Art. 7 Aw are met, as the party invoking the exception to the creator principle (Art. 1 Aw). In the absence of clear evidence, the creator principle prevails.

---

## 5. Evidence Summary: Why ChipOS Is Employee IP

### 5.1 Temporal Evidence (Created Outside Working Hours)

| Factor | Evidence |
|--------|---------|
| **Git commit timestamps** | ChipOS commits occur in evenings, weekends, and holidays, outside standard working hours |
| **Development duration** | Extensive commits from September 2025 to March 2026, sustained independent effort |
| **No overlap with work hours** | Employer's time registration shows normal working hours only |
| **Personal GitHub account** | Development conducted through personal FutureAtoms GitHub organization |

### 5.2 Resource Independence (Own Equipment and Accounts)

| Factor | Evidence |
|--------|---------|
| **Repository hosting** | Personal GitHub organization (github.com/FutureAtoms) |
| **Cloud services** | Personal Supabase project, personal GCP project |
| **Domain** | futureatoms.com (personally registered) |
| **Infrastructure** | Personal development machine, personal internet connection |
| **API keys** | Personal API keys for all LLM providers, cloud services |
| **No employer resources used** | No Axelera VPN, network, equipment, or licenses used |

### 5.3 Conceptual Independence (Own Idea, Own Direction)

| Factor | Evidence |
|--------|---------|
| **Vendor-neutral design** | ChipOS supports multiple vendors; not limited to Axelera |
| **Independent architecture** | Custom VS Code distribution, distinct from any Axelera product |
| **11 App Packs** | Broad semiconductor coverage; Axelera Voyager SDK is just one of 11 |
| **Business registration** | FutureAtoms (KvK: 99153289) registered independently |
| **Proprietary license** | FutureAtoms proprietary license independent of Axelera |
| **No Axelera input** | No evidence of Axelera direction, instruction, or contribution to ChipOS |

### 5.4 Scope of Employment (Outside Job Duties)

| Factor | Evidence |
|--------|---------|
| **Job title** | Senior Verification Engineer, not software platform developer |
| **Employment duties** | Hardware verification for Axelera chip products |
| **Employment performance** | Employee has actively contributed beyond core duties: developed open-source tooling adopted across the engineering team, represented Axelera at community presentations, and received internal recognition (MVP awards), confirming full engagement in employment role |
| **No IP assignment clause** | Original employment contract does not assign side-project IP to Axelera |
| **Different product type** | AI orchestration platform ≠ hardware verification |
| **Different technology** | VS Code distribution ≠ verification testbenches |
| **Employer never assigned this work** | Axelera never instructed Employee to develop ChipOS |

### 5.5 Knowledge Separation (No Axelera Trade Secrets)

| Factor | Evidence |
|--------|---------|
| **No runtime imports** | Wingman has no runtime imports from ChipOS; ChipOS has no Axelera confidential code |
| **Different codebases** | Separate git repos, separate histories, separate dependencies |
| **Different architectures** | Separate approaches (VS Code distribution vs. Docker microservices) despite shared general patterns |
| **No employer data** | ChipOS contains no Axelera confidential information, customer data, or trade secrets |
| **Vendor-neutral design** | ChipOS supports SkyWater, GlobalFoundries, FreePDK45, ASAP7 (not Axelera-specific) |

---

## 6. Wingman: Properly Scoped Deliverable

### 6.1 What Wingman Is

Wingman is an **application designed specifically for Axelera's Voyager SDK**. It was developed by FutureAtoms specifically for the Axelera engagement and is the **only deliverable** with a legitimate connection to the employment relationship.

### 6.2 Why Wingman Is Not ChipOS

| Criterion | ChipOS | Wingman | Conclusion |
|-----------|--------|---------|------------|
| **Architecture** | VS Code distribution | 8-service Docker microservices | Entirely different |
| **Repository** | FutureAtoms/ChipOS.git | FutureAtoms/voyager-wingman.git | Separate repos |
| **Git history** | Extensive (predominantly FutureAtoms) | 3 commits | Independent histories |
| **Code sharing** | N/A | No runtime imports from ChipOS; shares general patterns | Self-contained |
| **Database** | Own Supabase project | Separate Supabase project | Separate data |
| **Network** | chipos-network | wingman-network | Isolated |
| **Ports** | 3737, 8181, 8051 | 4080, 4737, 5433, 7800, 9051, 9181, 28017 | No overlap |
| **Target users** | Any semiconductor engineer | Axelera developers only | Different markets |
| **License** | FutureAtoms proprietary | Wingman License Agreement v1.0 | Separate terms |
| **Can run independently** | Yes | Yes | No mutual dependency |

### 6.3 Why "General Development Patterns" Do Not Create IP Claims

The counter-proposal (Recital D) acknowledges that Wingman "draws on general development patterns from Employee's independent work." This is legally significant because:

1. **General skills and experience are not trade secrets.** The Hoge Raad's jurisprudence on Art. 7 Aw distinguishes between specific employer IP and general professional skills.
2. **Art. 12 Rijksoctrooiwet 1995** distinguishes between "bijzondere kennis" (special knowledge intrinsic to the role) and general expertise. Using general programming patterns is not using employer IP.
3. **The EU Software Directive** does not capture software that merely uses similar techniques; it requires creation "in the execution of duties."
4. **No developer operates in a vacuum.** Using general patterns, architectures, and approaches learned through professional experience is inherent to professional software development and cannot be the basis for IP claims.
5. **The shared patterns originate from an open-source framework.** The structural patterns and general approaches common to both ChipOS and Wingman are derived from **Agentic Control**, an open-source workflow automation framework independently developed and publicly released by Employee through FutureAtoms. Agentic Control's source code is publicly available (see https://github.com/FutureAtoms/agentic-control-framework), meaning that the patterns in question are accessible to any developer worldwide. Under **Art. 12(1) Rijksoctrooiwet 1995**, publicly available techniques and patterns cannot constitute *bijzondere kennis* (special knowledge intrinsic to the employment role), as they are by definition not proprietary to the employer. Under **Art. 7 Auteurswet**, open-source code that pre-dates and exists independently of the employment relationship cannot be deemed to have been created *in de uitoefening van de dienstbetrekking*. The fact that Employee voluntarily presented Agentic Control at an Axelera company-wide meeting and encouraged colleagues to use it further demonstrates good faith (*goed werknemerschap*, Art. 7:611 BW) and confirms that the sharing of these patterns was an act of voluntary generosity, not a product of employment-directed work.

---

## 7. Addressing Common Questions

| Potential Question | Clarification | Legal Reference |
|---|---|---|
| "ChipOS relates to our field of activity" | Field relatedness is insufficient. The test is **task-based**: was creating ChipOS part of Employee's assigned duties? The answer is no. | Established Hoge Raad jurisprudence on Art. 7 Aw (functional connection requirement; see e.g. HR 19 januari 1951, NJ 1952/37) |
| "Employee used skills learned at Axelera" | General skills and experience are not trade secrets and do not create IP claims. The task-based criterion focuses on what was assigned, not what was learned. | Art. 12(1) Rijksoctrooiwet 1995 (distinguishes bijzondere kennis from general skills) |
| "Dutch law gives Axelera ownership of all employee software" | Art. 45h Aw concerns rental rights, not employer copyright. The correct test is Art. 7 Aw, which requires that software was created "in dienst van" the employer as part of assigned duties. ChipOS was not created as part of Employee's duties. | Art. 7 Auteurswet; Directive 2009/24/EC Art. 2(3); established Hoge Raad jurisprudence (functional connection requirement; see e.g. HR 19 januari 1951, NJ 1952/37) |
| "Employee had a duty of loyalty" | Art. 7:611 BW requires good faith, but not surrender of independently created property. Art. 7:653a BW explicitly protects side activities. | Art. 7:611 BW; Art. 7:653a BW |
| "Our non-compete clause covers this" | Non-compete clauses regulate competitive activity, not IP ownership. They are separate legal instruments. | Art. 7:653 BW (separate from Art. 7 Aw) |
| "Wingman proves ChipOS was created for us" | Wingman is a separate product with no runtime ChipOS imports, separate repo, and a completely different architecture. While Wingman applies general patterns from ChipOS (as transparently acknowledged), the existence of a deliverable for Axelera does not retroactively capture pre-existing independent IP. | Separation evidence in Section 3 |
| "The addendum covers ChipOS" | The addendum has not been signed. Proposed terms that are broader than necessary may be void under Art. 6:248 BW (redelijkheid en billijkheid) and fail the Stoof/Mammoet test (ECLI:NL:HR:2008:BD1847). | Art. 6:248 BW; HR 11 July 2008 (Stoof/Mammoet) |

---

## 8. Forward-Looking Independence Measures

### 8.1 Technical Measures Already in Place

1. **Separate git repositories** with no cross-references
2. **Dedicated Supabase projects** for each product (mandatory, enforced by configuration)
3. **Isolated Docker networks and volumes** (wingman-network vs chipos-network)
4. **Non-overlapping port ranges**
5. **Independence verification methodology** (see Section 3.7 above)
6. **No shared runtime libraries or submodules**

### 8.2 Recommended Additional Measures

1. **Maintain separate development environments** by using different machines or user accounts for ChipOS vs. Wingman development
2. **Continue timestamped commit discipline** to ensure ChipOS commits clearly fall outside Axelera working hours
3. **Document all ChipOS development decisions independently.** Maintain decision logs that demonstrate independent creative direction.
4. **Keep FutureAtoms business records separate**: clean KvK administration, separate invoicing, separate bank account if applicable
5. **Preserve all evidence**, including git history, commit timestamps, personal purchase receipts for equipment/services, and correspondence demonstrating independent development
6. **Secure written approval** for FutureAtoms side activities from Axelera (see side-business-permission-request.md)

---

## 9. Conclusion

The technical evidence is clear: **ChipOS and Wingman are independent products** with no runtime dependencies, architecturally different designs, and no data coupling. While Wingman draws on general patterns and structural approaches from ChipOS (as transparently acknowledged in the "Shared Development Patterns" provision), this does not create employer IP claims over the underlying platform. This technical independence maps directly onto the legal framework for employee IP under Dutch law:

1. **Art. 7 Auteurswet fails** on conditions (2) and (3): ChipOS development is not part of Employee's duties and was not created in the service of Axelera (condition (1) (employment) is conceded)
2. **Art. 7 Aw applied to software** (implementing EU Directive 2009/24/EC Art. 2(3)): ChipOS was not created in the exercise of employment duties, and no employer instructions were given
3. **EU Directive 2009/24/EC fails**: Neither "execution of duties" nor "employer instructions" are present
4. **Art. 12 Rijksoctrooiwet 1995** (by analogy): Even under the more employer-friendly patent standard, ChipOS would remain Employee's IP
5. **Art. 7:653a BW** protects Employee's right to develop ChipOS through FutureAtoms as a side activity

The only deliverable with a legitimate connection to the employment relationship is **Wingman v1.0.0**. While Wingman builds on general development patterns from ChipOS, it runs independently, as shown by the absence of runtime imports, separate repositories, separate databases, and entirely different architectures.

Both parties benefit from a clearly scoped addendum that gives Axelera strong Wingman rights while preserving FutureAtoms' independence across its diverse portfolio of projects. The technical evidence supports limiting the addendum scope to **Wingman v1.0.0**, with express acknowledgment of FutureAtoms' exclusive ownership of ChipOS and all related intellectual property.

---

## Legal References

### Dutch Legislation
- **Art. 1 Auteurswet**: creator principle (makersbeginsel)
- **Art. 7 Auteurswet**: employer copyright (werkgeversauteursrecht)
- **Art. 8 Auteurswet**: organizational authorship
- **Art. 45h Auteurswet**: software rental rights (*verhuurrechten*); part of the software chapter (Arts. 45h-45n Aw) implementing Directive 2009/24/EC. Note: employer copyright for software is governed by Art. 7 Aw, not Art. 45h.
- **Art. 12 Rijksoctrooiwet 1995**: employee patents
- **Art. 7:610 BW**: employment contract definition
- **Art. 7:611 BW**: good employer/employee practices
- **Art. 7:653 BW**: non-competition clause (concurrentiebeding)
- **Art. 7:653a BW**: side activities restriction (nevenwerkzaamhedenbeding)
- **Art. 6:248 BW**: reasonableness and fairness (redelijkheid en billijkheid)
- **Wet bescherming bedrijfsgeheimen**: trade secrets protection

### EU Legislation
- **Directive 2009/24/EC** (Software Directive), Art. 2(3): employer copyright in software
- **Directive 2019/1152** (Transparent and Predictable Working Conditions), Art. 9: parallel employment

### Case Law
- **HR 19 januari 1951, NJ 1952/37** (*Van der Laan/Schoonderbeek*): functional connection requirement for Art. 7 Aw. Note: some secondary sources cite "HR 19 November 1993" for this principle; the full ECLI/NJ citation for that reference could not be independently verified and should be confirmed by counsel before use in proceedings.
- **HR 12 April 2013, ECLI:NL:HR:2013:BY1532** (Stokke/Fikszo, Tripp Trapp): creator principle
- **HR 19 June 2009, ECLI:NL:HR:2009:BH7602** (Buma/Chellomedia): directive-conforming interpretation
- **HR 11 July 2008, ECLI:NL:HR:2008:BD1847** (Stoof/Mammoet): employment term modification test
- **HvJEU C-5/08** (Infopaq I): own intellectual creation standard

---

**DISCLAIMER:** This is an AI-generated analysis and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and must be reviewed and finalized by a licensed attorney admitted to the Dutch bar. All legal citations and technical evidence should be independently verified.

*Generated by the Netherlands AI Lawyer System*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2026-03-04*
