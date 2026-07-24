---
title: "R-014 — Социальный слой Garden: поддержка без наблюдения и давления"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-014 — Социальный слой Garden: поддержка без наблюдения и давления

**Версия:** 0.1  
**Дата:** 16 июля 2026  
**Статус:** foundational research / social support, shared practices and community safety  
**Контур:** `02_institute/research/R-014_social_layer_support_without_surveillance.md`

---

## 1. Главный вопрос

> Как Garden может помогать людям поддерживать друг друга, совместно действовать и чувствовать связь — не превращая отношения в отчётность, сравнение, взаимный контроль, бесконечное обсуждение проблем или доступ к чужой внутренней жизни?

Подвопросы:

- какие виды социальной поддержки действительно различаются;
- когда помощь близкого укрепляет автономию;
- когда accountability превращается в surveillance;
- какие данные можно разделять;
- чем совместная практика отличается от общего дневника;
- как проектировать двустороннее согласие;
- как учитывать неравенство власти;
- нужны ли группы и сообщества;
- как предотвращать co-rumination, misinformation, harassment и contagion;
- кто отвечает за moderation;
- что происходит при расставании, конфликте и отзыве доступа;
- какой социальный слой допустим в Alpha.

---

## 2. Главный вывод

Связь с другими людьми может давать:

- эмоциональную поддержку;
- практическую помощь;
- информацию;
- обратную связь;
- чувство принадлежности;
- надежду;
- совместное решение задач;
- возможность быть увиденным без оценки.

Но цифровизация поддержки меняет отношения. Продукт способен превратить заботу в:

- наблюдение;
- отчётность;
- сравнение;
- обязанность отвечать;
- эмоциональный труд;
- co-rumination;
- взаимное убеждение;
- конфликт из-за неполных данных;
- принудительное раскрытие;
- зависимость от группы.

Рабочая позиция Garden:

> **Социальный слой должен передавать человеку ровно ту поддержку, которую он запросил, и раскрывать ровно те данные, которые необходимы для этой поддержки. Отношения остаются между людьми; Garden не становится их судьёй, диспетчером или владельцем.**

---

## 3. Relatedness не равна постоянному контакту

Self-Determination Theory рассматривает relatedness как опыт связи, заботы и значимости для других.

Это не означает:

- быть всегда доступным;
- постоянно делиться;
- иметь группу;
- получать обратную связь на каждое действие;
- делать практики вместе;
- сообщать близкому о пропусках;
- жить публично.

Человек может поддерживать связанность через:

- редкий разговор;
- совместное действие;
- присутствие без обсуждения;
- практическую помощь;
- письмо;
- границу;
- одиночество, выбранное без изоляции.

### Принцип

Garden не считает отсутствие social features дефицитом пользователя.

---

## 4. Виды поддержки

Классические модели различают минимум четыре формы.

### 4.1. Emotional support

- выслушать;
- признать переживание;
- быть рядом;
- выразить заботу.

### 4.2. Instrumental support

- помочь с ребёнком;
- принести еду;
- сопроводить;
- взять часть задачи;
- создать условия.

### 4.3. Informational support

- передать информацию;
- предложить источник;
- объяснить процедуру;
- поделиться опытом.

### 4.4. Appraisal support

- помочь посмотреть на ситуацию;
- дать обратную связь;
- сверить восприятие;
- заметить изменение.

Один тип нельзя заменять другим.

Если человеку нужна инструментальная помощь, фраза поддержки может увеличить одиночество:

> «Я рядом и верю в тебя» не заменяет «я заберу ребёнка на два часа».

### Требование

Перед social request Garden помогает назвать вид поддержки, а не отправляет универсальное «поддержи меня».

---

## 5. Matching hypothesis

Польза поддержки зависит от соответствия:

- стрессору;
- потребности;
- отношениям;
- времени;
- ресурсу помощника;
- желаемой степени участия.

Неподходящая поддержка может ощущаться как:

- обесценивание;
- вторжение;
- совет без запроса;
- контроль;
- демонстрация превосходства;
- новая обязанность.

