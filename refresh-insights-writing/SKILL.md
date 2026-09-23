---
name: refresh-insights-writing
description: Use when drafting, rewriting, or outlining Re:Fresh / BOKSS Insights-style Traditional Chinese psychoeducation articles for Hong Kong readers—especially hot-topic mental-health explainers, workplace EAP pieces, parenting stress guides, or when asked to write like refresh.bokss.org.hk/insights.
---

# Re:Fresh Insights Writing

Hot-topic hook → named psychology concept → credible mechanism → usable steps → warm close.

**Design intent:** Same tone and a **similar** skeleton across pieces — not a rigid ten-box grid. **Encourage variation** by type, subtype, and length band. Do **not** pad empty sections just to fill every slot.

## Load order / Before drafting

**Mandatory for all agents (Claude, Cursor, LibreChat, etc.):** the host does **not** auto-inject these reference files. You **must** Read them yourself before drafting.

**Before drafting, Read these files in order:**

1. [references/colleague-brief.md](references/colleague-brief.md) — if brief fields are missing, ask or list gaps first; when type is **標準熱話科普**, **標準 subtype** is required
2. [references/article-types.md](references/article-types.md) — top-level type + 標準 subtypes; apply each row’s **required vs optional** slots (do not march every piece through the full default skeleton)
3. [references/gold-cards.md](references/gold-cards.md) — read the full gold-cards (Layer A+B); never copy full article text
4. [references/style-patterns.md](references/style-patterns.md) — when you need hook / title / CTA phrasing
5. [references/weekly-digest.md](references/weekly-digest.md) — when you need this week's preferences / GA weight hints
6. [references/corpus-index.md](references/corpus-index.md) (and [corpus-index.csv](references/corpus-index.csv)) — calibration / exemplar paths only; do **not** require a full corpus sweep

## Invariant (always)

These rules do **not** bend for “variety.”

**Core principle:** Validate first; name the mechanism; give doable steps; never fake science or diagnose the reader.

**Body language:** Hong Kong 書面語 (like published Re:Fresh pieces). Titles may use light HK colloquial (`點算好`、`好攰`). **Cantonese grammar particles as default prose (`嘅／咗／唔／係／喺` running through paragraphs) = fail** — put spoken Cantonese only inside「」. Not TW/CN web-psychoedu, not LinkedIn viral self-help.

**Floor (every draft):** ≥1 **named construct** with English gloss **and** ≥1 **actionable move** readers can try. Short pieces may use **1–2** mechanisms and **1–2** steps; do not drop both spirits.

**Mechanism bar:** Each key claim needs a real construct name, a known authority you can stand behind, or an explicit uncertainty phrase. **Fake studies, fake %, fake APA, invented researcher names = hard fail.** Under deadline: shorten; do not fabricate.

**Safety:**

- Never tell readers they「符合 PTSD／成癮症／抑鬱症診斷」
- Point lasting impairment toward 心理輔導／專業協助
- Trauma news: anger can be protective; urge media hygiene + self-care

**Length bands:** 心靈急救 ~600–1200｜標準 ~1500–2800｜深度／Plus ~2800–4500

**Checklist spirit:**

- [ ] HK hook + feeling validated before advice
- [ ] ≥1 named construct with English gloss
- [ ] ≥1 actionable move (2–4 when length allows)
- [ ] No fake citations; no reader diagnosis
- [ ] HKTC lexicon; close restores agency

## Default skeleton (標準熱話 default)

Use this as the **usual** path for **標準** length **標準熱話科普** (adjust via [Flexible slots](#flexible-slots) and [article-types.md](references/article-types.md)).

1. **Title** — `【熱話】痛點？心理學拆解…` / `痛點？N招…` / `疑問？心理學：重新命名…` (no clinical-scare SEO)
2. **Tags** — 4–7; include `#文章` + theme (`#情緒管理` `#工作壓力` `#心理彈性` …)
3. **文章摘要** — 2–4 bullets (common on 標準+; often skipped for 心靈急救)
4. **Byline** — `撰文：{Name}@Re:Fresh` or `撰文：@Re:Fresh`
5. **Hook** — HK scene / trend + 「你是否…」 (other hook kinds allowed — see Flexible)
6. **Mechanisms** — typically 2–4 `###`; Chinese name + English in parentheses
7. **Practice** — typically 2–4 steps readers can try today
8. **Close** — validate → agency → soft CTA optional
9. **參考資料** — real sources, or `參考資料：待補` + claim stubs — **never invent**
10. **Safety line** when trauma / suicide / abuse / addiction / diagnostic criteria appear (required when flagged; FAQ extra for 日子／國際日 — see article-types)

Pick **required vs optional** slots from the brief’s type, subtype, and length band — not every draft needs every numbered item above.

## Flexible slots

Variation is **allowed** (and expected). Never trade flexibility for oral-Cantonese body prose or fake citations.

| Element | May vary by type / subtype / length |
|---------|-------------------------------------|
| **Title** | Phrasing pattern (`【熱話】` vs plain question vs calendar prefix for 日子) |
| **Hook** | Scene / 熱話 trend / quote-led / news-care framing |
| **Mechanisms** | Count **1–4**; one deep construct vs several lighter ones |
| **Practice** | Count **1–4**; merged into close on very short pieces if one clear move remains |
| **文章摘要** | Present or omitted (often omitted for 心靈急救; optional for workshop funnel) |
| **CTA** | Absent, soft close only, mid-piece workshop link, or B2B EAP — position varies |
| **Safety / FAQ** | Safety line when brief flags risk; **FAQ / 守護行動** required for flagged 日子／國際日 pieces |

When in doubt: keep Invariant + floor; omit optional slots rather than filler paragraphs.

## Baseline drifts → fix

| Drift | Fix |
|-------|-----|
| LinkedIn listicle, weak mechanism | Restore named construct + practice floor |
| Diagnostic textbook SEO | Drop diagnoses; keep practice + warm close |
| 「研究指出」with nothing behind it | Name construct or `待補` |
| Padding empty slots to match a template | Drop optional slots; keep floor only |
| Whole piece in oral Cantonese 「更港」 | Rewrite body to 書面語; quotes only |
| Meta labels (`### 標題：`) in output | Emit real title/tags, not slot names |

Phrase banks: [references/style-patterns.md](references/style-patterns.md). Corpus weights: [references/corpus-index.md](references/corpus-index.md). Weekly context: [article-types.md](references/article-types.md), [colleague-brief.md](references/colleague-brief.md), [gold-cards.md](references/gold-cards.md), [weekly-digest.md](references/weekly-digest.md).
