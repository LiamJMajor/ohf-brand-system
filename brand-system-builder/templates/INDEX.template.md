# {{ORG}} brand system: index

The only file loaded before a task starts. One line per entry: what it is, when to load it. Budget 60 lines. Projects are never listed here; use the registry.

## Core (shared by every voice; load story and pillars for anything public)
- `core/story.md`: the single thread. Load when framing anything.
- `core/pillars.md`: the beliefs every output must serve. Load to name the pillar before shipping.
- `core/voices.md`: foundation voice vs project voice, and the product-or-cause test. Load first for any output.
- `core/escalation.md`: what needs a human. Load before producing any output.
- `core/channels.md`: channel classes and purposes. Load when choosing where something goes.
- `core/standards/`: one file per standard (website, docs, social profiles, search, and whatever the marketing team adds). Load those whose `applies_outputs` or `applies_surfaces` match the task.

## Projects (one directory per voice, all the same shape)
- `projects/REGISTRY.md`: find the project slug, tier and status here. Then load `projects/<slug>/PROJECT.md`, which lists that project's files.
- `projects/<slug>/`: naming, voice, messaging, audiences, channels, modes, visual. Load only the files the task needs. Build only against status `live`.

## Truths (dated facts; cite by path, copy approved phrasing verbatim)
- `truths/core/proof-points.md`: shared proof points for the foundation and the ecosystem.
- `truths/<slug>/proof-points.md` and `current-release.md`: per project.

## Examples (load two or three matching the project and output type)
- `examples/<slug>/<type>/`: annotated approved work. Fall back to a flagship project of the same voice type if empty.

## Skills (self-serve workflows, parameterised by project)
{{SKILL_INDEX_LINES}}

## Governance
- `OWNERS.md`: routes for escalation.
- `evals/rubrics/on-brand.md`: how every output is graded.
- `decisions/`: why things are the way they are. Search before proposing a change.
