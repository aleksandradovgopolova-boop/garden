---
title: "Context Pack: ADR Authoring"
status: accepted
owner: "AI OPS"
updated: 2026-09-14
review_cycle: quarterly
source_of_truth: false
---

# Context Pack: ADR Authoring

## Mission

Draft a new architecture or governance decision record, or draft a record
that supersedes an existing one.

## Allowed repository paths

- `../../../../internal/decisions/`
- `../../../../templates/adr.md`

## Required sources of truth

- `../../../../internal/decisions/decision-log.md`
- `../../../../internal/decisions/README.md`
- `../../../governance/SOURCE_OF_TRUTH.md`

## Product boundaries

A decision record captures a decision and its consequences. It does not
redefine product Canon or product boundaries.

## Known constraints

- Accepted ADRs are append-only.
- A changed decision creates a new ADR that supersedes the old one; the old
  record is not edited except to mark it superseded.
- Register every new record in `decision-log.md`.

## Prohibited assumptions

- Do not assume a decision is accepted before human approval.
- Do not treat archived decisions as active requirements.

## Expected output

One new ADR file following `templates/adr.md`, an updated decision log, and a
clear statement of risk class and rollback.

## Verification commands

```bash
python scripts/quality_gates.py --gate docs
```

## Reviewed against sources on
2026-09-14
