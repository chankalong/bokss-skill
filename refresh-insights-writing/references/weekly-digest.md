# Weekly digest — 2026-10-04 → 2026-10-10 (HKT)

Window: 7 days ending **2026-10-10**. Distill only; no full-text archive in skill.

## Method

Distillation corpus = **all listed Insights** + **GSC** organic weights (not last-7-days-only).
See [corpus-index.md](corpus-index.md) + [corpus-index.csv](corpus-index.csv).

Data source: Google Search Console API (`webmasters.readonly`) for `https://refresh.bokss.org.hk/`, dimension `page` contains `/insights`.
Quota project `refresh-bokss`. GA4 not used this week (GSC ok).

## New / notable Insights

| Date (list) | Slug | Type | One-line pattern |
|-------------|------|------|------------------|
| 2026-10-07 | `child-abuse-tuenmun-parenting-refresh-hk` | 標準・家庭／照顧者 | 屯門虐兒時事 → 看見異樣 → 引導受困孩子安全說出心聲 |
| 2026-10-05 | `recognisably-You-Uniqueness-psychology-refresh` | 標準・個人成長 | 獨特性消失 → 社會進步 vs 不敢做自己 → 自我接納 |

## GSC organic (site `https://refresh.bokss.org.hk/`)

Site Insights totals — **7d:** 170 clicks / 19,903 imps; **28d:** 1,293 / 204,383.

### Top Insights landings by organic clicks (7d)

Date range: **2026-10-04 → 2026-10-10**.

| Landing | Clicks | Impressions | Avg pos | CTR |
|---------|-------:|------------:|--------:|----:|
| `/tc/insights/Inner-child` | 14 | 367 | 5.84 | 3.81% |
| `/tc/insights/5-Love-Languages` | 12 | 1531 | 7.16 | 0.78% |
| `/tc/insights/highly-sensitive-people` | 9 | 1906 | 5.48 | 0.47% |
| `/tc/insights/AutomaticThoughts` | 7 | 179 | 5.45 | 3.91% |
| `/tc/insights/should-i-resign-2024` | 7 | 143 | 9.01 | 4.90% |
| `/tc/insights/procrastination-2024` | 6 | 275 | 7.81 | 2.18% |
| `/tc/insights/amygdala-hijack` | 5 | 871 | 10.22 | 0.57% |
| `/tc/insights/positive_quotes` | 5 | 467 | 8.01 | 1.07% |
| `/tc/insights/primary-student-academic-stress-tips` | 5 | 24 | 16.21 | 20.83% |
| `/tc/insights/caregivers` | 4 | 127 | 8.80 | 3.15% |

### Top Insights landings by organic clicks (28d)

Date range: **2026-09-13 → 2026-10-10**.

| Landing | Clicks | Impressions | Avg pos | CTR |
|---------|-------:|------------:|--------:|----:|
| `/tc/insights/5-Love-Languages` | 137 | 26348 | 6.81 | 0.52% |
| `/tc/insights/Inner-child` | 95 | 7819 | 6.09 | 1.21% |
| `/tc/insights/highly-sensitive-people` | 83 | 13912 | 5.57 | 0.60% |
| `/tc/insights/AutomaticThoughts` | 66 | 1167 | 6.91 | 5.66% |
| `/tc/insights/amygdala-hijack` | 32 | 5773 | 10.39 | 0.55% |
| `/tc/insights/caregivers` | 32 | 888 | 7.69 | 3.60% |
| `/tc/insights/hong-kong-art-therapy-stress-relief-refresh` | 31 | 876 | 8.88 | 3.54% |
| `/tc/insights/positive_quotes` | 28 | 5162 | 7.89 | 0.54% |
| `/tc/insights/should-i-resign-2024` | 28 | 1165 | 9.34 | 2.40% |
| `/tc/insights/procrastination-2024` | 23 | 2380 | 8.51 | 0.97% |

### Notes for writers / SEO desk

- Evergreen construct pages (五愛、內在小孩、HSP、Automatic Thoughts) still dominate 28d clicks.
- Two new URLs this week have **0** GSC clicks/imps so far (too fresh); track next week via clicks_7d.
- Gold Layer A/B paths **unchanged** (no clear path swap; Plus volumes still tiny / jittery).
- Weight-only numeric drift on same gold paths is not a separate PR trigger beyond the new-URL corpus update.

## New Insights (this distill)

- 2026-10-07: `/tc/insights/child-abuse-tuenmun-parenting-refresh-hk` — 【屯門虐兒疑雲】從看見異樣到走近心房：如何引導受困孩子安全說出心聲？ (clicks_28d=0, clicks_7d=0)
- 2026-10-05: `/tc/insights/recognisably-You-Uniqueness-psychology-refresh` — 消失的「獨特性」：為何社會愈進步，我們愈不敢「做自己」？ (clicks_28d=0, clicks_7d=0)

## Weight leaders (28d organic clicks) — skill focus

Evergreen construct pages still dominate: 五愛的語言、內在小孩、HSP、Automatic Thoughts、杏仁核劫持、照顧者、辭職決策等。

## Maintenance

- Incrementally update corpus-index when listing gains URLs
- Refresh weights weekly from GSC (28d primary, 7d contrast); GA4 fallback only if GSC fails
- Re-pick gold-cards only when rank/type mix shifts materially
