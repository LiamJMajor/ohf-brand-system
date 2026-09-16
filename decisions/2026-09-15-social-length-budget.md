---
date: 2026-09-15
area: brand/style
project: open-home-foundation
trigger: correction
change: The social character budget was wrong and truncated a post. The real limit is 256 weighted characters of body including line breaks, not 280 with the link excluded
affected:
  - projects/open-home-foundation/brand/style.md
  - projects/open-home-foundation/brand/voice.md
  - examples/open-home-foundation/social-post/2026-09-community-day-countdown.md
by: @liam
---

# The social length budget was wrong

`brand/voice.md` and the Community Day example both said "under 280 characters of body, link excluded (the X and Bluesky cap)". Both halves of that are wrong, and they are wrong in the same direction, so a post that measured as comfortably inside the limit truncated on X.

## What X actually counts
- **Any URL costs 23**, however short. `https://luma.com/t13dc6er` is 25 characters and costs 23; a 200-character URL also costs 23. It is never excluded.
- **Each emoji costs 2.** House style puts one in the opening line and a 👇 at the link, so every conforming post spends 4 before a word is written.
- The blank line before the link costs 1.

280 minus 23 minus 1 leaves **256 for the body**. Bluesky allows 300 and counts the URL at its real length, so anything that clears X clears Bluesky. X is the binding constraint and the only one worth measuring.

## How it surfaced
A Lisbon meetup post was drafted, measured at 277 by the old rule, and truncated on X: its real cost was 303. It lost its last line, which carried the remaining-spaces count. The working version came in at exactly 280.

## Why nobody caught it sooner
The Community Day example that the rule was inferred from measures 279 to 281, depending on whether X counts the skin-tone modifier in 👇🏼 as part of one emoji. It sits on the cap either way. Every approved post to date happened to be short enough that a rule giving 24 characters of phantom headroom never cost anything. The first slightly longer post paid for all of them.

## What changed
`brand/style.md` gains a Social length budget section with the arithmetic and a one-line command that counts a body correctly. The Modes table in `brand/voice.md` now cites it instead of restating the wrong number. The example file is annotated rather than edited, following the precedent set for the ampersands in the same file: the post is what it is, and the note explains why it does not teach what it appeared to teach.

## What this does not settle
The 23-character URL cost is X's documented behaviour and is stable, but the emoji weighting and the treatment of modifier sequences are worth re-checking if posts start truncating again. The counting command in `style.md` is an approximation of X's weighting table, deliberately pessimistic by a character or two. Nobody has measured Mastodon or LinkedIn, because neither has been the constraint.
