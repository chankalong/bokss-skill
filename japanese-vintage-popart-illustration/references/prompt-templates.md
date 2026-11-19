# Prompt Templates and Scene Vocabulary

Write every image prompt in English. Replace the bracketed fields with the current brief. Keep hex codes exactly as `#RRGGBB`.

## Base template

```text
Create a flat 2D editorial illustration for [USE CASE].

Scene: [SCENE].

People: [NUMBER AND DESCRIPTION OF PEOPLE]. Natural, slightly realistic proportions: adults about 7 heads tall, children about 5 heads tall. Simple minimal faces with tiny solid dot eyes or one short curved line, one short nose line and a small gentle smile. No eye whites or eyelashes. Natural interaction and eye contact: [WHO LOOKS AT WHOM / WHAT THEY DO TOGETHER].

Composition: full figures visible, a little white space above the heads and below the feet, grouped in a loose triangular arrangement with varied heights, [ASPECT RATIO] framing, nothing cropped.

Props: [3 TO 5 PROPS], drawn with simple ink lines and flat patterns, completely blank with no text, labels, logos or screen content.

Style: Japanese vintage hand-drawn educational illustration fused with Japanese pop-art screen printing. Hand-drawn ink contour lines with slight wobble, thicker outer contours and thinner interior details, gentle and friendly mood.

Color: use ONLY these hex colors for every garment, hair colour, accessory and prop: [COLOR 1], [COLOR 2], [COLOR 3]. Use [DARKEST COLOR] for all outlines, hair and shoes. Create lighter tones only with sparse halftone dots of the same inks. Skin and background are pure white #FFFFFF.

Texture: flat solid fills and uniform print patterns (round halftone dots, gingham checks, diagonal hatching, simple stripes), low to medium density, at most 30 percent coverage per garment, plenty of white breathing space.

Background: pure empty white #FFFFFF. No scenery, no floor line, no cast shadow, no vignette, no paper texture, no text, no labels, no hex codes, no sticker outline or halo around any figure.

[REFERENCE SENTENCE, ONLY IF THE TOOL ACCEPTS REFERENCE IMAGES]

Avoid: gradients, shading, highlights, 3D rendering, photorealism, glossy digital art, anime or manga style, chibi, oversized eyes, eyelashes, neon colours, extra hues, busy background, white sticker border, any text.
```

## Colour sentences

Two colours:

```text
Color: use ONLY #1B2A6B and #F5776E plus pure white #FFFFFF. All outlines, hair and shoes are #1B2A6B; garments and props use #F5776E as the main fill. No other hues.
```

Three colours with roles:

```text
Color: use ONLY #1B2A6B, #F5776E and #E7C6C8 plus pure white #FFFFFF. #1B2A6B is the ink for all outlines, hair and shoes. #F5776E is the main clothing colour. #E7C6C8 is the accent for inner tops, socks and small patterns. No other hues.
```

When a colour is very pale, add this sentence:

```text
[PALE COLOR] is very light against white; use it only as sparse halftone dots or thin accent stripes, never as a large solid fill.
```

Do not use colour names alone. Do not write "navy", "coral" or "mint" without the hex code.

## Reference-image sentence

Use this only when the host image tool accepts reference images:

```text
Use the reference images for line quality, pattern density and flat colour treatment only; do not copy their people, poses, objects or layout.
```

If the tool cannot accept reference images, delete the sentence. Do not describe the example images in words as a substitute; the style paragraph already covers the visual language.

## Scene vocabulary

