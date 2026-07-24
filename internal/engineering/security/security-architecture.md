---
title: "P-008 — Privacy and Security Architecture"
status: accepted
owner: "Engineering"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# P-008 — Privacy and Security Architecture

## Threats
Unauthorized access, broken object authorization, cross-user leakage, AI context leakage, export exposure, retained deleted data, malicious links, version-history disclosure, admin abuse and insecure media.

## Baseline controls
Strong authentication; secure sessions; row-level authorization; encrypted transport/storage; signed media; short-lived share tokens; audit events; rate limits; verified export; deletion workflow; secret management; dependency scanning.

## AI isolation
Explicit context assembly, allowlisted actions, output validation, prompt-injection defenses, tenant isolation and provider disclosure.

External Alpha gate: authorization, deletion, export and AI-leak tests plus threat-model review and incident owner.
