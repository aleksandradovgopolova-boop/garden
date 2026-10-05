---
title: "Garden Data Classification and Privacy Architecture"
status: proposed
owner: "Product"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: false
---

# Garden Data Classification and Privacy Architecture

**Версия:** 0.1  
**Статус:** `proposed`

## 1. Классы данных

| Class | Примеры | Default handling |
|---|---|---|
| D0 Public | public help, templates | normal controls |
| D1 Account/technical | email, timezone, device sessions | encrypted, limited retention |
| D2 Personal content | practices, reflections, attachments | private vault, no analytics content |
| D3 Sensitive | health, sexuality, beliefs, violence, finance | field protection, no staff/provider secondary use |
| D4 Crisis/high-harm | immediate-risk text, abuse disclosure | shortest necessary use, highly restricted, no profiling |
| D5 Secrets | tokens, keys, recovery factors | secrets manager, never in prompts/logs |
| D6 Derived AI data | embeddings, summaries, hypotheses, risk signals | provenance, expiry, purpose and deletion parity |

A record containing inseparable D3 content is handled at D3 level in full.

## 2. Data-flow rule

Every flow documents:

```yaml
source:
purpose:
data_classes:
controller:
processor:
region:
transit_encryption:
at_rest_encryption:
retention:
training_use:
logging:
deletion_path:
user_control:
```

No undocumented production flow.

## 3. Architecture zones

### Local Draft

Before submit, content remains local where technically feasible.

### User Vault

Canonical user-owned records. AI-derived elements stored separately from user-authored facts.

### Retrieval Layer

Per-user namespace; metadata includes source, domain, sensitivity, expiry and allowed uses.

### AI Gateway

Redacts unnecessary identifiers, limits context, applies provider routing, enforces no-training/no-retention configuration and records non-content audit metadata.

### Policy Engine

Authorization, safety and tool permissions are enforced deterministically outside the LLM.

### Analytics

Receives only approved structured events; no transcript, prompts, embeddings or inferred wellbeing traits.

### Research Environment

Physically/logically separated, consented and pseudonymized; production credentials unavailable.

## 4. Memory classes

- user fact;
- explicit preference;
- temporary commitment;
- user-authored interpretation;
- AI hypothesis;
- sensitive state;
- prohibited generated narrative.

AI hypothesis cannot silently become user fact.

## 5. Access matrix

| Role | D1 | D2 | D3 | D4 | D5 |
|---|---:|---:|---:|---:|---:|
| User | own | own | own | own | recovery only |
| Support | minimum | user-selected excerpt | no default | no default | none |
| Engineer | aggregated metadata | none | none | none | scoped secrets |
| Security IR | necessary | JIT | JIT/dual approval | JIT/dual approval | scoped |
| Researcher | pseudonymized consented | consented | protocol-specific | excluded by default | none |
| Model provider | minimal request | minimal request | only if approved route | prohibited by default | none |

## 6. Retention model

Retention is set by purpose, not storage cost.

- ephemeral inference context: shortest technically possible;
- unconfirmed AI hypothesis: short expiry;
- security log: limited justified period;
- user content: user-controlled with inactivity review;
- backups: fixed maximum overwrite cycle;
- research: protocol-specific;
- deleted account: deletion workflow with visible status.

## 7. Deletion graph

A delete request traverses:

1. canonical record;
2. attachments;
3. vector store;
4. search index;
5. summaries;
6. AI memory;
7. cached context;
8. scheduled prompts;
9. analytics identifiers;
10. provider APIs;
11. backups through expiration.

Deletion is tested automatically with canary records.

## 8. Provider routing

D3/D4 content can only go to an approved provider route with:

- contract and DPA;
- no training;
- minimum retention;
- supported region and transfer mechanism;
- incident SLA;
- deletion mechanism;
- security evidence;
- model version control.

D4 is prohibited from external providers by default until separately approved.

## 9. Analytics firewall

Forbidden analytics fields:

- raw text;
- prompt/output;
- diagnoses;
- inferred emotion;
- relationship content;
- crisis label;
- persuasion susceptibility;
- personality profile;
- third-party names.

Allowed examples:

- feature opened;
- save succeeded;
- deletion completed;
- prompt dismissed;
- safety fallback triggered as coarse aggregate after privacy review.

## 10. Backup and recovery

- encryption and separate keys;
- access restricted;
- restore into isolated environment;
- cross-user reconciliation;
- deletion does not re-enter production after restore;
- regular restore exercises;
- defined RPO/RTO;
- incident audit.

## 11. Architecture decision still unresolved

Local-first and on-device inference could materially reduce risk but affect cost, functionality and device support. It requires a separate technical spike; no marketing claim is made before validation.
