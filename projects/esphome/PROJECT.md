---
name: ESPHome
slug: esphome
tier: flagship
voice: project
status: drafted
owner: @liam
maintainers: [@jesserockz]  # confirmed a maintainer 2026-09-16, not the only one; interview may be run with anyone holding the knowledge
repo: https://github.com/esphome/esphome
website: https://esphome.io
pillars: [privacy, choice, sustainability]
surfaces: [website, docs, social-profiles, github]
related: [home-assistant]
standards: []
ready: []
last_reviewed: 2026-09-16
---

# ESPHome

ESPHome turns cheap microcontrollers into smart home devices you design yourself. You describe the hardware attached to a board in a YAML configuration, or pick it from a list in the ESPHome Device Builder, and ESPHome builds the software that runs on the chip. Everything you define shows up in Home Assistant over your own network, with no cloud account in between. The first install goes over a USB cable; every update after that can go over the air.

(Drafted 2026-09-16 from the home page, the Get Started guide and the README. Confirm in the maintainer interview whether this stays the canonical paragraph.)

## Owners
| Folder | Owner |
|---|---|
| brand/ | @liam |
| design/ | @liam |
| marketing/ | @liam |
| surfaces/ | @liam |

## Files
Brand files and `marketing/channels.md` drafted 2026-09-16 from public sources, all `draft: true`. Design, the rest of marketing, and the standards conformance files are untouched templates. `ready:` is empty: no area is confirmed, so every skill will refuse this project until the interview lands.

Sources used, all read on 2026-09-16: the README and LICENSE at `esphome/esphome@dev`; the documentation site source at `esphome/esphome-docs@current`, commit `1f91cc2`, which is what publishes to https://esphome.io. The live site was unreachable from the drafting environment, so every citation below names the published URL and the file in the source repository that produces it.

## Review policy
Every output requires human sign-off before publishing, regardless of a skill's reliability tier. Ruled on 2026-09-16 as applying to **all projects and the foundation**, not just Home Assistant, so this is an inherited rule rather than an ESPHome one; it belongs in `core/escalation.md` and travels in its own pull request. Skills producing for ESPHome deliver drafts marked "needs review" and name the reviewer.

## Open follow-ups
- **No social channels found.** The site footer, the Starlight social config and the community section list only Discord, GitHub and the Home Assistant forum category. If ESPHome has accounts on any network, they are not linked from its own site. Confirm at interview: either they exist and the site should link them, or `social-profiles` comes off `surfaces:`.
- **Em dashes.** Banned in every register by `decisions/2026-09-15-social-register-and-tells.md`. ESPHome's published copy uses them freely. Recorded as a conflict in `brand/style.md`; the interview settles whether the ban is organisation-wide or foundation-only.
- **"firmware" is settled.** Ruled avoided everywhere on 2026-09-16; say "the software ESPHome builds" or "the code that runs on the chip". ESPHome's own home page and Get Started guide still use the word, so this is now a gap between the brand system and published copy rather than an open question. Correcting the site is marketing's, per the same round.
- **Design files.** Not drafted. Checkable material exists if someone wants it: logo lockups at https://media.esphome.io/logo/ (`logo-text-on-light.svg`, `logo-text-on-dark.svg`), accent `#b3c7ff` and surface `#23272e` in `src/pages/index.astro`, and the OHF lockups the footer serves.
- **Ownership date.** The README carries the Open Home Foundation badge, but no source read gave the date ESPHome joined. Home Assistant's truth file dates its own transfer to April 2024; do not assume ESPHome's is the same.
- **Examples.** `examples/esphome/` is empty. Flagship live needs at least three. Harvest release posts and product announcements separately: they are two different registers.
