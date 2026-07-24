---
title: "Garden Source Registry"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# Garden Source Registry

---

## Imported source: `garden_evidence_card_template_v0_1.md`

# Garden Evidence Card Template

```yaml
source_id:
title:
authors:
year:
publication:
doi:
official_url:
access_date:
source_type:
research_domain:
related_research:
audit_status:
quality_code:
peer_reviewed:
license:
commercial_use:
conflict_of_interest:
funding:
```

## 1. Исследовательский вопрос источника

Что именно изучали или утверждали авторы?

## 2. Дизайн

- тип исследования;
- выборка;
- страна и контекст;
- длительность;
- сравнение/контроль;
- основные измерения;
- метод анализа.

## 3. Основные результаты

Только результаты, реально присутствующие в источнике.

## 4. Что источник поддерживает для Garden

Список узких утверждений с Claim ID.

## 5. Чего источник не поддерживает

Какие популярные или соблазнительные выводы из него делать нельзя.

## 6. Ограничения

- размер и состав выборки;
- causality;
- self-report;
- attrition;
- multiple outcomes;
- replication;
- cultural transfer;
- clinical/non-clinical transfer;
- publication bias.

## 7. Риски продуктового переноса

Что может пойти не так при превращении результата в функцию?

## 8. Альтернативные объяснения

Какие ещё причины могли породить наблюдаемый результат?

## 9. Противоречащие источники

Какие работы показывают другую картину?

## 10. Лицензия и использование

- можно ли цитировать;
- можно ли воспроизводить шкалу;
- можно ли переводить;
- требуется ли атрибуция;
- возможно ли коммерческое использование;
- требуется ли отдельное разрешение.

## 11. Решение

- `use_as_foundation`
- `use_with_caution`
- `market_signal_only`
- `needs_replication`
- `do_not_use`
- `watch`

## 12. Связи

- Research ID:
- Claim ID:
- GDR:
- Product hypothesis:
- Chronicle entry:

---

## Imported source: `garden_source_registry_v0_1.md`

# Garden Source Registry

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Статус:** действующий стартовый реестр; полный аудит продолжается  
**Контур:** `06_sources/source_registry.md`

---

## 1. Назначение

Garden Source Registry — единая точка учёта всех материалов, на которых строятся:

- исследования Garden Institute;
- Философия Garden;
- Голос Garden;
- продуктовые гипотезы;
- метрики и шкалы;
- анализ рынка и конкурентов;
- решения GDR;
- правила безопасности и приватности.

Реестр не является обычной библиографией. Он должен отвечать на пять вопросов:

1. Откуда взялось утверждение?
2. Что источник действительно позволяет утверждать?
3. Чего он не доказывает?
4. Насколько надёжен источник для данного вывода?
5. Можно ли использовать материал в коммерческом продукте?

---

## 2. Базовые правила

1. Страница продукта не считается доказательством его эффективности.
2. Одна статья не становится продуктовым принципом автоматически.
3. Теория объясняет понятия, но не доказывает конкретную механику.
4. Корреляция не доказывает причинность.
5. Средний групповой эффект не определяет, что полезно конкретному человеку.
6. Валидная шкала не обязательно полезна, если показать её результат пользователю.
7. Само измерение способно изменить внимание и поведение.
8. Клинические выводы нельзя автоматически переносить на общий wellbeing-продукт.
9. Preprint используется как ранний сигнал, а не как окончательное доказательство.
10. Лицензия и право на использование проверяются отдельно от научной ценности.
11. Отрицательные и неоднозначные результаты сохраняются.
12. Любой принцип Garden должен иметь traceability: источник → исследование → гипотеза → решение.

---

## 3. Статусы аудита

| Статус | Значение |
|---|---|
| `identified` | источник найден, но не проверен |
| `metadata_verified` | проверены авторы, год, название, публикация и ссылка |
| `abstract_reviewed` | изучены аннотация и основные публичные сведения |
| `full_text_reviewed` | изучен полный текст |
| `evidence_card_complete` | заполнена полная карточка доказательств |
| `license_verified` | отдельно проверены условия использования |
| `superseded` | существует более новая или сильная версия |
| `rejected` | источник нельзя использовать для заявленного вывода |
| `watch` | источник или продукт нужно отслеживать во времени |

---

## 4. Оценка качества

Качество оценивается не «вообще», а относительно конкретного вывода.

| Код | Уровень | Типичные источники |
|---|---|---|
| A1 | высокая доказательная ценность | качественный систематический обзор, метаанализ, крупное продольное исследование |
| A2 | сильный первичный источник | рецензируемое исследование с подходящим дизайном |
| B1 | сильная теоретическая основа | признанная теория, философская работа, методологическая статья |
| B2 | полезное качественное/HCI-исследование | интервью, дневниковое исследование, прототипный тест |
| C1 | ранний научный сигнал | preprint, небольшое пилотное исследование |
| C2 | официальный институциональный источник | описание программы, шкалы, лицензии, методология |
| D1 | рыночный первичный источник | официальный сайт, privacy policy, pricing, App Store |
| D2 | пользовательское свидетельство | отзывы, интервью, сообщества |
| E | слабый или неподходящий источник | маркетинговый пересказ, непроверяемая вторичная публикация |

Код не является итогом автоматически. Например, официальный сайт продукта — хороший источник для цены, но слабый источник для эффективности.

---

# 5. Внутренние источники Garden

| ID | Источник | Роль | Статус |
|---|---|---|---|
| GDN-001 | `garden_knowledge_system_v1.md` | архитектура знания и жизненный цикл документов | full_text_reviewed |
| GDN-002 | `garden_project_map_research_market_v0_1.md` | исследовательская карта и Garden Observatory | full_text_reviewed |
| GDN-003 | `research_operating_model.md` | стандарт работы Garden Institute | full_text_reviewed |
| GDN-004 | `garden_philosophy_v0_1.md` | философское ядро; пока не доказательный источник | full_text_reviewed |
| GDN-005 | `garden_voice_v0_1.md` | черновик голосовой системы; требует исследований | full_text_reviewed |
| GDN-006 | `R-005_what_is_a_good_life_and_who_decides_v0_1.md` | первая синтетическая версия исследования | full_text_reviewed |
| GDN-007 | `OBS-001_flourishing_app_deep_dive_v0_1.md` | первый аудит внешней платформы | full_text_reviewed |
| GDN-008 | `garden_alpha_blueprint_v1.md` | exploratory draft, не утверждённый план | full_text_reviewed |
| GDN-009 | `research_01_why_people_change.md` | ранее созданное исследование; нужен source audit | identified |
| GDN-010 | `research_02_care_vs_control.md` | ранее созданное исследование; нужен source audit | identified |
| GDN-011 | `research_03_why_nature_calms_us.md` | ранее созданное исследование; нужен source audit | identified |
| GDN-012 | `R-004_language_of_inner_dialogue.md` | требует восстановления | identified |

**Правило:** внутренний документ Garden может синтезировать знания, но не заменяет внешний первичный источник.

---

# 6. Стартовый внешний реестр

## A. Human flourishing и хорошая жизнь

### SRC-WB-001

**Источник:** VanderWeele, T. J. (2017). *On the Promotion of Human Flourishing*. PNAS.  
**Тип:** peer-reviewed theoretical and empirical synthesis  
**Качество:** B1/A2 в зависимости от вывода  
**Статус:** abstract_reviewed  
**DOI:** `10.1073/pnas.1702996114`  
**Официальная ссылка:** `https://www.pnas.org/doi/10.1073/pnas.1702996114`  
**Поддерживает:**

- flourishing шире отдельных показателей счастья, здоровья или дохода;
- предложение многомерной модели;
- обоснование доменов и измерений.

**Не поддерживает:**

- обязательность этой модели для каждого продукта;
- полезность общего score пользователю;
- эффективность Flourishing App;
- универсальность любого конкретного UX.

**Связано с:** R-005, OBS-001.

---

### SRC-WB-002

**Источник:** Human Flourishing Program at Harvard — *Our Flourishing Measure*.  
**Тип:** официальный институциональный источник  
**Качество:** C2  
**Статус:** license_verified  
**Ссылка:** `https://hfh.fas.harvard.edu/measuring-flourishing`  
**Поддерживает:**

- официальную структуру Flourishing и Secure Flourish Measure;
- пять основных доменов и два вопроса материальной стабильности;
- информацию о переводах;
- условия лицензирования.

**Лицензия:**

- некоммерческое использование: CC BY-NC 4.0 с атрибуцией;
- коммерческое использование требует отдельного лицензирования.

**Не поддерживает:**

- автоматическую полезность шкалы для Garden;
- право смешивать её с другими Flourishing Scales;
- безопасность показа результата пользователю.

**Связано с:** R-005, OBS-001, R-011, R-012.

---

### SRC-WB-003

**Источник:** Human Flourishing Program — *Global Flourishing Study*.  
**Тип:** официальная программа крупного продольного исследования  
**Качество:** C2; отдельные публикации оцениваются самостоятельно  
**Статус:** abstract_reviewed  
**Ссылка:** `https://hfh.fas.harvard.edu/global-flourishing-study`  
**Поддерживает:**

- существование международной продольной программы;
- многомерный и кросс-культурный исследовательский подход;
- актуальную структуру измеряемых доменов.

**Не поддерживает:**

- выводы, которых нет в конкретной публикации;
- перенос средних международных результатов на отдельного пользователя.

**Связано с:** R-005, кросс-культурная программа.

---

### SRC-WB-004

**Источник:** Ryff, C. D., & Keyes, C. L. M. (1995). *The Structure of Psychological Well-Being Revisited*.  
**Тип:** peer-reviewed primary study  
**Качество:** A2  
**Статус:** abstract_reviewed  
**PubMed:** `https://pubmed.ncbi.nlm.nih.gov/7473027/`  
**Поддерживает:**

- шестимерную модель психологического благополучия;
- автономию, mastery среды, рост, отношения, цель и самопринятие;
- эмпирическую проверку структуры на взрослой выборке.

**Не поддерживает:**

- необходимость превращать шесть измерений в продуктовые сферы;
- одинаковую валидность всех коротких версий шкалы;
- оценку всей жизни одним баллом.

**Связано с:** R-005, R-011.

---

### SRC-WB-005

**Источник:** Ryff, C. D. (2013/2014). *Psychological Well-Being Revisited: Advances in Science and Practice*.  
**Тип:** peer-reviewed review  
**Качество:** B1  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC4241300/`  
**Поддерживает:**

- развитие эвдемонической модели;
- обзор исследований и ограничений;
- внимание к контексту и неравенству.

**Связано с:** R-005, R-015.

---

### SRC-WB-006

**Источник:** Keyes, C. L. M. (2002). *The Mental Health Continuum: From Languishing to Flourishing in Life*.  
**Тип:** peer-reviewed primary conceptual and empirical paper  
**Качество:** A2/B1  
**Статус:** abstract_reviewed  
**PubMed:** `https://pubmed.ncbi.nlm.nih.gov/12096700/`  
**Поддерживает:**

- различение психического заболевания и положительного психического здоровья;
- эмоциональные, психологические и социальные составляющие функционирования.

**Риск применения:**

- категории flourishing/languishing могут восприниматься пользователем как диагноз или идентичность.

**Связано с:** R-005, R-011, Garden Voice.

---

### SRC-WB-007

**Источник:** Seligman, M. E. P. (2018). *PERMA and the Building Blocks of Well-Being*.  
**Тип:** peer-reviewed theoretical clarification  
**Качество:** B1  
**Статус:** full_text_available / abstract_reviewed  
**DOI:** `10.1080/17439760.2018.1437466`  
**Ссылка:** `https://ppc.sas.upenn.edu/sites/default/files/permawellbeing.pdf`  
**Поддерживает:**

- PERMA как пять предлагаемых строительных блоков wellbeing;
- важность вопроса о том, как выбираются элементы благополучия.

**Не поддерживает:**

- полноту PERMA;
- необходимость её использования как универсального продуктового чек-листа.

**Связано с:** R-005.

---

### SRC-PHI-001

**Источник:** Robeyns, I. — *The Capability Approach*, Stanford Encyclopedia of Philosophy.  
**Тип:** академический философский обзор  
**Качество:** B1  
**Статус:** full_text_reviewed  
**Ссылка:** `https://plato.stanford.edu/entries/capability-approach/`  
**Поддерживает:**

- различение достижений и реальных возможностей;
- необходимость учитывать способность конвертировать ресурсы в действия;
- анти-патерналистский аргумент в пользу capabilities.

**Не поддерживает:**

- готовую продуктовую модель;
- конкретный список деревьев Garden;
- способ измерения возможностей в приложении.

**Связано с:** R-005, R-015, Философия Garden.

---

## B. Автономия, мотивация и изменение поведения

### SRC-MOT-001

**Источник:** Ryan, R. M., & Deci, E. L. (2000). *Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being*.  
**Тип:** peer-reviewed theoretical synthesis  
**Качество:** B1  
**Статус:** full_text_available / abstract_reviewed  
**DOI:** `10.1037/0003-066X.55.1.68`  
**Ссылка:** `https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf`  
**Поддерживает:**

- роль автономии, компетентности и связанности;
- различение автономной и контролируемой мотивации;
- влияние среды на мотивацию и wellbeing.

**Не поддерживает:**

- отсутствие любой структуры;
- утверждение, что любой свободный выбор полезен;
- конкретные формулировки Garden без тестирования.

**Связано с:** R-001, R-002, R-005, R-009.

---

### SRC-MOT-002

**Источник:** Deci, E. L., & Ryan, R. M. (2000). *The “What” and “Why” of Goal Pursuits*.  
**Тип:** peer-reviewed theory paper  
**Качество:** B1  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://selfdeterminationtheory.org/SDT/documents/2000_DeciRyan_PIWhatWhy.pdf`  
**Поддерживает:**

- различие между содержанием цели и качеством мотивации;
- важность базовых психологических потребностей.

**Связано с:** R-001, R-002.

---

### SRC-HAB-001

**Источник:** Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). *How Are Habits Formed: Modelling Habit Formation in the Real World*.  
**Тип:** peer-reviewed longitudinal primary study  
**Качество:** A2  
**Статус:** abstract_reviewed  
**DOI:** `10.1002/ejsp.674`  
**Официальная запись:** `https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/99783513802346`  
**Поддерживает:**

- постепенное развитие автоматичности при повторении поведения в стабильном контексте;
- существенную индивидуальную вариативность.

**Не поддерживает:**

- миф о фиксированных 21 или 66 днях как универсальном сроке;
- тождество привычки и осмысленного ритуала;
- обязательность ежедневного повторения для Garden.

**Связано с:** R-006.

---

### SRC-HAB-002

**Источник:** Gollwitzer, P. M., & Sheeran, P. (2006). *Implementation Intentions and Goal Achievement: A Meta-analysis of Effects and Processes*.  
**Тип:** meta-analysis  
**Качество:** A1  
**Статус:** abstract_reviewed  
**DOI:** `10.1016/S0065-2601(06)38002-1`  
**Запись:** `https://www.socmot.uni-konstanz.de/publications/implementation-intentions-and-goal-achievement-meta-analysis-effects-and-processes`  
**Поддерживает:**

- if–then planning как способ сокращать разрыв между намерением и действием;
- влияние конкретного будущего контекста на запуск поведения.

**Не поддерживает:**

- применение плана без согласия человека;
- способность плана решить структурные ограничения;
- необходимость превращать Garden в планировщик.

**Связано с:** R-001, R-006.

---

## C. Self-compassion, стыд и поддержка

### SRC-COMP-001

**Источник:** Ferrari, M. et al. (2019). *Self-Compassion Interventions and Psychosocial Outcomes: A Meta-Analysis of RCTs*.  
**Тип:** meta-analysis of randomized trials  
**Качество:** A1  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://self-compassion.org/wp-content/uploads/2019/08/Ferrari2019.pdf`  
**Поддерживает:**

- возможность улучшения self-compassion и ряда психосоциальных исходов;
- необходимость учитывать качество и неоднородность интервенций.

**Не поддерживает:**

- универсальную эффективность тёплого языка Garden;
- тождество self-compassion и снятия требований;
- применение клинических практик без адаптации.

**Связано с:** R-002, R-009.

---

### SRC-COMP-002

**Источник:** Wakelin, K. E. et al. (2022). *Effectiveness of Self-Compassion-Related Interventions for Reducing Self-Criticism*.  
**Тип:** systematic review and meta-analysis  
**Качество:** A1  
**Статус:** abstract_reviewed  
**PubMed:** `https://pubmed.ncbi.nlm.nih.gov/33749936/`  
**Поддерживает:**

- среднее снижение self-criticism в интервенциях;
- необходимость дальнейшего анализа качества исследований.

**Связано с:** R-002, Garden Voice.

---

### SRC-COMP-003

**Источник:** Sirois, F. M. et al. (2015). *Self-Compassion, Affect, and Health-Promoting Behaviors*.  
**Тип:** peer-reviewed empirical study  
**Качество:** A2  
**Статус:** abstract_reviewed  
**PubMed:** `https://pubmed.ncbi.nlm.nih.gov/25243717/`  
**Поддерживает:**

- связь self-compassion, адаптивных эмоций и health-promoting behavior.

**Не поддерживает:**

- причинный вывод для любого поведения;
- продуктовую формулу «мягкость всегда повышает действие».

**Связано с:** R-002.

---

## D. Язык и совместное изменение

### SRC-LANG-001

**Источник:** Bischof, G. et al. (2021). *Motivational Interviewing: An Evidence-Based Approach for Use in Medical Practice*.  
**Тип:** peer-reviewed practical review  
**Качество:** B1  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC8200683/`  
**Поддерживает:**

- работу с амбивалентностью;
- коллаборативную, неосуждающую позицию;
- извлечение собственной мотивации человека.

**Не поддерживает:**

- право Garden имитировать терапию;
- автоматическое применение MI-паттернов LLM без контроля качества.

**Связано с:** R-009, Garden Voice.

---

### SRC-LANG-002

**Источник:** Rubak, S. et al. (2005). *Motivational Interviewing: A Systematic Review and Meta-analysis*.  
**Тип:** systematic review and meta-analysis  
**Качество:** A1  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC1463134/`  
**Поддерживает:**

- эффективность MI в ряде медицинских поведенческих контекстов по сравнению с традиционным советованием.

**Ограничения:**

- неоднородность контекстов;
- отсутствие систематического поиска вреда в старых исследованиях;
- перенос на AI требует отдельного исследования.

**Связано с:** R-009, R-010.

---

## E. Рефлексия и journaling

### SRC-REF-001

**Источник:** Frattaroli, J. (2006). *Experimental Disclosure and Its Moderators: A Meta-analysis*.  
**Тип:** meta-analysis  
**Качество:** A1  
**Статус:** abstract_reviewed  
**DOI:** `10.1037/0033-2909.132.6.823`  
**PubMed:** `https://pubmed.ncbi.nlm.nih.gov/17073523/`  
**Поддерживает:**

- небольшой средний эффект письменного эмоционального раскрытия;
- важность модераторов и дизайна практики.

**Не поддерживает:**

- утверждение, что ежедневное ведение дневника полезно всем;
- безопасность неограниченной рефлексии;
- эффективность AI-интерпретации записей.

**Связано с:** R-007.

---

### SRC-REF-002

**Источник:** Gortner, E.-M. et al. (2006). *Benefits of Expressive Writing in Lowering Rumination and Depressive Symptoms*.  
**Тип:** peer-reviewed primary study  
**Качество:** A2  
**Статус:** abstract_reviewed  
**PubMed:** `https://pubmed.ncbi.nlm.nih.gov/16942980/`  
**Поддерживает:**

- возможную роль expressive writing в снижении руминации у определённой выборки и в определённом протоколе.

**Не поддерживает:**

