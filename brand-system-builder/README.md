# Brand System Builder

The system that builds the system.

An organisation that stewards many projects needs every project's brand defined the same way: voice, messaging hierarchy, audiences, channels, naming, proof points, in the same files with the same headings, so any agent can load `projects/<slug>/` and build to it with structure. Guidelines cannot do this; they describe a brand but cannot participate in the work, and they drift the moment there are more than a handful of them.

This plugin builds and maintains a repository that can. Two layers:

| Layer | What it is | Who uses it |
|---|---|---|
| **Builder** (this repo) | Ten skills, five scripts, a project spec, standards, templates and seeds | The brand team |
| **Brand system** (what it produces) | A thin shared core, one identically shaped directory per project, dated truths, annotated examples, self-serve skills per beat | Everyone in the org, through agents |

## The idea in one diagram

```
core/                    story, pillars, who speaks when, escalation, channel classes
core/standards/          extensible: website, docs, social, search, whatever is added next; one file each
  │  inherited by every voice
  ▼
projects/<slug>/         PROJECT.md  naming  voice  messaging  audiences  channels  modes  visual
  │  same files, same headings, enforced by validate_project.py; tiered; status lifecycle
  ▼
truths/<slug>/           proof points (claim, figure, source, pillar, approved phrasing, verified)
examples/<slug>/<type>/  annotated approved work
  │
  ▼
skills/<beat>/           one skill per beat, project as intake: loads the project's directory and becomes its voice
```

## Skills

| Skill | Use it when |
|---|---|
| `bootstrap-brand-system` | Starting the repo, optionally seeded from a comms strategy |
| `onboard-project` | Adding a project, moving one up a tier, unsticking one. Walks registered → drafted → interviewed → validated → live |
| `capture-judgment` | Interviewing a maintainer to confirm a project's rules, messaging and boundaries |
| `harvest-examples` | Filing a project's best work with concrete why-it-works notes |
| `sync-truths` | A release shipped, a proof point needs verifying |
| `codify-workflow` | A request keeps coming through the queue and should become a self-serve skill |
| `evaluate-skill` | Checking a skill produces usable output across projects before people depend on it |
| `promote-correction` | Someone corrected a draft and it should stick |
| `define-standard` | Adding an org-wide practice (SEO, accessibility, website structure) as one file every skill and the validator pick up |
| `audit-brand-system` | Monthly health check, and before any batch onboarding |

## Scripts (standard library Python)

| Script | Does |
|---|---|
| `scaffold.py` | Creates the repo; `--seed <org>` copies a distilled shared core and registers seed projects |
| `new_project.py` | Registers a project from the spec templates for its tier |
| `validate_project.py` | Enforces the project spec; `live` needs zero errors |
| `build_registry.py` | Regenerates `projects/REGISTRY.md` from the manifests |
| `audit.py` | Whole-repo health: index, registry, every project, truths, skills, examples, owners, duplication |

## Quick start

1. Install the plugin:
   ```
   /plugin marketplace add <your-org>/brand-system-builder
   /plugin install brand-system-builder
   ```
2. Gather whatever your organisation already has that says who it is: a mission statement, brand guidelines, a style guide, a comms strategy, a pitch deck, the about page. Any one of them is enough to start. Ask Claude to bootstrap the brand system from it. The `bootstrap-brand-system` skill distils the shared core (story, pillars, who speaks when, escalation, channels) from whatever it is given and marks the rest TODO with an owner.
3. Onboard your organisation's own voice first, as a project. Every other project translates the shared pillars into its own product benefits, so the shared layer has to exist before any project can.
4. Onboard your flagship projects one at a time: register, draft from public sources, interview one maintainer, validate, file three examples, go live.
5. Codify the single most common request as a skill. Evaluate it across two live projects. Give it to a small group. Measure how many outputs ship without a human rebuild.
6. Batch-onboard the long tail of stewarded projects from a CSV. Audit before and after.

A worked example: `seeds/open-home-foundation/` is one organisation's shared core, distilled from its communications strategy document. Use it as a reference for what a seed looks like, not as a template for your content.

## Read next

- [PRINCIPLES.md](PRINCIPLES.md): the rules everything here follows.
- [references/project-spec.md](references/project-spec.md): the contract every project meets.
- [references/target-repo-layout.md](references/target-repo-layout.md): the produced repo and why it is shaped that way.
- [references/messaging-hierarchy-guide.md](references/messaging-hierarchy-guide.md): how to write a messaging.md that agents can build from.
- [CONTRIBUTING.md](CONTRIBUTING.md): how to change this builder.

## Credit

The framing comes from Paul Jun's essay "Brand as software" (2026). Taste remains human. Repetition becomes software.
