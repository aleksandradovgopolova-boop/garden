---
title: "Repository Quality Audit"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---

# Repository Quality Audit

## P0 remediation status

Garden is a documentation repository with site-verification tooling; the product application and research results do not exist. Owner decisions made on 2026-10-05 initially selected private visibility, then restored public visibility after the plan limitation; they narrow the first cycle to a local Place/Save/Leave/Return prototype. Pages is deleted and the legacy deploy workflow is disabled.

Three original accepted owner/amendment records were recovered from the July archive without substantive changes to their decision bodies. The decision registry preserves other proposals and scoped supersession. Six documents whose frontmatter overstated their body status were corrected. Old engineering links and inactive CODEOWNERS paths were replaced.

The pinned production renderer now includes all 54 candidate-publication pages, including the 40 nested foundational reports. CI checks metadata, local references, decision completeness, derived counts, artifact coverage/links and publication boundaries. Regression tests inject malformed metadata, missing sections, approval drift and private-artifact leakage.

## Evidence and limits

Current derived counts live in [MANIFEST.json](../../MANIFEST.json) and are regenerated from tracked files. They are not evidence of product functionality. Documentation checks and the production site build must be rerun for the final PR commit.

A targeted history/archive scan checks high-confidence private-key, GitHub-token and AWS-access-key patterns. Its scope and safe counts are recorded in [the exposure audit](repository-exposure-audit.md). This is not a comprehensive secrets, personal-data or scientific-source audit. No historical rewrite is authorized; visibility cannot recall existing copies.

The pinned WowRepo dependency audit found 22 advisories: 5 moderate, 16 high and 1 critical. The engine build is verified; security qualification is not. There is no deployment workflow or public artifact upload. Updating the external engine requires a separate bounded change and another artifact qualification before future publication.

## GitHub controls

Private-repository protection was rejected by the current GitHub plan. Public visibility was restored by the owner to allow protection. Main protection is now enabled with required PRs/checks, current branch, conversation resolution and admin enforcement; see [GitHub controls](github-controls.md) for effective settings. Independent human review still needs an owner-designated second collaborator and must not be described as enforced.

AI Ops Kit 4.9.3 is a pinned candidate only. Installation and compatibility qualification remain P1; approved scope does not authorize a live AI runtime or production backend.
