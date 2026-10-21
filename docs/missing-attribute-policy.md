# Missing attribute evidence

Status: proposed policy. Purpose, legibility, and readability remain the core checks. A documented mood association cannot compensate for a failed project requirement.

## Evidence must match the sample

A family-level tag does not necessarily describe every weight, width, optical size, or style. The current audit compares source tag coordinates with the exact instances used in the specimen manifest.

| Audit status | Meaning | Proposed handling |
| --- | --- | --- |
| Exact coordinates found | A source row lists all selected axis coordinates | Retain as a source assignment; review tag meaning and calibration before use |
| Partial coordinates need scope review | Listed coordinates match, but other selected axes are unspecified | Keep scope unresolved |
| Unlocated assignment needs scope review | A row has no explicit coordinates | Do not assume it describes the whole design space |
| Only other coordinates found | Located rows describe different settings | Do not transfer their values to this sample |
| Missing | No assignment for this family and tag was found | Preserve unknown; do not substitute zero |

The five-family diagnostic audit contains 25 checks: 3 exact-coordinate assignments, 6 unlocated assignments needing scope review, 9 checks with only other coordinates, and 7 missing assignments. These counts concern the older diagnostic traits Calm, Loud, Playful, Vintage, and Business. They do not establish coverage for the six proposed mood words.

Run `python scripts/report_instance_trait_coverage.py` to reproduce `research/source-audit/instance-trait-coverage.json`. An exact coordinate match establishes neither a validated mood judgment nor a preference-match score. No calibrated scores are produced.

## What to do with gaps

1. Preserve the provider row, raw value, source revision, and scope separately from local judgments.
2. Look for designer documentation relevant to the selected style and role. Stated intent remains an attribution, not a measured result.
3. If the attribute matters to the project and evidence remains insufficient, collect a reviewed comparison for that instance under a documented condition. Do not infer a label from its name or category.
4. If there is still no comparable evidence, say the mood fit is uncertain. Show an unscored alternative or ask for a visual preference comparison when that interaction exists.

Do not interpolate between source weights without a validated method. Do not convert absent Calm into Loud, or an absent trait into an average rating. Google tag values, reviewer impressions, reading performance, and project preferences belong to different evidence types.

## Ranking proposal

Apply confirmed practical requirements first, including required characters, available styles, and assigned text roles. Keep unverified requirements visible. Any later mood ranking should compare compatible evidence under a versioned method and report its limits.

A font with more documentation should not automatically win over a font with missing mood evidence. If too few candidates have comparable information, report that the mood ranking is incomplete rather than claiming an overall best match. A numerical coverage ratio is not a quality score.

All five pilot families remain ineligible for recommendations pending review. This policy adds no recommendation engine, mood ratings, or approved vocabulary.
