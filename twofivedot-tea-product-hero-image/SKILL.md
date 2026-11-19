---
name: twofivedot-tea-product-hero-image
description: Use when creating premium twofivedot tea-bag e-commerce hero images while preserving original packaging artwork, printed text, and logos.
license: Complete terms in LICENSE.txt
---

# twofivedot Tea Product Hero Image

## Purpose

Create premium e-commerce hero images for twofivedot tea bag products while preserving the original product artwork, text, logos, colors, and packaging design.

This skill is intended for online shop product images, social media product visuals, campaign key visuals, and product-series promotional images.

---

## When to Use

Use this skill when the user provides:

- One main tea bag product image to be promoted.
- One or more supporting tea bag product images from the same series.
- Optional style or composition reference images.
- A request to create a premium, editorial, minimalist product image.

The main goal is to make one product visually dominant while using the other products only as supporting accents.

---

## Core Principle

**The original product artwork is a protected asset.**

Do not redesign, rewrite, redraw, translate, simplify, replace, or reinterpret any printed content on the tea bag packaging.

The following elements must remain faithful to the supplied product image:

- Chinese and English text
- Illustration
- Artist credit
- Logo
- Brand marks
- Product colors
- Border shape
- Packet shape
- Printed layout
- Relative placement of printed elements

Only the following transformations are allowed:

- Scaling
- Rotation
- Positioning
- Cropping by the image frame
- Natural perspective adjustment
- Realistic shadow
- Minor lighting integration required to place the packet naturally in the scene

If the generated product visibly changes its printed artwork or wording, regenerate or revise the image.

---

## Default Output

Unless the user specifies otherwise:

- Aspect ratio: **4:5**
- Orientation: portrait
- Use case: premium online shop / social media product hero image
- Visual style: editorial flat lay
- Background: warm ivory, soft beige, muted cream
- Lighting: warm natural light with soft directional shadows
- Mood: calm, refined, thoughtful, premium, handcrafted
- Props: minimal and secondary

---

## Composition Rules

### 1. Main Product

The main promoted tea bag must:

- Be placed near the visual center.
- Be rotated slightly to create an editorial stationery feel.
- Be fully or almost fully visible.
- Occupy approximately **60–70% of the total visual area** by default.
- Be significantly larger than all supporting products.
- Be the first object the viewer notices.
- Keep its important text, illustration, artist credit, and logo readable whenever possible.

The main product should visually dominate the composition.

### 2. Supporting Products

Supporting tea bags are used only to communicate that the product belongs to a wider series.

Default rules:

- Use no more than **2 supporting products** unless the user asks otherwise.
- Place them toward the outer edges or corners.
- Crop most of each supporting packet outside the frame.
- Show approximately **15–30% of each supporting packet**.
- Never allow a supporting packet to compete visually with the main product.
- Supporting packets may appear at the upper-left, upper-right, lower-left, or lower-right edges.
- Avoid symmetrical placement unless specifically requested.

### 3. Visual Hierarchy

Priority order:

1. Main product
2. Product artwork and text
3. Supporting products
4. Background styling
5. Decorative props

Decorations must never distract from the main product.

---

## Styling Direction

Preferred aesthetic:

- Contemporary editorial stationery
- Minimal luxury packaging
- Warm lifestyle photography
- Soft paper-based visual language
- Matte surfaces
- Subtle tactile texture
- Refined asymmetry
- Generous negative space
- Gentle natural shadows

Recommended palette:

- Warm ivory
- Soft beige
- Muted terracotta
- Dusty blue
- Warm cream
- Natural wood tones

Avoid:

- Bright artificial gradients
- Neon colors
- Heavy glossy surfaces
- Excessive decorative objects
- Busy food styling
- Strong patterned backgrounds
- Dramatic cinematic lighting that obscures product details

---

## Optional Props

Use props sparingly.

Suitable props include:

- Ceramic tea cup
- Small amount of amber tea
- Neutral stone or terrazzo tray
- Dried flowers
- Linen fabric
- Pale paper or notebook
- Wooden dish
- Minimal stationery objects

Props should:

- Stay near the frame edges.
- Be partially cropped where appropriate.
- Use neutral colors.
- Support the premium tea / gifting mood.
- Never overlap important product text.

---

## Reference Image Handling

