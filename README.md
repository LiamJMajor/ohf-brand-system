# OHF Brand System

How the Open Home Foundation and its projects define their brand, voice, messaging and marketing practice in a form that people and AI agents can build to directly, without asking the marketing team each time.

## The problem this solves

The foundation stewards hundreds of projects. A handful, like Home Assistant, ESPHome and Music Assistant, have their own voice, audiences, channels and release cycles. Every one of them needs marketing: release posts, social, decks, pages, launch material. Today the knowledge of how each project should sound and what it may claim lives in people's heads and in documents that are read once. Requests queue up with the marketing team, or people make things without it.

A guidelines document cannot fix this. It describes a brand but cannot participate in the work, and it drifts the moment there are more than a few of them.

This repository fixes it differently. Every project's brand is written down in the same set of files with the same structure, machine-checked for consistency, and loaded by agents as context. Someone asks their agent for a release post, and the agent already knows the project's voice rules, its approved boilerplate, its verified facts, and what good looks like. The marketing team provides governance and inputs once; the system applies them every time.

## What is in this repository

```
ohf-brand-system/           The brand system itself. Everyone who contributes clones this.
brand-system-builder/       The Claude Code plugin that builds and maintains it. Installed, rarely cloned.
.claude-plugin/             Marketplace manifest so both can be installed as plugins.
```

### The brand system (`ohf-brand-system/`)

| Folder | What it holds |
|---|---|
| `INDEX.md` | The one file an agent loads before any task. It says what to open for what. |
| `core/` | What every voice shares: the story, the three pillars (privacy, choice, sustainability), who speaks when, what always needs a human, channel classes. Thin by design. |
| `core/standards/` | Organisation-wide practices, one file each: website structure, GitHub presentation, social profiles, search, and whatever the marketing team adds next. |
| `projects/<slug>/` | One directory per project, all the same shape: `brand/` (strategy, messaging, voice, style, naming, story, audiences), `design/` (logo, colour, type, imagery, motion, layout, templates, accessibility, tokens), `marketing/` (channels, beats, content, community, press, partners, events, measurement), `standards/` (how this project meets each shared standard). The foundation's own voice is a project here too. |
| `projects/REGISTRY.md` | Generated list of every project with tier, status and owner. Find a project here first. |
| `truths/` | Dated, sourced facts: proof points with approved phrasing, and the current release of each project. Agents cite these by path and copy the phrasing verbatim. |
| `examples/` | Approved past work, annotated with what makes it work and what not to copy, plus near-misses. |
| `skills/` | Self-serve workflows for recurring jobs, one per beat. The project is an input; the skill loads that project's directory to become its voice. |
| `decisions/` | Dated log of every rule added, fact changed and interview held, and why. |

### The builder (`brand-system-builder/`)

Ten skills and five scripts for maintaining the system. You install it as a plugin and then talk to Claude; the skills trigger from plain requests.

| Skill | Use it when |
|---|---|
| `onboard-project` | Adding a project, moving it up a tier, or unsticking one. Registers it, drafts every file from public sources, runs the interview, validates, goes live. |
| `capture-judgment` | Sitting with a maintainer to turn what they know into rules with examples. |
| `harvest-examples` | Filing a project's best work as annotated examples. |
| `sync-truths` | A release shipped or a fact needs re-verifying. |
| `define-standard` | Adding an organisation-wide practice such as SEO or captions, as one file. |
| `codify-workflow` | A request keeps coming through the queue and should become a self-serve skill. |
| `evaluate-skill` | Checking a skill produces usable output before people depend on it. |
| `promote-correction` | Someone fixed a draft and the fix should stick. |
| `audit-brand-system` | Monthly health check, and before any batch onboarding. |
| `bootstrap-brand-system` | Starting a brand system from scratch for another organisation. |

The scripts enforce the structure: `validate_project.py` checks a project against the spec, `audit.py` checks the whole repository, `new_project.py` registers a project, `build_registry.py` regenerates the registry. They find the repository from wherever they are run inside a clone.

## How it fits together

1. **Core is the source.** The story and pillars are the foundation's. Every project translates them into what its product concretely does about each one. A project never invents a pillar and never contradicts core.
2. **Every project has the same shape.** Same files, same headings, same frontmatter, so an agent's procedure is identical whether it is working on Home Assistant or a library nobody has heard of. Tiers decide how much is required: `flagship` projects fill everything, `active` ones the brand and channel essentials, `stewarded` ones only a manifest, naming, positioning and boilerplate.
3. **Consistency is a failing check, not a review opinion.** The validator refuses to let a project go live until its brand files have the required sections, every voice rule has a Yes and No example, every pillar has a translation, every audience has a key message, banned words are absent, and every proof point is verified.
4. **Readiness is per area.** A project can be live for its words while its design files are still drafts. Each skill declares which areas it needs, and refuses a project that is not ready in one of them.
5. **Facts are dated.** A proof point carries its source, its approved phrasing and the date it was verified. Undated is unusable.
6. **Standards are extensible.** Adding an organisation-wide practice is one file with frontmatter saying what it applies to. The validator, the audit and every skill pick it up the day it lands.
7. **Every correction becomes a commit.** When someone fixes a draft, the fix goes into the right file with a decision entry, so the same mistake is not made twice.

