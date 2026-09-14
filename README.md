# OHF Brand System

Two repositories, side by side.

| Folder | What it is | Status |
|---|---|---|
| `brand-system-builder/` | The Claude Code plugin that builds and maintains a brand system: 9 skills, 5 scripts, the project spec, templates, and the OHF seed distilled from the Communications Strategy & Architecture doc | Built and tested |
| `ohf-brand-system/` | The brand system itself, scaffolded from the seed. Core from the comms doc; four projects registered; Home Assistant drafted from public sources and interviewed | Home Assistant at `interviewed`, ready for live |

## Where to start reviewing

1. `brand-system-builder/README.md` for the idea and the lifecycle.
2. `brand-system-builder/references/project-spec.md` for the contract every project meets.
3. `ohf-brand-system/INDEX.md`, the only file an agent loads before a task.
4. `ohf-brand-system/projects/home-assistant/` for what a fully drafted project looks like. Start with `PROJECT.md`, then `brand/voice.md` and `brand/strategy.md`.
5. `ohf-brand-system/decisions/` for the log of every interview round and what it changed.

## Check the health of the brand system
```bash
python3 brand-system-builder/scripts/audit.py ohf-brand-system
```

## Validate one project
```bash
python3 brand-system-builder/scripts/validate_project.py ohf-brand-system home-assistant
```
