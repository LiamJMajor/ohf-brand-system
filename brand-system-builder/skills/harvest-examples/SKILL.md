---
name: harvest-examples
description: >
  Collect a project's best past work (posts, release notes, decks, pages, graphics) from its repo, site, blog, Slack or files, select the strongest, and file each under examples/<slug>/<type>/ with concrete why-it-works notes and near-misses. Use this whenever someone wants to gather examples, build a reference library, "show the model what good looks like", get a flagship project to live status, or asks what to do with a folder of old assets. Do not use it to write rules from an expert (capture-judgment).
---

# Harvest examples

Examples are where taste lives in a form a model can use. A flagship project cannot go live without at least three, and skills load them by project and output type, so this skill is picky about selection and strict about annotation.

## Where the repo is
The brand system is the current working directory or the nearest parent containing `INDEX.md`, `core/` and `projects/`; the scripts find it the same way when given no path. If the user is not inside a clone, get them into one before writing anything. Before the first write: `git fetch origin && git switch -c <type>/<slug> origin/main`, so the work starts from the current remote regardless of the clone's age. Finish with a commit and a pull request to the area owner. Read `${CLAUDE_PLUGIN_ROOT}/references/working-in-the-repo.md` for the flow.

## Intake
- **Project slug** and its `voice.md`, which you read first so selection is against the confirmed rules.
- **Type(s)**: release post, feature short, social post, deck, landing page, product graphic. Match skill names where they exist.
- **Sources**: the project's blog, release notes, social, community posts, local folders.
- **Who judges**: the maintainer interviewed in capture-judgment. If unavailable, select conservatively and set `pending_review: true`.

## Select
Follow `${CLAUDE_PLUGIN_ROOT}/references/annotation-protocol.md`.
- Three to six per type. Five strong beats forty average.
- Cover Low, Medium and High impact modes where the type has range.
- One near-miss per type, labelled, with what was wrong and the fix.
- Nothing older than the project's current identity.
- Prefer pieces that pass every contrast pair in `voice.md` cleanly.

## Annotate
`examples/<slug>/<type>/<yyyy-mm>-<slug>.md` from `${CLAUDE_PLUGIN_ROOT}/templates/example.template.md`. Frontmatter `project: <slug>`. At least two `why_it_works` items you could point at in the text. "Great tone" fails the audit. Include `## What not to copy`. Excerpt long pieces and link the source.

## File and log
- `decisions/<date>-harvest-<slug>-<type>.md`: sources scanned, selected, rejected, who judged.
- If this completes a flagship project's examples, tell the user it can move to `live` via `onboard-project` stage 5.

## Report
Per type: selected, near-misses, rejected count, pending review. Then the gaps: types and modes with nothing yet. Those gaps are why `codify-workflow` for that type on this project should wait.
