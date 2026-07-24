---
title: "R-012 — Данные, приватность и безопасность Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-012 — Данные, приватность и безопасность Garden

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Статус:** foundational research / privacy, security and human safety  
**Контур:** `02_institute/research/R-012_data_privacy_security_and_safety.md`  
**Правовой фокус:** EU/EEA-first baseline; документ не является юридическим заключением

---

## 1. Главный вопрос

> Какие данные Garden вправе получать о внутренней жизни человека, как технически и организационно защитить их — и какие функции продукт не должен запускать, пока не способен обеспечить реальную приватность, безопасность и помощь при серьёзном риске?

## 2. Главный вывод

Для Garden приватность — не раздел настроек, а ограничение самой продуктовой идеи.

Свободный текст может раскрывать здоровье, сексуальность, религиозные и политические убеждения, отношения, насилие, зависимости, финансы и данные других людей. AI способен дополнительно вывести чувствительные признаки, которых пользователь прямо не сообщал.

> **Garden сначала доказывает необходимость обработки, затем выбирает минимальный объём данных и только после этого проектирует функцию. Невозможность безопасно обработать данные — основание отказаться от функции, а не написать более длинное согласие.**

## 3. Три слоя безопасности

### Data protection

Законность, цели, минимизация, прозрачность, сроки, права человека, международные передачи и процессоры.

### Information and AI security

Утечка, взлом, employee access, prompt injection, retrieval poisoning, cross-user leakage, tool misuse, supply chain и восстановление.

### Human safety

Ошибочный совет, кризис, зависимость, скрытое убеждение, abusive access, вредное профилирование и замещение профессиональной помощи.

Ни один слой не заменяет другие.

## 4. GDPR baseline

Garden должен определить controller, processors, purposes, legal basis по Article 6, дополнительное основание Article 9 для special-category data, retention, international transfers и механизм реализации прав пользователя.

Основные принципы:

- lawfulness, fairness and transparency;
- purpose limitation;
- data minimisation;
- accuracy;
- storage limitation;
- integrity and confidentiality;
- accountability.

`Consent to use Garden` не является автоматически согласием на sensitive profiling, research, model training, marketing, передачу человеку или passive monitoring. Эти цели должны быть разделены.

## 5. Special-category data

Garden может получить чувствительные данные:

1. напрямую из текста;
2. из выбранных практик;
3. из файлов и voice input;
4. через connected services;
5. через AI inference;
6. из упоминаний третьих лиц.

Поэтому свободный текст по умолчанию рассматривается как **потенциально чувствительный**, а не как обычный пользовательский контент.

## 6. Non-clinical boundary

Alpha остаётся общим wellbeing-продуктом и не должен без отдельного regulatory track:

- диагностировать;
- лечить или предотвращать расстройство;
- оценивать клинический риск;
- менять назначенную терапию;
- рекомендовать медицинское решение;
- заявлять клиническую эффективность;
- обещать кризисный мониторинг.

Классификация зависит не только от дисклеймера, но и от intended purpose, claims, функций, целевой аудитории и последствий ошибки.

## 7. AI Act

AI Act вступил в силу 1 августа 2024 года. Запреты на отдельные AI practices и требования AI literacy начали применяться 2 февраля 2025 года. Официальный график Европейской комиссии указывает 2 августа 2026 года как ключевую дату общей применимости многих положений; текущие изменения и переходные правила нужно повторно проверить перед запуском.

Для Garden особенно релевантны риски:

- purposefully manipulative or deceptive techniques;
- ухудшение способности принять informed decision;
- эксплуатация уязвимости из-за возраста, disability или социально-экономического положения;
- transparency и AI literacy.

Окончательную AI Act classification нельзя установить до фиксации функций и claims.

## 8. Profiling

Скрытый профиль может существовать, даже если в базе нет таблицы `profile`.

В Alpha запрещены выводы вроде:

- «склонность избегать»;
- «эмоциональная стабильность»;
- «вероятность выполнить»;
- «уязвимость к напоминанию»;
- «идеальный persuasion style»;
- «риск зависимости» как коммерческий сегмент.

Нет скрытого психологического, рекламного или persuasion profile.

## 9. DPIA как launch gate

Garden сочетает special-category data, AI inference, долгосрочное наблюдение, profiling risk, novel technology и возможные кризисные состояния. Поэтому Data Protection Impact Assessment должна быть выполнена до пилота с реальными данными.

