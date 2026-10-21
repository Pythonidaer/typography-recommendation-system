# Attribute evidence and minimum information

Status: research proposal, version 0.1. Checked October 21, 2026. These gates are project decisions to test, not Google requirements or validated performance guarantees.

## Finding

Google Fonts already publishes human-assessed expressive and typographic tags. The repository distinguishes these from machine-assessed measurements. Its developer API can return tags that apply across an entire family designspace using capability=FAMILY_TAGS.

This gives us a starting vocabulary and existing source weights. It does not establish that those weights measure reader preferences or predict a successful pairing. Coverage and interpretation need a bounded audit before font sampling.

## Sources and scope

| Source | What we can obtain | Limit |
| --- | --- | --- |
| Google Fonts developer API | Families, variants, subsets, category, optional axes and family tags | Requires a key; family tags apply across the full designspace; no live API request was made |
| METADATA.pb | Font identity, files, source references, license label, styles, classification data | Available fields vary; inspect the actual family |
| Family About article / designer documentation | Background and stated intended uses | Descriptions vary; intended use is a source claim |
| tags/all/families.csv | Human-assessed expressive and typographic tag assignments, weights, and some style/axis locations | Missing assignments and blank locations need careful interpretation |
| tags/tags_metadata.csv | Tag names, numeric bounds, and descriptors | Names and bounds alone do not define a calibrated questionnaire |
| tags/tags_ui_details.textproto | UI grouping and display-label mappings | UI specimen fonts and display sizes are presentation choices, not recommendations |
| tags/all/quant.csv | Repository identifies these as machine-assessed measurements | Data and measurement methods not audited in this pass |

The tag metadata has many 0-100 ranges and separate quantitative ranges. Preserve raw source values. Do not call a weight a match percentage, confidence probability, accessibility score, or experimentally validated result.

## Candidate attributes and evidence gate

| Attribute | Minimum evidence for research use | Permitted use | Still needs review |
| --- | --- | --- | --- |
| Identity and source | Exact family name and repository/API identity, dated source | Join records | Aliases and releases |
| Broad category and substyle | Attributed metadata/tag assignment | Sampling and browsing | Overlapping classifications |
| Styles and axes | Current variants and axis information, with evidence | Filter required styles | Instance-specific behavior |
| Script/character support | Subset metadata for screening; required characters checked for a real brief | Requirement checks | A subset name is not proof that every required character exists |
| Usage permission | Applicable license source and intended usage | Eligibility review | Service/distribution conditions where relevant |
| Intended heading/body/interface role | Explicit designer statement, or documented role-specific review | Attributed explanation / provisional role | Actual reading performance |
| Feeling or expressiveness | Exact source tag, raw weight, source revision, and applicable scope | Candidate ranking experiments | Meaning, coverage, user understanding, score calibration |
| Formality or other new descriptor | Defined rubric plus documented evidence and reviewer | Research only until reviewed | Do not equate script/formal automatically with overall business formality |
| Character distinction | Documented glyph sample, style, size, language, and reviewer | Context-specific observation | Reader testing |
| Readability or accessibility | Context and actual reading/usability evidence | Qualified findings | No universal font score from appearance tags |
| Pairing suitability | Role-assigned combination with source examples or documented preview tests | Combination-level proposal | Not established by individual family scores |

## Minimum information depends on the task

### Ready for a sample inventory

Exact identity, a known category or documented overlap, and traceable current sources. This allows inclusion in an inventory, not recommendation eligibility.

### Ready for attribute experiments

Inventory gate plus the relevant source tags or a reviewed judgment, explicit variant/family scope, source references, and a recorded unknown-data policy. Only use supported dimensions.

### Ready for a project-specific recommendation trial

Relevant technical requirements pass, role evidence is present, and preference comparisons have sufficient comparable evidence. Every selected family needs a defined role. Multi-family results also require combination review.

No arbitrary requirement such as “80% of fields complete” substitutes for decision-relevant evidence. A missing required character blocks a trial even when all mood fields are filled.

## Unknowns and interpretation

- Missing tag is unknown, not zero or evidence for the opposite trait.
- Keep independent labels independent. Calm and loud are not automatically endpoints of one bipolar scale.
- Blank instance locations must not be assumed to mean a specific regular weight. Verify upstream semantics.
- Instance-specific tags must not be flattened into family-wide characteristics.
- A source “Childlike” appearance label does not mean suitable for beginning readers.
- “Easy Reading” is a source classification, not an accessibility guarantee.
- Do not map cultural or seasonal tags to a reader’s identity or assume agreement across cultures.
- Preserve source tags separately from our judgments and user-answer weights.
- Exclude quality ratings from initial user-facing recommendations until their role is justified.

## Next bounded audit before font sampling

1. Pin one upstream repository revision and read tag documentation and available assessment guidance.
2. Inspect structure and coverage: categories, expressive tags, purpose tags, and instance-specific rows. An aggregate coverage audit is not individual font research.
3. Identify available definitions, missing/duplicate assignments, aliases, and scope differences between CSV and API.
4. Produce a small set of candidate assessment dimensions with source mappings and unresolved interpretation notes.
5. Then select a subset across supported categories. Start with a small batch; coverage across all categories can span several batches of at most 5 families.

Use serif, sans serif, monospace, handwriting, and display as provisional provider categories, then add overlapping script, slab, blackletter, and other tags where supported. Symbols/icon-only candidates need a separate use case before joining ordinary heading/body trials.

## When Johnny is needed

Bring concrete examples when choosing which descriptors feel understandable or comparing visual alternatives. Ask for input when preferences would change assessment wording or output. Source discovery, gap recording, and maintaining research checkpoints can proceed independently.

## Source references

- https://developers.google.com/fonts/docs/developer_api#tags
- https://googlefonts.github.io/gf-guide/metadata.html
- https://googlefonts.github.io/gf-guide/article.html
- https://github.com/google/fonts/blob/main/tags/all/README.md
- https://github.com/google/fonts/blob/main/tags/all/families.csv
- https://github.com/google/fonts/blob/main/tags/tags_metadata.csv
- https://github.com/google/fonts/blob/main/tags/tags_ui_details.textproto

Inspected repository blob IDs: families.csv 7edab7f51736d23ac6cf268ff16787d53e081bbf (path/identity checked; only a limited row excerpt inspected), tags_metadata.csv ec2a2e908f9e770696e9f3a4427f3d0693aa820c, tags_ui_details.textproto 42d240c601a08b6e2acda7528c85967b49a87d64, tags/all/README.md f6e4589885a062b81bc61d33c936f4db3c172139. Do not claim a complete coverage audit or pin all excerpts to one revision yet.
