# Project instructions

Read README.md and research/checkpoint.md first. Read the relevant docs before changing research or behavior.

## Scope and continuity

- This repository is the source of truth for planning the typography assessment.
- Preserve the distinction between agreed requirements, proposals, and open questions.
- Work in batches of at most 5 families. Finish or checkpoint the current batch before expanding.
- Update research/checkpoint.md in every research session: completed records, exact next task, sources, blockers, and unresolved judgments.
- Keep one record per font family under research/fonts/<stable-id>.json. Store pairings separately; avoid duplicating complete font records.
- Do not assume chat history is available. Write enough for the next session to resume.

## Evidence and scoring

- Read primary sources before claiming font characteristics. Keep source URLs, retrieval dates, source revisions where available, and brief evidence paraphrases.
- Separate factual metadata, designer-stated intent, reviewer judgments, and user preferences.
- Unknown is null or explicitly unknown, never an invented neutral score.
- Do not assign numeric personality scores until the attribute rubric is defined and versioned.
- Automatic extraction or model-generated labels require review before recommendation eligibility.
- Do not infer readability, accessibility, personality, or pairing quality from category alone.
- Treat audience age and culture as context; ask about actual language and reading needs.
- Review combinations in real content and assigned roles. A third family needs an explicit purpose.
- Do not copy source images or full descriptions into this repository.

## Writing and design

Apply the Mailchimp-inspired guidance in Pythonidaer/llm-instruction-toolkit under design/content-and-tone: best-practices.md, mailchimp-tone-voice.md, mailchimp-writing-goals-principles.md, and mailchimp-grammar-mechanics.md. Read current guidance before drafting product copy. Use clear, considerate, conversational teaching; define useful technical terms; avoid hype and forced humor. No emoji. Preserve full visible resource URLs where useful.

Do not start UI implementation or select a stack as part of a research-only task. Validate changed records and links; distinguish source checks from browser or reader testing.
