---
date: 2026-09-14
area: examples
project: home-assistant
trigger: interview
change: Three release-post examples filed as candidates pending marketing team review
affected:
  - examples/home-assistant/release-post/
by: @liam
---

# Harvest: Home Assistant release posts

Sources scanned: blog index, release posts 2026.7, 2026.8, 2026.9. Selected: all three, as the three most recent stable release posts and the direct inputs for the first codified beat. Rejected: none; non-release pieces not yet scanned because no proud piece was named. All three carry `pending_review: true` until the marketing team confirms them.

Observations for the interview and the core owner:
- All three share a fixed closing order (Integrations, Other noteworthy changes, Patch releases, Need help, Backward-incompatible changes, All changes). That is a structural rule for `write-release-post`.
- Two of three open with an emoji and an exclamation. Either the Medium mode allows this for release posts or the examples should say so. Decide.
- 2026.7's heading uses "powerful", on the banned list. Same tension as the home page's "Powerful automations". Decide whether the list bends for feature headings.
- No near-miss example yet. The protocol wants one per type; ask the team for a release post or section they would write differently today.
