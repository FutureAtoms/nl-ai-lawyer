# Schedule 1: Wingman v1.0.0 Deliverables

**Referenced by:** Proposed Addendum v2, Article 1.2 and Article 6.1
**Date:** 5 March 2026
**Status:** Draft -- subject to execution of Addendum

---

This Schedule defines the complete scope of deliverables, acceptance criteria, and handover artifacts for Wingman v1.0.0 as referenced in the Proposed Addendum v2 (Article 1.2) and the Employment Addendum Counter-Proposal (Article B2.2).

---

## 1. Source Code

| Deliverable | Description |
|-------------|-------------|
| Git archive export | Complete source code of Wingman v1.0.0, tagged as `v1.0.0`, from the Wingman repository **only** |
| SHA-256 checksum | Integrity verification hash of the git archive |
| Git commit log | Provenance verification of all commits |
| `.gitignore` | Confirming exclusion of secrets and credentials |

**Exclusion:** The ChipOS repository, any other FutureAtoms repositories, or any ChipOS source code are expressly **not** included in this delivery (per Counter-Proposal Article B2.2(a)).

---

## 2. Container Assets and Build Files

| Deliverable | Description |
|-------------|-------------|
| Dockerfile(s) | For all Wingman services (8-service Docker microservices architecture) |
| Docker Compose configuration | Complete orchestration configuration for all services |
| Docker build documentation | Instructions to reproduce Docker images from source |
| Pre-built Docker images | If provided; Dockerfiles and build scripts are mandatory in all cases |

---

## 3. Documentation

| Deliverable | Description |
|-------------|-------------|
| Deployment guide (runbook) | Sufficient to deploy Wingman v1.0.0 without additional assistance |
| Configuration templates | All secrets replaced with placeholders |
| API documentation | OpenAPI/Swagger specifications matching actual endpoints |
| Architecture overview diagram | System architecture of the 8-service microservices platform |
| Environment variable reference | Complete list of all configuration parameters |
| Database schema definitions | Schema definitions and migration scripts |
| Database backup/restore procedures | Procedures for Supabase project backup and restore |

---

## 4. Database

| Deliverable | Description |
|-------------|-------------|
| Schema definitions / migrations | Complete database schema for the separate Wingman Supabase project |
| Seed data | If applicable, anonymized |
| Supabase project configuration | Separate from ChipOS Supabase; own instance with own API keys |
| RLS policies | All 26 row-level security policies |

---

## 5. Compliance, Security, and Integrity

| Deliverable | Description |
|-------------|-------------|
| Software Bill of Materials (SBOM) | Listing all dependencies, libraries, and their licenses |
| Third-party license inventory | Complete inventory of all open-source and third-party licenses |
| License compliance verification | Confirmation of compliance with all dependency licenses |
| SHA-256 checksums | For all delivered files and images |
| Secret removal confirmation | Confirmation that all secrets, credentials, API keys, and personal data have been removed |
| Secret templates/placeholders | Placeholder configuration for all required secrets |
| Security configuration guide | Authentication and authorization documentation |

---

## 6. Acceptance Criteria

### 6.1 Functional Acceptance

- Application builds successfully from source using provided instructions
- All documented API endpoints respond correctly
- Frontend renders and functions as demonstrated during pilot
- Connection to Voyager SDK functions as documented

### 6.2 Documentation Acceptance

- Deployment guide is sufficient to deploy without additional assistance
- All configuration parameters are documented
- API documentation matches actual endpoints

### 6.3 Security Acceptance

- No secrets, credentials, or API keys present in delivered code
- No references to FutureAtoms infrastructure remain
- No connections to ChipOS or other FutureAtoms services

---

## 7. Handover Protocol

### 7.1 Delivery Method

- Encrypted file transfer (method to be agreed) or secure repository transfer
- Delivery confirmation receipt signed by both parties

### 7.2 Verification Period

- **Duration:** 30 calendar days from delivery date
- Employer may raise objections during this period
- Employee available for reasonable clarification questions (maximum 8 working hours)
- If no written notice of material deficiencies is provided within the Verification Period: acceptance deemed final
- If material deficiencies are notified: deficiency resolution procedure under Counter-Proposal Article B2.5 applies

### 7.3 Post-Delivery

- No ongoing maintenance obligation
- No obligation to provide updates, patches, or new versions
- Future development work requires separate agreement and compensation

---

## 8. Items Expressly Excluded from Delivery

| Excluded Item | Reason |
|---------------|--------|
| ChipOS platform source code | Separate product, Employee/FutureAtoms IP |
| ChipOS git history | Separate repository, extensive independent commit history |
| Non-Wingman ChipOS App Packs | 11 packs unrelated to Wingman |
| FutureAtoms branding/logos | FutureAtoms proprietary |
| Future Wingman versions (v1.1+) | Not covered by this agreement |
| ChipOS Supabase project | Separate database/infrastructure |
| Employee's development environment | Personal tooling |

---

**DISCLAIMER:** This is an AI-generated document and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and should be reviewed by a qualified Dutch lawyer (advocaat) before use.

*Generated by FALCON (FutureAtoms AI Legal Counsel Of Netherlands)*
