---
title: "internal/engineering/ai-ops/installation-2026-10-05.md"
status: draft
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---

# AI Ops Kit installation evidence

## Scope and provenance

Installed locally on 2026-10-05 from official tag `v4.9.3`, commit `ad16611cec1ca65a659f597f7b3b0436df8e78b8`, on `codex/garden-ai-ops-install` based on P0 commit `e3c7d7dccd9ca550c4802458f07445cd1e35c088`. This change requires PR review and is not yet on main. Installation branch started at 13:58:23 Europe/Moscow; final CI and PR timestamps remain available in GitHub.

679 managed package files were installed by the official installer. Managed checksums are preserved. Garden config selects Codex and generic runtimes, maps all eight operating contours to existing canonical documents, pins the 4.9.3 qualification range and disables automatic updates. No global Codex prompts were written and no model API was called.

## Verification

Official child, registry, workflow, provider and OpenSpec validators passed after initialization. Doctor passed managed checksums, version compatibility and standalone-engine checks. Repository documentation tests and GitHub CI must also pass before merge; these are separately recorded on the PR.

## Honest limits

Garden application remains unimplemented. Automatic Kit classification inferred EXISTING_PRODUCT from CI/tests/documentation; this is a tooling heuristic, not evidence of an existing application. The generated passport retains that inferred result for traceability. Canonical current scope and plan govern work.

Root ARCHITECTURE, ROADMAP and SECURITY are entry points to existing Garden sources and current repository boundaries. Application architecture/security proposals do not become approved through installation.

Full qualification still requires a bounded application change, independent review, acceptance evidence and rollback. No token cost, productivity gain, research success or production readiness is claimed. Private vulnerability reporting is enabled; repository visibility remains public and Pages remains disabled.

## Delivered workflow correction

The upstream update workflow contained an empty GitHub expression inside a shell comment. GitHub rejected the workflow before execution (run 37300910173). The Garden copy removes that comment token; managed package files remain unchanged. This deliberate delivery-template difference must be preserved or superseded by an upstream fix during updates. Automatic updates remain disabled.

## Protected-main compatibility

Installation merged on 2026-10-05 at 14:29:17 Europe/Moscow. Main run 37303245290 exposed an upstream coverage workflow attempting a direct baseline push, rejected correctly by branch protection. Garden preserves read-only permissions and publishes the proposed baseline as a CI artifact for PR review. Managed package checksums remain unchanged.

CodeQL is configured for Python, the actual repository tooling language. The delivered JavaScript default failed with no source code (run 37303456300); no application JavaScript exists yet.