DPIA обновляется при новой модели, памяти, провайдере, passive data, human review, research use, social functions, новой стране или изменении claims.

## 10. Privacy by default

По умолчанию:

- no training on user content;
- no research reuse;
- no advertising based on content;
- no public profile;
- no social visibility;
- no passive sensing;
- no contact upload;
- no indefinite memory;
- no employee access;
- no precise location;
- no crisis-monitoring claim;
- no sensitive inference storage.

Базовая функциональность не должна требовать отказа от privacy.

## 11. Purpose separation

Данные разделяются по целям:

- core service;
- safety;
- security;
- product analytics;
- research;
- model improvement;
- marketing.

Production content не используется для model training в Alpha. Safety data не используется для personalization или marketing. Research требует отдельного opt-in процесса.

## 12. Data zones

### Zone A — Local private draft

Незавершённый текст не отправляется до явного действия; возможна on-device redaction.

### Zone B — User Vault

Практики, записи и подтверждённая память; encryption at rest, per-user isolation, user-controlled retention.

### Zone C — Ephemeral AI Context

Только необходимый фрагмент, purpose-bound, time-limited, no provider training, minimum provider retention.

### Zone D — Product Analytics

Технические события без raw journal text и чувствительных derived traits.

### Zone E — Safety and Security Logs

Минимально необходимые данные, ограниченный доступ, отсутствие использования для personalization.

### Zone F — Research

Separate consent, pseudonymization, controlled access and independent governance.

## 13. Encryption and architecture honesty

Минимум:

- TLS in transit;
- modern encryption at rest;
- managed keys and rotation;
- secrets manager;
- encrypted backups;
- field-level protection for highly sensitive data;
- strict tenant isolation.

Если server-side AI читает текст, продукт не должен называть его end-to-end encrypted. Полноценное E2EE несовместимо с unrestricted server-side processing, если сервер обладает ключом расшифровки.

## 14. Employee access

По умолчанию сотрудники не читают raw personal content.

Исключительный доступ требует:

- documented purpose;
- least privilege;
- just-in-time grant;
- ticket and reason;
- dual approval для особо чувствительных данных;
- immutable audit;
- short session;
- periodic access review;
- immediate revocation.

Нельзя читать реальные диалоги «для продуктового понимания» вне consented research.

## 15. Model provider gate

До подключения LLM provider проверяются:

- training policy;
- retention;
- region;
- sub-processors;
- deletion;
- incident notification;
- data-transfer mechanism;
- prompt/output logging;
- DPA and audit evidence;
- model change notice.

User content не используется provider’ом для training or product improvement. Если это нельзя гарантировать, provider не получает sensitive content.

## 16. Prompt injection and agent security

Untrusted content может поступить через message, file, web page, email, calendar или shared object.

> **Untrusted content is data, not instruction.**

Обязательны:

- tool allowlist;
- minimum scopes;
- read/write separation;
- human confirmation for external actions;
- policy enforcement outside the model;
- no raw secrets in prompts;
- sandboxed file processing;
- output validation;
- rate and transaction limits;
- rollback where possible;
- no model-generated authorization.

## 17. Cross-user isolation

Обязательные тесты:

- чужой user ID;
- vector namespace leak;
- cache contamination;
- shared embedding retrieval;
- backup restore mix-up;
- export with another user’s data;
- prompt injection requesting previous-user context;
- cross-domain memory leakage.

Cross-user disclosure имеет нулевую терпимость.

## 18. Logs

Logs не должны становиться скрытой копией продукта.

Без доказанной необходимости нельзя писать:

- full prompts and outputs;
- decrypted journal text;
- crisis text;
- tokens and secrets;
- contacts;
- provider payloads.

Нужны structured event codes, redaction, short retention, restricted querying и отдельные security logs.

## 19. Retention and deletion

`Indefinite` не является допустимым default.

Удаление охватывает:

- primary records;
- attachments;
- vector embeddings;
- summaries;
- memories;
- derived features;
- caches and indexes;
- queued jobs;
- processor copies;
- backups через объявленный expiration cycle.

Пользователь видит, что удалено сразу, что находится в backup и каков максимальный срок. Удалённая AI-гипотеза не должна возвращаться из summary или cache.

## 20. Export and access

Export включает:

- human-readable and machine-readable formats;
- provenance;
- user vs AI authorship;
- memory classes;
- corrections;
- consent history.

