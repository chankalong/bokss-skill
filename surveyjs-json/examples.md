# SurveyJS JSON example

Minimal valid survey: required first page, one 2-item scale, hidden score page.

```json
{
  "locale": "tc",
  "title": {
    "default": "Working Class Assessment",
    "tc": "在職人士評估問卷"
  },
  "pages": [
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
        },
        {
          "type": "text",
          "name": "career",
          "title": {
            "default": "Work / Industry",
            "tc": "工作/行業 Career"
          },
          "isRequired": true
        }
      ]
    },
    {
      "name": "wsas",
      "title": {
        "default": "Work and Social Adjustment Scale (WSAS)",
        "tc": "工作與社會適應量表 (WSAS)"
      },
      "elements": [
        {
          "type": "panel",
          "name": "wsas_instructions",
          "title": {
            "default": "Please read each item and select 0 to 8. 0 = no impact; 8 = very severe impact.",
            "tc": "請小心閱讀每一題，選擇 0 至 8。0 = 沒有影響；8 = 非常影響。"
          },
          "elements": [
            {
              "type": "radiogroup",
              "name": "wsas_work",
              "title": {
                "default": "1. Because of my emotional distress, my ability to work is impaired.",
                "tc": "1. 因為我的情緒困擾，我的工作能力受到了影響。"
              },
              "isRequired": true,
              "choices": [
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
            },
            {
              "type": "radiogroup",
              "name": "wsas_home",
              "title": {
                "default": "2. Because of my emotional distress, my home management is impaired.",
                "tc": "2. 因為我的情緒困擾，我的家務管理能力受到了影響。"
              },
              "isRequired": true,
              "choices": [
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
            }
          ]
        }
      ]
    },
    {
      "name": "scores",
      "visible": false,
      "elements": [
        {
          "type": "expression",
          "name": "wsas_total",
          "title": {
            "default": "WSAS Total Score",
            "tc": "WSAS 總分"
          },
          "expression": "{wsas_work} + {wsas_home}"
        }
      ]
    }
  ],
  "headerView": "advanced"
}
```

## Scoring snippets

**Simple sum (WSAS 5 items):**

```json
"expression": "{wsas_work} + {wsas_home} + {wsas_social_leisure} + {wsas_private_leisure} + {wsas_relationships}"
```

**Subscale + grand total:**

```json
[
  {
    "type": "expression",
    "name": "fiat_ca_total",
    "title": { "default": "FIAT-Q-SF Conflict Aversion", "tc": "FIAT-Q-SF 衝突迴避總分" },
    "expression": "{fiat_ca_1} + {fiat_ca_2} + {fiat_ca_3} + {fiat_ca_4} + {fiat_ca_5}"
  },
  {
    "type": "expression",
    "name": "fiat_total",
    "title": { "default": "FIAT-Q-SF Total", "tc": "FIAT-Q-SF 總分" },
    "expression": "{fiat_ca_total} + {fiat_other_total}"
  }
]
```

**Reverse item then sum:**

```json
"expression": "{phq_1} + (3 - {phq_2}) + {phq_3}"
```

**Cutoff category from a total:**

```json
{
  "type": "expression",
  "name": "wsas_band",
  "title": { "default": "WSAS band", "tc": "WSAS 分類" },
  "expression": "iif({wsas_total} < 10, 'mild', iif({wsas_total} < 21, 'moderate', 'severe'))"
}
```
