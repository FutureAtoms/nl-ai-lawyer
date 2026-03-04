# Sector-Specific Contract Review Playbooks - Netherlands

Reference guide for identifying and negotiating key contractual issues across major Dutch business sectors.

---

## 1. SaaS/IT Contracts

### Service Level Agreements (SLA)

**Key Benchmarks:**
- Standard uptime guarantees: 99.5% (monthly), 99.9% (premium)
- Calculation period: rolling 30-day windows (most favorable to customer)
- Planned maintenance windows: typically excluded (8 hours/month acceptable)

**Penalty Mechanisms:**
- Service credits (percentage of monthly fees) for downtime levels:
  - 95-99.5% uptime: 10% credit
  - 90-95% uptime: 25% credit
  - <90% uptime: 50% credit
- Cumulative caps: max 12 months credits/year (prevents unlimited liability)
- Credits as sole remedy vs. termination right (negotiate both)
- Force majeure exclusions: clearly defined (cyberattacks, government action)

### Escrow Arrangements for Source Code

**Typical Structure:**
- Third-party custodians: Escrow4all, NCC Group, Fortium (Dutch-based)
- Release triggers:
  1. Provider bankruptcy/insolvency (primary)
  2. Material SLA breach (uncured >60 days)
  3. IP infringement litigation threat
- Verification procedure: 10-15 days for customer to verify code completeness
- Costs: typically 0.75-1.5% of contract value annually
- Escrow4all standard terms: EUR 1,500-2,500 setup + 800-1,200 annual maintenance

### Data Processing Agreements (Verwerkersovereenkomst)

**AVG Compliance (GDPR-equivalent):**
- Mandatory for any personal data processing
- Include standard terms under Art. 28 GDPR (replicated in AVG)
- Sub-processors: requires prior written consent (Art. 28(2) GDPR)
- Data subject rights: data portability, deletion procedures
- Audit/inspection rights: minimum annual, 30-day notice standard
- Data breach notification: provider to notifier within 24 hours
- DPA as contractual annex (not separate agreement preferred in Netherlands)

### Intellectual Property Ownership

**Custom Development vs. Standard Platform:**
- Standard platform/modules: vendor retains ownership
- Custom modifications: typically work-made-for-hire (obra op bestelling)
- Pre-existing vendor tools/components: license grant only
- Client background IP: client retains unless incorporated in deliverables
- Third-party components: list required in Schedule (open source audits mandatory)
- Patent indemnity: limited to infringement of Dutch law (territory-specific)

### Exit Assistance Obligations

**Art. 7:408 BW (Mandate/Opdracht) Requirements:**
- Data export: within 30 days, machine-readable format (CSV/JSON/API)
- User access maintenance: 90-day transition period post-termination
- Knowledge transfer: 40 hours of technical support standard
- Documentation: all relevant source code documentation, configuration guides
- Runbooks: operational procedures for system management
- Failure to assist creates liability for damages (duty of good faith)

### Limitation of Liability

**Typical Caps (Customary Netherlands Practice):**
- Standard cap: 1x annual contract value
- Critical SaaS services: 2-3x annual value (negotiate down from vendor request)
- Data breach/security incidents: often uncapped in vendor terms
- Indemnification: separate cap (usually 1x annual minimum)
- Carve-outs (unlimited liability):
  - Death/bodily injury
  - Data protection violations (AVG)
  - IP infringement
  - Gross negligence/willful misconduct (bewuste roekeloosheid)
  - Breach of confidentiality
- Force majeure: excludes from liability but not from SLA measurement

### Standard Terms References

**Netherlands ICT General Terms (Commonly Used):**
- NLdigital Standard Terms (developed by industry association)
- ICT~Office standard conditions (smaller vendors)
- FENIT/FENIT-L: licensed frameworks by The Netherlands ICT association
- Always check: Art. 6:233 BW (unreasonable burdensome clauses void)
- Common negotiation points: payment terms (30 days vs. 45 days), renewal auto-extension

---

## 2. Distribution/Agency Agreements

### Agentuurovereenkomst (Commercial Agent)

