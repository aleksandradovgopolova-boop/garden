---
title: "GitHub Controls — Desired and Actual State"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: true
---

# GitHub Controls — Desired and Actual State

## Actual state on 2026-10-05

- Repository public under the owner's final decision, ADR-007. All tracked source and CI logs are publicly readable.
- Pages deleted; the former site returns HTTP 404. Legacy deployment workflow is disabled to prevent manual reruns before this PR merges.
- Main branch protection enabled and read back through GitHub API: PRs, current-branch successful `Documentation quality` and `Public site build` checks, resolved conversations, enforcement for administrators, no force push/deletion.
- One collaborator: project owner `aleksandradovgopolova-boop`.

[github-controls.json](github-controls.json) records the applied configuration. The earlier private-repository attempt returned a plan-related HTTP 403; the owner then chose public visibility. No plan purchase was made.

## Review limitation

Independent and code-owner approval cannot yet be mandatory: the only collaborator is the owner and GitHub authors cannot approve their own PRs. Zero required approving reviews is explicit, not a claim of independent review. CODEOWNERS identifies responsibility; it is not an independent reviewer.

Before requiring independent review, the owner must designate and authorize access for a second human reviewer. Then raise `required_approving_review_count` to 1 and enable code-owner review if appropriate. Do not add collaborators without explicit authorization.

The protected branch can require the new check names before this PR is merged; its own PR run supplies them. The P0 PR remains unmerged for owner review. No agent auto-merge is authorized.
