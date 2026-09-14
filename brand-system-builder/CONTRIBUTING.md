# Contributing to the builder

This repo is the tooling layer. Changes here affect every brand system built with it, so keep it general.

## Adding or changing a skill
- One skill per folder under `skills/`, with a `SKILL.md` and optional `references/`, `scripts/`, `assets/`.
- Frontmatter needs `name` and `description`. The description is the trigger: say what the skill does and the phrases that should invoke it. See `references/trigger-writing-guide.md`.
- Keep `SKILL.md` under 300 lines. Push detail into `references/` and point to it with a sentence saying when to read it.
- Write in the imperative. Explain why a step matters instead of shouting MUST.
- Anything org-specific belongs in the produced brand system, not here. Use placeholders.

## The spec
`references/project-spec.md` is the contract. Changing a required file, heading or frontmatter field means changing `templates/project/`, `scripts/validate_project.py` and the spec together, in one pull request, and re-validating a scaffolded repo.

## Seeds
`seeds/<org>/` holds an org's shared core distilled from its human-readable strategy document, plus `projects.csv`. Seeds carry placeholders for owners and dates. When the strategy doc changes, the seed changes and the change is logged in the produced repo's `decisions/`.

## Templates
Templates in `templates/` are copied into the produced repo by `scripts/scaffold.py`, `scripts/new_project.py` and by skills. Placeholders use `{{DOUBLE_BRACES}}`. If you add a placeholder, add it to the scaffold script.

## Scripts
Plain Python 3, standard library only, so they run anywhere Claude Code runs. Every script prints a short usage on `-h`.

## Review
Open a pull request. Run `python3 scripts/audit.py <a-test-brand-system>` against a scaffolded repo before merging changes to templates or the audit.
