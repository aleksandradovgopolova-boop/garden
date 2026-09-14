---
title: "Context Pack: Research Study"
status: accepted
owner: "AI OPS"
updated: 2026-09-14
review_cycle: quarterly
source_of_truth: false
---

# Context Pack: Research Study

## Mission

Plan or synthesize an internal research study and record it in the research
chronicle with traceable sources.

## Allowed repository paths

- `../../../../internal/research/`
- `../../../../templates/research-plan.md`

## Required sources of truth

- `../../../../internal/research/research-index.md`
- `../../../../internal/research/sources/source-registry.md`
- `../../../../internal/delivery/quality-gates/research-gate.md`

## Product boundaries

Research informs product decisions; it does not set Canon. Findings become
requirements only through an approved specification or decision record.

## Known constraints

- Every claim needs a registered source.
- Use synthetic or consented, minimized examples; never production private data.
- Record the study in the research chronicle and index.

## Prohibited assumptions

- Do not present a synthesis as a decision.
- Do not expose raw research data or participant detail in any public path.

## Expected output

A research plan or synthesis under `internal/research/`, linked from the
research index, with sources registered and the research gate satisfied.

## Verification commands

```bash
python scripts/quality_gates.py --gate docs
```

## Reviewed against sources on
2026-09-14
