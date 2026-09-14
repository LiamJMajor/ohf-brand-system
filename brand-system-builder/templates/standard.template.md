---
standard: {{STANDARD}}
title: {{STANDARD_TITLE}}
scope: {{core|shared|project}}
# Binding (shared only). Any match applies. Leave the ones you do not need out.
applies_surfaces: [{{website, docs, social-profiles, app-stores, github}}]
applies_outputs: [{{blog-post, landing-page, social-post, deck, video}}]
applies_tiers: []
applies_projects: []
applies_all: false
# Conformance (shared only): file = each applicable project keeps projects/<slug>/standards/{{STANDARD}}.md; none = no per-project file
conformance: file
conformance_headings: [Conformance]
conformance_table: [Required element, Location, Status, Deviation]
grace_until: {{DATE_PLUS_90}}
owner: {{OWNER}}
last_reviewed: {{DATE}}
review_every: 180d
status: active
---

# {{STANDARD_TITLE}}

One paragraph: what this standard governs and why it exists. Name the failure it prevents.

## Required elements
What every conforming project or output must have. Each line is checkable by looking at the thing.
- TODO

## Rules
Decisions with reasons and contrast pairs, so people and agents can check a draft against them.

### TODO rule
TODO. Because TODO.
- Yes: "TODO"
- No: "TODO"

## Never
- TODO

## Machine checks
Rules a script or agent can apply before a human sees the draft.
| Check | How | Fix |
|---|---|---|
| TODO | TODO | TODO |

## How skills use this
Skills whose output type is in `applies_outputs`, or whose destination surface is in `applies_surfaces`, load this file in their "Context to load" step and run Machine checks and Required elements in their review step. No skill needs editing when this standard changes.
