# Research checkpoint

Updated: October 21, 2026
Current stage: batch 1 source review and limited character checks complete; visual/attribute review next.

## Completed

- Source coverage audit at upstream Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6.
- 5 category-spanning family records, now marked needs_review and ineligible for recommendations.
- Read each pinned provider description and family OFL.txt; read Noto Sans’s longer About article.
- Recorded attributed intended uses, license source details, exact document blobs, source shortcomings, and scope boundaries.
- Inspected 1 normal binary per family. Printable ASCII and 3 documented example strings map in all 5; report preserves hashes and axes.
- Compared availability of the 5 proposed mood traits. Only Roboto Mono has source assignments for all 5; unknowns remain unknown.

## Active batch (do not expand)

Noto Sans, Merriweather, Roboto Mono, Caveat, Abril Fatface. Records: research/fonts/<id>.json. See docs/pilot-source-review.md.

No personality judgments, combined scores, pairing recommendations, or validated recommendations exist.

## Exact next task

Prepare a bounded research comparison protocol for these 5 families with identical content and explicit variants. Separate heading and body settings. Define what each proposed question is intended to measure and prepare concrete examples for Johnny’s feedback. No UI implementation or new family batch is needed yet.

Account for source-location differences; do not interpolate scores or turn unlocated assignments into full-family guarantees. Resolve how missing traits will be reviewed or excluded before any combined ranking.

## Validation

All updated JSON records parse and retain resolvable evidence references. Intended uses remain source_stated. Licenses have dated, pinned evidence. The character-check script records exact source-file hashes and limits its claims to cmap presence. Existing audit tests pass. No browser, visual, shaping, or reader verification has been done.

## Findings to preserve

Caveat has explicit body-text intent despite being handwriting. Abril Fatface is not the complete Abril family. Noto Sans is not the entire Noto collection. Merriweather’s pinned upstream README is unfilled template text. Raw trait coverage is too uneven for a combined 5-trait ranking of this batch.

## User input

No decision is needed for the completed source review. Bring Johnny concrete examples when choosing wording and evaluating appearance; do not ask them to resolve metadata or source-discovery work.

## Deferred

Behance access, competitor comparison, pairing research, system-font expansion, score calibration, UI design, and framework selection remain pending. The earlier arbitrary sample queue remains superseded.
