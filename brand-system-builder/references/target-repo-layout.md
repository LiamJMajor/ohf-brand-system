# Target repo layout

The shape of the brand system the builder produces. Built for an organisation that stewards many projects, each with its own voice, under one shared core. Every builder skill writes into this structure. Deviate only with a reason recorded in `decisions/`.

```
<org>-brand-system/
├── README.md
├── INDEX.md                  The ONLY always-loaded file. One line per entry. Budget 60 lines.
├── OWNERS.md                 Who owns core, truths, skills, and each project
├── CONTRIBUTING.md
├── .claude-plugin/           plugin.json, marketplace.json
├── core/                     Shared core. Thin. Every voice inherits it.
│   ├── story.md              The single thread through everything
│   ├── pillars.md            The beliefs every output must serve; the filter
│   ├── voices.md             Foundation voice vs project voice; product-or-cause test; edge cases
│   ├── escalation.md         What always needs a human, and the route
│   └── channels.md           Channel taxonomy and what each class of channel is for
├── projects/                 One directory per voice, all the same shape. See project-spec.md.
│   ├── REGISTRY.md           Generated. One line per project: slug, name, tier, status, owner.
│   ├── open-home-foundation/ The foundation's own voice, same schema, voice: foundation
│   ├── home-assistant/
│   └── <slug>/
├── truths/
│   ├── core/proof-points.md  Shared proof points
│   └── <slug>/               proof-points.md, current-release.md
├── examples/<slug>/<type>/   Approved, annotated work per project per output type
├── skills/<beat>/            Self-serve workflows. Parameterised by project; never per project.
│   ├── SKILL.md
│   ├── references/
│   └── evals/cases.md
├── evals/rubrics/            on-brand.md and any beat-specific rubrics
└── decisions/                Dated log of what changed and why
```

## Why each part exists

**INDEX.md** is the router. It cannot list hundreds of projects, so it lists `projects/REGISTRY.md` and the rule: find the slug there, then load `projects/<slug>/PROJECT.md`, which lists that project's files. Two hops, still under budget.

**core/** is deliberately thin. The story, the pillars, who speaks when, what needs a human, what channels are for. It holds no voice attributes of its own; the foundation's voice lives in `projects/open-home-foundation/`. Anything in core applies to every project without exception.

**projects/** is where scale lives. Every directory has the same files with the same headings, per `project-spec.md`, so an agent's procedure is identical across projects. Tiers decide which files are required. Status decides whether agents may build against it.

**truths/** is the fast layer. Proof points carry claim, figure, source, pillar, approved phrasing and a verified date. Skills cite them by path and copy approved phrasing verbatim. Automation writes `current-release.md`.

**examples/** is per project because voices differ; a Music Assistant post is not a template for an ESPHome post. Skills load examples from the project in play and fall back to a flagship project of the same voice type only when the project has none.

**skills/** are per beat: release, newsletter, hardware release, community meetup, announcement, store product. A skill takes the project slug as intake and loads that project's directory. Writing a skill per project would multiply maintenance by the number of projects and is the one thing this layout forbids.

**decisions/** is the memory of why.

## Size budgets
| File | Budget | When exceeded |
|---|---|---|
| INDEX.md | 60 lines | Never add project lines; that is what REGISTRY is for |
| PROJECT.md | 60 lines | It is a manifest, not a document |
| any project file | 200 lines | Split into `projects/<slug>/references/` |
| SKILL.md | 300 lines | Split into references |
| example | 150 lines | Excerpt and link |

## Naming
- Slugs: kebab-case, matching the project's GitHub org or repo name where one exists.
- Skills: verb-first (`write-release-post`, `build-hardware-launch`).
- Examples: `<slug>/<type>/<yyyy-mm>-<slug>.md`.
- Decisions: `<yyyy-mm-dd>-<slug>.md`.
