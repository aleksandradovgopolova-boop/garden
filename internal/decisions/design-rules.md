---
title: "Garden Design Rules"
status: accepted
owner: "Architecture"
updated: 2026-10-05
review_cycle: quarterly
source_of_truth: true
---

# Garden Design Rules

Historical proposal collection. Each GDR remains proposed unless the decision registry records an explicit approval. The accepted container status does not approve its embedded proposals. See [Decision Log](decision-log.md) for precedence and unresolved provenance.

---

## Imported source: `GDR-005_voice_and_calibrated_trust_proposed.md`

# GDR-005 — Голос Garden поддерживает субъектность и калиброванное доверие

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

R-004 показало, что язык Garden является механизмом влияния.

Риски:

- чрезмерно позитивные утверждения;
- reactance;
- фиктивный выбор;
- инфантилизация;
- личностные ярлыки;
- ложная уверенность ИИ;
- зависимость от готовых интерпретаций.

## Варианты

### A. Максимально тёплый companion voice

Риск: зависимость, faux-empathy и родительская позиция.

### B. Нейтральный аналитический голос

Риск: холодность и недостаточная поддержка.

### C. Адаптивный взрослый голос с epistemic calibration

Тепло меняется в пределах этических ограничений, а уверенность соответствует основанию.

## Предлагаемое решение

Выбрать вариант C.

Голос Garden:

- обращается ко взрослому;
- различает факт, наблюдение и гипотезу;
- использует реальный выбор;
- избегает неправдоподобной позитивности;
- не присваивает мотив;
- не хвалит послушание;
- не имитирует человеческую близость;
- помогает человеку сформулировать собственный язык;
- заканчивает разговор после появления ясности.

## Последствия

- четыре режима различаются плотностью и температурой, но не этикой;
- спокойный режим — кандидат, но не доказанный default;
- прямой режим не становится директивным;
- AI Gardener получает epistemic layer;
- Language QA включает reactance, dignity и overtrust;
- эффект голоса проверяется экспериментально.

## Что заставит пересмотреть

- маркировка uncertainty раздражает и не помогает;
- нейтральный голос даёт ту же пользу с меньшей зависимостью;
- tone modes не различаются;
- адаптация голоса усиливает ощущение манипуляции;
- самостоятельный язык человека не развивается.

## Статус решения

Меняется на `accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-006_practice_as_core_entity_proposed.md`

# GDR-006 — Базовая сущность Garden: практика, а не привычка

**Дата:** 15 июля 2026  
**Статус:** `proposed`

The user-language portion is superseded by [GDR-006A](gdr/gdr-006a-ritual-user-core.md). Remaining unapproved proposals are not implementation requirements.

## Контекст

Слоган Garden использует слово «ритуал». R-006 показало, что научный термин неоднороден и часто включает ригидность, формальность, символизм и социальную предписанность.

Большинство планируемых сущностей Garden должны быть осмысленными, адаптируемыми, не обязательно автоматичными и способными завершаться.

## Варианты

### A. Ритуал как единственная сущность

Выразительно, но концептуально неточно.

### B. Практика как базовая сущность; ритуал как особый случай

Сохраняет бренд и позволяет различать behavior types.

### C. Привычка как базовая сущность

Понятно рынку, но сдвигает Garden к automaticity и habit tracking.

### D. Пользователь сам выбирает термин

Автономно, но размывает внутреннюю модель.

## Предлагаемое решение

Выбрать вариант B:

> В продуктовой модели Garden пользователь создаёт **практики**.  
> Практика может стать привычкой, рутиной или личным ритуалом.

Слоган «Маленькие ритуалы. Большой сад» сохраняется до пользовательской проверки.

## Последствия

- обновить Product Model;
- не использовать habit formation как универсальную цель;
- добавить одноразовые шаги и задачи;
- создать anti-rigidity requirements;
- провести терминологическое исследование;
- не менять Bible до утверждения.

## Что заставит пересмотреть

- «практика» непонятна или звучит клинически;
- раздвоение терминов ухудшает onboarding;
- пользователи естественно понимают ritual именно в смысле Garden;
- классификация не даёт продуктовой пользы.

## Статус решения

Меняется на `accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-007_bounded_reflection_proposed.md`

# GDR-007 — Рефлексия Garden должна быть ограниченной и завершаемой

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

R-007 показало, что самофокус и repeated thought могут быть конструктивными или неконструктивными. Бесконечный AI dialogue создаёт особый риск: продукт всегда способен предложить ещё одну интерпретацию, даже когда она не добавляет понимания.

## Варианты

### A. Свободная неограниченная рефлексия

Плюсы: ощущение глубины и свободы.

Риски: rumination, disclosure pressure, endless interpretation и dependency.

### B. Только tracking без диалога

Плюсы: минимальное вмешательство.

Риски: данные без смысла, self-audit и ложные графические выводы.

### C. Bounded Reflection

Человек выбирает цель разговора, Garden ограничивает число вопросов и гипотез, а взаимодействие обязательно допускает Closure.

## Предлагаемое решение

Выбрать вариант C.

Garden:

- не требует ежедневной глубокой рефлексии;
- начинает с разрешения;
- привязывает разговор к конкретному событию;
- отделяет факт от интерпретации;
- исследует один вопрос;
- предлагает максимум две гипотезы;
- поддерживает решение «оставить открытым»;
- использует stop rules;
- не создаёт новый вопрос после Closure;
- оценивает эмоциональную цену.

## Последствия

