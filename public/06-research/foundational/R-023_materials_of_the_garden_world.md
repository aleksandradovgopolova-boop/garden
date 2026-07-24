---
title: "R-023 — Материалы мира Garden"
status: accepted
owner: "Research"
updated: 2026-07-18
review_cycle: quarterly
source_of_truth: false
---

# R-023 — Материалы мира Garden

**Версия:** 0.1  
**Дата:** 16 июля 2026  
**Статус:** design research / material language  
**Контур:** Garden Atlas → Materials / Objects / Architecture

---

## 1. Главный вопрос

> Как сделать цифровой мир Garden ощутимым через дерево, камень, воду, стекло, металл, ткань, керамику, бумагу и землю — не уходя в фотореализм, культурные стереотипы, ложную «натуральность» и наказание через визуальный распад?

---

## 2. Главный вывод

Материал воспринимается не через одну текстуру.

Человек считывает материал по сочетанию:

- формы;
- контура;
- отражения;
- шероховатости;
- прозрачности;
- движения;
- деформации;
- цвета;
- света;
- масштаба;
- знакомого контекста;
- ожидаемого веса и температуры.

Исследования visual material perception показывают, что человеческая зрительная система быстро распознаёт материальные свойства, хотя восстановить реальные физические параметры из изображения часто невозможно. Восприятие использует характерные визуальные признаки и типичные модели внешнего вида, а не точную физическую реконструкцию.

### Garden position

> **Материал должен быть убедительным по поведению, а не максимально реалистичным по количеству пикселей.**

---

## 3. Material identity is relational

Дерево выглядит деревом не только из-за древесного рисунка.

Нужны согласованные признаки:

- матовая или полуматовая поверхность;
- направленная структура волокон;
- характерная кромка;
- мягкое рассеивание света;
- ожидаемая масса;
- реакция на воду и время;
- подходящий звук или анимация взаимодействия.

Если текстура говорит «дерево», а свет, движение и масштаб говорят «пластик», материал ощущается ненастоящим.

### Principle

> **Visual, motion, sound and interaction cues should tell the same material story.**

---

## 4. Vision and imagined touch

Visual and haptic perception are not isolated.

Research shows:

- visual information can change roughness discrimination;
- touch can alter perceived gloss;
- visual and haptic object representations can converge;
- people can infer probable softness, hardness, weight and friction from appearance.

Garden is mostly screen-based, but it can support **visual haptics** through:

- deformation;
- motion;
- resistance animation;
- sound;
- scale;
- contact shadows;
- cursor or haptic response where available.

### Limitation

Garden cannot claim that a rendered texture reproduces real touch.

---

## 5. Roughness, gloss and softness

### Roughness

Signals may include:

- microcontrast;
- irregular highlights;
- edge breakup;
- shadow structure;
- motion under changing light.

### Gloss

Gloss perception depends on:

- specular highlights;
- surface roughness;
- shape;
- illumination;
- viewpoint;
- contextual expectations.

More reflection does not automatically mean more convincing gloss.

### Softness

Softness may be communicated through:

- rounded deformation;
- slow recovery;
- folds;
- diffuse light;
- low-frequency motion.

### Garden rule

Do not exaggerate every material property.

A world in which:

- all stone is extremely rough;
- all glass is mirror-like;
- all fabric is fluffy;
- all metal is shiny

looks synthetic and visually exhausting.

---

## 6. Stylisation vs photorealism

Photorealism can create:

- strong material recognition;
- immersive detail;
- visual prestige.

But it also creates:

- high production cost;
- expectation of physical accuracy;
- uncanny mismatch;
- greater hardware demands;
- visual noise;
- difficulty maintaining accessibility;
- less room for imagination.

Extreme stylisation can create:

- clarity;
- distinctive identity;
- performance efficiency;
- coherent abstraction.

But it can erase:

- weight;
- tactile difference;
- material history;
- meaningful imperfection.

### Garden position

Use **materially legible stylisation**:

- simplified geometry;
- controlled textures;
- clear material response;
- limited microdetail;
- consistent light behavior;
- readable silhouettes.

---

## 7. Material hierarchy

Not every object needs equal detail.

### Primary materials

Define world identity and appear often:

- wood;
- stone;
- soil;
- water;
- vegetation.

### Secondary materials

Add contrast and personal expression:

- ceramic;
- fabric;
- glass;
- metal;
- paper.

### Rare/special materials

Must not create status hierarchy:

- fictional luminous materials;
- unusual minerals;
- crafted composites.

### Alpha recommendation

Start with five primary materials and three secondary materials.

---

## 8. Wood

Wood is often perceived as warm in architectural material research, but perceived warmth depends on:

- colour;
- grain;
- finish;
- visual context;
- actual thermal properties;
- prior association.

Garden must not claim wood improves wellbeing.

### Useful qualities

- directional grain;
- moderate irregularity;
- visible construction;
- warmth without orange overload;
- repairability;
- compatibility with age and personal marks.

### Risks

