---
name: surveyjs-json
description: Writes SurveyJS survey JSON for BOKSS assessments with bilingual Traditional Chinese (tc) + English, locale tc, and a hidden last page of expression score totals. When editing existing JSON, preserve original names, values, titles, and widgets. Use when creating, converting, or editing SurveyJS questionnaire JSON, assessment forms, or scale surveys.
---

# SurveyJS JSON

Output valid SurveyJS JSON. Display language is Traditional Chinese.

When modifying an existing SurveyJS JSON, preserve every original `name`, `value`, title, and input widget. Add bilingual text and new scales around them. Use `testType` / `completionDate` only for new surveys, or when the source has no equivalent.

## Hard rules

1. **New vs edit:** decide first. **New survey** (no existing JSON): first page `testType` then `completionDate`, then extras. **Edit existing JSON** (user pasted a survey): keep their fields; do not inject `testType`/`completionDate` if they already have an occasion or date field.
2. **Last page** must be hidden (`"visible": false`) and hold `expression` questions that calculate scores. Never a visible results / 社工檢視 page unless the user wants scores on screen.
3. **Every user-visible string** is bilingual: English in `default`, Traditional Chinese in `tc`. Root `"locale": "tc"`. Do **not** add a Chinese/English language radiogroup; the host already switches locale.

Do not use bilingual objects on `description` or `html`. Do not use `"type": "html"` or `"calculatedValues"`. Put instructions in a **panel `title`**. End with `"headerView": "advanced"`.

## Root skeleton

```json
{
  "locale": "tc",
  "title": {
    "default": "English title",
    "tc": "繁體中文標題"
  },
  "pages": [],
  "headerView": "advanced"
}
```

- `"locale": "tc"` — survey opens in 繁體中文. Do not use `zh-tw` / `zh-hk`.
- `"default"` = English fallback; `"tc"` = 繁體中文.
- Localize `title` (survey, page, panel, question) and choice `text` only. Do not add an in-survey language question.
- **New survey:** bilingual title from the source papers; new `name` / `value` are stable ASCII. Never put Chinese in `name` or `value`.
- **Edit existing:** keep the original survey `title` (wrap a Chinese string into `"tc"` and add `"default"` English). Change `title` only if the user asks. Keep every original `name`, choice `value`, question `type`, and widget. New fields may use new ASCII names; never overwrite old names.

## Page order

1. First page — **new:** `general_info` with `testType` + `completionDate`, then extras. **edit:** keep their first-page `name`s and order; extras go after (or where the user asks)
2. Scale / content pages (panels to group items or instructions)
3. Optional extra pages only if the user asks (not a visible results page)
4. **`scores` — always last, always hidden**

## First page

**New survey:** `testType` then `completionDate` (snippet below). Extra fields after them. Two-option pre/post is the default for **new** surveys only. If the source form already has 前測 / 跟進 / 後測 (or similar three waves), use that instead of forcing two-option `testType`.

**Existing survey:** keep their first-page fields and order. Do not rename occasion/date fields (`question1`, `questionnaire_actual_date`, 問卷次數, etc.) or replace them with `testType` / `completionDate`. Extra fields (e.g. DASS-Y only vs full questionnaire) go **after** the preserved fields, or where the user asks. Three-way 問卷次數 is allowed and common.

`inputType: "date"`: keep when present in source JSON (including `min`/`max`). For brand-new date fields, omit `inputType` unless the user or source uses a date picker.

New-survey template:

```json
{
  "name": "general_info",
  "title": {
    "default": "General Information",
    "tc": "基本資料"
  },
  "elements": [
    {
      "type": "radiogroup",
      "name": "testType",
      "title": {
        "default": "Pre-test or Post-test",
        "tc": "前測或後測"
      },
      "isRequired": true,
      "choices": [
        {
          "value": "pre",
          "text": {
            "default": "Pre-test",
            "tc": "前測"
          }
        },
        {
          "value": "post",
          "text": {
            "default": "Post-test",
            "tc": "後測"
          }
        }
      ]
    },
    {
      "type": "text",
      "name": "completionDate",
      "title": {
        "default": "Completion Date (YYYY-MM-DD)",
        "tc": "完成日期 (YYYY-MM-DD)"
      },
      "isRequired": true
    }
  ]
}
```

