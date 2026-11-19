#!/usr/bin/env python3
"""Check a 2-3 colour palette for the Japanese vintage pop-art skill.

Usage:
    python3 palette_check.py "#E4573D" "#1B2A6B" "#F2C9C4"
    python3 palette_check.py "#E4573D" "#1B2A6B" --json

Checks contrast against the fixed pure-white background, picks the darkest
colour as the ink/outline colour, assigns primary and accent roles, and
prints a ready-to-paste English colour sentence for the image prompt.
Exit code 0 when the palette is usable, 1 on invalid input or a rejected palette.
"""

from __future__ import annotations

import argparse
import colorsys
import json
import re
import sys

HEX_RE = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def parse_hex(value: str) -> str:
    match = HEX_RE.match(value.strip())
    if not match:
        raise ValueError(f"Invalid hex colour: {value!r} (use #RRGGBB or #RGB)")
    digits = match.group(1)
    if len(digits) == 3:
        digits = "".join(ch * 2 for ch in digits)
    return "#" + digits.upper()


def rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def luminance(value: str) -> float:
    channels = []
    for c in rgb(value):
        s = c / 255
        channels.append(s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_vs_white(value: str) -> float:
    return 1.05 / (luminance(value) + 0.05)


def saturation(value: str) -> float:
    r, g, b = (c / 255 for c in rgb(value))
    return colorsys.rgb_to_hls(r, g, b)[2]


def distance(a: str, b: str) -> float:
    return sum((x - y) ** 2 for x, y in zip(rgb(a), rgb(b))) ** 0.5


def analyse(colors: list[str]) -> dict:
    if not 2 <= len(colors) <= 3:
        raise ValueError("Provide 2 to 3 colours (the style uses a limited palette).")
    if len(set(colors)) != len(colors):
        raise ValueError("Duplicate colours after normalisation. Supply 2 to 3 distinct hex codes.")

    ordered = sorted(colors, key=luminance)
    outline = ordered[0]
    rest = ordered[1:]
    primary = max(rest, key=saturation) if rest else None
    accent = next((c for c in rest if c != primary), None)

    rejections = []
    warnings = []

    if contrast_vs_white(outline) < 3.0:
        rejections.append(
            f"No deep colour for outlines ({outline} contrast {contrast_vs_white(outline):.2f}:1). "
            "Ask the user for one deeper colour; do not invent a navy or black."
        )
    elif contrast_vs_white(outline) < 4.5:
        warnings.append(
            f"The darkest colour {outline} has contrast {contrast_vs_white(outline):.2f}:1; "
            "lines may look faint. A deeper colour would be safer."
        )

    for color in colors:
        ratio = contrast_vs_white(color)
        if ratio < 1.3:
            rejections.append(
                f"{color} is almost white ({ratio:.2f}:1) and will disappear on the background."
            )
        elif ratio < 2.0:
            warnings.append(
                f"{color} is very pale ({ratio:.2f}:1); use it only as sparse halftone dots, not as a main fill."
            )

    for i, a in enumerate(colors):
        for b in colors[i + 1 :]:
            if distance(a, b) < 40:
                warnings.append(f"{a} and {b} are very similar; they may read as one colour.")

    if primary and distance(outline, primary) < 40:
        warnings.append("Outline and primary colours are close; consider swapping in a third distinct colour.")

    def role_for(color: str, solid_role: str) -> str:
        if contrast_vs_white(color) < 2.0:
            return "sparse halftone or thin stripes only, not a large fill"
        return solid_role

    role_map = {outline: "outline / ink, hair and shoes"}
    if primary:
        role_map[primary] = role_for(primary, "primary fill for garments and props")
    if accent:
        role_map[accent] = role_for(accent, "accent for inner tops, socks and small patterns")

    roles = []
    for color in colors:
        roles.append(
            {
                "hex": color,
                "luminance": round(luminance(color), 4),
                "contrast_vs_white": round(contrast_vs_white(color), 2),
                "role": role_map.get(color, "accent"),
            }
        )

    listed = ", ".join(colors[:-1]) + " and " + colors[-1] if len(colors) > 1 else colors[0]
    sentence = (
        f"Color: use ONLY {listed} plus pure white #FFFFFF. "
        f"Use {outline} for all outlines, hair and shoes."
    )
    if primary:
        if contrast_vs_white(primary) < 2.0:
            sentence += (
                f" {primary} is too pale for a large fill; use it only as sparse halftone dots or thin stripes."
            )
        else:
            sentence += f" Use {primary} as the main clothing colour."
    if accent:
        if contrast_vs_white(accent) < 2.0:
            sentence += (
                f" Use {accent} only as sparse halftone dots or thin stripes, never as a large solid fill."
            )
        else:
            sentence += f" Use {accent} for accent stripes, socks and small patterns."
    sentence += " Create lighter tones only with sparse halftone dots of the same inks. No other hues."

    return {
        "ok": not rejections,
        "colors": roles,
        "outline": outline,
        "primary": primary,
        "accent": accent,
        "rejections": rejections,
        "warnings": warnings,
        "prompt_line": sentence if not rejections else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a palette for the vintage pop-art illustration skill.")
    parser.add_argument("colors", nargs="+", help="2 to 3 hex colours, e.g. #E4573D #1B2A6B #F2C9C4")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of text")
    args = parser.parse_args()

    try:
        colors = [parse_hex(c) for c in args.colors]
        result = analyse(colors)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    code = 0 if result["ok"] else 1
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return code

    print("Palette accepted" if result["ok"] else "Palette rejected")
    for item in result["colors"]:
        print(
            f"  {item['hex']}  luminance {item['luminance']:.3f}  "
            f"contrast vs white {item['contrast_vs_white']:.2f}:1  role: {item['role']}"
        )

    if result["prompt_line"]:
        print("\nPrompt colour sentence:")
        print("  " + result["prompt_line"])

    print("\nRejections:")
    if result["rejections"]:
        for rejection in result["rejections"]:
            print(f"  - {rejection}")
        print("\nDo not generate. Ask the user for a replacement colour.")
    else:
        print("  None.")

    print("\nWarnings:")
    if result["warnings"]:
        for warning in result["warnings"]:
            print(f"  - {warning}")
    else:
        print("  None. Palette is ready to use.")
    return code


if __name__ == "__main__":
    sys.exit(main())
