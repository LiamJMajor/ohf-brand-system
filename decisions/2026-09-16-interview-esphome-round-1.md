---
date: 2026-09-16
area: brand/voice
project: esphome
trigger: interview
change: Four drafted voice rules ruled on; two confirmed, one rescoped to change notes, one reclassified as messaging. Em dash ban confirmed org-wide. Human sign-off confirmed org-wide. ESPHome social accounts confirmed to exist.
affected:
  - projects/esphome/brand/voice.md
  - projects/esphome/brand/messaging.md
  - projects/esphome/brand/style.md
  - projects/esphome/PROJECT.md
  - core/escalation.md (pending, separate pull request)
by: @liam
---

# ESPHome interview, round 1

Rulings by @liam on 2026-09-16 against the stage 2 drafts. Recorded here because three of them reach past ESPHome.

## The voice rules

Four were drafted. Each had a "Yes" taken verbatim from published ESPHome writing; three had a "No" that was constructed rather than found. That asymmetry is what the round was for.

| Rule | Ruling |
|---|---|
| Name the key, the component and the release | **Rescoped.** A rule for change notes. Too complex for release notes and social posts, which aim for accessibility |
| Credit by handle and pull request number | **Confirmed unchanged** |
| Both halves of the promise, in the same breath | **Reclassified.** A messaging rule, not a voice rule. Moved to `brand/messaging.md` |
| Say the plain thing, at the plain length | **Confirmed unchanged.** Both halves of this pair are the project's own; nothing was constructed |

The rescoping matters more than it looks. The drafted rule described what ESPHome's release posts currently do, at config-key granularity. The ruling is that this register belongs to change notes only, and that release notes should be more accessible, along the lines of Home Assistant's. So the draft was accurate as description and wrong as prescription, which is a failure mode worth naming: drafting from observed practice codifies the practice, including the parts the organisation wants changed.

## Home Assistant as the gold standard, and where that leaves the rules

Also ruled: Home Assistant is currently the gold standard for communications across the projects, and rules similar to its own apply to ESPHome's release notes and social.

This has a structural consequence that is **not resolved by this entry**. `CLAUDE.md` says project files hold only that project's own translation, and that core content is never copied into a project. Home Assistant's voice rules live in `projects/home-assistant/brand/voice.md`. If they are the standard other projects follow, then either:

1. They are promoted to `core/`, Home Assistant cites core, and each project translates, or
2. Every project copies them, which the repository's own rules forbid, or
3. ESPHome cites another project's files, which nothing in the layout supports.

Option 1 is the only one consistent with the layout, and it is a core change owned by the core owner, touching files owned by the marketing team. It is not made here. Until it is, `brand/voice.md` carries three rules and an explicit gap for release notes and social.

## Reaching past ESPHome

**Em dashes: banned across every project and the foundation.** This closes the question `decisions/2026-09-15-social-register-and-tells.md` left open, which scoped the ban from foundation examples without saying whether project voices inherited it. They do. Second-order: ESPHome's published 2026 posts contain 52 em dashes and 20 en dashes, so this converts an open question into a known gap in existing copy. New copy complies; correcting the archive is a separate decision nobody has funded.

**Human sign-off: every output, every project, and the foundation.** Previously recorded only as a Home Assistant policy (`projects/home-assistant/PROJECT.md`, interview 2026-09-14), with `core/escalation.md` governing the foundation voice alone. It is the organisation default. This belongs in `core/escalation.md` and travels in its own pull request rather than riding in an ESPHome onboarding.

**ESPHome has social accounts.** The stage 2 draft recorded that none were found and offered two resolutions. The answer is the second one: they exist and ESPHome's own site links none of them. That converts `standards/social-profiles.md` from "records an absence" to a live conformance gap, and makes the missing links a website finding. Handles are still needed before `marketing/channels.md` and `standards/social-profiles.md` can be filled.

**Maintainers.** @jesserockz is confirmed as a maintainer and is not the only one. The interview may be run with anyone holding the knowledge, so stage 3 is not blocked on a named individual.

**Website ownership.** Marketing handles websites. The footer attribution deviation found in stage 2 routes there rather than to ESPHome's engineering maintainers.

## Still open after this round
- Where the accessibility rules for release notes and social live (see above). Blocks completing `brand/voice.md`.
- ESPHome's social handles. Blocks two files.
- The 14 remaining TODOs in `brand/`, chiefly the undated history in `story.md` and the two audience objections.
- The "firmware" ruling.
- Units convention.

## Round 1, second pass (same day)

Three follow-up rulings, and what they changed.

**Social handles: deferred.** `marketing/channels.md` and `standards/social-profiles.md` keep their recorded gap. The accounts are confirmed to exist; the handles are not being chased now. Both files say so rather than implying an absence.

**Core promotion: not now; continue as before.** The accessibility rules for release notes and social were therefore written into `projects/esphome/brand/voice.md` as ESPHome's own, not promoted to `core/` and not copied from Home Assistant. The evidence for all three is ESPHome's own accessible register: the 2026 product announcements and the home page, which already write this way. Home Assistant remains the standard being matched, but no Home Assistant text was carried across, so `CLAUDE.md`'s rule against copying between projects holds.

