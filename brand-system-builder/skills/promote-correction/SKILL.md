---
name: promote-correction
description: >
  Take a correction someone made to a draft (a Slack message, review comment, edit, "we don't say that") and route it into the brand system so it sticks: a proof point, a voice rule, a messaging line, a skill step, an example or an escalation boundary, in the right project's files, with a decision entry. Use this whenever someone fixes generated output, says "that's wrong", "we never say X", "the logo is out of date", or pastes feedback and wants it remembered. Also use it when a skill produced something that had to be rebuilt. Do not use it for bulk fact refreshes (sync-truths).
---

# Promote correction

A correction that lives in Slack is gone by lunch. This skill makes each one a commit in exactly one place, and keeps the repo from filling with rules that were one person's preference on one Tuesday.

## Intake
- The correction, verbatim if short; both versions if it is a diff.
- Who made it and their standing: project owner, requester, colleague.
- Which project, and which skill or file produced the draft.

## Classify
| Kind | Sign | Goes to |
|---|---|---|
| Fact | number, name, date, claim wrong or stale | `truths/<slug>/proof-points.md` or `current-release.md` |
| Voice | word choice, tone, structure they would change every time | `projects/<slug>/voice.md` under Rules, with the pair |
| Messaging | positioning, a key message, boilerplate | `projects/<slug>/messaging.md` |
| Naming | capitalisation, forbidden variant | `projects/<slug>/naming.md` |
| Visual | colour, type, logo use | `projects/<slug>/visual.md` |
| Wrong voice | should have been foundation voice, or vice versa | a case in `core/voices.md`, via the core owner |
| Skill step | wrong file loaded, check skipped, wrong format | `skills/<name>/SKILL.md` plus an eval case |
| Missing example | rule existed, output still missed | `examples/<slug>/<type>/` |
| Boundary | should have gone to a person | `core/escalation.md`, via the core owner |
| Standard | a practice every project or output should follow (SEO, captions, footer) | `core/standards/<std>.md`, via define-standard |
| One-off | specific to this piece | `decisions/` only |

Ask before writing a rule: **would this project's team make this change every time?** If not yes, log a one-off. Three matching one-offs in `decisions/` earn a rule.

## Apply
1. Change exactly one file. Other files cite by path.
2. Voice rules get the pair: corrected as Yes, original as No.
3. Facts: move the old value to Superseded with its end date; update `valid_from`, `review_by`, and Verified.
4. Skill steps: add the check to the review list and an eval case that would have caught it.
5. Bump `last_reviewed`. Run the validator on the project; a correction should never leave it failing.
6. `decisions/<date>-<slug>.md`, `trigger: slack` or `review`, with `project:`.
7. Search `skills/` and `examples/<slug>/` for the old version. Fix if small; otherwise list.

## Commit
Per the repo's `CONTRIBUTING.md`: branch and pull request to the project owner by default. Anything touching `core/` goes to the core owner.

## Report
Kind, file changed, decision entry, validator result, downstream restatements found. If one-off, say why and how many similar entries exist.
