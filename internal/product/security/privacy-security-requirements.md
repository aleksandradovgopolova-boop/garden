---
title: "Privacy and Security Product Requirements"
status: accepted
owner: "Product + Security"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
related:
  - ../../engineering/security/security-architecture.md
---

# Privacy and Security Product Requirements

This document defines user-facing and product obligations. Technical controls live in `internal/engineering/security/security-architecture.md`.

## Product requirements

- Garden is private by default.
- Ownership, access and sharing state are visible and understandable.
- Export and deletion are explicit, testable flows.
- AI access to context is bounded and disclosed.
- Analytics exclude private user-authored text by default.
- Destructive actions provide confirmation and recovery where technically possible.
- Authorization is enforced server-side in production.
- High-risk and crisis language is handled without diagnosis or autonomous escalation.

## Product acceptance

A feature cannot be accepted when it creates an unclear data boundary, silent processing, irreversible loss without warning, or an inaccessible privacy control.
