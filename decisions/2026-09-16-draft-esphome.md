---
date: 2026-09-16
area: projects
project: esphome
trigger: onboarding
change: ESPHome drafted from public sources; status registered to drafted
affected:
  - projects/esphome/PROJECT.md
  - projects/esphome/brand/
  - projects/esphome/marketing/channels.md
  - projects/esphome/standards/
  - truths/esphome/
  - projects/REGISTRY.md
by: @liam
---

# Drafted ESPHome from public sources

Stage 2 of `onboard-project`. Every brand file, `marketing/channels.md`, the four standards conformance files and both truth files are filled from public sources and marked `draft: true`. `ready:` stays empty, so no skill will build against ESPHome until the interview. Status moves registered to drafted.

## Where it came from
esphome.io was unreachable from the drafting environment, so the drafting was done against the repositories that publish it: `esphome/esphome-docs@current` commit `1f91cc2` (the source of esphome.io, read 2026-09-16) and `esphome/esphome@dev` for the README and LICENSE. Every citation names the published URL so a reviewer can check it directly. The GitHub API was also unreachable, which is why the repository description row in `standards/github.md` says unknown rather than carrying a figure, and why there is no stars proof point.

## What the sources settled
**ESPHome writes in two registers, and it says so itself.** The blog opened in July 2026 as a deliberate second voice: "We usually share our updates through raw, engineering-focused changelogs [...] we want to make our milestone releases more digestible for everyone in the community." The release post and the product announcement are not the same voice, and a draft written from the wrong one will be wrong in ways no rule file catches. `brand/voice.md` records both; `examples/esphome/` needs harvesting for each separately before anything ships.

**The project has its own written style guidance, and it is better than ours.** `CONTRIBUTING.md` and `AGENTS.md` in the documentation repository specify heading case, line length, tense, example minimalism, and the literal `GPIOXX` pin rule. One line from `AGENTS.md` is a voice rule worth promoting to core: "Avoid the use of flowery language and weasel-words that add no useful content [...] you are not writing a press release."

**The vocabulary differs from Home Assistant's on the word that matters most.** Home Assistant says integration; ESPHome says component. An agent that has written for one will get the other wrong on the first sentence. `brand/style.md` carries a glossary written specifically against that.

## Three things that need a person, not a source
1. **Em dashes.** `decisions/2026-09-15-social-register-and-tells.md` bans them in every register on every surface. ESPHome's 2026 posts contain 52 of them. The ban was drawn from foundation examples and nobody asked whether it binds project voices. Recorded as an open conflict in `brand/style.md`; drafts written now avoid them, and existing ESPHome copy is not being edited to match.
2. **"firmware".** The OHF editorial guide wants the word avoided. It is the load-bearing noun in ESPHome's explanation of itself: "ESPHome reads that description and builds custom firmware for your device." No alternative has been offered that survives the swap. Left as TODO in both `brand/style.md` and `brand/messaging.md` rather than resolved by preference.
3. **No social accounts.** Three independent lists on esphome.io name the same three destinations: Discord, GitHub, and a category inside Home Assistant's forum. Nothing links a social account. `standards/social-profiles.md` records the absence and names the two ways it resolves. Note also that ESPHome's forum is another project's forum, which is a dependency worth a deliberate answer.

## Deviations found, not fixed
- The README never says what ESPHome is. It opens with badges and a logo, then a link row. `core/standards/github.md` requires the opposite, and the fix is one sentence.
- The site footer names the Open Home Foundation but not "non-profit" and not the three principles, which `core/standards/website.md` requires and home-assistant.io carries.

Both are recorded in the conformance files. Neither is this pull request's to change: they are edits to ESPHome's own repositories, and they go to that project's maintainers.

## What this does not do
No interview, so no rule is confirmed. `truths/esphome/current-release.md` has a `review_by` of 2026-09-23 because 2026.9.0 is due on or about 2026-09-16 on the project's own third-Wednesday cadence; run `sync-truths` before citing it. `examples/esphome/` is still empty, and `harvest-examples` should run before the first output, not after.

Next: `capture-judgment` scoped to ESPHome, with @jesserockz.