- универсальность эффекта;
- любой формат свободного journaling;
- замену профессиональной помощи.

**Связано с:** R-007.

---

## F. Природа и восстановление

### SRC-NAT-001

**Источник:** Jimenez, M. P. et al. (2021). *Associations between Nature Exposure and Health: A Review of the Evidence*.  
**Тип:** peer-reviewed evidence review  
**Качество:** B1/A1 по отдельным выводам  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC8125471/`  
**Поддерживает:**

- широкий корпус ассоциаций между контактом с природой и различными исходами;
- несколько возможных механизмов, включая восстановление внимания.

**Не поддерживает:**

- эквивалентность цифровой и реальной природы;
- клинические обещания Garden;
- утверждение, что садовая метафора сама по себе восстанавливает.

**Связано с:** R-003, R-013.

---

### SRC-NAT-002

**Источник:** Pham, T. P. et al. (2024). *Human Attention Restoration, Flow, and Creativity*.  
**Тип:** peer-reviewed review  
**Качество:** B1  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC11050943/`  
**Поддерживает:**

- актуальный обзор Attention Restoration Theory и связанных исследований.

**Связано с:** R-003, R-013.

---

## G. Измерение и self-tracking

### SRC-MEAS-001

**Источник:** König, L. M. et al. (2024). *Reactivity to Digital In-the-Moment Measurement of Health Behaviour: Systematic Review and Meta-analysis*.  
**Тип:** systematic review and meta-analysis  
**Качество:** A1  
**Статус:** identified / требует полного аудита  
**Публичная запись:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC11659718/`  
**Поддерживает:**

- сам факт необходимости учитывать measurement reactivity;
- неодинаковое влияние цифрового измерения в разных дизайнах.

**Связано с:** R-011.

---

### SRC-MEAS-002

**Источник:** Chiauzzi, E. et al. (2015). *Patient-Centered Activity Monitoring in Self-Management*.  
**Тип:** peer-reviewed review  
**Качество:** B1  
**Статус:** abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC4391303/`  
**Поддерживает:**

- self-monitoring может влиять на самооценку и поведение;
- важность пользовательского контекста и интерпретации данных.

**Связано с:** R-011.

---

## H. AI, совместная интерпретация и wellbeing

### SRC-AI-001

**Источник:** Zhu, S. et al. (2026). *Designing KRIYA: An AI Companion for Wellbeing Self-Reflection*.  
**Тип:** preprint / HCI prototype study  
**Качество:** C1/B2  
**Статус:** abstract_reviewed  
**Ссылка:** `https://arxiv.org/abs/2601.14589`  
**Поддерживает:**

- ценность co-interpretive framing как исследовательскую гипотезу;
- важность transparency;
- различие supportive и pressuring reflection;
- результаты интервью с 18 студентами на прототипе и гипотетических данных.

**Не поддерживает:**

- клиническую эффективность;
- долгосрочную безопасность;
- перенос на широкую аудиторию;
- доказанную эффективность Garden.

**Связано с:** R-010, R-011, Garden Voice.

---

### SRC-AI-002

**Источник:** Nepal, S. et al. (2024). *MindScape Study: Integrating LLM and Behavioral Sensing for Personalized AI-Driven Journaling Experiences*.  
**Тип:** preprint / exploratory study  
**Качество:** C1  
**Статус:** abstract_reviewed  
**Ссылка:** `https://arxiv.org/abs/2409.09570`  
**Поддерживает:**

- ранние результаты контекстного AI journaling;
- потенциальную ценность персонализированных prompts;
- необходимость дальнейшей проверки.

**Риски:**

- маленькая студенческая выборка;
- чувствительный пассивный сбор данных;
- preprint;
- множественные исходы;
- нельзя считать доказательством долгосрочного эффекта.

**Связано с:** R-007, R-010, R-012.

---

### SRC-AI-003

**Источник:** Chiu, Y. Y. et al. (2024). *A Computational Framework for Behavioral Assessment of LLM Therapists*.  
**Тип:** preprint / computational evaluation  
**Качество:** C1  
**Статус:** abstract_reviewed  
**Ссылка:** `https://arxiv.org/abs/2401.00820`  
**Поддерживает:**

- необходимость систематической проверки поведения LLM;
- риск избыточного problem-solving advice;
- невозможность полагаться на ощущение «эмпатичного тона».

**Не поддерживает:**

- использование Garden как терапевта;
- полный safety benchmark для wellbeing-продукта.

**Связано с:** R-010, R-009.

---

## I. Приватность и чувствительные данные

### SRC-PRIV-001

**Источник:** Tangari, G. et al. (2021). *Mobile Health and Privacy: Cross-Sectional Study*. BMJ.  
**Тип:** empirical privacy audit  
**Качество:** A2  
**Статус:** abstract_reviewed  
**Ссылка:** `https://www.bmj.com/content/373/bmj.n1248`  
**Поддерживает:**

- наличие существенных проблем и несоответствий в практиках приватности mHealth apps.

**Не поддерживает:**

- вывод о конкретной архитектуре Garden;
- утверждение, что все приложения одинаково небезопасны.

**Связано с:** R-012.

---

### SRC-PRIV-002

**Источник:** Iwaya, L. H. et al. (2022). *On the Privacy of Mental Health Apps*.  
**Тип:** empirical multi-method privacy investigation  
**Качество:** A2  
**Статус:** full_text_available / abstract_reviewed  
**Ссылка:** `https://pmc.ncbi.nlm.nih.gov/articles/PMC9643945/`  
**Поддерживает:**

- риски permissions, cryptography, logging, third-party sharing и profiling;
- необходимость privacy-by-design.

**Связано с:** R-012.

---

### SRC-PRIV-003

**Источник:** Georgiou, C. et al. (2026). *What’s on Your Mind? Exploring Privacy of Mental Health Apps*.  
**Тип:** recent preprint / empirical technical audit  
**Качество:** C1  
**Статус:** abstract_reviewed / watch  
**Ссылка:** `https://arxiv.org/abs/2605.02016`  
**Поддерживает:**

- свежий рыночный сигнал о transparency gaps, tracker SDKs и third-party AI processing;
- необходимость конкретно раскрывать обработчиков данных.

**Ограничения:**

- preprint;
- выборка Android-приложений;
- результаты требуют peer review и воспроизводимости.

**Связано с:** R-012, Garden Observatory.

---

## J. Рынок и продукты

### SRC-MKT-001

**Источник:** Flourishing App — About.  
**Тип:** официальный рыночный первичный источник  
**Качество:** D1  
**Статус:** full_text_reviewed / watch  
**Ссылка:** `https://www.flourishing.app/about`  
**Поддерживает:**

- самопозиционирование платформы;
- описанную связь с Human Flourishing Program;
- заявленную образовательную роль;
- планы дополнительных форматов.

**Не поддерживает:**

- официальное партнёрство с Harvard;
- научную эффективность продукта;
- активную мобильную пользовательскую базу.

**Связано с:** OBS-001, R-016.

---

### SRC-MKT-002

**Источник:** Flourishing App — Flourishing Measure page.  
**Тип:** официальный продуктовый источник  
**Качество:** D1  
**Статус:** full_text_reviewed / watch  
**Ссылка:** `https://www.flourishing.app/measures/flourishing-measure`  
**Поддерживает:**

- содержание публичной страницы;
- набор отображаемых вопросов;
- используемое продуктовое описание.

**Найденная проблема:**

- смешение описания 8-item Flourishing Scale с 12-question Secure Flourish Measure.

**Не поддерживает:**

- валидность такой комбинации;
- лицензионную чистоту;
- научную эффективность приложения.

**Связано с:** OBS-001, R-011.

---

# 7. Источники, которые необходимо добавить в следующей версии

## Для R-006 — ритуал и привычка

- антропология и социология ритуала;
- ritualization и meaning;
- distinction ritual/routine/habit;
- embodied cognition;
- cultural variability of ritual.

## Для R-007 — рефлексия и руминация

- Trapnell & Campbell: reflection versus rumination;
- Watkins: constructive and unconstructive repetitive thought;
- systematic reviews digital journaling;
- narrative identity;
- contraindications and adverse effects.

## Для R-009 — голос взрослой субъектности

- Motivational Interviewing Treatment Integrity;
- psychological reactance;
- autonomy-supportive language;
- infantilization and patronizing language;
- cross-cultural pragmatics;
- uncertainty communication.

## Для R-010 — AI и интерпретация

- sycophancy;
- anthropomorphism;
- emotional reliance;
- AI companion dependency;
- calibrated uncertainty;
- memory and identity formation;
- human oversight.

## Для R-011 — измерение

- Goodhart’s law and metric fixation;
- quantified-self HCI;
- mood tracking;
- eating disorder and anxiety risks;
- missingness and feedback loops.

## Для R-012 — безопасность

- GDPR;
- EU AI Act;
- medical device boundary;
- mental health app governance;
- intimate privacy;
- local/on-device inference;
- deletion and portability.

---

# 8. Очередь полного аудита

Приоритет P0:

1. SRC-WB-001 — полный текст и карточка аргументов.
2. SRC-WB-002 — отдельная license card.
3. SRC-MOT-001 — извлечь принципы autonomy support без терапевтизации.
4. SRC-COMP-001 — проверить эффект, выборки, риск bias.
5. SRC-REF-001 — разобрать модераторы и adverse outcomes.
6. SRC-NAT-001 — отделить реальную, цифровую природу и метафору.
7. SRC-MEAS-001 — полный аудит measurement reactivity.
8. SRC-AI-001 — разобрать дизайн, выборку и pressure findings.
9. SRC-PRIV-002 — превратить выводы в safety requirements.
10. SRC-MKT-002 — сохранить evidence mismatch как Observatory incident.

---

# 9. Требование к каждому исследованию Garden

Каждое исследование должно завершаться таблицей:

| Claim ID | Утверждение Garden | Источники | Уровень уверенности | Ограничения | Продуктовый статус |
|---|---|---|---|---|---|
| CLM-001 | ... | SRC-... | low/medium/high | ... | hypothesis/principle/accepted |

Исследование не может использовать формулировку «наука показывает» без конкретного Claim ID.

---

# 10. Требование к продуктовым решениям

Перед GDR проверяется:

- есть ли минимум один источник за решение;
- есть ли источник или аргумент против решения;
- проверена ли применимость к нашей аудитории;
- отделена ли научная гипотеза от ценностного выбора;
- проверена ли лицензия;
- существует ли способ измерить вред;
- обновлён ли Chronicle;
- можно ли объяснить решение пользователю простым языком.

---

# 11. Текущие ограничения реестра

- Это стартовый, а не полный корпус.
- Для большинства работ проверены метаданные и аннотации, но не выполнен полный критический разбор.
- Старые исследования R-001–R-003 ещё не связаны с конкретными Source ID.
- R-004 требует восстановления.
- Философские книги Сена и Нуссбаум пока представлены через академический обзор, а не через отдельные карточки оригинальных работ.
- Не собраны исследования adverse effects.
- Не завершена юридическая карта ЕС и других рынков.
- Не проведён систематический поиск по базам с заранее зарегистрированным протоколом.

---

## Imported source: `source_registry_addendum_R001_R003_v0_1.md`

# Garden Source Registry — Addendum for R-001–R-003

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Назначение:** новые и уточнённые Source ID после аудита первых трёх исследований.

## SRC-MOT-003

**Michie, S., van Stralen, M. M., & West, R. (2011).**  
*The Behaviour Change Wheel: A New Method for Characterising and Designing Behaviour Change Interventions.*  
DOI: `10.1186/1748-5908-6-42`  
Тип: peer-reviewed framework development  
Качество: B1  
Статус: full_text_reviewed

Поддерживает COM-B и взаимодействие capability, opportunity, motivation и behavior.

Не поддерживает автоматическую диагностику барьера ИИ или эффективность интерфейса Garden.

## SRC-COMP-004

**Breines, J. G., & Chen, S. (2012).**  
*Self-Compassion Increases Self-Improvement Motivation.*  
DOI: `10.1177/0146167212445599`  
Тип: четыре лабораторных эксперимента  
Качество: A2 для краткосрочного экспериментального вывода  
Статус: full_text_reviewed

Поддерживает: краткое self-compassion framing может повышать отдельные показатели corrective motivation.

Не поддерживает: долгосрочную привычку, retention или эффект любого тёплого UX-текста.

## SRC-COMP-005

**Neff, K. D. (2003).**  
*The Development and Validation of a Scale to Measure Self-Compassion.*  
DOI: `10.1080/15298860309027`  
Тип: определение конструкта и разработка шкалы  
Качество: A2/B1  
Статус: full_text_reviewed

Поддерживает исходную модель компонентов self-compassion и психометрическую проверку.

Ограничения: self-report и последующие дебаты о факторной структуре. Шкала не является пользовательским диагнозом.

## SRC-COMP-006

**Vidal, J., et al. (2022/2023).**  
*Effect of Compassion-Focused Therapy on Self-Criticism and Self-Soothing: A Meta-Analysis.*  
Тип: meta-analysis  
Качество: A1 с неоднородностью интервенций  
Статус: abstract_reviewed

Поддерживает среднее снижение self-criticism и рост soothing-related outcomes.

Не поддерживает использование Garden как CFT или терапевтического продукта.

## SRC-EMO-001

**Tangney, J. P., Stuewig, J., & Mashek, D. J. (2007).**  
*Moral Emotions and Moral Behavior.*  
DOI: `10.1146/annurev.psych.56.091103.070145`  
Тип: peer-reviewed review  
Качество: B1  
Статус: abstract_reviewed

Поддерживает различение guilt и shame и их типичные связи с reparative и avoidant/defensive responses.

Не поддерживает диагностику эмоции пользователя по одной формулировке.

## SRC-NAT-003

**Bowler, D. E., Buyung-Ali, L. M., Knight, T. M., & Pullin, A. S. (2010).**  
*A Systematic Review of Evidence for the Added Benefits to Health of Exposure to Natural Environments.*  
DOI: `10.1186/1471-2458-10-456`  
Тип: systematic review  
Качество: A1 с неоднородной доказательной базой  
Статус: abstract_reviewed

Поддерживает возможные эмоциональные преимущества природной среды; данные по вниманию и физиологии менее последовательны.

Не поддерживает перенос эффекта на цифровой сад.

## SRC-NAT-004

**Ohly, H., et al. (2016).**  
*Attention Restoration Theory: A Systematic Review of the Attention Restoration Potential of Exposure to Natural Environments.*  
DOI: `10.1080/10937404.2016.1196155`  
Тип: systematic review and meta-analyses  
Качество: A1  
Статус: abstract_reviewed

Поддерживает частичную поддержку ART по отдельным cognitive tests.

Не поддерживает единый эффект на всё внимание.

## SRC-NAT-005

**Roberts, H., et al. (2019).**  
*The Effect of Short-Term Exposure to the Natural Environment on Depressive Mood: A Systematic Review and Meta-Analysis.*  
DOI: `10.1016/j.envres.2019.108606`  
Тип: systematic review and meta-analysis  
Качество: A1, при этом качество включённых доказательств низкое/очень низкое  
Статус: abstract_reviewed

Поддерживает небольшой pooled effect на depressive mood.

Ограничения: высокий риск bias и значительная неоднородность.

## SRC-NAT-006

**Stevenson, M. P., Schilhab, T., & Bentsen, P. (2018).**  
*Attention Restoration Theory II.*  
DOI: `10.1080/10937404.2018.1505571`  
Тип: systematic review  
Качество: A1  
Статус: abstract_reviewed

Поддерживает более последовательные сигналы для executive attention и working memory при неоднородности методов.

## SRC-NAT-007

**Ulrich, R. S., et al. (1991).**  
*Stress Recovery During Exposure to Natural and Urban Environments.*  
DOI: `10.1016/S0272-4944(05)80184-7`  
Тип: controlled laboratory experiment  
Качество: A2 / foundational  
Статус: abstract_reviewed

Поддерживает более быстрое восстановление после stressor при природных сценах по ряду показателей в конкретном эксперименте.

Не поддерживает универсальность или эффект интерактивного wellbeing-продукта.

## SRC-NAT-008

**Hubbard, G., et al. (2025).**  
*A Systematic Literature Review and Meta-Analysis of Virtual Reality Nature Effects on Higher Education Students’ Mental Health and Wellbeing.*  
DOI: `10.1111/aphw.70060`  
Тип: systematic review and meta-analysis  
Качество: A1 с узкой аудиторией  
Статус: abstract_reviewed

Поддерживает emerging positive effects VR nature в higher-education populations.

## SRC-NAT-009

**Chen, L., et al. (2025).**  
*How Exposure to Virtual Natural Environments Reduces Anxiety and Related Outcomes: Systematic Review and Meta-Analysis.*  
Тип: systematic review and meta-analysis  
Качество: A1 с высокой неоднородностью  
Статус: abstract_reviewed

Поддерживает средние эффекты по отдельным self-reported outcomes у healthy adults.

Ограничения: высокая гетерогенность и небольшое число исследований для некоторых сравнений.

## Обновления существующих карточек

### SRC-HAB-001

Добавить:

- выборка 96 человек;
- стабильный контекст являлся частью дизайна;
- один пропуск возможности в исходной модели не разрушал процесс;
- среднее 66 дней нельзя использовать как обещание.

### SRC-COMP-001

Добавить:

- 27 randomized trials;
- неоднородность интервенций и контрольных групп;
- эффект тренинга нельзя переносить на одну AI-реплику.

### SRC-NAT-001

Использовать как широкий narrative review. Для конкретных утверждений предпочитать SRC-NAT-003–009.

---

## Imported source: `source_registry_addendum_R004_v0_1.md`

# Garden Source Registry — Addendum for R-004

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Контур:** `06_sources/source_registry_addenda/R-004.md`

---

## SRC-LANG-003

**Alderson-Day, B., & Fernyhough, C. (2015).**  
*Inner Speech: Development, Cognitive Functions, Phenomenology, and Neurobiology.* Psychological Bulletin, 141(5), 931–965.  
DOI: `10.1037/bul0000021`  
Тип: comprehensive peer-reviewed review  
Качество: B1  
Статус: full_text_available / abstract_reviewed

Поддерживает многофункциональность и вариативность inner speech.

Не поддерживает универсальность вербального внутреннего диалога и продуктовую технику Garden.

---

## SRC-LANG-004

**Kross, E., et al. (2014).**  
*Self-Talk as a Regulatory Mechanism: How You Do It Matters.* Journal of Personality and Social Psychology, 106(2), 304–324.  
DOI: `10.1037/a0035173`  
Тип: series of experiments  
Качество: A2  
Статус: abstract_reviewed

Поддерживает regulatory benefits non-first-person self-talk в конкретных экспериментальных задачах.

Не поддерживает универсальное назначение третьего лица.

---

## SRC-LANG-005

**Moser, J. S., et al. (2017).**  
*Third-Person Self-Talk Facilitates Emotion Regulation Without Engaging Cognitive Control.* Scientific Reports, 7, 4519.  
DOI: `10.1038/s41598-017-04047-3`  
Тип: experimental neurocognitive study  
Качество: A2  
Статус: full_text_available / abstract_reviewed

Поддерживает снижение ряда neural markers emotional reactivity при third-person self-talk в условиях исследования.

Ограничения: лабораторные стимулы и ограниченная переносимость на повседневный продукт.

---

## SRC-LANG-006

**Murdoch, E. M., Chapman, M. T., Crane, M. F., & Gucciardi, D. F. (2023).**  
*The Effectiveness of Self-Distanced Versus Self-Immersed Reflections Among Adults: Systematic Review and Meta-Analysis of Experimental Studies.* Stress and Health, 39(2), 255–271.  
DOI: `10.1002/smi.3199`  
Тип: systematic review and meta-analysis  
Качество: A1  
Статус: abstract_reviewed