- изменить Daily Check-in;
- убрать engagement through endless follow-up;
- ограничить Weekly Reflection;
- добавить режимы Record / Understand / Decide / Release;
- создать rumination red-team;
- ввести pattern requirements;
- не использовать number of insights как KPI.

## Что заставит пересмотреть

- bounded loop воспринимается как слишком жёсткий;
- neutral record даёт равную пользу с меньшим риском;
- пользователи закрывают разговор преждевременно;
- stop rules ошибочно блокируют полезное осмысление;
- режимы усложняют опыт;
- AI всё равно создаёт overtrust.

## Статус решения

`accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-008_chosen_support_not_product_ownership_proposed.md`

# GDR-008 — Garden поддерживает выбранное обязательство, но не владеет им

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

R-008 показало, что accountability способна помогать действию, но цифровой продукт легко превращает её в adherence к себе.

Особый риск Garden:

- тёплый AI воспринимается как моральный свидетель;
- обещание сохраняется после изменения обстоятельств;
- engagement принимается за пользу;
- напоминания усиливаются после молчания;
- Garden начинает защищать прежнюю цель от текущего решения человека.

## Варианты

### A. AI accountability partner

Пользователь отчитывается перед Garden.

Риск: ложные отношения, вина, dependency и product-centered adherence.

### B. Никакой активной поддержки

Риск: продукт не помогает преодолеть intention–action gap.

### C. Chosen Support Contract

Человек выбирает форму поддержки, Garden выполняет её в прозрачных пределах и регулярно возвращает право пересмотра.

## Предлагаемое решение

Выбрать вариант C.

Принципы:

- обязательство принадлежит человеку;
- support opt-in;
- expectations process-oriented;
- no hard commitments;
- no punishment;
- no escalation after silence;
- current choice can override past choice;
- changed conditions are considered;
- engagement is not the outcome;
- Garden teaches self-nudging and environment design;
- support should become less necessary.

## Последствия

- создать Chosen Support Model;
- пересобрать reminders;
- добавить support contract в Practice;
- определить beneficial disengagement;
- убрать «ты обещала»;
- запретить financial/social stakes в ранней версии;
- добавить human-support handoff;
- измерять reactance, guilt и dependence.

## Что заставит пересмотреть

- контракт слишком сложен;
- пользователи не понимают настройки;
- no-support condition даёт равную пользу;
- support contract повышает planning burden;
- пользователи всё равно воспринимают AI как судью;
- снижение intervention after silence пропускает нужную помощь;
- human connection создаёт privacy и coercion risks.

## Статус решения

`accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-009_explicit_voice_not_identity_inference_proposed.md`

# GDR-009 — Garden персонализирует стиль по выбору, а не по идентичности

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

R-009 показало:

- autonomy не равна individualism;
- прямота и вежливость зависят от контекста;
- внутри культур существует значительное разнообразие;
- gender и age stereotypes искажают коммуникацию;
- sociolect mirroring не гарантирует доверия;
- персонализация способна усиливать убеждение и overtrust.

## Варианты

### A. Один универсальный голос

Просто, но может быть культурно и функционально неуместным.

### B. Автоматическая адаптация по профилю

Удобно, но создаёт скрытые выводы, стереотипизацию и persuasion risk.

### C. Explicit Voice Contract

Этика фиксирована. Пользователь явно выбирает стиль, а контекстные изменения не сохраняются без согласия.

## Предлагаемое решение

Выбрать вариант C.

Garden:

- имеет спокойный взрослый default;
- позволяет выбрать формальность, тепло, прямоту, длину, метафору, вопросы и инициативность;
- не адаптируется по полу, стране, возрасту или диагнозу;
- не копирует социолект по умолчанию;
- подтверждает наблюдаемое предпочтение перед сохранением;
- показывает и позволяет удалить Voice Contract;
- не меняет факты и safety boundaries ради совпадения с пользователем;
- не оптимизирует стиль под согласие и engagement.

## Последствия

- создать Voice Personalization Model;
- изменить Garden Voice;
- добавить видимые настройки;
- создать no-mimicry policy;
- тестировать native-language scenarios;
- добавить gender/culture/accessibility audit;
- отделить localization от psychological personalization;
- хранить voice preferences отдельно от sensitive profile.

## Что заставит пересмотреть

- Voice Contract создаёт лишнюю нагрузку;
- большинство пользователей не понимают параметры;
- fixed default показывает равную пользу;
- настройки усиливают overtrust;
- no-mimicry воспринимается как холодность;
- explicit preference не отражает реальную потребность;
- accessibility требует более активной адаптации.

## Статус решения

`accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-010_ai_does_not_own_interpretation_proposed.md`

# GDR-010 — AI Gardener предлагает версии, но не владеет интерпретацией

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

R-010 показало:

- люди часто следуют AI-совету даже без доказанной долгосрочной пользы;
- LLMs склонны к social sycophancy;
- персонализация и позитивный persuasive language повышают доверие;
- relational affordances способны создавать emotional dependence;
- long-term memory усиливает cross-domain leakage и sycophancy;
- связный AI-нарратив может стать ложной идентичностью.

## Варианты

### A. AI Insight Engine

Garden самостоятельно выявляет скрытые паттерны и сообщает выводы.

Риск: overtrust, identity fixation, sycophancy и ложная причинность.

### B. Только хранение без интерпретации

Безопаснее, но теряется значительная часть ценности AI.

### C. Bounded Co-Interpretation