**Legal Framework: Art. 7:428-445 BW**
- Applies when agent acts for/on behalf of principal in business transactions
- Cannot be contracted out entirely (mandatory minimum protections)
- Dutch courts strictly interpret "acting on behalf" requirement

**Mandatory Goodwill Compensation (Klantenvergoeding):**
- Art. 7:437 BW: upon termination, agent entitled to compensation
- Trigger: agent brought customers/significantly increased existing customers' business
- Calculation: reasonable remuneration based on:
  - Value of business with customers agent brought
  - Duration of representation
  - Customary practices in sector
- Range: 6-12 months commissions typical
- Non-waivable: cannot be reduced by contract terms (Art. 7:445 BW)

### Non-Compete Clauses

**Maximum Duration: 2 Years Post-Termination (Art. 7:443 BW)**
- Longer clauses void and unenforceable
- Must be in writing (Art. 7:445 BW)
- Scope: defined customer/territory limitations acceptable
- Exceptions: non-solicitation of existing customers allowed beyond 2-year period
- Carve-out for subsequent agent appointment (can include non-compete)

### EU Vertical Block Exemption Regulation (VBER)

**Applicability (Regulation (EU) 330/2010):**
- Applies to distribution/agency relationships
- Safe harbor: if combined market share <30% (reseller) or <10% (agent)
- Restrictions allowed:
  - Territorial/customer restrictions (limited)
  - Minimum purchase obligations
  - Stock requirements (reasonable level)

**Hard-core Restrictions (Prohibited - Art. 4 VBER):**
- Price fixing/RPM (Art. 4(a))
- Customer/territorial restrictions preventing exports
- Duty to inform on discounts offered to end-customers
- Refusal to supply to alternative distribution channels

### Selective vs. Exclusive Distribution

**Selective Distribution:**
- Principal selects limited number of resellers based on qualitative criteria
- VBER-safe if criteria:
  - Non-discriminatory
  - Objectively justified (technical competence, investment)
  - Necessary to maintain brand positioning
- Agency agreements: typically selective (principal controls customer relationships)

**Exclusive Distribution:**
- Single distributor for territory; principal agrees not to appoint competitors
- Requires explicit VBER safe-harbor analysis
- Territorial exclusivity: generally acceptable (Art. 1(1)(c) VBER)
- Customer allocation: more restrictive, requires justification

### Minimum Purchase Obligations & Stock Requirements

**Enforceability Standards:**
- Must be proportionate and reasonable
- Cannot serve as disguised exclusivity
- Documentation: clear targets in schedule/appendix
- Quarterly/annual assessment: tied to market conditions
- Adjustment clause: if market declines >20%, obligations may be renegotiated
- Enforcement: termination only after 60-90 day cure period

### Price Maintenance Prohibition

**Art. 6 Mw (Cartel Prohibition) / VBER Art. 4(a):**
- Resale price maintenance (RPM) prohibited
- Exception: maximum price (less restrictive)
- Agent commissions: can be fixed (agent is not independent reseller)
- Recommended pricing: acceptable if non-binding suggestion
- Penalties: NMa enforcement authority; fines up to 10% turnover
- Vertical agreements cartel risk: minimize written price discussions

---

## 3. Construction/Aanneming van Werk

### UAV Standard Terms

**UAV 2012 (Uniforme Administratieve Voorwaarden):**
- Most commonly used framework in Dutch construction
- UAV-GC 2005: general conditions (general contractor)
- UAV-GC 2005-2: simplified version for smaller projects (<EUR 50k)
- Replaces individual contract negotiation in most cases
- Incorporation: must be explicitly referenced in contract

**Legal Basis: Art. 7:750-769 BW (Aanneming van Werk)**
- Contractor obligations: perform work according to specification
- Acceptance (oplevering): buyer's explicit acceptance creates milestone
- Payment: tied to acceptance; milestone-based payments standard
- Right to payment: only upon proper performance (no automatic invoicing)

### Raad van Arbitrage voor de Bouw (RAB)

