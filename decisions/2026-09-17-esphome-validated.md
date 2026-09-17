---
date: 2026-09-17
area: projects
project: esphome
trigger: onboarding
change: ESPHome brand files confirmed and ready; status drafted to validated
affected:
  - projects/esphome/PROJECT.md
  - projects/esphome/brand/
  - projects/REGISTRY.md
by: @liam
---

# ESPHome validated

All seven `brand/` files set `draft: false`, `ready: [brand]`, status `drafted` to `validated`. Validator: zero errors. Two warnings, both expected: `design/` and `marketing/` are not ready, so skills needing those areas will refuse and will say which.

## What confirmation rests on
Seven interview rounds across 2026-09-16 and 2026-09-17, recorded in `decisions/2026-09-16-interview-esphome-round-1.md`. Every rule in `brand/` has either been ruled on directly or is a verbatim quotation from a published source. The drafted files as they stood on 2026-09-16 are not what is being confirmed; four of the rulings changed them materially.

| Round | What it settled |
|---|---|
| 1 | Four voice rules: two confirmed, one rescoped to change notes, one reclassified as messaging. Em dashes banned org-wide. Human sign-off org-wide. Social accounts exist |
| 2 | "firmware" avoided everywhere. Units metric. Contributor objection is needing the hardware. Fourth audience confirmed |
| 3 | Four objections for the reclaiming audience, which reshaped its key message |
| 4 | History gaps recorded as absences rather than TODOs. Voice rulings propagated into `brand/strategy.md` |
| 5 | Naming inferences confirmed as rules. Short attribution form confirmed as an organisation pattern |
| 6 | A contradiction is a question, not a decision: Title Case stands, 2026.9.0 deviates. First example harvested |
| 7 | Positioning is building smart home devices; Home Assistant compatibility is a benefit, never the pitch |

## What is knowingly incomplete
- **Examples: one of three.** `examples/esphome/release-post/2026-09-release-202690.md` only. Flagship `live` requires three, and they should span registers: the release post and the product announcement are different voices, so the remaining two belong under a separate type rather than beside this one.
- **History.** Founding year, the date ESPHome joined the foundation, the date of the v1.10.0 rename, and the project's own description of its community are all recorded as not established, with the reason. `brand/story.md` carries what is known and refuses to approximate what is not.
- **Social handles.** Confirmed to exist, not supplied. `marketing/channels.md` and `standards/social-profiles.md` record the gap.
- **Two deviations in ESPHome's own surfaces**, routed to marketing: the README never says what ESPHome is, and the site footer omits "non-profit" and the three principles. Both recorded in the conformance files.
- **Three deviations in published copy against confirmed rules:** em dashes throughout the 2026 posts, "firmware" in the home page and Get Started guide, and sentence-case headings in 2026.9.0. All three are recorded as gaps in existing copy rather than as descriptions of practice, so an agent meeting them in the wild does not copy them.

## Next
`live` needs two more examples and an owner sign-off entry. Until then no skill builds against ESPHome.