### Product implication

Invite flow содержит:

```yaml
what_happened:
what_support_is_requested:
what_is_not_requested:
time_window:
response_optional:
data_visible:
```

---

## 6. Support и social control

Близкий человек может пытаться изменить поведение через:

- напоминания;
- просьбы;
- убеждение;
- похвалу;
- критику;
- мониторинг;
- санкции.

Это часто называют social control. Намерение может быть заботливым, но переживание — контролирующим.

Autonomy-supportive support:

- согласована;
- объясняет ожидания;
- допускает отказ;
- признаёт причины;
- не связывает выполнение с любовью;
- не расширяется самовольно;
- не превращает помощника в проверяющего.

### Принцип

> Хорошее намерение не отменяет необходимость согласия.

---

## 7. Пользователь не обязан превращать отношения в accountability

Garden не предлагает:

- «выберите человека, который будет контролировать»;
- «добавьте партнёра, чтобы не сдаться»;
- «друзья увидят ваш прогресс»;
- «позовите близкого вернуть вас в практику».

Возможные роли:

- свидетель;
- соучастник практики;
- практический помощник;
- слушатель;
- источник информации;
- emergency contact в отдельно регулируемом сценарии.

`Accountability partner` не является default-ролью.

---

## 8. Совместная практика

Совместная практика — это согласованное действие двух или более людей.

Примеры:

- прогулка раз в неделю;
- вечер без телефонов;
- общий семейный ужин;
- созвон;
- совместное чтение;
- помощь с подготовкой ко сну.

### Не является совместной практикой

- один человек следит за выполнением другого;
- партнёр получает отчёт о настроении;
- родитель видит личные записи взрослого ребёнка;
- работодатель получает wellbeing score;
- друг получает уведомление о пропуске без отдельного согласия.

---

## 9. Dyadic interventions

Research on couple- and dyadic interventions shows a broad range of techniques, including:

- joint planning;
- collaborative problem solving;
- communication;
- partner support;
- shared coping;
- environmental restructuring.

A 2024 compendium identified 122 dyadic interventions and 165 studies, demonstrating that «добавить партнёра» — не единая техника, а множество механизмов.

Earlier meta-analytic work found small effects of couple-oriented interventions in chronic illness contexts, with substantial variation.

### Ограничение

Medical or couple intervention evidence does not validate a generic shared-practice feature.

### Следствие

Каждая dyadic mechanic требует собственного:

- purpose;
- target;
- consent model;
- outcome;
- harm model.

---

## 10. Dyadic Support Contract

Перед совместной функцией оба человека принимают отдельный контракт.

```yaml
shared_object:
shared_goal:
each_person_reason:
roles:
visible_data:
hidden_data:
allowed_actions:
forbidden_actions:
notification_rules:
miss_handling:
conflict_handling:
end_date:
exit_rules:
```

### Обязательные свойства

- symmetrical visibility;
- individual private space;
- separate consent;
- no silent role expansion;
- no inferred consent from relationship;
- immediate pause;
- data portability;
- independent exit.

---

## 11. Совместный объект, а не совместная личность

Sharing строится вокруг конкретного объекта.

Можно разделить:

- название совместной практики;
- согласованное время;
- факт готовности;
- выбранный message;
- совместное событие;
- явный запрос помощи.

Нельзя раскрывать по умолчанию:

- личный дневник;
- AI hypotheses;
- mood history;
- другие практики;
- кризисные записи;
- memory profile;
- пропуски;
- relationship reflections;
- deleted content.

### Принцип

> Share the coordination, not the interior.

---

## 12. Granular consent

Согласие должно быть:

- per person;
- per object;
- per data type;
- per action;
- per time period.

Невалидно:

> «Добавить партнёра в мой Garden».

Валиднее:

> «Разрешить Анне видеть время и факт подтверждения прогулки до 31 августа. Личные заметки и остальные практики остаются закрыты».

---

## 13. Неравенство власти

Формальное согласие может быть несвободным, если приглашает:

