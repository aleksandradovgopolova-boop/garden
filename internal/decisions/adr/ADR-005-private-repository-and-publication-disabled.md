---
title: "ADR-005 — Private Repository and Disabled Publication"
status: superseded
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
---

# ADR-005 — Private Repository and Disabled Publication

Status: accepted

## Decision and approval

On 2026-10-05 the project owner chose “Весь Garden приватный” in the P0 implementation chat. Keep the entire Garden repository private and disable GitHub Pages. `public/` remains a candidate publication surface, not currently published material. CI may build it for verification but must not deploy it or upload a public artifact.

## Alternatives

A public repository with confidential content kept elsewhere was offered and declined. A private repository with a still-public Pages site would not satisfy the selected whole-Garden privacy boundary.

## Consequences

Repository access is granted through GitHub permissions, never directory names. Do not add raw participant data, production private content or credentials to Git even in a private repository. Prior public copies and clones cannot be recalled by changing repository visibility.

## Reopening publication

A new owner-approved decision must specify content, destination and audience, then pass publication review and artifact checks. No automatic re-enablement of Pages is allowed.

## Operational evidence

GitHub API confirmed `private: true` and `visibility: private` on 2026-10-05. Pages was deleted; authenticated lookup returned 404 afterwards. These settings apply independently of whether this documentation PR has merged.

## Supersession

[ADR-007](ADR-007-public-repository-publication-disabled.md) records the owner's later decision on 2026-10-05 to restore public repository visibility. This document preserves the earlier decision and operational history; it is not the current access policy. Pages remains disabled.