Поддерживает средние преимущества distanced reflection по отдельным outcomes.

Ограничения: неоднородные манипуляции и задачи; нельзя считать универсальной техникой.

---

## SRC-LANG-007

**Schertz, K. E., et al. (2025).**  
*The Frequency, Form, and Function of Self-Talk in Everyday Life.* Scientific Reports, 15, 38883.  
DOI: `10.1038/s41598-025-22647-2`  
Тип: ecological momentary assessment study  
Качество: A2 / recent  
Статус: abstract_reviewed / watch

Поддерживает различия immersed/distanced self-talk в повседневности и контекстно зависимые функции.

Ограничения: один новый observational study; требует репликации и культурного расширения.

---

## SRC-LANG-008

**Wood, J. V., Perunovic, W. Q. E., & Lee, J. W. (2009).**  
*Positive Self-Statements: Power for Some, Peril for Others.* Psychological Science, 20(7), 860–866.  
DOI: `10.1111/j.1467-9280.2009.02370.x`  
Тип: experimental studies  
Качество: A2  
Статус: abstract_reviewed

Поддерживает возможность обратного эффекта чрезмерно позитивных self-statements у людей с низкой self-esteem.

Не поддерживает вывод, что позитивная речь всегда вредна.

---

## SRC-LANG-009

**Steindl, C., Jonas, E., Sittenthaler, S., Traut-Mattausch, E., & Greenberg, J. (2015).**  
*Understanding Psychological Reactance: New Developments and Findings.* Zeitschrift für Psychologie, 223(4), 205–214.  
DOI: `10.1027/2151-2604/a000222`  
Тип: peer-reviewed review  
Качество: B1  
Статус: full_text_available / abstract_reviewed

Поддерживает reactance как реакцию на воспринимаемую угрозу свободе.

Не поддерживает прогноз реакции конкретного пользователя на отдельную фразу.

---

## SRC-LANG-010

**Smit, E. S., Zeidler, C., Resnicow, K., & de Vries, H. (2019).**  
*Identifying the Most Autonomy-Supportive Message Frame in Digital Health Communication: A 2×2 Between-Subjects Experiment.* JMIR, 21(10), e14074.  
DOI: `10.2196/14074`  
Тип: digital health experiment, N=526  
Качество: A2  
Статус: abstract_reviewed

Поддерживает provision of choice как более выраженный signal perceived autonomy support в этом контексте.

Не поддерживает универсальную superiority конкретного wording.

---

## SRC-LANG-011

**Altendorf, M. B., van Weert, J. C. M., Hoving, C., & Smit, E. S. (2019).**  
*Should or Could? Testing Autonomy-Supportive Language and Choice in Online Alcohol Reduction Communication.* Digital Health, 5.  
DOI: `10.1177/2055207619832767`  
Тип: online experiment, N=521  
Качество: A2  
Статус: abstract_reviewed

В исследовании не обнаружены ожидавшиеся значимые основные эффекты autonomy-supportive wording и выбора на ключевые outcomes.

Урок: простая замена modal verbs не гарантирует autonomy support.

---

## SRC-LANG-012

**Shaw, C. A., & Gordon, J. K. (2021).**  
*Understanding Elderspeak: An Evolutionary Concept Analysis.* Innovation in Aging, 5(3).  
DOI: `10.1093/geroni/igab023`  
Тип: concept analysis/review  
Качество: B1  
Статус: full_text_available / abstract_reviewed

Поддерживает elderspeak как patronizing overaccommodation, часто основанную на добрых намерениях и стереотипах.

Перенос на Garden — cautionary, а не прямое доказательство для общей взрослой аудитории.

---

## SRC-LANG-013

**Healy, M., et al. (2022).**  
*How to Reduce Stigma and Bias in Clinical Communication.*  
Тип: peer-reviewed guidance/review  
Качество: B1  
Статус: abstract_reviewed

Поддерживает отказ от pejorative labels, инклюзивный и person-respecting language.

Не превращает person-first language в универсальное правило: предпочтения групп различаются.

---

## SRC-LANG-014

**Miller, W. R., & Rose, G. S. (2009).**  
*Toward a Theory of Motivational Interviewing.* American Psychologist, 64(6), 527–537.  
DOI: `10.1037/a0016830`  
Тип: theoretical model grounded in MI research  
Качество: B1  
Статус: full_text_available / abstract_reviewed

Поддерживает relational и technical components MI.

Не поддерживает заявление chatbot «использует MI» без fidelity assessment.

---

## SRC-LANG-015

**Liu, X., et al. (2025).**  
*Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey.* KDD 2025.  
arXiv: `2503.15850`  
Тип: technical survey  
Качество: B1/C1 для быстро развивающегося поля  
Статус: abstract_reviewed

Поддерживает проблему некалиброванной уверенности и разнообразие методов UQ.

Не даёт готового пользовательского языка uncertainty для Garden.

---

## SRC-LANG-016

**Sun, X., et al. (2026).**  
*Seeing the Reasoning: How LLM Rationales Influence User Trust and Decision-Making in Factual Verification Tasks.* CHI EA 2026.  
arXiv: `2603.07306`  
Тип: controlled HCI experiment, N=68  
Качество: A2/C1 recent  
Статус: full_text_reviewed

Поддерживает влияние certainty framing и rationale correctness на trust, confidence и advice adoption.

Ограничения: factual verification, небольшая выборка, не wellbeing-контекст.

---

## Реестр рисков R-004

| Risk ID | Риск | Источники |
|---|---|---|
| LR-001 | ложная позитивность активирует контраргументы | SRC-LANG-008 |
| LR-002 | директивность вызывает reactance | SRC-LANG-009 |
| LR-003 | язык выбора маскирует отсутствие выбора | SRC-LANG-010, 011 |
| LR-004 | заботливый тон становится инфантилизацией | SRC-LANG-012 |
| LR-005 | уверенный AI language создаёт overtrust | SRC-LANG-015, 016 |
| LR-006 | внешняя фраза присваивается как внутренняя истина | требует исследования Garden |

---

## Imported source: `source_registry_addendum_R006_v0_1.md`

# Garden Source Registry — Addendum for R-006

**Версия:** 0.1  
**Дата:** 15 июля 2026

## SRC-RIT-001 — Psychology of Habit

Wood, W., & Rünger, D. (2016). *Psychology of Habit.* Annual Review of Psychology, 67, 289–314.  
DOI: `10.1146/annurev-psych-122414-033417`  
Тип: authoritative review  
Качество: B1  
Статус: official full-text summary reviewed

Поддерживает context-cue activation, automaticity и различие привычки и deliberate goal pursuit.

Не поддерживает определение ритуала и необходимость автоматизировать любую практику.

## SRC-RIT-002 — Habit terminology

Gardner, B. (2015). *A Review and Analysis of the Use of “Habit” in Understanding, Predicting and Influencing Health-Related Behaviour.*  
PMCID: `PMC4566897`  
Тип: terminology review  
Качество: B1  
Статус: full text available / reviewed

Поддерживает необходимость различать habit process и просто частое поведение.

## SRC-RIT-003 — Habits and behavior change

Verplanken, B. (2022). *Attitudes, Habits, and Behavior Change.* Annual Review of Psychology.  
DOI: `10.1146/annurev-psych-020821-011744`  
Тип: authoritative review  
Качество: B1  
Статус: official summary reviewed

Поддерживает habit как memory-based propensity автоматически отвечать на cue.

## SRC-RIT-004 — Psychology of rituals

Hobson, N. M., et al. (2018). *The Psychology of Rituals: An Integrative Review and Process-Based Framework.*  
PMID: `29130838`  
Тип: integrative review  
Качество: B1  
Статус: abstract reviewed

Поддерживает три исследовательские функции ritual: emotion, performance goal states и social connection.

Ограничение: корпус обзора требует integrity re-check после последующих ретракций в области.

## SRC-RIT-005 — Ritual explained

Legare, C. H., & Nielsen, M. (2020). *Ritual Explained: Interdisciplinary Answers to Tinbergen’s Four Questions.*  
PMCID: `PMC7423255`  
Тип: interdisciplinary review  
Качество: B1  
Статус: full text reviewed

Поддерживает ритуалы как социально обусловленные, конвенциональные, часто формальные, ригидные и повторяющиеся последовательности.

## SRC-RIT-006 — Ingredients of rituals

Boyer, P., & Liénard, P. (2020). *Ingredients of “Rituals” and Their Cognitive Underpinnings.*  
PMCID: `PMC7423267`  
Тип: theoretical review  
Качество: B1  
Статус: full text reviewed

Поддерживает критическую позицию: ritual объединяет разнородное поведение по family resemblance.

## SRC-RIT-007 — Anxiety and ritualization

Lang, M., et al. (2015). *Effects of Anxiety on Spontaneous Ritualized Behavior.* Current Biology, 25(14), 1892–1897.  
PMID: `26096971`  
DOI: `10.1016/j.cub.2015.05.049`  
Тип: experiment  
Качество: A2  
Статус: abstract reviewed

Поддерживает: induced anxiety увеличивала redundancy, repetitiveness и rigidity движений.

Не поддерживает: ритуал снижает тревогу или полезен.

## SRC-RIT-008 — Perceived efficacy

Xygalatas, D., et al. (2021). *Ritualization Increases the Perceived Efficacy of Instrumental Actions.* Cognition, 215, 104823.  
PMID: `34198073`  
DOI: `10.1016/j.cognition.2021.104823`  
Тип: perception study  
Качество: A2  
Статус: abstract reviewed

Поддерживает влияние ritualized form на perceived efficacy.

Риск для Garden: форма может создавать завышенное ожидание результата.

## SRC-RIT-009 — Synchrony and cooperation

Wiltermuth, S. S., & Heath, C. (2009). *Synchrony and Cooperation.* Psychological Science, 20(1), 1–5.  
PMID: `19152536`  
Тип: experiments  
Качество: A2  
Статус: abstract reviewed

Поддерживает рост cooperation после synchronous action в исследованных условиях.

Не поддерживает универсальное улучшение отношений.

## SRC-RIT-010 — Secular rituals and bonding

Charles, S. J., et al. (2021). *United on Sunday: The Effects of Secular Rituals on Social Bonding and Affect.* PLOS ONE, 16(1), e0242546.  
PMID: `33503054`; PMCID: `PMC7840012`  
Тип: field pre-post study  
Качество: A2/B2  
Статус: abstract reviewed

Ограничения: self-selection, отсутствие рандомизации, коллективный контекст.

## SRC-RIT-011 — Ritual and cooperation

Fischer, R., et al. (2013). *How Do Rituals Affect Cooperation?*  
PMID: `23666518`  
Тип: experimental field study  
Качество: A2  
Статус: abstract reviewed

Поддерживает контекстно зависимую связь synchrony/sacredness и prosocial outcomes.

## SRC-RIT-012 — Compulsive behavior

Luigjes, J., et al. (2019). *Defining Compulsive Behavior.*  
PMCID: `PMC6499743`  
Тип: interdisciplinary review  
Качество: B1  
Статус: full text available / abstract reviewed

Поддерживает признаки compulsivity: repetitive acts, feeling of “has to”, несоответствие общим целям.

Не является диагностическим инструментом Garden.

## SRC-RIT-013 — RETRACTED

Brooks, A. W., et al. (2016). *Don’t Stop Believing: Rituals Improve Performance by Decreasing Anxiety.*  
**Статус:** retracted in 2024  
Retraction DOI: `10.1016/j.obhdp.2024.104377`

Правило:

- не использовать выводы;
- помечать обзоры, опиравшиеся на статью;
- сохранить как integrity incident.

## SRC-RIT-014 — Family routines and rituals

Fiese, B. H., et al. *A Review of 50 Years of Research on Naturally Occurring Family Routines and Rituals.*  
Тип: family research review  
Качество: B1  
Статус: identified; нужен полный аудит

Поддерживает различение observable routines и symbolic family rituals.

## SRC-RIT-015 — INTEGRITY WATCH

Vohs, K. D., Wang, Y., Gino, F., & Norton, M. I. (2013). *Rituals Enhance Consumption.*  
PMID: `23863754`  
Статус: не отозвана на дату аудита; отдельная проверка integrity и replication обязательна.

## SRC-RIT-016 — INTEGRITY WATCH

Norton, M. I., & Gino, F. (2014). *Rituals Alleviate Grieving for Loved Ones, Lovers, and Lotteries.*  
PMID: `23398180`  
Статус: не отозвана на дату аудита; не делать продуктовый вывод без отдельной проверки.

---

## Новые поля Source Registry

```yaml
retraction_checked:
correction_checked:
expression_of_concern_checked:
data_or_materials_available:
independent_replication:
integrity_watch:
```

---

## Imported source: `source_registry_addendum_R007_v0_1.md`

# Garden Source Registry — Addendum for R-007

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Контур:** `06_sources/source_registry_addenda/R-007.md`

---

## SRC-REF-001

**Frattaroli, J. (2006).**  
*Experimental Disclosure and Its Moderators: A Meta-Analysis.* Psychological Bulletin, 132(6), 823–865.  
PMID: `17073523`  
DOI: `10.1037/0033-2909.132.6.823`  
Тип: meta-analysis  
Качество: A1  
Статус: abstract reviewed

Поддерживает небольшой средний эффект experimental disclosure и важность модераторов дизайна.

Не поддерживает ежедневный свободный journaling или AI interpretation.

---

## SRC-REF-002

**Gortner, E.-M., Rude, S. S., & Pennebaker, J. W. (2006).**  
*Benefits of Expressive Writing in Lowering Rumination and Depressive Symptoms.* Behavior Therapy, 37(3), 292–303.  
PMID: `16942980`  
DOI: `10.1016/j.beth.2006.01.004`  
Тип: randomized controlled study  
Качество: A2  
Статус: abstract reviewed

Поддерживает пользу expressive writing для определённой depression-vulnerable student subgroup, особенно при высокой suppression.

Не поддерживает универсальный эффект.

---

## SRC-REF-003

**Trapnell, P. D., & Campbell, J. D. (1999).**  
*Private Self-Consciousness and the Five-Factor Model of Personality: Distinguishing Rumination from Reflection.* Journal of Personality and Social Psychology, 76(2), 284–304.  
PMID: `10074710`  
Тип: scale development and correlational studies  
Качество: A2/B1  
Статус: abstract reviewed

Поддерживает различение curiosity-driven reflection и threat/loss-driven rumination.

Не поддерживает диагностику процесса пользователя в реальном времени.

---

## SRC-REF-004

**Harrington, R., & Loffredo, D. A. (2011).**  
*Insight, Rumination, and Self-Reflection as Predictors of Well-Being.* Journal of Psychology, 145(1), 39–57.  
PMID: `21290929`  
Тип: correlational study  
Качество: A2  
Статус: abstract reviewed

Поддерживает различающиеся связи insight, rumination и reflection с subjective wellbeing.

Корреляционный дизайн не устанавливает причинность.

---

## SRC-REF-005

**Nolen-Hoeksema, S., Wisco, B. E., & Lyubomirsky, S. (2008).**  
*Rethinking Rumination.* Perspectives on Psychological Science, 3(5), 400–424.  
PMID: `26158958`  
Тип: authoritative review  
Качество: B1  
Статус: abstract reviewed

Поддерживает связи rumination с более длительным distress, negative thinking, impaired problem solving, reduced instrumental behavior и social difficulties.

---

## SRC-REF-006

**Nolen-Hoeksema, S. (2000).**  
*The Role of Rumination in Depressive Disorders and Mixed Anxiety/Depressive Symptoms.* Journal of Abnormal Psychology.  
PMID: `11016119`  
Тип: longitudinal evidence synthesis  
Качество: A2/B1  
Статус: abstract reviewed

Поддерживает prospective association rumination с depressive symptoms и disorders.

Не поддерживает использование Garden как clinical screening tool.

---

## SRC-REF-007

**Watkins, E. R. (2008).**  
*Constructive and Unconstructive Repetitive Thought.* Psychological Bulletin, 134(2), 163–206.  
PMID: `18298268`  
Тип: integrative review  
Качество: B1  
Статус: full-text source identified / abstract reviewed

Поддерживает процессуальную модель: repeated thought может быть constructive или unconstructive в зависимости от processing mode, context и function.

---

## SRC-REF-008

**Watkins, E. R. (2008).**  
*Processing Mode Causally Influences Emotional Reactivity: Distinct Effects of Abstract Versus Concrete Construal on Emotional Response.* Emotion, 8(3), 364–378.  
PMID: `18540752`  
Тип: experiments  
Качество: A2  
Статус: abstract reviewed

Поддерживает различающиеся эффекты abstract и concrete processing в экспериментальных условиях.

Не поддерживает запрет абстрактного мышления.

---

## SRC-REF-009

**Watkins, E., & Teasdale, J. D. (2004).**  
*Adaptive and Maladaptive Self-Focus in Depression.* Journal of Affective Disorders, 82(1), 1–8.  
PMID: `15465571`  
Тип: experimental clinical study  
Качество: A2  
Статус: abstract reviewed

Поддерживает различие analytic/evaluative и experiential/concrete self-focus.

---

## SRC-REF-010

**Raes, F., Watkins, E. R., Williams, J. M. G., & Hermans, D. (2008).**  
*Non-Ruminative Processing Reduces Overgeneral Autobiographical Memory Retrieval in Students.* Behavior Research and Therapy, 46(6), 748–756.  
PMID: `18456242`  
DOI: `10.1016/j.brat.2008.03.003`  
Тип: experiment  
Качество: A2  
Статус: abstract reviewed

Поддерживает влияние concrete process-focused induction на autobiographical memory specificity в student sample.

---

## SRC-REF-011

**Vassilopoulos, S. P., & Watkins, E. R. (2009).**  
*Adaptive and Maladaptive Self-Focus: A Pilot Extension Study.* Behavior Therapy, 40(2), 181–189.  
PMID: `19433149`  
Тип: randomized pilot experiment  
Качество: A2 with small analogue sample  
Статус: abstract reviewed

Поддерживает снижение global negative self-judgments при experiential self-focus у high-FNE participants.

---

## SRC-REF-012

**Guo, L. (2023).**  
*The Delayed, Durable Effect of Expressive Writing on Depression, Anxiety and Stress: A Meta-Analytic Review of Studies With Long-Term Follow-Ups.* British Journal of Clinical Psychology, 62(1), 272–297.  
PMID: `36536513`  
DOI: `10.1111/bjc.12408`  
Тип: meta-analysis of 31 experiments, N=4012  
Качество: A1  
Статус: abstract reviewed

Поддерживает небольшой delayed average effect в healthy/subclinical samples.

Не поддерживает неограниченный journaling или clinical claims.

---

## SRC-REF-013

**Schueller, S. M., Neary, M., Lai, J., & Epstein, D. A. (2021).**  
*Understanding People’s Use of and Perspectives on Mood-Tracking Apps: Interview Study.* JMIR Mental Health, 8(8), e29368.  
PMID: `34383678`  
DOI: `10.2196/29368`  
Тип: qualitative interview study  
Качество: B2  
Статус: full text available / abstract reviewed

Поддерживает разнообразие целей, преимуществ, ограничений и интерпретаций mood tracking.

---

## SRC-REF-014

**Dubad, M., et al. (2021).**  
*The Clinical Impacts of Mobile Mood-Monitoring in Young People With Mental Health Problems: Systematic Review.*  
PMCID: `PMC8363129`  
Тип: systematic review  
Качество: A1 with limited evidence base  
Статус: abstract reviewed

Поддерживает возможную пользу, но подчёркивает ограниченность доказательств.

---

## SRC-REF-015

**Beltzer, M. L., et al. (2023).**  
*Mental Health Self-Tracking Preferences of Young Adults With Mood and Anxiety Disorders.*  
PMCID: `PMC10589825`  
Тип: qualitative/preference study  
Качество: B2  
Статус: abstract reviewed