Garden показывает данные, предлагает ограниченные версии, ищет альтернативы, принимает исправление и возвращает право значения человеку.

## Предлагаемое решение

Выбрать вариант C.

AI Gardener:

- не является главным толкователем;
- не производит identity or diagnosis claims;
- маркирует epistemic level;
- предлагает максимум две гипотезы;
- включает alternative and disconfirming evidence;
- не сохраняет AI hypothesis как fact;
- принимает correction без спора;
- не использует memory для persuasion;
- не создаёт relational debt;
- предлагает human bridge;
- умеет завершать и забывать.

## Последствия

- внедрить AI Interpretation Protocol;
- создать Memory Governance Model;
- добавить epistemic UI;
- создать correction/deletion flow;
- запретить AI-generated psychological profile;
- отделить support from endorsement;
- измерять overtrust, sycophancy and dependence;
- ограничить anthropomorphic copy;
- high-stakes recommendation требует external verification.

## Что заставит пересмотреть

- пользователи не понимают epistemic markers;
- альтернативы увеличивают тревогу;
- protocol делает Garden бесполезно осторожным;
- correction flow редко используется;
- bounded hypotheses всё равно становятся identity labels;
- memory controls слишком сложны;
- neutral non-interpretive mode даёт равную пользу с меньшим риском;
- human bridge недоступен или вызывает давление.

## Статус решения

`accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-011_measurement_is_intervention_proposed.md`

# GDR-011 — Измерение Garden является вмешательством, а не нейтральным наблюдением

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

R-011 показало:

- repeated assessment может менять внимание и поведение;
- Personal Informatics не гарантирует insight или action;
- self-report meaning может изменяться со временем;
- validated scales зависят от construct, context, population and use;
- passive sensing не даёт объективной психологической истины;
- measure, превращённое в target, искажает поведение;
- общий score скрывает ценностные решения.

## Варианты

### A. Rich Quantified Garden

Собирать много данных, строить scores и персональные patterns.

Риск: surveillance, false certainty, burden, Goodhart effects and moralization.

### B. No measurement

Максимальная осторожность, но теряется память и возможность проверять гипотезы.

### C. Minimal Purpose-Bound Measurement

No-tracking является полноценным режимом. Измерение включается для конкретного вопроса, ограничивается по времени и не создаёт total score.

## Предлагаемое решение

Выбрать вариант C.

Garden:

- предлагает no-tracking mode;
- использует Measurement Contract;
- различает `not recorded`, `did not happen` и `intentionally skipped`;
- не создаёт общий Garden Score;
- не использует streaks и cross-user ranking;
- показывает missingness, exceptions and uncertainty;
- не наследует validation после изменения шкалы;
- не выводит psychological states из passive data в Alpha;
- предпочитает временные эксперименты постоянному мониторингу;
- позволяет продолжать практику после отключения measurement;
- оценивает burden and harm alongside value.

## Последствия

- внедрить Garden Measurement Model;
- создать Measurement Catalog;
- пересобрать dashboards;
- убрать moral color encoding;
- добавить no-tracking comparator в Alpha;
- отделить product telemetry от personal meaning;
- завести review gate для каждого derived metric;
- R-012 должен определить privacy/security architecture.

## Что заставит пересмотреть

- minimal record не даёт достаточной пользы;
- Measurement Contract создаёт слишком высокую нагрузку;
- пользователи не понимают missingness;
- временные эксперименты редко завершаются;
- отсутствие scores ухудшает понимание;
- passive sensor data демонстрируют проверенную пользу с приемлемым risk;
- no-tracking mode не позволяет выполнить ключевой use case.

## Статус решения

`accepted` только после явного утверждения владельца проекта.

---

## Imported source: `GDR-012_privacy_security_as_product_boundary_proposed.md`

# GDR-012 — Privacy and security are product boundaries, not compliance layers

**Дата:** 15 июля 2026  
**Статус:** `proposed`

## Контекст

Garden handles intimate free text, inferred memory and potentially health, relationship, belief, sexuality, violence and crisis information. AI and long-term memory increase usefulness and simultaneously increase surveillance, manipulation and breach risk.

A privacy notice cannot compensate for unnecessary collection, uncontrolled employee access, provider training, incomplete deletion or crisis promises the service cannot fulfil.

## Варианты

### A. Build full personalization first, add compliance before launch

Fast discovery, but creates data architecture and incentives that are costly to reverse.

### B. Store minimal records without AI memory

Lower risk but limits some proposed value.

### C. Privacy- and safety-bounded architecture

Functions launch only after need, data flow, access, deletion, provider and failure modes are proven.

## Предлагаемое решение

Choose C.

Garden adopts:

- privacy by default;
- 18+ Alpha;
- no clinical claims;
- no crisis-monitoring promise;
- no provider training on production content;
- no raw-content analytics;
- no default employee reading;
- no hidden psychological/persuasion profile;
- no passive mental-state inference;
- user-visible memory provenance and deletion;
- deterministic authorization outside the LLM;
- DPIA before real-data pilot;
- threat-model and red-team launch gates;
- the right to remove or postpone an unsafe feature.

## Consequences

- personalization will be narrower;
- some workflows require extra confirmation;
- local/on-device options require technical research;
- analytics will contain less behavioral detail;
- Alpha scope becomes smaller;
- security/privacy/safety owners are needed before pilot;
- vendor choice is constrained by retention and training contracts;
- a crisis-aware feature cannot ship from copy alone.

## What would trigger reconsideration

