# Pilot evaluation plan: draft 0.1

Status: proposed tasks and observation structure. No participants or rendered tests have run. This is a bounded plan for the existing five-family sample, not a product requirement that every visitor complete a study.

## Scope

Use Noto Sans, Merriweather, Roboto Mono, Caveat, and Abril Fatface. All records remain needs_review and recommendation_eligible=false.

Use the fictional informational-website brief in assessment-questions.md. Record exact family/style/axes, content, text role, size, spacing, width, colors, device, and rendering environment. Existing mood comparison instances supply draft settings, not validated perceptual matches.

Keep separate observations for individual instances and complete combinations. Do not assume the top two individually preferred fonts form the best pair.

## Preparation before asking anyone

1. Verify the selected font files and actual rendering, including fallback detection.
2. Check that all required sample characters map. Keep this separate from visual identification.
3. Prepare heading, paragraph, action label, and character samples using identical controls within a comparison.
4. Define the task, expected response, and observation fields before collecting answers.
5. Keep the initial session to a few tasks; stop or shorten it when comparison becomes tiring.

No fixed participant count or statistical sufficiency is claimed. Plan comparisons and interpretation before reporting outcomes.

## Evaluation tasks

| Area | Task proposal | Record | Interpretation boundary |
| --- | --- | --- | --- |
| Purpose | Ask the reader to explain what the sample page offers and find how to reserve a place | Their explanation, found action, errors or missing information | Content and layout also affect success |
| Legibility | Ask the reader to transcribe a short identifier and symbols at the intended settings | Exact response, expected characters, substitutions, rendering context | Familiarity, content, and viewing conditions affect results |
| Readability | Ask the reader to read a short explanation and answer a factual question | Answer accuracy, optional elapsed time, comfort response, comments | A short task is not evidence about long-form fatigue |
| Mood | After definitions are agreed, ask which controlled sample expresses 1 mood | Attribute-specific choice, alternatives, order, uncertainty | A preference click is a different measure |
| Harmony | Show typography with the supplied surrounding design and ask whether it fits | Context shown, fit response, explanation | Leave untested when no real context exists |
| Hierarchy | Ask the reader to find the time, location, or action in the complete layout | Correct item found, wrong selections, search path or comments | Evaluate the full combination and layout, not a font alone |

## Example content

Fictional heading: “Riverside workshop”

Fictional paragraph: “The workshop starts at 2 pm in Room B. Bring a notebook. Doors open 15 minutes before the start. Registration closes on Friday.”

Action label: “Reserve a place”

Possible questions:
- “What should you bring?” Expected answer: a notebook.
- “Where is the workshop?” Expected answer: Room B.
- “How early do doors open?” Expected answer: 15 minutes before the start.

Character sample: “Il1 O0 rn m 8B {} [] () , . : ;”
A task needs an exact expected string and instructions that do not reveal the answer. First seeing a reference string can support matching but changes the task; record which method is used.

Use neutral practice content first. Repeated reading of the same paragraph creates learning effects. For comparisons across fonts, use a planned order and matched alternate passages where needed; record passage ID and acknowledge that content difficulty can also differ.

## Comfort question

“How comfortable was this to read?”

Proposed responses: uncomfortable / somewhat uncomfortable / neither comfortable nor uncomfortable / somewhat comfortable / comfortable / not sure.

This is a report of comfort in the tested condition. It is not an objective accessibility grade or a diagnosis. Ask optional “What made it easier or harder?” after the task.

## Task data structure

Keep one observation per participant, task, and condition. Proposed fields:
- observation_id and protocol_version
- participant_id and participant_kind
- area, task_id, passage_id, and condition_id
- exact font instances and layout/settings snapshot
- expected response and actual response
- accuracy result or not applicable
- elapsed time only if measured consistently
- reported comfort and optional comments
- outcome: completed / skipped / interrupted / invalid
- evidence provenance, environment, and date

No personal diagnosis or demographic inference is needed. Maintain separate records for human task observations and AI-assisted analysis.

## Interpretation and stopping points

Preserve observations by area. Do not average purpose, legibility, readability, mood, harmony, and hierarchy into one quality number.

If required characters are absent, revise the candidate or requirement before that trial. If the font fails to load, invalidate the intended font trial. If instructions confuse the participant, revise them rather than scoring the confusion as a font failure.

If mood words are unclear, revise vocabulary before collecting more mood votes. Continue independent technical checks as useful.

One reader can identify a problem and provide personal feedback; that does not establish performance for a population. More repeated clicks from that reader are not additional independent participants.

## Outputs of this pilot

A checked task format, documented evidence gaps, and examples of what we can responsibly explain. A later decision will determine whether to collect more evidence, revise attributes, or test a transparent recommendation method.

The plan creates no test results and changes no font eligibility. Actual sample rendering and participant feedback remain the next research activities after the relevant wording and mood definitions are reviewed.
