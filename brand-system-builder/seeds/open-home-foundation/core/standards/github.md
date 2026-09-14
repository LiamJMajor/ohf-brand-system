---
standard: github
title: GitHub presentation
scope: shared
applies_surfaces: [github]
applies_outputs: [readme]
conformance: file
conformance_headings: [Conformance]
conformance_table: [Required element, Location, Status, Deviation]
grace_until: {{REVIEW_DATE}}
owner: {{CORE_OWNER}}
last_reviewed: {{DATE}}
review_every: 180d
status: active
source: home-assistant/core README as the reference implementation
---

# GitHub presentation

How a project's repositories present to someone arriving from GitHub. Exists so every repository the foundation stewards is recognisably part of one organisation.

## Required elements
- Repository description is the project's one-line boilerplate.
- README carries the Open Home Foundation badge or a sentence of attribution using approved wording.
- README links to the website, documentation, and the community entry point.
- Licence visible in the repository root.
- TODO: social preview image rule.
- TODO: code of conduct and contributing file requirements.

## Rules
### The README opens with what it is, not how to build it
Because most arrivals are deciding whether this is the thing they need. Build instructions come after.
- Yes: "Open source home automation that puts local control and privacy first."
- No: "## Installation\n```pip install ...```" as the first section

## Never
- A repository description that differs from the boilerplate.
- Attribution wording other than the approved form.

## Machine checks
| Check | How | Fix |
|---|---|---|
| Description equals One line boilerplate | compare via GitHub API | update description |
| Attribution present | search README for "Open Home Foundation" | add badge or sentence |
