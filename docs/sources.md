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

Starting points for examples and guidance. They are not yet a reviewed comparison of competing recommendation products.

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
