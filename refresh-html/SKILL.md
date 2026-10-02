---
name: refresh-html
description: >-
  Build paste-ready HTML for CKEditor on refresh.bokss.org.hk using only
  classes from the official BOKSS theme CSS. Use when designing or writing
  HTML blocks for Re:Fresh pages, Insights bodies, landing sections, callouts,
  cards, buttons, FAQs, comparison tables, or video embeds that must match
  the live theme without a style tag.
---

# Re:Fresh CKEditor HTML

Paste-ready HTML for body fields on [refresh.bokss.org.hk](https://refresh.bokss.org.hk/). The page already loads [theme.css](https://refresh.bokss.org.hk/themes/custom/bokss/css/theme.css) and [lz_theme.css](https://refresh.bokss.org.hk/themes/custom/bokss/css/lz_theme.css). Insights and most nodes wrap the body in `<div class="prose">`.

**Output one HTML fragment.** No doctype, `<html>`, `<head>`, `<body>`, `<style>`, `<script>`, Vue (`v-html`, `:href`, `@click`), or invented Tailwind classes.

## Workflow

1. Keep the user's words, links, and image URLs. If they also want the copy written, follow `refresh-insights-writing` (Insights) or `bokss-hk-writing` (service pages). Do not invent phone, email, address, fees, or helplines.
2. Pick one pattern from [references/patterns.md](references/patterns.md). Button colour, hover, and cursor are in [references/design-system.md](references/design-system.md). Tokens are in [references/tokens.md](references/tokens.md).
3. Write the fragment. Start headings at `h2` (the page title is already `h1`).
4. Run the checker and fix every failure before returning:

```bash
python3 scripts/check_classes.py fragment.html
```

5. Return the HTML in one fenced `html` block, plus one line naming the pattern. If an image URL is unknown, use `src=""` and `【待補：圖片】` in `alt`, and say so.

## Hard rules

- A class is allowed only if it is in [references/classes.txt](references/classes.txt). That file is a snapshot of compiled theme classes (2026-10-02) plus a few content classes from `lz_theme.css`. `p-5`, `gap-8`, `rounded-lg`, `bg-blue-500`, `text-gray-default`, and `bg-green-default` are **not** in the build. Do not guess the Tailwind scale.
- No `<style>` block and no inline `style`, including on buttons.
- Inside `.prose`, `.prose a` turns button labels blue. Add `!text-grey-default` on orange, pale-yellow, green, and outline buttons. Do not lock red or black button text with `!text-white` or an inline colour: hover clears the fill and the theme changes that label colour. Prefer the pale or brand yellow button in article HTML. See [references/design-system.md](references/design-system.md).
- Yellow and light-orange backgrounds use `text-grey-default` or `text-black`. Do not put white text on `bg-orange-default`, `bg-orange-yellow`, or `btnRound-green`.
- Card grids and bands: add `not-prose` so prose heading sizes do not take over. Set `mb-*` on those paragraphs yourself.
- Buttons are real `<a>` with an `href` and visible text. External links: `target="_blank"` and `rel="noopener"`.
- Every `<img>` has a non-empty `alt`. Use `class="w-full"`. Do not copy huge `width`/`height` attributes.
- Do not use menu, form, Vue, member-zone, or calendar classes in page content.
- If the field is **not** already inside `.prose`, put `class="prose"` on the outer wrapper so headings and links pick up theme type.

## Paste

CKEditor → Source. The text format must keep `class` (Full HTML). Accordion and iframe need the format to allow `<dl>`, `<dt>`, `<dd>`, and `<iframe>`.

To preview, copy [assets/preview.html](assets/preview.html), replace `<!-- FRAGMENT -->`, and open the file. The preview loads the live theme CSS.
