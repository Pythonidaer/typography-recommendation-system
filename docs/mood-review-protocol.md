# Mood review and four-option comparisons

Status: protocol proposal, version 0.1. No comparison interface, votes, personal preference weights, or calibrated trait scores exist. Establish mood words first; prepare examples next.

## Three different things to measure

| Question | What its answer informs | What it does not establish |
| --- | --- | --- |
| Which sample looks most calm? | Association between a rendered font instance and Calm | Whether the person likes calm fonts |
| Which sample would you choose for your project? | Personal or project preference | A universal font mood |
| How important is a calm impression for this heading? | Importance of a requirement in the project | How calm any particular sample looks |

Keep these in separate records. The word weight can mean font stroke weight, source tag strength, learned attribute strength, or importance in a person’s preferences. Name the specific kind rather than storing one generic weight.

## Two interpretations of quadrant

**Four samples in a 2-by-2 grid:** show identical content in 4 font instances and ask which expresses 1 named mood most clearly. This is the proposed first comparison format.

**A point on a two-axis map:** ask someone to position a sample against 2 dimensions at once. This can be explored later, after people understand both dimensions. Axis endpoints must have a reason; do not assume Calm is the opposite of Playful or Elegant.

A four-sample grid has 4 options, not 4 psychological quadrants. On a small screen it could use another readable arrangement while preserving the same task.

## Proposed trial

Prompt: “Which sample feels most playful?” Add the agreed short definition when needed.

Show the same text with the same text color and background in 4 instances. Hide family names and provider mood tags during judgment. Vary positions across trials and record the displayed arrangement. Keep role and settings explicit; do not silently mix a large heading with a small paragraph.

Offer a single choice plus “None fit,” “Too similar to choose,” and “Not sure / skip.” Record these as different outcomes, not zero-valued moods. For a later pairwise task, allow a tie or skip. These options are a deliberate project proposal, rather than a reproduction of the cited study’s forced-choice method.

Use a short initial block, provisionally 5 trials. This is a workload choice, not a statistically sufficient sample size. Include different comparison sets and repeat a small number in changed positions later to inspect consistency. A repeated answer from one person is still one person’s experience.

## Control what is being judged

- Content: neutral text about a place or object, avoiding mood words and emotionally loaded content. Use the same text across options.
- Role: headings and paragraphs are separate conditions.
- Style: use pinned normal font files; record selected weights, widths, optical sizes, and font-feature settings.
- Size: use a documented starting size, line height, and available width. Equal CSS size does not guarantee equal perceived size; note this and use a separate matched-perceived-size pass if needed.
- Appearance: a shared dark text color, white background, and no pictures, textures, motion, or decorative styling.
- Rendering: confirm the actual font loaded; a fallback invalidates the intended comparison. Record viewport and environment. Do not infer rendered appearance from a family name or tag.

Initial research-only settings are in research/protocols/mood-comparison-draft.json. They are not the website design or a prescribed typography scale.

## How observations could become useful

Store each choice with the attribute, definition version, participant type, exact instances, options, order, outcome, role, and settings. Keep raw responses so later analysis can change without losing evidence.

Initially report descriptive outcomes such as “chosen in 3 of 5 presentations” alongside the exact alternatives. Unequal comparison sets and stronger opponents make raw selection rates unsuitable as a global score. A most-chosen option provides no ordering among unchosen options; do not count one selection as 3 independent votes.

Pairwise or multi-option ranking models can be evaluated after the trial format and enough observations exist. A score would be relative to the evaluated samples and context. Do not automatically convert choices into Google’s 0-100 values or present match probabilities without a validated model.

For the five-family pilot, use planned comparison sets with overlapping alternatives so information connects across the sample. If 4 at a time is difficult to read or compare, try 2 at a time. The purpose is useful judgments, not preserving a grid at the expense of comprehension.

## Johnny, other readers, and AI

Johnny can provide an initial personal calibration. Keep it labeled as personal; use additional target readers later to study agreement and differences. More clicks from the same person do not establish broad consensus.

Codex can organize observations, check missing data, suggest definitions, and compare rendered examples when actually available. Any AI-generated appearance judgment must remain separate, with model identity, prompt, actual visual input, and date. It is not an independent human vote or a substitute for reader testing. Do not label a model judgment human-reviewed or use knowledge of provider scores as independent confirmation.

Provider tags, human judgments, AI suggestions, and personal preferences remain separate evidence channels. No arbitrary pooling of their weights is approved.

## Exit criteria for this stage

A small understandable vocabulary, examples that can be compared without major confounds, and a record format that preserves disagreement and unknowns. Then decide whether the method helps fill missing attributes. No calibrated recommendation eligibility follows from writing this protocol.

## Research basis and limits

The 2014 O’Donovan paper uses attribute-specific pairwise comparisons and relative attribute estimation; our four-option and skip design is an original proposal. Generalizing to our font instances, words, people, or screen conditions requires checking it. Source link:
https://www.dgp.toronto.edu/~donovan/font/fontSelection.pdf
