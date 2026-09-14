---
name: define-standard
description: >
  Add or change a standard in the brand system: an org-wide practice such as SEO, accessibility, website structure, social profile setup, video captions, or any rule set that should apply across projects or outputs without editing every skill. Use this whenever someone says "we need a standard for X", "add SEO best practices", "every project site should have Y", "make all decks do Z", wants to change what a standard requires, or wants to promote a project's own practice to the whole organisation. Do not use it for one project's voice or messaging (capture-judgment) or a single correction (promote-correction).
---

# Define standard

A standard is one markdown file in the brand system. The validator, the audit and every skill read standards from the repo, so adding one changes what agents check and load without any code or skill edit. This skill helps the marketing team write that file well and see where it lands.

## Where the repo is
The brand system is the current working directory or the nearest parent containing `INDEX.md`, `core/` and `projects/`; the scripts find it the same way when given no path. If the user is not inside a clone, get them into one before writing anything. Work on a branch and finish with a commit and a pull request to the area owner. Read `${CLAUDE_PLUGIN_ROOT}/references/working-in-the-repo.md` for the flow.

## Intake
1. **What it governs**, in one sentence, and the failure it prevents.
2. **Scope**:
   - `core`: applies to outputs everywhere; no per-project file. SEO, accessibility, legal footer wording.
   - `shared`: an org-wide definition plus a per-project conformance file. Website structure, social profile setup, anything where each project has to say how it complies.
   - `project`: one project's own practice, living in that project's `standards/` folder. Promotable later.
3. **Binding** for shared and core: which surfaces (`website`, `docs`, `social-profiles`, `app-stores`, `github`), which output types (`blog-post`, `landing-page`, `home-page`, `social-post`, `deck`, `video`, `readme`), which tiers or named projects, or all. A standard that binds to nothing applies to nothing; the audit reports it.
4. **Grace period** for shared standards: the date after which a missing conformance file becomes an error rather than a warning. Default 90 days. Existing live projects keep their status until then.
5. **Owner** and review cadence.

## Write it
Copy `${CLAUDE_PLUGIN_ROOT}/templates/standard.template.md` to `core/standards/<slug>.md` (or `projects/<slug>/standards/<slug>.md` for project scope). Fill the frontmatter exactly; the validator reads it. Then the body:
- **Required elements**: each checkable by looking at the thing.
- **Rules**: decisions with a reason and a Yes and No pair. An adjective without a pair is not a rule.
- **Never**: the hard lines.
- **Machine checks**: what a script or agent can verify before a human sees the draft. This is what makes the standard cheap to enforce at scale. Write at least one.
Keep it under 200 lines. If it grows, split the detail into `core/standards/<slug>/` references and point to them.

## Wire it in
- Shared: for every project the binding applies to, create the conformance file from `${CLAUDE_PLUGIN_ROOT}/templates/standard-conformance.template.md`, or run `new_project.py --force` semantics per project. Existing projects get theirs as drafts with TODOs.
- Add one line to `INDEX.md` only if `core/standards/` is not already listed there; individual standards are never listed in the index.
- `decisions/<date>-standard-<slug>.md`: what it governs, why now, binding, grace date.

## Check it
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/audit.py <repo>
```
The audit reports the standard's coverage: how many applicable projects have a conformance file. Fix any frontmatter error it raises. Then run `validate_project.py` on one applicable project to see what its conformance file will demand.

## Promoting a project standard
When a second project wants a practice one project owns: copy the file to `core/standards/`, set `scope: shared`, bind it, give it a grace date, leave the original in place with a note pointing to core, and log the decision. If it turns out to need no per-project variation, set `scope: core` and `conformance: none`.

## Report
Slug, scope, binding, grace date, coverage from the audit, and which skills will now load it (those whose output types or surfaces match).