- руководитель;
- супруг в контролирующих отношениях;
- родитель;
- врач;
- преподаватель;
- заказчик;
- человек, от которого зависит жильё или доход.

### Risk signals

- invite linked to employment;
- requirement to share;
- penalty for refusal;
- repeated requests;
- account created by another person;
- one-sided visibility;
- shared password;
- demand for full history;
- inability to exit privately.

### Alpha prohibition

Garden social layer не предназначен для employer–employee monitoring, school oversight, insurer programs or coercive family tracking.

---

## 14. Surveillance creep

Функция может начинаться как помощь:

> «Сообщить партнёру, что я вышла на прогулку».

А затем расшириться:

- когда вышла;
- где находится;
- сколько прошла;
- почему вернулась;
- как себя оценила;
- пропуск;
- отклонённый reminder.

### Rule

Никакого автоматического расширения данных. Новая видимость требует отдельного consent event.

---

## 15. Miss handling

После пропуска shared practice система не:

- уведомляет другого автоматически;
- предлагает «подтолкнуть»;
- показывает красный статус;
- назначает виноватого;
- считает streak пары;
- создаёт disappointment animation;
- сравнивает вклад.

Разрешённые варианты, выбранные заранее:

- ничего;
- нейтрально предложить перенести;
- спросить каждого отдельно;
- закрыть событие;
- открыть короткий coordination message.

---

## 16. Социальное сравнение

Comparison can provide:

- information;
- норму;
- inspiration;
- sense of possibility.

Но также:

- shame;
- envy;
- inferiority;
- competition;
- concealment;
- unhealthy escalation;
- reduced autonomy;
- interpretation without context.

Fitness-app research shows users differ in whether they want upward, downward or similarity-based comparison. This variability itself argues against default comparison.

### Alpha prohibition

- no leaderboard;
- no percentile;
- no «люди как вы»;
- no public streak;
- no progress feed;
- no best garden;
- no popularity metrics;
- no reactions count.

---

## 17. Inspiration without comparison

Допустимые alternative forms:

- anonymous practice ideas;
- stories with context and limitations;
- user-selected examples;
- diverse outcomes;
- no ranking;
- no implied norm;
- no behavioral performance data.

История не должна превращаться в:

> «Другие смогли — и ты должна».

---

## 18. Peer support

Digital peer support studies report potential benefits:

- belonging;
- hope;
- empowerment;
- shared knowledge;
- reduced isolation;
- normalization;
- practical coping strategies.

But systematic reviews often describe:

- heterogeneous interventions;
- mixed quality;
- limited causal evidence;
- weaker long-term effects;
- unclear active ingredients.

A 2025 meta-analysis in broadly healthy populations found positive average effects, particularly for mental health, but also reported weaker effects with longer follow-up and raised concerns about longer exposure enabling negative interactions.

### Conclusion

Peer support is promising but is not a safe low-cost feature.

---

## 19. Harms of online peer support

Reported or theorized adverse events include:

- co-rumination;
- emotional contagion;
- collusion;
- harmful normalization;
- misinformation;
- triggering content;
- harassment;
- trolling;
- competition over severity;
- dependency;
- pressure to disclose;
- unpaid emotional labor;
- moderator conflict;
- displacement of offline help.

### Principle

A community cannot be launched on the assumption that kindness will self-organize.

---

## 20. Co-rumination

Co-rumination combines:

- repeated discussion of problems;
- focus on negative affect;
- speculation about causes and consequences;
- repeated revisiting;
- mutual encouragement to continue.

Research has linked it to:

- greater closeness or friendship quality in some studies;
- increased rumination;
- internalizing symptoms;
- reduced benefit of support seeking in some contexts.

### Product risk

A warm community can reward increasingly detailed negative disclosure because it generates attention and connection.

### Guardrails

- time-bounded threads;
- prompts toward concrete support;
- easy closure;
- no engagement ranking;
- no algorithmic amplification of distress;
- no reward for disclosure volume;
- offer offline/human/professional bridge;
- distinguish witnessing from endless analysis.

---

## 21. Misinformation

