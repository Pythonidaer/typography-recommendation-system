# Pilot sample: batch 1

Status: documentation and license sources reviewed; limited character mapping checked; visual and suitability review pending. This is a sample to test our method, not recommended fonts for a user’s project.

The source audit supports beginning an exploratory sample. We selected 1 family in each of the 5 broad provider categories, verified using METADATA.pb at revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6:

| Family | Provider category | Record |
| --- | --- | --- |
| Noto Sans | Sans serif | ../research/fonts/notosans.json |
| Merriweather | Serif | ../research/fonts/merriweather.json |
| Roboto Mono | Monospace | ../research/fonts/robotomono.json |
| Caveat | Handwriting | ../research/fonts/caveat.json |
| Abril Fatface | Display | ../research/fonts/abrilfatface.json |

This small batch checks whether the record format can represent category differences, variable and static families, and different styles. It does not represent all styles within each category or the full catalogue. Later batches can add within-category diversity and overlapping slab, script, and blackletter traits after this batch is reviewed.

Abril Fatface’s metadata also identifies a serif stroke, illustrating why Display and Serif need not be mutually exclusive. Keep the provider category separately from overlapping tags.

## Collected

Exact identities and categories, styles, weight ranges or static weights, axes, declared subsets, license identifiers, raw non-quality tags, source URLs, pinned revision, and evidence references.

Subsets are provider screening labels, not a full verified character inventory. Variable weight ranges come from the axis range, rather than incorrectly reading the per-file 400 entry as the only available weight. License identifiers are metadata claims; terms have not been reviewed.

## Current review stage

See pilot-source-review.md for documentation findings and source gaps. All 5 records are now needs_review and recommendation_eligible=false. Intended uses are attributed source claims; no personality judgments or pairing recommendations have been created.

Before recommendation trials, test selected variants and actual content, review missing attribute evidence, and check a real project’s character and reading needs. This batch does not yet support a comparable ranking on all 5 proposed mood dimensions.