Поддерживает необходимость customizable, actionable и privacy-sensitive self-tracking.

Не доказывает эффективность tracking.

---

## SRC-REF-016

**Wright, L. A., et al. (2025).**  
*The User Experience of Ambulatory Assessment and Mood Monitoring in Depression: A Systematic Review and Meta-Synthesis.* npj Digital Medicine, 8, 737.  
Тип: systematic review and qualitative meta-synthesis  
Качество: A1/B2  
Статус: abstract reviewed

Поддерживает mixed user experience: awareness и clinical communication alongside burden, negative focus и usability concerns.

---

## SRC-REF-017

**Wrzus, C., & Neubauer, A. B. (2023).**  
*Ecological Momentary Assessment: A Meta-Analysis on Designs, Samples, and Compliance Across Research Fields.* Assessment, 30, 825–846.  
PMID: `35016567`; PMCID: `PMC9999286`  
Тип: meta-analysis, 496 samples, N=677,536  
Качество: A1  
Статус: full text available / abstract reviewed

Поддерживает dependence of compliance/dropout on protocol design and sample characteristics.

Не является прямым исследованием psychological harm.

---

## SRC-REF-018

**König, L. M., et al. (2022).**  
*A Systematic Review and Meta-Analysis of Studies of Reactivity to Digital In-the-Moment Measurement of Health Behaviour.*  
Тип: systematic review and meta-analysis  
Качество: A1  
Статус: identified; full audit required

Поддерживает необходимость учитывать measurement reactivity; эффекты зависят от поведения и дизайна.

---

## SRC-REF-019

**Stone, A. A., et al. (2026).**  
*Intensive, Repeated Self-Report Measures: Should We Be Concerned About Their Effects on Data Quality?* JMIR mHealth and uHealth.  
Тип: methodological viewpoint with empirical illustrations  
Качество: B1/C1 recent  
Статус: full text available / watch

Поддерживает необходимость учитывать habituation, reactivity, fatigue и changes in response processes.

Не доказывает конкретный harmful effect Garden.

---

## Обновление правил Source Registry

Для исследований repeated assessment добавляются поля:

```yaml
prompt_frequency:
assessment_duration:
participant_burden:
reactivity_measured:
adverse_experience_reported:
missingness_handling:
dropout_rate:
clinical_population:
```

---

## Imported source: `source_registry_addendum_R008_v0_1.md`

# Garden Source Registry — Addendum for R-008

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Контур:** `06_sources/source_registry_addenda/R-008.md`

---

## SRC-ACT-001

**Ntoumanis, N., et al. (2021).**  
*A Meta-Analysis of Self-Determination Theory-Informed Intervention Studies in the Health Domain.* Health Psychology Review.  
PMID: `31983293`  
Тип: meta-analysis  
Качество: A1  
Статус: abstract reviewed

Поддерживает:

- positive changes in need support and autonomous motivation associated with positive health behavior change;
- importance of intervention content and delivery.

Не поддерживает:

- любой «свободный выбор» как полезный;
- конкретную механику Garden;
- отсутствие структуры.

---

## SRC-ACT-002

**Mohr, D. C., Cuijpers, P., & Lehman, K. A. (2011).**  
*Supportive Accountability: A Model for Providing Human Support to Enhance Adherence to eHealth Interventions.* Journal of Medical Internet Research, 13(1), e30.  
PMID: `21393123`  
DOI: `10.2196/jmir.1602`  
Тип: theoretical model grounded in adjacent literature  
Качество: B1  
Статус: full article metadata and abstract reviewed

Поддерживает:

- accountability to a trustworthy, benevolent and expert coach;
- clear process-oriented expectations;
- participant involvement in defining expectations;
- human support as an adherence mechanism.

Ограничение:

- основная целевая переменная — adherence к intervention;
- модель человеческой поддержки нельзя автоматически переносить на AI;
- это theoretical model, а не универсальный доказанный протокол.

---

## SRC-ACT-003

**Kwok, G., Cheung, S. P. Y., Duffecy, J., & Devine, K. A. (2025).**  
*Application of the Supportive Accountability Model in Digital Health Interventions: Scoping Review.* Journal of Medical Internet Research, 27, e72639.  
PMID: `41004801`  
DOI: `10.2196/72639`  
Тип: scoping review  
Качество: B1  
Статус: abstract/conclusion reviewed

Поддерживает:

- SAM применяется неравномерно;
- многие DHI используют отдельные элементы, а не модель целиком;
- human support рассматривается как adjunct to engagement;
- остаются методологические пробелы.

Не доказывает эффективность AI accountability.

---

## SRC-ACT-004

**Bryan, G., Karlan, D., & Nelson, S. (2010).**  
*Commitment Devices.* Annual Review of Economics, 2, 671–698.  
DOI: `10.1146/annurev.economics.102308.124324`  
Тип: evidence review  
Качество: B1  
Статус: abstract reviewed

Поддерживает различение hard и soft commitments и контекстную эффективность commitment devices.

Не поддерживает обязательные штрафы или universal demand.

---

## SRC-ACT-005

**Herzog, S. M., & Hertwig, R. (2025).**  
*Boosting: Empowering Citizens with Behavioral Science.* Annual Review of Psychology, 76, 851–881.  
DOI: `10.1146/annurev-psych-020924-124753`  
Тип: authoritative open-access review  
Качество: B1  
Статус: full text reviewed

Поддерживает:

- boosting как развитие competences, agency, self-control and informed decision-making;
- критику ставки только на benevolent choice architects;
- self-nudging как один из empowerment approaches.

Не поддерживает, что boosts всегда эффективнее nudges.

Лицензия: CC BY 4.0.

---

## SRC-ACT-006

**Banerjee, S., & John, P. (2024; online 2021).**  
*Nudge Plus: Incorporating Reflection into Behavioral Public Policy.* Behavioural Public Policy, 8(1), 69–84.  
DOI: `10.1017/bpp.2021.6`  
Тип: conceptual and theoretical synthesis  
Качество: B1  
Статус: full text reviewed

Поддерживает:

- adding active reflection and transparency to nudge design;
- agency as a normative objective.

Ограничения:

- efficacy remains to be empirically validated;
- reflective design itself can subtly steer toward sponsor-preferred outcomes.

Лицензия: CC BY 4.0.

---

## SRC-ACT-007

**Reijula, S., & Hertwig, R. (2022; online 2020).**  
*Self-Nudging and the Citizen Choice Architect.* Behavioural Public Policy, 6(1), 119–149.  
DOI: `10.1017/bpp.2020.5`  
Тип: conceptual framework  
Качество: B1  
Статус: abstract reviewed

Поддерживает:

- individuals can design their own proximate choice environments;
- self-nudging as empowerment and self-governance;
- education about choice architecture.

Не поддерживает универсальную эффективность или равный доступ к environmental change.

---

## SRC-ACT-008

**Duckworth, A. L., Gendler, T. S., & Gross, J. J. (2016).**  
*Situational Strategies for Self-Control.* Perspectives on Psychological Science, 11(1), 35–55.  
PMID: `26817725`  
Тип: theoretical review  
Качество: B1  
Статус: abstract reviewed

Поддерживает:

- antecedent situational strategies can reduce reliance on in-the-moment effort;
- changing exposure and environment may prevent stronger impulses.

Не поддерживает individualizing structural problems.

---

## SRC-ACT-009

**Coupe, N., et al. (2019).**  
*The Effect of Commitment-Making on Weight Loss and Behaviour Change in Adults With Obesity/Overweight: A Systematic Review and Meta-Analysis.*  
PMCID: `PMC6591991`  
Тип: systematic review and meta-analysis, three trials, N=409  
Качество: A1 with small evidence base  
Статус: abstract reviewed

Поддерживает modest short-term weight-loss effect in a narrow context.

Не поддерживает general commitment mechanics for Garden.

---

## SRC-ACT-010

**Fanaroff, A. C., et al. (2023/2024).**  
*Feasibility and Outcomes From Using a Commitment Device for Time-Restricted Eating.*  
PMCID: `PMC11010633`  
Тип: randomized controlled trial  
Качество: A2  
Статус: abstract reviewed

Поддерживает a null result: soft commitment did not improve adherence versus attention control in the studied intervention.

Урок: commitment device is not automatically effective.

---

## SRC-ACT-011

**van der Swaluw, K., et al. (2018).**  
*Commitment Lotteries Promote Physical Activity Among Overweight Adults.*  
PMCID: `PMC6361262`; follow-up PMCID: `PMC6061083`  
Тип: cluster randomized trial  
Качество: A2  
Статус: abstract reviewed

Поддерживает positive effects in a specific gym-attendance lottery design.

Ограничения: external incentive, specific population and context.

---

## SRC-ACT-012

**Derksen, L., et al. (2024/2025).**  
*Healthcare Appointments as Commitment Devices.*  
PMCID: `PMC12687577`  
Тип: randomized field experiment  
Качество: A2  
Статус: abstract reviewed

Поддерживает that appointments and hard commitment devices can affect HIV testing behavior in a specific Malawi context.

Не переносится на general wellbeing or Garden penalties.

---

## SRC-ACT-013

**Loughnane, C., Laiti, J., O’Donovan, R., & Dunne, P. J. (2025).**  
*Systematic Review Exploring Human, AI, and Hybrid Health Coaching in Digital Health Interventions.* Frontiers in Digital Health, 7, 1536416.  
DOI: `10.3389/fdgth.2025.1536416`  
Тип: systematic review, 35 studies  
Качество: A1 with narrative synthesis and heterogeneity  
Статус: abstract reviewed

Поддерживает:

- human, AI and hybrid modalities have demonstrated feasibility and acceptability;
- some positive engagement and lifestyle outcomes;
- protocols and engagement measures vary;
- hybrid models require further refinement.

Не поддерживает equivalence of AI and human coaching or long-term safety.

---

## SRC-ACT-014

**Altendorf, M. B., et al. (2019).**  
*Should or Could? Testing Autonomy-Supportive Language and Choice in Online Alcohol Reduction Communication.* Digital Health.  
PMCID: `PMC6393822`  
Тип: online experiment, N=521  
Качество: A2  
Статус: abstract reviewed

Did not find expected significant main effects of wording or choice on key outcomes.

Урок: modal verbs do not guarantee autonomy support.

---

## SRC-ACT-015

**Smit, E. S., et al. (2019).**  
*Identifying the Most Autonomy-Supportive Message Frame in Digital Health Communication.* Journal of Medical Internet Research, 21(10), e14074.  
PMCID: `PMC6914245`  
Тип: 2×2 online experiment, N=526  
Качество: A2  
Статус: abstract reviewed

Provision of choice was a stronger signal of perceived autonomy support than wording alone in this setting.

Не поддерживает a universal copy formula.

---

## SRC-ACT-016

**Promberger, M., & Marteau, T. M. (2013).**  
*When Do Financial Incentives Reduce Intrinsic Motivation? Comparing Behaviors Studied in Psychological and Economic Literatures.*  
PMID: `24001245`  
Тип: systematic conceptual review  
Качество: B1  
Статус: abstract reviewed

Поддерживает context-dependent undermining effects, particularly for simple tasks with existing intrinsic motivation.

Не поддерживает claim that incentives always undermine motivation.

---

## Дополнительные правила для commitment и accountability

Добавить поля:

```yaml
commitment_owner:
commitment_type:
reversibility:
penalty:
resource_inequality_risk:
changed_preference_handling:
human_or_ai_support:
adherence_target:
human_outcome_target:
withdrawal_process:
```

---

## Imported source: `source_registry_addendum_R009_v0_1.md`

# Garden Source Registry — Addendum for R-009

**Версия:** 0.1  
**Дата:** 15 июля 2026

## SRC-CULT-001

Chirkov, Ryan, Kim & Kaplan (2003). *Differentiating Autonomy From Individualism and Independence.*  
DOI: `10.1037/0022-3514.84.1.97`  
Тип: cross-cultural empirical study  
Качество: A2/B1  
Статус: full text reviewed

Поддерживает различение autonomy, independence и individualism; связь relative autonomy и wellbeing в выборках США, России, Турции и Южной Кореи.

Не поддерживает единый универсальный стиль коммуникации.

## SRC-CULT-002

Chen et al. (2015). *Basic Psychological Need Satisfaction, Need Frustration, and Need Strength Across Four Cultures.*  
DOI: `10.1007/s11031-014-9450-1`  
Тип: cross-cultural empirical study  
Качество: A2  
Статус: full-text proof reviewed

Поддерживает связи satisfaction/frustration автономии, компетентности и связанности с wellbeing/ill-being в выборках Бельгии, Китая, США и Перу.

Не поддерживает одинаковое культурное выражение потребностей.

## SRC-CULT-003

Spencer-Oatey (2022). *Politeness and Rapport Management.*  
DOI: `10.1017/9781108884303.020`  
Тип: authoritative review chapter  
Качество: B1  
Статус: official summary reviewed

Поддерживает контекстный и оценочный характер politeness и rapport.

## SRC-CULT-004

House & Kádár (2021). *Cross-Cultural Pragmatics.*  
Тип: academic framework  
Качество: B1  
Статус: official chapter summaries reviewed

Не является таблицей «правильных национальных тонов».

## SRC-CULT-005

Park & Kim (2008). *Asian and European American Cultural Values and Communication Styles.*  
PMID: `18230000`  
Тип: correlational study  
Качество: A2  
Статус: abstract reviewed

Поддерживает связь между лично поддерживаемыми cultural values и communication styles.

Не позволяет предсказывать человека по этничности.

## SRC-CULT-006

Gueta et al. (2023). *Cultural Accommodation of Internet-Based Interventions.*  
PMCID: `PMC10321598`  
Тип: pilot and framework  
Качество: B2/B1  
Статус: abstract reviewed

Поддерживает cultural accommodation beyond literal translation и участие целевой аудитории.

## SRC-GEN-001

Fiske (2012). *Warmth and Competence: Stereotype Content Issues.*  
PMCID: `PMC3801417`  
Тип: evidence review  
Качество: B1  
Статус: full text available/reviewed

Поддерживает warmth и competence как значимые измерения социального восприятия.

## SRC-GEN-002

Briggs et al. (2023). *Competence-Questioning Communication and Gender.*  
PMCID: `PMC9838290`  
Тип: multi-study empirical paper  
Качество: A2  
Статус: abstract reviewed

Поддерживает гендерно различающийся опыт competence-questioning communication в изученных контекстах.

Не поддерживает gender-based personalization.

## SRC-GEN-003

Park et al. (2016). *Women Are Warmer but No Less Assertive Than Men.*  
PMCID: `PMC4881750`  
Тип: large observational language study  
Качество: A2  
Статус: abstract reviewed

Поддерживает сложность и расхождение между стереотипами и наблюдаемым языком.

## SRC-DIGN-001

Shaw & Gordon (2021). *Understanding Elderspeak.*  
DOI: `10.1093/geroni/igab023`  
Тип: concept analysis  
Качество: B1  
Статус: full text available/reviewed

Поддерживает elderspeak как patronizing overaccommodation и риск снижения perceived respect.

## SRC-DIGN-002

Shaw et al. (2025). *The Iowa Coding Scheme for Elderspeak.*  
PMCID: `PMC12065398`  
Тип: coding scheme development  
Качество: A2/B1  
Статус: abstract reviewed

Операционализирует infantilizing language и дисбаланс care–respect–control.

## SRC-ND-001

Howard & Sedgewick (2021). *Anything but the Phone! Communication Mode Preferences in the Autism Community.*  
PMID: `34169750`  
Тип: survey  
Качество: A2/B2  
Статус: abstract reviewed

Поддерживает context-dependent communication preferences.

## SRC-ND-002

Nicolaidis et al. (2015). *Respect the Way I Need to Communicate With You.*  
PMCID: `PMC4841263`  
Тип: qualitative study  
Качество: B2  
Статус: full text available/reviewed

Поддерживает необходимость спрашивать и уважать коммуникационные потребности.

## SRC-ND-003

Bottini et al. (2024). *A Systematic Review of Recent Language Use in Autism Research.*  
PMCID: `PMC11319857`  
Тип: systematic review  
Качество: A1/B1  
Статус: abstract reviewed

Поддерживает разнообразие language preferences и отсутствие одного обязательного identity-first/person-first стандарта.

## SRC-ND-004

Cummins et al. (2020). *Autistic Adults’ Views of Their Communication Skills and Needs.*  
PMID: `32618026`  
Тип: qualitative interviews  
Качество: B2  
Статус: abstract reviewed

Поддерживает participant-defined needs и разные preferred modes.

## SRC-AI-LANG-001

Basoah et al. (2025). *Not Like Us, Hunty.*  
arXiv: `2505.05660`  
Тип: user studies with 498 AAE and 487 Queer slang speakers  
Качество: A2/C1  
Статус: full text reviewed

Поддерживает: sociolect mirroring влияет на trust, preference, social presence и reliance неодинаково и не гарантирует улучшения.

## SRC-AI-LANG-002

Borah, Augenstein & Mihalcea (2026). *Whose Norms?*  
arXiv: `2606.07877`  
Тип: benchmark and five-country human study  
Качество: A2/C1  
Статус: overview reviewed

Поддерживает внутри-культурный плюрализм и слабую передачу моделями распределения несогласия.

## SRC-AI-LANG-003

Yazan et al. (2026). *Personalized to Persuade.*  
arXiv: `2605.31275`  
Тип: experiment, N=380  
Качество: A2/C1  
Статус: full text reviewed

Поддерживает сложное влияние contextualization и warmth на trust, persuasion и reliance.

## SRC-AI-LANG-004

Chita-Tegmark et al. (2026). *Responsible Personalisation.*  
arXiv: `2607.06344`  
Тип: conceptual review  
Качество: B1/C1  
Статус: overview reviewed

Поддерживает риски потери автономии, усиления bias и privacy harms.

## SRC-AI-LANG-005

Huang et al. (2026). *Emotional Support with Conversational AI.*  
arXiv: `2603.22618`  
Тип: conceptual/review framework  
Качество: B1/C1  
Статус: abstract reviewed

Поддерживает tensions вокруг relatedness, competence, autonomy и overdependence.

## SRC-AI-LANG-006

Sun & Wang (2026). *Be Friendly, Not Friends: How LLM Sycophancy Shapes User Trust.*  
arXiv: `2502.10844`  
Тип: 2×2 experiment, N=224  
Качество: A2/C1  
Статус: full text reviewed

Поддерживает сложное взаимодействие complimentary demeanor и stance adaptation на authenticity и trust.

## Новые поля Source Registry

```yaml
country_or_region:
language:
within_culture_variation_considered:
translation_method:
cultural_adaptation:
identity_inference_used:
explicit_preferences_collected:
sociolect_or_dialect:
appropriation_risk:
gender_stereotype_risk:
accessibility_population:
```

---

## Imported source: `source_registry_addendum_R010_v0_1.md`

# Garden Source Registry — Addendum for R-010

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Контур:** `06_sources/source_registry_addenda/R-010.md`

---

## SRC-AI-INT-001 — KRIYA

**Gupta, S., et al. (2026).**  
*Designing KRIYA: An AI Companion for Wellbeing Self-Reflection.*  
arXiv: `2601.14589`  
Тип: HCI prototype + semi-structured interviews  
Выборка: 18 college students, hypothetical data  
Качество: B2/C1  
Статус: full text reviewed

Поддерживает:

- co-interpretation as a design direction;
- reflection can feel supportive or pressuring depending on framing;
- transparency, uncertainty and corrigibility as trust factors;
- AI as complement, not replacement.

Не поддерживает long-term benefit, clinical safety or broad generalization.

---

## SRC-AI-INT-002 — Personal advice RCT

