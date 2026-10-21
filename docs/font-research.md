# Font research

## Four types of information

| Type | Examples | Treatment |
| --- | --- | --- |
| Factual metadata | Family name, available weights, italics, scripts, license, variable axes | Verify against current primary sources |
| Designer-stated intent | Described use for headlines, continuous text, or interfaces | Attribute the claim and retain evidence |
| Reviewer judgment | Expressive, restrained, formal, warm, visually dense | Use a shared rubric; label subjectivity |
| User preference | Wants expressive headings or restrained body text | Store in the assessment response, not as a font fact |

A source description is evidence of intended use, not proof of performance for every reader. Serif/sans serif classification is insufficient to establish suitability.

## Candidate dimensions, not approved scores

Investigate role suitability, expressiveness, formality, geometric versus organic appearance, width, stroke contrast, character distinction, available styles, language support, and platform availability.

Some are measurable, some need interpretation, and some depend on the chosen size or style. Record the tested variant and context. A variable family may behave differently across axes.

Do not put every descriptor on a numeric scale. Language support is a requirement check; design mood is a preference judgment. Keep those separate.

## Source order

1. Google Fonts family About page and repository documentation.
2. Designer or foundry documentation and specimens.
3. Font metadata and applicable license.
4. Attributed secondary references for pairing examples.
5. Our own documented preview tests.

Google Fonts documents About content in ARTICLE.en_us.html. Repositories may contain older DESCRIPTION.en_us.html files or different documentation paths. Discover paths rather than assuming one filename per family.

## Record format

Use research/font-record.template.json as a starting structure. It is schema version 0.1 and still a draft. Copy it to research/fonts/<stable-id>.json only when researching a real family.

- Stable local ID; external names and IDs in a separate field.
- Structured technical fields with their evidence references.
- Stated intended uses separate from reviewer judgments.
- Evidence references with URL, retrieval date, optional revision, brief paraphrase, and claim location.
- Unknown values stay null or explicitly unknown.
- Review status and eligibility are separate from completeness.
- Future rubric versions identify what a score means.

Lists use null when not researched; an empty list means checked and none found. A null italic flag means unknown; false means checked and absent.

## Bounded batch workflow

1. Select at most 5 families and list them in the checkpoint.
2. Gather factual metadata and source descriptions first.
3. Save each family separately; keep short paraphrases rather than copied descriptions.
4. Flag ambiguous claims for review. Do not force a score.
5. Apply the draft rubric to a few shared examples only after defining its endpoints.
6. Review evidence, missing fields, contradictions, and consistency.
7. Checkpoint before adding another batch.

Separate research completion from recommendation eligibility. Do not send pending or unreviewed records into production recommendations.

## Validation and maintenance

First validate JSON syntax, unique IDs, required draft fields, evidence references, and allowed status values. Add a formal machine-readable schema once the pilot shows which fields are useful.

When a source changes, revisit affected factual fields and intended-use claims. When a rubric changes, mark affected judgments for re-review. Do not silently reinterpret older scores.

Store pairing evidence under research/pairings/ when collected, referencing family IDs, assigned roles, variants, context, source, and review status. Do not claim every pair among individually suitable fonts works.

## Recommended first experiment

Research 3-5 contrasting families, draft a small rubric, and have the same examples reviewed consistently. Expand only after that reveals which judgments are repeatable and which remain ambiguous.

## Entry shapes for the draft record

Each evidence item uses: id, url, retrieved_at (ISO date), source_revision (nullable), source_kind, and paraphrase.

Each intended-use item uses: role, statement, evidence_ids, and status. Keep a designer’s claim attributable; use status "source_stated" until independently evaluated.

Each judgment uses: attribute, value (nullable), rubric_version (nullable), evidence_ids, reviewer, reviewed_at, and context. Context records style, weight, size, language, sample text, and device when those affect the judgment.

Add technical_evidence as a mapping from technical field names to evidence IDs when populating a real record. Every non-null technical fact needs evidence. Dates and source revisions should make changed claims traceable.

Draft research statuses: not_started, in_progress, needs_review, reviewed, and blocked. A reviewed record can still be ineligible for recommendations; explain why. Keep unfinished evidence and next actions in the checkpoint rather than silently treating a partial record as complete.
