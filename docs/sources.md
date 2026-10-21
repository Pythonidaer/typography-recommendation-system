# Sources

These links are research starting points. Listing a source does not mean it has been fully reviewed or that its claims are our scoring rules.

## Current context

- Type Study organized notes and assessment idea:
  https://pythonidaer.github.io/typography-learning/choosing-type.html
- Writing profile:
  https://github.com/Pythonidaer/llm-instruction-toolkit/tree/main/design/content-and-tone

## Primary sources checked during planning, October 21, 2026

- Google Fonts About-content documentation:
  https://googlefonts.github.io/gf-guide/article.html
  Explains family About content and its source documentation.
- Google Fonts repository:
  https://github.com/google/fonts
  Starting point for family metadata, documentation, and licenses; individual families have not been researched here yet.
- Google’s font-selection guide:
  https://design.google/library/choosing-web-fonts-beginners-guide
  Project needs and text roles.
- Material Design typography:
  https://m3.material.io/styles/typography/overview
  Display, headline, title, body, and label roles.
- Modular Scale:
  https://www.modularscale.com/
  Generates related values from bases and ratios. Supports later size experiments, not personality scoring.

## Pairing and inspiration references

- https://www.behance.net/gallery/35768979/Typography-Google-Fonts-Combinations
- https://www.behance.net/gallery/41054815/Typography-Google-Fonts-Combinations-Volume-2

Both supplied by Johnny. Automated access returned 403 during planning. Their visual combinations have not been reviewed. Do not extract supposed pairings from their titles.

- https://www.typewolf.com/
- https://fontpair.co/
- https://typ.io/
- https://fonts.google.com/knowledge/choosing_type/pairing_typefaces

Starting points for examples and guidance. A first limited documentation comparison is now in existing-tools-review.md; the Fontpair body was unavailable.

## Pending research

Compare existing tools by their questions, inputs, font coverage, explanations, pairing behavior, and editable previews. Record direct observations with dates, limitations, and primary URLs. Distinguish catalogue filtering, curated pairing galleries, and preference-driven recommendations.

## Attribute evidence pass, October 21, 2026

Reviewed API tag documentation, metadata guidance, About-content guidance, tag-data README, tag dictionary, and UI mappings. A limited families.csv excerpt confirmed weighted expressive and typographic assignments and variant locations. Full coverage and calibration remain unreviewed.

- https://developers.google.com/fonts/docs/developer_api#tags
- https://googlefonts.github.io/gf-guide/metadata.html
- https://github.com/google/fonts/blob/main/tags/all/README.md
- https://github.com/google/fonts/blob/main/tags/all/families.csv
- https://github.com/google/fonts/blob/main/tags/tags_metadata.csv
- https://github.com/google/fonts/blob/main/tags/tags_ui_details.textproto

The tag-data README distinguishes human-assessed tags from machine-assessed measurements. Raw weights are not our preference-match scores. Detailed limitations and inspected blob identities are in attribute-evidence.md.

## Pinned source audit and first sample

On October 21, 2026, audited all families.csv rows at Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6 against its tag dictionary and UI mappings. Also inspected upstream tag tests, GF Tagger implementation, and https://googlefonts.github.io/gf-guide/tags.html for process context. Documentation describes relative human comparison within a tag; calibration against reader preference has not been established.

Metadata from that same revision seeded 5 partial family records. No font binaries, license terms, family About descriptions, or actual previews were reviewed in this batch. See source-audit.md for coverage denominators and limitations, and each family record for pinned evidence.

## Pilot documentation and character pass

Reviewed each pilot family’s pinned DESCRIPTION.en_us.html and OFL.txt and Noto Sans’s article/ARTICLE.en_us.html. Additional pinned upstream README checks and limitations are in pilot-source-review.md. Sources support intended-use attribution, not measured readability claims.

Inspected 1 normal binary per family using fontTools; hashes, source URLs, axis defaults, and sample strings are in research/source-audit/pilot-character-checks.json. This checks Unicode character mappings only. No visual, shaping, italic-file, or reader tests were completed.

## Mood vocabulary and comparison protocol, October 21, 2026

Reviewed the official Google Fonts tagging process and the authors’ full 2014 font-selection paper. The latter is a close precedent for attribute-specific comparisons and relative attribute estimation; it is not validation of our proposed vocabulary or four-option trial. Its substantial observed disagreement motivates preserving individual responses.

- https://googlefonts.github.io/gf-guide/tags.html
- https://www.dgp.toronto.edu/~donovan/font/fontSelection.pdf

Also reviewed the 2017 Arabic-typeface study abstract and study context as a reminder that script/population must be recorded. No claim of cross-cultural invariance is made:
https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01229/full

The MDPI emotion-based recommendation paper at https://www.mdpi.com/2076-3417/14/3/1123 returned 429; its methods have not been reviewed and do not support our protocol.

## Instance coverage, response format, and existing tools

The pinned pilot source rows were compared with the rendered axis settings. See missing-attribute-policy.md and research/source-audit/instance-trait-coverage.json. The 25 diagnostic checks are not coverage results for the proposed six-word vocabulary.

Reviewed Fontjoy’s main page and author explanation, and Adobe’s historical 2021 recommendation announcement, on October 21, 2026. Fontpair yielded a page title but no readable body. Exact URLs and review limits are in existing-tools-review.md.

The response schema uses JSON Schema draft 2020-12 conditional validation, documented at:
https://json-schema.org/understanding-json-schema/reference/conditionals
Structural checks do not validate psychological constructs or participant judgments.

## Broader attribute inventory and availability audit

On October 21, 2026, reread the official tagging-process guide and Developer API documentation. Reused the pinned families.csv and tag dictionary from revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6 after checking their SHA-256 hashes against the previous audit. All 20 expressive source labels are retained.

The 27 working candidate definitions are project proposals, not a validated taxonomy or provider definitions. The source-availability report compares unions and missing assignments without merging raw weights or filling unknowns. See attribute-inventory.md and attribute-coverage.md. No new font family, observed response, score, or recommendation eligibility was added.
