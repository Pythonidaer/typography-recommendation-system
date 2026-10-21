# Pilot sample: batch 1

Status: inventory and metadata collected; research incomplete. This is a sample to test our method, not recommended fonts for a user’s project.

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

## Remaining before recommendation trials

Read About/designer descriptions and actual licenses; evaluate intended roles and character requirements; review source attributes in context; test actual previews. All 5 records remain in_progress and recommendation_eligible=false.

No numeric judgments or pairing recommendations were generated. The next batch is blocked on reviewing these records, not on collecting more fonts.