Для export, delete and memory dashboard нужна re-authentication, чтобы защититься при доступе к устройству.

## 21. Account and coercive-access safety

Риски: украденный телефон, общий компьютер, abusive partner, shoulder surfing, notification previews и compromised recovery.

Controls:

- passkeys/MFA option;
- device/session list;
- remote logout;
- privacy lock;
- hidden notification content;
- re-authentication for sensitive operations;
- no personal text in emails;
- suspicious-login alerts.

Совместная практика не даёт доступ к личному дневнику.

## 22. Crisis boundary

Garden не является emergency service, suicide hotline, clinical monitoring system или 24/7 human-reviewed service.

Если нет staffed escalation, продукт не обещает monitoring.

При явном высоком риске Garden должен:

1. прекратить обычную рефлексию;
2. ответить ясно и неосуждающе;
3. минимально уточнить непосредственную безопасность;
4. предложить местную экстренную или кризисную помощь;
5. предложить выбранного реального человека;
6. показать проверенные локальные ресурсы;
7. не ограничиваться breathing exercise;
8. не требовать длинного disclosure;
9. не утверждать, что помощь уже вызвана.

Протокол требует clinical and crisis-professional review.

## 23. Automatic crisis detection

В Alpha:

- нет обещания passive crisis detection;
- safety response запускается прежде всего явным текущим содержанием;
- нет long-term crisis score;
- нет автоматического уведомления полиции или контактов;
- нет скрытого human review;
- crisis data не используется для marketing/personalization;
- нужны language-specific tests и deterministic safety layer where feasible.

## 24. Children

Garden Alpha — `18+` как product safety boundary.

До работы с несовершеннолетними нужны child-rights impact assessment, age-appropriate design, age assurance without excessive data, country legal review, separate safeguarding and crisis protocols и независимый child-safety review.

## 25. Research governance

Production data не становятся research data автоматически.

Нужны separate consent, protocol, minimization, withdrawal, re-identification assessment, controlled access и отсутствие product penalty за отказ.

`Anonymized` используется только если reasonable re-identification невозможна; иначе данные называются pseudonymized.

## 26. Security program

Минимальная программа:

- asset inventory and data-flow map;
- threat modeling;
- secure SDLC;
- dependency and secrets scanning;
- SAST/DAST;
- infrastructure hardening;
- penetration testing;
- LLM/agent, privacy and safety red-teams;
- vulnerability disclosure;
- patch SLAs;
- backup restore tests;
- incident response;
- business continuity;
- vendor risk management;
- security and AI-literacy training.

## 27. Incident response

Типы инцидентов:

- confidentiality, integrity or availability breach;
- cross-user memory;
- harmful model response at scale;
- deletion failure;
- processor incident;
- prompt-injection exploit;
- unauthorized employee access;
- crisis-protocol failure.

Процесс:

1. Detect.
2. Contain.
3. Preserve evidence.
4. Assess affected data and people.
5. Disable or degrade the feature.
6. Notify accountable roles.
7. Meet legal notification duties.
8. Communicate honestly to affected users.
9. Remediate and verify.
10. Update tests and Chronicle.

Under GDPR a supervisory authority may need notification within 72 hours where feasible when the breach is likely to risk individuals’ rights and freedoms; high-risk breaches may also require communication to affected people. Exact duties require incident-specific legal assessment.

## 28. Fail-safe behavior

- memory unavailable → do not invent;
- safety layer unavailable → restricted safe mode;
- authorization uncertain → deny action;
- data scope uncertain → do not retrieve;
- provenance lost → do not use as fact;
- deletion uncertain → keep request active and investigate;
- policy conflict → prefer privacy and safety boundary.

## 29. Alpha launch boundaries

Alpha does not include:

- minors;
- clinical claims;
- crisis-monitoring promises;
- passive mental-state inference;
- social comparison and public profiles;
- content-based advertising;
- data brokerage;
- training on production content;
- employee browsing;
- broad third-party integrations;
- autonomous external actions;
- hard commitments;
- hidden psychological profiles;
- biometric identification.

## 30. Claim Registry

