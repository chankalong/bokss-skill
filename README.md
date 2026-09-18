# bokss-skill

Cursor / Claude / Codex skills for Baptist Oi Kwan Social Service (浸信會愛群社會服務處).

Install the whole library:

```bash
npx skills add chankalong/bokss-skill
```

Or copy a single skill folder URL from the [BOKSS AI Resource Centre skill library](https://github.com/chankalong/bokss-skill) and paste it into your agent.

## Skills

The public skill library groups copied skills by use case (BOKSS, Writing, Design, Development). Skills that cannot live in this repo appear under **Other GitHub** and copy their original GitHub link.

### BOKSS originals

Staff documentation skills are **not** a client-facing therapist. Identifiable notes go through `pdpo-deidentify` first. Licensed [CC BY-NC-ND 4.0](LICENSE).

**Comms**

- **refresh-insights-writing** — Re:Fresh Insights-style Traditional Chinese psychoeducation articles
- **bokss-hk-writing** — Traditional Chinese service copy for bokss.org.hk, leaflets, and centre notices
- **surveyjs-json** — bilingual SurveyJS assessment JSON for BOKSS

**Safety**

- **pdpo-deidentify** — PDPO-aware redaction of Hong Kong identifiers before a model sees case-like text
- **clinical-safety-copilot** — staff documentation guardrails (draft only; never invent diagnosis/risk; not a therapist)

**ICCMW case recording**

- **social-worker-case-recording** — Case Worker four-field progress note
- **ot-case-recording** — OT four-field recording (occupation; SOAP letters only as optional sub-labels)
- **clinical-psychologist-case-recording** — CP six-field recording
- **apply-diagnosis-approach** — SW / OT / CP thinking when diagnosis/approach are known (includes technique naming and depression-domain checks)

**Intake, assessment, formulation, Q&A**

- **case-qa** — staff questions with supported / not-in-records / guideline-only; includes fact extract
- **draft-intake** — first-contact / intake draft
- **draft-mh-assessment** — mental health assessment draft (no invented MSE)
- **draft-5p** — 5P formulation from notes
- **draft-care-plan** — goals and interventions the client actually endorsed

### Anthropic (Apache 2.0 copies)

Copied from [anthropics/skills](https://github.com/anthropics/skills). Each folder has `SOURCE.md` and the upstream `LICENSE.txt`. **Not** BOKSS-licensed.

- discernment-nudge, frontend-design, mcp-builder, skill-creator, webapp-testing, web-artifacts-builder, claude-api

Document skills (`docx`, `xlsx`, `pptx`, `pdf`, `doc-coauthoring`) are **not** copied here. Their license forbids redistribution. The skill library lists them under Other GitHub and copies the Anthropic GitHub link.

### Other third-party (MIT)

Each folder has `SOURCE.md` and the upstream license. **Not** BOKSS-licensed.

| Skill | Upstream | Owner |
| --- | --- | --- |
| react-best-practices | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel |
| composition-patterns | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel |
| web-design-guidelines | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel |
| writing-guidelines | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel |
| brainstorming | [obra/superpowers](https://github.com/obra/superpowers) | Jesse Vincent |
| speak-human-tw | [Raymondhou0917/speak-human-tw](https://github.com/Raymondhou0917/speak-human-tw) | Raymond Hou |

`speak-human-tw` is Taiwan-register 去 AI 味. Do **not** use it on BOKSS clinical notes or bokss.org.hk 書面語 — use `bokss-hk-writing` / `refresh-insights-writing` instead.

## License

BOKSS original skills (every folder listed under **BOKSS originals** above) and this README:

Copyright © 2026 Baptist Oi Kwan Social Service.

This work is licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). See [LICENSE](LICENSE).

Third-party skill folders keep their original licenses and copyright. They are **not** covered by the BOKSS CC BY-NC-ND terms. See each folder’s `SOURCE.md` and `LICENSE` / `LICENSE.txt`.
