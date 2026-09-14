---
name: codify-workflow
description: >
  Turn a recurring request (release post, newsletter, hardware launch, community meetup, announcement, store product, deck, feature short) into an end-to-end self-serve skill that works for any live project: intake including project, voice and pillar; exact context to load; editable output; review checklist; escalation; eval cases. Use this whenever someone says a request "keeps coming up", wants to automate or template a beat, asks to make something self-serve, or wants to add a skill to the brand repo. Do not use it to write a project's rules (capture-judgment), add a project (onboard-project), or test an existing skill (evaluate-skill).
---

# Codify workflow

A skill in the brand system is a repeatable production path from settled decisions, parameterised by project. One skill per beat, never one per project: the project is intake, and the skill loads `projects/<slug>/` to become that project's voice. Writing per-project skills would multiply maintenance by the number of projects, and the layout forbids it.

## Preconditions
Before writing anything, check that at least one project is `live` in `projects/REGISTRY.md` with examples of this output type under `examples/<slug>/<type>/`. If none, say so and route to `onboard-project` and `harvest-examples` first. A skill built on drafts produces confident nonsense.

## Study the request
Find three or more real instances: Slack messages, tickets, Asana tasks. For each, note what the requester supplied, what the team had to go and find, what shipped, and what got corrected. Corrections become the review checklist. Things found become context-to-load. Things supplied become intake. If the org has a comms architecture with a manifest for this beat, its fields are the intake.

## When the request is a beat, not one output
A beat (a release, a hardware launch, a newsletter cycle) produces several artefacts on a schedule. Do not write one skill that produces everything; nobody can edit or evaluate that. Write one output skill per artefact (blog post, socials, party promotion, feature shorts) and one orchestrator skill that takes the beat's manifest as intake, applies the playbook's T-minus schedule, and calls the output skills in order, handing each the same manifest. Each output skill is evaluated alone. The orchestrator is evaluated on sequencing and on passing the right context, not on prose.

## Write the skill
Copy `${CLAUDE_PLUGIN_ROOT}/templates/SKILL.template.md` to `skills/<verb-first-name>/SKILL.md`.
- **Description**: `${CLAUDE_PLUGIN_ROOT}/references/trigger-writing-guide.md`. What it does, casual phrasings, sibling boundary by name.
- **Intake**: the template already asks project, voice (product-or-cause test), pillar, audience, mode. Add only what the requester alone knows.
- **Context to load**: exact paths under `projects/<slug>/` and `truths/<slug>/`. Boilerplate copied verbatim from `messaging.md`. Two or three examples by mode. Then every `core/standards/*.md` whose `applies_outputs` includes this skill's output type; the template already has this step. Never copy a standard's rules into the skill: the standard changes, the skill must not have to.
- **Produce**: the steps, with structural moves from the examples' `What to copy`.
- **Output**: editable. Markdown, HTML, PPTX, Google Doc. Never a flattened image of text.
- **Review**: the corrections as checkboxes, plus the rubric self-score.
- **Known limits**: cross-check `core/escalation.md`. Set `reliability: draft`.
Under 300 lines; detail into `skills/<name>/references/`.

## Write the evals
`${CLAUDE_PLUGIN_ROOT}/templates/eval-cases.template.md` to `skills/<name>/evals/cases.md`. At least three cases across at least two projects, so the skill is proven project-agnostic. Ten trigger cases: six that fire, four that should not, with the skill that should.

## Wire it in
One line in `INDEX.md` under Skills. `decisions/<date>-codify-<name>.md`: instances studied, corrections that became checks, limits chosen.

## Then evaluate
Run `evaluate-skill` before telling anyone the skill exists. Report its pass rate with the files written. Unevaluated means draft, and the report says so.