- independent review finds controls disproportionate or ineffective;
- local processing enables a materially safer architecture;
- clinical or child-focused product strategy is deliberately adopted with a new regulatory program;
- a provider cannot meet contractual controls and architecture changes;
- user research shows a control causes serious new safety harm.

## Status

`accepted` only after explicit owner decision and named accountable privacy/security reviewers.

---

## Imported source: `GDR-013_metaphor_as_optional_lens_proposed.md`

# GDR-013 — Метафора сада является опциональной линзой, а не моделью человека

**Дата:** 15 июля 2026  
**Статус:** `superseded`

Superseded by [GDR-013A](gdr/gdr-013a-player-owned-world.md). Retained for historical reasoning; do not implement this framing.

## Контекст

R-013 показало:

- metaphors can shape reasoning;
- effect depends on context;
- one metaphor can empower and disempower;
- garden language highlights care, process and environment;
- it can also impose growth, moralize nature and hide structural causes;
- immersive metaphor can become a disguised score;
- AI gardener framing can assign the system excessive authority.

## Варианты

### A. Fully immersive garden ontology

Every practice, state and person is represented through plant life.

Риск: distortion, infantilization, moral status, low accessibility.

### B. Brand-only metaphor

Garden remains only a name and visual identity.

Риск: loss of distinctive language and useful context framing.

### C. Layered optional metaphor

Literal core is always available. Brand atmosphere remains. Deeper mappings are explicit, user-controlled and reversible.

## Предлагаемое решение

Выбрать вариант C.

Garden:

- keeps its name and central slogan;
- provides full literal mode;
- does not represent the user as a plant;
- does not position AI as gardener of the person;
- does not use decay, weeds, pests or disease as feedback;
- does not equate bloom with success;
- does not require growth;
- preserves systemic explanations;
- labels Mycorrhiza as metaphor;
- stores AI-suggested metaphors only after confirmation;
- allows complete metaphor exit without function loss.

## Последствия

- implement Layered Metaphor Model;
- audit all interface copy and visuals;
- replace hidden plant-state scoring;
- create literal labels;
- test metaphors cross-culturally;
- add structural-context prompts;
- clarify AI Gardener role;
- red-team grief, abuse, disability and non-growth scenarios.

## Что заставит пересмотреть

- literal mode destroys product comprehension;
- user tests show metaphor causes material confusion;
- brand atmosphere alone creates unwanted evaluation;
- users cannot distinguish metaphor from claim;
- optional settings create excessive complexity;
- AI Gardener name produces relational dependence;
- cultural adaptation requires separate brand expressions.

## Статус

`accepted` только после явного решения владельца проекта.

---

## Imported source: `GDR-014_narrow_social_bridges_proposed.md`

# GDR-014 — Garden creates narrow social bridges, not a network around inner life

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Context

R-014 showed:

- support has multiple forms and must match need;
- dyadic interventions use distinct mechanisms;
- digital peer support has potential but mixed evidence and meaningful harms;
- social accountability can become surveillance;
- comparison preferences vary;
- co-rumination can increase closeness and distress simultaneously;
- moderation is operationally necessary;
- unequal relationships make formal consent insufficient.

## Options

### A. Social Garden

Profiles, friends, shared progress, feed and public/community layer.

Risk: surveillance, comparison, disclosure pressure and moderation burden.

### B. Fully solo Garden

Strong privacy, but no help transferring reflection into human relationships.

### C. Narrow social bridges

Prepare requests, one-time sharing and limited trusted-person roles. No feed or broad social graph.

## Proposed decision

Choose C.

Garden:

- does not require social participation;
- shares specific objects, not whole profiles;
- provides S1–S3 in Alpha;
- treats S4 shared practices as later tested function;
- excludes groups/community/feed from Alpha;
- has no leaderboards or public streaks;
- never discloses misses automatically;
- requires consent from both parties;
- supports safe exit;
- separates each person’s AI context;
- helps connection move into real life.

## Consequences

- implement Social Architecture Model;
- build consent/access matrix;
- test prepared offline request as baseline;
- build Trusted Person roles;
- no contact upload or friend graph;
- no community before moderation program;
- red-team coercive control and separation;
- measure helper burden and relationship friction.

## Reconsider if

- prepared offline requests provide no value;
- trusted-person role produces pressure;
- granular permissions are misunderstood;
- shared practice creates conflict;
- users need peer community for core value;
- safe moderation becomes operationally feasible;
- social functionality increases dependence on Garden rather than real relationships.

## Status

`accepted` only after explicit owner decision.

---

## Imported source: `GDR-015_relief_vs_source_change_proposed.md`

# GDR-015 — Garden distinguishes relief from source-directed change

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Context

R-015 showed:

- wellbeing is shaped across personal, relational, organizational, material and structural levels;
- individual advice can drift away from recognized upstream causes;
- personal practices can still provide real relief and capacity;
- cause, control and responsibility are different;
- burnout is an occupational phenomenon, not simply an individual resilience deficit;
- digital products can reproduce inequity and become institutional avoidance tools.

## Options

### A. Personal practice product

Garden limits itself to what the individual can do.

Risk: victim blaming and lifestyle drift.

### B. Structural analysis product

Garden foregrounds systems and avoids individual actions.

Risk: helplessness, excessive scope and false expertise.

### C. Multilevel action model

Garden names levels, separates relief from resolution and helps choose right-sized actions without claiming structural authority.

## Proposed decision

Choose C.

Garden:

