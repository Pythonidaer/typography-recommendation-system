# Recording attribute comparisons

Status: draft research format, version 0.1. No participant responses have been collected. The six mood words and their definitions still need review before an observed comparison session.

This format records which displayed sample best communicates one attribute. It does not record a favorite font, overall project suitability, a reading result, or a numerical mood score. Those need separate records and analysis.

The version 0.1 schema still enumerates only the historical six mood IDs. It is not a collector for the version 0.2 candidate inventory. Do not submit new candidates under a nearest old ID. Approve definitions and version the schema explicitly before expanding observed comparison collection.

## What a session records

A session covers one participant, attribute definition, text role, and presentation condition. Each response preserves the actual displayed order, selected instance or non-selection outcome, timestamp, and specimen manifest hash. Use a pseudonymous participant ID, without a name or contact information.

The proposed four-option schedule has five trials. A response may be `selected_option`, `none_fit`, `too_similar`, or `skip`. Only a selected option has a selected instance ID. Non-selections remain distinct; they are not zero ratings. The three unchosen samples are not ranked, and one winner does not become three independent pairwise votes.

Keep human and AI responses separate. An AI response requires the model ID, prompt hash, and visual-input hash; this provenance does not establish reliability or make an AI judgment equivalent to a participant response. Save the referenced prompt and visual input with access appropriate to the study. A hash alone cannot reconstruct either artifact. Do not pool AI and human responses by default.

`research/observations/attribute-responses.json` is intentionally empty. Synthetic fixtures exist only in unit tests and are rejected by the normal validator.

## Validation

Install research dependencies with `python -m pip install -r requirements-research.txt`, then run:

```sh
python scripts/validate_comparison_responses.py research/observations/attribute-responses.json
python -m unittest discover -s scripts -p 'test_*.py'
```

The schema in `research/schemas/attribute-response.schema.json` rejects unexpected score fields and malformed records. The validator also checks scheduled options, displayed selections, duplicate IDs and trials, consistent session metadata, timezone-bearing timestamps, and the current specimen manifest hash. Corrections must replace or version a prior response, not enter as an extra vote.

An observed record must declare a reviewed definition and verified presentation. Validation checks that these declarations exist; it cannot establish that a review happened, that a person saw the sample correctly, or that a judgment is valid. Reviewers must check the actual definition version and presentation before collecting observations. A passing check on an empty dataset means no invalid records were found, not that the study ran.

This pilot validator accepts the current manifest only. Before revising specimens, preserve the old manifest and version the validator or artifact lookup so historical records remain verifiable.

## Presentation limits

The raster gallery is a preparation artifact, not an implemented four-option test. Its numbered labels and fixed order are not blind or randomized presentation. For a session, show the scheduled options in the recorded order with consistent sample text and conditions, and check legibility of the presentation itself. Do not claim the scheduled layout was displayed until it actually was.

The display width is recorded, but viewing conditions also need notes: device, zoom, enlargement, and relevant limitations. Separate nominal-size and matched-perceived-size conditions. Repeated sessions from one person are not independent participants.

## Before estimating scores

Review vocabulary, preserve raw observations, inspect disagreement and skipped trials, and define a versioned estimation and uncertainty method. Four-option selections cannot be averaged together with Google tag weights or personal preference ratings. No aggregation or recommendation calculation is implemented here.
