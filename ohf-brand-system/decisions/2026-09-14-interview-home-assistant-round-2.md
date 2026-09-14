---
date: 2026-09-14
area: brand
project: home-assistant
trigger: interview
change: Round 2; writing style guide identified as separate source; no-ordinals date rule with pair; unverified-date rule sharpened; all-outputs-human-sign-off policy recorded
affected:
  - projects/home-assistant/brand/style.md
  - projects/home-assistant/brand/voice.md
  - projects/home-assistant/PROJECT.md
by: @liam
---

# Interview round 2: Home Assistant

Correction to round 1: a separate writing style guide governs prose for human reading; the developer style guide governs docs. style.md now names both and marks which rules need re-checking against the writing guide once it is linked.

Contrast pairs captured:
- Dates: "Sept 23" yes, "Sept 23rd" no. No ordinals, from the writing style guide.
- The wrong date came from an assumption made in conversation, never verified. Rule: a date is only a date when it is in a linkable source.

Boundary: at this stage every output requires human sign-off. Recorded in PROJECT.md and voice.md.

## Proposal for core
Both the date rule and the sign-off policy plausibly apply to every project, not only Home Assistant. Proposed for `core/escalation.md`: (1) any date or version not present in a truths file or linked source blocks publishing; (2) during the first phase of the brand system, every skill output goes to a human. Route: core owner. Not applied to core here; project files hold it until the core owner decides.

## Follow-ups
- Location of the writing style guide, so its rules can be imported and the developer-guide-derived rules re-checked.
- Where dates are verified (release calendar location).
- Serial proxy release link.
