# Weekly digest — 2026-10-11 → 2026-10-17 (HKT)

Window: 7 days ending **2026-10-17**. Distill only; no full-text archive in skill.

## Method

Distillation corpus = **all listed Insights** + **GA4** organic weights (not last-7-days-only).
See [corpus-index.md](corpus-index.md) + [corpus-index.csv](corpus-index.csv).

Data source: GA4 MCP property `298556736`, metrics `organicGoogleSearchClicks` / `organicGoogleSearchImpressions`, landing contains `/insights`.
28d window: **2026-09-20 → 2026-10-17**.

## New / notable Insights

| Date (list) | Slug | Type | One-line pattern |
|-------------|------|------|------------------|
| 2026-10-15 | `roommate-marriage-emotional-disconnection-refresh` | 標準・關係／親密／溝通技巧 | 室友式婚姻 construct → 疏離≠平淡 → 專屬時光＋好奇心提問 → FAQ |

## GA4 organic (property `298556736`)

Site Insights totals — **7d:** 298 clicks / 33,093 imps; **28d:** 1,367 / 177,491.

### Top Insights landings by organic clicks (7d)

Date range: **2026-10-11 → 2026-10-17**.

| Landing | Clicks | Impressions | CTR |
|---------|-------:|------------:|----:|
| `/tc/insights/Inner-child` | 25 | 675 | 3.70% |
| `/tc/insights/5-Love-Languages` | 22 | 2602 | 0.85% |
| `/tc/insights/AutomaticThoughts` | 17 | 288 | 5.90% |
| `/tc/insights/highly-sensitive-people` | 12 | 2723 | 0.44% |
| `/tc/insights/procrastination-2024` | 12 | 577 | 2.08% |
| `/tc/insights/should-i-resign-2024` | 11 | 201 | 5.47% |
| `/tc/insights/family-therapy-concepts` | 11 | 330 | 3.33% |
| `/tc/insights/hong-kong-art-therapy-stress-relief-refresh` | 8 | 206 | 3.88% |
| `/tc/insights/amygdala-hijack` | 7 | 1129 | 0.62% |
| `/tc/insights/caregivers` | 6 | 188 | 3.19% |

### Top Insights landings by organic clicks (28d)

Date range: **2026-09-20 → 2026-10-17**.

| Landing | Clicks | Impressions | CTR |
|---------|-------:|------------:|----:|
| `/tc/insights/5-Love-Languages` | 122 | 16137 | 0.76% |
| `/tc/insights/Inner-child` | 103 | 5943 | 1.73% |
| `/tc/insights/highly-sensitive-people` | 78 | 14615 | 0.53% |
| `/tc/insights/AutomaticThoughts` | 70 | 1248 | 5.61% |
| `/tc/insights/should-i-resign-2024` | 41 | 1190 | 3.45% |
| `/tc/insights/caregivers` | 36 | 923 | 3.90% |
| `/tc/insights/amygdala-hijack` | 33 | 5838 | 0.57% |
| `/tc/insights/hong-kong-art-therapy-stress-relief-refresh` | 34 | 949 | 3.58% |
| `/tc/insights/family-therapy-concepts` | 32 | 1481 | 2.16% |
| `/tc/insights/positive_quotes` | 29 | 4291 | 0.68% |

### Notes for writers / SEO desk

- Evergreen construct pages (五愛、內在小孩、HSP、Automatic Thoughts) still dominate 28d clicks.
- New URL `roommate-marriage-emotional-disconnection-refresh` has **0** GA4 organic clicks/imps so far (too fresh); track next week via clicks_7d.
- Gold Layer A/B paths **unchanged** (no clear path swap; Plus volumes still tiny / jittery).
- Avg position not in GA4 organic field set this week; corpus `avg_pos_*` columns left blank.

## New Insights (this distill)

- 2026-10-15: `/tc/insights/roommate-marriage-emotional-disconnection-refresh` — 夫妻愈來愈像室友？婚姻最傷人的不是爭吵，而是連架也懶得吵 (clicks_28d=0, clicks_7d=0)

## Weight leaders (28d organic clicks) — skill focus

Evergreen construct pages still dominate: 五愛的語言、內在小孩、HSP、Automatic Thoughts、杏仁核劫持、照顧者、辭職決策等。

## Maintenance

- Incrementally update corpus-index when listing gains URLs
- Refresh weights weekly from GA4 organicGoogleSearch* (28d primary, 7d contrast); GSC fallback if GA4 unavailable
- Re-pick gold-cards only when rank/type mix shifts materially
