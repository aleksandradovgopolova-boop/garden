---
title: "Garden Crisis and High-Risk Interaction Protocol"
status: draft
owner: "Engineering"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: false
---

# Garden Crisis and High-Risk Interaction Protocol

**Версия:** 0.1  
**Статус:** `draft — requires clinical, legal and crisis-professional review`

## 1. Boundary

Garden is not an emergency service, clinician, hotline or continuous monitoring system.

The product must not imply:

- that someone is always watching;
- that crisis will always be detected;
- that emergency services will be contacted;
- that a conversation is fully confidential regardless of infrastructure and law;
- that Garden can determine diagnosis or level of risk alone.

## 2. Trigger scope

Alpha responds to explicit current-message indicators of immediate self-harm, suicide, violence, abuse or acute medical danger.

It does not create a permanent `high-risk person` profile.

Indirect or ambiguous content may trigger a brief clarification, not a hidden escalation.

## 3. Response priorities

1. Immediate physical safety.
2. Connection to a real person or verified local resource.
3. Clear limits of Garden.
4. Minimum necessary questions.
5. No ordinary reflection, interpretation or habit coaching.
6. No blame, moralising or false reassurance.

## 4. Required response shape

### Acknowledge

Recognise seriousness without theatrical language.

### Clarify immediate danger

Ask only questions needed to decide whether immediate emergency help is appropriate.

### Connect

Offer:

- local emergency service where imminent danger exists;
- verified crisis resource appropriate to location and language;
- trusted person selected by the user;
- urgent professional care.

### Stay practical

Help prepare a call or message, move away from means of harm, or get near another person where appropriate and professionally reviewed.

### State limitation

Garden cannot monitor, dispatch or guarantee response.

## 5. Prohibited responses

- philosophical analysis;
- explaining the origin of suicidal thoughts;
- guilt about loved ones;
- generic gratitude lists;
- breathing exercise as sole answer;
- promises that everything will be fine;
- secrecy promise;
- relationship-building copy;
- long questionnaire;
- asking for unnecessary identifying information;
- announcing that authorities were contacted when they were not;
- automatically informing a contact without a designed and lawful process.

## 6. Deterministic safety layer

Where technically feasible, high-risk routing should not depend solely on the general LLM.

Components:

- multilingual detection layer;
- deterministic policy state machine;
- verified resource registry;
- safe fallback text;
- model-output validation;
- feature kill switch;
- monitoring of false positives/negatives without storing unnecessary raw text.

## 7. Human escalation

Human review is not added casually.

If introduced, it requires:

- explicit user-facing explanation;
- staffed service level;
- trained reviewers;
- confidentiality and access controls;
- jurisdiction and emergency procedure;
- documentation and audit;
- secondary-trauma support for staff;
- honest limits outside staffed hours.

Without these conditions, Alpha must not claim human escalation.

## 8. Crisis data

Crisis data is D4:

- shortest necessary retention;
- strict access;
- no model training;
- no product personalization;
- no advertising or engagement use;
- no permanent risk badge;
- separate audit of any disclosure;
- deletion subject to defined legal/safety requirements.

## 9. Abuse and coercion

For possible domestic or interpersonal abuse:

- do not automatically tell the person to confront or leave;
- do not expose notification content;
- do not create a visible shared record;
- consider device and account access by the abusive person;
- offer neutral quick-exit and local specialist resources;
- avoid storing identifiable details not needed for the user’s goal.

## 10. Medical and psychiatric boundary

Garden does not:

- diagnose;
- advise medication changes;
- interpret symptoms as a disorder;
- discourage professional help;
- position itself as replacement care.

High-risk medical symptoms require verified external medical guidance, not AI interpretation.

## 11. Testing

Minimum scenario suite:

- direct suicidal intent;
- vague hopelessness;
- historical event;
- quotation or fiction;
- sarcasm;
- non-standard language and spelling;
- multiple languages;
- self-harm without suicidal intent;
- violence by another person;
- eating-disorder danger;
- intoxication;
- acute medical symptoms;
- refusal of help;
- no known location;
- model/provider outage.

Metrics:

- safe routing;
- harmful false reassurance;
- unnecessary escalation;
- resource correctness;
- clarity of limits;
- time to actionable help;
- demographic/language disparities;
- user comprehension.

## 12. Release gate

No crisis-aware feature launches without:

- independent professional review;
- localized verified resources;
- multilingual testing;
- documented fallback;
- incident owner;
- model-update regression suite;
- privacy review;
- public explanation of limits.
