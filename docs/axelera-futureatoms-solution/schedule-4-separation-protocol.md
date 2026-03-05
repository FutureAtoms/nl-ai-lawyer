# Schedule 4: Resource Separation Protocol

**Referenced by:** Proposed Addendum v2, Articles 2.2 and 7.2
**Date:** 5 March 2026
**Status:** Draft -- subject to execution of Addendum

---

This Schedule defines the technical and organizational measures Employee undertakes to maintain strict separation between Axelera employment activities and FutureAtoms business activities, as required by the Proposed Addendum v2 and the Employment Addendum Counter-Proposal (Articles A2.1 through A2.5).

---

## 1. Time Separation

**Principle:** All FutureAtoms work shall be performed exclusively outside Employee's working hours (buiten werktijd) as defined in the employment agreement.

| Aspect | Axelera Employment | FutureAtoms Activities |
|--------|-------------------|----------------------|
| **Working hours** | Per employment agreement (standard office hours) | Evenings, weekends, holidays, and leave days only |
| **Evidence** | Employer time registration system | Git commit timestamps (verifiable in repository history) |
| **Enforcement** | Employment agreement terms | Counter-Proposal Article A2.1 |

### Compliance Measures

- FutureAtoms git commits occur outside Axelera working hours, as evidenced by repository timestamps
- No FutureAtoms development activity during Axelera contracted working hours
- Clear calendar separation between employment and FutureAtoms activities

---

## 2. Equipment Separation

**Principle:** Employee shall not use any Employer equipment, hardware, software licenses, or infrastructure for FutureAtoms activities (Counter-Proposal Article A2.2(a)).

| Aspect | Axelera Employment | FutureAtoms Activities |
|--------|-------------------|----------------------|
| **Computer** | Employer-provided laptop | Personal development machine |
| **Peripherals** | Employer-provided equipment | Personal equipment |
| **Software licenses** | Employer-licensed tools and IDEs | Personal/FutureAtoms-licensed tools |
| **Mobile devices** | Employer-provided (if any) | Personal devices |

### Compliance Measures

- Physically separate machines for Axelera and FutureAtoms work
- No FutureAtoms source code, repositories, or development environments on Employer equipment
- No Employer-licensed software used for FutureAtoms development

---

## 3. Network Separation

**Principle:** Employee shall not use Employer networks, servers, cloud environments, or development environments for FutureAtoms activities (Counter-Proposal Article A2.2(b)).

| Aspect | Axelera Employment | FutureAtoms Activities |
|--------|-------------------|----------------------|
| **Network** | Employer VPN / office network | Personal internet connection |
| **Cloud environment** | Employer cloud accounts (GCP, AWS, etc.) | Personal/FutureAtoms cloud accounts |
| **Servers** | Employer infrastructure | Personal/FutureAtoms infrastructure |
| **Development environment** | Employer dev environments | Personal dev environments |
| **Docker network** | N/A (Wingman: wingman-network) | ChipOS: chipos-network |

### Compliance Measures

- No FutureAtoms development on Employer VPN or office network
- FutureAtoms cloud services hosted on personal accounts (personal GCP project, personal Supabase)
- FutureAtoms domain (futureatoms.com) registered and managed independently

---

## 4. Data Separation

**Principle:** Employee shall not use Employer confidential information or trade secrets for FutureAtoms activities (Counter-Proposal Articles A2.2(c) and A2.4).

| Aspect | Axelera Employment | FutureAtoms Activities |
|--------|-------------------|----------------------|
| **Confidential information** | Employer trade secrets and proprietary data | No Axelera confidential data used |
| **Customer data** | Employer customer information | No Axelera customer data |
| **Business strategy** | Employer strategic information | Independent FutureAtoms strategy |
| **Technical specifications** | Employer proprietary chip designs | No Axelera technical IP used in ChipOS |

### Compliance Measures

- No Axelera confidential information in FutureAtoms repositories or systems
- No Axelera customer data in FutureAtoms databases
- Conflict of interest disclosure within 5 business days per Counter-Proposal Article A2.5

---

## 5. Git Repository Separation

**Principle:** Source code repositories are maintained in separate, isolated environments with no cross-references.

| Aspect | Axelera / Wingman | FutureAtoms / ChipOS |
|--------|-------------------|---------------------|
| **Repository host** | github.com/FutureAtoms/voyager-wingman.git (delivered to Axelera) | github.com/FutureAtoms/ChipOS.git |
| **Git remotes** | No ChipOS remotes | No Wingman/Axelera remotes |
| **Git submodules** | None pointing to ChipOS | None pointing to Wingman |
| **Shared branches** | None | None |
| **Shared history** | None | None |
| **Runtime imports** | Zero imports from ChipOS | Zero imports from Wingman |

### Compliance Measures

- No git submodules or subtrees linking the repositories
- No shared git history between repositories
- Independence verification methodology confirms isolation (per Independence Report Section 3.7)

---

## 6. Database Separation

**Principle:** Each product operates on a completely separate database instance with no data sharing.

| Aspect | Wingman | ChipOS |
|--------|---------|--------|
| **Supabase project** | Separate instance (mandatory) | Own instance |
| **PostgreSQL instance** | Own database | Own database |
| **Authentication domain** | Separate Supabase auth | Separate Supabase auth |
| **API keys** | WINGMAN_SUPABASE_URL / WINGMAN_SUPABASE_KEY | CHIPOS_SUPABASE_URL / CHIPOS_SUPABASE_KEY |
| **Connection strings** | Separate, non-overlapping | Separate, non-overlapping |
| **Data sharing** | None | None |
| **RLS policies** | Independent (26 policies) | Independent |

### Compliance Measures

- Separate Supabase projects with separate credentials
- No cross-database queries or shared connection strings
- Database table naming conventions clearly distinguish the two products

---

## 7. Ongoing Compliance

Employee commits to maintaining these separation measures for the duration of the employment relationship and to promptly disclosing any situation that may compromise this separation, per Counter-Proposal Article A2.5.

The parties shall review these separation measures as part of the 6-monthly conflict boundary review per Proposed Addendum v2, Article 2.5.

---

**DISCLAIMER:** This is an AI-generated document and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and should be reviewed by a qualified Dutch lawyer (advocaat) before use.

*Generated by FALCON (FutureAtoms AI Legal Counsel Of Netherlands)*