The structural question above is unresolved, not answered. If a third project needs the same rules, it will be rediscovered a third time from that project's evidence. That is the cost of deferring, and it is a deliberate choice rather than an oversight.

The three new rules: open with what the reader wanted to do and what was in the way; gloss the technical term the first time it appears; say what the reader gets, not what was rebuilt. `brand/voice.md` now carries six rules in total, three of them scoped to accessible registers and one scoped to change notes.

The third pair is worth noting. Its "No" is real ESPHome text from the 2026.8.0 release overview, not a constructed example. It is not bad writing; it is correct in a change note and wrong as the opening of a release note. The two-register ruling is that pair.

**Story dates: two recovered from the changelog archive.** The Otto Winter to Guillermo Ruffino handover is dated 13 September 2020 (v1.15.0). The rename to ESPHome is still undated but now bounded: v1.10.0 precedes v1.13.0, which is dated 30 May 2019.

Three history TODOs remain and none can be closed from public sources. The founding year: the changelog archive reaches back to v1.7.0 with no date, and the LICENSE copyright of 2019 dates the ESPHome name rather than the project, which existed earlier as esphomelib and esphomeyaml. The date ESPHome joined the Open Home Foundation: openhomefoundation.org is blocked by the drafting environment's egress proxy, as is esphome.io, so neither could be checked. Both need either a person or an unblocked environment.

## Round 2

Four rulings, 2026-09-16.

**"firmware": avoided everywhere.** Say "the software ESPHome builds" or "the code that runs on the chip". This is the heaviest ruling of the onboarding so far, because the word is load-bearing in ESPHome's own explanation of itself: the Get Started guide reads "ESPHome reads that description and builds custom firmware for your device", and the home page uses it too.

The consequence is worth stating plainly rather than burying. This is not a rule the brand system derived from ESPHome's practice; it is a rule that overrides it. Until the site is updated, the brand system and the published copy disagree on the central sentence of the project's pitch. `brand/style.md` and `brand/messaging.md` both record it as a gap in existing copy rather than a description of it, so an agent reading either file knows it will see "firmware" in the wild and must not copy it. The site correction routes to marketing, per the earlier ruling on website ownership.

Every use in the drafted files was rewritten, including the `PROJECT.md` summary paragraph and one in `brand/voice.md` where "another firmware project" became "another project in the same space".

**Units: metric, matching Home Assistant.** No exception for board and enclosure dimensions, even where the part is sold in inches. One organisation-wide convention beats a per-project judgment call.

**Contributor objection: needing the physical hardware.** You cannot write or test a component for a device you do not own, so contributing is conditional on having already bought the thing. Recorded in `brand/audiences.md`, and the contributor key message in `brand/messaging.md` was rewritten to answer it: the `host` platform runs components on a computer with no board attached, and devices.esphome.io shows what is already covered before you buy anything.

Worth noting this is a materially different barrier from Home Assistant's, where the recorded objections are the size of the project and not knowing where to start. Borrowing Home Assistant's answer would have been wrong, which is why the draft left it as a TODO rather than guessing.

**Fourth audience confirmed.** "People reclaiming off-the-shelf devices" stands as an audience in its own right, on the grounds that it carries the sustainability pillar and has its own documentation path. Its objection is still unwritten and is the only brand TODO that a person can close quickly.

## Round 3

**Fourth audience objections: all four confirmed.** "People reclaiming off-the-shelf devices" carries four objections rather than one, and they compound: not knowing whether the chip inside is supported, fear of bricking a device that currently works, having to physically open the case, and losing the vendor app's features.

Taken together they describe someone with more to lose than a first-time builder and less certainty about what they are holding. That shaped the key message in `brand/messaging.md`, which now opens on the device list at devices.esphome.io rather than on the sustainability argument, because "is my specific device on the list" is the question that has to be answered before any of the others matter.

**History gaps: left unfilled, with the project proceeding.** The founding year, the date ESPHome joined the Open Home Foundation, the date of the v1.10.0 rename, and how the project describes its own community are not established. Both esphome.io and openhomefoundation.org are blocked by the drafting environment's egress proxy, so none could be checked from here.

## Round 4

**story.md: TODO markers converted to recorded absences.** The facts are still unknown. What changed is that the file now states what is not established and why, rather than marking a task nobody can do. The founding year, the date ESPHome joined the foundation, and the date of the v1.10.0 rename are each written as "not established", with the bound that is known and the reason the source could not be reached. The community self-description says plainly that ESPHome has none, that writing should use the home page's "thousands of makers already using ESPHome" until it does, and that Home Assistant's must not be borrowed.

This is the same pattern `truths/esphome/proof-points.md` already uses in its "Not yet usable" section, and it carries more information than a TODO did. `brand/` is now free of TODO markers.

