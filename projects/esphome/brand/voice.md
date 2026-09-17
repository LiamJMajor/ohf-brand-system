---
area: brand/voice
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: false
---

# ESPHome: voice

Inherits `core/voices.md`. Each rule is a decision with a reason and a contrast pair. Drafted 2026-09-16 from the 2026.8.0 release post, the home page, the Get Started guide and the repository's own writing guidance. Every rule below is a draft candidate: the Yes is real published ESPHome writing, the No is constructed. Nothing here is confirmed.

Read this alongside `brand/style.md`. ESPHome writes in two registers that the sources keep clearly apart: the release post, written by a maintainer for people with a config file open, and the product announcement, written for people who have not built anything yet. A draft in the wrong one will be wrong in ways no rule here catches.

## Sounds like
| | ESPHome |
|---|---|
| Speaks about | its monthly releases, components, chip support, the Device Builder, YAML configuration, the Starter Kit, and the people who send pull requests |
| Speaks to | people building their own smart home devices, from a first sensor to fifty of them, and the developers adding components |
| Sounds like | a maintainer writing up what shipped: precise, unhurried, specific down to the configuration key. Warmer on the home page and in product announcements than in a release post |
| Typically says | "no need to code unless you want to". "If you use X, rename it to Y." "Thank You, Contributors." |
| Never | Criticises other companies by name. Speaks for the foundation. Writes a press release. |

## Rules

Confirmed by @liam on 2026-09-16 (interview round 1). Two rules stand as drafted, one was rescoped, one was moved out of this file. The release-note and social rules are a known gap; see below.

