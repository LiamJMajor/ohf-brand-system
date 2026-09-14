#!/usr/bin/env python3
"""Register a new project in a brand system: create projects/<slug>/ from the spec templates
for its tier, its truths/ files, its examples/ folder, a decision entry, and regenerate the registry.

Usage:
  new_project.py TARGET_DIR --slug home-assistant --name "Home Assistant" --tier flagship
                 [--voice project|foundation] [--owner @h] [--repo URL] [--website URL]
                 [--pillars privacy,choice,sustainability] [--force]
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from common import (find_root, REQUIRED_TRUTHS, SPEC, SURFACES, TEMPLATES, TIERS, TODAY, VOICES,
                    fill, fill_template, load_standards, required_files, slug as mkslug, standard_applies, write)
import build_registry


def create_project(root: Path, slug: str, name: str, tier: str, voice: str = "project", owner: str = "TODO-owner",
                   repo: str = "TODO", website: str = "TODO", pillars: str = "", surfaces: str = "", force: bool = False) -> list:
    slug = mkslug(slug)
    if tier not in TIERS:
        raise SystemExit(f"tier must be one of {TIERS}")
    if voice not in VOICES:
        raise SystemExit(f"voice must be one of {VOICES}")
    review = (TODAY + dt.timedelta(days=30)).isoformat()
    surf = [x.strip() for x in surfaces.split(",") if x.strip()]
    for x in surf:
        if x not in SURFACES:
            raise SystemExit(f"surface `{x}` not in {SURFACES}")
    org = "the organisation"
    try:
        org = json.loads((root / ".claude-plugin" / "plugin.json").read_text()).get("author", {}).get("name", org)
    except Exception:
        pass
    vals = dict(NAME=name, SLUG=slug, TIER=tier, VOICE=voice, OWNER=owner, DATE=TODAY.isoformat(), ORG=org,
                REPO=repo, WEBSITE=website, PILLARS=", ".join(p.strip() for p in pillars.split(",") if p.strip()),
                SURFACES=", ".join(surf), REVIEW_DATE=review)
    created = []
    pdir = root / "projects" / slug
    # Flagship and active get every spec file so nothing is missing when a project moves up; stewarded gets only its required set.
    files = list(SPEC) if tier in ("flagship", "active") else required_files(tier)
    for f in files:
        text = fill((TEMPLATES / "project" / f).read_text(), **vals)
        if write(pdir / f, text, force):
            created.append(pdir / f)
    # Conformance files for every shared standard that applies to this project
    pfm = {"slug": slug, "tier": tier, "surfaces": surf}
    for std in load_standards(root):
        if std.get("scope") != "shared" or not standard_applies(std, pfm):
            continue
        if str(std.get("conformance", "file")).lower() == "none":
            continue
        text = fill_template("standard-conformance.template.md", STANDARD=std["_slug"], STANDARD_TITLE=std.get("title", std["_slug"]), **vals)
        if write(pdir / "standards" / f"{std['_slug']}.md", text, force):
            created.append(pdir / "standards" / f"{std['_slug']}.md")
    for t in REQUIRED_TRUTHS[tier]:
        tmpl = "proof-points.template.md" if t == "proof-points.md" else "truth.template.md"
        text = fill_template(tmpl, TOPIC=t.replace(".md", ""), SOURCE_URL="TODO source URL", FACT="TODO fact", OLD_FACT="none yet", **vals)
        if write(root / "truths" / slug / t, text, force):
            created.append(root / "truths" / slug / t)
    (root / "examples" / slug).mkdir(parents=True, exist_ok=True)
    dec = root / "decisions" / f"{TODAY.isoformat()}-register-{slug}.md"
    if write(dec, (
        f"---\ndate: {TODAY.isoformat()}\narea: projects\nproject: {slug}\ntrigger: interview\n"
        f"change: Registered {name} as a {tier} {voice}-voice project\naffected:\n  - projects/{slug}/PROJECT.md\n"
        f"  - projects/REGISTRY.md\nby: {owner}\n---\n\n# Registered {name}\n\nTier {tier}. Status registered. "
        f"Next: draft spec files from public sources (onboard-project), then maintainer interview.\n"), force):
        created.append(dec)
    (root / "projects" / "REGISTRY.md").write_text(build_registry.render(root))
    return created


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", default=None, help="brand system root; default: found from the current directory")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--tier", required=True, choices=TIERS)
    ap.add_argument("--voice", default="project", choices=VOICES)
    ap.add_argument("--owner", default="TODO-owner")
    ap.add_argument("--repo", default="TODO")
    ap.add_argument("--website", default="TODO")
    ap.add_argument("--pillars", default="")
    ap.add_argument("--surfaces", default="", help="comma-separated: " + ",".join(SURFACES))
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    root = Path(a.target).expanduser().resolve() if a.target else find_root()
    created = create_project(root, a.slug, a.name, a.tier, a.voice, a.owner, a.repo, a.website, a.pillars, a.surfaces, a.force)
    print(f"registered {a.slug} ({a.tier}, {a.voice} voice): {len(created)} files created")
    for c in created:
        print("  ", c.relative_to(root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
