# Pilot documentation review

Reviewed October 21, 2026. Family documentation, licenses, metadata, and binary sources are pinned to Google Fonts revision 45e3d5269e4a17d823f6d84470bc084dc5ae46f6.

## What is now supported

| Family | Attributed intended use | Important boundary |
| --- | --- | --- |
| Noto Sans | General Latin, Cyrillic, and Greek text; a companion for script-specific Noto Sans families | This file does not inherit every script supported by the full Noto collection |
| Merriweather | Text designed for screen reading | Source intent is not a measured reading-performance result |
| Roboto Mono | Screen text and software source code, with deliberate code-character differentiation | A character mapping check cannot establish visual distinction |
| Caveat | Short annotations and body text | Handwriting category alone is insufficient to exclude body use; real reading conditions still matter |
| Abril Fatface | Heavy titles and headlines | The broader Abril family’s other styles and text roles are not automatically part of this Google Fonts family |

These roles are provider statements, not new performance judgments. Each record retains the exact document URL and blob identity. Noto’s longer About article was also read. The other 4 pinned family directories contain DESCRIPTION files and no article directory, so the records accurately use the available legacy descriptions.

## Source limitations

Merriweather’s provider description points to an older project location while metadata points to Merriweather4. The pinned Merriweather4 README remains a template and supplies no additional design evidence. Do not use its sample-font or example-changelog text as facts about Merriweather.

Caveat’s upstream README gives little role information; its warning about Caveat Brush belongs to a separate family. Roboto Mono’s pinned upstream README corroborates the provider’s code-character focus. The attempted pinned Abril Fatface upstream README returned 404.

## License-source review

All 5 reviewed OFL.txt files state SIL Open Font License 1.1. The source terms cover use and embedding, preserving copyright and license notices on redistributed copies, font modification and reserved-name conditions, and restrictions on selling font files by themselves. Merriweather and Abril Fatface files explicitly name reserved names. Keep the applicable source license with any eventual bundled files.

This pass records the source terms for planning. No packaging, redistribution implementation, modification, or service-specific agreement has been evaluated. The font files were downloaded only to temporary research storage for inspection; binaries and full source descriptions are not added to this repository.

## Limited character checks

Using fontTools, inspected one normal binary per family. All 5 map printable ASCII plus the documented English interface, character-distinction, and accented/punctuation example strings. The reproducible report records exact URLs, SHA-256 hashes, axis defaults/ranges, and tested strings.

This is Unicode cmap presence only. It does not test shaping, kerning, ligatures, drawn appearance, distinguishability, screen readability, every language character, or italic binaries. A project still needs its own required-character checks.

Run with local downloaded files named <record-id>.ttf:

```sh
python scripts/check_pilot_characters.py /path/to/pinned-font-files research/source-audit/pilot-character-checks.json
```

Requires fontTools. The script records hashes; compare them with the committed report rather than assuming similarly named files are identical.

## What the attribute records can currently compare

Raw source assignment values below are observations across all recorded locations. Ranges show differing source assignments, not continuous interpolation or preference confidence. Equal values do not prove variant independence. Values are not match percentages.

| Family | Calm | Loud | Playful | Vintage | Business |
| --- | ---: | ---: | ---: | ---: | ---: |
| Abril Fatface | Unknown | 64 | Unknown | 76 | 30 |
| Caveat | 3-5 | Unknown | 35 | 45 | Unknown |
| Merriweather | 92-94 | 20-58 | Unknown | 12-14 | 90-92 |
| Noto Sans | 90-94 | 12-72 | Unknown | Unknown | 80-88 |
| Roboto Mono | 53 | 1 | 1 | 10 | 12-20 |

Only Roboto Mono has an assignment for all 5 proposed traits in this batch. Treating unknowns as zeros would create invented differences. Averaging only known traits could favor incomplete records. Do not calculate a combined 5-trait ranking for these records yet.

This is a useful result of sampling: a rich-looking global dataset does not guarantee complete comparable evidence in a particular shortlist.

## Consequences for the assessment

1. Ask about text roles as well as mood. A family may support more than one role.
2. Preserve the chosen style and axis context. Noto Sans’s Loud assignments, for example, differ considerably between light and heavy source locations. We cannot always give one family a single mood score.
3. Let people refine weights later, but explain that changing a weight can change the appearance underlying a recommendation. A future result may need a suggested starting style.
4. Use only dimensions supported by comparable evidence, or review the missing values before ranking. Do not automatically derive opposite traits or interpolate axis corners.
5. Test combinations separately. These 5 individual role descriptions establish no pairing rule.

## Next bounded task

Prepare a research comparison protocol with identical content, explicit font instances, and separate heading and body settings. Review whether the 5 proposed question labels describe the examples usefully. Record missing judgments through a versioned rubric, using unknown until reviewed. Do not add more families before reviewing this batch.

Reader and visual testing are still pending. All records remain recommendation_eligible=false and now use needs_review to distinguish completed source collection from the remaining appearance and suitability review.

## Source trail

Each family record links the pinned DESCRIPTION and OFL files; Noto also links its About article. Additional inspected upstream sources:

- https://raw.githubusercontent.com/EbenSorkin/Merriweather4/e586023aa0fe1dba9a7d4ec80fa8b9e546cb7ecf/README.md
- https://raw.githubusercontent.com/googlefonts/RobotoMono/111eb14e367888c9374da4da0b018e72cf8ac46d/README.md
- https://raw.githubusercontent.com/googlefonts/caveat/59745e818ef7973e11e70cb1358d0e902b56c5fc/README.md
- https://raw.githubusercontent.com/librefonts/abrilfatface/5e899bfd997c34d1c2bd43ca9f94d2d0ded6346f/README.md (404)
- https://openfontlicense.org/open-font-license-official-text/ (official reference checked October 21, 2026; family files remain the source for family-specific headers)
