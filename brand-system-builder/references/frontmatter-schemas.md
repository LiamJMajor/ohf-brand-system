# Frontmatter schemas

Every markdown file in the brand system carries YAML frontmatter. The audit script checks these. Keep values simple: strings, dates as `YYYY-MM-DD`, lists as `- item` lines.

## Skill (`skills/<name>/SKILL.md`)
```yaml
---
name: write-release-post           # matches folder name
description: >                      # what it does AND when to trigger; see trigger-writing-guide.md
  ...
owner: @handle
reliability: production | beta | draft
last_reviewed: 2026-09-14
---
```

## Project manifest (`projects/<slug>/PROJECT.md`)
See `project-spec.md`. Fields: name, slug, tier, voice, status, owner, maintainers, repo, website, pillars, related, last_reviewed.

## Core or project file (`core/*.md`, `projects/<slug>/*.md`)
```yaml
---
area: voice                        # story | pillars | voices | escalation | channels | naming | voice | messaging | audiences | modes | visual
project: core | <slug>
owner: @handle
last_reviewed: 2026-09-14
review_every: 180d
draft: false                       # true while drafted from public sources, before the maintainer interview
---
```

## Truth (`truths/<slug>/*.md`, `truths/core/*.md`)
```yaml
---
project: home-assistant            # or core
topic: proof-points                # proof-points | current-release | <topic>
valid_from: 2026-09-03
review_by: 2026-10-01
source: https://github.com/home-assistant/core/releases/tag/2026.9.0
owner: @handle
auto_updated_by: sync-truths       # omit if hand-maintained
---
```
A truth past `review_by` is stale and the audit reports it.

`proof-points.md` bodies are a table with columns **Claim | Canonical figure | Source | Pillar | Approved phrasing | Verified**. Skills copy Approved phrasing verbatim. A row with Verified empty or "Never" fails the audit.

## Example (`examples/<slug>/<type>/*.md`)
```yaml
---
type: release-post                 # matches a skill name where one exists
project: esphome
date: 2026-08-20
source_url: https://...
mode: quiet | standard | loud
why_it_works:
  - Opens with the user's problem, not the feature name
  - Every claim links to a doc page
  - Under 400 words
tags: [launch, firmware]
---
```
`why_it_works` needs at least two concrete observations. "Great tone" fails audit.

## Eval cases (`skills/<name>/evals/cases.md`)
```yaml
---
skill: write-release-post
rubric: evals/rubrics/on-brand.md
---
```
Body: one `## Case: <slug>` section per case, each with `**Prompt:**`, `**Must include:**` (list), `**Must not include:**` (list), and optional `**Notes:**`. See `templates/eval-cases.template.md`.

## Decision (`decisions/YYYY-MM-DD-<slug>.md`)
```yaml
---
date: 2026-09-14
area: voice
project: home-assistant            # or core
trigger: slack | review | audit | release | interview
change: Added rule against "seamless"
affected:
  - projects/home-assistant/voice.md
  - skills/write-release-post/SKILL.md
by: @handle
---
```
