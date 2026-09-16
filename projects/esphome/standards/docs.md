---
conforms_to: docs
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: docs

The standard is `core/standards/docs.md`, whose Required elements are still TODO. Nothing can be checked against it yet. The rows below record what the documentation surface actually has, as of 2026-09-16, so that writing the standard is a matter of comparison rather than discovery.

## Conformance

| Required element | Location | Status | Deviation |
|---|---|---|---|
| TODO: the standard has no required elements yet | | TODO | |
| Observed: entry point for new readers | https://esphome.io/install/getting-started/, linked from the home page and first in the sidebar | present | |
| Observed: a written style source for contributors | `CONTRIBUTING.md` in the documentation repository: Title Case headings, 120 character wrap, present tense, active voice, minimal examples, literal `GPIOXX` pins | present | it is stricter and more specific than anything the brand system has, and it disagrees with Home Assistant's documentation guide on heading case. Reconcile when the standard is written |
| Observed: an AI collaboration guide | `AGENTS.md` in the documentation repository, plus `CLAUDE.md`, `GEMINI.md` and `.github/copilot-instructions.md` | present | it carries a voice rule worth promoting: "Avoid the use of flowery language and weasel-words that add no useful content [...] you are not writing a press release" |
| Observed: glossary | none as a page | missing | terms are defined in place. `brand/style.md` carries the first written glossary for ESPHome, drafted from usage |
| Observed: how components are named | by configuration key, lowercase with underscores; page titles in Title Case | present | documented in `brand/naming.md` |
| Observed: branch model for documentation | `current` tracks the published release, `next` carries unreleased features and merges to `current` at release | present | anyone editing documentation must pick the right branch; a release-time correction to `current` is a different PR from a new feature's page on `next` |
