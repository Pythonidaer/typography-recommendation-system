# Research checkpoint

Updated: October 21, 2026
Current stage: actual raster specimens prepared and visually inspected; no participant responses.

## Direction

Johnny delegated continued creation. Continue independent preparation without repeatedly asking them to reconfirm the framework. Purpose, legibility, and readability remain core; mood/harmony and hierarchy support purpose. Mood words and scoring remain provisional.

## Completed this pass

- Rendered the 5 pinned normal font instances in heading, paragraph, and character sheets.
- Added scripts/render_pilot_specimens.py, a reproducible specimen manifest, image assets, text alternatives, sample key, and QA record.
- Verified source-file hashes, sample character mappings, explicit variable axes, valid images, and sample bounds.
- Visually inspected all 3 final sheets: all 5 samples present, no observed clipping or missing-glyph boxes.
- Recorded actual line wraps and nominal-size differences without converting them to suitability or mood scores.
- Existing audit unit tests pass.
- Prepared and verified a 5-trial four-option schedule with equal sample and position exposure. Attribute, role, and participant remain unassigned; no trials have run.

## Artifacts

research/specimens/batch-1/README.md
research/specimens/batch-1/manifest.json
research/specimens/batch-1/review.json
docs/specimen-preparation.md

The manifest contains source hashes, actual sample text, settings, line breaks, rendering versions, and the numbered key. Font binaries are not committed.

## Important visual observation

Equal nominal size produced noticeably different apparent text sizes and line wraps. Preserve this as a research-condition issue, not a readability conclusion. A separate matched-perceived-size condition may be needed; do not silently modify the original specimens.

## Exact next work

Use these concrete specimens when discussing mood words and comparison instructions. Keep raw attribute association, personal preference, and reading task observations separate. The user asked to establish mood vocabulary before mood tests; no votes have been collected and no vocabulary is approved.

Independent work can refine the response-record format and investigate missing traits. A balanced trial schedule is already prepared in research/protocols/four-option-schedule.json. Any schedule must remain a proposed research artifact until fonts, wording, and presentation conditions are checked. Do not add more families, infer ratings from names, or begin product UI.

## Active sample

Noto Sans, Merriweather, Roboto Mono, Caveat, Abril Fatface. All remain needs_review and recommendation_eligible=false. No new scores, human responses, or pairing claims were created.

## Verification boundaries

Raster image generation and inspection are complete for these samples. Browser rendering, mobile enlargement, actual character recognition, reading comfort/comprehension, hierarchy, contextual harmony, and mood judgments remain untested.

## Deferred

Participant feedback, source-score calibration, pairing research, competitor comparison, system-font expansion, product UI, and framework selection remain pending.
