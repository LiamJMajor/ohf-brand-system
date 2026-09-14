"""Shared helpers for builder scripts. Standard library only."""
import csv
import datetime as dt
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILDER = HERE.parent
TEMPLATES = BUILDER / "templates"
SEEDS = BUILDER / "seeds"
TODAY = dt.date.today()

TIERS = ("flagship", "active", "stewarded")
VOICES = ("project", "foundation")
STATUSES = ("registered", "drafted", "interviewed", "validated", "live")
BANNED_WORDS = ["seamless", "robust", "powerful", "cutting-edge", "best-in-class",
                "innovative", "revolutionary", "leverage", "empower", "next-generation"]

SURFACES = ("website", "docs", "social-profiles", "app-stores", "github")

# Fixed project files. Each file: required tiers, required ## headings, required table columns.
# Special checks (voice rules, messaging alignment, banned words, tokens.json) live in validate_project.py.
SPEC = {
    "PROJECT.md":              {"tiers": ["stewarded", "active", "flagship"], "h2": ["Owners"], "table": []},
    "brand/strategy.md":       {"tiers": ["stewarded", "active", "flagship"], "h2": ["Purpose", "Positioning", "Personality", "Pillar translations"], "table": [],
                                "stewarded_h2": ["Positioning"]},
    "brand/messaging.md":      {"tiers": ["stewarded", "active", "flagship"], "h2": ["Key messages", "Boilerplate", "Taglines", "We don't say"], "table": [],
                                "stewarded_h2": ["Boilerplate"]},
    "brand/voice.md":          {"tiers": ["active", "flagship"], "h2": ["Sounds like", "Rules", "Modes", "Never"], "table": []},
    "brand/style.md":          {"tiers": ["active", "flagship"], "h2": ["Spelling and grammar", "Capitalisation", "Numbers and dates", "Formatting", "Glossary"], "table": []},
    "brand/naming.md":         {"tiers": ["stewarded", "active", "flagship"], "h2": ["Canonical", "Forbidden variants", "Attribution"], "table": [],
                                "stewarded_h2": ["Canonical", "Attribution"]},
    "brand/story.md":          {"tiers": ["flagship"], "h2": ["Origin", "Milestones", "People"], "table": []},
    "brand/audiences.md":      {"tiers": ["active", "flagship"], "h2": [], "table": []},
    "design/logo.md":          {"tiers": ["active", "flagship"], "h2": ["Files", "Clear space and size", "Backgrounds", "Misuse", "Co-branding"], "table": []},
    "design/color.md":         {"tiers": ["active", "flagship"], "h2": ["Palette", "Semantic roles", "Light and dark", "Contrast"], "table": []},
    "design/typography.md":    {"tiers": ["active", "flagship"], "h2": ["Families", "Scale", "Usage"], "table": []},
    "design/imagery.md":       {"tiers": ["flagship"], "h2": ["Photography", "Screenshots", "Illustration and icons", "Sources"], "table": []},
    "design/motion.md":        {"tiers": ["flagship"], "h2": ["Intro and outro", "Lower thirds", "Pacing and captions", "Music"], "table": []},
    "design/layout.md":        {"tiers": ["flagship"], "h2": ["Grid and spacing", "Components", "Libraries"], "table": []},
    "design/templates.md":     {"tiers": ["flagship"], "h2": [], "table": ["Format", "Template", "Location", "Use when"]},
    "design/accessibility.md": {"tiers": ["active", "flagship"], "h2": ["Contrast", "Alt text", "Captions", "Motion"], "table": []},
    "design/tokens.json":      {"tiers": ["active", "flagship"], "h2": [], "table": []},
    "marketing/channels.md":   {"tiers": ["active", "flagship"], "h2": [], "table": ["Channel", "Purpose", "Register", "Cadence", "Handle", "Owner"]},
    "marketing/beats.md":      {"tiers": ["flagship"], "h2": [], "table": ["Beat", "Cadence", "Skill or playbook", "Owner"]},
    "marketing/content.md":    {"tiers": ["flagship"], "h2": ["Themes", "Formats", "Evergreen", "Search terms"], "table": []},
    "marketing/community.md":  {"tiers": ["flagship"], "h2": ["Spaces", "Register", "Moderation"], "table": []},
    "marketing/press.md":      {"tiers": ["flagship"], "h2": ["Press kit", "Spokespeople", "Rules"], "table": []},
    "marketing/partners.md":   {"tiers": ["flagship"], "h2": ["Who may use the brand", "Brand licence", "Partner logos"], "table": []},
    "marketing/events.md":     {"tiers": ["flagship"], "h2": ["Presence", "Talks", "Swag"], "table": []},
    "marketing/measurement.md":{"tiers": ["flagship"], "h2": [], "table": ["Channel or beat", "Measure", "Target", "Where"]},
}
CONFORMANCE_TABLE = ["Required element", "Location", "Status", "Deviation"]
STANDARD_SCOPES = ("core", "shared", "project")
READY_AREAS = ("brand", "design", "marketing", "standards")
LIVE_REQUIRES_READY = ("brand",)
REQUIRED_TRUTHS = {
    "flagship": ["proof-points.md", "current-release.md"],
    "active": ["proof-points.md"],
    "stewarded": [],
}


def required_files(tier: str) -> list:
    return [f for f, spec in SPEC.items() if tier in spec["tiers"]]


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.strip().lower()).strip("-")


def read(p: Path) -> str:
    try:
        return p.read_text(errors="replace")
    except Exception:
        return ""


