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
