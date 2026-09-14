---
name: capture-judgment
description: >
  Interview a maintainer, designer, writer or comms lead about one project (or the foundation voice) and turn their taste into the project's spec files: voice rules with contrast pairs, messaging hierarchy, modes, and the escalation boundaries they insist on. Use this whenever someone wants to document a project's voice or messaging, "get what's in X's head into the repo", confirm drafted brand files with a maintainer, or turn an existing style guide into something an agent can follow. Also use it when a user pastes brand guidelines and asks what to do with them. Do not use it to collect finished examples (harvest-examples) or to build a workflow (codify-workflow).
---

# Capture judgment

Judgment lives in people's heads and in the fixes they make to other people's drafts. This skill gets it out as decisions with reasons and files it into `projects/<slug>/`, in the spec's headings, so the validator can check it and skills can load it.

## Scope
One project per interview. Confirm the slug and open its current files; `onboard-project` usually leaves drafts marked `draft: true`. The interview confirms, rejects or replaces each draft item. For the foundation voice, the project is `open-home-foundation` and the interviewee is whoever holds the cause, not a product.

## Who to interview
The person who fixes the most drafts for that project. Not necessarily the most senior.

## Run the interview
Follow `${CLAUDE_PLUGIN_ROOT}/references/interview-protocol.md`. Six short rounds around real pieces of work:
- Start from a piece they fixed. Every "I'd change that every time" is a rule.
- For every rule, get the version they would reject. Write the pair verbatim.
- Ask when they break the rule (modes) and what they would never let a tool do alone (escalation).
- Walk the drafted `messaging.md` top down: positioning, each pillar translation, each key message, each boilerplate. They edit; you record.
- End with what people ask them for that they could do in their sleep. That is the codify queue.

Asynchronous: ask in batches of three and wait. Pasted guideline: treat each statement as a candidate rule and run the contrast test; if no rejected version can be written, it is an adjective and is dropped or rewritten.

## Write it up
Into the project's spec files, keeping the required headings from `${CLAUDE_PLUGIN_ROOT}/references/project-spec.md`:
1. Rules into `voice.md` under `## Rules`, each an `###` with the rule, the reason, `- Yes:` and `- No:`. Confirmed rules lose their `(draft)` marker.
2. Messaging edits into `messaging.md`. Any new fact goes to `truths/<slug>/proof-points.md` with source.
3. Modes into `modes.md`.
4. Project-specific boundaries into `voice.md` under `## Never`. Anything that applies to every project is a proposal for `core/escalation.md`; log it in `decisions/` and route to the core owner rather than editing core directly.
5. Proud pieces become the handoff list for `harvest-examples`. The queue becomes the list for `codify-workflow`.
6. Set `draft: false` on confirmed files. Set `status: interviewed` in `PROJECT.md`. Log `decisions/<date>-interview-<slug>.md`.
7. Run the validator and report its result.

## Quality bar
- Every rule has a contrast pair. Count them.
- No rule could apply to any project unchanged.
- Every escalation proposal is checkable from the intake or the draft.
- Nothing from an old guideline was copied without passing the contrast test.

## Report
Rule count, pillar translations confirmed, boilerplate confirmed, validator errors remaining, then the two handoff lists in priority order.
