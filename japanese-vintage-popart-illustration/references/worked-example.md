# Worked Example: Instructor and Participant Cycling

This is a complete example of how to move from a short brief to a finished prompt. Use the structure, not the exact wording.

## Brief

- Use: article header for a community programme.
- Scene: a female instructor and a male participant ride bicycles side by side, both happy.
- People: two adults. The instructor is in her early 30s. The participant is in his late 20s.
- Colours: `#2B2D42` deep purple-grey, `#D1B6E1` pale lilac, `#58C9B9` teal.
- Aspect ratio: 16:9.
- Props: two city bicycles, front baskets, a water bottle, a bicycle bell.

## Palette check

```bash
python3 scripts/palette_check.py "#2B2D42" "#D1B6E1" "#58C9B9"
```

Expected roles:

- `#2B2D42`: outline, hair and shoes. Contrast against white is about 13.5:1.
- `#58C9B9`: main clothing colour and bicycle frames.
- `#D1B6E1`: pale accent. Contrast against white is only about 1.8:1, so use it for gingham checks, sparse dots and thin stripes, not a large solid fill.

## Filled prompt

```text
Create a flat 2D editorial illustration for a community programme article about a mentor and a participant cycling together.

Scene: A cheerful cycling moment between a woman instructor and a male participant, riding two bicycles side by side across the frame.

People: Two adults. On the left, a female instructor in her early 30s with shoulder-length dark hair, wearing a teal #58C9B9 knit cardigan over a plain white top and lilac #D1B6E1 gingham-check cropped trousers, seated on her bicycle slightly ahead, turning her head back over her shoulder toward the participant with a warm open smile, one hand on the handlebar, the other hand gesturing forward. On the right, a male participant in his late 20s with short dark hair, wearing a plain white T-shirt with thin teal #58C9B9 horizontal stripes and lilac #D1B6E1 shorts with sparse halftone dots, seated on his bicycle beside her, looking at her and grinning happily. Natural, slightly realistic proportions: adults about 7 heads tall. Simple minimal faces with tiny solid dot eyes or one short curved line, one short nose line and a small gentle smile. No eye whites or eyelashes. Natural interaction and eye contact: the two riders look at each other and laugh together, both clearly happy.

Composition: full figures and entire bicycles visible, a little white space above the heads and below the wheels, the two riders side by side with the left bicycle slightly ahead for depth, 16:9 framing, nothing cropped, loose and airy.

Props: two simple city bicycles with round spoked wheels, handlebars, pedals and small front baskets; a water bottle on one frame; a small round bicycle bell on one handlebar. All props drawn with simple ink lines and flat patterns, completely blank with no text, labels, logos or lettering.

Style: Japanese vintage hand-drawn educational illustration fused with Japanese pop-art screen printing. Hand-drawn ink contour lines with slight wobble, thicker outer contours and thinner interior details, gentle and friendly mood. Flat 2D, not 3D, not anime.

Color: use ONLY these hex colors for every garment, hair colour, accessory and prop: #2B2D42, #D1B6E1 and #58C9B9. Use #2B2D42 for all outlines, hair and shoes. Use #58C9B9 as the main clothing colour and for the bicycle frames. Use #D1B6E1 only as sparse halftone dots and thin accent stripes, socks and small patterns, never as a large solid fill. Create lighter tones only with sparse halftone dots of the same inks. Skin is pure white #FFFFFF with only line details, no skin tone.

Texture: flat solid fills and uniform print patterns (round halftone dots on a 45-degree grid, gingham checks, diagonal hatching, simple even stripes), low to medium density, at most 30 percent coverage per garment, plenty of white breathing space.

Background: pure empty white #FFFFFF. No scenery, no ground line, no road, no trees, no sky, no cast shadow under the wheels, no vignette, no paper texture, no text, no labels, no hex codes, no signature, no sticker outline or halo around any figure.

Use the reference images for line quality, pattern density and flat colour treatment only; do not copy their people, poses, objects or layout.

Avoid: gradients, shading, highlights, 3D rendering, photorealism, glossy digital art, anime or manga style, chibi, oversized eyes, eyelashes, neon colours, extra hues, busy background, white sticker border, any text.
```

## Host adapter notes

- If the image tool accepts reference images, attach `assets/examples/example-group-discussion.jpg` and `assets/examples/example-lantern-workshop.jpg`. Keep the reference sentence.
- If the tool is text-only, delete the reference sentence. The rest of the prompt still works.
- If the tool has a separate negative prompt, move the `Avoid` list there and remove it from the positive prompt.
- For a 1536-pixel-wide output, 16:9 is 1536x864. For a smaller file, 1344x768 is also 16:9.

## What to inspect

The finished image should pass all of these:

- The woman and the man look at each other, and both are smiling.
- The two bicycles are fully inside the frame, including both wheels.
- Faces, hands and necks are white with line details only.
- The teal is the dominant garment and bicycle colour.
- The lilac appears as checks, dots or thin stripes, not as a large flat block.
- The background is pure white, with no road, shadow or scenery.
- There is no text on the bicycles, baskets or clothing.
- The faces read as natural adults, not anime characters.
