---
name: audit-brand-system
description: >
  Health-check a brand system repo: projects failing the spec, stuck onboarding, stale registry, stale truths and unverified proof points, files missing from the index, oversized or eval-less skills, vague triggers, duplication, adjectives without rules, missing owners. Use this whenever someone asks if the repo is healthy, before expanding scope or onboarding a batch of projects, on a monthly cadence, when outputs drift, or when someone says "it's getting unwieldy". Produces a prioritised report and offers to fix.
---

# Audit brand system

An agent-loaded repo with hundreds of projects decays in predictable ways: projects stall mid-onboarding, the registry drifts, facts go stale, rules turn back into adjectives, skills grow past budget, nobody deletes. This audit catches those before people meet them in the output.

## Deterministic checks
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/audit.py <repo>
```
This runs the project validator across every project, checks the registry against the manifests, and checks index, truths, skills, examples, owners and duplication. `${CLAUDE_PLUGIN_ROOT}/references/audit-checks.md` explains each check. Spec gaps on projects not yet `validated` are reported as observations, not errors: they are expected at that stage.

## Qualitative checks
1. **Standards coverage.** The script reports, per shared standard, how many applicable projects have a conformance file, and flags standards that bind to nothing. Standards past their grace date with missing conformance are errors on live projects.
3. **Pipeline health.** From `projects/REGISTRY.md`: how many at each status; which have not moved in 30 days; whose owner they are. Stuck projects are the most common failure at scale.
3. **Adjectives without consequences.** Read `core/*.md` and the `voice.md` of live projects. Any brand description with no rule, reason or pair attached. Quote it.
4. **Trigger accuracy.** Per skill, run the trigger cases from `evals/cases.md` against every skill description. Report wrong fires and misses.
5. **Restated truths.** Search `skills/` and `projects/*/messaging.md` for figures that differ from `truths/`.
6. **Voice leakage.** Live project files that criticise other companies or speak for the foundation, against `core/voices.md`.
7. **Escalation coverage.** Output types skills produce with no applicable row in `core/escalation.md`.
8. **Decisions without effect.** Sample recent entries; confirm `affected` files changed.
9. **Orphans and unused.** References nothing points to; skills or examples with no decision or eval in a quarter.

## Report
The format in `audit-checks.md`: errors, warnings, observations, then the next three actions ranked by what would most likely produce a bad output next week. One line per finding plus path.

## Offer to fix
Script errors are mechanical: regenerate the registry, add the index line, fill frontmatter, split a file. Offer to fix in one pass. Qualitative findings route to owners from `OWNERS.md` and `REGISTRY.md`; name them.

## Cadence
Monthly, and before any batch onboarding or new skill. A repo failing audit does not get more surface area. Suggest a scheduled task posting the report to the brand team's channel.
