# Working in the OHF brand system

This repository is loaded by agents and maintained by people. Read `INDEX.md` first; it is the only always-loaded file and tells you what to open for a given task.

## If you are building something (a post, a page, a deck)
You do not need a clone. Install the `ohf-brand-system` plugin from the marketplace and refresh it; that is the current `main`. If you are reading this in a clone, run `git pull --ff-only origin main` first.
Find the project in `projects/REGISTRY.md`. Build only against status `live`, and only in the areas listed in its `ready:`. Load `core/voices.md` and decide the voice first. Name the pillar. Copy boilerplate verbatim. Cite truths by path. Load every `core/standards/*.md` that matches your output type. Every Home Assistant output currently requires a human sign-off before publishing.

## If you are maintaining the system
Use the `brand-system-builder` plugin: `onboard-project`, `capture-judgment`, `harvest-examples`, `sync-truths`, `codify-workflow`, `define-standard`, `evaluate-skill`, `promote-correction`, `audit-brand-system`. It lives in its own repository. Install it once with `/plugin marketplace add LiamJMajor/brand-system-builder` then `/plugin install brand-system-builder@brand-system-builder`.

## Rules for changes
- Before anything: `git fetch origin && git switch -c <type>/<slug> origin/main`. Never work on a stale main; the scripts warn if you are behind.
- Work on a branch. Open a pull request to `main`. The reviewer is the area owner in `OWNERS.md` or the project owner in `REGISTRY.md`.
- Run the validator before committing: `python3 ~/.claude/plugins/cache/brand-system-builder/brand-system-builder/*/scripts/validate_project.py <slug>` (the installed builder's scripts; or a clone of the builder) from anywhere inside this clone. Run the audit for anything touching `core/` or `core/standards/`.
- Every change that alters a rule, a fact or a standard gets a `decisions/YYYY-MM-DD-<slug>.md` entry in the same pull request.
- Never restate a truth; cite `truths/<slug>/...`. Never copy core content into a project; project files hold only the project's own translation.
- Project names are never shortened.

## Layout
`core/` shared story, pillars, voices, escalation, channels, standards. `projects/<slug>/` one identically shaped directory per voice: brand, design, marketing, standards. `truths/` dated facts. `examples/` annotated approved work. `skills/` self-serve workflows per beat. `decisions/` why things are the way they are.
