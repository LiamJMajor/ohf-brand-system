# Open Home Foundation brand system: index

The only file loaded before a task starts. One line per entry: what it is, when to load it. Budget 60 lines. Projects are never listed here; use the registry.

## Core (shared by every voice; load story and pillars for anything public)
- `core/story.md`: the single thread. Load when framing anything.
- `core/pillars.md`: the beliefs every output must serve. Load to name the pillar before shipping.
- `core/voices.md`: foundation voice vs project voice, and the product-or-cause test. Load first for any output.
- `core/escalation.md`: what needs a human. Load before producing any output.
- `core/channels.md`: channel classes and purposes. Load when choosing where something goes.
- `core/standards/`: one file per standard (website, docs, social profiles, search, and whatever the marketing team adds). Load those whose `applies_outputs` or `applies_surfaces` match the task.

## Projects (one directory per voice, all the same shape)
- `projects/REGISTRY.md`: find the project slug, tier and status here. Then load `projects/<slug>/PROJECT.md`, which lists that project's files and its open gaps.
- `projects/<slug>/brand/`: voice (rules and modes), style (mechanics), messaging, naming, audiences, story, strategy. Load voice and style for anything written.
- `projects/<slug>/design/`, `marketing/`, `standards/`: load only when the task needs them. Build only against status `live`, in the areas listed in `ready:`.

## Truths (dated facts; cite by path, copy approved phrasing verbatim)
- `truths/<slug>/proof-points.md` and `current-release.md`: per project. A row with Verified empty is not usable.
- `truths/core/proof-points.md`: facts belonging to no single project. Currently empty by design; the foundation's own facts live under `truths/open-home-foundation/`.

## Examples (load two or three before drafting, matching the project and output type)
- `examples/<slug>/<type>/`: annotated approved work. Load these *before* writing, not as a check afterwards; they carry register and mechanics no rule file states.
- If the directory is empty, say so in the output. Do not infer one surface's voice from another's: a project's blog register does not predict its social register.

## Skills (self-serve workflows, parameterised by project)
- `skills/write-release-post/SKILL.md`: TODO one line on what it produces and when to use it.

## Governance
- `OWNERS.md`: routes for escalation.
- `evals/rubrics/on-brand.md`: how every output is graded.
- `decisions/`: why things are the way they are. Search before proposing a change.
