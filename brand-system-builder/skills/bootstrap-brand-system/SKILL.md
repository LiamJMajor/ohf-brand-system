---
name: bootstrap-brand-system
description: >
  Scaffold a new org-wide brand system repository with the shared core, the project registry, the always-loaded index, owners, escalation, rubric, plugin manifest and first skill stubs, optionally seeded from an org's comms strategy. Use this whenever someone wants to start, set up, scaffold, initialise or create a self-serve brand, comms or knowledge repo, asks "where do we begin", or wants to bring an existing guidelines doc into an agent-loadable layout. Do not use it to add a project (onboard-project) or a skill (codify-workflow) to an existing repo.
---

# Bootstrap brand system

Create the skeleton every other builder skill writes into. Run once per organisation. The output is honest about what it does not yet know: every stub carries a TODO and an owner.

## Before scaffolding
Get these from the conversation or ask. Do not guess owners.
1. **Org name** and target directory. Do not create a remote repo unless asked.
2. **Source material**: anything the organisation already has that says who it is. A comms strategy is ideal but rare. A mission statement, brand guidelines, a style guide, a pitch deck, an annual report, the website's about page, a founder's talk transcript: any of these works, and several together work better. Read what is given and distil it into a seed under `${CLAUDE_PLUGIN_ROOT}/seeds/<org>/`: `story.md` (what the org fights for, in a line), `pillars.md` (the beliefs everything must serve), `voices.md` (who speaks about what), `escalation.md` (what needs a human), `channels.md` (what each class of channel is for), and a `projects.csv` of the projects to register. Where the sources are silent, the seed file keeps the template's TODO with an owner; never invent. Record which source each file came from in its frontmatter `source:` field. If a seed for this org already exists, use it and add to it.
3. **Owners** for core, truths and skills. One handle each.
4. **The two or three requests that clog the queue most.** These become skill stubs.

## Steps
1. Scaffold:
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/scaffold.py <dir> --org "<Org>" --seed <seed> --skills write-x,build-y --owners core=@h,truths=@h,skills=@h
   ```
   With a seed, the projects in its `projects.csv` are registered at status `registered`.
2. Read the generated `core/` files. Fill any TODO the conversation already answers. Leave the rest with the owner's handle.
3. Read `INDEX.md`. Confirm each line says what the entry is and when to load it. It never lists individual projects; that is the registry's job.
4. Baseline audit:
   ```
   python3 ${CLAUDE_PLUGIN_ROOT}/scripts/audit.py <dir>
   ```
   Expect warnings about drafts and TODOs. Expect no errors. Fix any error before reporting.
5. If the user wants git: init and one commit. Ask before pushing.

## Distilling a source into a seed
Read the whole document first. Then, for each seed file, pull only statements that are decisions: what the org believes, what it will and will not do, who speaks when, what needs sign-off. Adjectives without a consequence ("we are bold and approachable") are not seed material; note them in the seed README as candidates for `capture-judgment`. A guideline that is mostly voice and tone attributes yields a thin core and a long candidate list, and that is the correct outcome. Tell the user what the source did and did not settle.

## Report
What was created, as a short tree. Which projects are registered and at what tier. The next three actions: `onboard-project` for the foundation's own voice first (every project's pillar translation depends on it), then the flagship projects, then `codify-workflow` for the top queue item.

## Why this shape
`${CLAUDE_PLUGIN_ROOT}/references/target-repo-layout.md` and `project-spec.md`. Short version: a thin shared core, one identically shaped directory per project voice, dated truths, per-project examples, skills per beat that take the project as intake, and a decisions log.