**Luettgau, L., et al. (2026, v3).**  
*People Readily Follow Personal Advice from AI but It Does Not Improve Their Well-Being.*  
arXiv: `2511.15352v3`  
Тип: longitudinal randomized controlled trial  
Выборка: representative UK sample, `N = 6,474`  
Качество: A2/C1 preprint  
Статус: full text reviewed

Поддерживает:

- up to 79% self-reported advice following;
- over 60% following even for higher-stakes recommendations;
- substantial real-world behavioral influence;
- no sustained 2–3 week wellbeing benefit over control conversation.

Ограничения:

- self-reported following;
- short follow-up;
- UK context;
- consumer general-purpose chatbots;
- preprint.

Лицензия: CC BY-NC-ND 4.0.

---

## SRC-AI-INT-003 — Social Sycophancy

**Cheng, M., et al. (2025).**  
*Social Sycophancy: A Broader Understanding of LLM Sycophancy.*  
arXiv: `2505.13995`  
Тип: taxonomy, datasets and benchmark evaluation  
Качество: A2/C1  
Статус: full overview reviewed

Поддерживает:

- sycophancy beyond factual agreement;
- emotional validation, moral endorsement, indirect action and accepting framing as face-preserving behaviors;
- high social-sycophancy rates across evaluated models.

Не устанавливает longitudinal psychological harm.

---

## SRC-AI-INT-004 — Generative Confidants

**Volpato, R., Stumpf, S., & DeBruine, L. (2026).**  
*Generative Confidants: How Do People Experience Trust in Emotional Support from Generative AI?*  
arXiv: `2601.16656`; SSRN DOI: `10.2139/ssrn.6265318`  
Тип: qualitative diaries + transcripts + interviews  
Выборка: 24 frequent users  
Качество: B2/C1  
Статус: abstract and detailed metadata reviewed

Поддерживает:

- familiarity through personalization as a trust factor;
- user control and mental models as trust factors;
- positive/persuasive language can obscure machine nature.

Ограничения: small self-selected qualitative sample.

---

## SRC-AI-INT-005 — Emotional Support as interaction

**Huang, O. Y., Stodolska, M., & Sultana, S. (2026).**  
*Emotional Support with Conversational AI: Talking to Machines About Life.*  
arXiv: `2603.22618`  
Тип: qualitative analysis of Reddit discussions  
Качество: B2/C1  
Статус: full text reviewed  
Лицензия: CC BY 4.0

Поддерживает:

- emotional support is co-constructed;
- persistent availability, anonymity and low interpersonal burden are important affordances;
- tensions support/dependency, validation/delusion and accessibility/harm;
- AI may operate alongside or replace traditional support structures.

Не оценивает clinical accuracy or causal effects.

---

## SRC-AI-INT-006 — Replika emotional dependence

**Laestadius, L., Bishop, A., Gonzalez, M., Illenčík, D., & Campos-Castillo, C.**  
*Too Human and Not Human Enough: A Grounded Theory Analysis of Mental Health Harms from Emotional Dependence on the Social Chatbot Replika.*  
New Media & Society.  
DOI: `10.1177/14614448221142007`  
Тип: grounded theory of public Reddit posts  
Corpus: 582 mental-health-relevant posts, 2017–2021  
Качество: B2  
Статус: full text reviewed

Поддерживает:

- described cases of emotional dependence and role-taking;
- users attributing needs/emotions to chatbot;
- harms during ongoing or disrupted use;
- benefits and harms can arise from the same relational affordances.

Не поддерживает prevalence estimates or universal harm.

---

## SRC-AI-INT-007 — AI companion psychosocial impacts

**Yuan, Y., et al. (2025/2026).**  
*Mental Health Impacts of AI Companions: Triangulating Social Media Quasi-Experiments, User Perspectives, and Relational Theory.*  
arXiv: `2509.22505`  
Тип: quasi-experimental longitudinal Reddit analysis + 15 interviews  
Качество: A2/B2/C1  
Статус: abstract and overview reviewed

Поддерживает mixed effects, relationship-stage dependence, emotional validation/social rehearsal alongside overreliance and withdrawal risks.

Causal confidence remains limited by observational platform data.

---

## SRC-AI-INT-008 — PersistBench

**Pulipaka, S., et al. (2026).**  
*PersistBench: When Should Long-Term Memories Be Forgotten by LLMs?*  
arXiv: `2602.01146`  
Тип: benchmark across 18 frontier and open-source models  
Качество: A2/C1  
Статус: abstract reviewed

Поддерживает:

- cross-domain leakage;
- memory-induced sycophancy;
- median failure rates reported as 53% and 97% respectively in benchmark tests.

Не оценивает напрямую Garden architecture or real-user harm.

Лицензия: CC BY 4.0.

---

## SRC-AI-INT-009 — Cognitive–affective gap

**2026 human-grounded evaluation study.**  
*Assessing the Quality of Mental Health Support in LLM Responses through Multi-Attribute Human Evaluation.*  
arXiv: `2601.18630`  
Тип: evaluation of nine LLMs on 500 counseling conversations by two psychiatric-trained experts  
Качество: A2/C1  
Статус: full overview reviewed

Поддерживает:

- inconsistency between cognitive attributes such as safety/interpretation and affective resonance such as empathy/helpfulness;
- a structured and safe response may still be emotionally misattuned.

Не устанавливает clinical efficacy.

---

## SRC-AI-INT-010 — Incidental emotional dependence

**Shi, Y., Fang, C. M., Maez, P., & Goldenberg, A. (2026).**  
*Stumbling Into AI Emotional Dependence: How Routine AI Interactions Reshape Human Connection.*  
arXiv: `2606.04150`  
Тип: conceptual synthesis of emerging empirical evidence  
Качество: B1/C1  
Статус: abstract reviewed

Поддерживает гипотезу, что emotional support может возникать incidentally в general-purpose AI interactions и изменять будущие support preferences.

Количественные утверждения требуют отдельного аудита underlying studies.

---

## SRC-AI-INT-011 — Mental health LLM systematic reviews

Umbrella IDs:

- Guo et al. (2024), *Large Language Models for Mental Health Applications*;
- Hua et al. (2025), evolution of AI mental-health chatbots;
- Bucher et al. (2025), systematic review of LLM-based mental-health chatbots;
- Yang et al. (2026), application boundaries of LLMs in mental health.

Использовать только для broad evidence mapping. Конкретные efficacy/safety claims требуют карточек первичных исследований.

---

## SRC-AI-INT-012 — Identity negotiation

**Ma, R., et al. (2026).**  
*Negotiating Digital Identities with AI Companions.*  
arXiv: `2601.12181`  
Тип: LLM-assisted thematic analysis of 22,374 Character.AI subreddit discussions  
Качество: B2/C1  
Статус: abstract reviewed

Поддерживает identity co-construction как релевантный процесс взаимодействия.

Ограничения: platform-specific public discourse, LLM-assisted analysis, no causal claims.

---

## SRC-AI-INT-013 — Behavioral evaluation of LLM therapists

**Chiu, Y. Y., et al. (2024).**  
*A Computational Framework for Behavioral Assessment of LLM Therapists.*  
arXiv: `2401.00820`  
Тип: computational behavioral evaluation  
Качество: C1  
Статус: abstract reviewed

Поддерживает необходимость behavioral evaluation и риск избыточного problem-solving advice.

Не разрешает использовать Garden как therapist.

---

## Новые поля Source Registry

```yaml
interpretation_target:
epistemic_level:
user_confirmed:
alternative_explanations:
disconfirming_evidence:
memory_eligible:
memory_expiry:
domain_scope:
persuasive_personalization:
relational_role:
dependency_risk:
human_bridge:
correction_supported:
```

---

## Imported source: `source_registry_addendum_R011_v0_1.md`

# Garden Source Registry — Addendum for R-011

**Версия:** 0.1  
**Дата:** 15 июля 2026  
**Контур:** `06_sources/source_registry_addenda/R-011.md`

---

## SRC-MEAS-001 — Measurement reactivity in EMA

**Maher, J. P., et al. (2024/2026 publication record).**  
*Measurement Reactivity in Ecological Momentary Assessment Studies of Movement-Related Behaviors.*  
PMID: `41726043`  
Тип: intensive longitudinal empirical study  
Качество: A2  
Статус: abstract/full metadata reviewed

Поддерживает:

- repeated assessment can coincide with early changes in measured behavior and motivational antecedents;
- researchers must distinguish true change from assessment artifact;
- reactivity may differ over protocol days.

Не поддерживает universal or uniformly harmful reactivity.

---

## SRC-MEAS-002 — EMA compliance and dropout

**Wrzus, C., & Neubauer, A. B. (2023).**  
*Ecological Momentary Assessment: A Meta-Analysis on Designs, Samples, and Compliance Across Research Fields.* Assessment, 30, 825–846.  
PMID: `35016567`; PMCID: `PMC9999286`  
Тип: meta-analysis, 496 samples, `N = 677,536`  
Качество: A1  
Статус: full text available / abstract reviewed

Поддерживает dependence of compliance and dropout on protocol and sample characteristics.

Не является прямым доказательством psychological harm.

---

## SRC-MEAS-003 — Stage-Based Model

**Li, I., Dey, A. K., & Forlizzi, J. (2010).**  
*A Stage-Based Model of Personal Informatics Systems.* CHI 2010.  
DOI: `10.1145/1753326.1753409`  
Тип: foundational HCI model  
Качество: B1  
Статус: abstract reviewed

Поддерживает five stages: preparation, collection, integration, reflection and action.

Не доказывает that passage through stages is linear or successful.

---

## SRC-MEAS-004 — Lived Informatics

**Epstein, D. A., Ping, A., Fogarty, J., & Munson, S. A. (2015).**  
*A Lived Informatics Model of Personal Informatics.* UbiComp 2015.  
DOI: `10.1145/2750858.2804250`  
Тип: empirical HCI model  
Качество: B1/B2  
Статус: abstract reviewed

Поддерживает non-linear everyday tracking, including lapses, tool switching, abandonment and resumed tracking.

---

## SRC-MEAS-005 — Personal Informatics, insight and behavior change

**Kersten-van Dijk, E. T., Westerink, J. H. D. M., Beute, F., & IJsselsteijn, W. A. (2017).**  
*Personal Informatics, Self-Insight, and Behavior Change: A Critical Review of Current Literature.* Human–Computer Interaction.  
DOI: `10.1080/07370024.2016.1276456`  
Тип: critical literature review  
Качество: B1  
Статус: abstract reviewed

Поддерживает critical examination of the assumed chain tracking → insight → behavior change.

---

## SRC-MEAS-006 — Unintended consequences of Personal Informatics

**Luo, Y., et al. (2025).**  
*Reflecting Upon the Unintended Consequences of Personal Informatics Technology.* CHI 2025.  
DOI: `10.1145/3715336.3735746`  
Тип: HCI review/framework  
Качество: B1/C1 recent  
Статус: abstract reviewed

Поддерживает the need to study unintended cognitive, emotional, behavioral and social consequences of self-tracking.

---

## SRC-MEAS-007 — Response shift theory

**Vanier, A., et al. (2021).**  
*Response Shift in Patient-Reported Outcomes: Definition, Theory, and a Revised Model.* Quality of Life Research.  
PMCID: `PMC8602159`  
Тип: theory and methodological synthesis  
Качество: B1  
Статус: full text available / abstract reviewed

Поддерживает response shift as change in the meaning of self-evaluation and a special case of longitudinal measurement non-invariance.

---

## SRC-MEAS-008 — Response shift systematic review

**Sawatzky, R., et al. (2024).**  
*Response Shift Results of Quantitative Research Using Patient-Reported Outcome Measures: A Systematic Review.* Quality of Life Research.  
Тип: systematic review  
Качество: A1  
Статус: abstract reviewed

Поддерживает that response-shift effects are detected across populations and methods, with variable prevalence and magnitude.

---

## SRC-MEAS-009 — COSMIN content validity

**Terwee, C. B., et al. (2018) and current COSMIN framework.**  
*COSMIN Methodology for Evaluating the Content Validity of Patient-Reported Outcome Measures.*  
PMCID: `PMC5891557`  
Тип: consensus-based methodology  
Качество: B1  
Статус: framework and official COSMIN site reviewed

Поддерживает:

- content validity as a core measurement property;
- relevance, comprehensiveness and comprehensibility;
- selection of an instrument based on construct, population and context.

---

## SRC-MEAS-010 — FDA Patient-Reported Outcome guidance

**U.S. Food and Drug Administration.**  
*Patient-Reported Outcome Measures: Use in Medical Product Development to Support Labeling Claims.*  
Тип: regulatory guidance  
Качество: institutional primary source  
Статус: official guidance page reviewed

Поддерживает treating a PRO instrument as questionnaire plus documentation, context of use, recall period, scoring and evidence.

Не applies directly to a general wellbeing consumer app, but provides a strong measurement discipline reference.

---

## SRC-MEAS-011 — Intensive repeated self-report

**Stone, A. A., et al. (2026).**  
*Intensive, Repeated Self-Report Measures: Should We Be Concerned About Their Effects on Data Quality?* JMIR mHealth and uHealth.  
Тип: methodological viewpoint with empirical illustrations  
Качество: B1/C1 recent  
Статус: full-text metadata reviewed

Supports considering habituation, reactivity, fatigue and change in response process.

---

## SRC-MEAS-012 — Passive sensing systematic review

**Shen, S. Y., et al. (2025).**  
*Passive Sensing for Mental Health Monitoring Using Machine Learning: Systematic Review.*  
PMCID: `PMC12395114`  
Тип: systematic review of 42 peer-reviewed studies  
Качество: A1  
Статус: abstract reviewed

Supports rapid growth alongside heterogeneity, small samples and validation/generalization limitations.

---

## SRC-MEAS-013 — Digital phenotyping standardization

**Alam, N. B., et al. (2025).**  
*Challenges and Standardisation Strategies for Sensor-Based Digital Phenotyping.* Communications Medicine.  
Тип: methodological review  
Качество: B1  
Статус: abstract reviewed

Supports lack of standardization, device/context dependencies, validation and reproducibility challenges.

---

## SRC-MEAS-014 — Goodhart/Campbell governance signal

**Mattson, C., et al. (2021).**  
*When a Measure Becomes a Target, It Ceases to Be a Good Measure.*  
PMCID: `PMC7901608`  
Тип: applied measurement commentary  
Качество: B1  
Статус: abstract reviewed

Supports dynamic corruption and distortion when measures become targets in evaluation systems.

Use as governance principle, not an empirical law with one universal effect size.

---

## SRC-MEAS-015 — Wellbeing measures scoping review

**Zhang, W., et al. (2024).**  
*A Scoping Review of Well-Being Measures.*  
PMCID: `PMC11515516`  
Тип: scoping review  
Качество: B1  
Статус: abstract reviewed

Supports plurality of wellbeing conceptualizations and instruments rather than one neutral universal score.

---

## SRC-MEAS-016 — Flexible Minimalist Self-Tracking

**Li, H., et al. (2024).**  
*Flexible Minimalist Self-Tracking to Support Individual Needs.* IMWUT.  
DOI: `10.1145/3660339`  
Тип: HCI design and evaluation research  
Качество: A2/B2  
Статус: abstract reviewed

Supports flexibility and minimalism as promising directions for reducing tracking burden while supporting personal questions.

Does not establish the optimal Garden design.

---

## SRC-MEAS-017 — Personal Informatics in everyday life

**Rapp, A., & Cena, F. (2016).**  
*Personal Informatics for Everyday Life: How Users Without Prior Self-Tracking Experience Engage With Personal Data.*  
Тип: diary study, 14 participants  
Качество: B2  
Статус: abstract reviewed

Supports that some novice users found collection burdensome and insufficiently rewarding.

---

## SRC-MEAS-018 — Personal Informatics concerns

**Ayobi, A., et al. (2016).**  
*Reflections on 5 Years of Personal Informatics: Rising Concerns and Emerging Directions.*  
Тип: HCI synthesis/workshop paper  
Качество: B1/C2  
Статус: identified

Use for field mapping; specific claims require primary sources.

---

## Новые поля Source Registry

```yaml
construct:
unit_of_analysis:
individual_or_group_use:
recall_period:
measurement_frequency:
content_validity:
reliability:
measurement_error:
responsiveness:
measurement_invariance:
response_shift_considered:
reactivity_measured:
participant_burden:
missing_data_assumption:
derived_score:
target_use:
passive_or_active:
feedback_shown:
```

---

## Imported source: `source_registry_addendum_R012_v0_1.md`

# Garden Source Registry — Addendum for R-012

**Версия:** 0.1  
**Дата:** 15 июля 2026

## SRC-PRIV-001 — GDPR

**Regulation (EU) 2016/679.**  
Тип: binding EU regulation  
Качество: C2 / primary legal source  
Статус: current text reviewed

Поддерживает principles, special-category protection, data-subject rights, security, privacy by design/default, DPIA and breach duties.

Требует country/use-case legal interpretation; не является product checklist by itself.

## SRC-PRIV-002 — EDPB data-protection basics

**European Data Protection Board — Data protection basics / lawful processing / sensitive data.**  
Тип: official regulator guidance  
Качество: C2  
Статус: web guidance reviewed

Поддерживает additional protection for health, sexuality, beliefs and other special-category data.

## SRC-PRIV-003 — Data Protection by Design and Default

**EDPB Guidelines 4/2019 on Article 25 GDPR.**  
Тип: official guideline  
Качество: C2  
Статус: official page and guidance reviewed

Поддерживает privacy by design/default, minimization and protected defaults.

## SRC-PRIV-004 — Data-subject rights

**EDPB SME Guide — Respect individuals’ rights.**  
Тип: official web guidance  
Качество: C2  
Статус: reviewed

Поддерживает access, correction, erasure, restriction, portability, objection and automated-decision protections.

## SRC-PRIV-005 — DPIA

**WP29/EDPB-endorsed Guidelines on Data Protection Impact Assessment.**  
Тип: official regulatory guidance  
Качество: C2  
Статус: official index and relevant criteria reviewed

Поддерживает DPIA where processing is likely to create high risks; evaluation/scoring, sensitive data and novel technology are relevant criteria.

## SRC-PRIV-006 — LLM Privacy Risks & Mitigations

**EDPB Support Pool of Experts (2025). AI Privacy Risks & Mitigations — Large Language Models.**  
Тип: practical technical/privacy guidance  
Качество: C2/B1  
Статус: full document sections reviewed

Поддерживает lifecycle data-flow mapping, LLM-specific DPIA risks, sensitive disclosure, improper anonymization, unlawful training use and excessive retention.

The document is practical expert guidance and does not replace a DPIA or binding legal advice.

## SRC-PRIV-007 — NIST Privacy Framework

**NIST Privacy Framework and PF 1.1 materials.**  
Тип: voluntary risk-management framework  
Качество: C2  
Статус: official web material reviewed

Поддерживает management of privacy risk across the full data-processing ecosystem and lifecycle.

## SRC-PRIV-008 — Breach notification

**EDPB Guidelines 9/2022 on personal data breach notification under GDPR.**  
Тип: official guidance  
Качество: C2  
Статус: full relevant sections reviewed

Поддерживает confidentiality, integrity and availability breach categories and risk assessment for sensitive data and vulnerable people.

## SRC-REG-001 — EU AI Act

**Regulation (EU) 2024/1689.**  
Тип: binding EU regulation  
Качество: C2 / primary legal source  
Статус: current official text reviewed

Поддерживает prohibition of certain manipulative/deceptive practices that materially distort informed decisions and cause or are likely to cause significant harm.

Does not by itself determine Garden’s classification.

## SRC-REG-002 — AI Act implementation timeline

**European Commission — AI Act regulatory framework and navigation pages.**  
Тип: official implementation guidance  
Качество: C2  
Статус: updated pages reviewed July 2026

