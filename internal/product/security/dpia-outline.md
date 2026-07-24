---
title: "Garden DPIA Outline"
status: accepted
owner: "Product"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: true
---

# Garden DPIA Outline

**Версия:** 0.1  
**Статус:** working template; complete with qualified privacy/legal review

## 1. Processing description

- product and intended purpose;
- user groups and countries;
- data subjects, including third parties mentioned in text;
- data categories and sensitivity;
- sources;
- recipients and subprocessors;
- data-flow diagram;
- AI models and tools;
- retention and deletion;
- international transfers.

## 2. Purpose and legal basis

For every purpose:

```yaml
purpose:
necessary_data:
article_6_basis:
article_9_condition_if_needed:
why_necessary:
less_intrusive_alternative:
consent_or_objection_flow:
```

## 3. Necessity and proportionality

- Can the feature work without raw content?
- Can processing be local or ephemeral?
- Is each inference necessary?
- Is frequency proportionate?
- Is memory needed?
- Are third-party data minimized?
- Can no-tracking/no-memory modes work?

## 4. Rights and transparency

- notice;
- access;
- correction;
- erasure;
- restriction;
- portability;
- objection;
- automated profiling explanation;
- memory provenance;
- consent history;
- complaint route.

## 5. Risk scenarios for people

Assess likelihood and severity of:

- humiliation and reputational harm;
- relationship or domestic-abuse harm;
- employment or insurance discrimination;
- medical or psychological harm;
- manipulation and autonomy loss;
- identity fixation;
- unwanted disclosure;
- stalking and location harm;
- exclusion or bias;
- dependency;
- denial of rights;
- inability to delete;
- harm to third parties.

## 6. Controls

Map every risk to preventive, detective and corrective controls, owner, evidence and residual risk.

## 7. AI-specific assessment

- hallucination and advice risk;
- sycophancy;
- prompt injection;
- model/provider retention;
- training provenance;
- cross-user leakage;
- memory poisoning;
- bias and language disparities;
- model-update drift;
- human oversight;
- kill switch.

## 8. Consultation

- DPO/privacy counsel;
- security;
- clinical/crisis professional;
- affected users;
- accessibility and abuse-safety experts;
- supervisory authority if residual high risk requires prior consultation.

## 9. Decision

```yaml
approved_scope:
prohibited_scope:
required_actions:
residual_risks:
accountable_sign_off:
review_trigger:
next_review:
```

DPIA is versioned and linked to GDRs and Chronicle.
