---
name: bokss-hk-writing
description: Draft Traditional Chinese service copy for Baptist Oi Kwan Social Service (浸信會愛羣社會服務處) websites, leaflets, programme blurbs, announcements, and centre newsletters. Use when writing BOKSS/愛群/樂心匯/ICCMW public or staff-facing service text that is not a Re:Fresh Insights article and not a clinical case note; also when stripping AI-套話 from that copy while keeping Hong Kong 書面語.
---

# BOKSS Hong Kong writing

Agency voice for **service copy**. Not Insights columns (`refresh-insights-writing`), not SurveyJS (`surveyjs-json`), not case notes (`clinical-safety-copilot`).

**Body:** Hong Kong 書面語. Titles may use light HK colloquial. Spoken Cantonese (`嘅／咗／唔／係／喺`) only inside「」. Not TW/CN 衛教, not LinkedIn.

## Agency facts (do not “improve”)

- Chinese: 浸信會愛羣社會服務處 (keep **羣** as on [bokss.org.hk](https://www.bokss.org.hk/))
- English: Baptist Oi Kwan Social Service (BOKSS)
- Mental health arm: 精神健康綜合服務; ICCMW centres branded **樂心匯** (灣仔 / 東區 / 葵青)
- Preferred people language: **復元人士**, 家屬／照顧者, 社區人士. Avoid default 精神病患者 / 病人
- Frame: 全人健康（身、心、社、靈）; 及早辨識; 外展; 社區接納與共融; 優勢與復元 — not diagnostic scare

Do **not** invent phone, fax, email, address, hours, fees, or catchment. If unknown: `【待核實：聯絡資料】` or ask. Do not diagnose readers.

## Service-page skeleton (omit empty slots)

1. 服務名稱（中 + EN if the brief is bilingual）
2. 宗旨及簡介 — one short paragraph
3. 服務目標 — 3–5 bullets
4. 服務對象 / 地區 — only if in the brief
5. 服務內容 — grouped (評估及輔導 / 活動 / 職訓 / 家屬 / 社區教育 / 朋輩 …)
6. 申請 / 退出 / 收費
7. 開放時間
8. 聯絡 — copy from source only

Leaflet / poster: shorter. Keep 對象 + 如何申請 + 聯絡. One CTA.

Announcement / 中心通訊: date + what + who + how to join. No fake “研究指出”.

## Lexicon

| Prefer | Avoid |
| --- | --- |
| 復元人士、精神健康、情緒困擾 | 精神病患 as default, 心靈雞湯 |
| 綜合社區精神健康服務、樂心匯 | Invented centre nicknames |
| 朋輩支援工作員 | 病友義工 as the job title |
| 外展探訪、及早辨識 | 強制就醫 scare copy |
| 照顧者、家屬 | 家屬一定「有病」 |
| 的／了／不是／在 in body | Body default 嘅／咗／唔係／喺 |
| 中學、小學、屋邨、社署、醫管局 | 國中、社區衛生服務中心 |

## Safety in public copy

- Do not tell readers they 符合某診斷
- Lasting distress → 聯絡本中心／專業社工／輔導 — not a treatment protocol
- Trauma in the news: short care line, no graphic method
- Helpline CTA only with a **verified** number from the user or official page

## Bilingual

If asked: `default` English matches the Chinese; do not mix TW/CN English (“mental disordered friends”). ICCMW English on the site uses “mental health service users” / “persons in mental recovery”.

## Checklist

- [ ] 書面語 body; Cantonese only in quotes
- [ ] 復元／全人健康 frame; no reader diagnosis
- [ ] No invented contacts or catchment
- [ ] Insights article? Switch to `refresh-insights-writing`
- [ ] Case note? Switch to `clinical-safety-copilot` (+ `pdpo-deidentify`)

Phrase bank: [references/lexicon.md](references/lexicon.md).
