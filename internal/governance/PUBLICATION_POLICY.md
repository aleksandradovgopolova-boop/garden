---
title: "Publication and Repository Access Policy"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
---

# Publication and Repository Access Policy

## Current access boundary

The entire Garden repository is public under [ADR-007](../decisions/adr/ADR-007-public-repository-publication-disabled.md). GitHub Pages remains disabled. `public/` identifies candidate publication content only; it is not currently served publicly. `internal/` and `archive/` are publicly readable. These folders identify audiences and history, not access controls. Renderer exclusions restrict the site artifact only.

Only publication-safe material belongs anywhere in this repository. Do not put confidential working material, secrets, production private content or raw participant data in Git. Any confidential research store must have its own access and retention controls. Repository visibility cannot recall earlier public copies.

## Future publication gate

Require an explicit owner-approved decision describing audience, destination and content. Rewrite proposed material for external readers, remove sensitive details, review product/privacy/security/accessibility, then approve the publication change. Never render `internal/` or `archive/`; `public/` is the only permitted candidate content root.

CI must pass metadata, references, decision registry and actual artifact checks before publication can be enabled. A successful CI build is not approval to publish. The current workflow has no deployment credentials, Pages job or public artifact upload.
