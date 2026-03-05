# Comprehensive Legal Solution: Protecting FutureAtoms, ChipOS IP, and Employment at Axelera

**Date:** 4 March 2026
**Prepared for:** Abhilash Chadhar
**Status:** Design Document (Internal Only)

---

## The Problem

Axelera's legal department proposed employment addendum clauses 1.1-1.19 that would:
- Capture the entire ChipOS platform (not just Wingman)
- Claim ownership of all future IP, including off-hours work
- Require suspending FutureAtoms
- Grant Axelera enforcement rights over IP it doesn't own
- Demand delivery of the full ChipOS repository

You need to: (1) keep your permanent job, (2) protect ChipOS IP, (3) keep FutureAtoms running, and (4) deliver Wingman fairly.

---

## The Solution: "Licensed Derivative" Model

A standard software licensing arrangement where Axelera receives an **exclusive license** to the Wingman deliverable for its hardware products, while FutureAtoms retains ownership of the underlying ChipOS platform.

This is how every major software company handles derivative products: the client gets the deliverable, the developer keeps the platform.

---

## Five Legal Pillars

### Pillar 1: Employment Law -- Art. 7:653a BW (Side Activities)

**What it says:** Since 1 August 2022, an employer CANNOT prohibit side activities without objective justification. Implements EU Directive 2019/1152, Art. 9.

**How it protects you:**
- Axelera's blanket prohibition (clauses 1.13-1.14) is **void** under this article
- Your employment contract Clause 13 already permits side activities with consent "not unreasonably withheld on objective grounds"
- 34% of Axelera employees maintain concurrent side businesses -- denial is indefensible
- Anti-retaliation protection: Art. 7:653a lid 2 prohibits disadvantaging you for asserting this right
- A founding team member operates a concurrent technology company; a peer-level engineer operates a software development business (see anonymized comparators in axelera-dual-roles-precedent.md)

**In the counter-proposal:** Part A formally discloses FutureAtoms and secures written approval with objective separation conditions (outside hours, own equipment, no solicitation, no trade secrets, prompt conflict disclosure).

### Pillar 2: IP Law -- Art. 7 Auteurswet + Art. 12 ROW 1995

**What it says:** Employer copyright is limited to works created (a) within employment duties, (b) using employer resources, (c) under employer direction. Independent work on own time/equipment = employee's IP.

**How it protects you:**
- ChipOS was developed independently, outside working hours, using your own equipment
- Art. 7 Aw does NOT give Axelera copyright over ChipOS
- Wingman is a derivative that can be **licensed** without transferring the underlying platform
- The "Embedded Components" clause (Art. B1.4) honestly addresses shared patterns while limiting the license to Wingman use only

**In the counter-proposal:** Art. A3 establishes clear IP boundary. Art. A3.3 explicitly acknowledges ChipOS as exclusive FutureAtoms IP. Art. A3.4 prevents testing/demos from creating ownership claims.

### Pillar 3: Contract Law -- Art. 6:248 BW (Reasonableness and Fairness)

**What it says:** Contract clauses are unenforceable if they are unacceptable according to standards of reasonableness and fairness (*derogerende werking van redelijkheid en billijkheid*).

**How it protects you:**
- "All of computing" exclusive license scope is disproportionate and likely unenforceable
- Irrevocable waiver of all termination rights is one-sided
- Capturing all future IP regardless of creation context is unreasonable
- Art. 7:611 BW (good employer practice) requires balanced terms

**In the counter-proposal:** License scoped to Axelera hardware products only. Standard termination-for-breach provisions. Future IP split by creation context.

### Pillar 4: Immigration Law -- Art. 3.30a Vb 2000 (HSM Permit)

**What it says:** HSM (kennismigrant) permit is tied to permanent employment with a recognized sponsor.

