---
name: ot-case-recording
description: Rewrite or polish a BOKSS/ICCMW occupational therapy progress note (four fields: Descriptions/Intervention, Progress Summary/Evaluation, Areas for Improvement, Follow Up Plan). Use when the user pastes an OT note, home-visit SOAP, or ADL/IADL/vocational draft. Not a counselling process note.
---

# OT progress note — Occupational Therapy (ICCMW)

Editorial assistant for occupational therapy progress notes. Humans remain clinically responsible. Output is a **draft until the worker reviews it**.

Identifiable text: run `pdpo-deidentify` first. Shared guardrails: `clinical-safety-copilot`.

The note should let another worker understand: what OT did and observed, how the session went, what still needs work, and what happens next — occupation-based, not a transcript.

Load when needed:
- Assessment score bands (only if draft has scores) → [references/assessment-cutoffs.md](references/assessment-cutoffs.md)
- SOAP-style phrase stems (style only; never invent facts) → [references/soap-phrase-bank.md](references/soap-phrase-bank.md)

## Input → output (recipe)

**Read** the four headings (messy OK), or one unsorted draft → sort into the four fields before polishing.

**Write** only these headings, in order:

```
## Descriptions / Intervention
## Progress Summary / Evaluation
## Areas for Improvement
## Follow Up Plan
```

Do **not** replace these four headings with DARP letters.

SOAP letter headings (**S** / **O** / **A** / **P**) **may** be used as **sub-labels inside** the four headings when sorting Clt report vs observation vs interpretation vs plan. Keep the four headings.

If the user names a diagnosis or counselling approach, use that vocabulary only when the draft supports it.

## Rules (non-negotiable)

1. Preserve facts from input only — never invent symptoms, risk, diagnoses, quotes, interventions, FIM/COPM/ROM/pain/**assist levels**, scores, history, or “WNL” for unassessed domains
2. Do not add or remove risk content relative to the draft
3. Keep draft language (EN or 中文) unless translation requested
4. Missing required info → `[Insufficient information in draft: …]`
5. Progress Summary / Evaluation synthesises; does not repeat Descriptions
6. If clinical meaning would change (“more severe/positive”), refuse; note under Gaps
7. Keep notes **occupation-based** (person–environment–occupation); home visits include environment when draft has it
8. Separate **Clt report** vs **OT observation** when both appear; short bullets; quote sparingly and only if in draft
9. Use **past tense** when reporting visits, interviews, and what was done/observed
10. If diagnosis and/or approach are known: think with `apply-diagnosis-approach` (OT brain — occupation, not a psychiatric formulation). Name techniques only when used in activity; never invent worksheets, scores, or homework results
11. If draft includes assessment results (HKBC / AMT / MoCA-HK / Lawton IADL / MBI / CWPP), put score + outcome in **Progress Summary / Evaluation**; interpret with [assessment-cutoffs.md](references/assessment-cutoffs.md) only when required demographics are present — never invent scores or cut-off conclusions

## Four fields (skip empty domains; never invent)

### Descriptions / Intervention
1. Setting (home / centre / community) if stated  
2. Clt/caregiver report that frames the session (**S**-style)  
3. Interventions OT delivered (activity + purpose when draft supports)  
4. Observed performance; environment on home visits (**O**-style; concrete time, prompts, peers, tasks when in draft)  
5. MH/cognitive sessions: categorical findings with concrete detail (Memory, Problem-solving, Safety awareness, Medication management, Daily routines, Attention)

Point form OK. Phrase stems: [soap-phrase-bank.md](references/soap-phrase-bank.md).

### Progress Summary / Evaluation
- Clt response (accepted / hesitation / tired but willing / left early — as draft states)
- Progress vs care-plan / session aims if known
- Assessment results / outcome when present in draft
- Occupation-linked interpretation (**A**-style: progress / functional impact / recovery focus) — no invented scores

### Areas for Improvement
Occupation deficit ↔ contributing factor (person / env / occupation) **only if in draft**. Prefer statements like: “Unable to sustain meal prep safely due to impaired sequencing (Clt observation).”

### Follow Up Plan
Next occupation-focused step; equipment; env mod; education; handoff/liaison; next visit (date/time only if known). Prefer concrete **P**-style stems (Continue / Introduce / Liaise / Refer / Reassess…) only when draft supports the action. Referral targets (SET / IVRSC / CP / HWH / etc.) only if in draft.

## Occupation areas (use when present in draft)

| Area | Examples |
|------|----------|
| ADLs | Bathing, dressing, feeding, functional mobility, hygiene, toileting; **daily routine / structure** |
| IADLs | Finances, home management, meal prep, shopping, safety, health/med management; **transportation**; **community resources** |
| Rest & sleep / Health management | Sleep preparation / participation; **insight**; **treatment compliance**; **exercise habit** |
| Education / Work | Learning, job seeking/performance, volunteer; **work adjustment**; **Vocational Services** |
| Play / Leisure / Social | Exploration, participation, community/family/peers; **social engagement**; **communication** |

Goals: if draft has them, keep measurable and occupation-linked (COAST elements only if present). Avoid “participate in OT treatment” as a goal.

## Abbreviations

| Short | Full | Short | Full |
|-------|------|-------|------|
| Clt | Client | Wrk | Worker |
| MS | Mental state | Tx | Treatment |
| Dx | Diagnosis | mgt | Management |
| Ax | Assessment | Trg | Training |

## Output package

After the four fields, always emit:

```
## Gaps flagged
## Questions to resolve
```

Write `None` under each if empty. If risk is already in the draft, also emit `## Risk-management flags`.

Footer (exact):

```
---
Status: DRAFT — worker review required before save.
Not a diagnosis or final risk decision.
```

## Quality bar

- [ ] Another worker can act on Follow Up Plan tomorrow
- [ ] No new people, agencies, diagnoses, risks, assist levels, or scores
- [ ] Areas for Improvement are occupation-based
- [ ] Four headings present (SOAP letters only as optional sub-labels)
- [ ] Past tense for visit/interview report
- [ ] DRAFT footer present

## Common mistakes

- Replacing the four headings with SOAP-only output — keep the four headings; SOAP letters are optional sub-labels
- Guessing min/mod/max A or “S cue” / inventing Ax scores to fill empty fields
- Dumping Evaluation as a second Descriptions
- Ignoring home environment when draft has it
- Replacing OT note with generic counselling narrative
- Present tense for completed visits (“Clt walks to kitchen…” → “Clt walked…”)
- Skipping Gaps/Questions, or renaming them
- Paraphrasing the DRAFT footer

### Micro-example (synthetic)

**Draft:** “Home visit. Clt afraid fall when cook. Clutter near stove. Practised safe reach. Tired after 10 min. Clear floor; next Thu meal prep with daughter.”

**Descriptions / Intervention:** Home visit. Clt reported fear of falling when cooking. Observed clutter near stove. Practised safe reach to cupboard.  
**Progress Summary / Evaluation:** Clt was tired after ~10 min but remained willing to practise; kitchen safety work started.  
**Areas for Improvement:** Meal prep safety limited by fall concern and floor clutter near stove.  
**Follow Up Plan:** Clear floor; next visit Thu — meal prep with daughter present.
