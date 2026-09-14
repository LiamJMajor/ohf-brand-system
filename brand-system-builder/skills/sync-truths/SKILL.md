---
name: sync-truths
description: >
  Refresh the dated facts under truths/ from their authoritative sources: GitHub releases, docs, changelogs, project pages, and verify proof points against their sources. Use this whenever a release ships, someone asks "is the repo up to date", a truth is past its review date, a proof point is unverified, the audit reports stale truths, or on a schedule. Also use it to add a truth file skills keep needing. Do not use it for a single human correction (promote-correction).
---

# Sync truths

Truths are the fast layer. Skills cite them by path and copy approved phrasing verbatim, so one update propagates everywhere. This skill keeps them current, keeps their history, verifies proof points, and reports downstream content that restated an old value.

## Where the repo is
The brand system is the current working directory or the nearest parent containing `INDEX.md`, `core/` and `projects/`; the scripts find it the same way when given no path. If the user is not inside a clone, get them into one before writing anything. Before the first write: `git fetch origin && git switch -c <type>/<slug> origin/main`, so the work starts from the current remote regardless of the clone's age. Finish with a commit and a pull request to the area owner. Read `${CLAUDE_PLUGIN_ROOT}/references/working-in-the-repo.md` for the flow.

## Find what needs syncing
1. List every file under `truths/`, frontmatter only.
2. Flag: `review_by` past; source changed since `valid_from` (compare latest release tag to the one recorded; for web pages, fetch and compare the relevant section); proof-point rows with Verified empty or "Never".
3. If the user named an event (a release, a rename), start there.

## Update current-release
1. Fetch the release. Extract only what a skill would state: version, date, headline features, breaking changes, links.
2. Diff. Move old lines to `## Superseded` with `(until <date>)`. Write the new lines.
3. `valid_from` = release date; `review_by` = next expected release; `source` = the exact tag URL.
4. Do not infer. If the source does not say it, the file does not say it.

## Verify proof points
For each unverified row: open the Source, confirm the Canonical figure, update it if it moved, and set Verified to today. If the source no longer supports the claim, do not delete the row; mark Verified "failed <date>" and route to the truths owner. A skill treats anything not verified as unusable.

## Adding a truth
`truths/<slug>/<topic>.md` from `${CLAUDE_PLUGIN_ROOT}/templates/truth.template.md`. No index change needed; skills find truths by project slug.

## Downstream check
Search `skills/`, `examples/<slug>/` and `projects/<slug>/messaging.md` for superseded values. Boilerplate that restated a figure instead of matching the proof point is a defect; fix it.

## Log and report
One `decisions/<date>-sync-<slug>.md` per run, `trigger: release`. Report a table: truth, old, new, source, next review; verified count; downstream files fixed or listed.

## Scheduling
Safe to run unattended for release-backed truths. If the organisation already has a release-detection skill or job, chain this after it so the truth updates the same hour the release lands.