**How it protects you (and constrains you):**
- You MUST remain a permanent employee -- your residence depends on it
- HSM permit valid until 15 November 2027; citizenship eligible ~December 2027
- Side business alongside employment IS permitted (no obligation to report eenmanszaak to IND)
- Switching to contractor would FAIL: FutureAtoms has EUR 0 revenue, zelfstandige permit requires 300+ points and proven business viability
- Any gap in residence could reset the 5-year citizenship clock (Art. 8 Rijkswet op het Nederlanderschap)

**In the counter-proposal:** Compensation flows through employment (bonus/SARs), preserving the employment relationship and permit basis.

### Pillar 5: Tax Law -- Wet DBA (Schijnzelfstandigheid)

**What it says:** If a contractor works primarily for one client, tax authorities may reclassify as employment, with back-taxes and penalties for both parties.

**How it protects you:**
- You must NOT invoice Axelera from FutureAtoms for overlapping services
- Wingman compensation (EUR 14K bonus + EUR 10K SARs + ~USD 1.4K expenses) flows through payroll
- FutureAtoms income (when it comes) from external clients gets declared separately

**In the counter-proposal:** Art. B6 structures all compensation through the employment relationship.

---

## Document Architecture

### Tier 1 -- Send to Bram (This Week)

| # | Document | File | Purpose |
|---|----------|------|---------|
| 1 | Cover message | `cover-message-to-bram.md` | Bram reads, forwards attachments |
| 2 | Response letter | `response-to-axelera-legal.md` | For legal: concerns + proposed scope |
| 3 | Counter-proposal | `employment-addendum-counter-proposal.md` | For legal: replacement addendum |
| 4 | Delivery manifest | `wingman-delivery-manifest.md` | For legal/engineering: what's delivered |

### Tier 2 -- Hold in Reserve

| Document | File | Deploy When |
|----------|------|-------------|
| Side business permission request | `side-business-permission-request.md` | If legal says "we need formal process" |
| Addendum analysis | `axelera-addendum-analysis.md` | If legal says "be more specific" |
| 34% precedent | *Verbal only* | If legal says "we don't allow side businesses" |

### Tier 3 -- NEVER Send

| Document | File | Why |
|----------|------|-----|
| Immigration risk assessment | `immigration-risk-assessment.md` | Reveals you can't afford to lose the job |
| Dual-roles precedent (with names) | `axelera-dual-roles-precedent.md` | Naming colleagues creates backlash |
| Master strategy | `01-master-strategy.md` | Reveals red lines and settlement zone |
| Counsel Q&A / negotiation script | `04-counsel-qa-and-negotiation-script.md` | Private preparation notes |

---

## Counter-Proposal Structure Summary

### Part A: Side Business Permission
- Art. A1: Disclosure and approval of FutureAtoms
- Art. A2: Separation conditions (hours, equipment, no solicitation, no trade secrets)
- Art. A3: IP boundary (employment scope = Axelera; independent work = FutureAtoms)
- Art. A4: ChipOS definition and ownership acknowledgment

### Part B: Wingman Delivery
- Art. B1: Wingman definition (honest derivative framing + Embedded Components clause)
- Art. B2: Delivery scope and timeline (15 April 2026)
- Art. B3: License grant (perpetual, irrevocable, worldwide, exclusive for Permitted Purpose)
- Art. B4: No future obligation
- Art. B5: Explicit exclusions
- Art. B6: Compensation (EUR 14K + EUR 10K SARs + ~USD 1.4K)

### Part C: Marketing Rights
- Mutual rights with prior written approval

### Part D: Conflict of Interest Safeguards
- Art. D1: Narrow non-compete (Axelera accelerator card programming only, employment term only)

### General Provisions
- Governing law: Netherlands
- Disputes: Mediation first, then court
- Severability, amendments, counterparts

---

## Negotiation Strategy

### Red Lines (Non-Negotiable)
1. **ChipOS = FutureAtoms IP** -- no transfer, no broad license to the platform
2. **FutureAtoms continues** -- suspension clause is void under Art. 7:653a BW
3. **Off-hours IP = yours** -- cannot capture what you build on own time/equipment
4. **Remain permanent employee** -- immigration depends on it
5. **No irrevocable waiver** -- both sides need breach remedies