**Dispute Resolution Forum:**
- Mandatory for UAV 2012 contracts
- Arbitration procedure: faster than litigation (6-12 months typical)
- Three-arbitrator panel for contracts >EUR 1 million
- Single arbitrator: <EUR 500k
- Costs: party-pays-own unless clear winner determined
- Appeal: limited to points of law (not fact-finding)

### Oplevering & Gebrekenaansprakelijkheid

**Acceptance (Oplevering) Requirements:**
- Formal transfer of work from contractor to buyer
- Inspection procedure: 10-30 days standard post-completion notice
- Acceptance certificate: required for payment obligation to arise
- Provisional acceptance: allows minor defects; fixes deadline for remedy
- Final acceptance: after 1 year warranty period (garantietermijn)

**Hidden Defects Liability (Gebrekenaansprakelijkheid):**
- 5-year statute of limitations from final acceptance (Art. 7:759 BW)
- Contractor liable for defects discovered within 5 years
- Exception: obvious defects at acceptance (buyer's inspection duty)
- Latent defects: discovered after final acceptance, contractor still liable
- Limitation: cannot be contracted out (mandatory protection, Art. 7:760 BW)

### Meerwerk/Minderwerk Procedures

**Extra Work (Meerwerk):**
- Definition: work outside original scope
- Approval: written authorization required before commencement
- Price adjustment: agreed in advance or "customary prices" if not specified
- Documentation: detailed daywork records (timesheets, materials)
- Cost verification: invoiced within 30 days of completion

**Deduction Work (Minderwerk):**
- Definition: work scope reduction or non-performance
- Buyer's remedy: price reduction (not deduction from final payment)
- Procedure: buyer must notify contractor within acceptance period
- Amount: reasonable proportion of contract price saved
- Dispute resolution: if parties disagree on value (RAB arbitration)

### Retentierecht & Bankgaranties

**Retentierecht (Payment Holdback):**
- Standard: 5-10% of each invoice retained until final acceptance
- Purpose: security for defect remediation
- Duration: typically 1 year from final acceptance (or 2 years for major defects)
- Release: upon final acceptance certificate
- Non-waivable under UAV 2012 (mandatory provision)

**Bankgaranties (Performance Bonds):**
- Typical: 10% of contract value
- Types:
  1. Advance payment guarantee: protects employer advance payments
  2. Performance guarantee: security for proper completion
  3. Defects guarantee: security for 5-year liability period
- Issuer: EU-licensed bank acceptable; Dutch bank standard
- On-demand guarantee: must specify (not usual in construction)

### DNR 2012 for Design Professionals

**DNR 2012 (Design Terms for Architects/Engineers):**
- Covers design phase: feasibility through working drawings
- Applies to independent designers (not design-build contractors)
- Key provisions:
  - Designer liability: limited to design phase defects
  - Builder responsible for execution defects
  - Progress payments: typically 5 milestones during design
  - Intellectual property: designer retains unless bought-out (explicit clause)
- Integration: often used alongside UAV 2012 (design phase separately)

---

## 4. Healthcare/Zorgsector

### WGBO (Gedragsregels Gezondheidszorg)

**Legal Framework: Art. 7:446-468 BW**
- Rights of patients/clients in healthcare relationships
- Applies to care providers (doctors, dentists, therapists)
- Cannot be contracted out (mandatory protection)

**Key Patient Rights:**
- Right to information: adequate disclosure before treatment
- Right to refuse treatment: must be respected
- Confidentiality: medical records confidential (Art. 7:458 BW)
- Access to records: patient may request copies of medical file
- Medical file retention: minimum 20 years (professional standard)

### NZa Regulations & Maximum Tariffs

**Dutch Health Authority (NZa):**
- Regulates maximum tariffs for health services
- Applies to insurance-reimbursable treatments
- Tariff book: published annually; compliance mandatory
- Private billing: allowed above NZa maximum if patient informed in advance
- Billing transparency: must provide estimate before service

### Zorgverzekeringswet Requirements

**Health Insurance Law:**
- Healthcare providers must have NZa registration
- Insurance contracts: defined benefits packages (mandatory coverage)
- Referral requirements: some treatments require GP/specialist referral
- Pre-authorization: insurer may require for high-cost treatments
- Direct billing: provider may bill insurer directly if contracted

### Informed Consent Requirements

**Standard: Art. 7:450 BW (Toestemming voor medische behandeling)**
- Written or documented oral consent required
- Must be informed: patient understands nature, risks, alternatives
- Capacity: patient must be mentally capable (minor parents/guardians decide)
- Emergency treatment: consent implied if patient cannot decide
- Withdrawal: patient may withdraw consent at any time
- Documentation: written evidence of consent discussion (Dutch hospitals standard)

---

## 5. Franchise Agreements

### Wet Franchise (Effective 1 January 2021)

**Legal Framework: Art. 7:911-922 BW**
- Mandatory minimum protections; cannot be waived entirely
- Applies to ongoing commercial relationship where franchisor provides:
  - Trade name/brand
  - Know-how/commercial systems
  - Continuous assistance/support
- Reciprocal performance exchange: franchisee pays fees (upfront/ongoing)

**Scope:**
- Retail franchises (most common)
- Service franchises (cleaning, tutoring services)
- Manufacturing franchises (less common in Netherlands)

### Pre-Contractual Disclosure Obligations

**Art. 7:913-916 BW (Disclosure Requirements):**
- Timeline: information disclosed minimum 14 days before signing
- Content must include:
  1. Franchisor identification: corporate info, legal structure
  2. Business details: years of operation, number of franchisees
  3. Financial information: annual turnover, number of franchises per territory
  4. Litigation history: lawsuits involving franchisor (5-year lookback)
  5. Insolvency/bankruptcy: previous proceedings
  6. Experience: franchisor/management background in franchising
  7. Costs/fees: initial franchise fee, royalties, marketing contributions
  8. Restrictions: territorial/customer limitations
  9. Confidentiality: NDA terms
  10. Training: type, duration, costs
  11. Support services: ongoing assistance provided
  12. Trademarks/IP: licensing rights, protection responsibility

**Violations:** Franchisee may terminate and claim damages (Art. 7:920 BW)

### Goodwill Compensation on Termination

**Art. 7:918 BW (Winstderving, Goodwill Compensation):**
- Upon termination/non-renewal: franchisee entitled to indemnity
- Condition: franchisee brought significant goodwill/customer base
- Applicable: if relationship lasted >2 years
- Calculation:
  - Comparable to agentuurovereenkomst (see Distribution section)
  - 6-12 months royalties typical
  - Based on business value contributed
- Non-waivable: cannot be eliminated by contract
- Professional indemnity: non-compete may replace goodwill compensation

### Non-Compete Restrictions

**Maximum Duration: 1 Year Post-Termination (Art. 7:919 BW)**
- Applies to franchisee
- Scope: same territory, similar business
- Longer periods: void and unenforceable
- Customer non-solicitation: separate right, may extend beyond 1 year
- Geographic scope: must be clearly defined (not entire Netherlands if unreasonable)
- Exception: franchisor may require trade secret protection longer (rare, requires justification)

**Enforceability:**
- Must be reasonable regarding territory/activity
- Cannot prevent franchisee from working in related fields
- Covenant not to sue: franchisor waiver of enforcement (increasingly common)

---

## Cross-Sector Contract Review Principles

**Always check:**
1. Mandatory statutory protections: cannot be contracted out in above sectors
2. Unreasonable Burden Test (Art. 6:233 BW): terms heavily favoring one party void
3. Incorporation of standard terms: must be clearly referenced; conflicting terms (oral vs. written) resolved in favor of non-drafter
4. Governing law: Netherlands preferred for enforceability; EU jurisdiction clauses subject to recast Brussels Regulation
5. Dispute resolution: arbitration in Dutch framework (RAB, NOM, WICE) more efficient than litigation

**Documentation Always Required:**
- Written contract (geen handschoen contract)
- Standard terms incorporation clause
- Schedules/appendices: payment terms, delivery specifications, pricing
- Signature/acceptance evidence
- AVG compliance (if personal data involved)

---

**Last Updated:** March 2026
**Jurisdiction:** Kingdom of the Netherlands
**Governing Law Reference:** Dutch Civil Code (Burgerlijk Wetboek), Books 3, 6, and 7
