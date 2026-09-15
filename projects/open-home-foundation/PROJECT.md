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

Confirmed and `draft: false`: `brand/voice.md`. Six rules with contrast pairs, and a four-row Modes table, split so blog and social are no longer treated as one register.

`examples/open-home-foundation/social-post/` holds three approved posts, filed 2026-09-15 and `pending_review: true`. They are the only register evidence in the repository for this project and they changed the drafts materially. Load them before writing anything social.

Still `draft: true`: `brand/style.md` (three rulings confirmed inline; the rest is observation), `brand/strategy.md` (personality confirmed; positioning and the sustainability translation are not), `brand/messaging.md`, `brand/naming.md`, `brand/audiences.md`, `brand/story.md`. Design, marketing and standards files remain untouched stubs.

No area is `ready:`, so no skill may build against this project yet. Status stays `interviewed` rather than `validated` because messaging is not confirmed and no proof point is verified. The validator passing is necessary, not sufficient.

## What unblocks the next stage
1. **Verify the proof points.** Every row in `truths/open-home-foundation/proof-points.md` has Verified empty, which `core/escalation.md` treats as not usable. Boilerplate and taglines are now confirmed wording, but every figure inside them is unusable until a person confirms it and dates it. This is the only thing standing between this project and a working `brand/messaging.md`.
2. **Walk the five key messages.** The interview covered boilerplate, taglines and pillar translations and ran out before these. The funders and commercial partners message has no draft at all, because no published piece addresses that audience.
3. **Qualify the gloss rule by audience.** `brand/voice.md`, "Assume they have never heard of it", is written absolutely. It is right for broadcast social and wrong for community channels, where glossing Zigbee to contributors reads as patronising. It was written from a broadcast rejection and has not been tested anywhere else.
4. **Settle the social censoring question.** `brand/style.md` permits "f\*ck" on social on an explicitly unverified belief about platform ranking. The file records what would test it.
5. Then `ready: [brand]`, owner sign-off in `decisions/`, and `live`. The flagship three-example minimum is met for social posts; no other output type is covered.

## Confirmed in interview and correction (2026-09-15)
- Six voice rules with contrast pairs; Modes by set-piece versus steady state, with a separate social row; fourth personality attribute.
- House style: US English, serial comma always, em dashes never, ampersands never, strong language where it carries the argument, and a named list of writing tells banned outright.
- Social register, from the examples: emoji expected (one in the opening, a pointer at the link), one copy across networks, under 280 characters of body, months abbreviated.
- Every event, acronym, standard and partner gets glossed on first mention.
- Taglines are not sign-offs. Canonical does not mean droppable-in.
- Boilerplate opens differently by length on purpose: 50 words leads with structure, 100 with the stake. Not a drafting inconsistency, and not to be harmonised.
- The `/about/` pillar taglines are canonical.
- Sustainability is real ongoing work that is under-evidenced in public. The fix is proof points, not better adjectives.
- "Over 250 projects" now lives in `truths/open-home-foundation/`; `truths/core/` cites it.

## Website follow-ups (not brand-system work)
- The home page runs a superseded set of pillar taglines. The canonical set is in `brand/messaging.md`; the most-read surface disagrees with it.
- `truths/core/proof-points.md` recorded the project count as 257 against `/projects`, while `/` says "over 250". Confirm which is current before verifying.

## Codify queue
From the interview, in priority order: blog post → social post set, then partner announcement. Both go to `codify-workflow`. The first is the beat that prompted this onboarding.

## Deferred
- The UK→US spelling sweep across `core/` and `projects/home-assistant/`, agreed in interview but carried as its own pull request: it touches files the marketing team owns. See `decisions/2026-09-15-ohf-house-style.md`.
