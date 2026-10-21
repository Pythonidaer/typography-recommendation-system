# Product plan

## Reader and outcome

For people who find browsing a large font catalogue difficult. Help them choose fonts for a specific project and understand why the suggestions fit. This describes the intended audience, not validated user research.

## Agreed requirements

- Let people request 1, 2, or 3 font families.
- Return recommended fonts with suggested roles and understandable reasons.
- Consider purpose, information, mood, tone, style, relationship with the surrounding design, and audience needs.
- Preserve readability, legibility, and purpose as evaluation concerns.
- Keep font selection distinct from later sizing experiments.
- Provide a path toward a typography style guide.

## Assessment structure

Purpose, legibility, and readability are the core principles. Mood and harmony, and hierarchy, support the design’s purpose; audience needs inform all areas. See assessment-principles.md for the proposed questions, evidence, and methods. Mood scores alone must not drive the recommendation.

## Proposed journey

| Stage | Inputs or activity | Result |
| --- | --- | --- |
| Describe the project | Purpose, medium, information, language, reading conditions, existing design | Project requirements |
| Express preferences | Desired mood, visual comparisons, family count | Preference profile |
| Review recommendations | Suggested fonts and assigned roles | A shortlist to try |
| Experiment | Actual content, weights, sizes, spacing, colors, optional scale | Refined text styles |
| Document | Family, fallback, role, size, weight, style, line height, letter spacing, color, examples | Typography style guide |

No question count, result count, scoring formula, or visual design is approved yet.

## Roles and family count

1 family can cover headings, paragraphs, and labels through styles and weights.
2 families might separate headings from body and interface text.
3 families need a defined extra role, such as code or occasional accent text. Ask what that role is.

Additional text roles may include navigation, buttons, form labels, helper text, errors, links, quotations, lists, tables, captions, and code. Each role does not require a different family.

## Timing of weights, sizes, and colors

Offer useful starting styles in previews; refine them in the experiment stage. Check necessary weights, italics, language coverage, and availability before recommending a family. Evaluate text colors against the palette and background contrast. Finalize and record decisions in the style guide.

A modular scale supplies size candidates. Visual judgment and real-content testing remain necessary.

## Open decisions

- Google Fonts first, or Google Fonts plus system fonts in the pilot?
- How many alternative sets should results offer?
- How do people express and revise preferences?
- Which characteristics can we document reliably?
- How should evidence gaps affect eligibility and ranking?
- How do we handle an unsuitable request or too few supported candidates?
- How will we validate combinations and recommendations with readers?
- Which export formats would make the final guide useful?

The database, framework, hosting, and any model/API use remain undecided.
