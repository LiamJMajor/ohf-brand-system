---
name: evaluate-skill
description: >
  Run a brand-system skill against its eval cases in fresh contexts, grade each output with the shared rubric and the case's must/must-not lists, report a pass rate and failure patterns, and propose edits to the skill. Use this whenever someone asks whether a skill works, wants to test or benchmark it, wants to move it from draft to beta or production, or after codify-workflow or promote-correction changed a skill. Do not use it to write eval cases from scratch for a skill that has none; that is codify-workflow.
---

# Evaluate skill

A skill that has not been run against realistic requests is a draft, whatever its frontmatter says. This skill runs the cases, grades honestly, and turns failures into specific edits. Its job is to answer one question: would this ship without a human rebuild?

## Where the repo is
The brand system is the current working directory or the nearest parent containing `INDEX.md`, `core/` and `projects/`; the scripts find it the same way when given no path. If the user is not inside a clone, get them into one before writing anything. Before the first write: `git fetch origin && git switch -c <type>/<slug> origin/main`, so the work starts from the current remote regardless of the clone's age. Finish with a commit and a pull request to the area owner. Read `${CLAUDE_PLUGIN_ROOT}/references/working-in-the-repo.md` for the flow.

## Intake
- Which skill. Confirm `skills/<name>/evals/cases.md` exists with at least three cases across at least two live projects. If not, stop and route to `codify-workflow`.
- Rubric: from the cases frontmatter, default `evals/rubrics/on-brand.md`.
- How many runs per case. Default one. Use three when deciding a reliability tier change, because output varies.

## Run
For each case, run the skill in a fresh context so nothing leaks between cases. Two options:
- **Subagent**: launch a general-purpose agent with the case prompt and instructions to follow `skills/<name>/SKILL.md` in the target repo, loading only what it says to load. Ask it to return the output and the files it loaded.
- **CLI**: `claude -p "<prompt>"` from the target repo directory with the skill installed. Use this when the user wants results they can reproduce.

Record, per run: the output, the files loaded, whether the skill checked escalation, and the self-score it reported.

## Grade
Per run:
1. **Must include / must not include**: check each item literally. One miss fails the case.
2. **Rubric**: score each axis 1 to 5 against the rubric's anchors. Below 3 on any axis fails.
3. **Context discipline**: did it load only what the skill says, from the right `projects/<slug>/`? Loading the whole repo, or another project's files, is a failure even if the output was fine.
4. **Voice and pillar**: did it state which voice and which pillar? Wrong voice is a boundary failure.
5. **Editable**: could the requester change the output alone?

Be strict. The cost of a false pass is a designer rebuilding under deadline.

## Report
```
# Eval: <skill> on <date>
Pass rate: x/y cases (z runs)
| Case | Pass | Failed on | Lowest axis |
## Failure patterns
## Proposed edits to SKILL.md
## Tier recommendation
```
Failure patterns are the point. Three cases failing on the same axis is one edit, not three. Proposed edits are concrete: the line to change, the check to add, the example to harvest.

## Tier recommendation
- Below 70 percent: stay `draft`; make the edits; rerun.
- 70 to 90 percent with no truth or boundary failures: `beta`, requester reviews own output, brand team samples weekly.
- Above 90 percent over three runs per case, and the brand team has sampled real outputs: `production`.
Any truth or boundary failure blocks promotion regardless of rate.

## Heavier benchmarking
For variance analysis across many runs or description optimisation, the `skill-creator` plugin has scripts for it. Point the user there once the skill passes here.
