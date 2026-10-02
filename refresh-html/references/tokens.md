# Theme tokens

Snapshot date: 2026-10-02. Source: `themes/custom/bokss/css/theme.css` and `lz_theme.css`. Body font on the published page is Noto Sans HK. Default text color is `#343434`.

The body field is already inside `.prose` (color `#313131`). Prose sets:

| Element | Result |
| --- | --- |
| `h2` | `#343434`, 1.5rem, bold, margin 1.5rem / 1rem |
| `h3` | `#343434`, 1.5rem, weight 600 |
| `p` | margin-bottom 1rem |
| `a` | `#0C488E`, weight 500, underline on hover |
| `ul` / `ol` | disc / decimal |
| `blockquote` | italic, left border |
| `table` | full width, cell padding |

`not-prose` opts **descendants** out of those `:where()` rules. It does **not** cancel `.prose a` (that rule has no `not-prose` guard). Beat link color with the `!` utilities below.

## Colour

| Class | Colour | Use |
| --- | --- | --- |
| `text-grey-default` / `bg-grey-default` | `#343434` | Body text; white text on this background |
| `text-grey-dark` | `#666666` | Secondary text on white |
| `text-grey-brown` / `border-grey-brown` | `#4A4A4A` | Dark border |
| `border-grey-light` | `#D8D8D8` | Card border |
| `bg-grey-f5` | `#F5F5F5` | Soft band |
| `bg-grey-ee` | `#EEEEEE` | Slightly darker band, table zebra |
| `bg-orange-default` | `#F9C810` | Brand yellow. Dark text only |
| `bg-orange-yellow` | `#F5C533` | Softer yellow band. Dark text only |
| `text-green-dark` | `#3F772C` | Eyebrow / step label |
| `text-blue` | `#0678BE` | Occasional emphasis, not body links |
| `text-red` / `btnRound-red` | `#E65456` | Alert or destructive action only |
| `text-black` / `text-white` / `bg-white` / `bg-black` | | As named |
| `bg-red-default` | `#D0021B` | From `lz_theme.css`. Rare alert fill |

`btnRound-green` fill is `#6FBE52` with dark text. There is no `bg-green-default` utility (only `hover:bg-green-default`).

## Buttons

Measured defaults, hover, and cursor: [design-system.md](design-system.md).

The site's default pill is the thin pale one. The brand yellow pill is the primary action. Both use black text outside `.prose`. Inside a body field add `!text-grey-default`.

| Role | Classes |
| --- | --- |
| Default「詳情」 | `btnRound-thin btnRound-orange-light !text-grey-default` |
| Primary「報名」 | `btnRound-thin btnRound-orange !text-grey-default` |
| Green | `btnRound btnRound-green !text-grey-default` |
| Outline | `btnRoundOutline !text-grey-default` |

Hover keeps `cursor: pointer`, drops the underline, and makes the fill transparent so the 1px border remains. It does not move or add a shadow. Outline hover fills with `#F9C810` instead. Do not use `btnRound-red` or `btnRound-black` in article HTML.

## Type and layout that exist

Type: `text-xs` `text-sm` `text-lg` `text-xl` `text-2xl` `text-3xl` `text-4xl` `text-5xl` `text-6xl` `font-bold` `font-normal` `leading-relaxed` `text-left` `text-center` `text-right` `italic` `underline`. Larger steps also exist at `lg:` (`lg:text-xl` through `lg:text-6xl`) and `xl:text-2xl` `xl:text-4xl`. There is no default `text-base` (only `sm:text-base`).

Layout: `block` `inline-block` `flex` `inline-flex` `grid` `flex-col` `flex-wrap` `items-center` `items-start` `justify-center` `justify-between` `grid-cols-1` `grid-cols-2` `grid-cols-3` `grid-cols-4` `w-full` `mx-auto` `overflow-hidden`.

Responsive grid/gap that exist: `sm:grid-cols-2` `sm:flex` `md:grid-cols-2` `md:grid-cols-3` `lg:grid-cols-2` `lg:grid-cols-3` `lg:grid-cols-4` `lg:flex` `lg:gap-4` `lg:gap-6` `lg:gap-8` `gap-2` `gap-3` `gap-4` `gap-6`.

Spacing that exists (not the full scale): `p-0` `p-1` `p-2` `p-3` `p-4` `p-6`; `px-3` `px-4` `px-5` `px-6` `px-8`; `py-2` `py-3` `py-4` `py-6` `py-8`; `m-1`; `my-2` `my-4` `my-6` `my-8`; `mt-2` `mt-4` `mt-6` `mt-8`; `mb-0` `mb-2` `mb-3` `mb-4` `mb-6` `mb-8`; `gap` as listed above. Many `lg:` padding/margin variants exist; check `classes.txt` before using one.

Radius and shadow: `rounded-sm` `rounded` `rounded-md` `rounded-3` `rounded-4` `rounded-full` `shadow-sm` `shadow` `shadow-lg`.

Borders: `border` (1px) plus a colour (`border-grey-light`, `border-grey-default`, `border-grey-brown`, `border-black`). `border-2` and `border-4` exist.

## Components

- `list-tick` draws a ✓ via `::before`. Inside prose also add `!list-none`, or the disc marker remains.
- `faq-container` / `faq-box` / `faq-question` — static FAQ, no JavaScript.
- `ckeditor-accordion` on a `<dl>` of `<dt>`/`<dd>`. The accordion module turns each `<dt>` into a toggle. Do not pre-build the toggle `<a>`.
- `benefit-compare-table` — white table, 4px border, odd rows `#EEEEEE`, first column 50% and left-aligned, other cells centered.
- `iframe-wrapper` — 16:9 frame. The `<iframe>` sits inside it.
- `lz-img-container` — 220px float left. `lz-align-right` — float right.
- `container` / `container-narrow` / `container-wide` — page shells. Skip them inside a body field; the node template already supplies width.
