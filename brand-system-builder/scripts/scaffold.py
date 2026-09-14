#!/usr/bin/env python3
"""Scaffold a brand system repository from the builder templates, optionally seeded.

Usage:
  scaffold.py TARGET_DIR --org "Org Name" [--seed open-home-foundation]
              [--skills write-release-post,write-feature-short]
              [--owners core=@h,truths=@h,skills=@h] [--force]

Creates core/ (from seed if given), truths/core/, evals/rubrics/, INDEX.md, OWNERS.md, CONTRIBUTING.md,
README.md, plugin manifests, a bootstrap decision, draft skills + evals for each named skill, and registers
every project in the seed's projects.csv via new_project.py. Standard library only.
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from common import SEEDS, TEMPLATES, TODAY, fill, fill_template, read_seed_projects, slug as mkslug, write
from new_project import create_project
import build_registry


def parse_owners(s: str) -> dict:
    out = {"core": "TODO-owner", "truths": "TODO-owner", "skills": "TODO-owner"}
    for pair in (s or "").split(","):
        k, _, v = pair.partition("=")
        if k.strip() and v.strip():
            out[k.strip()] = v.strip()
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--org", required=True)
    ap.add_argument("--seed", default="")
    ap.add_argument("--skills", default="")
    ap.add_argument("--owners", default="")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    target = Path(a.target).expanduser().resolve()
    owners = parse_owners(a.owners)
    org_slug = mkslug(a.org)
    review = (TODAY + dt.timedelta(days=30)).isoformat()
    vals = dict(ORG=a.org, CORE_OWNER=owners["core"], TRUTHS_OWNER=owners["truths"], SKILLS_OWNER=owners["skills"],
                DATE=TODAY.isoformat(), REVIEW_DATE=review)
    seed_dir = SEEDS / a.seed if a.seed else None
    if a.seed and not seed_dir.is_dir():
        print(f"no such seed: {a.seed}; available: {[p.name for p in SEEDS.iterdir() if p.is_dir()]}", file=sys.stderr)
        return 2

    for d in ["core", "core/standards", "projects", "truths/core", "examples", "skills", "evals/rubrics", "decisions", ".claude-plugin"]:
        (target / d).mkdir(parents=True, exist_ok=True)

    # Core: seed overrides template
    for f in ["story.md", "pillars.md", "voices.md", "escalation.md", "channels.md"]:
        src = seed_dir / "core" / f if seed_dir and (seed_dir / "core" / f).exists() else TEMPLATES / "core" / f
        write(target / "core" / f, fill(src.read_text(), **vals), a.force)
    # Shared standards: seed overrides template; templates ship the five surface standards plus an SEO example
    std_src_dirs = [TEMPLATES / "core" / "standards"] + ([seed_dir / "core" / "standards"] if seed_dir and (seed_dir / "core" / "standards").exists() else [])
    for d in std_src_dirs:
        for f in sorted(d.glob("*.md")):
            write(target / "core" / "standards" / f.name, fill(f.read_text(), **vals), a.force or d != TEMPLATES / "core" / "standards")
    # Shared proof points
    pp_src = seed_dir / "truths" / "proof-points.md" if seed_dir and (seed_dir / "truths" / "proof-points.md").exists() else None
    if pp_src:
        write(target / "truths" / "core" / "proof-points.md", fill(pp_src.read_text(), **vals), a.force)
    else:
        write(target / "truths" / "core" / "proof-points.md",
              fill_template("proof-points.template.md", SLUG="core", OWNER=owners["truths"], **vals), a.force)
    write(target / "evals" / "rubrics" / "on-brand.md", fill_template("rubric-on-brand.template.md"), a.force)

    # Skills
    skills = [mkslug(s) for s in a.skills.split(",") if s.strip()]
    skill_index = []
    for s in skills:
        write(target / "skills" / s / "SKILL.md", fill_template(
            "SKILL.template.md", SKILL_NAME=s, SKILL_TITLE=s.replace("-", " ").capitalize(), OWNER=owners["skills"],
            WHAT_IT_DOES=f"TODO: one sentence on what {s} produces.", TRIGGER_PHRASES="TODO: casual phrasings",
            SIBLING_BOUNDARY="TODO: name sibling skills and the boundary.",
            ONE_PARAGRAPH_PURPOSE="TODO: fill via codify-workflow after studying three real requests.",
            DEFAULT_MODE="Medium", INTAKE_ITEM="**TODO**: the one thing only the requester knows",
            RELEVANT_TRUTH="current-release", EXAMPLE_TYPE=s, PRODUCTION_STEPS="TODO steps",
            OUTPUT_FORMAT="TODO editable format", KNOWN_LIMITS="TODO", **vals), a.force)
        write(target / "skills" / s / "evals" / "cases.md", fill_template(
            "eval-cases.template.md", SKILL_NAME=s, CASE_SLUG="TODO", REALISTIC_REQUEST="TODO",
            OBSERVABLE_REQUIREMENT="TODO", OBSERVABLE_FAILURE="TODO", WHY_THIS_CASE_MATTERS="TODO",
            PHRASE="TODO", OTHER_SKILL="TODO"), a.force)
        skill_index.append(f"- `skills/{s}/SKILL.md`: TODO one line on what it produces and when to use it.")

    # Governance
    write(target / "INDEX.md", fill_template("INDEX.template.md",
          SKILL_INDEX_LINES="\n".join(skill_index) or "- (no skills yet; use codify-workflow)", **vals), a.force)
    write(target / "OWNERS.md", fill_template("OWNERS.template.md", **vals), a.force)
    write(target / "CONTRIBUTING.md", fill_template("CONTRIBUTING.template.md", **vals), a.force)
    write(target / "README.md", (
        f"# {a.org} brand system\n\nThe shared core, one directory per project voice, dated truths, annotated examples "
        "and self-serve skills, written for agents to load and act on. Start at `INDEX.md`.\n\n"
        f"## Install\n```\n/plugin marketplace add <org>/{org_slug}-brand-system\n/plugin install {org_slug}-brand-system\n```\n\n"
        "## Maintained with\nThe brand-system-builder plugin. New projects through `onboard-project`; corrections through "
        "`promote-correction`; new skills through `codify-workflow`; monthly health through `audit-brand-system`.\n"), a.force)
    write(target / "decisions" / f"{TODAY.isoformat()}-bootstrap.md", (
        f"---\ndate: {TODAY.isoformat()}\narea: repo\nproject: core\ntrigger: interview\nchange: Bootstrapped the brand system\n"
        f"affected:\n  - INDEX.md\nby: {owners['core']}\n---\n\n# Bootstrapped the brand system\n\nOrg: {a.org}. "
        f"Seed: {a.seed or 'none'}. Initial skill stubs: {', '.join(skills) or 'none'}.\n"), a.force)
    plugin = {"name": f"{org_slug}-brand-system", "version": "0.1.0",
              "description": f"{a.org} brand system: shared core, project voices, truths, examples and self-serve skills.",
              "author": {"name": a.org}}
    write(target / ".claude-plugin" / "plugin.json", json.dumps(plugin, indent=2) + "\n", a.force)
    write(target / ".claude-plugin" / "marketplace.json", json.dumps({
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json", "name": plugin["name"],
        "description": plugin["description"], "owner": {"name": a.org},
        "plugins": [{"name": plugin["name"], "description": plugin["description"], "source": "./", "category": "productivity"}],
    }, indent=2) + "\n", a.force)

    # Seed projects
    registered = []
    for row in read_seed_projects(a.seed) if a.seed else []:
        create_project(target, row["slug"], row["name"], row["tier"], row.get("voice", "project"),
                       owners.get(row["slug"], owners["core"]), row.get("repo", "TODO"), row.get("website", "TODO"),
                       row.get("pillars", ""), row.get("surfaces", ""), a.force)
        registered.append(row["slug"])
    (target / "projects" / "REGISTRY.md").write_text(build_registry.render(target))

    print(f"Scaffolded {target}")
    print(f"  seed: {a.seed or 'none'}; projects registered: {', '.join(registered) or 'none'}")
    print(f"  skills: {', '.join(skills) or '(none)'}")
    print("  next: onboard-project for each registered project; audit.py for a baseline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
