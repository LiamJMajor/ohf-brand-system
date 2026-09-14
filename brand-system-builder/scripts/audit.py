#!/usr/bin/env python3
"""Deterministic health checks for a brand system repository.

Usage: audit.py TARGET_DIR [--json]
Checks are listed in references/audit-checks.md. Runs validate_project for every project.
Exit 1 on any error-severity finding.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from common import check_fresh, find_root, TEMPLATES, TODAY, _as_list, body, days, load_projects, load_standards, parse_frontmatter, read, standard_applies, to_date
import build_registry
import validate_project

INDEX_BUDGET, SKILL_BUDGET, MIN_EVAL_CASES, MIN_WHY, DUP_MIN = 60, 300, 3, 2, 200


class Audit:
    def __init__(self, root: Path):
        self.root, self.errors, self.warns, self.obs = root, [], [], []

    def rel(self, p):
        return str(p.relative_to(self.root)) if isinstance(p, Path) else (p or "")

    def err(self, m, p=None): self.errors.append((m, self.rel(p)))
    def warn(self, m, p=None): self.warns.append((m, self.rel(p)))

    def run(self):
        r = self.root
        index = r / "INDEX.md"
        it = read(index) if index.exists() else ""
        if not index.exists():
            self.err("INDEX.md missing: nothing loads without the router")
        else:
            n = len([l for l in it.splitlines() if l.strip()])
            if n > INDEX_BUDGET:
                self.warn(f"INDEX.md has {n} non-empty lines; budget {INDEX_BUDGET}", index)
            if "projects/REGISTRY.md" not in it:
                self.err("INDEX.md does not point at projects/REGISTRY.md", index)
            for ref in re.findall(r"`((?:core|truths|projects|examples|skills|evals|decisions)/[^`<>]*?)`", it):
                if not (r / ref).exists():
                    self.err(f"INDEX.md points at missing path `{ref}`", index)
            if re.search(r"`projects/(?!REGISTRY|<slug>)[a-z0-9-]+/", it):
                self.warn("INDEX.md lists individual projects; that is what REGISTRY.md is for", index)
        for p in sorted(r.glob("core/*.md")) + sorted(r.glob("skills/*/SKILL.md")):
            if it and str(p.relative_to(r)) not in it and "core/standards/" not in it:
                self.err("not listed in INDEX.md (invisible to agents)", p)

        # Registry
        reg = r / "projects" / "REGISTRY.md"
        if not reg.exists():
            self.err("projects/REGISTRY.md missing; run build_registry.py")
        else:
            strip = lambda s: "\n".join(l for l in s.splitlines() if not l.startswith("Regenerated") and " projects." not in l)
            if strip(read(reg)) != strip(build_registry.render(r)):
                self.err("projects/REGISTRY.md is stale; run build_registry.py", reg)

        # Projects via validator
        for fm in load_projects(r):
            res = validate_project.validate(r, fm)
            for e in res["errors"]:
                (self.err if res["status"] in ("validated", "live") else self.warn)(f"[{res['slug']}] {e}", fm["_dir"] / "PROJECT.md")
            for w in res["warnings"]:
                self.warn(f"[{res['slug']}] {w}", fm["_dir"] / "PROJECT.md")
            if res["status"] not in ("validated", "live") and res["errors"]:
                self.obs.append((f"[{res['slug']}] status {res['status']}: {len(res['errors'])} spec gap(s) expected at this stage", self.rel(fm["_dir"] / "PROJECT.md")))

        # Standards: definitions valid, coverage per shared standard
        projects = load_projects(r)
        for std in load_standards(r):
            sp = std["_path"]
            for key in ("standard", "title", "scope", "owner", "last_reviewed"):
                if not std.get(key):
                    self.err(f"standard missing `{key}`", sp)
            if std.get("scope") not in ("core", "shared", "project"):
                self.err(f"standard scope `{std.get('scope')}` not in core|shared|project", sp)
            if std.get("scope") == "shared" and not any(std.get(k) for k in ("applies_surfaces", "applies_tiers", "applies_projects", "applies_all")):
                self.err("shared standard binds to nothing (applies_surfaces / applies_tiers / applies_projects / applies_all)", sp)
            if std.get("scope") == "shared":
                applicable = [pj for pj in projects if standard_applies(std, pj)]
                have = [pj for pj in applicable if (pj["_dir"] / "standards" / f"{std['_slug']}.md").exists()]
                if applicable:
                    self.obs.append((f"standard `{std['_slug']}`: {len(have)} of {len(applicable)} applicable project(s) have a conformance file", self.rel(sp)))
            if "TODO" in read(sp) and std.get("status", "") != "example":
                self.obs.append((f"standard `{std['_slug']}` has {read(sp).count('TODO')} TODO marker(s)", self.rel(sp)))

        # Core files
        for p in sorted(r.glob("core/*.md")):
            fm = parse_frontmatter(read(p))
            if not fm.get("owner") or "TODO" in str(fm.get("owner")):
                self.warn("core file has no owner", p)
            lr = to_date(fm.get("last_reviewed"))
            if lr and (TODAY - lr).days > days(fm.get("review_every", "180d")):
                self.warn(f"last_reviewed {lr} older than review_every", p)
            t = read(p)
            if "TODO" in t:
                self.obs.append((f"{t.count('TODO')} TODO marker(s)", self.rel(p)))

        # Skills
        for p in sorted(r.glob("skills/*/SKILL.md")):
            t = read(p); fm = parse_frontmatter(t)
            if not fm.get("name"): self.err("SKILL.md missing `name`", p)
            elif fm["name"] != p.parent.name: self.warn(f"name `{fm['name']}` differs from folder", p)
            d = str(fm.get("description", ""))
            if not d: self.err("SKILL.md missing `description`; it cannot trigger", p)
            elif len(d) < 60: self.warn("description very short; will under-trigger", p)
            if len(t.splitlines()) > SKILL_BUDGET: self.warn(f"SKILL.md over {SKILL_BUDGET} lines; split", p)
            if not fm.get("owner") or "TODO" in str(fm.get("owner")): self.warn("skill has no owner", p)
            cases = p.parent / "evals" / "cases.md"
            if not cases.exists(): self.warn("no evals/cases.md; a skill without evals is a draft", p)
            else:
                ct = read(cases); n = len(re.findall(r"^## Case:", ct, re.M))
                if n < MIN_EVAL_CASES or "TODO" in ct: self.warn(f"{n} eval case(s) (min {MIN_EVAL_CASES}) or TODOs remain", cases)
                if "## Trigger cases" not in ct: self.warn("no trigger cases", cases)
            for ver in re.findall(r"\b20\d\d\.\d{1,2}\.\d+\b", t):
                self.warn(f"restates version `{ver}`; cite truths/ by path", p)
            if fm.get("reliability") == "production" and not (p.parent / "evals" / "cases.md").exists():
                self.err("production skill without evals", p)

        # Truths (all)
        for p in sorted(r.glob("truths/**/*.md")):
            fm = parse_frontmatter(read(p))
            for key in ("source", "valid_from", "review_by", "owner"):
                if not fm.get(key): self.err(f"truth missing `{key}`", p)
            rb = to_date(fm.get("review_by"))
            if rb and rb < TODAY: self.err(f"truth past review_by ({rb}); stale facts propagate", p)
            if p.name == "proof-points.md":
                rows = [l for l in body(read(p)).splitlines() if l.startswith("|") and not l.startswith("|--") and "Claim" not in l]
                unv = [l for l in rows if l.rstrip("| ").rsplit("|", 1)[-1].strip().lower() in ("", "never", "todo")]
                if unv: self.warn(f"{len(unv)} proof point(s) unverified; not usable by skills", p)

        # Examples
        for p in sorted(r.glob("examples/**/*.md")):
            fm = parse_frontmatter(read(p)); why = fm.get("why_it_works") or []
            if not isinstance(why, list) or len(why) < MIN_WHY: self.warn(f"example has fewer than {MIN_WHY} why_it_works items", p)
            for w in why if isinstance(why, list) else []:
                if len(w.split()) < 4: self.warn(f"why_it_works item too vague: `{w}`", p)
            if not fm.get("type"): self.err("example missing `type`", p)
            if not fm.get("project"): self.err("example missing `project`", p)

        # Owners
        ow = r / "OWNERS.md"
        if not ow.exists(): self.err("OWNERS.md missing; nobody prunes")
        else:
            ot = read(ow)
            for area in ("core/", "truths/", "skills/", "projects/"):
                if area not in ot: self.err(f"OWNERS.md has no row for {area}", ow)
            if "TODO" in ot: self.warn("OWNERS.md has TODO owners", ow)
        if not list(r.glob("decisions/*.md")): self.warn("decisions/ is empty; nothing is being logged")

        # Duplicates, ignoring template boilerplate
        th = set()
        for tp in list(TEMPLATES.rglob("*.md")):
            for para in re.split(r"\n\s*\n", read(tp)):
                norm = re.sub(r"\{\{[A-Za-z_|]+\}\}", "", re.sub(r"\s+", " ", para)).strip()
                if len(norm) >= DUP_MIN: th.add(hashlib.sha1(norm.encode()).hexdigest())
        seen = {}
        for p in sorted(r.rglob("*.md")):
            if ".claude-plugin" in p.parts or p.name == "REGISTRY.md": continue
            for para in re.split(r"\n\s*\n", body(read(p))):
                norm = re.sub(r"\s+", " ", para).strip()
                if len(norm) < DUP_MIN or "TODO" in norm: continue
                # normalise project-specific tokens so seeded boilerplate across projects is not flagged
                key = hashlib.sha1(norm.encode()).hexdigest()
                if key in th: continue
                if key in seen and seen[key].parent != p.parent:
                    self.warn(f"paragraph duplicated from {seen[key].relative_to(r)}; point to one source", p)
                seen.setdefault(key, p)

    def report(self) -> str:
        f = lambda rows: [f"- {m}  `{p}`" if p else f"- {m}" for m, p in rows] or ["- none"]
        return "\n".join([f"# Brand system audit: {TODAY}", "", f"Root: `{self.root}`", "",
                          "## Errors (fix before next use)", *f(self.errors), "",
                          "## Warnings (fix this month)", *f(self.warns), "",
                          "## Observations", *f(self.obs), "",
                          "## Recommended next three actions",
                          "- (filled in by the audit-brand-system skill after the qualitative pass)"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", default=None, help="brand system root; default: found from the current directory")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    root = Path(a.target).expanduser().resolve() if a.target else find_root()
    fresh = check_fresh(root)
    if fresh:
        print(fresh, file=sys.stderr)
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr); return 2
    au = Audit(root); au.run()
    print(json.dumps({"errors": au.errors, "warnings": au.warns, "observations": au.obs}, indent=2) if a.json else au.report())
    return 1 if au.errors else 0


if __name__ == "__main__":
    sys.exit(main())