### Acceptable Concessions
1. Broader Wingman exclusive license scope (all AI accelerator cards, not just Axelera-branded)
2. Specific non-compete for named Axelera competitors
3. Detailed embedded components schedule
4. Extended verification period (45 instead of 30 days)
5. Mutual audit rights for separation compliance
6. Periodic written disclosure of FutureAtoms activities

### Verbal Talking Points for Bram
- **"Is this going to be a problem?"** -- "No, the scope just needs to match what we discussed."
- **"Can you just sign the original?"** -- "I can't sign something that captures my entire independent platform and requires shutting down my company. But the counter-proposal gives Axelera everything it needs."
- **"Legal won't like this."** -- "The counter-proposal gives Axelera strong protections. Legal drafted broadly because they didn't have the full context."
- **"What if they say no?"** -- "I'm flexible on details. The core structure just needs to properly scope it to Wingman."

---

## Risk Matrix

| Scenario | Probability | Impact | Action |
|----------|------------|--------|--------|
| Axelera accepts counter-proposal | Medium | Best case | Sign, deliver by 15 April |
| Axelera negotiates details | **High** | Manageable | Use acceptable concessions, preserve red lines |
| Axelera refuses all negotiation | Low | Serious | Deploy Tier 2, invoke Art. 7:653a in writing, consult lawyer |
| Axelera terminates employment | Very Low | Critical | 3-month HSM grace period; consult arbeidsrecht + vreemdelingenadvocaat immediately |

---

## Timeline

| When | Action |
|------|--------|
| **This week** | Send Tier 1 package to Bram (Tuesday/Wednesday morning) |
| **Same/next day** | Brief verbal follow-up with Bram |
| **After 5 business days** | Short follow-up email if no response |
| **Within 1-2 days of pushback** | Respond to legal's counter-points |
| **If fully blocked** | Engage arbeidsrechtadvocaat |
| **Target: End of March 2026** | Signed agreement |
| **15 April 2026** | Deliver Wingman v1.0.0 |
| **Before Dec 2027** | Prepare citizenship application (civic integration, documents) |
| **~December 2027** | Apply for Dutch citizenship |

---

## Legal References

| Reference | Subject |
|-----------|---------|
| Art. 7:653a BW | Side activities protection (void without objective justification) |
| Art. 7:611 BW | Good employer practice (*goed werkgeverschap*) |
| Art. 7 Auteurswet | Employer copyright (limited to employment duties) |
| Art. 6:248 lid 2 BW | Reasonableness and fairness (*derogerende werking*) |
| Art. 12 ROW 1995 | Employee inventions/patents |
| Art. 3.30a Vb 2000 | HSM permit conditions |
| Art. 8 Rijkswet op het Nederlanderschap | Naturalization requirements |
| EU Directive 2019/1152, Art. 9 | Right to parallel employment |
| Wet DBA | False self-employment risk |
| Clause 13, Employment Agreement | Side activities "not unreasonably withheld" |
| Stoof/Mammoet (HR 2008) | Unilateral change test under Art. 7:611 BW |
| Deliveroo (HR 2023:443) | Employment relationship criteria |

---

## Critical Warnings

1. **DO NOT resign or accept termination** without consulting both an employment lawyer and immigration lawyer
2. **DO NOT switch to contractor status** -- zelfstandige permit would almost certainly fail
3. **DO NOT invoice Axelera from FutureAtoms** -- schijnzelfstandigheid risk
4. **DO NOT send** immigration assessment, dual-roles names, or master strategy to Axelera
5. **DO consult a qualified arbeidsrechtadvocaat** before signing any agreement

---

*This document is an AI-generated legal analysis for lawyer review. It does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). All legal citations should be independently verified by qualified Dutch legal counsel.*
