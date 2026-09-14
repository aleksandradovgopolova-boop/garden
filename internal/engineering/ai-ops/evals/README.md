---
title: "AI OPS Eval Suite"
status: accepted
owner: "AI OPS"
updated: 2026-09-14
review_cycle: monthly
source_of_truth: false
---

# AI OPS Eval Suite

This directory holds the evaluation sets that gate model, prompt, tool and
context-policy changes. It operationalizes
`../evals-and-observability.md`; read that document for the metrics and the
release-gate rule.

## Principle

Evaluate the system, not only the model. A change ships only when the fixed
critical safety and privacy cases in `cases.md` pass their thresholds — never
because average quality improved.

## Contents

- `cases.md` — the fixed critical eval cases and their pass rules.

## Data rules

- Use synthetic or consented, minimized examples only.
- Never commit secrets, production private content, real participant data or
  raw research data as fixtures.
- A fixture that would expose internal detail does not belong here.

## Adding a case

1. Pick the category in `cases.md`.
2. Describe the input, the expected safe behavior and the pass threshold.
3. Keep the fixture minimal and synthetic.
4. Record it so a failing case blocks the release gate.