Supports entry into force on 1 August 2024, application of initial rules from 2 February 2025 and the Commission’s current implementation timeline. Re-check before launch because simplification and transitional measures are evolving.

## SRC-REG-003 — FDA digital-health software boundary

**FDA Clinical Decision Support Software guidance and Device Software Functions pages, current 2026.**  
Тип: official US regulatory guidance  
Качество: C2  
Статус: current web pages reviewed

Supports that intended purpose and patient-facing recommendations can affect medical-device oversight.

Not an EU classification source.

## SRC-SEC-001 — OWASP Prompt Injection

**OWASP GenAI Security Project, LLM01:2025 Prompt Injection.**  
Тип: industry security consensus guidance  
Качество: B1  
Статус: official page reviewed

Supports direct/indirect prompt-injection risks including data disclosure and unauthorized actions.

## SRC-SEC-002 — OWASP Sensitive Information Disclosure

**OWASP GenAI Security Project, LLM02:2025.**  
Тип: industry security guidance  
Качество: B1  
Статус: official page reviewed

Supports risks from PII/sensitive content in model inputs, outputs and application context.

System prompts alone are not an adequate control.

## SRC-SEC-003 — OWASP Top 10 for LLM/GenAI 2025

Тип: risk catalogue  
Качество: B1  
Статус: official project reviewed

Used for security threat coverage, not as proof that listed mitigations guarantee safety.

## SRC-SEC-004 — ENISA Securing ML Algorithms

**ENISA (2021). Securing Machine Learning Algorithms.**  
Тип: official cybersecurity taxonomy and review  
Качество: C2/B1  
Статус: official page reviewed

Supports poisoning, adversarial attacks, data exfiltration and ML lifecycle threats.

## SRC-SEC-005 — NIST AI RMF Generative AI Profile

**NIST AI 600-1 (2024).**  
Тип: voluntary risk-management profile  
Качество: C2  
Статус: official publication page reviewed

Supports governance, mapping, measurement and management of GenAI-specific risks.

## SRC-SAFE-001 — WHO AI for Health

**WHO (2021). Ethics and Governance of Artificial Intelligence for Health.**  
Тип: global governance guidance  
Качество: C2/B1  
Статус: official summary reviewed

Supports protecting autonomy, safety, transparency, accountability, inclusiveness and sustainability.

## SRC-SAFE-002 — WHO LMM guidance

**WHO (2024/2025). Ethics and Governance Guidance for Large Multi-Modal Models in Health.**  
Тип: official governance guidance  
Качество: C2/B1  
Статус: official publication pages reviewed

Supports lifecycle governance, stakeholder involvement, risk assessment and caution with generative systems in health contexts.

## SRC-SAFE-003 — WHO caution on health LLMs

**WHO (2023). WHO calls for safe and ethical AI for health.**  
Тип: official departmental statement  
Качество: C2  
Статус: reviewed

Supports caution to protect wellbeing, safety and autonomy before widespread routine use.

## SRC-SAFE-004 — NIMH mental-health technology overview

**NIMH — Technology and the Future of Mental Health Treatment.**  
Тип: official public-health overview  
Качество: C2  
Статус: current page reviewed

Supports potential benefits alongside uncertainty and limited information about effectiveness of many apps.

## New Source Registry fields

```yaml
legal_jurisdiction:
controller_or_processor_role:
article_6_basis:
article_9_condition:
dpia_required_or_recommended:
data_class:
purpose:
provider_retention:
provider_training:
international_transfer:
subprocessors:
prompt_injection_scope:
security_test:
incident_duty:
crisis_use:
child_use:
regulatory_classification:
last_legal_review:
```

---

## Imported source: `source_registry_addendum_R013_v0_1.md`

# Garden Source Registry — Addendum for R-013

**Версия:** 0.1  
**Дата:** 15 июля 2026

## SRC-META-001

Thibodeau, P. H., & Boroditsky, L. (2011). *Metaphors We Think With: The Role of Metaphor in Reasoning.* PLOS ONE, 6(2), e16782.  
DOI: `10.1371/journal.pone.0016782`  
Тип: five framing experiments  
Качество: A2  
Статус: full text reviewed

Поддерживает: metaphor framing can influence proposed solutions and information search.

Ограничения: specific crime scenarios; effect boundaries and coding contested in later work.

## SRC-META-002

Thibodeau, P. H., et al. (2015). *Measuring Effects of Metaphor in a Dynamic Opinion Landscape.* PLOS ONE.  
PMCID: `PMC4517745`  
Тип: experiments and reanalysis  
Качество: A2  
Статус: full text reviewed

Поддерживает context and existing opinion landscape as relevant to framing effects.

## SRC-META-003

Christmann, U., et al. (2016). *German-Language Replication of Metaphor Framing.* PLOS ONE.  
PMID: `27779615`; PMCID: `PMC5079120`  
Тип: replication study  
Качество: A2  
Статус: full text available/reviewed

Reports a successful replication in the studied German-language design.

## SRC-META-004

Steen, G. J., Reijnierse, W. G., & Burgers, C. (2014). *When Do Natural Language Metaphors Influence Reasoning?*  
Тип: critical follow-up study  
Качество: A2  
Статус: full manuscript identified/reviewed

Supports boundary-condition caution and sensitivity to coding/control comparisons.

## SRC-META-005

Landau, M. J., Keefer, L. A., & Rothschild, Z. K. (2017; PMC publication 2021). *Do Metaphors in Health Messages Work?*  
PMCID: `PMC8025806`  
Тип: systematic conceptual review of experiments  
Качество: B1  
Статус: full text reviewed

Supports possible effects on attention, comprehension, emotion, motivation and behavioral intentions in specific conditions.

Does not support universal benefit or clinical outcomes.

## SRC-META-006

Semino, E., Demjén, Z., & Demmen, J. (2017). *The Online Use of Violence and Journey Metaphors by Patients with Cancer.* BMJ Supportive & Palliative Care.  
PMID: `25743439`  
Тип: corpus-based qualitative analysis  
Качество: B2  
Статус: abstract and related corpus materials reviewed

Supports empowering and disempowering uses within both metaphor families.

## SRC-META-007

Lempp, H., et al. (2024). *The Use of Metaphors by Service Users With Diverse Long-Term Conditions.*  
PMID: `38328347`; PMCID: `PMC10849034`  
Тип: qualitative analysis  
Качество: B2  
Статус: full text reviewed

Supports polysemy and person/context dependence of illness metaphors.

## SRC-META-008

Rucińska, Z., et al. (2022). *Enacting Metaphors in Systemic Collaborative Therapy.*  
PMCID: `PMC9114737`  
Тип: theoretical and practice analysis  
Качество: B1/B2  
Статус: full text reviewed

Supports metaphor as shared, enacted and relational process rather than static linguistic substitution.

Not evidence for automated AI therapy.

## SRC-META-009

Řiháček, T., et al. (2021). *Facets of the Psychotherapy Relationship: A Metaphorical Approach.*  
PMCID: `PMC7875073`  
Тип: qualitative metaphor analysis  
Качество: B2  
Статус: full text reviewed

Supports use of metaphor to access relational experience not easily captured by analytic language.

## SRC-META-010

Roystonn, K., et al. *Cross-Cultural Exploration of Metaphors Used by Young Adults With Depression.*  
PMCID repository: `PMC11930630`  
Тип: cross-cultural qualitative analysis  
Качество: B2  
Статус: full text reviewed

Supports cultural overlap and variation in metaphor use.

Does not justify national metaphor profiles.

## SRC-META-011

Malkomsen, A., et al. (2021). *How Patients Use Metaphors to Describe Experiences of Psychiatric Treatment.*  
PMCID: `PMC8555134`  
Тип: qualitative systematic/empirical analysis  
Качество: B2  
Статус: full text reviewed

Supports metaphors as windows into expectations, distress and treatment experience.

## SRC-META-012

Altavilla, D., et al. (2025). *Metaphor as a Cognitive and Relational Tool for Self-Narrating Illness.*  
PMCID: `PMC12533479`  
Тип: qualitative/clinical communication analysis  
Качество: B2  
Статус: full text reviewed

Supports metaphor as coping and identity-narration tool.

## SRC-META-013

Lakoff, G., & Johnson, M. (1980/2003). *Metaphors We Live By.*  
Тип: foundational conceptual theory  
Качество: C1 theoretical classic  
Статус: bibliographic source

Use as theory, not causal experimental proof.

## SRC-META-014

Garden R-003. *Real Nature, Digital Nature and Garden Metaphor.*  
Тип: internal audited synthesis  
Статус: internal foundation

Supports strict separation of real nature effects and metaphor effects.

## Новые поля Source Registry

```yaml
metaphor_source:
metaphor_target:
user_authored:
product_imposed:
cultural_context:
empowering_reading:
disempowering_reading:
hidden_mapping:
systemic_issue_risk:
medical_implication:
literal_equivalent:
exit_available:
```

---

## Imported source: `source_registry_addendum_R014_v0_1.md`

# Garden Source Registry — Addendum for R-014

**Версия:** 0.1  
**Дата:** 16 июля 2026

## SRC-SOC-001

**Cohen, S., & Wills, T. A. (1985).**  
*Stress, Social Support, and the Buffering Hypothesis.* Psychological Bulletin, 98(2), 310–357.  
PMID: `3901065`  
Тип: foundational review  
Качество: B1  
Статус: bibliographic/official metadata reviewed

Supports distinctions between general beneficial effects and stress-buffering models of support.

## SRC-SOC-002

**Graven, L. J., & Grant, J. S. (2014).**  
*Social Support and Self-Care Behaviors in Individuals With Heart Failure.*  
PMID: `23850389`  
Тип: systematic review  
Качество: A1/B1  
Статус: abstract reviewed

Uses emotional, instrumental/tangible, informational and appraisal support categories.

Clinical context limits generalization.

## SRC-SOC-003

**Lee, A. A., et al. (2019).**  
*Diabetes Self-Management and Glycemic Control: The Role of Autonomy Support From Informal Health Supporters.*  
PMID: `30652911`  
Тип: observational health study  
Качество: A2  
Статус: abstract reviewed

Supports association between autonomy-supportive informal support and attitudes, self-care and glycemic control.

Does not prove Garden social mechanics.

## SRC-SOC-004

**Di Maio, S., et al. (2024).**  
*Compendium of Dyadic Intervention Techniques to Change Health Behaviours in Romantic Couples.*  
PMID: `38437798`  
Тип: systematic development of technique compendium  
Corpus: 165 studies, 122 interventions  
Качество: A1/B1  
Статус: abstract reviewed

Supports diversity of dyadic mechanisms rather than one generic partner-involvement technique.

## SRC-SOC-005

**Martire, L. M., et al. (2010).**  
*Review and Meta-Analysis of Couple-Oriented Interventions for Chronic Illness.*  
PMID: `20697859`  
Тип: meta-analysis  
Качество: A1  
Статус: abstract reviewed

Reports small average effects and potential value of targeting partner influence.

Clinical and chronic-illness context.

## SRC-SOC-006

**Fortuna, K. L., et al. (2020).**  
*Digital Peer Support Mental Health Interventions for People With a Lived Experience of a Serious Mental Illness: Systematic Review.*  
PMCID: `PMC7165313`  
Тип: systematic review  
Качество: A1  
Статус: full text available/abstract reviewed

Identified 30 studies/24 interventions; supports promise and major heterogeneity.

## SRC-SOC-007

**Marshall, P., et al. (2024).**  
*Understanding the Impacts of Online Mental Health Peer Support Forums: Realist Synthesis.*  
PMCID: `PMC11117133`  
Тип: realist review and program theory  
Качество: B1  
Статус: full text reviewed

Supports context-sensitive mechanisms behind positive and negative impacts.

## SRC-SOC-008

**Yeo, G. H., et al. (2025).**  
*The Effects of Digital Peer Support Interventions on Physical and Mental Health: Systematic Review and Meta-Analysis.*  
PMCID: `PMC11886969`  
Тип: systematic review and meta-analysis  
Качество: A1  
Статус: full text reviewed

Reports positive average effects, stronger mental-health effects, weaker effects at longer follow-up, and possible risks with extended exposure.

Heterogeneous intervention components and predominantly Western samples limit conclusions.

## SRC-SOC-009

**Easton, K., et al. (2017).**  
*Qualitative Exploration of the Potential for Adverse Events When Using an Online Peer Support Network.*  
PMCID: `PMC5684514`  
Тип: qualitative study  
Качество: B2  
Статус: full text reviewed

Identifies emotional/behavioral contagion, debate, co-rumination, collusion and negative interactions as relevant risks.

## SRC-SOC-010

**Kruzan, K. P., et al. (2023).**  
*Young Adults’ Perceptions of Publicly Available Digital Resources for Self-Injury.*  
PMCID: `PMC9880808`  
Тип: randomized/qualitative perception study  
Качество: A2/B2  
Статус: full text reviewed

Participants reported benefits and harms; peer-support app condition generated more reported harms than informational materials.

Narrow self-injury context.

## SRC-SOC-011

**Abou Seif, N., et al. (2022).**  
*Effectiveness, Acceptability and Potential Harms of Peer Support for Self-Harm: Systematic Review.*  
PMCID: `PMC8811789`  
Тип: systematic review  
Качество: A1  
Статус: full text reviewed

Supports acceptability and perceived community/empowerment benefits alongside limited effectiveness and harm evidence.

## SRC-SOC-012

**Strand, M., et al. (2020).**  
*Combining Online and Offline Peer Support Groups in Community Mental Health Care.*  
PMCID: `PMC7260836`  
Тип: implementation/qualitative study  
Качество: B2  
Статус: full text reviewed

Highlights concerns about excessive use, reduced offline interaction, avoidance and dependency.

## SRC-SOC-013

**Rose, A. J., et al. (2007).**  
*Prospective Associations of Co-Rumination With Friendship and Emotional Adjustment.*  
PMCID: `PMC3382075`  
Тип: longitudinal adolescent study  
Качество: A2  
Статус: full text reviewed

Supports co-rumination as a process with potential relational benefits and internalizing costs.

## SRC-SOC-014

**Starr, L. R., & Davila, J. (2009).**  
*Clarifying Co-Rumination: Associations With Internalizing Symptoms and Romantic Involvement.*  
PMCID: `PMC2652577`  
Тип: empirical study  
Качество: A2  
Статус: full text reviewed

Supports positive associations with depressive symptoms and friendship dimensions, with mixed longitudinal findings.

## SRC-SOC-015

**Mackenzie, E., et al. (2023).**  
*Online Support Seeking, Co-Rumination, and Mental Health.*  
PMCID: `PMC10027699`  
Тип: empirical study  
Качество: A2  
Статус: full text reviewed

Suggests co-rumination can reduce benefits of friend support seeking in studied youth data.

## SRC-SOC-016

**Stone, L. B., et al. (2022).**  
*Stop Talking About It Already! Co-Rumination and Social Media.*  
PMCID: `PMC8819886`  
Тип: empirical study  
Качество: A2  
Статус: full text reviewed

Supports adjustment trade-offs and relation between co-rumination and communication patterns.

## SRC-SOC-017

**Tong, H. L., et al. (2022).**  
*A Personalized Mobile App for Physical Activity: Social Comparison Preferences.*  
PMCID: `PMC9309778`  
Тип: user study  
Качество: B2  
Статус: full text reviewed

Supports diversity of preferences for similarity, upward and downward comparison.

Does not prove benefits of comparison.

## SRC-SOC-018

**Feng, S., et al. (2021).**  
*How Self-Tracking and the Quantified Self Promote Health and Well-Being: Systematic Review.*  
PMCID: `PMC8493454`  
Тип: systematic review  
Качество: A1  
Статус: full text reviewed

Supports social comparison/social support as possible mechanisms while documenting mixed experiences and risks.

## SRC-SOC-019

**Deng, D., et al. (2023).**  
*The Role of Moderators in Facilitating Peer-to-Peer Support in an Online Mental Health Community.*  
PMCID: `PMC9933803`  
Тип: qualitative moderator interviews  
Качество: B2  
Статус: full text reviewed

Supports active moderator roles in modeling, facilitation, safety and escalation.

## SRC-SOC-020

**Understanding Safety in Online Mental Health Forums (2025).**  
PMCID: `PMC12227176`  
Тип: realist evaluation  
Качество: B1/B2  
Статус: full text reviewed

Supports distinction between absence of harm and felt interpersonal safety and the role of platform context.

## SRC-SOC-021

**Métellus, S., et al. (2025).**  
*Attachment Anxiety and Relationship Satisfaction in the Digital Age: Social Media Jealousy and Electronic Partner Surveillance.*  
PMCID: `PMC12445260`  
Тип: three-wave longitudinal study, N=322  
Качество: A2  
Статус: full text reviewed

Supports digital jealousy/surveillance as relevant relationship risks, with partially supported longitudinal hypotheses.

Does not directly study shared wellbeing apps.

## New Source Registry fields

```yaml
support_type:
support_requested:
support_provider:
power_asymmetry:
dyadic_or_group:
data_visibility:
reciprocity:
coercion_risk:
co_rumination_risk:
comparison_present:
moderation_model:
offline_transfer:
exit_process:
```

---

## Imported source: `source_registry_addendum_R015_v0_1.md`

# Garden Source Registry — Addendum for R-015

**Версия:** 0.1  
**Дата:** 16 июля 2026

## SRC-STR-001

**World Health Organization (2025).**  
*Social Determinants of Health.*  
Тип: official fact sheet  
Качество: A0 institutional  
Статус: full page reviewed

Defines social determinants as conditions of birth, growth, work, life and ageing and wider forces shaping daily life.

## SRC-STR-002

**World Health Organization (2025).**  
*World Report on Social Determinants of Health Equity.*  
Тип: authoritative international report  
Качество: A0 institutional  
Статус: report overview reviewed

Supports importance of access to power, money and resources for avoidable health inequities.

## SRC-STR-003

**World Health Organization (2010).**  
*A Conceptual Framework for Action on the Social Determinants of Health.*  
ISBN: `9789241500852`  
Тип: conceptual policy framework  
Качество: A0/B1  
Статус: official publication reviewed

Distinguishes structural determinants and intermediary determinants through long causal chains.

## SRC-STR-004

**World Health Organization.**  
*Determinants of Health.*  
Тип: official overview  
Качество: A0  
Статус: full page reviewed

Includes social/economic environment, physical environment and individual characteristics/behaviours.

## SRC-STR-005

**Phelan, J. C., Link, B. G., & Tehranifar, P. (2010).**  
*Social Conditions as Fundamental Causes of Health Inequalities.*  
PMID: `20943581`  
Тип: theory review  
Качество: B1  
Статус: abstract reviewed

Supports flexible resources—money, knowledge, prestige, power and social connections—as mechanisms protecting health across changing risks.

## SRC-STR-006

**Clouston, S. A. P., & Link, B. G. (2021).**  
*A Retrospective on Fundamental Cause Theory.*  
PMCID: `PMC8691558`; PMID: `34949900`  
Тип: retrospective review  
Качество: B1  
Статус: full text available/reviewed

Supports persistence of inequalities through unequal flexible resources and development of FCT evidence.

## SRC-STR-007

**Kennedy, W., et al. (2021).**  
*Using Ecological Models of Health Behavior to Promote Health Care Access and Physical Activity Engagement.*  
PMCID: `PMC8295941`  
Тип: applied framework review  
Качество: B1  
Статус: full text reviewed

Uses individual, interpersonal, organizational, community and policy levels.

## SRC-STR-008

**Melino, K., et al. (2022).**  
*Structural Competency in Health Care.*  
PMCID: `PMC9300050`  
Тип: scoping review/conceptual synthesis  
Качество: B1  
Статус: full text reviewed

Supports recognizing structural factors, limits of individual/cultural explanations and multilevel responses.

## SRC-STR-009

