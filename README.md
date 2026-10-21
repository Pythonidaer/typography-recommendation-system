# Typography recommendation system

A guided assessment to help people choose font families for a design.

Status: a small editorial walkthrough is available for testing. It uses 80 source-reviewed editorial candidates and transparent rules; it is not a validated catalogue-wide recommendation engine.

## Test the walkthrough

https://pythonidaer.github.io/typography-recommendation-system/

GitHub Actions builds and deploys the static site from site/. Start with the portfolio example or enter your own brief. The four-step flow returns the requested 1-3 families, keeps replacements separate, and checks role-specific character requirements. Family selection comes before styling choices.

Use the top-right **Font data** link to inspect categories, file checks, role evidence, sorting points, sources, and missing measurements. The pinned repository snapshot contains 2,040 family metadata directories; the pilot uses 80, not the full catalogue.

For local setup, see [the pilot guide](docs/walkthrough-pilot.md).

## Agreed direction

1. Ask whether the person wants 1, 2, or 3 font families. Explain that regular, bold, and italic can belong to the same family.
2. Ask about the project’s purpose, information, audience needs, medium, desired mood, and existing design.
3. Recommend the requested number of families, with suggested text roles and an explanation.
4. Provide a later space to experiment with real content, weights, sizes, spacing, colors, and optional modular scales.
5. Help document final decisions in a typography style guide.

The main research challenge is describing fonts consistently enough to support useful recommendations. Scores and pairing rules are not settled.

## Project documents

- [Assessment principles](docs/assessment-principles.md): purpose, legibility, and readability, with supporting mood/harmony and hierarchy checks.

- [Draft assessment questions](docs/assessment-questions.md): project prompts, conditional follow-ups, and example input.
- [Pilot evaluation plan](docs/pilot-evaluation-plan.md): role-specific tasks and observation methods.
- [Product plan](docs/product-plan.md): decisions, proposed workflow, and open questions.
- [Attribute evidence](docs/attribute-evidence.md): minimum information and source findings before sampling.
- [Font research](docs/font-research.md): attributes, evidence, and manageable batches.
- [Recommendation approach](docs/recommendation-approach.md): proposed filters, ranking, and combination checks.
- [Sources](docs/sources.md): references and what has or has not been reviewed.
- [Source audit](docs/source-audit.md): coverage, data-quality findings, and reproducible checks.
- [Candidate questions](docs/assessment-dimensions.md): proposed dimensions and source mappings.
- [Pilot sample](docs/pilot-sample.md): 5 records across provider categories, awaiting visual and suitability review.
- [Pilot documentation review](docs/pilot-source-review.md): intended uses, license sources, character checks, and attribute gaps.
- [Broader attribute inventory](docs/attribute-inventory.md): 27 candidate terms across separate layers, with all 20 source expressive labels retained.
- [Attribute coverage](docs/attribute-coverage.md): reproducible availability counts and limits.
- [First guided test](docs/first-guided-test.md): a short project brief and visual exploration to try in conversation.
- [Original mood vocabulary](docs/mood-vocabulary.md): historical six-word proposal; not the catalogue scope.
- [Mood review protocol](docs/mood-review-protocol.md): four-option comparisons, personal preferences, and evidence separation.
- [Rendered specimen gallery](research/specimens/batch-1/README.md): headings, paragraphs, and character samples for the 5 pilot instances.
- [Specimen preparation](docs/specimen-preparation.md): reproducible rendering and verification limits.
- [Response records](docs/response-records.md): raw comparison format and validation limits.
- [Missing attribute policy](docs/missing-attribute-policy.md): source scope, instance coverage, and unknown values.
- [Existing tools review](docs/existing-tools-review.md): first documentation pass and approaches to investigate.
- [Audience needs](docs/audience-needs.md): primary resources, task-based profiles, and proposed assessment questions.
- [Content and tone brief](docs/content-and-tone.md): knowledgeable, approachable, concise writing, with light playfulness during exploration.
- [Current checkpoint](research/checkpoint.md): progress and the next bounded task.
- [Font record template](research/font-record.template.json): a draft record, not a researched font.

Read [AGENTS.md](AGENTS.md) before contributing. Start each session with the checkpoint. The current walkthrough is a buildless HTML/JavaScript pilot hosted on GitHub Pages. Research and calibration remain separate from its editorial rules.
