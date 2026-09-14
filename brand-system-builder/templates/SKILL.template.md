---
name: {{SKILL_NAME}}
description: >
  {{WHAT_IT_DOES}} Use this whenever someone {{TRIGGER_PHRASES}}, even if they don't use those words.
  {{SIBLING_BOUNDARY}}
owner: {{OWNER}}
reliability: draft
requires_ready: [brand]     # project areas this skill needs; add design for anything visual, marketing for channel choices
last_reviewed: {{DATE}}
---

# {{SKILL_TITLE}}

{{ONE_PARAGRAPH_PURPOSE}}

## Intake
Collect these before producing anything. Look up what you can; ask only for what you cannot.
1. **Project**: the slug from `projects/REGISTRY.md`. Confirm its status is `live` and that its `ready:` list covers this skill's `requires_ready`. If not, say which area is missing and stop, unless the requester accepts a draft built on unconfirmed files.
2. **Voice**: apply the product-or-cause test in `core/voices.md`. Product: project voice. Cause: foundation voice (`projects/open-home-foundation/`).
3. **Pillar**: which of `core/pillars.md` this advances. If none, do not ship; say why.
4. **Audience**: one of the headings in `projects/<slug>/audiences.md`.
5. **Mode**: Low, Medium or High from `projects/<slug>/modes.md`. Default: {{DEFAULT_MODE}}.
6. {{INTAKE_ITEM}}

Check intake against `core/escalation.md`. If a trigger fires, stop, produce a clearly marked draft, name the route.

## Context to load
In this order, nothing else unless a step says otherwise:
1. `projects/<slug>/PROJECT.md`, then `voice.md`, `messaging.md`, and `naming.md`.
2. `truths/<slug>/{{RELEVANT_TRUTH}}.md` and `truths/<slug>/proof-points.md`. Cite by path. Copy approved phrasing verbatim.
3. Two or three files from `examples/<slug>/{{EXAMPLE_TYPE}}/` matching the mode. Read `why_it_works` first.
4. Every `core/standards/*.md` whose `applies_outputs` includes `{{EXAMPLE_TYPE}}` or whose `applies_surfaces` includes the destination surface, plus the project's conformance file for it under `projects/<slug>/standards/` if one exists. Standards are added by the marketing team without touching this skill; never hard-code their content here.

## Produce
{{PRODUCTION_STEPS}}

## Output
Deliver as {{OUTPUT_FORMAT}}. The requester must be able to edit it alone. Never a flattened image of text.

## Review before handing over
- [ ] Voice decided and stated. Pillar named.
- [ ] Every fact traces to a `truths/` path. Boilerplate copied, not paraphrased.
- [ ] Each contrast pair in `voice.md` checked against the draft.
- [ ] Nothing from `messaging.md` "We don't say". No banned words.
- [ ] Mode matches intake. No escalation trigger fired.
- [ ] Every loaded standard's Required elements present and Machine checks run.
- [ ] Rubric `evals/rubrics/on-brand.md` self-score stated.

## Known limits
{{KNOWN_LIMITS}}
Route anything outside these to the project owner in `PROJECT.md`.