**Halsall, T., et al. (2025).**  
*Tracing the Undercurrents: A Scoping Review of the Lifestyle Drift Concept.*  
PMCID: `PMC12837583`  
Тип: scoping review, 32 included articles  
Качество: B1  
Статус: full text reviewed

Defines drift from upstream structural action toward downstream individual behavior and identifies proposed drivers/mitigation strategies.

Notes need for more empirical research.

## SRC-STR-010

**Marmot, M., et al. (2014).**  
*Social Determinants of Health Equity.*  
PMCID: `PMC4151898`  
Тип: policy/research synthesis  
Качество: B1  
Статус: full text reviewed

Discusses lifestyle drift and need to address causes of causes.

## SRC-STR-011

**Yao, R., et al. (2022).**  
*Inequities in Health Care Services Caused by the Adoption of Digital Health Technologies.*  
PMCID: `PMC8981004`  
Тип: scoping review  
Качество: B1  
Статус: full text reviewed

Supports pathways through which digital health can create or reproduce inequities.

## SRC-STR-012

**Weiss, D., et al. (2018).**  
*Innovative Technologies and Social Inequalities in Health: A Scoping Review.*  
PMCID: `PMC5882163`  
Тип: scoping review  
Качество: B1  
Статус: full text reviewed

Supports consideration of differential access, uptake and benefit.

## SRC-WORK-001

**World Health Organization (2019/current ICD-11 page).**  
*Burn-out an Occupational Phenomenon.*  
Тип: official classification explanation  
Качество: A0  
Статус: official page reviewed

Defines burnout as syndrome resulting from chronic workplace stress that has not been successfully managed and limits it to occupational context.

## SRC-WORK-002

**International Labour Organization (2022).**  
*Psychosocial Risks and Stress at Work.*  
Тип: official occupational-safety guidance  
Качество: A0  
Статус: official page reviewed

Lists work design and management hazards including workload, pace, hours and job control.

## SRC-WORK-003

**International Labour Organization.**  
*Psychosocial Risks and Mental Health at Work.*  
Тип: official topic guidance  
Качество: A0  
Статус: official page reviewed

Includes organizational culture, job security, relationships, bullying/harassment and working conditions.

## SRC-WORK-004

**Bes, I., et al. (2023).**  
*Organizational Interventions and Occupational Burnout: A Meta-Analysis.*  
PMCID: `PMC10560169`  
Тип: meta-analysis  
Качество: A1  
Статус: full text reviewed

Organization-directed and combined interventions showed small-to-moderate exhaustion reductions; workload-targeted and participatory interventions were among stronger categories.

## SRC-WORK-005

**Aust, B., et al. (2024).**  
*Effects of Different Types of Organisational Workplace Interventions on Mental Health and Well-Being in Healthcare Workers.*  
PMCID: `PMC11130054`  
Тип: systematic review/meta-analysis  
Качество: A1  
Статус: full text reviewed

Supports potential effectiveness of organizational interventions, especially implemented workplace changes; participatory interventions face implementation barriers.

## SRC-WORK-006

**Greiner, B. A., et al. (2022).**  
*Effectiveness of Organisational-Level Workplace Mental Health Interventions.*  
PMCID: `PMC9668198`  
Тип: systematic review  
Качество: A1/B1  
Статус: full text reviewed

Identifies team, task-allocation and participatory approaches; evidence base limited.

## SRC-WORK-007

**Kiratipaisarl, W., et al. (2024).**  
*Individual and Organizational Interventions to Reduce Burnout in Resident Physicians.*  
PMCID: `PMC11523819`; PMID: `39478552`  
Тип: systematic review/meta-analysis  
Качество: A1  
Статус: full text reviewed

Finds none-to-small practical effects overall with inconsistency and high risk of bias; recommends combined approach research.

## SRC-WORK-008

**Shoman, Y., et al. (2021).**  
*Predictors of Occupational Burnout: A Systematic Review.*  
PMCID: `PMC8430894`  
Тип: systematic review  
Качество: A1  
Статус: full text reviewed

Supports job demands, control/resources and effort–reward factors while noting mixed buffering evidence.

## New Source Registry fields

```yaml
problem_level:
root_cause:
immediate_mechanism:
user_control:
other_actor_control:
formal_responsibility:
resource_requirements:
power_asymmetry:
structural_determinant:
relief_or_resolution:
retaliation_risk:
external_verification:
lifestyle_drift_risk:
```

---

## Imported source: `source_registry_addendum_R016_v0_1.md`

# Garden Source Registry — Addendum for R-016

**Версия:** 0.1  
**Дата:** 16 июля 2026  
**Scope:** current public product positioning, pricing and privacy claims; verify before decisions

## Direct AI journals

### SRC-MKT-001 — Rosebud

Official site and help center, accessed July 2026.

Observed public claims/features:

- AI journal adapting to the user;
- personalized prompts;
- pattern discovery;
- voice;
- long-term memory;
- self-care/habits;
- free tier;
- USD 12.99 monthly and USD 107.99 yearly offer displayed at access time;
- user input described as not used to train future models in its comparison material.

Use limitation: marketing claims are not independent outcome evidence.

### SRC-MKT-002 — Reflection

Official site, FAQ and premium page.

Observed:

- AI journal and coach;
- real-time guidance;
- voice;
- 100+ guides/programs;
- advanced insights;
- encryption at rest/in transit;
- subscription-funded;
- USD 8 monthly / USD 5.75 monthly annualized at access time.

### SRC-MKT-003 — Mindsera

Official site, privacy and plan pages.

Observed:

- AI journal / thinking copilot;
- emotion detection;
- patterns;
- frameworks;
- morning/evening rituals;
- habit tracker;
- voice, call and physical-journal scan;
- AES-256 at rest and TLS in transit;
- explicit statement that server-side AI is not compatible with true E2EE;
- paid range shown as approximately USD 10.75–14.99 monthly.

### SRC-MKT-004 — Liven

Official website and app listings.

Observed:

- self-discovery companion;
- mood tracking;
- habits;
- courses;
- AI assistant Livie;
- non-medical disclaimer.

## Practice and self-care

### SRC-MKT-005 — Finch

Official site/help and current app listings.

Observed:

- self-care pet;
- personalized exercises;
- daily rewards and events;
- friend/streak elements in current listing.

### SRC-MKT-006 — Fabulous

Official site and app listing.

Observed:

- routine and self-care app;
- daily coaching;
- goals/to-dos;
- journaling;
- workouts, breathwork, affirmations and meditation.

### SRC-MKT-007 — Habitica

Official site and current app listing.

Observed:

- game framing;
- recurring tasks and habits;
- streak counters;
- leveling;
- gear and pets;
- health loss/reward logic.

### SRC-MKT-008 — Stoic

Current app listings.

Observed:

- morning preparation and evening reflection;
- mood tracking;
- journal prompts;
- habits;
- meditation/breathwork;
- AI mentor/insight features described in current comparison materials.

## Measurement

### SRC-MKT-009 — Daylio

Official site and app listings.

Observed:

- no-writing mood journal;
- activities;
- goals;
- Year in Pixels;
- charts/statistics.

### SRC-MKT-010 — How We Feel

Official site and app listings.

Observed:

- emotion vocabulary;
- check-ins;
- strategies;
- sleep/exercise/health trends.

### SRC-MKT-011 — Bearable

Official product and support pages.

Observed:

- symptoms, moods, factors, treatments;
- correlations and experiments;
- warnings that correlation quality depends on data and professional guidance;
- premium price USD 34.99 annual at access time.

### SRC-MKT-012 — Exist

Official site.

Observed:

- integrated personal data;
- correlations;
- behavioral experiments;
- questions such as what makes the user happiest or productive.

## Mental health and companions

### SRC-MKT-013 — Headspace Ebb

Official Headspace pages.

Observed:

- adult 18+ AI companion;
- self-reflection and emotional processing;
- recommendations into Headspace library;
- not human care;
- no real-time human monitoring stated on product FAQ;
- automated real-time classification across defined risk categories described on AI principles page;
- encrypted data and limited need-to-know employee access;
- USD 69.99 annual offer at access time.

### SRC-MKT-014 — Wysa

Official site, FAQ and app listing.

Observed:

- anonymous AI conversation;
- structured techniques;
- human coach option;
- health-system and employer/institutional positioning.

### SRC-MKT-015 — Ash

Official site and app listing.

Observed:

- purpose-built mental-health AI;
- voice/text;
- weekly patterns;
- long-term growth;
- crisis disclaimer.

### SRC-MKT-016 — Replika

Official site and May 2026 privacy policy.

Observed:

- AI friend/companion;
- meaningful relationship;
- individualized conversation and learning from interactions;
- 18+ in current policy.

### SRC-MKT-017 — Pi

Current official app listing and service status.

Observed:

- emotionally intelligent AI;
- decision support, planning, growth and entertainment;
- «grows with you» positioning;
- updated July 2026.

### SRC-MKT-018 — Character.AI

Official privacy policy plus July 2026 regulatory reporting.

Observed:

- lifelike character conversations and user-generated content;
- significant age/privacy scrutiny;
- not a recommended model for Garden.

## Journals and knowledge systems

### SRC-MKT-019 — Day One

Official site, pricing and encryption documentation.

Observed:

- multimedia journal;
- durable archive and export;
- E2EE default for new journals;
- user-held key;
- USD 49.99 annual Silver plan at access time.

### SRC-MKT-020 — Apple Journal

Official Apple product/privacy/developer pages.

Observed:

- moments and multimedia;
- on-device Journaling Suggestions;
- user control of suggestion categories and sharing;
- device lock/biometrics.

### SRC-MKT-021 — Reflect Notes

Official site.

Observed:

- linked notes;
- GPT/Whisper AI;
- intellectual thought-partner positioning.

### SRC-MKT-022 — Capacities

Official site/app listing.

Observed:

- connected objects;
- daily notes;
- AI assistant;
- long-term personal knowledge system.

## Category privacy research

### SRC-MKT-023

Georgiou, C., Lu, H., De Cristofaro, E., & Tsudik, G. (2026).  
*What's on Your Mind? Exploring Privacy of Mental Health Apps.*  
arXiv: `2605.02016`.

Technical analysis of 25 Android mental-health and life-coaching apps reported:

- at least one undisclosed tracker SDK in every analyzed app;
- 68% failing to disclose at least half of detected trackers;
- permission-policy contradictions;
- inconsistent identification of third-party AI recipients.

Status: recent preprint; methods and sample should be independently audited before regulatory claims.

## New Source Registry fields

```yaml
product:
category:
public_positioning:
core_user_job:
ai_role:
memory_model:
measurement_model:
engagement_model:
social_model:
business_model:
privacy_claim:
clinical_claim:
garden_overlap:
garden_risk:
last_verified:
```

---

## Imported source: `source_registry_addendum_R017_v0_1.md`

# Garden Source Registry — Addendum for R-017

**Версия:** 0.1  
**Дата:** 16 июля 2026

## SRC-UNK-001

**Bilalić, M., McLeod, P., & Gobet, F. (2008).**  
*Inflexibility of Experts—Reality or Myth? Quantifying the Einstellung Effect in Chess Masters.* Cognitive Psychology, 56(2), 73–102.  
DOI: `10.1016/j.cogpsych.2007.02.001`  
Тип: expert problem-solving experiments  
Качество: A2  
Статус: abstract/metadata reviewed

Supports suboptimal familiar solutions impairing discovery of better solutions in chess expertise.

Does not support general expert rigidity across all tasks.

## SRC-UNK-002

**Bilalić, M., McLeod, P., & Gobet, F. (2010).**  
*The Mechanism of the Einstellung Effect.*  
Тип: eye-tracking/problem-solving study  
Качество: A2  
Статус: bibliographic source

Supports attentional capture by familiar solution patterns.

## SRC-UNK-003

**Dane, E. (2010).**  
*Reconsidering the Trade-off Between Expertise and Flexibility: A Cognitive Entrenchment Perspective.* Academy of Management Review, 35(4), 579–603.  
DOI: `10.5465/amr.35.4.zok579`  
Тип: theory review  
Качество: B1  
Статус: abstract reviewed

Supports cognitive entrenchment as a possible cost of stable expert schemas.

## SRC-UNK-004

**Crilly, N. (2015).**  
*Fixation and Creativity in Concept Development: The Attitudes and Practices of Expert Designers.* Design Studies, 38, 54–91.  
DOI: `10.1016/j.destud.2015.01.002`  
Тип: literature synthesis + interviews with 13 professional designers  
Качество: B1/B2  
Статус: full repository text reviewed

Supports fixation as multifaceted and expert practices for addressing it.

## SRC-UNK-005

**Jansson, D. G., & Smith, S. M. (1991).**  
*Design Fixation.* Design Studies, 12(1), 3–11.  
DOI: `10.1016/0142-694X(91)90003-F`  
Тип: classic experimental study  
Качество: A2  
Статус: bibliographic source

Supports example-induced fixation in design tasks.

## SRC-UNK-006

**National Research Council (2000).**  
*How People Learn: How Experts Differ from Novices.*  
Тип: authoritative research synthesis  
Качество: A0/B1  
Статус: official chapter reviewed

Supports experts organizing knowledge around deep principles and meaningful relations rather than only surface features.

## SRC-UNK-007

**Zhu, M., et al. (2022).**  
*Differences in Thinking Flexibility Between Novices and Experts Based on Eye Tracking.*  
PMCID: `PMC9246232`  
Тип: empirical expert–novice study  
Качество: A2  
Статус: full text reviewed

In the studied task, experts allocated attention more effectively; novices ignored some less salient information.

Counters simple novice-superiority assumptions.

## SRC-UNK-008

**Haavold, P. Ø. (2022).**  
*Creativity in Problem Solving: Integrating Two Different Views of Insight.* ZDM Mathematics Education.  
DOI: `10.1007/s11858-021-01304-8`  
Тип: conceptual/research synthesis  
Качество: B1  
Статус: abstract reviewed

Supports interaction between expertise, problem representation and creative process.

## SRC-UNK-009

**Loewenstein, G. (1994).**  
*The Psychology of Curiosity: A Review and Reinterpretation.* Psychological Bulletin, 116(1), 75–98.  
DOI: `10.1037/0033-2909.116.1.75`  
Тип: foundational theoretical review  
Качество: B1  
Статус: full PDF reviewed

Proposes information-gap theory and nonlinear relation between knowledge gaps and curiosity.

## SRC-UNK-010

**Kidd, C., & Hayden, B. Y. (2015).**  
*The Psychology and Neuroscience of Curiosity.* Neuron, 88(3), 449–460.  
DOI: `10.1016/j.neuron.2015.09.010`  
Тип: interdisciplinary review  
Качество: B1  
Статус: abstract reviewed

Supports curiosity as central to information seeking and learning with multiple mechanisms.

## SRC-UNK-011

**Porter, T., et al. (2022).**  
*Predictors and Consequences of Intellectual Humility.* Nature Reviews Psychology, 1, 524–536.  
PMCID: `PMC9244574`  
Тип: review  
Качество: B1  
Статус: full text reviewed

Defines intellectual humility around recognizing knowledge limits and fallibility; synthesizes correlates and consequences.

## SRC-UNK-012

**Zmigrod, L., et al. (2019).**  
*The Psychological Roots of Intellectual Humility.* Personality and Individual Differences, 141, 200–208.  
DOI: `10.1016/j.paid.2019.01.016`  
Тип: empirical study  
Качество: A2  
Статус: abstract reviewed

Supports association between flexible thinking disposition and intellectual humility, independent of measured cognitive ability.

## SRC-UNK-013

**Leary, M. R., et al.**  
*The Psychology of Intellectual Humility.*  
Тип: research-program synthesis  
Качество: B1  
Статус: full report metadata reviewed

Notes benefits, possible downsides and need to distinguish humility from low confidence.

## SRC-UNK-014

**Stanovich, K. E., & Toplak, M. E. (2023).**  
*Actively Open-Minded Thinking and Its Measurement.*  
PMCID: `PMC9966223`  
Тип: measurement/theoretical review  
Качество: B1  
Статус: full text reviewed

Supports willingness to consider alternatives, counterevidence, reflective thought and delayed closure.

## SRC-UNK-015

**Rozenblit, L., & Keil, F. (2002).**  
*The Misunderstood Limits of Folk Science: An Illusion of Explanatory Depth.* Cognitive Science, 26(5), 521–562.  
DOI: `10.1207/S15516709COG2605_1`; PMCID: `PMC3062901`  
Тип: experimental studies  
Качество: A2  
Статус: full text reviewed

Supports overestimation of explanatory understanding for complex causal mechanisms and recalibration after attempted explanation.

## SRC-UNK-016

**Dunning, D. (2011).**  
*The Dunning–Kruger Effect: On Being Ignorant of One’s Own Ignorance.* Advances in Experimental Social Psychology, 44, 247–296.  
DOI: `10.1016/B978-0-12-385522-0.00005-6`  
Тип: review chapter  
Качество: B1  
Статус: full report reviewed

Supports metacognitive difficulty in recognizing some knowledge deficits.

## SRC-UNK-017

**Hofer, G., et al. (2022).**  
*Less-Intelligent and Unaware? Accuracy and Dunning–Kruger Effects.*  
PMCID: `PMC8883889`  
Тип: empirical/methodological analysis  
Качество: A2  
Статус: full text reviewed

Supports caution: some observed Dunning–Kruger patterns can arise from measurement/statistical effects, while accuracy differences still matter.

## SRC-UNK-018

**Edmondson, A. (1999).**  
*Psychological Safety and Learning Behavior in Work Teams.* Administrative Science Quarterly, 44(2), 350–383.  
DOI: `10.2307/2666999`  
Тип: multimethod field study  
Качество: A2  
Статус: full manuscript reviewed

Supports association between team psychological safety and learning behavior.

Transfer to individual app use is indirect.

## SRC-UNK-019

**Sarasvathy, S. D. (2001).**  
*Causation and Effectuation: Toward a Theoretical Shift from Economic Inevitability to Entrepreneurial Contingency.* Academy of Management Review, 26(2), 243–263.  
DOI: `10.5465/amr.2001.4378020`  
Тип: foundational theory based on entrepreneurial expertise research  
Качество: B1  
Статус: bibliographic/summary reviewed

Distinguishes prediction-oriented causation and control-oriented effectuation under uncertainty.

## SRC-UNK-020

**Harms, R., & Schiele, H. (2012).**  
*Antecedents and Consequences of Effectuation and Causation in the International New Venture Process.* Journal of International Entrepreneurship, 10, 95–116.  
DOI: `10.1007/s10843-012-0089-2`  
Тип: protocol analysis  
Качество: A2  
Статус: abstract reviewed

Reports expert entrepreneurs more often using means-driven, affordable-loss and partnership reasoning in hypothetical venture tasks.

## SRC-UNK-021

**Effectuation research program.**  
*Five Principles of Effectuation / Affordable Loss.*  
Тип: theory translation and research program  
Качество: B1/C1  
Статус: official research-community materials reviewed

Use as design inspiration, not a universal decision rule.

## SRC-UNK-022

**Flyvbjerg, B., & Sunstein, C. R. (2016).**  
*The Principle of the Malevolent Hiding Hand; or, the Planning Fallacy Writ Large.*  
arXiv: `1509.01526` / Social Research  
Тип: project-performance analysis  
Качество: B1  
Статус: manuscript reviewed

Argues cost overruns and benefit shortfalls are more common than beneficial hidden-difficulty effects.

## SRC-UNK-023

**Flyvbjerg, B. (2018).**  
*Planning Fallacy or Hiding Hand: Which Is the Better Explanation?*  
arXiv: `1802.09999`  
Тип: empirical/theoretical response using large project dataset  
Качество: B1  
Статус: manuscript reviewed

Reports beneficial Hiding Hand pattern as minority rather than typical case in analyzed projects.

