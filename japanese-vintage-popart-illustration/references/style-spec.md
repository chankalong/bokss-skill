# Visual Specification

## 1. Style definition

- Japanese vintage textbook illustration fused with Japanese pop-art screen printing.
- Useful English prompt keywords: `flat 2D editorial illustration`, `vintage Japanese educational illustration`, `Japanese pop-art screen printing`, `ink contour line art`, `halftone patterns`, `limited palette`.
- Mood: natural, friendly, plain and clean, with the nostalgia of an old printed page.
- Not watercolour, not American comic, not anime, not 3D. The vintage feel comes from line quality and halftone dots, not from grain filters, paper texture or faded overlays.

## 2. Composition

- Pure white background. People are the only subject. Props exist only to support an action.
- Full figure or seven-eighths figure. Leave about 5 to 8 percent of the image height above the head and white space below the shoes.
- Group people in a triangle, a half-moon or a staggered front-back arrangement. Avoid a straight row.
- Keep breathing room between people. Arms should not press into another person's outline.
- 16:9 is the default. 3:2 suits article headers. 1:1 needs two people in a compact seated or standing group, with every head, hand and foot inside the frame.
- No border, no coloured paper block, no ground line, no cast shadow, no background decoration.

## 3. People

### Proportions

- Adults about 6.5 to 7.5 heads tall. Teenagers about 6 to 7. Children about 4.5 to 5.5.
- Limbs should look plausible. Hands may be simplified, but should not become balls or stick figures.

### Face

- Oval or slightly square face with a simple jawline.
- Eyes are one or two solid dark dots, or very short curved lines. No whites of the eyes, no eyelashes, no pupil highlights.
- Nose is one short vertical line, a small hook or a side fold.
- Mouth is a short curved smile. A speaking person may have a small open mouth.
- Eyebrows are usually omitted, or reduced to one very short line.
- Glasses use two or three round or square frames in the same ink as the main outline.

### Hair

- Use a large solid dark shape, or a dark base with white halftone dots.
- Shape the hairstyle with the outer contour. Do not draw individual strands.
- A parting line or a few angled tips are enough. Avoid dense parallel lines.
- Dark hair usually uses the darkest supplied colour, the same as the outline.

### Clothing

- Collar, cuff, pocket and hem need only one or two lines.
- Each person gets at most one or two patterned garments. Keep the rest solid to avoid visual noise.
- Patterns follow the garment shape but do not create a gradient or shading effect.
- Shoes and socks can echo the main colour or the darkest colour.

### Poses and interaction

- Sitting, standing, crouching, leaning on a table or sitting cross-legged are all acceptable. Keep the centre of gravity believable.
- People who talk look at each other. People who make something look at their hands. An instructor looks at the participant or at the object being demonstrated.
- Use a hand-off, a pointing finger or a forward lean to show the relationship.
- Avoid having everyone face the camera.

## 4. Lines

- One ink colour only: the darkest supplied colour. Do not use pure black unless the user supplied black.
- For an image 1024 to 1536 pixels wide, outer contours are about 3 to 5 pixels, interior details about 1.5 to 2.5 pixels.
- Line ends taper slightly, corners are rounded, and weight varies a little to keep a hand-drawn feel.
- Draw only the main clothing folds. Two or three lines are enough. Do not fill garments with dense hatching.
- Do not use a white outline or glow to separate overlapping people. Use line and white space instead.

## 5. Textures

Four usable families:

| Texture | English wording | Good for |
| --- | --- | --- |
| Round halftone dots | `round halftone dots, evenly spaced, 45-degree grid` | Jackets, vests, lanterns, hair, bags |
| Gingham check | `gingham check` or `windowpane plaid` | Trousers, skirts, shirts, aprons |
| Diagonal hatching | `diagonal hatching` or `cross-hatching` | Trousers, bags, chair seats, darker blocks |
| Stripes | `simple even stripes` | Sweaters, T-shirts, socks |