Peer knowledge can be valuable, but lived experience is not universal instruction.

Risks:

- diagnosis;
- stopping treatment;
- supplement or medication advice;
- relationship verdicts;
- conspiracy;
- false certainty;
- anecdote as causal proof.

### Labels

- `My experience`;
- `Personal suggestion`;
- `Source-backed information`;
- `Professional guidance`;
- `Garden safety notice`.

The system does not label a peer as expert based on popularity.

---

## 22. Moderation

Research on online mental-health forums highlights moderation as central to both benefit and harm.

Moderators may:

- model supportive interaction;
- redirect unsafe content;
- de-escalate conflict;
- protect boundaries;
- connect to resources;
- remove abuse.

But moderation may also be perceived as:

- censorship;
- arbitrary power;
- inconsistent;
- invisible;
- retraumatizing;
- slow.

### Requirement

Any Garden community requires:

- published rules;
- trained human moderation;
- escalation paths;
- appeals;
- coverage expectations;
- wellbeing support for moderators;
- transparent enforcement;
- language and cultural competence;
- incident logs;
- no sole reliance on AI moderation.

---

## 23. AI in social interaction

AI may help:

- draft a support request;
- clarify desired support;
- summarize logistics with consent;
- suggest nonjudgmental language;
- identify data sharing boundaries;
- facilitate turn-taking.

AI must not:

- decide who is right;
- infer a partner's motive;
- grade relationship quality;
- privately coach both sides using hidden information;
- reveal one person's reflection to influence another;
- generate pressure;
- simulate group consensus;
- impersonate a member;
- mediate high-conflict or abusive relationships as neutral authority.

---

## 24. Confidentiality between parties

If two people use Garden:

- each has separate private space;
- AI context is partitioned;
- private content from A cannot influence advice to B;
- shared content has explicit provenance;
- no secret cross-analysis;
- no couple score;
- no «what your partner really feels»;
- each can export their contribution;
- one person's deletion rights are preserved.

---

## 25. Conflict and separation

Social features must assume relationships can end.

Required flows:

- pause sharing instantly;
- leave privately;
- remove future access;
- retain own copy where lawful;
- delete shared object;
- handle disputed shared content;
- stop notifications;
- revoke links;
- rotate keys/tokens;
- prevent re-invite harassment;
- show access history.

Garden does not ask users to explain why they leave.

---

## 26. Shared content ownership

A shared message may contain data about both people.

The product needs rules for:

- authorship;
- copies;
- editing;
- deletion;
- export;
- screenshots outside system;
- moderation evidence;
- legal holds.

### Honest boundary

Garden cannot guarantee that another human will forget, delete a screenshot or stop using knowledge already seen.

This must be clear before sharing.

---

## 27. Social graph minimization

Garden does not build a broad social graph unless necessary.

Alpha does not require:

- contact upload;
- follower graph;
- public discovery;
- friend suggestions;
- social proof;
- mutual connections;
- address-book matching.

Invite by specific secure link or verified account, with narrow purpose.

---

## 28. Human bridge

R-010 proposed a human bridge when AI should not be the primary interpreter or source of support.

R-014 clarifies:

A human bridge is not:

- automatic disclosure;
- a warning sent behind the user’s back;
- «tell your partner everything»;
- replacement of professional care with peers.

It is:

- helping formulate a request;
- identifying an appropriate person;
- planning timing;
- defining what can be shared;
- preparing for different responses;
- preserving the option not to send.

---

## 29. Social Layer Levels

### S0 — Solo

No social data.

### S1 — Prepared connection

Garden helps prepare an offline request, but sends nothing.

### S2 — One-time share

A user-controlled message or artifact.

### S3 — Trusted person role

Narrow permission around one practice.

### S4 — Shared practice

A jointly owned coordination object with private individual spaces.

### S5 — Small circle

Moderated or self-governed small group with explicit rules.

### S6 — Community

Discovery, peer interaction and content moderation.

### S7 — Public network

Feed, follows, ranking and broad social graph.

### Recommended product boundary