| Scene | People and action | Props | Interaction focus |
| --- | --- | --- | --- |
| Group discussion or panel | 3 to 5 people seated in a circle; one leans forward, one nods, one takes notes | Chairs, notebook, water glass, tablet | People look at the speaker; the speaker looks at the group |
| Craft workshop | Instructor stands on the left; 3 participants sit along a long table | Lantern, clay, dried flowers, scissors, glue, brush | Instructor points at the sample; participants look at their own work |
| One-to-one counselling | Two chairs at an angle; the counsellor leans slightly forward; the participant rests both hands on the knees | Tissue box, notebook, teacup | Gentle eye contact; relaxed posture |
| Family activity | Adult and child sit side by side; the child holds up a finished piece | Picture book, crayons, drawing paper, blocks | Adult looks at the child and the work; the child smiles |
| Youth online learning | A young person sits at a desk with headphones and a laptop | Headphones, laptop, notebook, desk lamp | Screen stays blank; the person looks focused |
| Community booth | Staff stand behind a table; residents stand in front | Folding table, leaflet, small gift, tote bag | Staff hand over a leaflet; the resident takes it |
| Older adult group | Older adults sit; a staff member crouches or stands to the side | Teapot, board game, yarn, reading glasses | Staff and older adult talk at eye level |
| Team collaboration | 2 or 3 people stand at a whiteboard; one points at it | Whiteboard, marker, noticeboard | Whiteboard stays blank or carries simple line shapes |
| Cycling or outdoor activity | Two people ride bicycles side by side or one behind the other | Bicycles, baskets, water bottle, picnic mat | Riders look at each other, wave or point ahead |

Props must be blank. Avoid posters, roll-up banners, book covers and screen interfaces that will force text. Draw them as blank surfaces or from the back.

## People and proportions

| Aspect ratio | Suggested number of people | Composition |
| --- | --- | --- |
| 16:9 | 2 to 5 | Full figures, horizontal group, most common |
| 3:2 | 3 to 4 | Full figures, good for article headers |
| 4:3 | 2 to 4 | Full figures or seven-eighths |
| 1:1 | 2 | Seated or compact full figures, nothing cropped |

More than 6 people becomes crowded and the patterns fight each other. For a large group, split the image or reduce detail.

## Series consistency

When making a set of images for one campaign:

1. Keep the same hex palette and the same darkest ink colour.
2. Copy the character description exactly: age, hairstyle, glasses, clothing patterns and shoe colour.
3. From the second image onward, attach the two style examples plus one finished image, up to three references. Add this sentence:

```text
Keep the same character designs, line weight, pattern density and palette as the reference images. Only change the scene and poses.
```

4. Do not attach more than three references. Too many confuse the model.

## Correction prompts

Use a targeted edit or a fresh generation. Change one problem at a time.

| Problem | Correction sentence |
| --- | --- |
| Gradients or shading | `Remove all gradients, shading and highlights. Every fill must be a flat solid colour or a uniform dot pattern.` |
| Looks like anime | `Redraw the faces with natural adult proportions: tiny solid dot eyes, one short nose line, small smile. No manga eyes, no eyelashes, no chibi.` |
| Extra colours | `Recolour using only #A, #B, #C and pure white. Remove every other hue.` |
| Background not white | `Make the entire background pure white #FFFFFF. Remove the floor line, shadows, texture and any scenery.` |
| Halftone too dense | `Reduce pattern density so at most 30 percent of each garment is dots, and at least 70 percent stays flat colour or white.` |
| Text on props | `Remove all letters, numbers, labels, signs and screen content. All props must be blank.` |
| White sticker edge | `Remove any white outline, halo or sticker border around the figures.` |
| Figures cropped | `Zoom out so every figure is fully visible with white space above the head and below the feet.` |

If the correction still fails after one attempt, rebuild the prompt from the base template. Do not stack ten corrections in one prompt.

## Prompt hygiene

- Keep the prompt under about 450 English words unless the image tool supports long prompts. The base template is already detailed.
- Put the most important constraints early: scene, people, palette, background.
- Do not use "beautiful", "masterpiece", "best quality" or similar filler. They do not help this style and can push the model toward glossy digital art.
- Do not mention "white background" only once. Repeat it in the background paragraph and the negative list.
- Do not ask for a transparent background. The white must be part of the generated image.
- For tools that treat negations poorly, move the `Avoid` list into the negative prompt field and delete it from the positive prompt.