## Last page — hidden scores

Always the final page. Participants never see it; expressions still run and values are stored in the result.

```json
{
  "name": "scores",
  "visible": false,
  "elements": [
    {
      "type": "expression",
      "name": "scale_total",
      "title": {
        "default": "Scale Total Score",
        "tc": "量表總分"
      },
      "expression": "{item_1} + {item_2} + {item_3}"
    }
  ]
}
```

- One `expression` per total **and** per subscale the scoring key defines.
- Reference items with `{questionName}`. Values are numeric strings (`"0"`…); SurveyJS coerces them in `+`.
- Reverse-scored item: `{max} - {item}` e.g. `7 - {phq_2}` when 0–3 is reversed.
- Cut-offs / severity bands **only** if the scoring key defines them (e.g. DASS-Y). Academic / pre–post scales: one total (and optional `score + ' / ' + max` string). No invented cut-offs.
- Never put score expressions on a visible page. Never substitute `calculatedValues`.
- Do **not** add a visible 社工檢視 / results / caseworker page unless the user explicitly wants people to **see** scores on screen. “Caseworker view” means fields stored in the result, not a visible page.
- Optional batteries: `"visibleIf": "{questionnaireScope} = 'full'"` on extra scale pages; `"clearInvisibleValues": "onHidden"` is OK so skipped scales do not keep leftover answers.

## Scale questions

- Likert / symptom items: `"type": "radiogroup"`, `"isRequired": true`.
- Group a scale under a **panel**; put 0–N instructions in the panel `title`.
- Choice `value` is the score as a string. Duplicate the bilingual `text` even when it equals the number.
- Number items in the `title` (`"1. …"`).

**0–8 choices** (copy for each item):

```json
[
  { "value": "0", "text": { "default": "0", "tc": "0" } },
  { "value": "1", "text": { "default": "1", "tc": "1" } },
  { "value": "2", "text": { "default": "2", "tc": "2" } },
  { "value": "3", "text": { "default": "3", "tc": "3" } },
  { "value": "4", "text": { "default": "4", "tc": "4" } },
  { "value": "5", "text": { "default": "5", "tc": "5" } },
  { "value": "6", "text": { "default": "6", "tc": "6" } },
  { "value": "7", "text": { "default": "7", "tc": "7" } },
  { "value": "8", "text": { "default": "8", "tc": "8" } }
]
```

**1–6 choices**: same pattern, values `"1"` through `"6"`.

Conditional follow-up:

```json
"visibleIf": "{presentingProblem} contains 'others'"
```

## Compatibility

| Avoid | Use instead |
|-------|-------------|
| Bilingual `description` / `html` | Panel `title` |
| `"type": "html"` | Panel |
| `"calculatedValues"` | Hidden last-page `expression` |
| `"colCount"` | Omit unless asked |
| `"inputType"` on **new** fields | Omit unless asked; **keep** `inputType` / `min` / `max` when the source survey already has them |
| Locale `zh-tw` / `zh-hk` | `"tc"` |

## Workflow

1. Decide **new vs edit**. If edit, inventory existing `name`s and do not change them.
2. Collect English + 繁體中文 for every title and choice (translate if only one language is given).
3. **New:** bilingual title from source papers; first page `testType` + `completionDate` (or the source’s three-wave occasion if it has one). **Edit:** wrap existing `title`; do not change it unless asked.
4. Add scale pages (panels + radiogroups) around preserved fields. New fields get new ASCII names.
5. Add hidden `scores` page with one expression per total/subscale. No visible results page.
6. Close with `"headerView": "advanced"`.
7. Run the checklist.

## Checklist

- [ ] `"locale": "tc"`
- [ ] First page uses `testType`+`completionDate` **only for new surveys** (or if source has no equivalent)
- [ ] If editing existing JSON: original `name` / `value` / question `type` / date `inputType` / survey title unchanged unless asked
- [ ] No in-survey language question
- [ ] No visible results page
- [ ] Last page `"visible": false` with `expression` score fields
- [ ] Cut-offs only where the scoring key defines them
- [ ] Every `title` and choice `text` has `default` + `tc`
- [ ] No bilingual `description` / `html`; no `calculatedValues`
- [ ] `"headerView": "advanced"`

Compact full example: [examples.md](examples.md).
