# Defining escalation rules

Escalation rules are what make a self-serve system trustworthy. They state, in advance, what the system will not do alone. Without them, people discover the boundary by shipping something wrong.

## The file
`foundation/escalation.md` is a table of trigger → route → why. Skills read it before producing output and check their intake against it.

| Trigger | Route | Why |
|---|---|---|
| New product or feature name | Brand lead | Naming is identity work |
| Security incident or vulnerability | Security lead + comms lead | Legal and trust stakes |
| Pricing, licensing or partnership terms | Leadership | Commitments |
| Anything mentioning a competitor by name | Comms lead | Legal review |
| First-ever communication to a new audience | Brand lead | No examples yet to ground the work |
| Output the skill's rubric scores below threshold | Human review | Honest about reliability |

## Writing good triggers
- Observable from the intake or the draft, not from intent. "Mentions pricing" is checkable. "Is sensitive" is not.
- Specific enough that two people would agree whether it fired.
- Includes the fallback: what the requester gets while waiting. Usually a draft clearly marked as needing review, plus the name of who reviews.

## Reliability tiers for skills
Every skill declares one in frontmatter:
- `draft`: output always goes to a human before use.
- `beta`: output can be used by the requester after their own review; the brand team samples.
- `production`: output can ship. Escalation rules still apply.

A skill moves up a tier only after `evaluate-skill` shows it passes and the brand team has sampled real outputs. It moves down the moment a bad output ships.
