# Document depressive presentation (ICCMW)

**Staff documentation / Case Q&A aid only.**  
Vocabulary: [depression](references/depression.md).  
Procedure here = **how to write and answer** without inventing diagnosis or care steps.

## When to use
- Draft or source notes mention low mood, anhedonia, depression, MDD, or clear Criterion A–style domains  
- the draft shows depression / low mood  
- Rewrite of CW / OT / CP notes with depressive content  
- Case Q&A: “what domains matter?”, “grief vs depression?”, “what is my next step?” when depression is the theme  

## Hard rules
1. Do **not** write “Dx: MDD / major depression” unless the **file/source notes already** use that label  
2. Do **not** invent symptom counts, duration, PHQ-9/BDI scores, or specifier labels  
3. Do **not** pad the note to five domains — write **only** domains assessed or evidenced  
4. Do **not** equate a few days of low mood with a full major depressive episode picture  
5. Prefer **Clt’s words** for mood and anhedonia; keep functional anchors (attendance, self-care, sleep, withdrawal)  
6. Do **not** collapse bipolar, medical/substance, grief, or psychotic features into “just depression”  
7. Name interventions (activation, CBT, CBT-I, meds liaison, safety plan) **only if done / in draft**  
8. Risk content (SI, plan, attempt) always wins over tidy formulation — do not invent or soft-delete risk  
9. For Case Q&A “next step”: answer from **source notes first**; label guideline wording as **not about this client**  
10. Human remains accountable — output is DRAFT / assistive only  

## Fidelity mini-check (before output)
- [ ] No invented Dx, scores, or duration  
- [ ] Every depressive domain named maps to draft/excerpt evidence  
- [ ] Bipolar / grief / medical / substance distinctions preserved when present  
- [ ] Interventions named only if evidenced  
- [ ] Risk handled carefully (or explicitly “not elicited / not in records”)  

## What to capture when present
- Gate features: depressed mood and/or loss of interest/pleasure (Clt words)  
- Other domains assessed: appetite/weight, sleep, psychomotor, energy, guilt/worthlessness, concentration, death/SI  
- Duration / change / functional impact **only if evidenced**  
- Differential flags: elevated mood or decreased need for sleep; substance/medical link; grief; psychosis  
- File-only labels: severity/specifiers if already written  
- Work done: activation, CBT elements, sleep work, meds liaison, safety planning — as drafted  

## Output snippet (rewrite)

```markdown
### Depressive presentation (from draft only)
- Domains evidenced: [list only what draft supports]
- Function: [attendance / self-care / sleep / social — if stated]
- Risk: [as drafted, or “no SI elicited today” if stated]
- Intervention (if any): [name only what was done]
- [Insufficient information: …] (if staff implied MDD but draft lacks domains)
```

## Case Q&A — “what is my next step?”
Use assertion classes from `case-qa`:

1. **supported** — cite dated source notes for known goals, plan, risk, prior activation/CBT  
2. **not_in_records** — missing care plan, missing SI screen, missing agreed goals, etc.  
3. **guideline_only** — general community practice (e.g. functional anchors; agreed micro-step; do not stamp Dx) labeled as *not about this client*  
4. Never invent the next intervention from “Clt has depression” alone  

## Examples (synthetic)

### A — draft supports domain documentation
**Draft:** “Clt low mood ~3 weeks; no interest in usual activities; sleep onset delay; fatigue; missed two work days; denies SI today. Agreed short daily walk.”

**Output:**
```markdown
### Depressive presentation (from draft only)
- Domains evidenced: low mood (~3 weeks), anhedonia, sleep onset delay, fatigue
- Function: missed two work days
- Risk: denies SI today
- Intervention: behavioural activation — agreed short daily walk
```

### B — vague draft — do not invent MDD
**Draft:** “Clt seemed down today.”

**Output:**
```markdown
### Depressive presentation (from draft only)
- Domains evidenced: low mood implied (“seemed down”) — insufficient detail for duration, anhedonia, or other Criterion A domains
- [Insufficient information: MDD / full depressive episode wording]
```

### C — Q&A next step (shape)
**Question:** “Clt has depression, withdrawn and sleeping poorly — what is my next step?”  
**Excerpts:** one note with withdrawal + hypersomnia; no care plan; no SI question documented.

```markdown
## Answer
From provided records, withdrawal and sleeping poorly are documented; no agreed care-plan step and no SI enquiry appear in the source notes. Next documentation step is to clarify risk and agree one concrete functional step with Clt — only after clinical judgement / agency process.

## Evidence
- [date]: withdrawal; sleeping poorly (supported)

## Not in provided records
- File diagnosis of MDD
- Care plan / agreed activation task
- SI enquiry result

## Guideline context (optional)
Guideline wording (not about this client): community notes often use functional anchors and document only assessed depressive domains; do not invent Dx or interventions.

## Caution
Human remains accountable. DRAFT for clinical use.
```

## Anti-patterns
- Stamping “Dx: MDD” from staff chat or vague “felt down”  
- Padding domains to look like a full Criterion A count  
- Upgrading “talked about mood” into CBT restructuring or activation not done  
- Ignoring bipolar caution signs (elevated mood, decreased need for sleep)  
- Answering next-step Q&A from the depression card alone without source notes  

## References (bundled)
- [depression.md](depression.md)
- [mood-bipolar-depression.md](mood-bipolar-depression.md)
- [suicide-self-harm-risk.md](suicide-self-harm-risk.md)
- Technique naming: [therapy-techniques.md](therapy-techniques.md)
