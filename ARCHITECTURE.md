---
title: "ARCHITECTURE.md"
status: draft
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---

# Garden architecture index

## Context

Garden currently contains product documentation and repository verification tools; there is no application runtime. Canonical proposed architecture: [system overview](internal/engineering/architecture/system-overview.md) and [frontend architecture](internal/engineering/frontend/frontend-architecture.md). This index does not approve those proposals.

## System Overview

Public GitHub source; disabled Pages. Documentation CI builds a candidate site with pinned WowRepo. AI Ops Kit 4.9.3 supplies a managed development layer, not Garden application code.

## Components

`public/`: candidate site content; `internal/`: publicly readable team documentation; `scripts/` and `tests/`: repository validation; `.ai/managed/`: checksum-protected Kit package; `.ai/project/`: Garden operational overlays.

## Data Flows

The approved [research slice](internal/delivery/current/first-place-return-spec.md) requires local persistence and no external telemetry. It remains unimplemented. Kit operational metadata must not become a graph of participant data.

## Failure Modes

Repository checks reject broken links and stale manifests. Application persistence, recovery and import/export still need implementation and verification.

## Known Limitations

No backend, accounts, deployed app or live AI. Installation is not full reference-product qualification.
