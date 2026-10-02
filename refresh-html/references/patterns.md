# Patterns

Copy the closest pattern. Replace the Chinese with the user's copy. One fragment can combine two patterns (a callout under a card grid). Do not stack three decorative bands in one field.

## Section

```html
<h2>小標題</h2>
<p>一段說明，直接寫在內文裡。標題和連結會跟文章的 prose 樣式。</p>
<ul>
  <li>第一點</li>
  <li>第二點</li>
</ul>
```

## Callout

```html
<div class="not-prose bg-grey-f5 rounded-md p-4 my-6">
  <p class="font-bold text-grey-default mb-2">小提醒</p>
  <p class="text-grey-default mb-0">一句具體的話。不要只靠顏色表達警告。</p>
</div>
```

Yellow band (dark text only):

```html
<div class="not-prose bg-orange-yellow rounded-md p-6 my-8">
  <p class="font-bold text-xl text-grey-default mb-2">重點</p>
  <p class="text-grey-default mb-0">一句話。</p>
</div>
```

Alert (red is for real caution, not decoration):

```html
<div class="not-prose bg-white border border-grey-light rounded-md p-4 my-6">
  <p class="font-bold text-red mb-2">請注意</p>
  <p class="text-grey-default mb-0">如果情況持續，請聯絡專業人員。聯絡方法必須來自使用者提供的資料。</p>
</div>
```

## Cards

```html
<div class="not-prose grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 lg:gap-6 my-6">
  <div class="bg-white border border-grey-light rounded-md p-4 shadow-sm">
    <p class="text-green-dark text-sm font-bold mb-2">01</p>
    <p class="font-bold text-lg text-grey-default mb-2">卡片標題</p>
    <p class="text-grey-default mb-0">一句說明。</p>
  </div>
  <div class="bg-white border border-grey-light rounded-md p-4 shadow-sm">
    <p class="text-green-dark text-sm font-bold mb-2">02</p>
    <p class="font-bold text-lg text-grey-default mb-2">卡片標題</p>
    <p class="text-grey-default mb-0">一句說明。</p>
  </div>
</div>
```

Two columns, text beside an image. Omit the image column if there is no `src`.

```html
<div class="not-prose grid grid-cols-1 lg:grid-cols-2 gap-6 my-6 items-center">
  <div>
    <p class="font-bold text-xl text-grey-default mb-3">標題</p>
    <p class="text-grey-default mb-0">說明。</p>
  </div>
  <img class="w-full rounded-md" src="" alt="【待補：圖片】" />
</div>
```

## Buttons

Default pill is pale yellow. Primary action is brand yellow. Hover stays a pointer, removes the underline, and clears the fill so the border remains. No lift and no shadow. Full states: [design-system.md](design-system.md).

```html
<p class="my-6">
  <a class="btnRound-thin btnRound-orange !text-grey-default mx-2" href="/tc/example">報名</a>
  <a class="btnRound-thin btnRound-orange-light !text-grey-default mx-2" href="/tc/example">詳情</a>
</p>
```

Outline is the quiet second action. Hover fills it yellow.

```html
<p class="my-6">
  <a class="btnRoundOutline !text-grey-default" href="/tc/example">了解更多</a>
</p>
```

## Homepage section title

Use this only when the block should look like a homepage heading. Article sections stay a plain `h2`.

```html
<div class="not-prose text-center mb-6 lg:mb-12">
  <h2 class="text-3xl lg:text-5xl font-bold text-grey-default">自助課程</h2>
</div>
```

## Insight card

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

## Tick list

```html
<ul class="list-tick !list-none">
  <li>第一項</li>
  <li>第二項</li>
</ul>
```

## FAQ accordion

The accordion script is loaded on the site. Leave `<dt>` as plain text.

```html
<dl class="ckeditor-accordion">
  <dt>第一條問題？</dt>
  <dd><p>答案。</p></dd>
  <dt>第二條問題？</dt>
  <dd><p>答案。</p></dd>
</dl>
```

Static FAQ, always open:

```html
<div class="faq-container">
  <div class="faq-box">
    <p class="faq-question font-bold text-grey-default">問題？</p>
    <p class="text-grey-default mb-0">答案。</p>
  </div>
</div>
```

## Comparison table

```html
<div class="benefit-compare-table my-6">
  <table>
    <thead>
      <tr>
        <th>項目</th>
        <th>方案 A</th>
        <th>方案 B</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>內容</td>
        <td>✓</td>
        <td>—</td>
      </tr>
    </tbody>
  </table>
</div>
```

For a simple data table, use `<table>` with no wrapper. Prose already styles it. Header cells are `<th>`.

## Video

```html
<div class="iframe-wrapper">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="影片標題" allowfullscreen></iframe>
</div>
```

## Quote

```html
<blockquote>
  <p>引用原文。</p>
</blockquote>
```

## Image

```html
<img class="w-full rounded-md my-4" src="" alt="圖片說明" />
```

Small portrait floated left: `class="lz-img-container mr-4 mb-4"`.
