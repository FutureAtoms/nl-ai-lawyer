# Wingman v1.0.0 Delivery Manifest

**Annex B to Response Letter / Annex 3 to Employment Addendum**

| Field | Value |
|-------|-------|
| Document Title | Wingman v1.0.0 Delivery Manifest |
| Date | 4 March 2026 |
| Party 1 (Employee) | Abhilash Chadhar / FutureAtoms (KvK: 99153289) |
| Party 2 (Employer) | Axelera AI B.V. |
| Document Status | Final (subject to execution of Addendum) |

---

## 1. Purpose

This Delivery Manifest defines the complete scope, contents, acceptance criteria, and handover protocol for the delivery of Voyager Wingman v1.0.0 from Abhilash Chadhar / FutureAtoms to Axelera AI B.V. pursuant to the Employment Addendum between the Parties.

This document serves as the authoritative reference for what is included in, and what is excluded from, the deliverable.

---

## 2. Product Definition

| Attribute | Detail |
|-----------|--------|
| **Product Name** | Voyager Wingman |
| **Version** | 1.0.0 |
| **Description** | Application built for programming Axelera AI accelerator cards using the Voyager SDK |
| **Repository** | Wingman repository (separate from ChipOS) |
| **Delivered as** | Standalone, self-contained codebase |

### Scope Clarification: Items Outside This Delivery

- ChipOS platform (broader platform with extensive commit history, 11 App Packs, vendor-neutral)
- Non-Wingman ChipOS App Packs or modules
- FutureAtoms branding or proprietary components
- Any ChipOS infrastructure not required for Wingman operation

---

## 3. Deliverables Checklist

### 3.1 Source Code

- [ ] Git archive export (tag: `v1.0.0`), Wingman repository ONLY
- [ ] SHA-256 checksum of git archive
- [ ] Git commit log (for provenance verification)
- [ ] `.gitignore` (secrets/credentials excluded)

### 3.2 Container Assets

- [ ] Dockerfile(s) for all services
- [ ] Docker Compose configuration
- [ ] Docker build documentation
- [ ] Pre-built Docker images (if provided; Dockerfiles and build scripts are mandatory)

### 3.3 Documentation

- [ ] Deployment guide (runbook)
- [ ] Configuration templates (all secrets replaced with placeholders)
- [ ] API documentation (OpenAPI/Swagger specs)
- [ ] Architecture overview diagram
- [ ] Environment variable reference

### 3.4 Database

- [ ] Database schema definitions / migrations
- [ ] Seed data (if applicable, anonymized)
- [ ] Supabase project configuration (separate from ChipOS Supabase)
- [ ] Database backup/restore procedures

### 3.5 Compliance & Legal

- [ ] Software Bill of Materials (SBOM)
- [ ] Third-party license inventory
- [ ] License compliance verification
- [ ] Open source dependency list with licenses

### 3.6 Security

- [ ] All secrets, API keys, tokens REMOVED
- [ ] Secret templates/placeholders provided
- [ ] Security configuration guide
- [ ] Authentication/authorization documentation

---

## 4. Acceptance Criteria

### 4.1 Functional Acceptance

- Application builds successfully from source using provided instructions
- All documented API endpoints respond correctly
- Frontend renders and functions as demonstrated during pilot
- Connection to Voyager SDK functions as documented

### 4.2 Documentation Acceptance

- Deployment guide is sufficient to deploy without additional assistance
- All configuration parameters are documented
- API documentation matches actual endpoints

### 4.3 Security Acceptance

- No secrets, credentials, or API keys present in delivered code
- No references to FutureAtoms infrastructure remain
- No connections to ChipOS or other FutureAtoms services

---

## 5. Handover Protocol

### 5.1 Delivery Method

- Encrypted file transfer (method to be agreed)
- OR secure repository transfer
- Delivery confirmation receipt signed by both parties

### 5.2 Verification Period

- **Duration:** 30 calendar days from delivery date
- Employer may raise objections during this period
- Employee available for reasonable clarification questions (maximum 8 hours)
- If no written notice of material deficiencies is provided within the Verification Period: acceptance deemed final
- If material deficiencies are notified within the Verification Period: the deficiency resolution procedure under Article B2.5 of the Addendum applies (15-business-day Cure Period, followed by independent IT expert determination if unresolved). The Testing License continues during the resolution process.