- maps L1–L5;
- distinguishes cause, control and responsibility;
- labels interventions;
- always separates immediate support from source change;
- runs power, resource and safety checks;
- includes relational, organizational, institutional, collective and exit actions;
- does not provide legal verdicts;
- does not become employer resilience surveillance;
- keeps no-tracking and external-resource paths;
- treats structural recognition as part of agency, not as a reason for passivity.

## Consequences

- implement Multilevel Action Model;
- add Problem Location Protocol;
- create Intervention Integrity Labels;
- red-team recurring coping loops;
- add current external-resource verification capability;
- block employer individual data;
- include organizational/system scenarios in Alpha tests;
- update Garden Language.

## Reconsider if

- level mapping overwhelms users;
- structural framing increases helplessness;
- AI frequently misclassifies problems;
- users prefer direct personal action without analysis;
- external resources cannot be safely maintained;
- Intervention Labels appear moralistic;
- model scope becomes indistinguishable from legal/social work advice.

## Status

`accepted` only after explicit owner decision.

---

## Imported source: `GDR-016_compete_on_agency_architecture_proposed.md`

# GDR-016 — Garden competes on agency architecture, not an AI-journal feature bundle

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Context

R-016 found a crowded and converging market:

- AI journals already offer prompts, voice, memory, patterns and habits;
- self-care apps combine routines, mood and content;
- meditation platforms add AI companions;
- mental-health AI offers long-term conversation;
- trackers offer correlations and experiments;
- PKM tools offer AI thought partners;
- general AI can imitate many isolated features.

## Options

### A. Better AI journal

Compete on prompt quality, insights, memory and voice.

Risk: crowded, copyable and contrary to epistemic boundaries.

### B. Broad wellbeing super-app

Combine journal, tracker, content, community and companion.

Risk: scope, generic positioning, regulatory and dependency risk.

### C. Agency-preserving practice system

Compete on a distinctive object model, constraints and real-world outcomes.

## Proposed decision

Choose C.

Garden:

- uses practice as core object;
- has bounded rather than endless reflection;
- restricts AI interpretation;
- governs memory;
- separates relief from source change;
- makes measurement optional;
- excludes streaks and public comparison;
- designs social features as narrow bridges;
- includes completion and product exit as success;
- launches with one-direction/one-practice wedge.

## Consequences

- category copy must not lead with AI journal;
- Alpha scope remains narrow;
- competitor roadmap is tracked quarterly;
- general AI is a required comparator;
- no content-library arms race;
- no companion persona;
- business model must not require dependence;
- privacy/safety become differentiating operations, not only messaging.

## Reconsider if

- users cannot understand the category;
- closest competitors adopt the full model;
- generic AI matches outcomes;
- users will not pay for bounded support;
- no-streak practice underperforms;
- off-product success makes business unsustainable;
- safety differentiation is not visible or trusted.

## Status

`accepted` only after explicit owner decision.

---

## Imported source: `GDR-017_protect_acknowledged_uncertainty_proposed.md`

# GDR-017 — Garden protects acknowledged uncertainty, not blind ignorance

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Context

R-017 showed:

- prior knowledge can create fixation;
- expertise also provides deep representation and safety;
- curiosity benefits from bounded, visible gaps;
- intellectual humility is compatible with conviction and action;
- unrecognized ignorance can create overconfidence;
- small reversible probes can create knowledge under uncertainty;
- deliberate ignorance of project risk is often costly;
- Garden memory can become a personal Einstellung effect;
- AI can accelerate premature convergence.

## Options

### A. Pattern-driven personalization

Use past behavior and expert knowledge to recommend the most likely path.

Risk: identity lock-in and predictable solutions.

### B. Naive optimism

Encourage action before thinking about constraints.

Risk: anti-expertise, preventable harm and planning fallacy.

### C. Productive unknowing

Keep verified knowledge and safety boundaries, suspend soft assumptions and use bounded experiments.

## Proposed decision

Choose C.

Garden:

- distinguishes recognized and unrecognized ignorance;
- separates hard from soft constraints;
- includes Learn, Question, Explore and Decide modes;
- offers optional Fresh Eyes Mode;
- delays personal-history retrieval during divergence;
- prevents identity conclusions from blocking experiments;
- requires expertise gates for high-stakes domains;
- uses affordable loss and reversibility;
- asks what will be learned;
- closes exploration;
- never markets ignorance as superior to competence.

## Consequences

- implement Productive Unknowing Model;
- add Fresh Eyes Protocol;
- add constraint classification;
- update memory retrieval order;
- add AI fixation tests;
- include `Unknown` as valid outcome;
- train Garden language to admit uncertainty;
- prevent Fresh Eyes in unsafe contexts;
- incorporate R-017 into Alpha experimentation.

## Reconsider if

- hiding history causes repeated harm;
- users misread the mode as motivational optimism;
- Garden misclassifies hard constraints;
- Fresh Eyes increases reckless action;
- users feel their experience is being dismissed;
- expertise gate becomes excessive friction;
- divergent options worsen paralysis;
- generic brainstorming provides equal value.

## Status

`accepted` only after explicit owner decision.

---

## Imported source: `GDR-018_persistent_player_owned_place_proposed.md`

# GDR-018 — Garden is a persistent player-owned place, not a decorated dashboard

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden should be designed as a persistent personal place.

It must provide:

- stable spatial continuity;
- meaningful empty space;
- user naming and customization;
- persistent reversible traces;
- user-controlled history;
- safe absence;
- safe departure.

## It must not

