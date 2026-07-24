---
title: "Contributing"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# Contributing

Create a new file only when it is a source of truth, has a separate owner or review cycle, records a standalone decision, or will be linked regularly. Otherwise update an existing document.

Use lowercase kebab-case. Do not put version numbers or “final” in active filenames; Git stores history.

Statuses: `draft`, `proposed`, `accepted`, `deprecated`, `superseded`, `archived`.

Major documents should use:

```yaml
---
title:
status:
owner:
updated:
review_cycle:
source_of_truth:
related:
---
```

Canon changes require a decision record, cross-functional review and a changelog entry. Superseded material goes to `08_ARCHIVE/`.
