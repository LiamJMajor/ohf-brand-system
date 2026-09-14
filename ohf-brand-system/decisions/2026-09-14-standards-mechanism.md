---
date: 2026-09-14
area: repo
project: core
trigger: review
change: Standards became declarations in core/standards/; surfaces/ conformance files moved to projects/<slug>/standards/
affected:
  - core/standards/
  - projects/*/standards/
  - INDEX.md
by: @liam
---

# Standards mechanism

Requirement from review: the marketing team must be able to add an org-wide practice (SEO was the example) without code or skill edits. A standard is now one markdown file with frontmatter declaring scope (core, shared, project), binding (surfaces, output types, tiers, projects) and conformance requirements. The validator, audit and skill template read standards from the repo.

Seeded: website and github (settled elements from the comms doc and the Home Assistant reference implementation), docs, social-profiles and app-stores (required elements TODO), and seo as a `status: example` core standard to be replaced or deleted by the marketing team.

Grace period for all shared standards: 2026-12-13. Until then a missing conformance file is a warning.
