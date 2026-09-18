---
name: draft-5p
description: Draft a 5P formulation (Presenting, Predisposing, Precipitating, Perpetuating, Protective) from the source notes the user provides. Use when staff ask for case conceptualization or 5P. Never invent trauma, diagnosis, or risk to fill empty Ps. Prefer domain-tagged bullets and Questions to resolve.
---

# Draft 5P formulation

Output is always a **DRAFT** for human review. Formulation ≠ diagnosis.

See `clinical-safety-copilot`.

## Inputs
- source notes the user provided (**required**)
- optional prior fact extract — hints only (schema in `case-qa`)
- optional role lens (social worker / OT / CP); optional named approach

## Non-negotiable
1. Do **not** invent provisional DSM/ICD labels.  
2. Every bullet traceable to the source notes (or marked insufficient).  
3. Missing P → `[Insufficient information: <P>]` **and** Questions to resolve.  
4. Never invent trauma, ACE, scores, or risk to “complete” a nice 5P.  
5. Preserve risk already in the source notes; surface Risk-management flags; no invented crisis pathways.  

## Three products (do not conflate)

| Product | Question | AI may… |
|---------|----------|---------|
| Diagnosis | Already in the clinical file? | Copy if documented; else leave out |
| **5P formulation** | How do we understand difficulties + strengths now? | Draft from the source notes only |
| Care plan | What will we do, by when? | Hand off to `draft-care-plan` |

## The five Ps

| P | 中文參考 | Write |
|---|---------|-------|
| **Presenting** | 呈現問題 | Why contact now; 1–3 problems + impact; Clt goal if stated |
| **Predisposing** | 易感／背景因素 | Long-standing vulnerabilities **only if documented** |
| **Precipitating** | 促發因素 | Recent triggers / onset of this episode |
| **Perpetuating** | 維持因素 | What keeps it going now |
| **Protective** | 保護／優勢因素 | Concrete strengths, supports, skills, values |

Tag bullets when clear: `(Bio)` `(Psych)` `(Social)` `(Cultural)` `(Env/OT)` `(System)`.  
Source labels: `(Clt report)` `(Wher observation)` `(file)` `(family report)` `(clinic letter)`.

## Procedure
1. Optional: `case-qa` fact extract first on long records.  
2. Fill each P with 1–6 specific bullets.  
3. **Formulation narrative** (4–8 sentences).  
4. One **change mechanism** only if evidenced.  
5. **Questions to resolve** for every unknown.  
6. If plan requested → `draft-care-plan`.  

## Output package

```markdown
# 5P Formulation — DRAFT
**Role lens:** social worker | OT | CP (only if the user named one)
**Sources used:** [dated notes the user provided]
**Status:** DRAFT — worker review required. Not a diagnosis.

## Presenting
## Predisposing
## Precipitating
## Perpetuating
## Protective
## Formulation narrative
## Change mechanism (if evidenced)
## Diagnosis (only if already in record)
## Risk-management flags
## Questions to resolve

---
Status: DRAFT — worker review required before save.
```

## Worked example (synthetic — anxiety / avoidance)
- **Presenting:** Panic on MTR; avoiding trains; wants to travel to work again. `(Clt report)`
- **Predisposing:** `[Insufficient information: Predisposing]`
- **Precipitating:** Panic episode on train ~1 month ago. `(Clt report)`
- **Perpetuating:** Avoidance of MTR; night-time worry; taxi as safety behaviour.
- **Protective:** Motivated for practice; engaged in session; no SI stated in the source notes.
- **Questions to resolve:** Prior panic history; sleep; medication.

## References
Bundled formulation cards in `references/` (5P, 4P vs 5P, formulation from notes). Optional: `apply-diagnosis-approach` if diagnosis/approach are known.

## Related
`draft-care-plan`, `case-qa`, `clinical-safety-copilot`