**strategy.md: voice rulings propagated, and the skill fixed.** Two of the three rulings made against `brand/voice.md` had not reached `brand/strategy.md`, where the same ideas sat as Personality attributes in different words. The Personality section now holds two attributes rather than three: the change-note precision rule is scoped to match the ruling, "No code required, and the code is right there" is deleted because it was reclassified as a messaging rule and lives in `brand/messaging.md`, and the contributors attribute stands.

The cause is structural rather than an oversight in this onboarding. `references/project-spec.md` says `brand/strategy.md` is the source the other brand files derive from; stage 2 drafts them in parallel as siblings. A ruling against one therefore does not reach the others. `skills/onboard-project/SKILL.md` in `brand-system-builder` now carries a propagation checklist at stage 3, covering the four cases seen here, and a requirement to record what a ruling overrides rather than only what it decides. That change travels in its own pull request in that repository.

## Round 5, and 2026.9.0

**Naming inferences confirmed as rules.** The lowercase `esphome` boundary (command, package, repository and URL paths) and first-mention-in-full for named products both stand as rules. Each file records that the boundary was drawn from measured usage rather than stated by the project, so a later reader does not mistake the drafting for ESPHome's own decision.

**Short attribution form: an organisation pattern.** "ESPHome, an Open Home Foundation project" is not ESPHome's wording and no ESPHome source uses it. It is the form confirmed for Home Assistant by the marketing team on 2026-09-14, applied across projects with the name swapped.

This is the same shape as the question deferred in round 1: a rule confirmed for one project, living in that project's directory, applied to others. It has now come up twice in one onboarding. Deferring it once is reasonable; the third time a project needs a form that is really the organisation's, it belongs in `core/`.

## 2026.9.0 landed, and corrected two drafted rules

ESPHome 2026.9.0 was published on 16 September 2026, during this onboarding. `truths/esphome/current-release.md` is updated and 2026.8.0 moved to Superseded. Two rules drafted from 2026.8.0 turned out to be wrong the moment a second release existed to compare against.

**Heading case in release posts changed.** 2026.8.0 wrote "Release Overview", "Upgrade Checklist", "Thank You, Contributors". 2026.9.0 writes "Release overview", "Upgrade checklist", "Thank you, contributors". The change is consistent across every heading in the post, so it is a decision rather than a slip. `brand/style.md` now splits the rule: Title Case in documentation, sentence case in release posts, following 2026.9.0.

**The release post structure changed, in the direction of the accessibility ruling.** 2026.9.0 is the first to open with a plain-language section, "Short on time? Here's the quick version", ahead of the technical write-up. It names the three changes that affect a typical configuration in ordinary words, then says plainly that a typical setup needs nothing else, then hands off: "Keep reading below for the full release overview and technical detail."

That is the two-register ruling of 2026-09-16, implemented by the project itself, in the same week and without reference to this work. The Modes table and the "say what the reader gets" rule both now cite it. It is the strongest available example of ESPHome's accessible register and should be first in line for `harvest-examples`.

Worth drawing the general lesson, because it will recur. A rule drafted from a single release describes that release. Two of the rules here survived contact with the next one and two did not, and nothing in the drafting flagged which were which. Where a rule rests on one observation, the file should say so.

## Round 6, on 2026-09-17

**A contradiction is a question, not a decision.** Ruled after this onboarding resolved one by assuming. The 2026.9.0 release post uses sentence case headings against a Title Case rule drawn from the documentation's `CONTRIBUTING.md` and the 2026.8.0 post, and `brand/style.md` was rewritten to follow the newer post. That was wrong twice over: it treated the most recent artefact as authoritative, and it changed a stated rule on the strength of one post.

The ruling is that **the rule stands and the post deviates**. `brand/style.md` is restored to Title Case for documentation and release posts, with 2026.9.0 recorded as a known deviation and an instruction not to follow it. A change in published copy is not a change in the rule; it is a copy that needs correcting.

`skills/onboard-project/SKILL.md` in `brand-system-builder` now forbids resolving a contradiction by assumption, and requires marking any rule that rests on a single observation so the next contradiction can be weighed rather than guessed at.

**The "Short on time?" section is a direction, not a rule.** It demonstrates ESPHome lowering the technical language in its communications, to make the project easier to understand and adopt. The Modes table records it as that, and does not require it of future posts. This is the same one-post evidence base as the heading case, ruled differently and deliberately: the section moves toward the accessibility direction already ruled on 2026-09-16, where the heading case moved away from a stated rule.

**2026.9.0 harvested as the first ESPHome example.** Filed at `examples/esphome/release-post/2026-09-release-202690.md`, annotated per the protocol, with the deviations called out in `What not to copy`: the sentence-case headings, the en dashes, and the summary section's status as a direction rather than a required heading.

Harvesting a post that breaks a rule is deliberate. It carries the best available writing in ESPHome's accessible register, and an example that teaches register while naming its own defects is more useful than waiting for a clean one. The annotation has to do that work, or the example teaches the defect.

Two examples still needed before `live`: the minimum for flagship is three.
