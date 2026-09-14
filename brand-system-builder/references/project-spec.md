# Project spec

The contract. Every project in the brand system has the same directory with the same files, the same headings and the same frontmatter, so an agent that has built for one project can build for any. The validator (`scripts/validate_project.py`) enforces this by machine. Consistency is not a review step; it is a failing check.

The organisation's own voice is a project directory too, with `voice: foundation` (or whatever the parent voice is called); it follows the same schema. One schema, one validator, one loop.

## Directory
```
projects/<slug>/
├── PROJECT.md        Manifest: metadata, tier, status, what this project serves
├── naming.md         Canonical names, forbidden variants
├── voice.md          How it sounds: sounds-like table, rules with contrast pairs, never
├── messaging.md      Messaging hierarchy: positioning, pillar translations, key messages, boilerplate
├── audiences.md      Who it speaks to and what they care about
├── channels.md       Channel, purpose, register, cadence
├── modes.md          What changes between Low, Medium and High impact
└── visual.md         Tokens, logo rules, asset locations
truths/<slug>/
├── proof-points.md   Claim, canonical figure, source, pillar, approved phrasing, verified
└── current-release.md
examples/<slug>/<type>/*.md
```

## Tiers
Not every project needs the full spec. Most of the hundreds are libraries and drivers with no comms beat of their own. The tier sets what is required.

| Tier | Who | Required files | Also required |
|---|---|---|---|
| `flagship` | Projects with their own release beat, community and channels | all eight, plus `truths/<slug>/proof-points.md` and `current-release.md` | at least 3 examples per active beat |
| `active` | Projects that get talked about but do not run beats | PROJECT, naming, voice, messaging, audiences, channels, `truths/<slug>/proof-points.md` | |
| `stewarded` | Everything else the organisation owns | PROJECT, naming, messaging (Positioning and Boilerplate only) | inherits core voice rules |

A project can move up a tier; the validator then reports the missing files.

## Status lifecycle
`PROJECT.md` carries `status`. The audit reports projects stuck in a stage for more than 30 days.

| Status | Meaning | Exit condition |
|---|---|---|
| `registered` | Directory created, manifest filled from public sources | Drafts of all required files exist |
| `drafted` | Files drafted from README, site, docs; marked as drafts | Maintainer interview done |
| `interviewed` | Rules and messaging confirmed with a maintainer | Validator passes with zero errors |
| `validated` | Passes validator | Owner signs off, examples filed for flagship |
| `live` | Agents may build against the ready areas | Fails validator or truth goes stale: drops to `validated` |

## Readiness per area
Words are usually confirmed before visuals, and a release post should not wait for a logo file. `PROJECT.md` carries `ready: [...]` listing the areas whose files are confirmed and TODO-free: `brand`, `design`, `marketing`, `standards`. The validator applies its TODO and draft checks only inside ready areas. `live` requires `brand` to be ready; other areas can follow. Each skill declares `requires_ready:`; a release post needs `brand`, a home page needs `brand` and `design`. A skill refuses a project that is live but not ready in an area it needs, and says which.

## PROJECT.md frontmatter
```yaml
---
name: Home Assistant
slug: home-assistant
tier: flagship            # flagship | active | stewarded
voice: project            # project | foundation
status: live
owner: @handle
maintainers: [@a, @b]
repo: https://github.com/home-assistant/core
website: https://www.home-assistant.io
pillars: [privacy, choice, sustainability]   # subset of core/pillars.md; messaging must translate each
related: [esphome, music-assistant]
ready: [brand, marketing]
last_reviewed: 2026-09-14
---
```
Body: one paragraph on what the project is, in the project's own voice. Then `## Files` listing which spec files exist and their state.

## Required headings per file
The validator checks for these `##` headings. Extra headings are allowed.

**naming.md**: `## Canonical`, `## Forbidden variants`.
**voice.md**: `## Sounds like` (table with rows Speaks about, Speaks to, Sounds like, Typically says, Never), `## Rules` (each rule an `###` with a `- Yes:` and a `- No:` line), `## Never`. Minimum three rules for `active` and `flagship`.
**messaging.md**: `## Positioning`, `## Pillar translations` (an `###` per pillar in PROJECT.md), `## Key messages` (an `###` per audience in audiences.md), `## Boilerplate` (`### One line`, `### 50 words`, `### 100 words`), `## We don't say`. Stewarded projects need only `## Positioning` and `## Boilerplate`.
**audiences.md**: an `##` per audience, each with `**Cares about:**` and `**Found on:**`.
**channels.md**: a table with columns Channel, Purpose, Register, Cadence.
**modes.md**: a table with rows Low, Medium, High and columns for what changes.
**visual.md**: `## Logo`, `## Colour`, `## Type`, `## Assets`.
**truths/<slug>/proof-points.md**: table with columns Claim, Canonical figure, Source, Pillar, Approved phrasing, Verified. Frontmatter per `frontmatter-schemas.md`.

## Word rules the validator applies everywhere
Banned in any boilerplate or key message: seamless, robust, powerful, cutting-edge, best-in-class, innovative, revolutionary, leverage, empower, next-generation. They describe nothing. The validator reports them; the fix is the specific thing.

## Inheritance
A skill building for a project loads `core/` first, then `projects/<slug>/`. Where a project file is absent (stewarded tier), the skill uses the defaults in `core/voices.md` for a project voice. A project file never contradicts `core/`; if it needs to, that is a decision for the core owner and goes through `decisions/`.

## Standards
Everything above is the fixed part of the spec. Standards are the extensible part. A standard is one markdown file with frontmatter the validator reads:

| Scope | Lives at | Per-project file | Applies to |
|---|---|---|---|
| `core` | `core/standards/<std>.md` | none | outputs and surfaces listed in `applies_outputs` / `applies_surfaces`; skills load it |
| `shared` | `core/standards/<std>.md` | `projects/<slug>/standards/<std>.md` with `conforms_to: <std>` | projects whose `surfaces`, `tier` or slug match the binding |
| `project` | `projects/<slug>/standards/<std>.md` with `scope: project` | it is its own file | that project only; listed in its `PROJECT.md` `standards:` |

Frontmatter fields: `standard`, `title`, `scope`, `applies_surfaces`, `applies_outputs`, `applies_tiers`, `applies_projects`, `applies_all`, `conformance` (file or none), `conformance_headings`, `conformance_table`, `grace_until`, `owner`, `last_reviewed`, `review_every`, `status` (active or example).

Body sections: Required elements, Rules (with pairs), Never, Machine checks. Skills load every standard matching their output type or destination surface and run its checks in review, so a new standard (SEO, captions, legal footer) changes agent behaviour the day the file lands, with no skill edit. Missing conformance is a warning until `grace_until`, an error after.

Projects declare `surfaces:` in `PROJECT.md` (`website`, `docs`, `social-profiles`, `app-stores`, `github`). Standards bind to surfaces, so a library with only `github` never sees the website standard.
