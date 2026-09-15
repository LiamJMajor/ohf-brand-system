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
- Colon constructions in titles capitalise the second half: "Anonymous and open to all: The Home Assistant survey dataset", "Proxy all the things: no device left behind". ⚠️ Inconsistent in the wild — the first capitalises after the colon, the second does not. TODO rule.
- Project and organisation names: see naming.md.

## Numbers and dates
- Numbers: figures with thousands separators, "8,616 Home Assistant users". Approximations spelled as "over 250", not "250+".
- Dates: "Saturday, November 7, 2026" (US long form, weekday first where the day matters). Ranges: "From September 4 to 8, 2026". TODO confirm the short form and whether the year is always written.
- Read time appears on blog posts as "5 minute read". TODO confirm whether this is authored or generated.

## Formatting
- Links: descriptive text. TODO confirm the rule for linking to a project's own site versus the foundation's.
- Emphasis: TODO. Bold subheads appear in the IFA post; unclear whether that is house style or that author's.
- Quotes from people: TODO. The IFA post quotes a contributor by first name only ("Web developer Darren"); `/about/` quotes the president in full. Confirm the rule for first name, full name, and role.
- Emoji: TODO. None observed in foundation blog copy, in contrast to Home Assistant's release posts, which fix "🎉" as house style. If the absence is deliberate, it is a rule worth writing down.

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
Permitted wherever it is earned, in the foundation's own sentences as well as in quoted artefacts (interview 2026-09-15). No channel carve-out, no asterisks, no "[expletive]". The foundation is anti-corporate by design and saying so plainly is the argument, not a lapse from it.

Earned is the operative word and it is checkable: the profanity has to be carrying the point. "fuck VCs and private equity" on a cross-stitch at IFA names the specific thing the foundation's structure exists to prevent (https://www.openhomefoundation.org/blog/making-room-for-privacy-choice-and-sustainability-at-ifa-2026/). Profanity as intensifier — "this is a fucking great release" — is doing no work and is just noise in a different register.

- Yes: "fuck VCs and private equity"
- No: "f**k VCs and private equity" — sanitising it concedes the point
- No: "this update is fucking great" — intensifier, not argument

This rule is the foundation's, not the ecosystem's. Project voices inherit nothing from it; a project wanting the same latitude asks for it in its own `voice.md`.
