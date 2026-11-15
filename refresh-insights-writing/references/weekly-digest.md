# Weekly digest — 2026-11-08 → 2026-11-14 (HKT)

Window: 7 days ending **2026-11-14**. Sunday incremental distill; no full-text archive in skill.

## Method

Distillation corpus = **all listed Insights** + **GA4** organic weights (not last-7-days-only).
See [corpus-index.md](corpus-index.md) + [corpus-index.csv](corpus-index.csv).

Data source: GA4 property `298556736`, metrics `organicGoogleSearchClicks` / `organicGoogleSearchImpressions`, dimension `landingPagePlusQueryString` contains `/insights`.
28d window: **2026-10-18 → 2026-11-14**.

## New / notable Insights

| Date (list) | Slug | Type | One-line pattern |
|-------------|------|------|------------------|
| 2026-11-10 | `working-carers-respite-guide-EAP` | Re:Fresh Plus 深度專欄 | 在職照顧者日常場景開場 → 定義雙重角色／無形牽掛 → 照顧者倦怠警號 → 界線／把不好意思變成謝謝／允許休息 |

EN twin: **none** (`/en/insights/working-carers-respite-guide-EAP` 404). Unprefixed `/insights/<slug>` returns 200 and is still zh-hant. Byline: 張家瑛 Kiwi（本處輔導心理學家）. Listing cat: 工作與財務管理.

## GA4 organic (property `298556736`)

Site Insights totals — **7d:** 312 clicks / 35,082 imps; **28d:** 1,392 / 169,213.

Prior Sunday window (ending 2026-11-07, continuity only): 7d 267 / 34,679; 28d 1,341 / 166,148.

### Top Insights landings by organic clicks (7d)

Date range: **2026-11-08 → 2026-11-14**.

| Landing | Clicks | Impressions |
|---------|-------:|------------:|
| `/tc/insights/Inner-child` | 20 | 623 |
| `/tc/insights/5-Love-Languages` | 19 | 2,743 |
| `/tc/insights/highly-sensitive-people` | 14 | 2,767 |
| `/tc/insights/AutomaticThoughts` | 13 | 289 |
| `/tc/insights/amygdala-hijack` | 11 | 1,094 |
| `/tc/insights/caregivers` | 11 | 183 |
| `/tc/insights/investment-2024` | 10 | 471 |
| `/tc/insights/should-i-resign-2024` | 9 | 200 |
| `/tc/insights/Extrovert-Introvert` | 6 | 1,990 |
| `/tc/insights/once-in-a-lifetime` | 6 | 1,232 |

### Top Insights landings by organic clicks (28d)

Date range: **2026-10-18 → 2026-11-14**. Weight = clicks + 0.002×imps + 50×ctr.

| Landing | Clicks | Impressions | weight_28d |
|---------|-------:|------------:|----------:|
| `/tc/insights/5-Love-Languages` | 94 | 12,929 | 120.222 |
| `/tc/insights/Inner-child` | 82 | 3,316 | 89.868 |
| `/tc/insights/highly-sensitive-people` | 74 | 16,590 | 107.403 |
| `/tc/insights/caregivers` | 50 | 889 | 54.590 |
| `/tc/insights/AutomaticThoughts` | 48 | 1,337 | 52.469 |
| `/tc/insights/amygdala-hijack` | 45 | 5,264 | 55.955 |
| `/tc/insights/family-therapy-concepts` | 36 | 1,130 | 39.853 |
| `/tc/insights/should-i-resign-2024` | 34 | 1,017 | 37.706 |
| `/tc/insights/procrastination-2024` | 32 | 2,800 | 38.171 |
| `/tc/insights/hong-kong-art-therapy-stress-relief-refresh` | 30 | 822 | 33.469 |

### Notes for writers / SEO desk

- Site organic clicks rose vs last Sunday (7d 267→312; 28d 1,341→1,392); impressions also up slightly (7d 34,679→35,082; 28d 166,148→169,213). Traffic movement alone is not a gold-card swap.
- 7d/28d leaders remain evergreen construct pages（五愛、內在小孩、HSP、照顧者、Automatic Thoughts、杏仁核）.
- New URL `working-carers-respite-guide-EAP`: **0** clicks / **3** imps (7d and 28d).
- `sychology-effective-apology-relationship-repair-refresh-hk`: 0 clicks / 5 imps (7d and 28d).
- `scam-victim-psychology-cognitive-dissonance-refresh-hk`: **no organic rows** in either window.
- `off-duty-work-messages-3-tips-EAP`: 0 clicks / 1 imp (7d); 0 clicks / 7 imps (28d).
- Gold Layer A/B paths **unchanged**. Layer A top-3 標準 remain 五愛 / HSP / 內在小孩 (HSP still ahead of 內在小孩 by 28d weight, same order nuance as last week). Plus coverage slot remains `deal-with-toxic-coworkers-3-ways` (6/212, w=7.839). 日子 coverage slot remains `midlife-crisis-fathers-stress-guide` (6/484, w=7.588); `hong-kong-mean-culture-australia-dairy-company` is still heavier (16/1,978, w=20.360) but this gap is pre-existing, not a new coverage change.
- Avg position not in this extract; leave corpus `avg_pos_*` blank.

## New Insights (this distill)

- 2026-11-10: `/tc/insights/working-carers-respite-guide-EAP` — 【Re:Fresh Plus專屬內容】深度專欄 | 下班後，另一份工作才開始：給在職照顧者的喘息指南 (clicks_28d=0, clicks_7d=0, impressions=3)

## Weight leaders (28d organic clicks) — skill focus

Evergreen construct pages still lead: 五愛的語言、高敏感、內在小孩、照顧者、Automatic Thoughts、杏仁核劫持、家庭治療、辭職決策、拖延自測等。

## Maintenance

- Incrementally update corpus-index when listing gains URLs
- Refresh weights weekly from GA4 organicGoogleSearch* (28d primary, 7d contrast)
- Re-pick gold-cards only when rank/type mix shifts materially
