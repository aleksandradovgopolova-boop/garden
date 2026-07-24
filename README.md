---
title: "Garden Repository"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: monthly
source_of_truth: false
---
# Garden Repository
Garden uses one repository with two surfaces.

```text
public/    → public product site rendered by WowRepo
internal/  → private team documentation and AI OPS
```

Start with [public/README.md](public/README.md) for the product site or [internal/README.md](internal/README.md) for team work.

WowRepo receives only `public/`. Public pages never depend on internal access. Internal documents may link to public Canon. Publication requires human review.

Run `python scripts/check_docs.py` to validate the repository.
