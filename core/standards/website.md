---
standard: website
title: Website structure
scope: shared
applies_surfaces: [website]
applies_outputs: [landing-page, home-page]
conformance: file
conformance_headings: [Conformance]
conformance_table: [Required element, Location, Status, Deviation]
grace_until: 2026-12-13
owner: @liam
last_reviewed: 2026-09-14
review_every: 180d
status: active
source: Communications Strategy & Architecture (1.1.4 Voices, Commercial boundary); home-assistant.io footer as the reference implementation
---

# Website structure

What every project website has, and what a project site never does. Exists so a person moving between project sites recognises the organisation, and so a site never speaks in the wrong voice. Required elements marked TODO were not settled by the source documents and need the marketing team.

## Required elements
- Attribution to the Open Home Foundation in the footer, using the approved wording from `core/voices.md`, naming the foundation as a non-profit and its three principles.
- The project's one-line boilerplate visible on the home page, verbatim from `brand/messaging.md`.
- Entry points to the community spaces listed in `marketing/channels.md`.
- Entry points to release notes or changelog and to the blog, where the project has them.
- Privacy-respecting analytics only; the analytics provider named on the site or in its privacy statement.
- TODO: required top-level navigation and its order.
- TODO: required legal pages (privacy, terms, trademark).

## Rules
### Product on the project site, cause on the foundation site
A project site talks about its product. Advocacy, industry commentary and praise or criticism of others live on openhomefoundation.org. Because the two kinds of trust must not mix (`core/voices.md`).
- Yes: "Home Assistant keeps your data local. No need for a cloud."
- No: "Unlike Big Tech, we believe your data belongs to you."

### Commercial partners are named as partners
Hardware and services from commercial partners may be promoted on the project site in the project's voice, and the partner is named as a partner, never as the owner. Because promotion follows the brand licence (`core/voices.md`, Commercial boundary).
- Yes: "Nabu Casa makes official Home Assistant products."
- No: "Buy from us."

## Never
- Foundation advocacy voice and a product, hardware or store item in the same block.
- A competitor named critically.
- Tracking or affiliate links.

## Machine checks
| Check | How | Fix |
|---|---|---|
| Footer attribution present | search footer for "Open Home Foundation" and "non-profit" | add approved wording |
| Boilerplate verbatim | diff hero or intro copy against `brand/messaging.md` One line | copy, do not paraphrase |
| Banned words | list in `core` | the specific thing |
| Competitor named | list of names, critical context | route to foundation voice or remove |