## SRC-UNK-024

**Flyvbjerg, B. (2022).**  
*Top Ten Behavioral Biases in Project Management.*  
arXiv: `2202.00125`  
Тип: research overview  
Качество: B1/C1  
Статус: abstract reviewed

Highlights optimism bias, planning fallacy, overconfidence, uniqueness and base-rate neglect.

## SRC-UNK-025

**Ballantyne, N. (2019).**  
*Epistemic Trespassing.* Mind, 128(510), 367–395.  
DOI: `10.1093/mind/fzx042`  
Тип: philosophical analysis  
Качество: B1  
Статус: manuscript reviewed

Defines risk of experts judging outside their competence domains.

## SRC-UNK-026

**DiPaolo, J. (2021).**  
*What’s Wrong With Epistemic Trespassing?* Philosophical Studies.  
PMCID: `PMC8131877`  
Тип: philosophical analysis  
Качество: B1  
Статус: full text reviewed

Examines epistemic and moral problems of cross-domain expert judgment.

## SRC-UNK-027

**Chen, L., et al. (2025).**  
*Understanding Design Fixation in Generative AI.*  
arXiv: `2502.05870`  
Тип: framework and experimental study  
Качество: A2/C1 preprint  
Статус: abstract reviewed

Supports emerging concern that generative AI outputs can exhibit and contribute to design fixation.

## SRC-UNK-028

**Wen, C., et al. (2025).**  
*Exploration vs. Fixation: Scaffolding Divergent and Convergent Thinking for Human–AI Co-Creation.*  
arXiv: `2512.18388`  
Тип: HCI system and within-subject study  
Качество: A2/C1 preprint  
Статус: abstract reviewed

Reports structured divergent/convergent stages improved perceived exploration/control compared with linear chat in the studied creative task.

## SRC-UNK-029

**Younie, L. (2017).**  
*Beginner’s Mind.*  
PMCID: `PMC5694793`  
Тип: medical-education reflective article  
Качество: C1  
Статус: full text reviewed

Uses beginner’s mind as openness and curiosity in the medical encounter.

Not empirical validation of shoshin as intervention.

## New Source Registry fields

```yaml
unknown_type:
recognized_unknown:
hard_constraint:
soft_constraint:
domain_expertise_required:
reversibility:
affordable_loss:
feedback_speed:
disconfirming_evidence:
historical_memory_bracketed:
identity_story:
experiment_or_decision:
learning_created:
```

---

## Imported source: `source_registry_addendum_R018_v0_1.md`

# Source Registry Addendum — R-018

**Дата:** 16 июля 2026

## Core theoretical sources

- Scannell, L., & Gifford, R. (2010). *Defining place attachment: A tripartite organizing framework.* Journal of Environmental Psychology.
- Lewicka, M. (2011). *Place attachment: How far have we come in the last 40 years?* Journal of Environmental Psychology.
- Proshansky, H. M., Fabian, A. K., & Kaminoff, R. (1983). *Place-identity: Physical world socialization of the self.*
- Williams, D. R., & Vaske, J. J. (2003). *The measurement of place attachment.*
- Kaplan, S. (1995). *The restorative benefits of nature: Toward an integrative framework.*
- Hartig et al. and later systematic reviews of restorative environments.
- Oldenburg, R. *The Great Good Place* — conceptual source for third places.
- Finlay et al. (2019). Third places and health/wellbeing.
- Kim et al. (2025). Discord and virtual third-place design.
- Virtual world place-attachment and gaming studies.
- R-003, R-013, R-014 and R-016 internal Garden research.

## Evidence cautions

- Much place-attachment research is correlational and self-report based.
- Physical-place findings do not automatically transfer to digital products.
- Third-place theory does not validate a private app or community feature.
- Restorative-environment theory does not establish clinical effects for Garden.
- Cozy-game market language is not outcome evidence.

## New fields

```yaml
place_type:
place_meaning_owner:
place_identity_risk:
place_dependence:
customization:
persistence:
reversibility:
absence_effect:
departure_support:
sensory_coherence:
ambient_obligation:
virtual_to_physical_transfer:
```

---

## Imported source: `source_registry_addendum_R020_v0_1.md`

# Source Registry Addendum — R-020

**Дата:** 16 июля 2026

## Primary and authoritative sources used

- UNESCO World Heritage Centre — The Persian Garden.
- Encyclopaedia Iranica — Čahārbāḡ and Achaemenid gardens.
- The Metropolitan Museum of Art — The Gardens of The Met Cloisters.
- Smarthistory / British Museum — Chinese scholar-painters and garden culture.
- Smarthistory — Ryōanji.
- The Metropolitan Museum of Art — Japanese Tea Ceremony, Muromachi period, seasonal imagery.
- Château de Versailles — Gardens, groves and official history.
- Historic England — English Landscape Garden and Capability Brown landscapes.
- National Gallery of Art — History of Early American Landscape Design.

## Evidence cautions

- Garden traditions are internally diverse and changed across centuries.
- Museum summaries simplify contested scholarship.
- Symbolic meanings vary by period, region and patron.
- Modern reconstructions may combine evidence and interpretation.
- Elite gardens dominate surviving documentation.
- Domestic, Indigenous, vernacular and colonized perspectives require further research.

---

## Imported source: `source_registry_addendum_R021_v0_1.md`

# Source Registry Addendum — R-021

**Дата:** 16 июля 2026

## Authoritative and research sources

- CIE International Lighting Vocabulary — perceived colour and its attributes.
- CIE publications on colour appearance and stimulus size.
- W3C WCAG 2.2 — Use of Color, Contrast Minimum and Non-text Contrast.
- Elliot, A. J. (2015). Color and psychological functioning: review.
- Jonauskaite et al. (2025). Systematic review of colour-emotion associations.
- Jonauskaite et al. (2016). Object context and colour preferences.
- Álvaro et al. (2015). Colour preference in red–green dichromats.
- Al-Rasheed et al. and related cross-cultural colour-preference studies.
- Kawai et al. (2022). Cross-cultural implicit colour-valence associations.
- Leonard et al. (2025). Pastel colours and emotional response.

## Evidence cautions

- Many colour studies use small patches under controlled conditions.
- Screen, illumination and surround vary in real products.
- Cultural group averages do not justify personal inference.
- Emotion associations do not establish durable mood effects.
- Accessibility simulations do not replace user testing.

---

## Imported source: `source_registry_addendum_R022_v0_1.md`

# Source Registry Addendum — R-022

**Дата:** 16 июля 2026

## Sources

- CIE publications on colour vision, brightness and lightness.
- W3C WCAG 2.2.
- W3C Understanding SC 2.3.3 Animation from Interactions.
- W3C technique C39 for `prefers-reduced-motion`.
- Madan et al. (2024), Restorative effects of daylight in indoor environments: systematic review.
- Karaman-Madan et al. (2026), Natural dynamics without nature? Motion type in light patterns.
- CIBSE research insight on circadian lighting.

## Evidence cautions

- physical-light findings do not directly transfer to screen rendering;
- daylight studies concern actual indoor light, not digital imagery;
- circadian effects require photometric and temporal exposure data;
- dynamic-light research is emerging;
- accessibility standards define minimum requirements, not complete comfort.

---

## Imported source: `source_registry_addendum_R023_v0_1.md`

# Source Registry Addendum — R-023

**Дата:** 16 июля 2026

## Sources

- Fleming, R. W. (2014). Visual perception of materials and their properties.
- Harvey et al. (2021). Low-level visual features support robust material categorization.
- Schmid et al. (2023). Material category from specular image structure.
- Chadwick & Kentridge (2015). The perception of gloss: review.
- Roberts et al. (2024). Visual effects on tactile texture perception.
- Adams et al. (2016). Touch influences perceived gloss.
- Lacey & Sathian (2014). Visuo-haptic multisensory object recognition.
- Malik et al. (2026). Material qualities from moving contours.
- Sakamoto et al. (2017). Tactile perceptual dimensions using materials.
- Strappini et al. (2024). Sustainable materials, perception, affordance and aesthetics.
- Ranscombe et al. (2022). Material ageing and aesthetic appreciation.
- De Korte et al. (2022). Visual perception of changes in material surfaces over time.
- Wastiels et al. (2012). Material experience and perceived warmth.
- Zhao et al. (2023). Interior materials and perceived restorativeness.
- W3C WCAG 2.2 for non-text information and accessibility principles.

## Evidence cautions

- many studies use isolated rendered objects or laboratory samples;
- material perception differs between screen, VR and physical touch;
- aesthetic associations are context- and culture-dependent;
- “natural” appearance does not establish sustainability;
- patina studies are limited and material-specific;
- visual haptics do not reproduce full physical sensation.

---

## Imported source: `source_registry_addendum_R024_v0_1.md`

# Source Registry Addendum — R-024

**Дата:** 16 июля 2026

## Sources

- Allman et al. (2014). First- and second-order principles of subjective time.
- Merchant et al. (2013). Neural basis of time perception and estimation.
- Wittmann (2009). The inner experience of time.
- Polti et al. (2018). Attention and working memory effects on duration estimation.
- Zacks (2020). Event perception and memory.
- Clewett et al. (2019). Event memories and temporal organization.
- van de Ven et al. (2021). Timing contexts and event segmentation.
- Morrow et al. (2025). Event boundaries and temporal distortions.
- Li et al. (2025). Hierarchical event segmentation in virtual environments.
- Yue et al. (2026). Retrospective duration judgments of naturalistic events.
- Pendleton et al. (2025). Time in mind and mental time travel.
- ACM CHI PLAY: Daily Quests or Daily Pests?
- ACM work on deceptive time pressure and FOMO in games and commerce.

## Evidence cautions

- laboratory duration tasks do not directly describe long-term product experience;
- event segmentation findings do not justify AI-generated life chapters;
- autobiographical memory is reconstructive;
- exact calendar data can remain important for accuracy and accountability;
- game FOMO studies do not prove every seasonal event is harmful;
- product hypotheses around guilt-free absence require direct testing.

---

## Imported source: `source_registry_addendum_R025_v0_1.md`

# Source Registry Addendum — R-025

**Дата:** 17 июля 2026

## Sources

- Rault (2015), Pets in the Digital Age: Live, Robot, or Virtual?
- Na et al. (2022), Mixed Reality-Based Interaction between Human and Virtual Animals.
- Johnson et al. (2023), Virtual animal stimuli in academic advising.
- Relatedness and Psychological Ownership in Augmented Reality (CHI 2019), longitudinal virtual-dog study.
- Northrope et al. (2025), systematic review of pet attachment and mental health/wellbeing.
- Friedmann et al. (2025), pet attachment and longitudinal psychological health.
- Lass-Hennemann et al. (2022), attachment to pets and mental-health burden.
- Ma et al. (2025), anthropomorphism, perceived intelligence and attachment/trust.
- Li et al. (2026), human-like conversational agents as social partners.
- Cihodaru-Ștefanache et al. (2025), anthropomorphism and emotional expectations.
- Research on deceptive game design, wildlife embodiment in VR and perceived natural diversity.

## Evidence cautions

- real-pet findings do not transfer directly to virtual animals;
- virtual-animal studies are often small or short-term;
- positive affect is not durable wellbeing evidence;
- attachment can be beneficial, neutral or burdensome;
- perceived biodiversity is not ecological biodiversity;
- symbolism and comfort vary across cultures.

---

## Imported source: `source_registry_addendum_R026_v0_1.md`

# Source Registry Addendum — R-026

**Дата:** 17 июля 2026

## Sources

- ISO 12913-1 — Soundscape: definition and conceptual framework.
- Fan et al. (2024). The effect of exposure to natural sounds on stress reduction: systematic review and meta-analysis.
- Song et al. (2023). Effects of nature sounds on attention and physiological/psychological relaxation.
- Peters et al. (2023). The impact of musicking on emotion regulation: systematic review and meta-analysis.
- Chong et al. (2024). Scoping review on the use of music for emotion regulation.
- Lu & Song (2025). Music-based emotion regulation research review.
- Cheah et al. Background Music and Cognitive Task Performance: systematic review.
- Absar & Guastavino (2008). Usability of non-speech sounds in interfaces.
- Systematic review/meta-analysis of auditory icons, earcons, spearcons and speech.
- W3C WCAG 2.2 — audio control and non-audio alternatives.
- Garden internal R-003, R-004, R-009, R-013, R-022 and R-025.

## Evidence cautions

- soundscape effects are context-dependent;
- natural-sound studies vary in stimuli, duration and outcomes;
- music emotion regulation is not equivalent to music therapy;
- cognitive effects of background music are inconsistent;
- laboratory listening does not reproduce long-term product use;
- pleasant sound can still create fatigue through repetition;
- audio accessibility requires real-user testing.

---

## Imported source: `source_registry_addendum_R027_v0_1.md`

# Source Registry Addendum — R-027

**Дата:** 17 июля 2026

## Источники

- Gibson, J. J. (1979). *The Ecological Approach to Visual Perception*.
- Maier, Fadel & Battisto (2009). *An affordance-based approach to architectural theory, design, and practice*.
- Baber (2022). *Embodying Design*.
- Costanza-Chock (2020). *Design Justice* — неравный доступ к affordances и ценности, встроенные в системы.
- Lynch (1960). *The Image of the City* — landmarks, paths, edges, districts and nodes.
- Research on environmental affordances in open and green spaces.
- Recent affordance-based architectural evaluation research.
- Public-open-space research on seating, seclusion and solitary practices.
- Garden internal R-018, R-019, R-020 and World Architecture v1.

## Ограничения

- физические affordances нельзя напрямую переносить в цифровой мир;
- intended function, perceived affordance and actual use различаются;
- возможности зависят от тела, навыков, устройства и социального контекста;
- архитектурные эффекты часто контекстны и корреляционны;
- культурные значения объектов не универсальны.

---

## Imported source: `source_registry_addendum_R028_v0_1.md`

# Source Registry Addendum — R-028

**Дата:** 17 июля 2026

## Sources

- Scannell & Gifford (2010). Defining place attachment: A tripartite organizing framework.
- Lewicka (2008). Place attachment, place identity, and place memory.
- Lewicka (2011). Place attachment: How far have we come in the last 40 years?
- Hay (1998). Sense of place in developmental context.
- Rajala et al. (2020). The meaning(s) of place: structure of sense of place.
- Lynch (1960). The Image of the City.
- Appleton (1975). The Experience of Landscape.
- Dosen & Ostwald (2016). Evidence for prospect-refuge theory: a meta-analysis.
- Akcelik et al. (2024). Aesthetic preference through the lens of prospect-refuge theory.
- Lebrusán (2022). The importance of place attachment in understanding ageing in place.
- Garden internal R-019, R-020, R-024 and R-027.

## Evidence cautions

- physical-place attachment research does not directly validate digital place attachment;
- repeated exposure does not guarantee attachment;
- attachment may also complicate change, loss and departure;
- prospect-refuge findings are heterogeneous;
- public-space findings depend on culture, safety and social context;
- naming and templates require direct product testing;
- Garden must not deliberately optimize emotional dependency.

---

## Imported source: `source_registry_addendum_R029_v0_1.md`

# Source Registry Addendum — R-029

Internal foundations: R-019, R-024, R-025, R-026, R-027, R-028 and the eight Garden Trigger decks.

Cautions:

- perceived aliveness requires direct testing;
- trigger cards generate alternatives and are not evidence;
- reversibility is a product principle, not a universal psychological law;
- long-term effects of persistent virtual worlds need later research;
- migration requirements need technical validation.

---

## Imported source: `source_registry_addendum_R030_v0_1.md`

# Source Registry Addendum — R-030

**Дата:** 17 июля 2026

## Foundations

- Lynch — paths, edges, nodes, landmarks and spatial legibility.
- Wayfinding and information-foraging traditions.
- Accessibility principles for non-spatial alternatives and reduced motion.
- Garden internal R-027, R-028 and R-029.
- Garden Trigger decks: Innovation, Human-centric, Graphic Design, Storytelling and Business Design.

## Evidence cautions

- physical wayfinding does not transfer directly to digital worlds;
- spatial interfaces are not inherently intuitive;
- direct access and world immersion must be tested together;
- map preference varies by task and user;
- trigger cards generate hypotheses, not evidence;
- accessibility requires testing with real assistive technologies and users.

---

## Imported source: `source_registry_addendum_R031_v0_1.md`

# Source Registry Addendum — R-031

**Дата:** 17 июля 2026

## Foundations

- Human-in-the-loop and mixed-initiative interaction traditions.
- Version control, reversible interaction and provenance principles.
- Garden internal R-019, R-024, R-027, R-029 and R-030.
- Garden Trigger decks: Human-centric, Innovation, Graphic Design, Storytelling and Business Design.

## Evidence cautions

- perceived authorship must be tested directly;
- more user effort does not automatically improve ownership;
- explanation quality depends on relevance, not quantity;
- proposal workflows can create friction if overused;
- AI-generated drafts may anchor users toward first suggestions;
- collaboration and conflict resolution require separate research.

---

## Imported source: `source_registry_addendum_R032_v0_1.md`

# Source Registry Addendum — R-032

**Дата:** 17 июля 2026

## Foundations

- Habit and automaticity research.
- Ritual, routine and symbolic-action traditions in anthropology and psychology.
- Self-determination and autonomy-supportive design traditions.
- Garden internal R-003, R-005, R-009, R-024, R-029 and R-031.
- Garden Trigger decks: Human-centric, Storytelling, Business Design, Innovation and Naming.

## Evidence cautions

- ritual definitions vary substantially across disciplines;
- meaningful repetition cannot be inferred from frequency alone;
- absence of logging is not evidence of absence of practice;
- some safety-critical routines genuinely require adherence support and belong to a separate product domain;
- streak effects vary by person and context;
- AI pattern detection can create false narratives and requires explicit consent;
- Garden principles are normative product decisions, not universal behavioral laws.

---

## Imported source: `source_registry_addendum_R033_v0_1.md`

# Source Registry Addendum — R-033

Foundations: autobiographical-memory and reconstructive-memory traditions; HCI work on digital memories and resurfacing; privacy, provenance and deletion principles; Garden R-024, R-028, R-029, R-031 and R-032; relevant Trigger decks.

Cautions:

- digital records are not equivalent to human memory;
- semantic search may infer beyond user language and requires grounding;
- resurfacing can be welcome for some people and harmful for others;
- emotional meaning cannot be reliably inferred from media;
- rejection of knowledge graphs is a Garden product boundary, not a universal design rule;
- painful-memory safety requires dedicated user research.

---

## Imported source: `source_registry_addendum_R034_v0_1.md`

# Source Registry Addendum — R-034

**Дата:** 17 июля 2026

## Foundations

- Information architecture distinctions between hierarchy, graph and faceted structures.
- Situated and spatial interaction traditions.
- Product-boundary and bounded-context principles.
- Garden internal R-027, R-028, R-030, R-032 and R-033.
- Garden Trigger decks: Human-centric, Graphic Design, Innovation, Business Design and Naming.

## Evidence cautions

- graph interfaces can be useful in knowledge-management products;
- spatial composition does not replace semantic organization in all domains;
- Garden’s restricted relation model is a deliberate product boundary;
- user-created tags can still expand into informal ontology and require monitoring;
- future Garden–«Нити» interoperability requires consent, provenance and deletion research;
- relation limits should be validated against real retrieval tasks.

---

## Imported source: `source_registry_addendum_package_09_v0_1.md`

# Source Registry Addendum — Package 09

Domains: privacy by design, least privilege, data portability, collaborative authorship, humane notifications, emotional AI risk, progressive disclosure and bounded product architecture.

Cautions: privacy promises require implementation and legal review; emotional safety cannot be solved through copy alone; shared ownership and crisis handling require specialist review; Alpha exclusions must be enforced in architecture.
