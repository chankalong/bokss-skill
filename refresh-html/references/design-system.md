# Re:Fresh design system

Measured on 2026-10-02 from [theme.css](https://refresh.bokss.org.hk/themes/custom/bokss/css/theme.css) and the live pages (homepage, Insights listing, consultation). Homepage buttons sit outside `.prose`. CKEditor body HTML sits inside `.prose`, so article buttons need the extra text class noted below.

Font: Noto Sans HK. Body text `#343434`. Article prose text `#313131`. Prose links `#0C488E`, weight 500, underline on hover, cursor pointer.

## Buttons

Pill shape, `border-radius: 9999px`, `cursor: pointer`. No lift, no shadow, no transition. Hover and focus do not change the cursor.

Two widths:

| Role on the site | Classes | Resting fill | Resting text | Padding |
| --- | --- | --- | --- | --- |
| Default. Insights「詳情」, course「觀看」 | `btnRound-thin btnRound-orange-light` | `#FFF2CF` | `#000`, weight 700 | 9px 27px |
| Primary. Course「報名」, consultation apply | `btnRound-thin btnRound-orange` | `#F9C810` | `#000`, weight 700 | 9px 27px |
| Full-width choice (chatbot menu) | `btnRound btnRound-orange-light text-center w-full` | `#FFF2CF` | `#000`, weight 700 | 9px 45px |
| Green, rare | `btnRound btnRound-green` | `#6FBE52` | `#000`, weight 700 | 9px 45px |
| Red, rare | `btnRound btnRound-red` | `#E65456` | `#fff`, weight 700 | 9px 45px |
| Black, rare | `btnRound btnRound-black` | `#000` | `#F9C810`, weight 700 | 9px 45px |
| Outline | `btnRoundOutline` | transparent | `#343434`, weight 400 | 4.5px 18px, 2px border `#F9C810` |

`btnRound-thin` already includes the pill. Do not also add `btnRound` unless you want the wider 45px padding.

### Hover and focus

Filled buttons (`orange`, `orange-light`, `green`, `red`, `black`):

- Cursor stays `pointer`
- Underline is removed (`text-decoration: none`)
- Fill goes transparent (`--tw-bg-opacity: 0`)
- The 1px border stays in the fill colour
- Nothing moves

Text on hover, outside `.prose`:

| Variant | Hover text | Hover border |
| --- | --- | --- |
| `btnRound-orange-light` | stays `#000` | `#FFF2CF` (faint on white) |
| `btnRound-orange` | stays `#000` | `#F9C810` |
| `btnRound-green` | stays `#000` | `#6FBE52` |
| `btnRound-red` | changes to `#E65456` | `#E65456` |
| `btnRound-black` | changes to `#000` | `#000` |

Outline does the opposite: hover fills the pill with `#F9C810` and keeps the text `#343434`.

`btnRound-green-disable` is the exception: cursor becomes `default` and the green fill stays.

### Inside a CKEditor body

`.prose a` is stronger than the button text colour. An unfixed button label renders `#0C488E` at weight 500, including on the pale and yellow pills.

Add `!text-grey-default` to orange, orange-light, green, and outline buttons. The label stays `#343434` at rest and on hover, and the fill still clears. Weight stays 500 inside prose; that cannot be forced back to 700 with an existing class.

Do not add `!text-white` or `style="color:#fff"` on a red button. Hover clears the fill, and a locked white label disappears. Do not lock `btnRound-black` with `style="color:#F9C810"`: hover is supposed to turn that label black, and the inline colour blocks it. Use the pale or brand yellow button in article HTML.

Header icon links use `hover:-translate-y-1`. Content buttons do not.

## Type

| Use | Classes | Size |
| --- | --- | --- |
| Homepage section title | `text-3xl lg:text-5xl text-center font-bold text-grey-default` | 1.875rem, 3rem from `lg` |
| Space under that title | `mb-6 lg:mb-12` | |
| Article heading | plain `h2` / `h3` inside `.prose` | 1.5rem, `#343434` |
| Card title | `text-2xl font-bold text-grey-default` | 1.5rem |
| Category label | `text-sm text-green-dark` | `#3F772C` |
| Secondary line | `text-sm text-grey-dark` | `#666666` |

`.page-title` is the node template (centered, 1.875rem, 3rem from `lg`). Do not repeat it inside the body.

A homepage-style title inside the body must sit in `not-prose`, or prose heading rules fight the utilities:

```html
<div class="not-prose text-center mb-6 lg:mb-12">
  <h2 class="text-3xl lg:text-5xl font-bold text-grey-default">自助課程</h2>
</div>
```

## Cards and lists

Insights listing card, simplified for the body. The theme paints `.card .cat` in `#3F772C` and prefixes each `li` with `#`.

```html
<div class="card mb-6">
  <a class="!text-grey-default" href="/tc/example">
    <img class="thumb w-full mb-3" src="" alt="【待補：圖片】" />
    <div class="cat mb-2"><span class="text-sm">#情緒管理</span></div>
    <div class="text-2xl font-bold">卡片標題</div>
  </a>
  <div class="text-right pt-2 pb-3">
    <a class="btnRound-thin btnRound-orange-light !text-grey-default mx-2" href="/tc/example">詳情</a>
  </div>
</div>
```

The title link needs `!text-grey-default` because it is an `<a>` inside `.prose`. `not-prose` does not cancel `.prose a`.

Stacked full-width choices use `mb-3` between pills. Side-by-side actions use `mx-2`.

## Colour pairs that match the site

- Dark text `#000` or `#343434` on `#F9C810`, `#FFF2CF`, `#6FBE52`, `#F5F5F5`, `#EEEEEE`, white
- White text only on `#E65456`, `#343434`, or black
- Green `#3F772C` is for category labels, not button fills
- Red is a caution or a red pill, not a section background
