---
name: surveyjs-json
description: Writes SurveyJS survey JSON for BOKSS assessments with bilingual Traditional Chinese (tc) + English, locale tc, required first-page pre/post test and completion date, and a hidden last page of expression score totals. Use when creating, converting, or editing SurveyJS questionnaire JSON, assessment forms, or scale surveys.
---

# SurveyJS JSON

Output valid SurveyJS JSON. Display language is Traditional Chinese.

## Hard rules

1. **First page** must include at least these two questions: pre/post test (`testType`) and completion date (`completionDate`). Extra first-page fields are allowed after them.
2. **Last page** must be hidden (`"visible": false`) and hold `expression` questions that calculate scores.
3. **Every user-visible string** is bilingual: English in `default`, Traditional Chinese in `tc`. Root `"locale": "tc"`.

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
- Localize `title` (survey, page, panel, question) and choice `text` only.
- Question `name` / choice `value`: stable ASCII (`testType`, `pre`, `wsas_work`). Never put Chinese in `name` or `value`.

## Page order

1. `general_info` — required `testType` + `completionDate`, then any extra fields
2. Scale / content pages (panels to group items or instructions)
3. Optional staff-only pages (visible; not required)
4. **`scores` — always last, always hidden**

## First page (required)

Copy these two questions verbatim as the first elements of page `general_info`. Keep `name`, `title`, and `choices` exactly as below.

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

Do not replace `testType` with a dropdown of 前測/中期/後測 unless the user explicitly asks. Do not use `inputType: "date"` unless asked (import compatibility).

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

- One `expression` per total **and** per subscale the source scoring key defines.
- Reference items with `{questionName}`. Values are numeric strings (`"0"`…); SurveyJS coerces them in `+`.
- Reverse-scored item: `{max} - {item}` e.g. `7 - {phq_2}` when 0–3 is reversed.
- Conditional / cutoffs: `iif({total} <= 9, 'higher_risk', 'lower_risk')`.
- Never put score expressions on a visible page. Never substitute `calculatedValues`.

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
| `"colCount"`, `"inputType"` | Omit unless asked |
| Locale `zh-tw` / `zh-hk` | `"tc"` |

## Workflow

1. Collect English + 繁體中文 for every title and choice (translate if only one language is given).
2. Build root (`locale`, bilingual `title`).
3. Build `general_info` with required `testType` + `completionDate` first.
4. Add scale pages (panels + radiogroups).
5. Add optional staff page **before** scores.
6. Add hidden `scores` page with one expression per total/subscale.
7. Close with `"headerView": "advanced"`.
8. Run the checklist.

## Checklist

- [ ] `"locale": "tc"`
- [ ] First page starts with `testType` then `completionDate`
- [ ] Last page `"visible": false` with `expression` score fields
- [ ] Every `title` and choice `text` has `default` + `tc`
- [ ] No bilingual `description` / `html`; no `calculatedValues`
- [ ] `"headerView": "advanced"`

Compact full example: [examples.md](examples.md).