Density control:

- Dot diameter is about half the main line width. Dot spacing is about 1.5 to 2 times the dot diameter.
- Keep halftone coverage at or below 30 percent of each garment. At least 70 percent of each patterned garment stays white or solid colour.
- At normal viewing size, the pattern should read as texture, not turn the garment grey.
- Use at most three pattern families in one image.

## 6. Colour

- Use only 2 or 3 supplied colours plus white.
- Suggested roles:
  - Darkest colour: lines, hair, shoes, dark trousers.
  - Main colour: the largest garment or the key prop.
  - Third colour: inner top, socks, stripes, checks, small patterns.
- Make lighter tones with the same ink at 20 to 40 percent dot density. This is not a new hue.
- Adjacent colour blocks need a clear lightness difference. Do not place two similar mid-tones next to each other.
- Skin, eye whites and background are always `#FFFFFF`.
- Do not add gold, silver, neon, metallic or any unlisted colour.

## 7. Props

- Draw only objects that support the action. Keep 3 to 5 main props.
- Common props: laptop, tablet, headphones, lantern, scissors, glue, brush, picture book, teacup, long table, chair, wooden crate, whiteboard, bicycle.
- Props use lines and local halftone only. Do not imitate real materials.
- No brand, text, screen content or label on any prop. Screens stay blank or carry a simple line diagram.
- Tables and chairs use simple perspective. Let people overlap them naturally. Do not turn them into an architectural drawing.

## 8. Common failures and fixes

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Anime eyes | The prompt contains anime triggers, or the model over-copies a reference | Add `natural proportions, tiny solid dot eyes, no manga eyes, no eyelashes`; put `anime, manga, chibi, oversized eyes` in the negative prompt |
| Grey, gradient or paper-textured background | The model adds its own lighting | Add `pure white #FFFFFF background, no paper texture, no vignette, no gradient` |
| Skin turns flesh-coloured | The model fills by habit | Add `skin left pure white with only line details, no skin tone` |
| Halftone turns grey | No density limit | Add `sparse halftone, at most 30 percent dot coverage, large white areas` |
| Extra colours appear | Only colour names were used | List every `#RRGGBB` and add `no other hues` |
| White sticker edge | The model adds a cut-out effect | Add `no white outline, no halo, no sticker border around figures` |
| Lines turn black | The ink colour was not specified | Add `all outlines, hair and shoes in #XXXXXX` |
| Props clutter the image | The scene description is too long | Keep 3 to 5 key props and delete the rest |
| People stand in a row | No front-back relationship was described | State who sits, who stands and who crouches |

## 9. Example breakdown

### example-group-discussion.jpg

- Four people: one sits on a crate with a laptop, one stands with headphones and a tablet, one sits on the floor, one stands and speaks.
- The group forms a triangle. The eye line moves from left to right.
- The lines are dark blue. The coral jacket carries navy halftone. The checked trousers use navy lines. Large white areas remain.
- Useful reference: group height variation, pattern density, how hands hold devices.

### example-lantern-workshop.jpg

- An instructor stands on the left. Three participants sit along a long table. Lanterns, scissors, glue and brushes are on the table.
- Coral sweater, pink stripes, checked trousers and a halftone top. Many textures, but each area is small.
- The table objects are tidy, with white space in the middle and no text.
- Useful reference: simplified table props, seated poses, the instructor pointing at a demonstration object.

The approximate palette of the two examples is dark blue `#0B1C63`, coral `#F5776E`, pale pink `#E7C6C8` and grey-purple `#8C7F9E`. These are examples only, not presets. Never treat them as the user's palette.

## 10. Output specifications

- PNG for lossless output, JPG for a smaller file.
- Default 16:9. Other useful ratios: 3:2, 4:3, 1:1.
- The background is opaque white, not transparent. Transparent output violates the white-background rule.
- Do not add sharpening, filters, grain or colour grading after generation. Keep the flat print look.
