# Annotating examples

An example teaches only as much as its annotation explains. The file is for a model as much as for a person, so annotations are concrete and observable.

## Selecting
- Choose the best, not the most. Five strong examples beat forty average ones.
- Cover the range of modes: at least one quiet, one standard, one loud per type where they exist.
- Include at least one near-miss per type: work that was almost right, with what was wrong. Label it clearly.
- Prefer recent work. Anything older than the current identity is a historical note, not an example.

## Annotating `why_it_works`
Each item is something you could point at in the text or design:
- "Opens with the user's problem in the first sentence"
- "Every version number links to its release notes"
- "Uses 'you' throughout; never says 'users'"
- "Stops at 380 words; no summary paragraph"

Not acceptable: "great tone", "feels on-brand", "clear". If you cannot point at it, keep asking why until you can.

## Body of the example file
1. Frontmatter per `frontmatter-schemas.md`.
2. `## Context`: two or three sentences on the situation. Who asked, what for, what constraints.
3. `## The work`: the text itself, or for visual work a description plus a link. Excerpt if long, and say what was cut.
4. `## Why it works`: the frontmatter list expanded with one sentence each.
5. `## What to copy` and `## What not to copy`: because even good examples have parts that were specific to their moment.

## Near-misses
Same structure, plus `## What was wrong` and `## The fix`. Set `type` to the real type and add `near_miss: true` to frontmatter.
