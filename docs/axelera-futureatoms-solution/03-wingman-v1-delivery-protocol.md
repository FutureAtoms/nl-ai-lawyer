# Wingman v1.0 Delivery Protocol (Legal + Technical)

Purpose: produce a one-time autonomous Wingman package for Axelera without exposing full ChipOS platform IP.

## 1. Scope Baseline

- ChipOS repository (reference only): `~/uncloud/ChipOS-jan/ChipOS` at commit `e131031`.
- Wingman repository (delivery target): `~/uncloud/ChipOS-jan/voyager-wingman` at commit `091beef`.

## 2. Deliverable Definition

`Wingman v1.0.0` package includes only:

1. Source tree required to build/run Wingman.
2. Build scripts, lockfiles, and dependency list.
3. Deployment documentation and runbooks.
4. Environment variable schema (`.env.example` only, no secrets).
5. Database migrations/schema required for Wingman runtime.
6. Known limitations and handover notes.

`Wingman v1.0.0` package excludes:

1. Unrelated ChipOS apps/modules.
2. Full ChipOS git history unless explicitly licensed.
3. FutureAtoms-internal tooling unrelated to Wingman operation.
4. Personal accounts/tokens/credentials.

## 3. Separation Procedure

1. Start from Wingman repo only.
2. Remove references to non-required ChipOS modules.
3. Replace all secret values with placeholders.
4. Generate third-party dependency inventory and license list.
5. Freeze version as tag `v1.0.0` in Wingman repo.
6. Export release artifacts with checksums.

## 4. Artifact Set

Minimum package:

1. `wingman-v1.0.0-source.tar.gz`
2. `wingman-v1.0.0-docs.tar.gz`
3. `wingman-v1.0.0-artifacts.tar.gz` (optional build images/binaries)
4. `SHA256SUMS.txt`
5. `DELIVERY_MANIFEST.md`
6. `THIRD_PARTY_LICENSES.md`
7. `SBOM` (CycloneDX or SPDX)

## 5. Acceptance Criteria

Axelera acceptance should require successful completion of:

1. Fresh environment build from provided instructions.
2. Startup and health checks passing.
3. Core workflow demonstration (card programming + support workflow used in pilot scope).
4. No dependency on personal accounts of Employee.
5. Secrets successfully rotated to Axelera-owned accounts.

## 6. Accounts and Credential Handover

Transfer or re-create under Axelera ownership:

1. Source repository admin control.
2. Container registry/project ownership.
3. Hosting/runtime accounts.
4. Monitoring/alerting access.
5. Support/ticket integration keys.

Document each transfer in `ACCOUNT_TRANSFER_LOG.md` with timestamp and responsible owner.

## 7. Legal Evidence Bundle

Create evidence files to support IP boundary:

1. `PROVENANCE_STATEMENT.md`
- Explains source repo, snapshot date, and what was removed.

2. `EXCLUDED_COMPONENTS_LIST.md`
- Lists ChipOS components intentionally excluded.

3. `EMBEDDED_COMPONENTS_LIST.md`
- Exhaustive list of any FutureAtoms components that remain embedded.

4. `CONFIDENTIALITY_AND_RESOURCE_SEPARATION_ATTESTATION.md`
- Statement on equipment/time/data separation.

## 8. Version-Lock and Update Rule

Contract language should confirm:

1. Delivery is limited to `Wingman v1.0.0`.
2. Updates, feature requests, and future versions are out of scope unless separately agreed in writing.
3. Axelera may modify internally after delivery.

## 9. Optional Escrow

If requested, place final source + decrypt instructions in escrow with release conditions, e.g.:

1. Employee no longer employed and no support transition available.
2. FutureAtoms dissolution affecting continuity.

## 10. Minimum Security Controls Before Handover

1. Secret scanning pass and remediation.
2. Dependency vulnerability scan at release time.
3. Removal of hardcoded URLs/accounts tied to Employee.
4. Principle-of-least-privilege review for service accounts.

## Legal Disclaimer

Operational checklist for counsel/engineering review; not legal advice.
