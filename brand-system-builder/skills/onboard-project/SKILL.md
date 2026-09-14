---
name: onboard-project
description: >
  Bring a new project into the brand system so it has the same voice, messaging hierarchy, audiences, channels, naming and proof points as every other project, in the same files with the same headings. Use this whenever someone wants to add, register, onboard or set up a project (or a standard, driver, library, or the foundation itself), asks "how do we define the brand for X", wants X's voice or messaging written down, or says a project "needs the same treatment as Home Assistant". Also use it to move a project up a tier or unstick one in the pipeline. Do not use it to turn a recurring request into a skill (codify-workflow).
---

# Onboard project

Every project gets the same directory, the same files, the same headings. The spec is `${CLAUDE_PLUGIN_ROOT}/references/project-spec.md`; read it once before onboarding anything. The validator enforces it, so consistency is a failing check rather than a review opinion. This skill walks a project through the status lifecycle: registered, drafted, interviewed, validated, live.

## Where the repo is
The brand system is the current working directory or the nearest parent containing `INDEX.md`, `core/` and `projects/`; the scripts find it the same way when given no path. If the user is not inside a clone, get them into one before writing anything. Before the first write: `git fetch origin && git switch -c <type>/<slug> origin/main`, so the work starts from the current remote regardless of the clone's age. Finish with a commit and a pull request to the area owner. Read `${CLAUDE_PLUGIN_ROOT}/references/working-in-the-repo.md` for the flow.

## Intake
1. **Project**: name, GitHub repo, website. Look up what you can from the repo before asking.
2. **Tier**: `flagship` (runs its own beats and channels), `active` (gets talked about), `stewarded` (everything else). Suggest one from the repo's activity and whether it has its own blog or social. Confirm.
3. **Voice**: `project`, unless this is the foundation itself.
4. **Owner** and one or two **maintainers** to interview.
5. **Pillars** it serves, from `core/pillars.md`. Default: all. A project that serves none is a stewarded registry entry, not a voice.

## Stage 1: register
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/new_project.py <repo> --slug <slug> --name "<Name>" --tier <tier> --voice <voice> --owner @h --repo <url> --website <url> --pillars a,b,c
```
This creates `projects/<slug>/` from the spec templates for the tier, a conformance file under `projects/<slug>/standards/` for every shared standard that binds to the project's surfaces or tier, `truths/<slug>/`, `examples/<slug>/`, a decision entry, and regenerates `projects/REGISTRY.md`. Status is `registered`. Pass `--surfaces website,docs,github` for what the project actually has; standards bind to surfaces, so this decides which conformance files appear.

## Stage 2: draft from public sources
Read the README, the website's about and docs landing pages, the latest release notes, and the repo description. From these, fill every draft file with what is checkable. Mark everything `draft: true`. Specifically:
- `PROJECT.md`: the one paragraph, in the project's own register.
- `naming.md`: canonical name and capitalisation as the project itself writes it; forbidden variants you saw in the wild.
- `messaging.md`: Positioning from the README's first paragraph, rewritten to pass the swap test in `${CLAUDE_PLUGIN_ROOT}/references/messaging-hierarchy-guide.md`. Pillar translations from features that demonstrably serve each pillar. Boilerplate at all three lengths. Every fact you state goes into `truths/<slug>/proof-points.md` with its source and Verified left empty.
- `audiences.md`: from who the docs address.
- `channels.md`: from the links in the README footer and site nav.
- `standards/<std>.md` conformance files: for each required element in the standard, record where the project meets it today, or `missing`.
- `voice.md`: the Sounds-like table from how the project's own blog and release notes read. Rules: draft candidates only, each with a real Yes from their writing and a No you construct. Mark each `(draft)`.
Set status `drafted`. Do not invent. A TODO is better than a guess; the interview fills it.

For `stewarded` projects, stop after Positioning, Boilerplate and naming. Set status `drafted`, then run the validator and move to `validated` if it passes. No interview.

## Stage 3: interview the maintainer
Run `capture-judgment` scoped to this project, with the drafted files open. The interview confirms or rejects each draft rule, supplies the contrast pairs, fills modes, and gives the examples to harvest. Set status `interviewed`. Set `draft: false` on files the maintainer confirmed.

## Stage 4: validate
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/validate_project.py <repo> <slug>
```
Fix every error. Errors are mechanical: a missing heading, a rule without a No, a pillar with no translation, a banned word, an unverified proof point. Verify proof points against their sources and fill the Verified date. Rerun until zero errors. Set status `validated`.

## Stage 5: go live, area by area
Readiness is per area. When the brand files are confirmed and TODO-free, set `ready: [brand]`; that is the minimum for `live`. Add `marketing`, `design` and `standards` as each is finished; the validator only demands zero TODOs inside areas listed as ready. For `flagship`: run `harvest-examples` until at least three examples exist. Owner signs off in a `decisions/` entry. Set status `live` and `last_reviewed` today. Regenerate the registry:
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/build_registry.py <repo>
```
Only `live` projects may be built against by skills.

## Moving up a tier
Change `tier` in `PROJECT.md`, run the validator, and it lists exactly what is missing. Run stages 2 to 5 for the missing files only.

## Batch onboarding
For dozens of stewarded projects at once: a CSV with slug, name, tier, voice, repo, website, pillars, then `new_project.py` per row, then stage 2 per project from README only, then validate `--all`. Report the count that passed and the list that did not with their first error.

## Report
Slug, tier, status reached, validator result, files still marked draft, proof points still unverified, and what unblocks the next stage.
