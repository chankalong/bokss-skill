---
---

# Shared clinical safety patterns (ICCMW)

Shared safety patterns for AI-assisted documentation drafts.

## 1. DRAFT banner (always)
End or start every clinical AI output with:

```
---
Status: DRAFT — worker review required before save.
Not a diagnosis, not a final risk decision, not a substitute for clinical judgement.
```

## 2. Never invent
Do not add: diagnoses, risk severity, trauma history, scores, quotes, interventions, meds, people, agencies — unless present in the source notes.

## 3. Insufficient information + Questions to resolve
When a required field is empty:
- In-body: `[Insufficient information in draft: …]`
- Also list under `## Questions to resolve` (next contact / assessment)

## 4. Domain tags (formulation)
When possible, tag bullets: `(Bio)` `(Psych)` `(Social)` `(Cultural)` `(Env/OT)` `(System)`  
Only if the draft supports that domain.

## 5. Source labels
Prefer: `(Clt report)` `(Wher observation)` `(file)` `(family report)` `(clinic letter)`

## 6. Risk stop (surface, don’t invent)
If draft shows active SI/HI with plan+means, child protection trigger, acute psychosis/withdrawal:
- Preserve facts as written
- Add `## Risk-management flags` urging agency procedures / human decision
- Do **not** invent crisis plans, hotlines, or LOC (IOP/PHP) unless already in draft
- Do **not** downgrade severity

## 7. Identifiers
Do not invent or expand identifiers. Prefer role-based supports (“a sibling”). For pilots, prefer de-identified text before cloud LLM use.

## 8. AI disclosure (CAPE-lite Background)
- Never imply the AI is a clinician, therapist, friend, or diagnostician
- Output must remain clearly a **staff draft** for the worker to approve
- Do not role-play therapy toward the client in the note

## 9. Automation bias (copilot, not GPS-as-driver)
- Prefer under-claiming over polished invention when draft is thin
- Surface `## Questions to resolve` instead of filling gaps
- Worker may reject or heavily edit; do not argue for invented content

## 10. Privacy & harm (CAPE-lite)
- No new PII; no encouragement to paste cases into public tools
- Do not recommend no-suicide contracts or other non–evidence-based harm-reduction theatre
- Unsafe method detail: never expand beyond what draft already states

## 11. Care stage awareness
When helpful, align depth with Exploration / Insight / Action ([care-stages](references/care-stages.md)). Do not invent that a stage was completed.

## 12. Approach fidelity
If the user names an approach: see _approach fidelity — name techniques only when draft actions match.
