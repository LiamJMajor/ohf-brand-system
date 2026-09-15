# Contributing to the Open Home Foundation brand system

This repo is loaded by agents. Write for them first. See the builder's PRINCIPLES.md for the full set.

## Fixing something
You saw a draft that was wrong and know the fix. Use the `promote-correction` skill, or by hand:
1. Decide what kind of fix it is: a fact (`truths/`), a rule (`core/` or `projects/<slug>/`), a skill instruction (`skills/<name>/SKILL.md`), or an example (`examples/`).
2. Make the change in that one place. Do not copy it anywhere else.
3. Add a `decisions/YYYY-MM-DD-<slug>.md` entry saying what changed and why.
4. Open a pull request. The area owner reviews.

## Adding a skill
Use the `codify-workflow` skill from the builder. It writes the skill, its evals and the index line. Skills land as `draft` reliability and move up after evaluation.

## Adding an example
Use `harvest-examples`, or follow `templates/example.template.md`. Two concrete `why_it_works` items minimum.

## What not to do
- Do not restate a truth inside a skill. Cite `truths/<brand>/<file>.md`.
- Do not put voice attributes in `core/`. Core holds story, pillars, who speaks when, escalation and channel classes. Voice lives in `projects/<slug>/`.
- Do not create a skill per project. Skills are per beat and take the project as intake.

## Adding a project
Use the `onboard-project` skill. Every project gets the same files per the spec; the validator enforces it. Nothing is hand-assembled.
- Do not add a rule from a single correction unless it would apply every time. Log the decision instead.
