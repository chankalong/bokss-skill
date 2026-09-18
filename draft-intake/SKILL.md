---
name: draft-intake
description: Draft a BOKSS/ICCMW intake or first-contact note from the source notes the user provides. Use when staff ask for help writing an intake or opening summary. Never invent history, screens, or risk. Output is DRAFT for human edit.
---

# Draft intake

**Care stage:** Exploration ([care-stages](references/care-stages.md)).  

Help staff draft an **intake / initial interview** summary from what is already in the record.  
Grounded in agency intake coverage (distilled). Do not paste copyrighted interview question banks into the note.

Read [intake-process](references/intake-process.md) and [care-stages](references/care-stages.md) when helpful.

## Inputs
- source notes the user provided (**required**)
- optional prior fact extract — hints only (schema in `case-qa`)
- optional staff instruction (e.g. “focus on risk screens done”)

## Aims
1. Chief complaint + why now  
2. Enough HPI / background for next-step decision  
3. Risk **as screened in the source notes**  
4. Engagement, confidentiality, plan  

## Draft into these blocks (only if info exists)

### A. Administrative / context
Date, worker, setting; referral; who attended; interpreter.

### B. Presenting / chief complaint + themes
Clt words; onset; why now; hopes from service. Themes heard **without inventing**.

### C. HPI & background
Symptom dimensions only if elicited. Tag `(Bio)` `(Psych)` `(Social)` `(Cultural)` when clear.

### D. Screen coverage (topics, not scripts)
Which clusters were explored. Unasked → Questions to resolve — **never invent “yes”**.

### E. Risk & safeguarding
SI / self-harm / harm to others / children — only as asked/answered; actions taken.

### F. MSE
Domains actually covered (mse checklist). Not assessed ≠ NAD.

### G. Engagement & process
Role explained; confidentiality; rapport/resistance facts.

### H. Plan + Questions to resolve
Next appointment type; interim supports; skipped domains to follow up.

## Non-negotiable
1. Every claim traceable to the source notes (or insufficient marker)  
2. No invented trauma / sexual history / Dx / risk  
3. DRAFT footer; human edits before saving the record  

## Output footer

```
---
Status: DRAFT — worker review required before save.
Not a diagnosis or final risk decision.
```

## Related
`draft-mh-assessment`, `draft-5p`, `case-qa`, `pdpo-deidentify`
