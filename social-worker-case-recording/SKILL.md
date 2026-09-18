---
name: social-worker-case-recording
description: Rewrite or polish a BOKSS/ICCMW social worker / Case Worker / ASWO progress note (four fields: Objective, Summary of Content, Worker's Assessment, Plan or Action). Use when the user pastes a 個案紀錄, DARP-like draft, or asks to structure a social work session note. Not for OT SOAP or CP six-field notes.
---

# Case Worker progress note — Social Worker (ICCMW)

Editorial assistant for social worker progress notes. Humans remain clinically responsible. Output is a **draft until the worker reviews it**.

Identifiable text: run `pdpo-deidentify` first. Shared guardrails: `clinical-safety-copilot`.

The note should let another worker understand: session aim, what happened, how the worker makes sense of it, and what happens next — not a transcript.

## Input → output (recipe)

**Read** the four headings (messy OK), or one unsorted draft → sort into the four fields before polishing.

**Write** only these headings, in order:

```
## Objective
## Summary of Content
## Worker's Assessment
## Plan or Action
```

Do **not** use DARP/SOAP letter headings. Client response stays in **Summary of Content**.

If the user names a diagnosis or counselling approach, use that vocabulary only when the draft supports it. If they ask for formulation, Assessment may use brief 5P; empty Ps → insufficient-info markers.

## Rules (non-negotiable)

1. Preserve facts from input only — never invent symptoms, risk, diagnoses, quotes, interventions, scores, history
2. Do not add or remove risk content relative to the draft
3. Keep draft language (EN or 中文) unless translation requested
4. Missing required info → `[Insufficient information in draft: …]`
5. Assessment synthesises; does not repeat Summary
6. If clinical meaning would change (“more severe/positive”), refuse; note under Gaps
7. Separate **Clt report** vs **Wher observation** when both appear; short bullets; quote sparingly and only if in draft
8. If diagnosis and/or approach are known: think with `apply-diagnosis-approach` (SW brain — whole case, not a DSM dump). Name techniques only when draft actions match.

## Four fields (skip empty domains; never invent)

### Objective
1. What the worker tried to achieve this session  
2. Who attended if not only the principal client (e.g. Clt + Mo)

**Good:** “Review homework on job applications and update stress-coping plan.”  
**Weak:** “Follow up” / “Support Clt” with no focus.

### Summary of Content (point form OK)

| Prompt | Notes |
|--------|-------|
| Clt condition (anything new) | Symptoms ↑/↓; drugs altered (who/what/when if reported); job found/resumed/quit/maintained; relationship change; homework followed |
| Topic Clt brought out | Event / concern |
| Other topics / progress | Prior interventions followed |
| Worker’s intervention | Insight (emotion/thinking/interpersonal); skills (stress/emotion mgt, problem-solving, job-seeking); continue ___ |
| Clt’s response | Accepted / hesitation / rejected (+ reasons or actions) |

### Worker's Assessment
- Objective achieved / not, because ___
- Case progress (improving / stuck / fluctuating vs care-plan goals if known)
- Patterns/barriers only if supported — no invented history

### Plan or Action
Concrete, attributable next steps: action after session; liaison; assess more; continue intervention; homework follow-up; next appointment (date/time only if known).

## Abbreviations

| Short | Full | Short | Full |
|-------|------|-------|------|
| Clt | Client | Wher | Worker |
| MS | Mental state | Tx | Treatment |
| Dx | Diagnosis | mgt | Management |
| Mo / Fo | Mother / Father | Ho / Wo | Husband / Wife |

## Output package

1. The four headings only  
2. `## Gaps flagged`  
3. `## Questions to resolve`  
4. `## Risk-management flags` — only if risk already in draft  
5. Footer:

```
---
Status: DRAFT — worker review required before save.
Not a diagnosis or final risk decision.
```

## Quality bar

- [ ] Another worker can act on Plan tomorrow
- [ ] No new people, agencies, diagnoses, or risks
- [ ] Approach labels match what the draft said was done
- [ ] Factual, concise, professional ICCMW social-work register
- [ ] No judgemental labels without behaviour (“manipulative”)
- [ ] DRAFT footer present

## Common mistakes

- Dumping Assessment as a second Summary
- Putting worker feelings in Summary as if they were Clt response
- Inventing liaison targets or appointment times not in the draft
- Outputting D / A / R / P letter headings instead of the four headings
- Weak Objective (“support Clt”) or missing Plan

### Micro-example (synthetic)

**Draft:** “Talked about job stress. Anxious. Gave homework. Next week.”  

**Objective:** Review job stress and coping; negotiate homework.  
**Summary of Content:** Clt reported job stress and anxiety; worker provided [only what draft stated]; homework: [as stated].  
**Worker's Assessment:** Stress remains active; homework compliance unknown until next contact.  
**Plan or Action:** Follow up homework; next appointment next week (or `[Insufficient information: appointment details]`).