### 5.3 Post-Delivery

- No ongoing maintenance obligation
- No obligation to provide updates, patches, or new versions
- Future development work requires separate agreement and compensation
- Support beyond verification period requires separate agreement

---

## 6. Delivery Boundary Clarifications

| Item | Reason |
|------|--------|
| ChipOS platform source code | Separate product, Employee/FutureAtoms IP |
| ChipOS git history | Separate repository, extensive independent commit history |
| Non-Wingman ChipOS App Packs | 11 packs unrelated to Wingman |
| FutureAtoms branding/logos | FutureAtoms proprietary |
| Future Wingman versions (v1.1+) | Not covered by this agreement |
| ChipOS Supabase project | Separate database/infrastructure |
| Employee's development environment | Personal tooling |

---

## 7. Product Distinction: ChipOS vs Wingman

The following table summarises the key differences between ChipOS (the broader platform retained by FutureAtoms) and Wingman (the deliverable to Axelera). While Wingman uses patterns and approaches from ChipOS, it is an application built specifically for Axelera's needs. The delivered Wingman v1.0.0 will operate as a standalone codebase.

| Aspect | ChipOS | Wingman v1.0.0 |
|--------|--------|----------------|
| **Purpose** | Vendor-neutral semiconductor orchestration platform | Axelera Voyager SDK programming tool |
| **Scope** | 11 App Packs, multiple workflows | Single application, single use case |
| **Target users** | Any semiconductor engineer | Axelera developers only |
| **Business context** | FutureAtoms independent product | Developed for Axelera's specific needs |
| **Git repository** | Separate repo (extensive independent commit history) | Separate repo |
| **Database** | Own Supabase project | Separate Supabase project |
| **Branding** | FutureAtoms / ChipOS | Voyager Wingman |
| **Licensing** | FutureAtoms proprietary | Licensed exclusively to Axelera |
| **Delivered** | Not delivered | Standalone codebase per this manifest |

---

## 8. Pre-Delivery Preparation

Prior to delivery of Wingman v1.0.0, Employee will complete the following preparation steps to ensure the deliverable is a standalone, self-contained codebase:

- [ ] Remove all non-Wingman ChipOS modules and App Packs
- [ ] Remove any components not required for Wingman operation
- [ ] Remove ChipOS branding and references
- [ ] Ensure Wingman operates standalone without ChipOS infrastructure
- [ ] Use `git filter-repo` to remove non-Wingman files while preserving commit metadata, timestamps, and author attribution; archive full unfiltered repository as a separate evidence package before filtering (retained by Employee/FutureAtoms for legal provenance purposes only; NOT part of the delivery to Axelera)
- [ ] Remove all secrets, credentials, and API keys
- [ ] Generate Software Bill of Materials (SBOM)
- [ ] Test standalone deployment and verify all acceptance criteria

---

## 9. Signatures

### Party 1: Employee

| Field | Value |
|-------|-------|
| Name | Abhilash Chadhar |
| Entity | FutureAtoms (KvK: 99153289) |
| Title | |
| Date | |
| Signature | |

### Party 2: Employer

| Field | Value |
|-------|-------|
| Name | |
| Entity | Axelera AI B.V. |
| Title | |
| Date | |
| Signature | |

---

*This document and its contents are confidential.*

---

**DISCLAIMER:** This is an AI-generated document and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and should be reviewed by a qualified Dutch lawyer (advocaat) before use.

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) registered with the Netherlands Bar Association (Nederlandse Orde van Advocaten).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a lawyer.** For legal decisions, proceedings, contracts, or disputes, you must always consult a qualified lawyer authorized to practice law in the Netherlands.

4. **Does not guarantee confidentiality.** Information shared with this AI system is not protected by attorney-client privilege (verschoningsrecht). Do not share confidential or privileged information.

5. **May not reflect current law.** Dutch legislation and case law change continuously. This analysis is based on the state of the law as of the indicated date and may not account for recent amendments.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

7. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal advisor.**

---

*Generated by FALCON (FutureAtoms AI Legal Counsel Of Netherlands)*
*Date of analysis: 2026-03-04*