- auto-decorate the user’s identity;
- infer psychology from layout;
- use decay to force return;
- make ambient animals dependent;
- make weather a mood score;
- use artificial scarcity or FOMO;
- destroy value after cancellation or absence.

## Open decision

The product must test whether the dominant creation model is:

- ritual-first;
- place-first;
- hybrid.

## Alpha consequence

Add a place-first prototype and measure ownership separately from task completion.

---

## Imported source: `GDR-019_garden_language_system_proposed.md`

# GDR-019 — Garden language preserves adult agency and world coherence

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden adopts a formal language system.

User-facing language:

- uses Ritual, Garden, Place, Review, Rest, Complete and Release;
- avoids task, streak, failure, achievement and optimization framing;
- marks AI uncertainty;
- never creates emotional debt;
- always offers literal equivalents for metaphor;
- ends conversations when sufficient clarity appears.

## Consequences

- all UX copy must pass Language QA;
- AI prompts must encode epistemic labels;
- notifications require separate review;
- safety mode disables metaphor;
- product analytics names remain internal;
- “AI coach”, “AI friend” and “AI therapist” are prohibited positioning.

---

## Imported source: `GDR-020_designed_incompleteness_proposed.md`

# GDR-020 — Garden uses designed incompleteness rather than finished perfection

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision candidate

The initial garden should be:

- visually coherent;
- cared for;
- incomplete enough to invite authorship;
- free of implied missing progress.

The product should not present a fully decorated canonical garden as the ideal.

## Alpha test

Compare polished pre-decoration with designed incompleteness. Measure beauty, ownership, fear of changing, desire to create, cultural fit, accessibility and perceived judgment.

---

## Imported source: `GDR-021_cultural_borrowing_without_collage_proposed.md`

# GDR-021 — Garden learns from garden histories without becoming a cultural collage

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden may use spatial and interaction principles learned from historical garden traditions.

It must not combine identifiable cultural motifs as a generic “calm garden” aesthetic without documenting origin, meaning and transformation.

## Requirements

- Cultural Borrowing Protocol;
- Atlas provenance;
- fictional core world rather than direct replica;
- cultural review for identifiable motifs;
- user choice of aesthetics;
- no tradition described as universally calming, natural or humane.

## Core position

> Garden knows the history of gardens but does not pretend to be one of them.

---

## Imported source: `GDR-022_colour_not_psychological_score_proposed.md`

# GDR-022 — Colour belongs to the world, not to a psychological score

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden uses colour for:

- atmosphere;
- materials;
- interaction;
- hierarchy;
- user expression.

Garden does not use colour to infer or judge:

- mood;
- wellbeing;
- discipline;
- success;
- failure;
- ritual value.

## Requirements

- no colour-only information;
- no green/good and red/bad lifecycle;
- palette families rather than personality palettes;
- light and dark worlds have equal status;
- high-contrast mode is aesthetically complete;
- preference is explicit, not demographic;
- archive is not automatically grey;
- no premium-only dignity.

---

## Imported source: `GDR-023_light_not_person_state_proposed.md`

# GDR-023 — Light creates space and atmosphere, not a state of the person

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden uses light for:

- depth;
- materials;
- atmosphere;
- time;
- focus;
- user expression.

It does not use light to infer or indicate:

- wellbeing;
- success;
- failure;
- neglect;
- crisis;
- productivity.

## Requirements

- separate world and UI lighting;
- optional real-time synchronization;
- complete night usability;
- reduced-motion and static-light modes;
- no circadian or therapeutic claims;
- no lifecycle mapped to brightness;
- user control of local lights;
- safety mode removes ambient transitions.

---

## Imported source: `GDR-024_materials_carry_chosen_history_proposed.md`

# GDR-024 — Materials carry chosen history, never punishment

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden uses a materially legible stylised world.

Materials communicate through:

- light;
- texture;
- motion;
- sound;
- shape;
- contextual behavior.

## Boundaries

- no automatic decay after absence;
- no rust, cracks, dirt or fading as ritual feedback;
- patina and repair are user-chosen;
- material age is not lifecycle state;
- “natural” is not described as inherently ethical or therapeutic;
- no status economy based on rare materials in Alpha;
- reduced-detail and accessible modes remain aesthetically complete.

## Core formula

> Objects may remember chosen use. They never accuse the owner of neglect.

---

## Imported source: `GDR-025_time_adds_history_not_debt_proposed.md`

# GDR-025 — Time adds history, never debt

**Дата:** 16 июля 2026  
**Статус:** `proposed`

## Decision

Garden may use:

- calendar dates;
- ambient time;
- user-selected seasons;
- world cycles;
- personal epochs.

It must not use time to create:

- decay;
- streak loss;
- backlog;
- guilt;
- forced urgency;
- limited-time status;
- automatic ritual failure.

## Requirements

- optional time modes;
- exact dates recoverable;
- user-created epochs;
- no AI-generated life chapter without confirmation;
- freeze time;
- no lifecycle transition from inactivity;
- no seasonal FOMO;
- unchanged return after absence.

## Core formula

> Time in Garden adds history, never debt.

---

## Imported source: `GDR-026_ambient_life_not_digital_pets_proposed.md`

# GDR-026 — Garden contains independent ambient life, not dependent digital pets

**Дата:** 17 июля 2026  
**Статус:** proposed

## Decision

Alpha uses ambient wildlife only.

Living beings:

- do not need care;
- do not suffer;
- do not respond to absence;
- do not speak for AI;
- are not collectible;
- do not create rarity or status;
- can be disabled;
- may appear and leave independently.

