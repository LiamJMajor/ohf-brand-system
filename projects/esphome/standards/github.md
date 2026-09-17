---
conforms_to: github
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: github

The standard is `core/standards/github.md`. Checked 2026-09-16 against https://github.com/esphome/esphome at `dev`. The GitHub API was not reachable from the drafting environment, so the repository description could not be read; that row stays unknown rather than guessed.

## Conformance

| Required element | Location | Status | Deviation |
|---|---|---|---|
| Repository description is the project's one-line boilerplate | repository description | unknown | not readable from the drafting environment. Check against `brand/messaging.md` One line: "ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices." |
| README carries the Open Home Foundation badge or approved attribution | README footer badge: "ESPHome - A project from the Open Home Foundation", linking openhomefoundation.org | present | |
| README links to the website, documentation and the community entry point | README links Documentation (esphome.io), Issues, Feature requests (GitHub Discussions), and Discord via badge | present | the Discord link is a badge rather than a named link, and the Home Assistant forum category is not linked from the README |
| Licence visible in the repository root | `LICENSE`: GPLv3 for C++ and runtime, MIT for Python and everything else | present | dual-licence by file extension. Anyone writing "ESPHome is MIT licensed" or "GPL licensed" alone is wrong |
| Social preview image | | unknown | the standard leaves this TODO |
| Code of conduct and contributing file | `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` in the root of `esphome/esphome`; both also in the documentation repository | present | `CONTRIBUTING.md` delegates to https://developers.esphome.io/contributing/code/ rather than carrying the guidance itself |

## Rules checked
- **The README opens with what it is, not how to build it.** Fails. The README opens with badges and the logo, then a link row, then the foundation badge. It never says what ESPHome is. Someone arriving from a search result learns nothing without clicking through to esphome.io. This is the single clearest actionable gap found in this onboarding, and the fix is one sentence: the One line boilerplate, under the logo.
