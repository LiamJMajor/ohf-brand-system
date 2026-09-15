# Working in the OHF brand system

This repository is loaded by agents and maintained by people. Read `INDEX.md` first; it is the only always-loaded file and tells you what to open for a given task.

## If you are building something (a post, a page, a deck)
You do not need a clone. Install the `ohf-brand-system` plugin from the marketplace and refresh it; that is the current `main`. If you are reading this in a clone, run `git pull --ff-only origin main` first.

In order:
1. Find the project in `projects/REGISTRY.md`. Build only against status `live`, and only in the areas listed in its `ready:`. If it is not live, you may still draft, but say so plainly in your output and name what you built from instead.
2. Load `core/voices.md` and decide the voice. Name the pillar.
3. **Load `examples/<slug>/<type>/` before you draft.** Two or three matching the project and output type. Examples carry register and mechanics that no rule file states, and a draft written without them will be wrong in ways the validator cannot catch. If the directory is empty, say so in your output rather than guessing from a neighbouring surface: a project's blog voice does not predict its social voice.
4. Load the project's `brand/voice.md` and `brand/style.md`. Voice carries the rules and modes; style carries the mechanics, which is where most rejections happen.
5. Copy boilerplate verbatim. Cite truths by path. A proof point with Verified empty is not usable, whatever else is true of it.
6. Load every `core/standards/*.md` that matches your output type.

Every Home Assistant output currently requires a human sign-off before publishing. No equivalent policy exists for the foundation voice; `core/escalation.md` governs it alone.

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
