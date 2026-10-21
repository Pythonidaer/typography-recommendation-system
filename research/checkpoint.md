# Research checkpoint

Updated: October 21, 2026
Current stage: source audit complete; batch 1 metadata collected, review pending.

## Completed this pass

- Pinned Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6.
- Audited 34,163 tag rows, 1,941 exact family names, and 74 tags. These are file counts, not complete live catalogue coverage.
- Recorded per-tag coverage, locations, 8 out-of-range zero rows, and exact UI/data name differences.
- Read official tagging-process guidance: source values rank human assessments within a tag; they are not calibrated preference probabilities.
- Added a reproducible audit script and JSON report with source hashes.
- Proposed 5 independent questionnaire dimensions in docs/assessment-dimensions.md.
- Created 5 partial font-family records spanning provider categories.

## Active batch: 1 (do not expand yet)

| Record | Category | State |
| --- | --- | --- |
| research/fonts/notosans.json | Sans serif | Metadata and raw tags collected |
| research/fonts/merriweather.json | Serif | Metadata and raw tags collected |
| research/fonts/robotomono.json | Monospace | Metadata and raw tags collected |
| research/fonts/caveat.json | Handwriting | Metadata and raw tags collected |
| research/fonts/abrilfatface.json | Display | Metadata and raw tags collected |

All are in_progress and recommendation_eligible=false. No judgments or recommendations have been generated. The original arbitrary named queue remains superseded.

## Exact next task

Start with Noto Sans. Discover and read its About/designer documentation and actual license at the pinned revision. Record short attributed intended-use claims, remaining gaps, and evidence. Then repeat for the remaining 4 families in this batch. Do not create a new batch until reviewing these records.

After source review, prepare comparable text examples for the 5 candidate mood questions, checking variant scope. Ask Johnny to judge wording or visual preferences when concrete choices are ready. No user input is currently required for source research.

## Validation

Audit parsed all rows and detected upstream zero-weight exceptions; it found no duplicate family/location/tag keys or malformed axis-location strings. A synthetic fixture checked malformed-row, duplicate, range, and scope detection. All 5 JSON records passed identity, evidence-reference, raw-value-range, no-invented-judgment, and ineligible-status checks. No rendered or reader testing took place.

## Remaining uncertainties

Blank CSV location scope is not guaranteed equivalent to API full-designspace scope. No live API call or catalogue identity join was made. Detailed semantic anchors and repeatability of source scores remain unverified. Purpose-tag coverage is sparse; intended text roles need more evidence. Display is absent as a tag in this file and must be obtained from family metadata.

## Resume instructions

Read AGENTS.md, docs/source-audit.md, docs/pilot-sample.md, and the active record. Preserve raw provider assignments, our judgments, and user preferences separately. Update this checkpoint with exact source paths and next action in every research session.

## Deferred

Behance examples remain unreviewed after 403. Competitor comparison, pairing research, system-font expansion, scoring calibration, UI design, and framework choices remain pending.
