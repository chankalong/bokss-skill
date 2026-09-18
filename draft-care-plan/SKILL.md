---
name: draft-care-plan
description: Draft a BOKSS/ICCMW care or intervention plan from the source notes the user provides. Use when staff ask for goals, interventions, and review dates. Do not invent goals the client never endorsed. Output is DRAFT for human edit.
---

# Draft care plan

**Care stage:** Action ([care-stages](references/care-stages.md)).  

Turn understanding from the source notes (especially **5P** if present) into a living plan: goals, who does what, review date.

Read [intervention-planning](references/intervention-planning.md) when helpful.  
If 5P is missing but needed, suggest `draft-5p` first.

## Inputs
- source notes the user provided (**required**)
- optional prior fact extract — hints only (schema in `case-qa`)
- optional prior 5P text in the source notes or staff paste
- optional named approach

## Logic chain
1. Presenting problems → what must change for Clt  
2. Perpetuating factors → intervention targets  
3. Protective factors → resources to mobilise  
4. Goals → observable / agreed  
5. Interventions → CW/OT/CP/Clt/family/agency actions  
6. Review → date + indicators  

## Goal quality (SMART-enough)

| Element | Weak | Stronger |
|---------|------|----------|
| Specific | “Be more social” | “Attend church volunteer Sat 10–12” |
| Observable | “Feel better” | “Complete sleep diary 5/7 nights” |
| Agreed | Staff-only goal | Clt wording preserved |
| Relevant | Random activity | Linked to formulation / programme |
| Time-bound | “Someday” | “Review in 4 weeks (date)” |

If multiple goals: state **lead target first** and why (from Perpetuating / Clt priority). Do not invent level-of-care.

## Suggested sections
1. Clt goals (short / medium term)  
2. Service interventions (name approach only if in the source notes: SMCM, ACT, CBT-I…)  
3. Clt actions / homework  
4. Family/network involvement (consent as applicable)  
5. Inter-agency actions  
6. Risk review triggers (**only if in the source notes**)  
7. Review date & success indicators  

## Mapping examples (synthetic)

| 5P element | Plan implication |
|------------|------------------|
| Perpetuating: MTR avoidance | Graded travel practice with CW; log attempts |
| Protective: supportive sister | Sister accompanies first 2 practices (if Clt agrees) |
| Presenting: loneliness after move | SMCM link to volunteer desk; weekly structure goal |

## Non-negotiable
1. Do not invent goals Clt never endorsed  
2. Do not add programmes/modules not in the source notes  
3. Vague wishes → tentative goals + `[Insufficient information: collaborative goal-setting]`  
4. Keep language of the source notes (EN/中文)  
5. Questions to resolve + DRAFT footer  

## Output footer

```
---
Status: DRAFT — worker review required before save.
Not a final clinical decision.
```

## Related
`draft-5p`, [intervention-planning](references/intervention-planning.md), `case-qa`
