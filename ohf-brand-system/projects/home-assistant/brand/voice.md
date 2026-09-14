---
area: brand/voice
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 180d
draft: false
---

# Home Assistant: voice

Inherits `core/voices.md`. The three rules below were drafted from the 2026.9 release post and the home page, and confirmed in interview on 2026-09-14.

## Sounds like
| | Home Assistant |
|---|---|
| Speaks about | its monthly releases, integrations, how-tos, dashboards, voice, energy, its community |
| Speaks to | people running it at home, people deciding to, and the contributors who build it |
| Sounds like | a maker talking to other makers; candid, warm, occasionally playful (a musical note emoji in a release post about chart accessibility) |
| Typically says | "Here's what's new." "You simply pick your device in the UI." "I'll be honest." |
| Never | Criticises other companies by name. Speaks for the foundation. Hypes. |

## Rules

### Lead with the problem, then the fix
Open with what was hard for the person, then what changed. Because readers run a home and want to know what it means for them before what it is called.
- Yes: "Modbus has always meant hand-writing your own register map in YAML. This release finally makes room on the bus." (https://www.home-assistant.io/blog/2026/09/02/release-20269/)
- No: "Introducing the new shared Modbus connection architecture."

### Say what it means for you, not what we built
Frame changes as outcomes for the reader. Because the release post itself has a section titled "From what changed to why it changed."
- Yes: "You can now see the whole chain from trigger to state change, with millisecond timestamps." (https://www.home-assistant.io/blog/2026/09/02/release-20269/)
- No: "We refactored the activity dialog to surface causal metadata."

### Credit people by name
Name the contributors behind a feature. Because the community is the product, and the release post credits handles throughout (@googanhiem, @piitaya, @Diegorro98 and others in 2026.9).
- Yes: "Thanks to @piitaya, the tile card now supports..."
- No: "The team has added tile card features."

## Modes
| Mode | When | Length | Energy | Channels | Never changes |
|---|---|---|---|---|---|
| Low | patch releases, single-integration news | as short as correct | neutral, factual | dev social, forum | facts cited; voice rules |
| Medium | the monthly release post and its socials | long-form, sectioned, screenshots per feature | warm, candid, a little playful. Release posts open "Home Assistant YYYY.M! 🎉" as house style (interview 2026-09-14); that is the only fixed emoji | blog, social, community, video | facts cited; contributors credited; fixed closing order (Integrations, Other noteworthy changes, Patch releases, Need help, Backward-incompatible changes, All changes) |
| High | Community Day, State of the Open Home, landmark releases | one idea, many formats | celebratory | all | facts cited; no banned words |

## When this bends
The editorial guide has a "Tone changes by channel" section, empty in draft v1. Until it is written: docs are governed by the developer style guide and are quieter; everything else follows the Modes table above. Unclear cases go to #marketing-comms.

## Never
- Publishes a date or version that is not in a linkable source. A date from a conversation is an assumption, not a fact (the most recent social post carried one and it was wrong; interview 2026-09-14). Sources: `truths/home-assistant/current-release.md`, the published post or tag. No release calendar exists yet; until one does, a planned date is confirmed by a person on the release team before it is written down, and that confirmation is recorded in the truth file (interview 2026-09-14).
- Publishes anything without a human signing it off. Current policy (interview 2026-09-14): every output for Home Assistant is reviewed by a person before it ships, whatever a skill's reliability tier says. Revisit when skills have eval history.
- Claims a device or integration works unless it is in `truths/home-assistant/`.
- Names a competitor critically; that is the foundation's job.
- Announces on another project's behalf (core/voices.md, Cross-promotion).
