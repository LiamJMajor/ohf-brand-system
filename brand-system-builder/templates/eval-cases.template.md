---
skill: {{SKILL_NAME}}
rubric: evals/rubrics/on-brand.md
---

# Eval cases: {{SKILL_NAME}}

Each case is a realistic request. `evaluate-skill` runs each in a fresh context and grades the output.

## Case: {{CASE_SLUG}}
**Prompt:** {{REALISTIC_REQUEST}}
**Must include:**
- {{OBSERVABLE_REQUIREMENT}}
**Must not include:**
- {{OBSERVABLE_FAILURE}}
**Notes:** {{WHY_THIS_CASE_MATTERS}}

## Trigger cases
Should trigger this skill:
- {{PHRASE}}
Should not trigger this skill (and which skill should):
- {{PHRASE}} → {{OTHER_SKILL}}
