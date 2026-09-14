# Audit checks

`scripts/audit.py` runs the deterministic checks, including `validate_project.py` on every project. The `audit-brand-system` skill adds the qualitative ones. Together they answer: is this repo still something an agent can load and trust?

## Deterministic (script)
| Check | Severity | Why |
|---|---|---|
| INDEX.md missing, or not pointing at `projects/REGISTRY.md` | error | Nothing loads without the router |
| Core file or skill not listed in INDEX.md | error | Invisible to agents |
| INDEX.md entry points at a missing path | error | Dead pointer wastes a turn |
| INDEX.md lists individual projects | warn | That is the registry's job; the index has a 60-line budget |
| REGISTRY.md missing or stale against the manifests | error | Agents find projects through it |
| Project spec violation on a `validated` or `live` project | error | The contract is broken where agents build |
| Project spec violation on an earlier-status project | observation | Expected at that stage; the pipeline is working |
| Project not moved in 30 days and not live | warn | Stuck onboarding |
| SKILL.md missing name or description | error | Cannot trigger |
| SKILL.md over 300 lines | warn | Split into references |
| Skill without evals or fewer than 3 cases | warn | A skill without evals is a draft |
| Production skill without evals | error | Cannot be trusted |
| Truth missing source, valid_from, review_by or owner | error | Undated fact is a rumour |
| Truth past review_by | error | Stale facts propagate |
| Proof point with Verified empty or Never | warn (error on a live project) | Not usable by skills |
| Example with fewer than 2 why_it_works items, or no project | warn / error | Teaches nothing; cannot be found |
| Duplicate paragraph across directories | warn | Drift risk; point to one source |
| OWNERS.md missing a row for core, truths, skills or projects | error | Nobody prunes |
| Standard missing standard, title, scope, owner or last_reviewed | error | The validator cannot apply it |
| Shared standard that binds to nothing | error | Applies to no project; probably a typo in the binding |
| Shared standard coverage (n of m applicable projects have a conformance file) | observation | The number that matters at scale |
| Applicable shared standard with no conformance file | warn before grace_until, error after | Grace lets existing projects catch up |

## Project spec (validate_project.py)
| Check | Why |
|---|---|
| Required files for the tier exist | Same shape everywhere |
| Required `##` headings per file | Agents find sections by heading |
| voice.md: Sounds-like rows; each rule has Yes and No; at least 3 real rules for active and flagship | Rules without pairs are adjectives |
| messaging.md: a `###` per pillar in PROJECT.md; a `###` per audience in audiences.md; three boilerplate lengths | The hierarchy holds together |
| Banned words in positioning, key messages, boilerplate | They describe nothing |
| audiences.md sections have Cares about and Found on | Key messages need something to aim at |
| channels.md and modes.md tables have the required columns and rows | Skills read them by position |
| Pillars in PROJECT.md exist in core/pillars.md | No project invents a pillar |
| Proof-points table has the six columns | Skills copy approved phrasing by column |
| `live`: zero TODOs, no `draft: true`, verified proof points, 3 examples for flagship | Live means agents may build against it |

## Qualitative (skill)
- Pipeline health: count per status, stuck projects, their owners.
- Adjectives without consequences in core and live voice files.
- Trigger accuracy: run each skill's trigger cases against every description.
- Restated truths: figures in skills or messaging that differ from truths.
- Voice leakage: project files that criticise companies or speak for the foundation.
- Escalation coverage: output types with no row in core/escalation.md.
- Decisions without effect: `affected` files that did not change.
- Orphans and unused.

## Report format
```
# Brand system audit: <date>
## Errors (fix before next use)
## Warnings (fix this month)
## Observations
## Recommended next three actions
```
