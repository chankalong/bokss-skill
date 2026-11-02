# Weekly digest — 2026-10-25 → 2026-10-31 (HKT)

Window: 7 days ending **2026-10-31**. Sunday incremental distill; no full-text archive in skill.

## Method

Distillation corpus = **all listed Insights** + **GA4** organic weights (not last-7-days-only).
See [corpus-index.md](corpus-index.md) + [corpus-index.csv](corpus-index.csv).

Data source: GA4 property `298556736`, metrics `organicGoogleSearchClicks` / `organicGoogleSearchImpressions`, landing contains `/insights`.
28d window: **2026-10-04 → 2026-10-31**.

This run’s GA4 MCP connection failed, so page-level rows were **not** re-pulled. Site totals, the 7d click sample, and the three scored URLs below come from the 2026-11-01 decision extract. Do not treat older per-URL clicks as this window.

## New / notable Insights

| Date (list) | Slug | Type | One-line pattern |
|-------------|------|------|------------------|
| 2026-10-30 | `sychology-effective-apology-relationship-repair-refresh-hk` | 標準・關係／親密／溝通技巧 | 口語引用開場 → 假道歉／二次傷害 → 承認責任 vs 請求原諒 → 3個修復步驟 |
| 2026-10-27 | `scam-victim-psychology-cognitive-dissonance-refresh-hk` | 標準・個人成長／情緒機制（evergreen） | H2：認知失調、沉沒成本／承諾升級、羞恥與孤立 → 懷疑家人被騙時怎樣幫忙 |

EN twin: **none** for both (`/en/insights/<slug>` 404). Unprefixed `/insights/<slug>` returns 200 and is still zh-hant. Apology slug spells `sychology` as published.

## GA4 organic (property `298556736`)

Site Insights totals — **7d:** 274 clicks / 30,090 imps; **28d:** 1,338 / 163,669.

Prior mid-week window (ending 2026-10-26, continuity only): 7d 235 / 31,996; 28d 1,291 / 165,516.

### Sample of top Insights landings by organic clicks (7d)

Date range: **2026-10-25 → 2026-10-31**. Decision extract only (not a full top-10). Impressions were not supplied, so CTR is not computed.

| Landing | Clicks |
|---------|-------:|
| `/tc/insights/5-Love-Languages` | 17 |
| `/tc/insights/caregivers` | 14 |
| `/tc/insights/Inner-child` | 11 |
| `/tc/insights/highly-sensitive-people` | 10 |
| `/tc/insights/amygdala-hijack` | 10 |

### 28d page ranks

Not rebuilt this run. Stored `weight_28d` and the Top 25 in [corpus-index.md](corpus-index.md) remain the pull ending **2026-10-26**. This window’s site total is **1,338** clicks / **163,669** impressions.

### Notes for writers / SEO desk

- Site organic clicks rose vs the prior week (7d 235 → 274; 28d 1,291 → 1,338) while impressions eased (7d 31,996 → 30,090; 28d 165,516 → 163,669).
- The 7d click sample is still evergreen construct pages (五愛、內在小孩、HSP、杏仁核) plus 照顧者. Not enough to swap gold cards: no new 28d page weights, and the new URLs have no organic rows.
- `off-duty-work-messages-3-tips-EAP`: **0** clicks / **1** impression (7d and 28d).
- Apology and scam-victim: **no organic rows** in either window.
- Gold Layer A/B paths **unchanged**.
- Avg position not in this extract; corpus `avg_pos_*` columns left blank.

## New Insights (this distill)

- 2026-10-30: `/tc/insights/sychology-effective-apology-relationship-repair-refresh-hk` — 別用「對不起」二次傷害：為什麼有些道歉，聽起來比犯錯更殘忍？ (clicks_28d=0, clicks_7d=0)
- 2026-10-27: `/tc/insights/scam-victim-psychology-cognitive-dissonance-refresh-hk` — 【詐騙心理】為什麼你愈勸，他愈信騙徒？揭開「不願醒」背後的心理困局 (clicks_28d=0, clicks_7d=0)

## Weight leaders (28d organic clicks) — skill focus

No new 28d page ranking this run. Stored leaders (pull ending 2026-10-26) are still the evergreen construct pages: 五愛的語言、高敏感、內在小孩、Automatic Thoughts、藝術治療減壓、辭職決策、照顧者、杏仁核劫持等。

## Maintenance

- Incrementally update corpus-index when listing gains URLs
- Refresh weights weekly from GA4 organicGoogleSearch* (28d primary, 7d contrast); GSC fallback if GA4 unavailable
- Re-pick gold-cards only when rank/type mix shifts materially
