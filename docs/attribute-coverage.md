# Attribute source availability

Checked October 21, 2026 against Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6. Input file hashes match the earlier source audit. This is a count of source assignments, not a fairness result or approved mood coverage.

## Findings

| Source set | Distinct family names with at least one valid assignment | No assignment in that set |
| --- | ---: | ---: |
| Eight source tags previously considered for six moods | 1,922 | 19 |
| All 20 expressive source tags | 1,936 | 5 |

Denominator: 1,941 distinct exact family names in the pinned tag CSV. This is not the live catalogue count. The eight tags are Calm, Playful, Happy, Active, Excited, Sophisticated, Fancy, and Rugged. Related labels remain independent.

The large first number does not establish that the six words are sufficient: a family can have one tag at a low raw value, or at another weight, while lacking information for the requested impression. No family has assignments for all eight tags, but that alone is not evidence of inadequate design coverage either; those eight tags are not eight mandatory attributes. Missing and low are different states.

Adding every expressive source label finds an assignment for 14 more family names. It does not demonstrate that the other 1,922 were already adequately described. Some extra family names concern special-purpose fonts, so exclusion may sometimes follow a project’s purpose rather than a vocabulary problem. Do not infer the reason from a missing tag.

## Uneven availability

These counts include any valid source strength and any scope. They do not establish exact-style coverage, high association, consistency of ratings, or suitability.

| Source label | Families with a valid assignment, any scope |
| --- | ---: |
| Active | 514 |
| Artistic | 345 |
| Awkward | 1,120 |
| Business | 1,025 |
| Calm | 920 |
| Childlike | 490 |
| Competent | 885 |
| Cute | 487 |
| Excited | 520 |
| Fancy | 132 |
| Futuristic | 374 |
| Happy | 703 |
| Innovative | 244 |
| Loud | 1,429 |
| Playful | 1,044 |
| Rugged | 1,791 |
| Sincere | 1,162 |
| Sophisticated | 93 |
| Stiff | 854 |
| Vintage | 1,672 |

Eight invalid zero-valued rows from the earlier audit were excluded before counting. There are 2 affected family names, which can still have other valid assignments. Zero rows are not converted to absence of the underlying trait.

## The broader inventory

The report checks each proposed source relationship against the same five rendered instances. It retains one result per source tag and leaves all assessment scores null. A candidate without a proposed mapping has an empty source-check list, not a zero score. A matching provider word still needs interpretation, scope, and calibration review.

The report does not compute category or script parity. We do not yet have a checked catalogue-wide mapping of family names, styles, scripts, and practical eligibility. The pilot has one family per provider category and is not representative within those categories. It cannot establish equal opportunity for the roughly 2,000-family catalogue.

## Reproduce

Download families.csv from the pinned source URL in research/source-audit/google-fonts-tags.json, then run:

```sh
python scripts/audit_attribute_inventory.py /path/to/families.csv
python -m unittest discover -s scripts -p 'test_*.py'
```

The audit requires the original source hash. Its generated report is research/source-audit/attribute-inventory-coverage.json. It never turns counts or raw weights into a recommendation score.

## Decision

Keep the six-word proposal as historical preparation, not the scope of the recommendation system. Investigate the broader inventory and unsupported requests. The next useful check is whether people’s design intentions can be captured clearly; more tags alone will not answer it.

Sources:
https://raw.githubusercontent.com/google/fonts/45e3d5269e4a17d823f6d84470bc084dc5ae46f6/tags/all/families.csv
https://googlefonts.github.io/gf-guide/tags.html
https://developers.google.com/fonts/docs/developer_api#tags

The guide describes relative comparison within tags. The Developer API describes whole-designspace family tags; this audit uses the repository CSV, whose located and unlocated assignments require separate scope checks. No API query was made.
