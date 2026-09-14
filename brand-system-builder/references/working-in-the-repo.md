# Working in the brand system repository

The brand system is a git repository. Nobody edits it in place on a shared drive, and nobody's laptop path is special. Every skill assumes this flow.

## Where the repo is
The current working directory, or the nearest parent that contains `INDEX.md`, `core/` and `projects/`. The scripts find it the same way, so `python3 .../audit.py` with no argument works from anywhere inside a clone. If the skill is invoked from outside a clone, ask for the path or offer to clone:
```
git clone git@github.com:<org>/<brand-system>.git
cd <brand-system>
claude
```
Never write brand system files anywhere else. If the user is not in a clone, stop and get them into one.

## Readers and contributors are different
People and agents that *build to* the brand system read it from `main` on GitHub: through the installed brand-system plugin, or by fetching files at read time. They never keep a clone, so they are never stale. Only people *changing* the brand system clone it.

## Freshness for contributors
A clone is only as current as its last fetch. Three guards, in order of strength:
1. Branch from the remote, never from local main: `git fetch origin && git switch -c <type>/<slug> origin/main`. The age of the clone stops mattering.
2. The scripts fetch and warn when the checkout is behind `origin/main` or when there are uncommitted changes on main. Do not ignore the warning.
3. Pull requests to `main` require the branch to be up to date before merging (enable "require branches to be up to date" on the repository). A stale branch is caught even if the first two were skipped.

## How changes get in
1. Fetch, then start on a branch from `origin/main` named for the work: `onboard/<slug>`, `correction/<slug>-<topic>`, `standard/<slug>`, `sync/<slug>`.
2. Do the work. Run the validator (and the audit for anything touching core or standards) before committing. A commit that leaves the validator failing on a live project is not made.
3. Commit with a message that names the skill and the project. Every skill run that changes files ends with an offer to commit; take it unless the user says otherwise.
4. Push the branch and open a pull request to `main`. The reviewer is the owner of the area in `OWNERS.md` or the project owner in `REGISTRY.md`. Corrections to `core/` go to the core owner.
5. The `decisions/` entry travels in the same pull request as the change it explains.

Direct commits to `main` are for the core owner and for automation (`sync-truths`, the audit report) only.

## Concurrency
Two people onboarding two projects touch different directories and never conflict. Two people editing the same project's brand files do, which is why one interview owns a project at a time; the registry status tells you if someone is mid-onboarding.

## What lives where
| Thing | Where | Cloned by |
|---|---|---|
| The builder (skills, scripts, spec) | its own repository, installed as a plugin | almost nobody; installed, not cloned |
| The brand system (core, projects, truths, examples, skills) | its own repository | everyone who contributes |
The two can share one repository while a team is small. Split them when contributors to the brand system stop caring about the builder's internals.
