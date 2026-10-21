# Font walkthrough pilot

Version: editorial-pilot-0.2. Created October 21, 2026 at the user’s request for an immediately testable sequential walkthrough. The public test destination is this repository’s GitHub Pages site. The earlier ChatGPT-hosted preview was a temporary prototype.

## Scope

Four steps collect purpose, reading task, a main language and optional additional language with role scope, 1-3-family count, optional known needs, a visual direction, two preference sliders, and a purpose for a third family. The review step allows correction before results. Results show exactly the requested number when the pool can meet requirements, characters before reasons, in-slot replacements, optional user text, feedback, and a JSON download. No color, weight, size, texture, or motion controls.

Eight editorial candidates are available. These are not the five researched JSON pilot records from the project repository, and their inclusion does not change those records’ recommendation eligibility. No calibrated mood ratings, measured reading scores, learned model, or catalogue-wide accuracy is claimed.

## Rules and their meaning

engine.js is the executable source of truth. Its weights are unvalidated editorial tie-breaking priorities, not personality measurements or match probabilities. Version changes require count, script, and replacement regression checks in scripts/test-pilot.cjs.

1. Restrict slots by required scripts and exact supplied-text character coverage. Restrict supporting-text slots to the editorial body-text shortlist. Unknown coverage does not pass.
2. A source-linked style association matching the chosen main direction adds 20 priority units to a display slot. Retro emphasis adds 2 units per step to earlier-print or digital associations. Rough emphasis adds 2 per step to headings or 5 to accent slots for typewriter, marker, or stencil associations.
3. A contrasting third-family slot does not repeat the main-direction bonus; rough candidates receive 20 additional units only when rough emphasis is above zero. This is an editorial heuristic, not evidence of pairing quality.
4. Supporting-text defaults favour IBM Plex Sans; Japanese requirements favour Noto Sans JP only in supporting-text roles that require Japanese. Editorial direction can favour Merriweather. DotGothic16 has a small Japanese display preference. All tie breaks are deterministic.
5. Keep all selected families unique. Replacements must meet the same slot requirements and preserve the family count. There are only 2 Japanese-capable families; a request for 3 bilingual-throughout roles returns an explicit pool limitation, not a padded result.

Reading-needs answers are retained for follow-up evaluation, not automatically converted into font ratings. Purpose and open text provide the brief and proposed roles, not semantic AI matching. This prototype does not fully model multiple scene moods. The rough-lettering priority plus contrasting-heading role provides one limited exploration of that request.

## Sources and assets

Source About descriptions were read from Google Fonts for Chakra Petch, IBM Plex Sans, Special Elite, Rock Salt, Black Ops One, DotGothic16, and Noto Sans JP. Merriweather’s intended screen-text purpose and pinned binary were already researched in the earlier pilot. Each family links its primary design notes in the result.

New Japanese files were fetched from google/fonts on October 21, 2026. Noto Sans JP was instantiated at weight 400. Merriweather was instantiated at weight 400 and its remaining default axes. Font sizes and weights are reference conditions, not user styling decisions. Source licenses are included and linked. assets/coverage.json records exact shipped-file hashes and compressed cmap ranges for all candidates. Character-map coverage does not establish correct shaping, regional form suitability, reading comfort, or pairing quality.

English and Japanese heading example was checked in the browser. All 3 selected typefaces loaded, including actual kana. Count, unique-family, unsupported-text, Japanese-throughout failure, and replacement constraints passed automated checks. This is not participant feedback. User-entered draft data stays in browser storage; feedback can be downloaded. No analytics or feedback transmission is implemented.

## GitHub Pages build

The source is site/. Run python -m pip install fonttools==4.61.1, then python scripts/build_pilot_site.py and node scripts/test-pilot.cjs. Serve site/ with a static file server for local testing. All paths are relative so the repository subpath works. GitHub Actions repeats the build and checks before uploading site/ to Pages.

The build downloads regular source files from Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6, locks variable axes to their defaults except weight 400, includes licenses, and generates fonts.css, coverage.json, and a source-hash manifest. The reference font settings remain fixed. Generated assets are not checked into the source repository.

## Pilot correction 0.1.1

Japanese-capable selected families show kana in their character review regardless of assigned role. Script requirements still apply by role. A heading-only Japanese requirement no longer adds a preference to the body slot. The optional Japanese-text field explicitly checks supplied characters without translating English; Latin-only entries receive a correction message. Question labels use plainer wording and explain family count. Slider and count values remain numbers after change events and draft restoration.

Regression checks cover heading-only ranking, Japanese replacement eligibility and specimen display, mixed-script input, blank input, and restored numeric values. These fixes do not establish recommendation quality or reading performance.

## General assessment 0.2

The default assessment has no project, family count, retro priority, rough priority, or additional language selected. English is the initial main language; language dropdowns offer English, Japanese, Thai, and an explicitly unsupported other-language option. Additional-language scope is asked only after one is selected and requires an explicit choice. Unsupported languages and unavailable combinations receive a clear limitation rather than Latin-only recommendations presented as suitable. This is a small script-based pool, not a validated multilingual language catalogue.

The portfolio example button alone fills the English-plus-Japanese brief. Optional text checking uses a general label, accepts the actual supplied text without translation, and checks the roles where the additional language is used (or all roles when there is no additional language). This supersedes the Japanese-specific input restriction in correction 0.1.1. English text in a mixed-language design is allowed; supplied text is not treated as proof of language suitability. Existing 0.1 drafts migrate to the new language fields. Japanese-capable families show kana and Thai-capable families show Thai letters regardless of role.

Run scripts/test-pilot.cjs for primary/additional language scope, legacy-draft migration, heading-only ranking, unsupported language and role combinations, exact family counts, and supplied character checks. Reading needs and free-text purpose remain context for testing rather than learned recommendation inputs.
