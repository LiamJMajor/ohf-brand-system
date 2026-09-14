#!/usr/bin/env python3
"""Validate projects against the project spec (references/project-spec.md).

Usage: validate_project.py TARGET_DIR [SLUG ...] [--all] [--json]
Exit 1 if any project has errors. A project with status `live` must have zero errors and zero TODOs.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from common import (BANNED_WORDS, CONFORMANCE_TABLE, LIVE_REQUIRES_READY, READY_AREAS, REQUIRED_TRUTHS, SPEC, STATUSES, SURFACES, TIERS, VOICES,
                    _as_list, body, headings, load_projects, load_standards, parse_frontmatter, read,
                    required_files, standard_applies, to_date, TODAY)

SOUNDS_LIKE_ROWS = ["Speaks about", "Speaks to", "Sounds like", "Typically says", "Never"]


def table_has_columns(text: str, cols: list) -> bool:
    for line in body(text).splitlines():
        if line.strip().startswith("|") and all(c.lower() in line.lower() for c in cols):
            return True
    return False


def validate(root: Path, fm: dict) -> dict:
    slug = fm["slug"]
    pdir = fm["_dir"]
    errors, warns = [], []
    E = lambda m, f="PROJECT.md": errors.append(f"{f}: {m}")
    W = lambda m, f="PROJECT.md": warns.append(f"{f}: {m}")

    tier, voice, status = fm.get("tier"), fm.get("voice"), fm.get("status")
    for key in ("name", "slug", "tier", "voice", "status", "owner", "pillars", "last_reviewed"):
        if not fm.get(key):
            E(f"missing frontmatter `{key}`")
    if tier not in TIERS:
        E(f"tier `{tier}` not in {TIERS}"); tier = "stewarded"
    if voice not in VOICES:
        E(f"voice `{voice}` not in {VOICES}")
    if status not in STATUSES:
        E(f"status `{status}` not in {STATUSES}")
    ready = _as_list(fm.get("ready"))
    for a in ready:
        if a not in READY_AREAS:
            E(f"ready area `{a}` not in {READY_AREAS}")
    if status in ("validated", "live"):
        for a in LIVE_REQUIRES_READY:
            if a not in ready:
                E(f"status {status} requires `ready:` to include `{a}`")
    def area_of(relpath: str) -> str:
        return relpath.split("/", 1)[0] if "/" in relpath else "brand"
    def strict(relpath: str) -> bool:
        """TODO and draft checks apply to files in areas the project declares ready."""
        return area_of(relpath) in ready
    if fm.get("slug") != pdir.name:
        E(f"slug `{fm.get('slug')}` differs from directory `{pdir.name}`")
    if str(fm.get("owner", "")).startswith("TODO"):
        W("owner is TODO")

    core_pillars = [h.lower() for h in headings(read(root / "core" / "pillars.md"))]
    pillars = fm.get("pillars") or []
    if isinstance(pillars, str):
        pillars = [p.strip() for p in pillars.split(",") if p.strip()]
    for p in pillars:
        if core_pillars and p.lower() not in core_pillars and not p.lower().startswith("todo"):
            E(f"pillar `{p}` is not in core/pillars.md")

    # Files per spec
    not_ready = {}
    pillars_l = [p.lower() for p in pillars]
    surfaces = fm.get("surfaces") or []
    if isinstance(surfaces, str):
        surfaces = [x.strip() for x in surfaces.split(",") if x.strip()]
    for x in surfaces:
        if x not in SURFACES:
            E(f"surface `{x}` not in {SURFACES}")
    for f in required_files(tier):
        fp = pdir / f
        if not fp.exists():
            E(f"required for tier {tier} but missing", f); continue
        spec = SPEC[f]
        text = read(fp)
        if f.endswith(".json"):
            try:
                tok = json.loads(text)
                for key in ("color", "type", "space"):
                    if key not in tok:
                        E(f"tokens.json missing `{key}`", f)
                if strict(f) and "TODO" in text:
                    E("TODO values in an area declared ready", f)
            except json.JSONDecodeError as ex:
                E(f"invalid JSON: {ex}", f)
            continue
        ffm = parse_frontmatter(text)
        if f != "PROJECT.md":
            for key in ("area", "project", "owner", "last_reviewed"):
                if not ffm.get(key):
                    E(f"missing frontmatter `{key}`", f)
            if ffm.get("project") and ffm.get("project") != slug:
                E(f"frontmatter project `{ffm.get('project')}` != `{slug}`", f)
        req = spec.get("stewarded_h2", spec["h2"]) if tier == "stewarded" else spec["h2"]
        h2 = headings(text)
        for h in req:
            if h not in h2:
                E(f"missing `## {h}`", f)
        if spec["table"] and not table_has_columns(text, spec["table"]):
            E(f"no table with columns {', '.join(spec['table'])}", f)
        if f == "brand/voice.md":
            for row in SOUNDS_LIKE_ROWS:
                if not re.search(r"^\|\s*" + re.escape(row) + r"\s*\|", body(text), re.M):
                    E(f"Sounds like table missing row `{row}`", f)
            rules_text = next((sct for sct in re.split(r"^## ", body(text), flags=re.M) if sct.startswith("Rules")), "")
            rules = re.split(r"^### ", rules_text, flags=re.M)[1:]
            real = [r for r in rules if "TODO" not in r.splitlines()[0]]
            if len(real) < 3:
                E(f"{len(real)} real rule(s) under ## Rules; minimum 3", f)
            for r in rules:
                if "- Yes:" not in r or "- No:" not in r:
                    E(f"rule `{r.splitlines()[0].strip()}` lacks a `- Yes:` and `- No:` contrast pair", f)
            for row in ("Low", "Medium", "High"):
                if not re.search(r"^\|\s*" + row + r"\s*\|", body(text), re.M):
                    E(f"Modes table missing row `{row}`", f)
        if f == "brand/strategy.md" and tier != "stewarded":
            h3 = [h.lower() for h in headings(text, 3)]
            for pl in pillars_l:
                if pl not in h3:
                    E(f"no `### {pl.capitalize()}` under Pillar translations for a pillar in PROJECT.md", f)
            pers = next((sct for sct in re.split(r"^## ", body(text), flags=re.M) if sct.startswith("Personality")), "")
            attrs = re.split(r"^### ", pers, flags=re.M)[1:]
            for at in attrs:
                if "- Yes:" not in at or "- No:" not in at:
                    E(f"personality attribute `{at.splitlines()[0].strip()}` lacks a contrast pair", f)
            for w in BANNED_WORDS:
                if re.search(r"\b" + re.escape(w) + r"\b", text.split("## Positioning",1)[-1].split("## Personality",1)[0], re.I):
                    E(f"banned word `{w}` in Positioning", f)
        if f == "brand/messaging.md":
            h3 = headings(text, 3)
            if tier != "stewarded":
                aud = headings(read(pdir / "brand" / "audiences.md")) if (pdir / "brand" / "audiences.md").exists() else []
                for au in aud:
                    if au not in h3 and not au.startswith("TODO"):
                        E(f"no `### {au}` under Key messages for an audience in brand/audiences.md", f)
            for hb in ("One line", "50 words", "100 words"):
                if hb not in h3:
                    E(f"Boilerplate missing `### {hb}`", f)
            check = " ".join(sct for sct in re.split(r"^## ", body(text), flags=re.M) if sct.startswith(("Boilerplate", "Key messages", "Taglines")))
            for w in BANNED_WORDS:
                if re.search(r"\b" + re.escape(w) + r"\b", check, re.I):
                    E(f"banned word `{w}` in key messages, boilerplate or taglines", f)
            one = re.search(r"### One line\n+(.+)", body(text))
            if one and "TODO" not in one.group(1) and len(one.group(1).split()) > 20:
                W("One line boilerplate is over 20 words", f)
        if f == "brand/audiences.md":
            secs = re.split(r"^## ", body(text), flags=re.M)[1:]
            if not secs:
                E("no audience sections", f)
            for sct in secs:
                if "**Cares about:**" not in sct or "**Found on:**" not in sct:
                    E(f"audience `{sct.splitlines()[0]}` lacks **Cares about:** or **Found on:**", f)
        if strict(f) and "TODO" in text:
            E(f"{text.count('TODO')} TODO marker(s) in an area declared ready", f)
        if strict(f) and str(ffm.get("draft", "")).lower() == "true":
            E(f"draft: true in an area declared ready", f)
        if not strict(f) and status in ("validated", "live") and ("TODO" in text or str(ffm.get("draft", "")).lower() == "true"):
            not_ready.setdefault(area_of(f), []).append(f)
    for area, files in not_ready.items():
        W(f"area `{area}` not in ready: {len(files)} file(s) still draft or TODO; skills needing {area} will refuse", f"{area}/")
    # Standards: conformance file per applicable shared standard; project-owned definitions declared
    standards = load_standards(root)
    sdir = pdir / "standards"
    for std in standards:
        if not standard_applies(std, fm) or std.get("scope") == "project":
            continue
        if str(std.get("conformance", "file")).lower() == "none":
            continue
        cf = sdir / f"{std['_slug']}.md"
        grace = to_date(std.get("grace_until"))
        sev = W if (grace and grace > TODAY) else E
        if not cf.exists():
            sev(f"standard `{std['_slug']}` applies (via {std.get('applies_surfaces') or std.get('applies_tiers') or 'all'}) but has no conformance file", f"standards/{std['_slug']}.md"); continue
        ct = read(cf); cfm = parse_frontmatter(ct)
        if cfm.get("conforms_to") != std["_slug"]:
            E(f"conformance file must declare `conforms_to: {std['_slug']}`", f"standards/{std['_slug']}.md")
        for h in _as_list(std.get("conformance_headings")):
            if h not in headings(ct):
                E(f"missing `## {h}` required by standard `{std['_slug']}`", f"standards/{std['_slug']}.md")
        cols = _as_list(std.get("conformance_table")) or CONFORMANCE_TABLE
        if not table_has_columns(ct, cols):
            E(f"no table with columns {', '.join(cols)}", f"standards/{std['_slug']}.md")
        if "standards" in ready and "TODO" in ct:
            E("TODO markers but standards declared ready", f"standards/{std['_slug']}.md")
    declared = set(_as_list(fm.get("standards")))
    for std in standards:
        if std.get("scope") == "project" and std.get("_owner_project") == slug and std["_slug"] not in declared:
            W(f"project-owned standard `{std['_slug']}` exists but is not listed in PROJECT.md `standards:`", f"standards/{std['_slug']}.md")
    for d in declared:
        if not (sdir / f"{d}.md").exists():
            E(f"PROJECT.md declares standard `{d}` but standards/{d}.md is missing")
    if sdir.exists():
        known = {st["_slug"] for st in standards}
        for sp in sdir.glob("*.md"):
            cfm = parse_frontmatter(read(sp))
            if cfm.get("conforms_to") and cfm["conforms_to"] not in known:
                W(f"conforms to unknown standard `{cfm['conforms_to']}`", f"standards/{sp.name}")
            if not cfm.get("conforms_to") and cfm.get("scope") != "project":
                W("neither a conformance file (`conforms_to:`) nor a project standard (`scope: project`)", f"standards/{sp.name}")

    # Truths
    for t in REQUIRED_TRUTHS[tier]:
        tp = root / "truths" / slug / t
        if not tp.exists():
            E(f"required for tier {tier} but missing", f"truths/{slug}/{t}"); continue
        text = read(tp)
        tfm = parse_frontmatter(text)
        for key in ("source", "valid_from", "review_by", "owner"):
            if not tfm.get(key):
                E(f"missing `{key}`", f"truths/{slug}/{t}")
        rb = to_date(tfm.get("review_by"))
        if rb and rb < TODAY:
            E(f"past review_by {rb}", f"truths/{slug}/{t}")
        if t == "proof-points.md":
            if not table_has_columns(text, ["Claim", "Canonical figure", "Source", "Pillar", "Approved phrasing", "Verified"]):
                E("proof-points table missing required columns", f"truths/{slug}/{t}")
            rows = [l for l in body(text).splitlines() if l.startswith("|") and not l.startswith("|--") and "Claim" not in l]
            unverified = [r for r in rows if r.rstrip("| ").rsplit("|", 1)[-1].strip().lower() in ("", "never", "todo")]
            if unverified:
                (E if status == "live" else W)(f"{len(unverified)} proof point(s) unverified", f"truths/{slug}/{t}")

    # Examples for flagship live
    if tier == "flagship" and status == "live":
        ex = list((root / "examples" / slug).rglob("*.md"))
        if len(ex) < 3:
            E(f"flagship live project has {len(ex)} example(s); minimum 3", f"examples/{slug}/")

    # Stuck
    lr = to_date(fm.get("last_reviewed"))
    if lr and status != "live" and (TODAY - lr).days > 30:
        W(f"status `{status}` for {(TODAY - lr).days} days; stuck?")

    return {"slug": slug, "tier": tier, "status": status, "errors": errors, "warnings": warns}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = Path(a.target).expanduser().resolve()
    projects = load_projects(root)
    if a.slugs:
        projects = [p for p in projects if p["slug"] in a.slugs]
        missing = set(a.slugs) - {p["slug"] for p in projects}
        for m in missing:
            print(f"no such project: {m}", file=sys.stderr)
    results = [validate(root, p) for p in projects]
    if a.json:
        print(json.dumps(results, indent=2)); return 1 if any(r["errors"] for r in results) else 0
    print(f"# Project validation: {TODAY}\n")
    for r in results:
        mark = "FAIL" if r["errors"] else "ok"
        print(f"## {r['slug']}  ({r['tier']}, {r['status']})  {mark}: {len(r['errors'])} error(s), {len(r['warnings'])} warning(s)")
        for e in r["errors"]:
            print(f"- error: {e}")
        for w in r["warnings"]:
            print(f"- warn: {w}")
        print()
    return 1 if any(r["errors"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
