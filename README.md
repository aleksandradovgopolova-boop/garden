---
title: "Garden Repository"
status: accepted
owner: "aleksandradovgopolova-boop"
updated: 2026-10-05
review_cycle: monthly
source_of_truth: false
---

# Garden Repository

Garden is a public product repository containing product/design/research documentation and site-verification tools. The Garden application is not implemented yet.

```text
public/    → candidate publication content; publication currently disabled
internal/  → team product, engineering and delivery documents
archive/   → historical sources; not active requirements
```

All tracked files, including `internal/` and `archive/`, are publicly readable. Directory names and WowRepo exclusions do not provide access control. Only publication-safe material belongs here; confidential material, credentials and raw participant data must stay outside Git. GitHub Pages remains disabled under [ADR-007](internal/decisions/adr/ADR-007-public-repository-publication-disabled.md).

Start with [Source of Truth](internal/governance/SOURCE_OF_TRUTH.md), [Decision Log](internal/decisions/decision-log.md) and [current cycle](internal/delivery/current/current-cycle.md). The first approved slice is [create a Place, save, leave and return](internal/delivery/current/first-place-return-spec.md). AI Preview and Undo follow later. The complete [Alpha](internal/product/alpha/alpha-scope.md) remains the longer-term target.

## Verification

```sh
python -m pip install -r scripts/requirements.txt
python scripts/check_docs.py
python scripts/sync_repository.py --check
python -m unittest discover -s tests -v
```

CI builds all 54 candidate publication pages with WowRepo pinned in `.github/workflows/quality.yml`, checks coverage/links and rejects non-public source artifacts. It has no Pages deployment or public artifact upload. `scripts/build_site.py` is a secondary Python preview, not production-rendering evidence.

AI Ops Kit 4.9.3 is installed from release `v4.9.3` at `ad16611cec1ca65a659f597f7b3b0436df8e78b8`. [Installation evidence and remaining qualification](internal/engineering/ai-ops/installation-2026-10-05.md) distinguish tooling installation from product readiness.
