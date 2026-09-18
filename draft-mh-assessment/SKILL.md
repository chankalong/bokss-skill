---
name: draft-mh-assessment
description: Draft a BOKSS/ICCMW mental health assessment from the source notes the user provides. Use when staff ask for an MH assessment write-up across domains including MSE and risk as documented. Never invent diagnoses or unassessed MSE findings.
---

# Draft mental health assessment

**Care stage:** Exploration → Insight ([care-stages](references/care-stages.md)).  

Read [mental-health-assessment](references/mental-health-assessment.md) and [mse-checklist](references/mse-checklist.md).

## Inputs
- source notes the user provided (**required**)
- optional prior fact extract — hints only (schema in `case-qa`)
- optional staff focus (social worker / OT / CP / nurse)

## Domains (write only what was gathered)
1. Identifying & context  
2. Presenting / chief complaint + functional impact  
3. HPI (onset, course, stressors, vegetative, prior episodes/treatment)  
4. Screen/syndrome topics actually covered — never invent positives  
5. Psychiatric / medical / medication history  
6. Psychosocial history  
7. MSE — form domains; unexamined → not assessed (not NAD)  
8. Risk — ideation/intent/plan/means/attempts/violence as documented  
9. Strengths & resources  
10. Formulation — prefer `draft-5p`; no invented Dx  
11. Plan / recommendations  
12. Questions to resolve  

## Psychometrics
Copy instrument + scores only if fully present; scores ≠ diagnosis; item-level SI flags → Risk-management flags.

## If staff want therapy-process emphasis
Point them to `clinical-psychologist-case-recording` for a CP **session** note; this skill stays assessment breadth from the source notes.

## Non-negotiable
Preserve facts from the source notes; DRAFT footer; insufficient-information markers; never invent Dx or unassessed MSE.

## Output footer

```
---
Status: DRAFT — worker review required before save.
Not a final diagnosis or risk decision.
```

## Related
`draft-intake`, `draft-5p`, `case-qa`