## Deferred

- cats and dogs;
- named companions;
- persistent individual animals;
- feeding;
- following;
- petting;
- breeding;
- loss;
- animal memory;
- educational catalogue.

> **Life exists in the garden without becoming another responsibility.**

---

## Imported source: `GDR-027_silence_complete_sound_not_control_proposed.md`

# GDR-027 — Silence is a complete Garden; sound creates presence, not emotional control

**Дата:** 17 июля 2026  
**Статус:** `proposed`

## Decision

Garden separates:

- ambience;
- music;
- interaction sounds;
- accessibility audio.

## Requirements

- Silent mode has full functionality;
- no essential meaning through sound alone;
- sound layers controlled independently;
- music off by default in review;
- no inferred mood soundtrack;
- no obvious short loops;
- no animal attention calls;
- safety mode disables decorative audio;
- accessibility speech has priority;
- no microphone analysis or environmental listening.

## Core formula

> Sound may make the world present. It must not decide how the person should feel.

---

## Imported source: `GDR-028_objects_form_places_not_meaning_proposed.md`

# GDR-028 — Objects help form places; they do not assign meaning

**Дата:** 17 июля 2026  
**Статус:** proposed

## Решение

Garden рассматривает места как основную единицу композиции мира.

Объекты:

- поддерживают пространственные отношения;
- дают контекстные возможности;
- могут оставаться декоративными;
- могут связываться с ритуалами и памятью;
- получают значение от пользователя.

## Требования

- нет универсальной символики;
- нет personality inference по layout;
- lifecycle объекта и ритуала разделены;
- не каждый объект интерактивен;
- landmarks ограничены и стабильны;
- есть доступное не-spatial editing;
- нет object economy в Alpha;
- AI suggestions требуют подтверждения.

> **Objects make places possible. People make places meaningful.**

---

## Imported source: `GDR-029_conditions_for_place_not_attachment_proposed.md`

# GDR-029 — Garden creates conditions for place, not attachment

**Дата:** 17 июля 2026  
**Статус:** `proposed`

## Decision

Place is the primary spatial unit of Garden.

Garden supports:

- boundaries;
- centers;
- paths;
- views;
- spatial qualities;
- atmosphere;
- use;
- history;
- optional naming.

## Requirements

- attachment is not measured or optimized;
- all Alpha places are private;
- no universal prospect/refuge prescription;
- no identity inference from layouts;
- emptiness is allowed;
- direct accessible navigation;
- visual privacy separated from permissions;
- templates contain no personality or wellbeing claims;
- lifecycle and changes remain user-controlled.

## Core formula

> Garden creates conditions for place. The person creates belonging.

---

## Imported source: `GDR-030_world_variation_persistent_change_requires_authorship_proposed.md`

# GDR-030 — The world may vary; persistent evolution requires authorship

**Статус:** proposed

Garden allows autonomous ambient variation but forbids autonomous persistent evolution in Alpha.

Requirements:

- no autonomous growth;
- no decay;
- no absence effects;
- reversible presets;
- Manual and Frozen modes;
- persistent changes require confirmation;
- snapshots and variants;
- visible change log;
- migrations preserve authored worlds;
- AI cannot silently transform the world.

> The world may change around the user. It must not change the user’s world without them.

---

## Imported source: `GDR-031_movement_optional_access_direct_proposed.md`

# GDR-031 — Movement is optional; access is direct

**Дата:** 17 июля 2026  
**Статус:** `proposed`

## Decision

Garden supports equal spatial and direct navigation.

## Requirements

- every destination has direct access;
- search is primary;
- no forced walking;
- no travel time;
- no fog of war;
- no completion map;
- user-controlled entry point;
- neutral return after absence;
- clear mode and privacy context;
- list/tree accessibility;
- reduced motion;
- one-place usage is complete.

## Core formula

> You may wander. You may also arrive directly. Both are Garden.

---

## Imported source: `GDR-032_ai_proposes_user_commits_proposed.md`

# GDR-032 — AI proposes; the user commits

**Дата:** 17 июля 2026  
**Статус:** `proposed`

## Decision

AI-generated changes remain proposals until explicitly accepted.

## Requirements

- clear View/Edit modes;
- complex changes begin as drafts;
- before/after preview;
- visible assumptions;
- partial acceptance;
- immediate undo;
- version history;
- trash and recovery;
- provenance;
- manual creation complete;
- AI intensity controlled by user;
- no autonomous apply.

## Core formula

> AI can help imagine the garden. Only the person decides what grows into reality.

---

## Imported source: `GDR-033_rituals_recognized_not_enforced_proposed.md`

# GDR-033 — Rituals are recognized, not enforced

**Дата:** 17 июля 2026  
**Статус:** `proposed`

## Decision

Garden supports meaningful practices without streak, failure states or required logging.

## Requirements

- distinguish task, habit, routine and ritual;
- no streak;
- no failed occurrence;
- completion optional;
- logging optional;
- no quality score;
- no frequency morality;
- lineage;
- retrospective creation;
- lifecycle controlled by user;
- ending is legitimate;
- AI pattern detection opt-in;
- no ritual inferred or created without confirmation.

## Core formula

> A ritual is not something Garden makes the person obey. It is something the person may choose to recognize as their own.

---

## Imported source: `GDR-034_garden_memory_not_second_brain_proposed.md`

# GDR-034 — Garden memory is not a second brain

**Статус:** proposed

Garden memory supports places, rituals and lived experience without becoming a knowledge graph, notes system or external-memory architecture.

