#!/usr/bin/env python3
"""Validate the rampart skill (system design) package (and optionally the .skill zip).

Checks:
  1. SKILL.md frontmatter: name, description (non-empty, <=1024 chars)
  2. Every package-internal path referenced in markdown exists
  3. No unresolved relative escapes (../../) out of the package
  4. Optional: .skill zip contains the same files as the directory

Usage:
  validate_skill.py [skill_dir] [--zip path/to/rampart.skill]
Exit codes: 0 = pass, 1 = fail
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
DESC_RE = re.compile(r"^description:\s*(?:>-\n((?:[ \t]+.*\n?)+)|(.+))", re.M)
# package-internal refs: `references/...`, `templates/...`, `scripts/...`
INTERNAL_RE = re.compile(r"`((?:references|templates|scripts)/[\w./-]+)`")
ESCAPE_RE = re.compile(r"\]\(\.\./\.\./|\b(?:references|templates|scripts)/\.\./")


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)
    print(f"  FAIL  {msg}")


def ok(msg: str) -> None:
    print(f"  ok    {msg}")


def check_frontmatter(skill_md: Path, errors: list[str]) -> None:
    text = skill_md.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        fail("SKILL.md missing YAML frontmatter", errors)
        return
    fm = m.group(1)
    nm = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    if not nm or not nm.group(1):
        fail("frontmatter missing name", errors)
    else:
        ok(f"name = {nm.group(1)}")
    dm = DESC_RE.search(fm)
    if not dm:
        fail("frontmatter missing description", errors)
        return
    desc = " ".join((dm.group(1) or dm.group(2) or "").split())
    if not desc:
        fail("description empty", errors)
    elif len(desc) > 1024:
        fail(f"description {len(desc)} chars > 1024", errors)
    else:
        ok(f"description {len(desc)} chars (<=1024)")


def check_internal_links(root: Path, errors: list[str]) -> None:
    total = 0
    for md in sorted(root.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for ref in INTERNAL_RE.findall(text):
            total += 1
            if not (root / ref).exists():
                fail(f"{md.relative_to(root)}: broken ref `{ref}`", errors)
        for _ in ESCAPE_RE.findall(text):
            fail(f"{md.relative_to(root)}: relative escape outside package", errors)
    ok(f"{total} package-internal refs checked across {len(list(root.rglob('*.md')))} markdown files")


def check_zip(root: Path, zip_path: Path, errors: list[str]) -> None:
    if not zip_path.exists():
        fail(f"zip not found: {zip_path}", errors)
        return
    dir_files = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file()
        and p.name != ".DS_Store"
        and "__pycache__" not in p.parts
        and p.suffix != ".pyc"
        # co-located package archive (this repo's convention: <name>/<name>.skill)
        and not (p.name == zip_path.name and p.parent == root)
    }
    # zip stores paths under the skill folder name
    prefix = root.name + "/"
    with zipfile.ZipFile(zip_path) as z:
        zip_files = {n for n in z.namelist() if not n.endswith("/") and ".DS_Store" not in n}
    stripped = {n[len(prefix):] if n.startswith(prefix) else n for n in zip_files}
    missing = dir_files - stripped
    extra = stripped - dir_files
    if missing:
        fail(f"zip missing: {sorted(missing)}", errors)
    if extra:
        fail(f"zip has extra: {sorted(extra)}", errors)
    if not missing and not extra:
        ok(f"zip matches directory ({len(dir_files)} files)")
    # frontmatter readable from zip
    with zipfile.ZipFile(zip_path) as z:
        skill_in_zip = z.read(prefix + "SKILL.md").decode("utf-8")
    if not FM_RE.match(skill_in_zip):
        fail("SKILL.md inside zip has no frontmatter", errors)
    else:
        ok("SKILL.md inside zip parses")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("skill_dir", nargs="?", default=str(Path(__file__).resolve().parent.parent),
                   help="skill folder (default: parent of scripts/)")
    p.add_argument("--zip", dest="zip_path", default=None,
                   help="path to .skill archive to verify (default: sibling of skill dir if present)")
    args = p.parse_args()

    root = Path(args.skill_dir).resolve()
    errors: list[str] = []
    print(f"Validating {root}")

    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        fail("SKILL.md not found", errors)
    else:
        check_frontmatter(skill_md, errors)
        check_internal_links(root, errors)

    zip_path = Path(args.zip_path) if args.zip_path else root.parent / f"{root.name}.skill"
    if args.zip_path or zip_path.exists():
        print(f"Validating archive {zip_path}")
        check_zip(root, zip_path, errors)

    if errors:
        print(f"\n{len(errors)} error(s).")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
