---
area: brand/voice
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
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

### Name the key, the component and the release
When something changes, say exactly what the reader must edit and when the old spelling stops working. Because they have a configuration file open and a device that will not compile. Source: the 2026.8.0 upgrade checklist (https://esphome.io/blog/2026/08/19/esphome-2026-8/).
- Yes: "If you use `command_throttle` on `modbus_controller`, move the setting to `turnaround_time` on the `modbus` component; `allow_duplicate_commands` no longer has any effect."
- No: "Modbus configuration has been streamlined. Review your setup after updating."

### Credit by handle and pull request number
A feature belongs to whoever sent it, named, linked, with the number. Because that is what a release is made of, and the count is published: 348 pull requests from over 40 contributors in 2026.8.0 (https://esphome.io/blog/2026/08/19/esphome-2026-8/).
- Yes: "[@exciton](https://github.com/exciton) - 25 PRs including the `modbus_controller` refactor and the new `modbus_client` component with typed actions"
- No: "The team delivered a major Modbus overhaul this release."

### Both halves of the promise, in the same breath
No code required, and the YAML is right there. Never one without the other. Because the beginner needs permission to start and the veteran needs proof they are not being fenced out. Source: the home page (https://esphome.io/).
- Yes: "Its intuitive Device Builder replaces code with simple visual choices [...] And for experienced users who prefer writing code manually, YAML is always there if you need it."
- No: "ESPHome now handles everything for you, so you never need to see a configuration file again."

### Say the plain thing, at the plain length
No adjective that survives its noun being swapped out. The repository states this as a rule for its own contributors: "Avoid the use of flowery language and weasel-words that add no useful content. Keep comments concise and technically accurate - you are not writing a press release." (https://github.com/esphome/esphome-docs/blob/current/AGENTS.md)
- Yes: "Created documentation with examples and instructions."
- No: "Created comprehensive documentation with configuration examples and setup instructions."

## Modes
| Mode | When | Length | Energy | Channels | Never changes |
|---|---|---|---|---|---|
| Low | patch releases, single-component news | as short as correct | neutral, factual | Discord, GitHub release notes | facts cited; voice rules |
| Medium | the monthly release post and the changelog entry | long-form, sectioned: overview, upgrade checklist, feature sections, contributors, breaking changes, full changelog | plain and technical; no celebration beyond the contributor thanks | blog, changelog, Discord, forum | facts cited; contributors credited; upgrade checklist before feature sections |
| High | first-party product launches, Community Day, State of the Open Home | one idea carried across the piece, images, quotes from partners | warm, second person, direct address | blog, and wherever the foundation amplifies | facts cited; no banned words; the local-control claim stated as a property, not a value |

Two things this table records that the interview should either confirm or correct. ESPHome has no social row, because no ESPHome social account was found on its own site. And the High row is drafted from exactly three posts, all from 2026 (Device Builder, Desktop App, Starter Kit), two of which were written by people outside the engineering team.

## When this bends
Documentation is governed by `CONTRIBUTING.md` in the documentation repository, which is stricter and quieter than anything here: Title Case section headings, 120 character lines, present tense, active voice, minimal examples. Where documentation guidance and this file disagree inside a documentation page, the documentation guidance wins. Everywhere else, this file wins.

## Never
- States that a component, chip or device works unless it is in `truths/esphome/` or the linked documentation page.
- Gives a version or a date that is not in a published release, tag or post.
- Writes an upgrade instruction that has not been checked against the release's own breaking-changes list. A wrong instruction here does not embarrass anyone, it breaks a reader's house.
- Criticises another company by name, or another firmware project by name. That is the foundation's job, and it is not ESPHome's fight (`core/voices.md`).
- Announces on another project's behalf, including Home Assistant's (`core/voices.md`, Cross-promotion).
- Shortens or recases the name: never ESP, EspHome, or esphome in prose.