- “natural = ethical” assumption;
- cottage stereotype;
- cultural default;
- excessive brown world;
- premium handcrafted status.

### Garden use

Wood may support:

- benches;
- small structures;
- bridges;
- signs;
- tools;
- frames.

---

## 9. Stone

Stone can communicate:

- stability;
- weight;
- duration;
- coolness;
- geological variation.

But these are contextual associations, not universal meanings.

### Material cues

- mass;
- irregular fracture;
- controlled roughness;
- low deformation;
- varied mineral response;
- contact with soil and water.

### Risks

- every stone becoming memorial or spiritual;
- Japanese-garden shorthand;
- grey = lifeless;
- inaccessible low-contrast scenes.

---

## 10. Water

Water is a material and a dynamic system.

It communicates through:

- reflection;
- transparency;
- refraction;
- surface motion;
- depth;
- sound;
- interaction with light.

### Garden rules

- no excessive mirror reflection;
- no flashing highlights;
- motion respects reduced-motion mode;
- water remains visible in dark palettes;
- water is not an emotional score;
- ritual success does not make water clearer.

### Accessibility

Provide:

- static water;
- reduced shimmer;
- sound control;
- clear boundaries.

---

## 11. Glass

Glass can communicate:

- fragility;
- transparency;
- enclosure;
- reflection;
- modernity.

But glass-heavy UI and architecture may create:

- readability problems;
- unclear boundaries;
- visual coldness;
- glare;
- accessibility failures.

### Garden use

Glass is secondary.

Use for:

- greenhouse details;
- windows;
- vessels;
- small reflective accents.

Avoid:

- full glassmorphic interface;
- invisible controls;
- transparency as privacy metaphor.

---

## 12. Metal

Metal may suggest:

- precision;
- strength;
- craft;
- machinery;
- coldness;
- age.

Different metals behave differently.

Do not collapse:

- iron;
- copper;
- bronze;
- aluminium;
- steel

into one generic shiny surface.

### Garden use

- hardware;
- lanterns;
- hinges;
- tools;
- small structural details.

Metal should not dominate the world unless chosen by the user.

---

## 13. Ceramic

Ceramic may combine:

- hand-scale;
- form;
- colour;
- glaze;
- fragility;
- repair;
- domestic familiarity.

### Garden use

- pots;
- bowls;
- tiles;
- markers;
- small water elements.

### Risks

- cultural motifs without provenance;
- handmade look used as authenticity theatre;
- cracks coded as emotional damage.

---

## 14. Fabric

Fabric introduces:

- softness;
- movement;
- shelter;
- colour;
- domestic scale.

### Garden use

- cushions;
- awnings;
- flags without achievement logic;
- curtains;
- picnic textiles.

### Requirements

- motion optional;
- no constant flutter;
- no texture detail that creates visual noise;
- culturally identifiable patterns require review.

---

## 15. Paper

Paper connects Garden with:

- writing;
- notes;
- letters;
- maps;
- archives;
- temporary objects.

### Garden use

Paper should not imply that the entire world is a journal.

Possible forms:

- labels;
- folded note;
- ritual description;
- map;
- memory card.

### Accessibility

Text remains real UI text, not baked into texture.

---

## 16. Soil and earth

Soil grounds the garden but must not become:

- dirt as neglect;
- barren land as failure;
- fertile soil as personal potential;
- visual punishment after inactivity.

### Material cues

- varied granular surface;
- moisture states only when user-selected or ambient;
- stable readable value;
- relation to stones, plants and paths.

### Rule

No automatic dry/cracked earth after absence.

---

## 17. Natural, synthetic and sustainable

“Natural” is not equivalent to:

- sustainable;
- ethical;
- healthy;
- safe;
- beautiful.

Material sustainability depends on:

- source;
- processing;
- transport;
- durability;
- toxicity;
- maintenance;
- reuse;
- end of life.

In a digital world, a wood texture is not materially sustainable by itself. Rendering, hardware, energy and production practices remain relevant.

### Garden language

Do not call a digital aesthetic “eco-friendly” without lifecycle evidence.

---

## 18. Patina, ageing and memory

Patina can be understood as visible change produced by:

- time;
- environment;
- use;
- care;
- oxidation;
- wear.

Research on aesthetic appreciation of ageing shows mixed outcomes. Patina does not automatically increase attachment or reduce disposal. Preferences depend on material and form of change; decay can be disliked.

### Garden distinction

#### User-authored patina

Allowed:

- chosen wear;
- named memory;
- optional darkening;
- added repair mark;
- preserved transformation.

#### System-imposed decay

Forbidden:

- cracks after absence;
- rust after missed ritual;
- faded fabric after inactivity;
- dirt as neglect;
- broken object as failure.

### Principle

> **The world may remember use. It must not punish absence.**

---

## 19. Repair

Repair can communicate:

- continuity;
- care;
- history;
- change.

But visible repair must not become:

- forced symbolism;
- “broken person” metaphor;
- cultural borrowing without context;
- premium transformation.

### Garden use

The user may choose:

- repair mark;
- replacement;
- preserved crack;
- invisible restoration;
- no repair story.

AI does not propose repair as psychological meaning.

---

## 20. Material age

Objects can have:

- new;
- used;
- weathered;
- restored;
- timeless/stylised

appearance.

This is aesthetic choice, not lifecycle state.

A newly created ritual may use an old-looking object.

A completed ritual may retain a new-looking object.

---

## 21. Material consistency

Each material needs a specification across:

- colour range;
- roughness;
- reflectance;
- edge behavior;
- motion;
- sound;
- scale;
- ageing options;
- accessibility;
- performance budget.

### Example

```yaml
wood:
  colour_range:
  grain_scale:
  roughness:
  specular:
  edge_softness:
  sound_family:
  ageing_options:
  contrast_floor:
  reduced_detail:
```

---

## 22. Material and sound

Object interaction can be supported by subtle sounds:

- wood tap;
- stone placement;
- ceramic touch;
- paper movement;
- water contact.

### Rules

- sound optional;
- no loud reward sounds;
- material sound remains subtle;
- no essential feedback only through audio;
- culturally specific instruments are not generic object sounds.

---

## 23. Material and motion

Material motion should reflect expected behavior.

- fabric folds;
- water flows;
- foliage bends;
- stone remains stable;
- paper moves lightly;
- metal does not wobble like rubber.

Research on moving contours indicates that motion itself can provide diagnostic material information beyond static shape.

### Garden implication

One accurate motion cue may do more than a high-resolution texture.

---

## 24. Material and performance

Garden must work on modest devices.

### Progressive material fidelity

#### Level 0

- flat colour;
- silhouette;
- accessible label.

#### Level 1

- simple shading;
- low-resolution texture;
- static material.

#### Level 2

- normal/roughness detail;
- reflection;
- subtle motion.

#### Level 3

- enhanced light and material effects.

No level may remove core readability or meaning.

---

## 25. Material and accessibility

Provide:

- sufficient value contrast;
- non-texture labels;
- reduced visual complexity;
- no meaning based only on gloss;
- optional static surfaces;
- list mode;
- screen-reader material names;
- boundaries visible without shadows.

### Principle

A blind or low-vision user must not lose ritual ownership because the visual material system is unavailable.

---

## 26. Material system for Alpha

### Primary

- soil;
- wood;
- stone;
- water;
- vegetation.

### Secondary

- ceramic;
- fabric;
- metal.

### Defer

- complex glass architecture;
- advanced transparency;
- large reflective surfaces;
- procedural weathering;
- material crafting economy;
- rare material collections.

---

## 27. Alpha experiments

### A — Photoreal vs stylised legibility

Measure:

- material recognition;
- beauty;
- performance;
- visual noise;
- ownership.

### B — Texture vs motion cue

Test whether simple material with correct motion feels more convincing.

### C — Clean vs user-chosen patina

Measure:

- attachment;
- age interpretation;
- fear of decay;
- perceived judgment.

### D — Material families

Allow users to choose:

- woodland;
- mineral;
- domestic craft;
- mixed.

Do not label as personality.

### E — Low-fidelity accessibility

Test whether reduced-detail version feels intentional and complete.

---

## 28. Candidate principles

1. Material behavior before texture detail.
2. Cross-sensory consistency.
3. Materially legible stylisation.
4. Primary and secondary material hierarchy.
5. Natural does not mean ethical.
6. Patina is chosen memory, not punishment.
7. Repair has no fixed psychological meaning.
8. Material age is aesthetic, not ritual state.
9. Motion can communicate matter.
10. Accessibility does not depend on texture.
11. No rare-material status economy in Alpha.
12. Progressive fidelity preserves meaning.

---

## 29. What Garden must not claim

- wood improves wellbeing;
- stone creates stability;
- water reduces anxiety;
- natural materials are sustainable;
- patina always increases attachment;
- realistic texture reproduces touch;
- cultural craft motifs are universal;
- damaged appearance represents growth;
- clean materials represent success;
- digital material choice has no environmental cost.

---

## 30. Claim Registry

| Claim | Confidence | Status |
|---|---:|---|
| Humans rapidly infer material properties from visual cues | high | foundation |
| Exact physical material parameters can be recovered from appearance | low | rejected |
| Visual and haptic material information interact | high | foundation |
| Material motion can aid recognition | medium-high | design foundation |
| More texture detail always improves material perception | low | rejected |
| Wood is universally perceived as warm | medium/contextual | limited |
| Patina always improves aesthetic appreciation | low | rejected |
| Natural materials are necessarily sustainable | low | rejected |
| Materially legible stylisation can support Garden | design synthesis | candidate |
| User-authored wear may support memory | low | Alpha hypothesis |

---

## 31. Verdict

Garden should feel tangible without pretending to be physically real.

Its materials should provide:

- weight;
- softness;
- roughness;
- reflection;
- movement;
- history;
- difference.

But the material world never becomes a disciplinary system.

> **Objects may carry traces of chosen use. They never carry accusations about absence.**
