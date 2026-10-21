# Pilot specimen preparation

Status: raster specimens prepared for the existing five-family batch. No participant responses, mood ratings, readability results, or pairing recommendations exist.

See [the specimen gallery](../research/specimens/batch-1/README.md), [manifest](../research/specimens/batch-1/manifest.json), and [generator](../scripts/render_pilot_specimens.py).

## What the generator does

- Checks each input font against its committed source-file SHA-256 hash.
- Verifies all sample characters have mappings.
- Instantiates the selected variable axes explicitly, including Merriweather at weight 400 rather than its file default of 300.
- Renders the same content for headings, paragraphs, and character samples in all five instances.
- Uses each real font file directly; it does not silently substitute a fallback.
- Records settings, line breaks, glyph bounds, source identities, renderer versions, and image hashes.

Images use a shared width and nominal size by role. Different line breaks are an observed layout consequence, not a score. Preserve that distinction in later comparisons.

## What these artifacts establish

They demonstrate that the pinned instances can be instantiated and raster-rendered with the sample content. Image inspection can identify clipping or missing lines. It does not show that participants find them legible, comfortable, calm, playful, or suitable for a project.

Raster proofs do not verify a browser renderer, mobile text enlargement, responsive behavior, or assistive technology. Font records remain needs_review and recommendation_eligible=false.

## Next work

Use the images to make the mood discussion concrete. Keep the vocabulary provisional. If later mood judgments depend heavily on unequal apparent text sizes, compare an explicitly documented matched-perceived-size condition rather than silently changing the original settings. No product UI or recommendation scoring is introduced here.

## Prepared comparison schedule

[The five-trial schedule](../research/protocols/four-option-schedule.json) presents 4 of the 5 instances per trial. Each instance appears 4 times, occupies each position once, and appears with each other instance 3 times. The generator verifies these counts. This is exposure balance, not proof that a judgment is unbiased or statistically reliable.

The attribute, role, and participant are deliberately unassigned. Before a real session, choose an agreed attribute and one role, vary and record trial order, and verify the presentation. Do not run every mood and role by default. A partial block may lose the planned balance. No responses have been collected.
