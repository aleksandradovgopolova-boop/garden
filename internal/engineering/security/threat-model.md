---
title: "Garden Threat Model"
status: accepted
owner: "Engineering"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden Threat Model

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Статус:** `proposed`  
**Метод:** abuse cases + STRIDE/LINDDUN-inspired review

## 1. Защищаемые активы

- сырой текст и voice transcripts;
- практики, commitments и reflections;
- AI memories, summaries, hypotheses and embeddings;
- account identifiers and recovery data;
- connected-service tokens;
- crisis and safety signals;
- third-party information inside user content;
- encryption keys and secrets;
- audit logs;
- model/system prompts and policies;
- доверие и свобода пользователя.

## 2. Threat actors

- внешний злоумышленник;
- malicious user;
- abusive partner or family member;
- compromised device;
- insider or support employee;
- model/cloud/subprocessor;
- compromised connector;
- attacker embedding instructions in files/pages;
- developer with excessive production access;
- automated bot scraping or account takeover;
- legal or coercive requester;
- the product itself through harmful incentives.

## 3. Основные abuse cases

| ID | Abuse case | Возможный вред | P0 controls |
|---|---|---|---|
| TM-01 | Account takeover | раскрытие интимной истории | passkeys/MFA option, session management, alerts, re-authentication |
| TM-02 | Abusive partner reads device | насилие, шантаж, surveillance | privacy lock, hidden previews, quick logout, no email content |
| TM-03 | Cross-user retrieval | чужие записи в ответе | per-user namespaces, auth outside LLM, isolation tests, fail closed |
| TM-04 | Indirect prompt injection | exfiltration or unsafe tool action | untrusted-content boundary, tool allowlist, output validation, confirmation |
| TM-05 | Malicious upload | malware, hidden instructions | sandbox, file-type allowlist, scanning, no active content execution |
| TM-06 | Employee browsing | humiliation, discrimination, blackmail | no default raw access, JIT, dual approval, audit, sanctions |
| TM-07 | Provider training/retention | secondary use and leakage | contract, no-training setting, retention controls, provider gate |
| TM-08 | Sensitive text in analytics/logs | broad internal exposure | structured events, redaction, no raw text, short retention |
| TM-09 | Deleted memory reappears | loss of control, false identity | deletion graph, derived-store purge, backup expiry, tests |
| TM-10 | Stale AI hypothesis reused | identity fixation, wrong advice | epistemic class, expiry, confirmation, domain separation |
| TM-11 | Crisis false negative | missed urgent help | explicit-current-message safety layer, deterministic fallback, tested resources |
| TM-12 | Crisis false positive | panic, chilling effect, loss of trust | no hidden escalation, explain boundary, no long-term crisis label |
| TM-13 | Social/shared feature leaks diary | relationship and workplace harm | object-level permissions, separate shared/private stores, explicit preview |
| TM-14 | Data export to wrong person | full-history disclosure | re-authentication, encrypted export, expiration, audit |
| TM-15 | Backup restore mixes users | silent mass breach | encrypted per-tenant backup, restore tests, reconciliation |
| TM-16 | API/tool overreach | email/send/delete without intent | least scopes, confirmation, transaction limits, rollback |
| TM-17 | Model update changes safety | harmful advice or leakage | versioned evals, canary, rollback, kill switch |
| TM-18 | Dependency mechanics | displaced human support | no relational debt, no missing-you copy, engagement not KPI |
| TM-19 | Profiling for persuasion | autonomy loss and manipulation | persuasion firewall, no hidden traits, prohibited analytics |
| TM-20 | Research re-identification | public exposure | separate consent, pseudonymization, access controls, release review |

## 4. Highest-risk chains

### Chain A — File to external action

Malicious instruction in uploaded PDF → model treats it as instruction → connector action → disclosure or deletion.

Controls: parsed content marked untrusted, no tool calls from document text, confirmation based on user-visible action summary, policy engine outside model.

### Chain B — Memory to identity

Temporary distress statement → AI summary → long-term memory → repeated personalized interpretation → user accepts false trait.

Controls: memory classes, AI hypothesis expiry, user confirmation, no generated narrative memory, correction propagation.

### Chain C — Product metric to manipulation

Low retention → model receives goal to increase return → uses sensitive history and emotional language → dependence.

Controls: human outcomes, no persuasion use of memory, no engagement optimization in dialogue policy, governance review.

### Chain D — Insider access

Support ticket → employee receives unrestricted account access → reads unrelated journal → screenshots/export.

Controls: user-selected scope, redacted support view, JIT access, no download, watermarking where appropriate, audit and review.

### Chain E — Coercive relationship

Partner demands shared access or export → user cannot safely refuse → sensitive material exposed.

Controls: no default sharing, granular permissions, no visible refusal notification, privacy-preserving exit, abuse-safety review.

## 5. Security assumptions that must not be trusted

- «LLM follows the system prompt»;
- «provider says data is private» without contract and settings;
- «anonymized» when identifiers were merely removed;
- «encrypted» without specifying where decryption happens;
- «employees are trustworthy» without access controls;
- «user consented» as a substitute for safety;
- «only one user reported it» as proof of low severity;
- «the model refused in manual testing» as a security control.

## 6. Required red-teams

### AI/agent

Prompt injection, indirect injection, system-prompt extraction, data exfiltration, tool escalation, unsafe chained actions, memory poisoning.

### Privacy

Cross-user retrieval, stale deletion, employee misuse, vendor retention, analytics leakage, sensitive inference, coercive access.

### Psychological safety

Sycophancy, dependency, crisis, delusion, abuse, eating disorders, medical advice, reassurance loops, shame and manipulation.

### Operational

Provider outage, key compromise, backup failure, wrong deployment, revoked employee, expired consent, incident communication.

## 7. Risk treatment

Each threat receives:

```yaml
threat_id:
owner:
likelihood:
impact:
affected_people:
existing_controls:
residual_risk:
test:
monitor:
accept_or_mitigate:
review_date:
```

Critical residual risks cannot be accepted by a product manager alone. They require security, privacy, safety and accountable executive sign-off.