def parse_frontmatter(text: str) -> dict:
    """Minimal YAML-ish parser: key: value, key: >, '- item' lists, [a, b] lists."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm, cur_key, cur_list, folded = {}, None, None, None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if folded is not None and line[:1] in (" ", "\t"):
            fm[folded] = (fm[folded] + " " + line.strip()).strip()
            continue
        folded = None
        ls = line.strip()
        if ls.startswith("- ") and cur_key and line[:1] in (" ", "\t", "-"):
            cur_list = cur_list if cur_list is not None else []
            cur_list.append(ls[2:].strip().strip("'\""))
            fm[cur_key] = cur_list
            continue
        cur_list = None
        k, sep, v = line.partition(":")
        if not sep or line[:1] in (" ", "\t"):
            continue
        k, v = k.strip(), v.strip()
        cur_key = k
        if v in (">", "|", ">-", "|-"):
            fm[k], folded = "", k
        elif v.startswith("[") and v.endswith("]"):
            fm[k] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        else:
            fm[k] = v.strip("'\"")
    return fm


def body(text: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)


def headings(text: str, level: int = 2) -> list:
    return [h.strip() for h in re.findall(r"^" + "#" * level + r" (.+)$", body(text), re.M)]


def to_date(s):
    try:
        return dt.date.fromisoformat(str(s)[:10])
    except Exception:
        return None


def days(s: str, default: int = 180) -> int:
    m = re.match(r"(\d+)\s*d", str(s))
    return int(m.group(1)) if m else default


def fill(text: str, **vals) -> str:
    for k, v in vals.items():
        text = text.replace("{{" + k + "}}", str(v))
    return text


def fill_template(name: str, **vals) -> str:
    return fill((TEMPLATES / name).read_text(), **vals)


def write(path: Path, text: str, force: bool = False) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return True


def load_projects(root: Path) -> list:
    out = []
    for p in sorted((root / "projects").glob("*/PROJECT.md")):
        fm = parse_frontmatter(read(p))
        fm["_dir"] = p.parent
        fm.setdefault("slug", p.parent.name)
        out.append(fm)
    return out


def read_seed_projects(seed: str) -> list:
    f = SEEDS / seed / "projects.csv"
    if not f.exists():
        return []
    with f.open() as fh:
        return list(csv.DictReader(fh))


def _as_list(v):
    if v is None or v == "":
        return []
    if isinstance(v, list):
        return v
    return [x.strip() for x in str(v).split(",") if x.strip()]


def load_standards(root: Path) -> list:
    """Standards declared in the repo: core/standards/*.md (scope core|shared) and
    projects/*/standards/*.md with scope: project. Each returns its frontmatter plus _path, _slug."""
    out = []
    for p in sorted((root / "core" / "standards").glob("*.md")) if (root / "core" / "standards").exists() else []:
        fm = parse_frontmatter(read(p))
        if not fm.get("standard"):
            continue
        fm["_path"] = p; fm["_slug"] = fm["standard"]; fm["_owner_project"] = "core"
        out.append(fm)
    for p in sorted(root.glob("projects/*/standards/*.md")):
        fm = parse_frontmatter(read(p))
        if fm.get("scope") == "project" and fm.get("standard"):
            fm["_path"] = p; fm["_slug"] = fm["standard"]; fm["_owner_project"] = p.parent.parent.name
            out.append(fm)
    return out


def standard_applies(std: dict, project: dict) -> bool:
    """A shared standard applies to a project if any binding matches. Core-scope standards bind to
    outputs and skills, not projects. Project-scope standards apply only to their owner."""
    if std.get("scope") == "core":
        return False
    if std.get("scope") == "project":
        return std.get("_owner_project") == project.get("slug")
    if str(std.get("applies_all", "")).lower() == "true":
        return True
    surfaces = set(_as_list(project.get("surfaces")))
    if surfaces & set(_as_list(std.get("applies_surfaces"))):
        return True
    if project.get("tier") in _as_list(std.get("applies_tiers")):
        return True
    if project.get("slug") in _as_list(std.get("applies_projects")):
        return True
    return False


def find_root(start: Path = None) -> Path:
    """Walk up from start (default cwd) to the nearest directory that looks like a brand system:
    has INDEX.md and projects/. Raises SystemExit with guidance if none is found."""
    cur = (start or Path.cwd()).resolve()
    for d in [cur] + list(cur.parents):
        if (d / "INDEX.md").exists() and (d / "projects").is_dir() and (d / "core").is_dir():
            return d
    raise SystemExit("Not inside a brand system repository (no INDEX.md + core/ + projects/ found here or above). "
                     "cd into your clone of the brand system, or pass its path as the first argument.")


def check_fresh(root: Path, fetch: bool = True) -> str:
    """If root is inside a git clone with an origin, fetch quietly and report whether the checkout is behind
    origin/main. Returns a one-line warning or empty string. Never raises; offline is silent."""
    import subprocess
    def git(*args):
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=20)
    try:
        if git("rev-parse", "--is-inside-work-tree").returncode != 0:
            return ""
        if git("remote", "get-url", "origin").returncode != 0:
            return ""
        if fetch:
            git("fetch", "--quiet", "origin", "main")
        behind = git("rev-list", "--count", "HEAD..origin/main")
        if behind.returncode != 0:
            return ""
        n = int(behind.stdout.strip() or 0)
        if n:
            return f"WARNING: this clone is {n} commit(s) behind origin/main. Run `git pull --ff-only origin main` before making changes."
        dirty = git("status", "--porcelain").stdout.strip()
        branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        if branch == "main" and dirty:
            return "WARNING: uncommitted changes on main. Work on a branch: `git switch -c <type>/<slug> origin/main`."
        return ""
    except Exception:
        return ""
