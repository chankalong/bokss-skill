---
name: clinical-psychologist-case-recording
description: Rewrite or polish a BOKSS/ICCMW clinical psychologist progress note (six fields: Objective, Behavioral Observation, Description or Progress, Clinical Impression, Intervention, Plan and Follow-up). Use when the user pastes a CP session note. Not a social-work four-field note.
---

# CP case recording — Clinical Psychologist (ICCMW)

Editorial assistant for clinical psychologist progress notes. Humans remain clinically responsible. Output is a **draft until the worker reviews it**.

Identifiable text: run `pdpo-deidentify` first. Shared guardrails: `clinical-safety-copilot`.

The note should let another worker understand: session aim, what was observed and discussed, clinical sense-making, what was done, and what happens next — not a transcript.

## Input → output (recipe)

**Read** the six headings (messy OK), or one unsorted draft → sort into the six fields before polishing.

**Write** only these headings, in order:

```
## Objective
## Behavioral Observation
## Description or Progress
## Clinical Impression
## Intervention
## Plan and Follow-up
```

Do **not** use DARP/SOAP letter headings or alternate skeletons (`Session Focus`, `Mental State Examination`, …).  

If the user names a diagnosis or counselling approach, use that vocabulary only when the draft supports it. If they ask for formulation, Clinical Impression may use brief 5P; empty Ps → insufficient-info markers.

## Rules (non-negotiable)

1. Preserve facts from input only — never invent symptoms, risk, diagnoses, quotes, techniques, psychometrics, percentiles, severity bands, MSE items, history, or private process content
2. Do not add or remove risk content relative to the draft
3. Keep draft language (EN or 中文) unless translation requested
4. Missing required info → `[Insufficient information in draft: …]`
5. If clinical meaning would change (“more severe/positive”), refuse; note under Gaps
6. Separate **Clt report** vs **CP observation** vs **clinical opinion** vs **test data** when both appear; short bullets; quote sparingly and only if in draft
7. If diagnosis and/or approach are known: think with `apply-diagnosis-approach` (CP brain — clinical process, not a restamped Dx). Name techniques only when draft actions match

## Six fields (from CP Case Recording Guideline)

Use each prompt **only when the draft supports it** — never invent to fill the guideline list. Skip empty domains. Clinical Impression synthesises; does not repeat Description or Progress.

### Objective

1. Goals the worker aimed to achieve in the present session  
2. Mode of service delivery, e.g. face-to-face, online, home visit  
3. The persons involved in the session, if not only the principal client  

**Good:** “Review MTR exposure homework and examine panic prediction (face-to-face).”  
**Weak:** “Follow up” / “Support Clt” with no focus.

### Behavioral Observation

1. Attendance status (e.g., attended on time, late, missed)  
2. Appearance, including grooming, hygiene, dress, physical condition (e.g., groomed, dishevelled)  
3. Behavior, including eye contact, psychomotor activity, cooperation, engagement level (e.g., avoided eye contact, restless, rigid)  
4. Speech, including rate, volume, tone, coherence (e.g., rapid, monotone, hesitant)  
5. Mood (client's self-report), affect (therapist's observation of emotional expression), and the congruence between mood and affect  
6. Thought process and content, including logical/coherent thinking, delusions, hallucinations, suicidal or homicidal ideation (if present)  
7. Cognition, including orientation, attention, memory, insight, judgement  

Point form OK. Never invent a full MSE from a thin draft.

### Description or Progress

1. The primary focus or presenting problem discussed by the client  
2. Updates on symptoms, life events, or stressors since the last session  
3. Client's response to previous homework or interventions  
4. Potential challenges, setbacks, or barriers  
5. New insights or developments  

If draft includes measures: instrument name + score **only as written** — never compute totals, never add severity bands, never upgrade scores to Dx. Preserve any risk wording in the narrative without expanding.

### Clinical Impression

1. Clinical interpretation of the client's symptoms and behavior  
2. Current level of functioning  
3. Assessment of risk (e.g., suicidal ideation, self-harm, harm to others) — preserve draft only  
4. Progress toward treatment goals (e.g., improving, plateaued, deteriorating)  
5. Diagnostic consideration (if appropriate) — only if already in draft; never invent Dx  
6. Factors maintaining or contributing to symptoms  
7. Objective achieved / not, because ___  

### Intervention

1. Therapeutic modalities utilized (e.g., CBT, DBT, ACT, EFT) — only if named or clearly supported; never bare “CBT done”  
2. Specific skills taught or practiced (e.g., psychoeducation, cognitive restructuring, grounding)  
3. Client’s engagement with and response to the intervention  
4. Crisis intervention measures (if appropriate)  

### Plan and Follow-up

1. Homework or therapeutic tasks assigned to the client  
2. Focus or treatment goals of the upcoming session  
3. Referrals or collateral contacts needed  
4. Specific safety monitoring or crisis plans if applicable — only if in draft  
5. Coordination with other service providers, if appropriate  
6. Date and time of the next scheduled appointment — only if known  

## Abbreviations

| Short | Full | Short | Full |
|-------|------|-------|------|
| Clt | Client | Wher | Worker |
| MS | Mental state | Tx | Treatment |
| Dx | Diagnosis | mgt | Management |
| Mo / Fo | Mother / Father | Ho / Wo | Husband / Wife |

## Output package

1. The six headings only  
2. `## Gaps flagged`  
3. `## Questions to resolve`  
4. `## Risk-management flags` — only if risk already in draft  
5. Footer:

```
---
Status: DRAFT — worker review required before save.
Not a diagnosis or final risk decision.
```

Write `None` under Gaps/Questions if empty.

## Common mistakes

- Outputting Session Focus / MSE / Risk Assessment / Outcome Measures / Plan instead of the six headings
- Inventing attendance, appearance, speech, thought content, or cognition when the draft lacks them
- Adding PHQ/GAD severity bands or Dx from a raw score; inventing “diagnostic consideration”
- Dumping Clinical Impression as a second Description or Progress
- Expanding “No SI today” into a full risk assessment or contingency plan not in the draft
- Skipping Gaps/Questions, or renaming them; paraphrasing the DRAFT footer

### Micro-example (synthetic)

**Draft:** “Worry on MTR. Practised one stop further; anxiety rose then settled. Looked at thought 'I'll panic and faint' for/against. Homework: two stops next week; Clt willing but scared. No SI today.”

**Objective:** Review MTR exposure and examine panic prediction.  
**Behavioral Observation:** `[Insufficient information in draft: presentation detail]`  
**Description or Progress:** Clt reported MTR worry; practised one stop further — anxiety rose then settled; examined thought “I'll panic and faint” for/against; willing but scared for next step; no SI today.  
**Clinical Impression:** Panic prediction remains active; homework willingness present with fear.  
**Intervention:** One-stop practice; for/against on panic prediction (as draft stated).  
**Plan and Follow-up:** Homework — two stops next week; follow up fear and compliance next session.
