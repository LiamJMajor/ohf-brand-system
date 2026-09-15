---
area: marketing/beats
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 90d
draft: true
---

# Home Assistant: beats

Recurring communications and what runs them. Cadence observed from the blog (https://www.home-assistant.io/blog/2026/09/02/release-20269/; 2026.8 on August 5, 2026.9 on September 2, both first Wednesdays). Playbooks per the comms architecture; confirm Asana template names.

| Beat | Cadence | Skill or playbook | Owner |
|---|---|---|---|
| Release (the beat) | monthly, first Wednesday | `run-release-beat` orchestrates from the release manifest: `write-release-post` (blog), `write-release-socials` (posts around the blog, T-0 and boosts), `promote-release-party` (T-21 artwork brief, T-7 event and schedule, T-7 and T-0 social), `write-feature-shorts` (T+1 per feature log item). Stable Medium playbook. Defined in interview 2026-09-14. | marketing team |
| Beta release | monthly, TODO: last Wednesday of prior month | Beta playbook by impact | TODO |
| Patch release | roughly weekly after a stable | Low: notes in the release post's Patch releases section | TODO |
| Works with Home Assistant partner announcement | as partners join (FireAvert, July 2026) | TODO skill | TODO |
| Community Day | annual (2026 save-the-date posted August 13) | TODO | TODO |
| State of the Open Home | annual, TODO | foundation-led; project posts its own angle (core/voices.md, Cross-promotion) | TODO |
| Hardware launch (Nabu Casa products) | per launch | Home Assistant voice promotes, per brand licence (core/voices.md, Commercial boundary) | TODO |