| Claim ID | Утверждение | Источники | Уверенность | Статус |
|---|---|---|---|---|
| R012-C01 | Free text may contain special-category data | SRC-PRIV-001, 002 | высокая | foundation |
| R012-C02 | Privacy by design/default and minimization are GDPR duties | SRC-PRIV-001, 003 | высокая | foundation |
| R012-C03 | Users have access, correction, erasure, restriction, portability and objection rights | SRC-PRIV-004 | высокая | foundation |
| R012-C04 | One blanket consent legitimises all processing | no | отсутствует | rejected |
| R012-C05 | DPIA should precede a real-data pilot | SRC-PRIV-001, 005 + synthesis | высокая | launch gate |
| R012-C06 | AI Act prohibits certain manipulative/deceptive harmful practices | SRC-REG-001, 002 | высокая | legal constraint |
| R012-C07 | Garden is definitively high-risk AI | classification incomplete | unknown | unresolved |
| R012-C08 | LLM apps face prompt injection and sensitive disclosure risks | SRC-SEC-001–003 | высокая | foundation |
| R012-C09 | System prompts alone prevent disclosure | no | отсутствует | rejected |
| R012-C10 | AI systems face poisoning, exfiltration and component threats | SRC-SEC-004 | высокая | foundation |
| R012-C11 | Health AI needs autonomy, safety, transparency and accountability | SRC-SAFE-001–003 | высокая | governance foundation |
| R012-C12 | Garden can guarantee crisis detection | no | отсутствует | rejected |
| R012-C13 | Raw production content is necessary for improvement | no | отсутствует | rejected |
| R012-C14 | Deletion must include derived stores | legal/technical synthesis | высокая | requirement |
| R012-C15 | E2EE is compatible with unrestricted server-side AI reading | no | отсутствует | rejected |
| R012-C16 | Employee access should be exceptional and audited | standards synthesis | высокая | requirement |
| R012-C17 | Alpha should be 18+ | Garden safety synthesis | proposed | boundary |
| R012-C18 | Production content should not train provider models by default | privacy synthesis | высокая | launch gate |

## 31. Основные источники

- SRC-PRIV-001 — GDPR, Regulation (EU) 2016/679.
- SRC-PRIV-002 — EDPB data-protection basics and sensitive-data guidance.
- SRC-PRIV-003 — EDPB Guidelines 4/2019, Data Protection by Design and Default.
- SRC-PRIV-004 — EDPB guide to data-subject rights.
- SRC-PRIV-005 — EDPB-endorsed DPIA guidelines.
- SRC-PRIV-006 — EDPB LLM Privacy Risks & Mitigations.
- SRC-PRIV-007 — NIST Privacy Framework.
- SRC-REG-001 — Regulation (EU) 2024/1689, AI Act.
- SRC-REG-002 — European Commission AI Act implementation pages.
- SRC-REG-003 — FDA digital-health/software guidance.
- SRC-SEC-001 — OWASP LLM01:2025 Prompt Injection.
- SRC-SEC-002 — OWASP LLM02:2025 Sensitive Information Disclosure.
- SRC-SEC-003 — OWASP Top 10 for LLM/GenAI Applications 2025.
- SRC-SEC-004 — ENISA Securing Machine Learning Algorithms.
- SRC-SEC-005 — NIST AI RMF Generative AI Profile.
- SRC-SAFE-001 — WHO Ethics and Governance of AI for Health.
- SRC-SAFE-002 — WHO guidance for large multimodal models in health.
- SRC-SAFE-003 — WHO call for safe and ethical LLM use.
- SRC-SAFE-004 — NIMH overview of mental-health apps.

## 32. Что исследование не доказывает

R-012 не является final legal opinion, medical-device classification, completed DPIA, penetration test, security architecture review или clinical crisis protocol.

Оно не доказывает, что перечисленных мер достаточно, что EU baseline покрывает глобальный запуск или что consent делает вредный дизайн допустимым.

## 33. Вердикт

Garden работает с данными, способными повлиять на достоинство, отношения, репутацию, работу, здоровье и безопасность.

Поэтому продукт спрашивает не «сможем ли мы собрать эти данные?», а:

1. нужны ли они человеку;
2. можно ли добиться цели без них;
3. понимает ли человек последствия;
4. защищены ли они от внешнего и внутреннего доступа;
5. можно ли удалить их полностью;
6. что произойдёт при ошибке;
7. готовы ли мы отказаться от функции.

> **Забота Garden начинается не с того, как много он помнит. Она начинается с дисциплины не брать, не выводить и не сохранять то, без чего человек может обойтись.**
