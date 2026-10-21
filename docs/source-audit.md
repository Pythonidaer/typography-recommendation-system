# Google Fonts tag-source audit

Checked October 21, 2026. Upstream revision: 45e3d5269e4a17d823f6d84470bc084dc5ae46f6.

## Decision

There is enough traceable data to begin a small category-spanning research sample and prototype mood questions. There is not enough evidence to claim universal reading suitability, validated personality scores, or pairing quality.

The source does not supply a complete heading/body suitability matrix. Use family documentation and later preview tests for those roles.

## Coverage

The pinned families.csv contains **34,163 rows, 1,941 exact family names, and 74 distinct tags**. These counts describe the file, not the entire live Google Fonts catalogue. No live catalogue join or release/alias audit has been completed.

**1,936 names have at least 1 expressive tag.** Individual traits are sparse. A missing trait is unknown, not zero. A font with a very small value still counts as having an assignment in the table below; these are coverage counts, not counts of strong examples.

| Source label | Families with any assignment | Families with an unlocated assignment |
| --- | ---: | ---: |
| Calm | 920 | 429 |
| Loud | 1,429 | 1,151 |
| Playful | 1,044 | 706 |
| Vintage | 1,672 | 1,491 |
| Business | 1,025 | 641 |
| Easy Reading | 14 | 13 |
| Learn To Write | 125 | 125 |

There are 22,533 unlocated rows and 11,630 location-specific rows across 538 families. These groups overlap. Preserve both forms and axis coordinates. Do not collapse scores across weights or widths.

## What the source weights mean

The official tagging guide describes human comparison within a tag category. It provides an onboarding and review process, rather than a psychometric calibration or experimental measure of reader response. Existing strengths can support exploratory ranking; they cannot be displayed as a probability of preference or quality.

The developer API documents FAMILY_TAGS as tags applying across an entire family designspace. CSV instance rows contain more specific coordinates. We have not tested API responses, so blank CSV locations must remain “unlocated source assignment,” not be relabeled “guaranteed across all variants.”

## Data-quality findings

- No malformed 4-column rows, duplicate family/location/tag keys, or unknown tag-definition keys were found.
- Eight rows have zero weights, outside the upstream test’s accepted 1-100 interval: 4 Datatype Cute assignments and 4 Linefont Cute assignments. Quarantine these from ranking. Keep the original rows and reason in an import log; do not silently convert them to missing or valid values. The tagger uses zero for placeholders, but that does not prove why these rows are present.
- UI mapping /Script/Upright differs from the dictionary/data /Script/Upright Script. Flag for an explicit reviewed mapping; no automatic alias was applied.
- UI technology tags have no exact entries in this dictionary/data. They may be derived elsewhere; absence here is not proof of an error.
- /Display/Display is defined but absent from this file. Use family metadata to sample Display. Serif, slab, script, and theme tags can overlap broad categories.
- Quality tags cover nearly all listed names. Coverage does not justify using them as a user-facing quality score. Keep them outside the initial mood ranking.

## Minimum evidence now

For the sample: exact family identity, verified broad category, traceable metadata, available raw tags and scope, and documented gaps. For recommendation trials: verify required styles, characters, permission, intended role, and the dimensions actually used in ranking. Review complete combinations separately.

## Reproduce

Download the 3 files at the pinned revision, then run:

```sh
python scripts/audit_font_tags.py families.csv tags_metadata.csv tags_ui_details.textproto research/source-audit/google-fonts-tags.json
```

The script stores SHA-256 hashes. Canonical source paths and hashes allow the output to be compared even when local input filenames differ. The report intentionally does not vendor the full upstream dataset. It checks syntax, counts, scope, ranges, and exact tag names; it does not validate complete variable-axis interpolation grids, real font files, or the truth of human labels.

## Sources

- https://github.com/google/fonts/blob/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/tags/all/families.csv
- https://github.com/google/fonts/blob/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/tags/tags_metadata.csv
- https://github.com/google/fonts/blob/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/tags/tags_ui_details.textproto
- https://github.com/google/fonts/blob/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/tags/all/README.md
- https://github.com/google/fonts/blob/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/.ci/test_font_tags.py
- https://github.com/google/fonts/blob/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/.ci/tags.html
- https://googlefonts.github.io/gf-guide/tags.html (live documentation reviewed October 21, 2026)
- https://developers.google.com/fonts/docs/developer_api#tags (live documentation reviewed October 21, 2026)

The code and data are pinned; the external documentation is dated, not pinned. Its recommendation of 2-6 onboarding tags does not describe the current data’s full row count, which includes collection-wide additions and instance rows.
