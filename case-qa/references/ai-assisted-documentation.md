---
title: AI-assisted documentation — ethics and PDPO
source_status: distilled_from_manuals
source: Adapted for ICCMW from Bloch-Atefi (PCJA 2025) ethics themes + CAPE Privacy/Background criteria; aligned with HK PDPO principles. Not legal advice — confirm with agency DPO / clinical lead.
review_status: pending_clinical_approval
version: 2026-07-v1
---

# AI-assisted documentation — ethics and PDPO (ICCMW)

ICCMW uses AI as a **staff copilot** to rewrite case recordings and answer staff Case Q&A. AI does **not** replace the therapeutic relationship or clinical decisions.

## What AI may do
| Allowed | Not allowed |
|---------|-------------|
| Restructure / polish notes from worker draft | Client-facing psychotherapy chatbot |
| Flag gaps / questions for next contact | Invent diagnosis, risk severity, or interventions |
| Pull guideline wording labelled as guideline-only | Paste live identifiable case text into unapproved public tools |
| Suggest approach vocabulary when draft supports it | Treat the draft as already saved |

## Accountability
- The **named worker** remains author of the clinical record.
- AI output is always **DRAFT** until human approve.
- Staff must be able to explain every retained sentence.

## Client transparency and consent
Follow agency policy. Recommended practice:
1. Include AI-assisted documentation in service information / consent materials when notes may be AI-assisted.
2. Clients may ask how notes are produced; answer factually (staff draft → optional AI rewrite → staff approve).
3. Offer **opt-out** of AI rewrite where agency policy allows (human-only edit path).
4. Do not pressure clients to accept AI involvement.

Sample staff wording (adapt to agency form):

> Some of our clinical documentation may be assisted by an approved AI tool that helps structure notes. A worker always reviews and approves the final record. The AI is not your therapist and does not make diagnoses or risk decisions. You may ask about opting out of AI-assisted note rewrite.

## PDPO-oriented controls (HK)
| Control | Practice |
|---------|----------|
| Purpose limitation | Use case text only to produce the requested rewrite / Q&A answer |
| Data minimisation | Pass the smallest useful excerpt; prefer de-identified pilots |
| Access / retention | Audit logs (user, case id internal, timestamp, app version); retention per DPO |
| Security | Use only approved agency tools — no public chatbots with live cases |
| Secondary use | Do not use production case text to train public models |
| Third parties | Vendor contracts must match PDPO / agency DPA requirements |

## Therapeutic relationship
- AI must not present itself as a friend, clinician, or substitute for the worker–client relationship.
- Do not let AI “over-validate” or soft-pedal risk relative to the draft.
- Documentation quality supports alliance (clear, respectful, accurate) — AI is editorial help only.

## Staged rollout
1. Rewrite Case Recording (assistive) with human approve  
2. Case Q&A on provided source notes  
3. Any higher autonomy (triage bots, client chat) — **out of scope** unless separately approved  

### Common pitfalls
- Treating AI draft as already-approved record text  
- Inventing that consent for AI was discussed when draft is silent  
- Using unapproved tools with identifiable notes  

### Q&A use
For “was AI used?” / consent questions: answer from agency policy + this card as **guideline_only** unless the case excerpt documents what was said to Clt.
