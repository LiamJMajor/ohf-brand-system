---
name: Open Home Foundation
slug: open-home-foundation
tier: flagship
voice: foundation
status: interviewed
owner: @liam
maintainers: []
repo: https://github.com/OpenHomeFoundation
website: https://www.openhomefoundation.org
pillars: [privacy, choice, sustainability]
surfaces: [website, social-profiles, github]
related: [home-assistant, esphome, music-assistant]
standards: []
last_reviewed: 2026-09-15
---

# Open Home Foundation

The Open Home Foundation fights for privacy, choice, and sustainability in the smart home. Founded in 2024 out of Home Assistant, it is a tax-exempt non-profit foundation in Switzerland that owns and governs over 250 open source projects, standards, drivers, and libraries, so the infrastructure of the open home cannot be acquired, abandoned, or turned against the people who depend on it. (Assembled from https://www.openhomefoundation.org/ and /structure/ on 2026-09-15; confirm in interview.)

## Owners
| Folder | Owner |
|---|---|
| brand/ | @liam |
| design/ | @liam |
| marketing/ | @liam |
| surfaces/ | @liam |

## Files
Brand files drafted from public sources on 2026-09-15 (`onboard-project` stage 2), then interviewed the same day (`capture-judgment`). The validator passes with zero errors.

Confirmed and `draft: false`: `brand/voice.md` — four rules with contrast pairs, and a Modes table set by set-piece versus steady state.

Still `draft: true`: `brand/style.md` (three rulings confirmed inline; the rest is observation), `brand/strategy.md` (personality confirmed; positioning and the sustainability translation are not), `brand/messaging.md`, `brand/naming.md`, `brand/audiences.md`, `brand/story.md`. Design, marketing and standards files remain untouched stubs.

No area is `ready:`, so no skill may build against this project yet. Status stays `interviewed` rather than `validated` because messaging is not confirmed and no proof point is verified — the validator passing is necessary, not sufficient.

## What unblocks the next stage
In order:
1. **Verify the proof points.** Every row in `truths/open-home-foundation/proof-points.md` has Verified empty, which `core/escalation.md` treats as not usable. Until this is done, `brand/messaging.md` cites nothing an agent may state, and no boilerplate is usable. This is the single gate on everything downstream.
2. **Confirm messaging.** Boilerplate at all three lengths, the five key messages, and two open questions: whether boilerplate leads with structure or with the stake, and which of the two competing sets of pillar taglines is canonical (`/` and `/about/` currently differ).
3. **Resolve the duplicate figure.** "over 250 projects" lives in both `truths/core/proof-points.md` (marked Verified: Never) and `truths/open-home-foundation/proof-points.md`. Duplicated figures go stale apart; pick one home.
4. Then `ready: [brand]`, owner sign-off in `decisions/`, three examples via `harvest-examples`, and `live`.

## Codify queue
From the interview, in priority order: blog post → social post set, then partner announcement. Both go to `codify-workflow`. The first is the beat that prompted this onboarding.

## Deferred
- The UK→US spelling sweep across `core/` and `projects/home-assistant/`, agreed in interview but carried as its own pull request: it touches files the marketing team owns. See `decisions/2026-09-15-ohf-house-style.md`.
