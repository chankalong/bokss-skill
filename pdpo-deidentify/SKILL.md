---
name: pdpo-deidentify
description: Redact Hong Kong personal data in case notes, teaching examples, or drafts before a cloud model sees them. Use when the user asks to de-identify, anonymise, 去識別, redact PII/PDPO identifiers, or prepare BOKSS/ICCMW text for AI. Preserve clinical meaning; replace names and IDs with labelled tokens. Not a legal determination of PDPO compliance.
---

# PDPO de-identify (BOKSS)

Technical aid for Hong Kong NGO staff. **Not legal advice.** Agency DPO / clinical lead rules win. Do not claim “PDPO compliant”.

If the text is a Re:Fresh article, use `refresh-insights-writing` instead. If the user wants clinical rewrite of a live note, run this **first**, then `clinical-safety-copilot`.

## Do

1. Replace direct identifiers with **stable** tokens (same person → same token):
   - `[CLIENT]`, `[CLIENT_2]`
   - `[FAMILY_MO]`, `[FAMILY_FA]`, `[FAMILY_SISTER]`, `[PARTNER]`, `[CARER]`
   - `[WORKER]`, `[OT]`, `[CP]`, `[NURSE]`, `[PEER]`
   - `[PHONE]`, `[HKID]`, `[ADDRESS]`, `[EMAIL]`, `[CASE_NO]`
   - `[SCHOOL]`, `[EMPLOYER]`, `[ESTATE]`, `[CLINIC]` (keep generic “HA clinic” / “地區醫院” if already non-identifying)
   - `[WHATSAPP]`, `[WECHAT]`, `[CSSA_NO]`
2. Keep symptoms, interventions, and **risk wording as written**. Redaction is not sanitising distress.
3. Prefer decade age (“30s”) when exact age/DOB is unused and identifying.
4. Keep relationship labels (mother ≠ father). Do not invent a new family map.
5. Return **Redacted text**, **Token map**, **Residual risk**.

## Do not

1. Put the token map into git, Slack, or another chat
2. Strip SI / violence / child-protection content while “cleaning”
3. Expand method detail of self-harm beyond the source
4. Invent fake HK names as replacements (tokens only — fake names re-identify poorly and look like real clients)
5. Send original text to web search or unapproved tools

## Hong Kong leak vectors (scan every draft)

| Class | Typical form | Token |
| --- | --- | --- |
| Name | Chinese + English, nickname, 花名 | `[CLIENT]` / role token |
| HKID | letter + 6 digits + check | `[HKID]` |
| Phone | 8-digit (2/3/5/6/9…), +852 | `[PHONE]` |
| Address | estate + block + flat; street + number | `[ADDRESS]` / `[ESTATE]` |
| School / work | named school, employer, shop | `[SCHOOL]` / `[EMPLOYER]` |
| File nos | case-file / SWD / HA / CSSA numbers | `[CASE_NO]` |
| Clinic | named OPD, private doctor | `[CLINIC]` |
| Online | email, WhatsApp, IG handle | `[EMAIL]` / `[WHATSAPP]` |

Quasi-identifiers: rare diagnosis + named district + exact age + school year. Flag these even after tokenising.

Full scan list: [references/hk-identifiers.md](references/hk-identifiers.md).

## Output

```markdown
## Redacted text
…

## Token map (keep offline)
| Token | Original |
|-------|----------|
| [CLIENT] | … |

## Residual risk note
Quasi-identifiers still present: …
```

If the source is empty of identifiers, say so and return the text unchanged — do not invent tokens.

## Synthetic example

**Source:** 「陳大文（HKID A123456(7)）住在葵芳邨，電話 9123 4567。社工李小姐今午外展。陳表示一週來不想出門，否認自殺念頭。」

**Redacted:** 「[CLIENT] 住在 [ESTATE]，電話 [PHONE]。[WORKER] 今午外展。[CLIENT] 表示一週來不想出門，否認自殺念頭。」
