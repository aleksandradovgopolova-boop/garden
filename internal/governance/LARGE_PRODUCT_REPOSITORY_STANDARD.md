---
title: "Large Product Repository Standard"
status: accepted
owner: "Product + AI OPS"
updated: 2026-07-18
review_cycle: yearly
source_of_truth: true
---
# Large Product Repository Standard
This applies to large, long-lived products such as Garden and Niti.

```text
public/    # WowRepo site and public Canon
internal/  # team and AI OPS operating system
archive/   # historical material
```

Smaller utilities and experiments do not require this structure unless their scope grows.

A large product should not maintain a marketing story separate from product truth. Its public site is a curated representation of the repository itself.
