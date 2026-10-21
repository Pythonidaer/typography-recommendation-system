# Font walkthrough pilot

Version: editorial-pilot-0.4. Updated October 21, 2026. The public test destination is this repository’s GitHub Pages site.

## Current scope

The experimental pool contains 80 distinct families, expanded from 8. The pinned Google Fonts repository snapshot contains 2,040 family metadata directories under ofl, apache, and ufl. This is a reproducible repository count, not the current web catalogue total or evidence that the pilot represents every style or language fairly. See research/source-audit/pilot-catalogue-snapshot.json.

Four steps collect project purpose, reading length, languages and role scope, exact 1-3-family count, optional text, heading type, lettering association, and independent retro/rough preferences. The third family requires an explicit purpose. Results show characters before explanations, in-slot replacements, optional custom text, feedback, and downloadable JSON notes. No color, weight, size, texture, or motion controls are added.

The reading question uses concrete examples: titles/navigation/buttons/captions; short project or product descriptions; and sustained articles/guides/stories/case studies. The ambiguous optional reading-help checklist is removed. Old draft fields remain readable for continuity, but the checklist is no longer shown or used in ranking. Purpose, written goal, and reading length provide context for evaluation; this version does not interpret them semantically or assign reading-performance scores.

## Source records and review boundaries

research/pilot-catalog.json is the manifest. Each included family has a separate editorial_pilot section in research/fonts/<stable-id>.json. The original five-family records and their recommendation_eligible=false research status remain intact. Separate editorial comparison eligibility does not approve their mood scores or reading performance.

Review proceeded in batches of at most 5, checkpointed before expansion. Family identity, provider categories, metadata subsets, and selected normal-file names were read at the pinned revision. Available descriptions were read and briefly paraphrased. Missing descriptions for Bungee and Space Mono remain explicit; their verified metadata is retained without inventing stylistic or intended-use claims. Descriptions are not copied into the repository. Hashes, URLs, reviewer, date, and review scope accompany each record.

Body/all-text eligibility is a bounded shortlist, not a verdict about other fonts. Most candidates have a source describing text or interface use; Noto Sans JP is explicitly marked as an editorial proposal based on script coverage rather than a designer-stated body-text recommendation. Unknown roles remain unknown. Headings and accents are proposed visual comparisons, not validated suitability. Source-linked lettering associations are editorial mappings, not necessarily the provider’s exact labels.

Every family has null mood_scores, reading_performance, and pairing_scores in its generated pilot record. No trained model, match percentages, user-study results, or catalogue-wide recommendation accuracy is claimed.

## Transparent editorial rules

site/engine.js is the executable source of truth. site/data.html, linked from the top-right “Font data” link, displays all 80 records, the current brief’s eligibility and points, source links, character counts, equal Latin-letter width checks, and missing metrics. The neutral-table control does not change the assessment draft. Search and broad category filters aid inspection.

1. Filter by required scripts and exact supplied-text character mapping. Supporting-text slots also require shortlist membership. Missing file coverage fails the requirement.
2. Supporting-text shortlist membership adds 12 points to body/all-text roles.
3. The requested heading type adds 30 points to heading/all-text roles. Provider categories may overlap; monospace also uses the measured equal-width Latin-letter property.
4. A matching lettering association adds 20 points to heading/accent roles and 6 to body/all-text roles. A contrasting accent skips the main association bonus.
5. Retro preference adds 2 points per slider step for documented print, digital, retro, or typewriter associations. Rough preference adds 2 per step to headings and 5 to accents for rough associations. A contrasting rough accent gains 20 more points only when rough preference is above zero.
6. Ties sort by family name. All selections remain unique, with exactly the requested count when requirements can be met. Replacements preserve the same slot’s requirements and total count.

Version 0.3 removes the prior hardcoded per-family defaults and Japanese body preference. Points describe our provisional sorting rules, not measured font attributes or confidence. Type is a preference, not a hard requirement: if language and role constraints prevent a match, the explanation makes that gap explicit. No automatic pairing optimizer or scene-specific mood model is present.

## Language and defaults

Main and optional additional language dropdowns offer English, Japanese, and Thai. Other languages receive an explicit current-pool limitation. Selecting an additional language requires a choice of main-heading-only or throughout usage. Actual text is checked without translation. Text applies to the roles using that additional language, or to all roles if there is none. Subset labels do not guarantee every character, shaping, or regional form.

Fresh assessments have no project or family count selected, no additional language, no heading-type or lettering-association preference, and zero retro/rough priorities. English is the initial main language. The portfolio demo button alone fills its example brief. Existing 0.1/0.2 drafts migrate to the general fields. Japanese-capable selected families show kana, and Thai-capable selected families show Thai letters, regardless of assigned role.

There are now 3 Japanese-capable families, enabling 3 unique bilingual slots in this limited pool. Only Chakra Petch supplies Thai in this pool, and it is not on the supporting-text shortlist. Unsupported combinations stop with a clear limitation.

## Build and verification

Run python -m pip install fonttools==4.61.1, python scripts/build_pilot_site.py, and node scripts/test-pilot.cjs. Serve site/ with a static server for local testing. GitHub Actions repeats the build and checks before deployment.

The build downloads source files from Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6, instantiates fixed reference styles with weight 400 where available and default remaining axes, includes licenses, computes exact cmap ranges, counts mapped characters, and checks whether A-Z and a-z share one advance width. It generates ignored assets including catalog.js, fonts.css, coverage.json, and font-sources.json. Font files load on demand through CSS; the full pool is not preloaded. All paths work under the repository Pages subpath.

Automated checks cover 80 unique records, pinned evidence, unknown metric preservation, broad type preferences, script/text constraints, exact counts, replacements, legacy migration, and agreement between displayed rule breakdowns and ranking totals. These are software/source checks, not reader, mood, or pairing validation. Browser verification must be reported separately.

Drafts and feedback stay in browser storage; exports are downloaded locally. No analytics or feedback transmission is implemented. Personal test exports and participant wording are not copied into the public repository.

## Visual assessment correction 0.4

Shape choices now lead with ordinary descriptions and actual neutral-character specimens. Technical terms remain secondary. Each group has two named examples where available; these illustrate variation and are not recommendations or a complete taxonomy. All examples use the same character sequence and fixed reference settings. Samples remain hidden until their actual font files load, with a visible error instead of a fallback-font preview on failure.

Lettering looks distinguish older screens/games, books/articles, posters/advertising, simple geometric construction, typewriting, handwriting, and stencils. Poster associations for Abril Fatface, Anton, and Righteous were reviewed as one bounded batch against their existing pinned source descriptions. A short disclosure explains that print also covers newspapers, magazines, signs, and other traditions; unrepresented distinctions remain an explicit limitation. No mood scores or new families were introduced.

One-family assessments require a use choice: titles/short labels only, or titles plus supporting text. The first uses the heading pool; the second retains the supporting-text restriction. Older drafts that lack this field retain the all-text interpretation and show it in the assessment and review. The software does not change language requirements to manufacture a visual match. It shows sole-candidate and unmet-shape/look warnings before results and on results.

The 80-family pool still has only 3 Japanese-capable families and one Japanese candidate on its supporting-text shortlist. A one-family bilingual request for all text therefore has only that candidate, even when the visual preferences are different. A title-only request can compare the 3 heading candidates. This is a pool/role limitation, not evidence that the remaining family is the best stylistic choice.

Optional local rebuild: python scripts/build_pilot_site.py --reuse-font-files. Reuse requires the exact pinned source URL and verified generated-file and license hashes from the previous local manifest. It recomputes character checks and regenerates the catalog from current records. CI continues to build from source without this option.