Alpha can explore S1–S3.

S4 only after dyadic consent and separation testing.

S5–S7 remain outside Alpha.

---

## 30. Trusted Person Model

Available roles:

### Listener

Receives a chosen message. No data access.

### Practical helper

Receives a specific request.

### Witness

Can see a user-selected event or statement.

### Co-practitioner

Participates in one shared practice.

### Contact for difficult moment

Appears as an option the user can choose; no automatic alert in Alpha.

Roles do not grant access to:

- full Garden;
- history;
- AI memory;
- other contacts;
- inferred state.

---

## 31. Reciprocity

Support should not automatically require equal disclosure or equal performance.

But Garden must make visible:

- who is giving labor;
- whether one person always initiates;
- whether helper wants to continue;
- whether requests exceed capacity;
- whether refusal is safe.

### Supporter controls

A helper can:

- accept;
- decline;
- set availability;
- choose role;
- pause;
- leave;
- report coercion or harm;
- prevent repeated requests.

---

## 32. Notifications

Allowed:

- invitation;
- accepted shared event;
- chosen coordination reminder;
- direct user message;
- permission change;
- safety/moderation notice.

Not allowed by default:

- «Alexandra missed her practice»;
- «She may need encouragement»;
- mood alerts;
- location alerts;
- AI-generated concern;
- inactivity escalation;
- relationship-health warnings.

---

## 33. Metrics

### Human outcomes

- perceived support fit;
- autonomy;
- connection;
- practical help received;
- ability to refuse;
- lower isolation;
- transfer to real-world communication;
- balanced support burden;
- safe exit.

### Guardrails

- pressure;
- surveillance;
- unwanted disclosure;
- jealousy;
- conflict;
- co-rumination;
- misinformation;
- harassment;
- dependency;
- helper burden;
- offline displacement;
- coercion.

### Not North Star

- number of friends;
- group messages;
- reactions;
- shares;
- social DAU;
- invites sent;
- public disclosure;
- streak of pair;
- community time.

---

## 34. Alpha experiment

Compare:

### A. Prepared offline request

Garden helps write and plan but does not connect accounts.

### B. One-time narrow share

User sends a selected request.

### C. Trusted person role

Limited ongoing permission around one practice.

Measure:

- support received;
- perceived fit;
- pressure;
- clarity;
- privacy understanding;
- relationship friction;
- ability to revoke;
- helper burden;
- behavior in real life;
- need for product mediation.

Do not test public feed as an engagement experiment.

---

## 35. Claim Registry

| Claim ID | Утверждение | Источники | Уверенность | Статус |
|---|---|---|---|---|
| R014-C01 | Social support includes emotional, instrumental, informational and appraisal functions | SRC-SOC-001, 002 | высокая as framework | foundation |
| R014-C02 | Any social support is beneficial | no | отсутствует | rejected |
| R014-C03 | Autonomy-supportive support can relate to better self-care/outcomes | SRC-SOC-003, R-008 | средняя in health contexts | foundation |
| R014-C04 | Dyadic interventions include multiple distinct mechanisms | SRC-SOC-004 | высокая | foundation |
| R014-C05 | Adding a partner universally improves behavior | SRC-SOC-005 | no, small/mixed effects | rejected |
| R014-C06 | Digital peer support can improve connection and some outcomes | SRC-SOC-006–008 | средняя, heterogeneous | limited support |
| R014-C07 | Longer peer support exposure is always better | SRC-SOC-008 | not supported | rejected |
| R014-C08 | Online peer support can produce co-rumination and adverse interactions | SRC-SOC-009–012 | средняя | safety foundation |
| R014-C09 | Co-rumination can coexist with relational closeness and distress | SRC-SOC-013–016 | высокая | foundation |
| R014-C10 | Social comparison affects all users similarly | SRC-SOC-017, 018 | rejected | constraint |
| R014-C11 | Moderation shapes safety and benefit in peer forums | SRC-SOC-009, 019, 020 | высокая | launch gate |
| R014-C12 | AI moderation alone can safely operate mental-health community | no | absent | rejected |
| R014-C13 | Shared practice implies consent to share reflections | no | absent | rejected |
| R014-C14 | One-time narrow sharing is safer than full profile access | privacy/design synthesis | средняя | proposed |
| R014-C15 | Trusted Person Model improves support without pressure | no direct Garden data | низкая | product hypothesis |
| R014-C16 | Prepared offline request may deliver value without social graph | no direct Garden data | низкая | mandatory comparator |
| R014-C17 | Public feed is necessary for community benefit | no | absent | rejected |
| R014-C18 | Social layer must account for coercive control and unequal power | SRC-SOC-021, R-012 | высокая | safety requirement |
| R014-C19 | Relationship support should lead outward to human interaction | Garden philosophy + qualitative peer literature | средняя | philosophy candidate |
| R014-C20 | Social engagement metrics are proxies for human connection | no | absent | rejected |