If the user provides a reference image:

Use it only for:

- Composition
- Mood
- Negative space
- Color palette
- Lighting direction
- Editorial styling
- Layering approach

Do **not** copy unrelated objects literally unless requested.

Do not replace the tea packaging design with elements from the reference image.

---

## Image Generation Workflow

### Step 1 — Identify Inputs

Determine:

- Which image is the main product.
- Which images are supporting products.
- Whether a separate style reference is provided.
- Desired aspect ratio.
- Any specific size or composition instructions.

If the user clearly identifies the main product, do not ask again.

### Step 2 — Lock Product Fidelity

Treat each supplied tea packet image as a protected visual asset.

Explicitly instruct the image model:

> Preserve the supplied tea packet artwork, printed text, logo, illustration, colors, border, and packet shape. Do not rewrite, redraw, translate, remove, replace, or reinterpret any printed content.

### Step 3 — Build Composition

Default composition:

- Main product: center, diagonal, 60–70% visual area.
- Supporting product A: near upper-left edge, only 15–30% visible.
- Supporting product B: near lower-right edge, only 15–30% visible.
- Background: warm beige / ivory.
- Props: minimal.
- Lighting: warm soft sunlight.

### Step 4 — Generate

Use image editing / image generation with the supplied product images as references.

Prioritize:

1. Product fidelity
2. Main-product dominance
3. Clean editorial composition
4. Premium lighting
5. Decorative styling

### Step 5 — Quality Check

Before accepting the image, check:

- Is the correct tea bag clearly the hero product?
- Does the main product occupy more than 60% of the composition when requested?
- Are supporting products cropped so no more than about 30% of each is visible?
- Is any original text changed?
- Is any logo distorted?
- Has any illustration been altered?
- Are the packet shape and white borders preserved?
- Are props distracting?
- Is the background consistent with a premium e-commerce image?
- Does the image still look like the user's actual product?

If any protected product element is visibly changed, revise or regenerate.

---

## Default Prompt Template

Use the following structure as a base prompt:

> Create a premium e-commerce hero image using the uploaded tea bag product images.
>
> The designated main product must be the clear focal point. Place it diagonally near the center and enlarge it so that it occupies approximately 60–70% of the total visual area.
>
> Use up to two additional tea bag designs only as supporting accents. Move them toward the outer edges or corners and crop them heavily so that only approximately 15–30% of each packet is visible.
>
> Preserve all supplied product packaging exactly as shown. Do not alter, rewrite, translate, redraw, remove, replace, or reinterpret any printed text, illustration, logo, artist credit, color, border, or packaging design.
>
> Use a warm ivory or soft beige background with a refined editorial flat-lay aesthetic. Add only minimal lifestyle props such as a ceramic tea cup, neutral tray, dried flowers, linen, pale paper, or natural wood. Keep props subtle and secondary.
>
> Use soft warm natural light with gentle directional shadows. The overall mood should feel premium, calm, thoughtful, handcrafted, and suitable for a contemporary online shop.
>
> Maintain strong visual hierarchy: main product first, supporting products second, props last.

---

## User-Controlled Parameters

The user may override any default using short instructions.

Examples:

- `主產品：黃色款`
- `主產品佔畫面 70%`
- `配角每款最多顯示 20%`
- `背景改為 dusty blue`
- `不要茶杯`
- `只要紙張感，不要生活 props`
- `比例 1:1`
- `做得更似高級文具品牌`
- `留多啲負空間俾我加文案`
- `右上角留空`
- `配角只用一款`
- `光線柔和啲`
- `不要乾花`

Always follow explicit user instructions over defaults.

---

## Fast Invocation

The user can invoke this skill with a short request such as:

> 用 twofivedot Tea Product Hero Image skill。黃色係主產品，佔畫面 65%，另外兩款各自只露 20%，4:5。

Or:

> 用 twofivedot 茶包商品圖 skill，今次藍色兔仔做主角，背景保持米白，右邊留位放文案。

---

## Quality Standard

A successful output should look like a professionally art-directed online shop product image rather than a generic AI still life.

The viewer should immediately understand:

- Which tea bag is being promoted.
- What the real product looks like.
- That there are other designs in the series.
- That the brand feels warm, creative, refined, and giftable.

Product fidelity is always more important than decorative creativity.
