---
name: japanese-vintage-popart-illustration
description: Create flat Japanese vintage pop-art halftone illustrations of people on pure white backgrounds with a strict 2-3 hex colour palette. Use for 日系復古插畫, 網點人物, editorial or social-media artwork.
---

# Japanese Vintage Pop-Art Illustration

Turn a short scene brief into a flat 2D illustration in the style of Japanese vintage educational books and pop-art screen printing: white background, hand-drawn ink contours, flat colour and halftone dots. This skill is tool-agnostic. Use the host agent's image-generation capability, or output the finished prompt when no image tool exists. Communicate with the user in their language; write every image prompt in English.

## Non-negotiable rules

1. Ask for 2-3 hex colours before generating. Never invent a palette. If the user says "use the sample colours", repeat them once and wait for confirmation.
2. Background is always opaque pure white `#FFFFFF`. No scenery, horizon, floor line, shadow, vignette, paper texture or colour block.
3. Skin is always pure white `#FFFFFF`, described only with lines. Never fill faces, hands or necks with a skin tone.
4. Use only the supplied colours plus white. Every garment, hair colour, accessory and prop comes from that palette. Make lighter tones with sparser halftone dots of the same ink, not with a new hue.
5. Use the darkest supplied colour for all outlines, hair and shoes. Thick outer contours, thin interior lines, slight hand-drawn wobble. Do not default to black.
6. Flat print look only: solid fills, even halftone dots, gingham checks, diagonal hatching, simple stripes. No gradients, shading, highlights, 3D, gloss or photorealism.
7. No text anywhere: no titles, labels, logos, signatures, screen content or hex codes.
8. No sticker border: no white outline, halo or cut-out edge around people or objects.
9. Natural proportions: adults about 7 heads tall, children about 5. Eyes are tiny solid dots or one short curved line, with one short nose line and a small smile. No eye whites, eyelashes, anime eyes, chibi or oversized heads.
10. People interact: eye contact, a shared task, a hand-off or a gesture. Avoid a row of people all facing the camera.
11. Show full figures and full props with white space above heads and below feet. Do not crop heads, hands, wheels or shoes.

## Workflow

### 1. Collect the brief

Ask once, in the user's language, for anything missing. Do not ask one item at a time.

| Field | What to confirm |
| --- | --- |
| Scene | What the people are doing and the setting type: workshop, group, counselling, family, online learning |
| People | Number, rough age, gender mix, poses, who looks at or acts toward whom |
| Colours | 2-3 hex codes, at least one clearly dark colour for lines |
| Aspect ratio | Default 16:9; 3:2 for article headers; 1:1 for square social posts |
| Use | Article image, poster, social post, shop banner or slide. This controls how tight the composition is |
| Props | 3-5 objects that support the action. Props must be blank, with no text |

If the user has already supplied enough, go straight to the palette check. Do not re-ask.

### 2. Check the palette

Run from the skill root:

```bash
python3 scripts/palette_check.py "#2B2D42" "#D1B6E1" "#58C9B9"
```

The script picks the darkest colour for ink, assigns primary and accent roles, checks contrast against white, and prints a ready-to-paste colour sentence. Use `--json` if the runtime prefers structured output.

Exit code 1 means the palette is rejected. That happens when no colour is dark enough for lines (contrast against white under 3:1), two hex codes are the same, or a colour disappears on white. Read the rejection, ask for a replacement colour, and do not generate. Exit code 0 with warnings is usable: follow the warning, usually by keeping a pale colour as sparse dots.

If Python is unavailable, apply the same rules by hand: the darkest colour must be clearly darker than the others, with contrast against white of at least 3:1. Reject a palette with no dark colour. Use very pale colours only for sparse dots, not large fills. Do not add a colour the user did not supply.

If the palette fails, ask the user for one deeper colour. Do not substitute navy or black yourself.

### 3. Write the prompt

Read `references/prompt-templates.md` and fill the template with the brief. Keep every required section: scene and people, composition, style and line quality, colour list, white background and skin, negative list. Write hex codes exactly as `#RRGGBB`, never as colour names alone.

For a complete filled prompt, read `references/worked-example.md`. Use it as a pattern, not as content to copy.

### 4. Generate with the host's image tool

Use whatever image-generation tool the host provides. Do not assume a specific tool name. Translate the request into that tool's parameters.

| Host capability | What to do |
| --- | --- |
| Text-to-image with reference images | Attach `assets/examples/example-group-discussion.jpg` and `assets/examples/example-lantern-workshop.jpg` as style references. Keep the reference sentence in the prompt. |
| Text-to-image only | Omit the reference sentence. Keep the style paragraph and the negative list. |
| Separate negative prompt | Move the "Avoid" list into the negative prompt. Keep negations out of the positive prompt if the tool penalises them. |
| Size parameters | Map 16:9 to 1536x864 or 1344x768; 3:2 to 1536x1024; 1:1 to 1024x1024; 4:3 to 1365x1024. |
| No image tool | Output the finished English prompt in a code block and tell the user it can be pasted into an image tool. Do not claim an image was generated. |

Save output to the folder the user chose, or `./output/` if none is given. Create the folder if it does not exist. Never write into the skill folder. Use PNG or JPG. The background must be opaque white, not transparent. Do not run background removal.

Generate one image by default. Generate 2-3 directions only when the user asks for options, and keep the same palette and prompt skeleton.

### 5. Check the result

Look at the image before delivering it. If an item fails, regenerate with a targeted instruction. Do not fix these problems with post-processing.

- [ ] All four corners and the space around the figures are pure white; no scenery, shadow or halo.
- [ ] Faces and hands are white, with no skin tone.
- [ ] Only the supplied colours and white appear.
- [ ] No gradients, highlights, 3D shading or glossy rendering.
- [ ] No text, labels, logos, signatures or hex codes.
- [ ] Natural proportions; eyes are tiny dots or one short curve, not anime eyes.
- [ ] Halftone and check patterns are light enough to read as texture, not grey.
- [ ] People look at each other or share an action.
- [ ] Every head, hand, wheel and shoe is inside the frame.

If one thing fails, change only that instruction and regenerate. If it still fails, rewrite the prompt from the template rather than layering corrections.

## Palette roles

- Darkest colour: outlines, hair, shoes and dark trousers.
- Most saturated mid-tone: main garment or key prop.
- Third colour: inner top, socks, stripes, checks or small patterns. If it is very pale, use sparse dots only.

Keep at least one large white or near-white area per person so the figure does not turn into a solid block.

## File map

- `references/style-spec.md`: full visual rules, line weights, pattern density and common failures.
- `references/prompt-templates.md`: English prompt template, scene vocabulary and correction prompts.
- `references/worked-example.md`: a complete two-person cycling brief and prompt.
- `assets/examples/`: two style reference images. Use them for line quality and pattern density only.
- `scripts/palette_check.py`: palette validation and colour sentence generator. Standard library only.

Resolve all relative paths from the folder containing this `SKILL.md`. In Claude Code, `${CLAUDE_SKILL_DIR}` may be available. In other hosts, use the skill folder path directly.

## Do not

- Do not add scenery, colour blocks, decorative lines or a ground shadow to fill empty space.
- Do not copy the people, lanterns, laptops or layout from the example images.
- Do not reuse the example palette (dark blue, coral, pale pink, grey-purple) unless the user explicitly asks for it.
- Do not add a third or fourth hue "for balance".
- Do not use paper grain, film grain, blur or colour grading to fake a vintage look. Texture must come from lines and halftone dots.
- Do not describe the image as "anime", "manga", "3D", "photorealistic" or "glossy".
- Do not put text on props, screens, posters or clothing.