---

## 36. Основные источники

- SRC-SOC-001 — Cohen & Wills (1985), social support and buffering hypothesis.
- SRC-SOC-002 — Graven & Grant (2014), four social-support types in self-care.
- SRC-SOC-003 — Lee et al. (2019), autonomy support and diabetes self-management.
- SRC-SOC-004 — Di Maio et al. (2024), compendium of dyadic intervention techniques.
- SRC-SOC-005 — Martire et al. (2010), couple-oriented intervention meta-analysis.
- SRC-SOC-006 — Fortuna et al. (2020), digital peer support systematic review.
- SRC-SOC-007 — Marshall et al. (2024), realist theory of online peer-support impacts.
- SRC-SOC-008 — Yeo et al. (2025), digital peer support meta-analysis.
- SRC-SOC-009 — Easton et al. (2017), adverse events in online peer support.
- SRC-SOC-010 — Kruzan et al. (2023), perceived benefits and harms of peer-support apps.
- SRC-SOC-011 — Abou Seif et al. (2022), peer support for self-harm review.
- SRC-SOC-012 — Strand et al. (2020), online/offline peer support concerns.
- SRC-SOC-013 — Rose et al. (2007), prospective co-rumination findings.
- SRC-SOC-014 — Starr & Davila (2009), co-rumination clarification.
- SRC-SOC-015 — Mackenzie et al. (2023), support seeking and co-rumination.
- SRC-SOC-016 — Stone et al. (2022), co-rumination and social media communication.
- SRC-SOC-017 — Tong et al. (2022), personalized social comparison preferences.
- SRC-SOC-018 — self-tracking/quantified-self systematic review.
- SRC-SOC-019 — Deng et al. (2023), moderators in peer-support communities.
- SRC-SOC-020 — online mental-health forum safety realist study (2025).
- SRC-SOC-021 — digital partner surveillance and relationship research.
- SRC-SOC-022 — R-008, Chosen Support Model.
- SRC-SOC-023 — R-012, privacy/security boundaries.

---

## 37. Что исследование не доказывает

R-014 не доказывает:

- что social features нужны Garden;
- что близкий человек даст подходящую поддержку;
- что explicit consent полностью устраняет coercion;
- что one-time sharing безопасно;
- что circles cannot be useful;
- что moderation предотвращает all harm;
- что co-rumination can be reliably detected;
- что people will understand granular permissions;
- что prepared offline request equals human connection;
- что AI facilitation will not distort relationships;
- что public community can never be built responsibly;
- что social comparison is always harmful.

---

## 38. Вердикт

Garden должен помогать человеку не собирать аудиторию, а получать подходящую связь.

Социальная функция хороша, если она:

- начинается с конкретной потребности;
- оставляет внутреннее пространство закрытым;
- различает помощь и контроль;
- учитывает ресурс второго человека;
- допускает отказ с обеих сторон;
- не создаёт соревнования;
- не награждает раскрытие;
- умеет завершаться;
- переводит связь из приложения в жизнь.

> **Garden не строит социальную сеть вокруг внутренней жизни. Он создаёт узкие, добровольные мосты между людьми — и не превращает мост в наблюдательную башню.**