Requirements:

- no graph view;
- no arbitrary semantic linking;
- no automatic related memories;
- no importance ranking;
- no unsolicited resurfacing;
- no inferred emotional meaning;
- search-first retrieval;
- one primary place link in Alpha;
- later reflections do not overwrite originals;
- user-controlled hide, archive, export and delete;
- explicit boundary from «Нити».

> Garden holds what the person chooses to keep. It does not turn a life into a database.

---

## Imported source: `GDR-035_garden_uses_context_not_graph_proposed.md`

# GDR-035 — Garden uses context, not a knowledge graph

**Дата:** 17 июля 2026  
**Статус:** `proposed`

## Decision

Garden uses a small enumerated set of functional relations and does not develop a semantic graph.

## Requirements

- no graph view;
- no backlinks;
- no arbitrary relation types;
- no semantic clusters;
- no automatic related content;
- no inferred themes;
- spatial composition as primary organizing model;
- user meaning remains text;
- Garden and «Нити» keep separate schemas;
- any future transfer is explicit and user-controlled.

## Core formula

> Garden holds things in context. «Нити» may connect ideas. They are not the same work.

---

## Imported source: `GDR-036_privacy_is_starting_condition_proposed.md`

# GDR-036 PRIVACY IS STARTING CONDITION

**Статус:** `proposed`

Privacy is the starting condition of Garden.

---

## Imported source: `GDR-037_presence_is_contextual_not_social_proposed.md`

# GDR-037 PRESENCE IS CONTEXTUAL NOT SOCIAL

**Статус:** `proposed`

Presence is contextual, not social.

---

## Imported source: `GDR-038_garden_witnesses_but_does_not_diagnose_proposed.md`

# GDR-038 GARDEN WITNESSES BUT DOES NOT DIAGNOSE

**Статус:** `proposed`

Garden witnesses expression but does not diagnose.

---

## Imported source: `GDR-039_a_garden_may_wait_proposed.md`

# GDR-039 A GARDEN MAY WAIT

**Статус:** `proposed`

A Garden may wait; no retention pressure.

---

## Imported source: `GDR-040_begin_with_one_place_proposed.md`

# GDR-040 BEGIN WITH ONE PLACE

**Статус:** `proposed`

Onboarding begins with one place.

---

## Imported source: `GDR-041_alpha_constitution_proposed.md`

# GDR-041 ALPHA CONSTITUTION

**Статус:** `proposed`

Alpha tests meaningful return without obligation.

---

## Imported source: `GDR-042_two_equal_navigation_systems_proposed.md`

# GDR-042 — Two equal navigation systems

**Статус:** `proposed`

Spatial and direct navigation are equal.

---

## Imported source: `GDR-043_preview_is_a_separate_state_proposed.md`

# GDR-043 — Preview is a separate state

**Статус:** `proposed`

Preview cannot mutate committed Garden state.

---

## Imported source: `GDR-044_ai_uses_minimum_context_proposed.md`

# GDR-044 — AI uses minimum context

**Статус:** `proposed`

Full-Garden context is prohibited by default.

---

## Imported source: `GDR-045_design_system_encodes_ethics_proposed.md`

# GDR-045 — Design system encodes ethics

**Статус:** `proposed`

Reversibility, privacy, silence and accessibility are component-level rules.

---

## Imported source: `GDR-046_html_prototype_before_full_backend_proposed.md`

# GDR-046 — HTML prototype before full backend

**Статус:** `proposed`

Validate the vertical slice with a coded prototype first.

---

## Imported source: `GDR-047_first_value_is_return_proposed.md`

# GDR-047 — First value is return

**Статус:** `proposed`

The first value moment is not finishing setup. It is leaving and returning to a preserved place.

---

## Imported source: `GDR-048_non_spatial_navigation_is_equal_proposed.md`

# GDR-048 — Non-spatial representation is equal

**Статус:** `proposed`

Every spatial Place has a structured, keyboard- and screen-reader-accessible representation with equal functional status.

---

## Imported source: `GDR-049_analytics_excludes_private_content_proposed.md`

# GDR-049 — Analytics excludes private content

**Статус:** `proposed`

Raw memories, rituals, emotional text and AI prompts are not collected in product analytics by default.

---

## Imported source: `GDR-050_deterministic_ai_before_live_ai_proposed.md`

# GDR-050 — Test interaction before model quality

**Статус:** `proposed`

The first coded prototype uses deterministic AI proposals before live-model integration so Preview, partial Apply and Undo can be validated independently.

---

## Imported source: `GDR-051_garden_is_inhabitable_not_simulated_proposed.md`

# GDR-051 — Garden is inhabitable, not simulated

**Статус:** `proposed`

The visual system creates a sense of place without a maintenance-heavy simulated world.

---

## Imported source: `GDR-052_world_context_and_system_surfaces_are_distinct_proposed.md`

# GDR-052 — World, context and system surfaces are distinct

**Статус:** `proposed`

The interface shows whether the person is inhabiting, editing or operating system controls.

---

## Imported source: `GDR-053_motion_supports_orientation_not_reward_proposed.md`

# GDR-053 — Motion supports orientation, not reward

**Статус:** `proposed`

Motion may show continuity but cannot celebrate compliance or create urgency.

---

## Imported source: `GDR-054_visual_accessibility_has_equal_status_proposed.md`

# GDR-054 — Visual accessibility has equal status

**Статус:** `proposed`

Structured non-spatial interaction, reduced motion and keyboard access are first-class modes.
