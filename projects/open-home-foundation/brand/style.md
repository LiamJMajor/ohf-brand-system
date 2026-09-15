---
area: brand/style
project: open-home-foundation
owner: @liam
last_reviewed: 2026-09-15
review_every: 180d
draft: true
---

# Open Home Foundation: style

Mechanics. The things agents get wrong most often. Drafted 2026-09-15 by observing published copy rather than by asking. Two of the observations contradict this repository's own core files; both are flagged below and need a ruling, not a guess.

## Spelling and grammar
- Spelling convention: **US**, observed. The survey post uses "anonymized"; the IFA post uses "organizations" and "monetization". ⚠️ Conflict: `core/` is written in UK English ("criticises", "organisation", "recognisable"). Published copy and the brand system disagree. Ruling needed: does the ruling apply to published output only, or to the repository too?
- Serial comma: **yes**, observed. "privacy, choice, and sustainability" on the home page, the about page and in the IFA post title. ⚠️ Conflict: `core/story.md:19` writes the thread as "privacy, choice and sustainability" without it. One of the two is wrong and the thread is the more visible of the two.
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
The IFA 2026 post reproduces a cross-stitch reading "fuck VCs and private equity" in foundation voice on the foundation's own blog. Either profanity is permitted in specific circumstances — quoting an artefact, community register — or that post is a precedent to correct. This is the single highest-value ruling in this file, because an agent has no way to infer it and will either sanitise the foundation's actual voice or swear on its behalf. TODO interview.
