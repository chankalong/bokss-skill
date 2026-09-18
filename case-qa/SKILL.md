---
name: case-qa
description: Answer staff questions about a BOKSS/ICCMW case from the source notes the user provides. Use when asking what records say, listing documented facts, risk questions, or guideline questions tied to a case. Cite note dates; say Not in provided records when unknown; never invent diagnosis or risk. If the user wants a structured fact table, extract first using the schema in this skill.
---

# Case Q&A (ICCMW)

Adapted from clinical note-extract provenance ideas (null-safety, citations) — without US EHR coding.

## Inputs
- the staff question
- source notes: dated notes the user provided (required)
- optional prior fact extract — **hints only** (schema below)
- optional staff role, theme, or care stage (exploration / insight / action)

## Assertion classes (use explicitly)
| Class | Meaning | How to write |
|-------|---------|--------------|
| **supported** | Stated in the source notes | Answer + cite note/date (quote or paraphrase) |
| **not_in_records** | Absent from the source notes | **Not in provided records** |
| **guideline_only** | From bundled references | Label clearly: “Guideline wording (not about this client): …” |

Never blur guideline_only into supported. Never treat a prior fact extract alone as supported without confirmation in the source notes (or explicit “last documented in [date] per memory; not restated in current notes”).

## Rules
1. Prefer answering from the **source notes** first; bundled references are vocabulary / general guidance only
2. Cite which note/date supports each claim
3. Do not invent diagnosis or risk; do not escalate/de-escalate relative to the source notes
4. For risk themes: urge clinical judgement / agency risk procedures; no harmful method detail
5. Do not output identifiers beyond what the source notes already contain (suggest `pdpo-deidentify` for demos)
6. If the question needs a structured fact list, **extract first** with the schema below — then answer
7. Longitudinal: when multiple dated notes exist, state trajectory with dates; do not erase earlier risk because a later note is silent
8. If the question implies intake vs formulation vs care plan, read matching pathway/approach cards ([care-stages](references/care-stages.md))

## Suggested answer shape

```markdown
## Answer
[direct answer]

## Evidence
- [date / note type]: "…" or paraphrase (supported)
- …

## Not in provided records
- …

## Guideline context (optional)
Guideline wording (not about this client): …

## Caution
Human remains accountable. DRAFT for clinical use.
```

## Fact extract (when asked “what is documented” / before 5P)

Only extract what is explicitly in the source notes. Every non-null field needs `value` + `source` (note type + date) + optional `confidence` (`explicit` / `paraphrase`). Absent → `null`. Separate **Clt report** vs **Wher observation** vs **third party**. Risk: copy wording; never escalate. Diagnosis: only if already written.

| Field | Value | Source | Notes |
|-------|-------|--------|-------|
| care_stage | exploration \| insight \| action \| null | inferred only if clear | Do not invent stage completion |
| presenting_problems | … | progress 2026-03-01 | Clt report |
| goals_stated | … | intake 2026-02-10 | |
| symptoms | … | … | |
| meds | … / null | … | |
| risk_si | … / null | … | verbatim if present |
| risk_self_harm | null | — | |
| risk_others | null | — | |
| child_protection | null | — | |
| interventions_done | … | … | |
| homework | … | … | |
| approach_used | … / null | … | only if named or clearly evidenced |
| supports | … | … | role-based |
| diagnosis_documented | null | — | do not invent |
| formulation_hints | … | … | only phrases already in notes |
| open_questions | … | … | gaps for next contact |
| last_note_date | … | … | |

Prior fact-extract rows are hints only — re-verify against the current source notes; do not silently drop prior risk.

```
Status: DRAFT fact extract — human check before clinical use.
```

## References
- Bundled: [care-stages](references/care-stages.md), [suicide-self-harm-risk](references/suicide-self-harm-risk.md)
- `clinical-safety-copilot` for AI/consent questions
- `apply-diagnosis-approach` when the theme is depression or a named approach
- Never treat guideline cards as facts about *this* client

## Related
`draft-5p`, `pdpo-deidentify`, `clinical-safety-copilot`