## Getting started

### I want to build something for a project

You do not need a clone. Read `ohf-brand-system/INDEX.md`, find the project in `projects/REGISTRY.md`, and build only against projects with status `live`, in the areas listed under `ready:`. Decide the voice first using `core/voices.md`: is this about a product (project voice) or the cause (foundation voice)? Name the pillar it serves. Copy boilerplate from `brand/messaging.md` verbatim. Cite facts from `truths/`. Load every standard in `core/standards/` that matches your output type.

Self-serve skills for recurring beats (release post, socials, release party promotion) are being codified now and will be installable as the `ohf-brand-system` plugin. Until then, agents follow the files directly. Every Home Assistant output currently requires a human sign-off before publishing.

### I want to add or maintain a project

Install the builder once, from a Claude Code terminal:

```
/plugin marketplace add LiamJMajor/ohf-brand-system
/plugin install brand-system-builder@ohf-brand-system
```

Clone the repository and open Claude Code inside the brand system folder:

```bash
git clone git@github.com:LiamJMajor/ohf-brand-system.git
cd ohf-brand-system/ohf-brand-system
claude
```

Then say what you want: "onboard ESPHome", "audit the brand system", "add an SEO standard". The skill does the work on a branch, runs the validator, and ends by offering to commit. Push the branch and open a pull request; the reviewer is the owner named in the registry or in `OWNERS.md`.

Before writing anything, start from the current remote so your clone's age does not matter:

```bash
git fetch origin && git switch -c onboard/<slug> origin/main
```

The scripts warn if your checkout is behind `origin/main` or if you are editing on `main` directly.

### I am on the marketing team

You own governance. Three things are yours:

- **Approve.** Files drafted from public sources are marked `draft: true` until someone from the team reads them and confirms. Interviews happen with a project maintainer and take about six short rounds.
- **Set standards.** Anything that should apply across projects or outputs goes in `core/standards/` through `define-standard`. Write the rules as decisions with Yes and No examples, and give each at least one check a machine can run.
- **Review pull requests** for your area, and read the monthly audit report.

## Current state

| Project | Tier | Status | Ready areas |
|---|---|---|---|
| Home Assistant | flagship | live | brand |
| Open Home Foundation | flagship | registered | |
| ESPHome | flagship | registered | |
| Music Assistant | flagship | registered | |

Home Assistant was onboarded first, from its README, site, release posts, design tokens and documentation style guide, then confirmed with the marketing team over six interview rounds. Its brand area is live; design and marketing are drafts awaiting the team. Three release-post examples and one near-miss are filed. The first self-serve skill, the release beat, is the next piece of work.

The foundation's own voice should be onboarded next, because every project's pillar translations depend on it and several rules from the interviews are waiting to be applied to core.

## Rules for changes

- Work on a branch from `origin/main`. Open a pull request. Never commit to `main` directly.
- Run the validator before committing. A change that leaves a live project failing is not made.
- Every rule, fact or standard change gets a `decisions/` entry in the same pull request.
- Never restate a fact; cite `truths/`. Never copy core content into a project.
- Project names are never shortened. "Home Assistant", never "HA".

## Glossary

| Term | Meaning |
|---|---|
| Voice | Who is speaking: the foundation (about the cause) or a project (about its product). |
| Pillar | One of the three beliefs every output must serve: privacy, choice, sustainability. |
| Tier | How much of the spec a project must fill: flagship, active, stewarded. |
| Status | Where a project is in onboarding: registered, drafted, interviewed, validated, live. |
| Ready | The areas of a live project whose files are confirmed and complete: brand, design, marketing, standards. |
| Truth | A dated, sourced fact an agent may state. |
| Proof point | A truth with a canonical figure, a pillar, and approved phrasing to copy. |
| Standard | An organisation-wide practice that applies to outputs or projects, defined in one file. |
| Contrast pair | A rule shown as a Yes example and a No example, so it can be checked. |
| Near-miss | An example of work that was almost right, filed with what was wrong and the fix. |
| Beat | A recurring communication cycle, such as a release: several outputs on a schedule. |

## Where the ideas come from

The comms strategy that defines the shared core is the foundation's Communications Strategy & Architecture document. The framing of brand as software, where guidelines cannot participate in the work but a system can, comes from Paul Jun's 2026 essay of that name. Taste remains human. Repetition becomes software.
