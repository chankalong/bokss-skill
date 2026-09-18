# Document therapy techniques in notes (ICCMW)

**Staff documentation aid only.** Do not role-play therapist to the public.  
Vocabulary adapted from Therapy Mode / CBT–DBT toolkits / counselor technique lists — used here to **label what the worker already did**, not to invent interventions.

## When to use
- Draft mentions skills, homework, exposure, defusion, values, MI, etc.
- the user names an approach (CBT, ACT, DBT, MI, SFBT, …) and the rewrite needs accurate naming
- CP or CW session describes psychological intervention

## Hard rules
1. Only name a technique if the draft’s actions match it  
2. If draft says “talked about worry” without a method → do **not** write “cognitive restructuring”  
3. Prefer: technique name + what was done + Clt response (as drafted)  
4. Never invent homework results or “breakthrough”  
5. Trauma processing labels (PE, CPT, EMDR…) only if explicitly in draft  
6. When the user names an approach, apply [approach-fidelity.md](approach-fidelity.md) pass/fail checks before finishing  
7. Do **not** write bare “CBT done” / “provided CBT” / “provided CBT psychoeducation” — name the element practised  
8. Do **not** invent distortion labels, SUDS/ratings, exposure hierarchies, worksheet completion, or experiments not in the draft  
9. Keep **Clt’s words** for thoughts/quotes; do not overwrite with textbook jargon  
10. Distortion labels, core beliefs, compensatory strategies — only if named or collaboratively evidenced in the draft (mark beliefs as tentative if framed that way)

## Fidelity mini-check (before output)
- [ ] Every technique name maps to a draft action  
- [ ] No modality jargon sprayed onto vague conversation  
- [ ] No bare modality claim without named technique  
- [ ] Clt wording for thoughts preserved  
- [ ] Risk/intake structure not overwritten by approach style  

## Vocabulary cheat-sheet (use only when evidenced)

| Family | Names you may use if draft supports | Note-friendly phrasing |
|--------|-------------------------------------|-------------------------|
| **CBT** | Thought record, testing thoughts, cognitive restructuring / evidence review, continuum, behavioural activation, activity chart / pleasure–mastery, graded task assignment, problem-solving, advantage/disadvantage, graded exposure, behavioural experiment (prediction → test → result), worry postponement | “Practised graded MTR exposure step 2; Clt completed with anxiety peak 6/10 (Clt report).” |
| **ACT** | Defusion, acceptance, values clarification, committed action, present-moment, self-as-context | “Explored values around family role; linked to one committed action for week.” |
| **DBT** | Mindfulness, distress tolerance, emotion regulation, interpersonal effectiveness (DEAR MAN etc.) | “Practised TIPP / paced breathing as drafted — do not rename if draft only says ‘breathing’.” |
| **MI** | Open questions, affirmations, reflective listening, summarising; decisional balance; elicit–provide–elicit | “Used reflective listening on ambivalence about meds; Clt identified own reason to continue.” |
| **SFBT** | Preferred future, exception finding, scaling, miracle question, coping question, compliments tied to evidence | Only if those moves appear in draft — see sfbt |
| **SMCM** | Strengths, goals, natural supports, outreach | Prefer SMCM vocabulary from smcm |

## Anti-patterns (from consumer “Therapist/Psychologist” skills — do **not** do in progress notes)
- Validating the **reader** as if AI is their therapist  
- Inventing crisis hotlines in the clinical note  
- Adding Socratic questions the worker never asked  
- Filling empty sessions with textbook technique lists  
- Writing “CBT done” / “provided CBT psychoeducation” without naming the technique practised  
- Overwriting Clt’s automatic-thought wording with textbook labels  

## Output snippet (for insertion into rewrite)

```markdown
### Intervention / techniques (from draft only)
- [Technique]: [what was done] — [Clt response if stated]
- [Insufficient information: specific technique name] (if actions vague)
```

## Examples (synthetic)

### A — draft supports naming (`approach=cbt`)
**Draft:** “Practised going one MTR stop further; anxiety rose then settled. Looked at thought ‘I’ll panic and faint’ for/against. Homework: two stops next week; Clt will try but scared.”

**Output:**
```markdown
### Intervention / techniques (from draft only)
- Graded exposure: practised MTR travel one stop further than previous — Clt reported anxiety rose then settled
- Cognitive restructuring / evidence review: examined thought “I’ll panic and faint” with for/against evidence
- Homework set: attempt two stops next week — Clt willing but reported fear
```

### B — vague draft — do not invent
**Draft:** “Talked about worry on the train.”

**Output:**
```markdown
### Intervention / techniques (from draft only)
- [Insufficient information: specific technique name] — draft describes conversation topic only, no method
```

## References (bundled)
- [approach-fidelity](references/approach-fidelity.md)
- [rewrite-rules](references/rewrite-rules.md)

