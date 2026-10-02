#!/usr/bin/env python3
"""Check a Re:Fresh CKEditor HTML fragment against the theme class allowlist."""

import re
import sys
from pathlib import Path

ALLOW = set(
    Path(__file__).resolve().parents[1].joinpath("references", "classes.txt").read_text().split()
)


def main() -> int:
    html = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else sys.stdin.read()
    errors: list[str] = []

    if re.search(r"<\s*(style|script)\b", html, re.I):
        errors.append("Remove <style> and <script>.")
    if re.search(r"@(click|vue)\b|v-html|v-if|v-for|:href", html):
        errors.append("Remove Vue attributes. CKEditor HTML is static.")
    if re.search(r"<!DOCTYPE|<html\b|<head\b|<body\b", html, re.I):
        errors.append("Return a fragment only, not a full document.")

    unknown: list[str] = []
    for blob in re.findall(r"""class\s*=\s*["']([^"']*)["']""", html):
        for token in blob.split():
            if token not in ALLOW:
                unknown.append(token)
    if unknown:
        errors.append("Classes not in theme.css: " + ", ".join(sorted(set(unknown))))

    for style in re.findall(r"""style\s*=\s*["']([^"']*)["']""", html):
        errors.append(f"Inline style not allowed: {style!r}. Use a theme class.")

    for tag in re.findall(r"<img\b[^>]*>", html, re.I):
        alt = re.search(r"""alt\s*=\s*["']([^"']*)["']""", tag, re.I)
        if not alt or not alt.group(1).strip():
            errors.append(f"Image needs a non-empty alt: {tag[:120]}")

    if errors:
        print("FAIL")
        for item in errors:
            print(f"- {item}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