### In change notes, name the key, the component and the release
**Scoped to change notes only** (ruling, 2026-09-16). When something changes, say exactly what the reader must edit and when the old spelling stops working. Because they have a configuration file open and a device that will not compile. Source: the 2026.8.0 upgrade checklist (https://esphome.io/blog/2026/08/19/esphome-2026-8/).
- Yes: "If you use `command_throttle` on `modbus_controller`, move the setting to `turnaround_time` on the `modbus` component; `allow_duplicate_commands` no longer has any effect."
- No: "Modbus configuration has been streamlined. Review your setup after updating."

This register is **too complex for release notes and social posts**, which are aiming for accessibility (ruling, 2026-09-16). Do not carry it across. What was drafted here described ESPHome's current release-post practice; the ruling is that release notes should read more like Home Assistant's.

### Credit by handle and pull request number
A feature belongs to whoever sent it, named, linked, with the number. Because that is what a release is made of, and the count is published: 348 pull requests from over 40 contributors in 2026.8.0 (https://esphome.io/blog/2026/08/19/esphome-2026-8/). Confirmed unchanged 2026-09-16.
- Yes: "[@exciton](https://github.com/exciton) - 25 PRs including the `modbus_controller` refactor and the new `modbus_client` component with typed actions"
- No: "The team delivered a major Modbus overhaul this release."

### Say the plain thing, at the plain length
No adjective that survives its noun being swapped out. The repository states this as a rule for its own contributors: "Avoid the use of flowery language and weasel-words that add no useful content. Keep comments concise and technically accurate - you are not writing a press release." (https://github.com/esphome/esphome-docs/blob/current/AGENTS.md) Confirmed unchanged 2026-09-16. Both halves of this pair are the project's own; neither was constructed.
- Yes: "Created documentation with examples and instructions."
- No: "Created comprehensive documentation with configuration examples and setup instructions."

### Open with what the reader wanted to do, and what was in the way
In release notes and social, start from the reader's intention, not the change. Because the accessibility ruling of 2026-09-16 puts these registers in reach of people who have never built a device. Source: the Starter Kit announcement (https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/).
- Yes: "Ever wanted to build your own smart home device, but didn't know where to begin?"
- No: "This release introduces a hardware bundle containing four pre-configured sensor modules."

### Gloss the technical term the first time it appears
Every chip, protocol, component and product gets a plain-language gloss on first mention. Because the reader who needs the release note least is the one who already knows what a microcontroller is. This is also an organisation-wide rule (`decisions/2026-09-15-social-register-and-tells.md`); ESPHome's home page already does it well. Source: https://esphome.io/.
- Yes: "Every ESPHome device is built around a small, inexpensive chip called a microcontroller"
- No: "Install the Device Builder and flash your ESP32-C6 over OTA."

### Say what the reader gets, not what was rebuilt
Lead with the outcome in the reader's home. The architecture goes underneath, or in the change notes. Source: the home page's third step (https://esphome.io/), and now the release posts themselves: 2026.9.0 opens "Here's the plain-language version for anyone short on time or newer to ESPHome" and leads with what a typical configuration needs, not with the architecture (https://esphome.io/blog/2026/09/16/esphome-2026-9/). That section is evidence of the project lowering the technical language in its communications to make ESPHome easier to understand and adopt. It is not itself a required section.
- Yes: "Your new device automatically pops up in Home Assistant over your local network: no cloud accounts or external servers required."
- No: "A new platform-neutral BLE layer moves all 39 BLE sensor platforms off their ESP32-only foundation."

The No above is real ESPHome text, from the 2026.8.0 release overview. It is not wrong; it is correct in a change note and wrong as the opening of a release note. That is the 2026-09-16 ruling in one pair.

## Rule changes and gaps

### Moved out of this file
"Both halves of the promise, in the same breath" (no code required, and the YAML is right there) was drafted here and ruled a **messaging rule, not a voice rule** (2026-09-16). It now lives in `brand/messaging.md` under Message rules.

### Release note and social rules added 2026-09-16
The accessibility ruling of 2026-09-16 required rules for these registers. Rather than carry Home Assistant's across, the three rules above under Rules were written from ESPHome's own accessible register: the 2026 product announcements and the home page, which already write this way. Home Assistant remains the standard being matched; the evidence is ESPHome's.

## Modes
| Mode | When | Length | Energy | Channels | Never changes |
|---|---|---|---|---|---|
| Low | patch releases, single-component news | as short as correct | neutral, factual | Discord, GitHub release notes | facts cited; voice rules |
| Medium | the monthly release post and the changelog entry | long-form, sectioned: overview, upgrade checklist, feature sections, contributors, breaking changes, full changelog. 2026.9.0 added a plain-language "Short on time?" summary ahead of the technical write-up; that is a direction, not a required structure (ruling 2026-09-17) | accessible: opens from the reader's intention, glosses every term, leads with outcomes. The change-note sections keep the exact config-key register; the surrounding post does not | blog, changelog, Discord, forum | facts cited; contributors credited; upgrade checklist before feature sections |
| High | first-party product launches, Community Day, State of the Open Home | one idea carried across the piece, images, quotes from partners | warm, second person, direct address | blog, and wherever the foundation amplifies | facts cited; no banned words; the local-control claim stated as a property, not a value |

Two corrections from 2026-09-16. ESPHome **does** have social accounts; they are simply not linked from its own site, so the social row is pending handles rather than absent. And the Medium row as drafted codified current practice, which the same ruling rejects as too complex for release notes. The High row is drafted from exactly three posts, all from 2026 (Device Builder, Desktop App, Starter Kit), two of which were written by people outside the engineering team.

## When this bends
Documentation is governed by `CONTRIBUTING.md` in the documentation repository, which is stricter and quieter than anything here: Title Case section headings, 120 character lines, present tense, active voice, minimal examples. Where documentation guidance and this file disagree inside a documentation page, the documentation guidance wins. Everywhere else, this file wins.

## Never
- States that a component, chip or device works unless it is in `truths/esphome/` or the linked documentation page.
- Gives a version or a date that is not in a published release, tag or post.
- Writes an upgrade instruction that has not been checked against the release's own breaking-changes list. A wrong instruction here does not embarrass anyone, it breaks a reader's house.
- Criticises another company by name, or another project in the same space by name. That is the foundation's job, and it is not ESPHome's fight (`core/voices.md`).
- Announces on another project's behalf, including Home Assistant's (`core/voices.md`, Cross-promotion).
- Shortens or recases the name: never ESP, EspHome, or esphome in prose.
