#!/usr/bin/env python3
"""Port ICCMW production skills into the public bokss-skill library."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

SRC = Path("/Users/kalongchan/programmer/iccmw-knowledge-base")
DST = Path("/Users/kalongchan/programmer/bokss-skill")
MAP = json.loads((SRC / "scripts/skill_references_map.json").read_text())["skills"]

# Public library already has pdpo-deidentify covering this job.
SKIP = {"deidentify-case-text"}

SKILL_LINKS = {
    "skills/support/deidentify-case-text": "pdpo-deidentify",
    "skills/support/apply-diagnosis-approach": "apply-diagnosis-approach",
    "skills/support/document-therapy-techniques": "document-therapy-techniques",
    "skills/support/document-depression": "document-depression",
    "skills/support/extract-case-facts": "extract-case-facts",
    "skills/rewrite/social-worker-case-recording": "social-worker-case-recording",
    "skills/rewrite/ot-case-recording": "ot-case-recording",
    "skills/rewrite/clinical-psychologist-case-recording": "clinical-psychologist-case-recording",
    "skills/pathway/draft-intake": "draft-intake",
    "skills/pathway/draft-mh-assessment": "draft-mh-assessment",
    "skills/pathway/draft-5p": "draft-5p",
    "skills/pathway/draft-care-plan": "draft-care-plan",
    "skills/qa/case-qa": "case-qa",
}

KNOWLEDGE_TO_SKILL = {
    "knowledge/clinical/ethics/clinical-safety-patterns": "clinical-safety-copilot",
    "knowledge/clinical/ethics/ai-assisted-documentation": "clinical-safety-copilot",
}

PASSWORD_LINE = re.compile(r"^password:\s*bokss\s*\n", re.M)
WIKI = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
TRAILING_SLASH = re.compile(r"/+$")


def strip_password(text: str) -> str:
    text = PASSWORD_LINE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def normalize_wiki_target(raw: str) -> str:
    t = raw.strip()
    t = t.replace("\\", "/")
    t = TRAILING_SLASH.sub("", t)
    if t.endswith("/SKILL"):
        t = t[: -len("/SKILL")]
    if t.endswith("/index"):
        t = t[: -len("/index")]
    return t


def wiki_replacer(match: re.Match[str], bundled: set[str]) -> str:
    target = normalize_wiki_target(match.group(1))
    label = match.group(2)
    key = target
    if key.startswith("../../"):
        key = key.replace("../../", "")
    skill = SKILL_LINKS.get(key)
    if skill is None:
        for prefix, name in SKILL_LINKS.items():
            if key == prefix or key.startswith(prefix + "/") or key.endswith("/" + prefix.split("/")[-1]):
                skill = name
                break
    if skill:
        return f"`{skill}`"
    knowledge = KNOWLEDGE_TO_SKILL.get(key)
    if knowledge:
        return f"`{knowledge}`"
    base = Path(key).name
    fname = base if base.endswith(".md") else f"{base}.md"
    if fname in bundled:
        shown = label or base.replace(".md", "")
        return f"[{shown}](references/{fname})"
    if key.startswith("knowledge/") or key.startswith("skills/") or key.startswith("pilots/") or key.startswith("dify/"):
        shown = label or base.replace(".md", "").replace("-", " ")
        return shown
    if label:
        return label
    return base.replace("-", " ")


def rewrite_markdown(text: str, bundled: set[str]) -> str:
    return WIKI.sub(lambda m: wiki_replacer(m, bundled), text)


def copy_skill(name: str, spec: dict) -> None:
    rel = spec["path"]
    src_dir = SRC / "skills" / rel
    dst_dir = DST / name
    if dst_dir.exists():
        shutil.rmtree(dst_dir)
    dst_dir.mkdir(parents=True)
    (dst_dir / "references").mkdir(exist_ok=True)

    bundled: set[str] = set()

    def take_md(src: Path, dest_name: str | None = None) -> None:
        if src.name in {"README.md", "index.md"} or src.name.startswith("_"):
            return
        dest = dst_dir / "references" / (dest_name or src.name)
        dest.write_text(strip_password(src.read_text()), encoding="utf-8")
        bundled.add(dest.name)

    local = src_dir / "references_local"
    if local.is_dir():
        for p in sorted(local.glob("*.md")):
            take_md(p)
    refs = src_dir / "references"
    if refs.is_dir():
        for p in sorted(refs.glob("*.md")):
            if (dst_dir / "references" / p.name).exists():
                continue
            take_md(p)
    for item in spec.get("from_knowledge") or []:
        src = SRC / item["src"]
        if src.is_file():
            take_md(src, item["as"])

    skill_src = src_dir / "SKILL.md"
    body = strip_password(skill_src.read_text())
    body = rewrite_markdown(body, bundled)
    dst_dir.joinpath("SKILL.md").write_text(body, encoding="utf-8")

    for p in (dst_dir / "references").glob("*.md"):
        p.write_text(rewrite_markdown(p.read_text(), bundled), encoding="utf-8")

    leftover = list((dst_dir / "references").iterdir())
    if not leftover:
        (dst_dir / "references").rmdir()


def main() -> None:
    for name, spec in MAP.items():
        if name in SKIP:
            print(f"skip {name} (use pdpo-deidentify)")
            continue
        copy_skill(name, spec)
        print(f"ported {name}")


if __name__ == "__main__":
    main()
