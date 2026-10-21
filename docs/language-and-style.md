# Language, historical styles, and lettering associations

Status: requirement clarification and proposed organisation. Updated October 21, 2026. No new family, Japanese companion, source mapping, or numerical score has been approved.

## Language is a practical requirement

Ask which languages the design must display, which roles use each language, and whether the text is bilingual in the same view or appears in separate language versions. Request actual text when available. Preserve unknowns when the wording or scope has not been supplied.

English usually uses Latin letters. Japanese can require hiragana, katakana, kanji, and punctuation, often alongside Latin characters and numbers. Language and writing system are related but different fields; a broad script label does not prove support for every character in a project.

Google Fonts exposes script/subset metadata. Use it for discovery, then check the exact files and actual text, confirm rendering and the intended regional forms, and review language-specific composition. A broad CJK label alone is not verification of Japanese suitability. Character-map presence is not proof of correct rendering, reading comfort, or a good pairing. Do not let an automatic fallback appear to demonstrate that the selected family contains Japanese characters.

The current private preview only loads and reviews the English/basic Latin samples. It does not establish Japanese coverage or suitability for any of the displayed families. The earlier editorial shortlist needs language review before it can serve a bilingual project.

## Current example

Japanese is required for the main heading. The user has not requested Japanese for navigation or supporting paragraphs. Scope the Japanese character and pairing checks to that heading before choosing a companion; the requested total remains 3 families. No new Japanese family or bilingual pairing has been selected or validated.

## Japanese and the family budget

Return the requested number of families, from 1 to 3. If a single family supports the required scripts and fits the assigned roles, it can serve more than one language. If a separate Japanese family is needed, count it as a family in the same budget. A companion for another script is not automatically a free extra family.

For a request for 3 families, an English display family, a Japanese companion, and a shared supporting family could occupy all 3 slots. That is an example allocation, not a selected combination. We may instead need families that handle more than one role or script. Do not silently add a fourth family or force an unsuitable result to satisfy a count. Explain any unresolved conflict between requirements.

Show only the requested families as the recommendation. Additional candidates belong in an explicitly separate replacement flow; replacing one preserves the count. The same rule applies to the character review, explanation list, and user-entered sample text.

Language matching requires more than finding similar shapes: review the actual text, assigned roles, apparent balance, character coverage, and contextual harmony. A cross-script companion need not copy Latin shapes exactly. Script-appropriate conventions and reading needs take priority over a superficial resemblance.

## Keep classification separate from mood

| Layer | Examples | How it helps |
| --- | --- | --- |
| Language and writing system | Japanese, English; kana, kanji, Latin | Establish the required coverage for each text role |
| Structural classification | Serif, sans serif, monospace, script | Describe construction or spacing; categories can overlap |
| Lettering association | Handwritten, brush, typewriter, stencil | Describe a visible relationship to tools or production methods |
| Historical or cultural style association | Art Deco, 1990s grunge, retro digital | Narrow a requested visual reference or period |
| Documented origin | Original release date, designer, earlier typeface being revived | Supply historical facts when reliable sources establish them |
| Mood or perceived character | Calm, playful, ominous, energetic | Describe the impression people associate with a rendered sample |
| Text role and reading task | Heading, paragraph, navigation, code | Guide intended-use research and contextual tests |

This is project organisation, not a universal typography taxonomy. Preserve source categories and local interpretations separately. A family may have several relevant descriptors.

A modern typeface can imitate a typewriter or revive a much older print design. Its release date, the age of its inspiration, and the style it evokes must be recorded separately. Do not infer pre-web origin merely from appearance. A font associated with handwriting is not automatically playful; a typewriter association is not automatically ominous; an old design is not automatically unsuitable for screens.

Geometric sans, handwritten script, period references, and moods should not be forced into a single mutually exclusive menu. Use them as separate layers with optional multiple selections. Broad styles such as “retro” need an example or a follow-up about the intended period.

## Assessment order

Start with purpose, reading needs, required languages, and requested family count. Identify roles and which scripts appear in each role. Then explore structural preferences, lettering associations, period references, and desired impressions as needed. Review actual character samples before word examples or interpretive explanations. Choose the families before final colour, weight, size, texture, or motion decisions.

Use concrete visual comparisons where a term is unfamiliar. Permit no preference and requests outside the inventory. Do not turn a style association into a mandatory exclusion unless the person explicitly makes it a requirement. Mood evidence never compensates for missing required characters.

## Sources and limits

Reviewed October 21, 2026:

https://developers.google.com/fonts/docs/developer_api

The API documentation supplies script/subset metadata and category filtering. This supports a metadata discovery step, not proof of every language, character, rendering condition, or recommendation.

The grouping, family-budget rules, and assessment sequence above are project decisions and proposals. No live API query, Japanese binary inspection, Japanese specimen rendering, or cross-script pairing test was performed in this pass.
