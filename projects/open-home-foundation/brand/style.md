---
area: brand/style
project: open-home-foundation
owner: @liam
last_reviewed: 2026-09-15
review_every: 180d
draft: true
---

# Open Home Foundation: style

Mechanics. The things agents get wrong most often. Drafted 2026-09-15 by observing published copy; the three rulings below were settled in interview on 2026-09-15.

## Spelling and grammar
- Spelling convention: **US English**, in published output *and* in this repository (interview 2026-09-15). Observed in published copy: "anonymized", "organizations", "monetization". The core files were written in UK English and are being corrected to match; until that sweep lands, trust this rule rather than the spelling of the file you are reading. See `decisions/2026-09-15-ohf-house-style.md`.
- Serial comma: **yes**, always, including in the thread (interview 2026-09-15). "privacy, choice, and sustainability". `core/story.md:19` omitted it and was corrected in the same pull request; every public surface already used it.
- Contractions: yes. "we're no ordinary foundation", "here's all you need to know", "don't require".

## Capitalisation
- Headings and blog titles: sentence case. "Making room for privacy, choice, and sustainability at IFA 2026". "A big win for Android interoperability". Proper nouns keep their capitals.
- Subheads within a post: sentence case. "Opening the doors to the public", "People at the heart of the home".
- Colon constructions in titles capitalise the second half: "Anonymous and open to all: The Home Assistant survey dataset", "Proxy all the things: no device left behind". ⚠️ Inconsistent in the wild: the first capitalises after the colon, the second does not. TODO rule.
- Project and organisation names: see naming.md.

## Numbers and dates
- Numbers: figures with thousands separators, "8,616 Home Assistant users". Approximations spelled as "over 250", not "250+".
- Dates: "Saturday, November 7, 2026" (US long form, weekday first where the day matters). Ranges: "From September 4 to 8, 2026". Short form in social copy abbreviates the month and drops the year when it is obvious: "starting Sept 17" (example 2026-09-15).
- Read time appears on blog posts as "5 minute read". TODO confirm whether this is authored or generated.

## Punctuation
- **Em dashes: never.** Not in published copy, in any register, on any surface (interview 2026-09-15). Use a colon, a full stop, a comma, or a line break. This is the single most common way drafted copy gives itself away, and an agent will reach for one roughly every second paragraph unless told not to.
  - Yes: "We're closing our merch store‼️ / (temporarily)". A line break carries it
  - Yes: "the answers are yours!" / "now free for everyone: a rich dataset published openly"
  - No: "We built a living room at IFA Berlin — sofas, plants, coffee."
- En dashes in number ranges are fine ("September 4–8"), though "from 4 to 8 September" reads better in prose.
- **Ampersands: never.** Always "and", in every register including social (interview 2026-09-15). The only exception is a name that contains one ("Product & UX" as a job title).
  - This was briefly recorded as the opposite, inferred from a single approved post that uses "hosts & guests" and "& more". One post is not a pattern, and the ruling went the other way. That post is annotated as an outlier in `examples/open-home-foundation/social-post/2026-09-community-day-countdown.md`.

## Formatting
- Links: descriptive text. TODO confirm the rule for linking to a project's own site versus the foundation's.
- Emphasis: TODO. Bold subheads appear in the IFA post; unclear whether that is house style or that author's.
- Quotes from people: TODO. The IFA post quotes a contributor by first name only ("Web developer Darren"); `/about/` quotes the president in full. Confirm the rule for first name, full name, and role.
- Emoji: **yes on social, and expected** (examples 2026-09-15). Every approved social post carries at least one. The pattern is one in the opening line carrying the mood (‼️ 🥳 🎉 👀) and a 👇 immediately before the link. Blog prose is a different surface and carries none. An emoji-free foundation social post reads as somebody else's copy.
- Social posts end with the link alone on its own line, preceded by a 👇 pointer.

## Glossary
Terms the foundation uses in a specific sense, where a writer would otherwise reach for a loose synonym. Drafted from observed usage; the interview confirms and extends.

| Term | Means | Not |
|---|---|---|
| the open home | the cause: a smart home that is private, offers choice, and is sustainable | a product, a certification, or a brand |
| local control | the home works without an internet connection, and cloud is opt-in | "cloud optional" as a pricing tier |
| collaboration partner | an organisation working with the foundation on interoperability, e.g. OpenDisplay | commercial partner, which is the funding relationship (Apollo Automation, Nabu Casa) |
| commercial partner | contributes a majority of profit from licensed products; may license foundation brands | sponsor, donor, or customer |
| stewarded | the foundation owns and governs a project so it cannot be sold or abandoned | maintained, or funded |
| TODO | TODO | TODO |

## Strong language
Permitted wherever it is earned, in the foundation's own sentences as well as in quoted artefacts (interview 2026-09-15). The foundation is anti-corporate by design and says so plainly.

Earned is the operative word and it is checkable: the profanity has to be carrying the point. "fuck VCs and private equity" on a cross-stitch at IFA names the specific thing the foundation's structure exists to prevent (https://www.openhomefoundation.org/blog/making-room-for-privacy-choice-and-sustainability-at-ifa-2026/). Profanity as intensifier ("this is a fucking great release") is doing no work and is just noise in a different register.

- Yes: "fuck VCs and private equity"
- No: "this update is fucking great". Intensifier doing no work

This rule is the foundation's, not the ecosystem's. Project voices inherit nothing from it; a project wanting the same latitude asks for it in its own `voice.md`.

### Censoring on social, and only on social
On social channels, write "f\*ck". One asterisk, second character (correction 2026-09-15).

Two different reasons to soften a word, and only one of them is allowed:

| Reason | Ruling |
|---|---|
| To sound more respectable, or because it feels risky | Never. This concedes the argument the language is making, and it is what the interview ruling was written against |
| Because a platform's ranking may penalise the post and fewer people will see it | Allowed, on social only. The word is not the goal; the argument reaching people is |

**The basis is unverified.** The belief is that social platforms down-rank posts containing profanity. It was recorded as a belief, not a finding, by the person who made the call. Nobody has tested it here, platform behaviour differs between organic reach and anything promoted, and it changes without notice.

What would settle it: run the same post censored on one network and uncensored on another with comparable audiences, and compare reach. Until somebody does, this is a cheap hedge carrying a real cost, and it should be revisited rather than inherited.

Everywhere else — the blog, the website, press materials, the printed artefacts themselves — stays uncensored. A cross-stitch does not have an algorithm.

## Constructions that give a draft away
Banned outright (interview 2026-09-15). These are the shapes generated copy falls into, and they are all recognisable enough that a reader discounts everything around them.

| Never | Why | Instead |
|---|---|---|
| "It's not X, it's Y" and every variant: "X isn't just Y, it's Z", "Most people do X. We did Y." | The negative-parallel setup. It manufactures a contrast the reader did not ask for, and it is the single most recognisable tell | State the thing. "We built a living room at IFA Berlin." |
| The standalone summary sentence: "That's the point." "Both halves are the argument." "And that changes everything." | A short declarative closing a paragraph to tell the reader what they just read means. Condescending, and always cuttable | Cut it. If the paragraph did not land, fix the paragraph |
| Triads that escalate into abstraction: "no account, no subscription, no compromise" | The first two are concrete, the third is filler carried by rhythm | Two concrete items beat three where the third is decoration |
| "Here's the thing", "Let's be clear", "The reality is" | Throat-clearing that promises candour instead of being candid | Delete and start at the next word |

The house alternative is visible in every approved example: open with the news, give the facts, point at the link. The foundation's own posts do not argue by construction, they argue by what they show.
