---
standard: seo
title: Search best practices
scope: core
applies_surfaces: [website, docs]
applies_outputs: [blog-post, landing-page, home-page, docs-page]
conformance: none
owner: {{CORE_OWNER}}
last_reviewed: {{DATE}}
review_every: 180d
status: example
---

# Search best practices

An example of a core-scope standard: it applies to every output of the listed types, on every project, with no per-project conformance file. Skills that write pages or posts load it and run its machine checks. It ships as `status: example`; the marketing team replaces the content or deletes the file. The point is that adding a standard like this is one markdown file, and every skill picks it up.

## Required elements
- One H1 per page, matching the intent of the page title.
- Title tag under 60 characters, description under 160, both written for a person, not a keyword list.
- Descriptive link text; never "click here" or a bare URL.
- Alt text on every image (accessibility and search agree here).
- The project's search terms from `marketing/content.md` appear where they are natural, and nowhere they are not.

## Rules
### Write the title for the reader who has not arrived yet
The title is read in a results list before it is read on the page. Because that reader has no context.
- Yes: "How to control infrared devices with Home Assistant"
- No: "Infrared: first-class citizen"

### One page, one intent
A page answers one question. Because two intents on one page rank for neither.
- Yes: a page for installation and a page for hardware choice
- No: "Getting started and choosing hardware and FAQ"

## Never
- Keyword stuffing, hidden text, or copy written for a crawler rather than a person.
- Affiliate or tracking links (also a style rule).

## Machine checks
| Check | How | Fix |
|---|---|---|
| Exactly one H1 | count `<h1>` or `# ` | merge or demote |
| Title length | ≤ 60 characters | shorten |
| Meta description | present, ≤ 160 | write it for a person |
| Link text | no "click here", "here", bare URLs | describe the destination |
| Images | every `<img>` has alt | write alt or mark decorative |
