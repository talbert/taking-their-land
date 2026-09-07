# Stage 2 LLM-artifact tells findings

Date: 2026-08-28
Review type: Editorial Suite Stage 2, findings only
Target: repaired post-v5 correction candidate at commit `fc3056c4`
Venue: public working monograph, data package, and Latrian atlas
Provenance: explicitly model-assisted
Disposition: no blocking artifact; one material style/presentation cluster; two minor prose findings
Authority boundary: this review does not edit, approve, promote, deploy, stage, or commit the candidate.

## Blocking findings

**Zero blocking findings.** The changed release-facing material contains no Tier 1 hard artifact, fabricated-looking citation marker, placeholder, chatbot wrapper, abrupt cutoff, or raw tool markup. Nothing found in this pass prevents Stage 3 from running after the findings are adjudicated.

## Material findings

| ID | Instance and location | Tell | Tier / decay class | Why it matters here | Minimal proposed fix |
|---|---|---|---|---|---|
| M-1 | `CORRECTION_PLAN.json:66` and generated `corpus_v2.json:46361`: “a separate list **must not be added** to either figure”; `CORRECTION_PLAN.json:100` and `corpus_v2.json:24966`: “later Katmuhi and Suru material **is excluded**”; `CORRECTION_PLAN.json:126,131` and `corpus_v2.json:25007,25012`: cohorts “**must remain separate**” and figures “**must not be summed**” | Research-process narration and process-artifact leakage into reader-facing fields | Tier 2 style-only / Tier 3 structural; slow-decaying structural tell | These are sound editorial controls, but the public `victims` and `summary` fields sometimes address a future coder or reviewer rather than describe the event to a reader. The same controls already have a proper home in `post_v5_source_calibration`. Repetition across three of the seven repaired records makes the public data read like an adjudication transcript even though the underlying distinctions are necessary. | Keep the commands in `post_v5_source_calibration`; make public fields declarative. For example, describe the Year 9 list as “separate and non-additive,” omit the Nipur sentence about material outside the event boundary, describe the Nirbu cohorts as having different outcomes, and state that its figures represent distinct cohorts rather than a cumulative resident census. Do not remove the distinctions themselves. |

This is material to presentation, not to historical coding or statistical validity. It requires no model rerun unless the reproducible source plan is edited and its manifests are designed to bind narrative hashes.

## Minor findings

| ID | Instance and location | Tell | Tier / decay class | Why it is a tell rather than a factual objection | Minimal proposed fix |
|---|---|---|---|---|---|
| m-1 | `MODEL_COMPARISON_INTERPRETATION.md:41`: “**The correct interpretation is therefore** stable nine-factor subspace with forced-eight axis rotation.” | Self-referential coherence checking plus performative certainty | Tier 3/4 structural-sentence tell; slow-decaying | Stage 1 found the interpretation supported, so this is not a calibration or source finding. The phrase announces that the memo has selected the correct reading instead of stating the result directly. | State the result without the editorial throat-clearing: “**The nine-factor subspace remains stable, while forcing eight factors rotates the axes.**” Preserve the following explanation of F2/F7/F8. |
| m-2 | `MONOGRAPH_DRAFT_v1.md:91-93`: “Ten source-adjudicated roster and cell corrections arising during atlas authoring **have completed** one finite application and model-comparison cycle.” | False agency and synthetic umbrella phrasing | Tier 4/5 sentence-level; statistical/stylistic decay class | Corrections do not perform or complete a cycle; the project applies them. The stacked noun phrase also makes a precise checkpoint sound like workflow-generated administrative prose. The counts and procedural status are useful and should stay. | Use an actor and a plain verb, for example: “A finite post-v5 cycle applied ten source-adjudicated authoring corrections and compared the resulting model.” |

## Zero-finding categories

### Tier 1 — hard artifacts and fabrications

Zero findings. The required mechanical search covered the scoped files and changed lines for:

- OpenAI, ChatGPT, Copilot, Perplexity, and Grok tracking parameters;
- `oaicite`, `oai_citation`, `turn…search`, `citeturn`, `iturn…image`, `[cite:]`, span markers, attribution JSON, Grok cards, Perplexity upload tags, attached-file/web tags, and lenticular citation residue;
- `:::writing` blocks, fenced `wikitext`, return-arrow footnotes, raw `openai.com` source URLs, and private tool references;
- placeholder names, dates, URLs, comments, and impossible access-date forms;
- new DOI, ISBN, URL, and access-date strings in the changed release-facing lines.

No new DOI, ISBN, URL, or access-date string was introduced by `fc3056c4`; therefore no identifier-resolution claim is made here. This pass did not browse and did not reperform Stage 1 source verification.

### Tier 2 — source-integrity patterns

Zero guideline-violating findings. The repaired Iberia sentence “This supports strongly sex-biased ancestry turnover, not documented killing, expulsion, or residential displacement” and the Thutmose sentence “The campaign supports movement … but not total depopulation…” use recognizable interpretive surface forms, but the contrasts do real work: they state the accepted evidentiary boundary and were checked in Stage 1 against the adjudication record. Flagging them merely because they contain “supports” or negative parallelism would be a false positive.

There is no changed-span instance of fabricated attribution, vague-authority consensus, source-count inflation, canned notability, inflated significance, source-pass-to-prose organization, or sentence-final participial analysis.

### Tier 3 — structural and rhetorical patterns

Apart from M-1 and m-1, zero findings. The chronological organization of the monograph is historical and methodological rather than a converted source log. The `MODEL_COMPARISON_INTERPRETATION.md` headings “What this does and does not authorize,” “Monograph consequence,” and “Reproducible record” are legitimate apparatus in a technical decision record; their process language is not pretending to be atlas case prose. The Stage 1 findings and adjudication files are process documents by design and were used as context, not misclassified for containing process language.

No sycophantic opener, question restatement, diplomatic sandwich, closing legacy zoom-out, “despite challenges” template, collaborative-chat leakage, emoji formatting, miniature-table performance, or unearned conclusion section was found in the changed release-facing material.

### Tier 4 — sentence and paragraph patterns

Apart from m-2, zero findings. Lists in the model memo and structured arrays in the corpus are genuinely list-shaped. Semicolons and compact enumerations in `mechanism`, `victims`, and `confidence` fields carry distinct evidence constraints rather than perform variety. Negative parallels generally rule out specific, live misreadings exposed by Stage 1 and are not decorative reversals. No rule-of-three padding, repetitive participial opening, transitional rotation, dramatic fragmentation, elegant variation, or repetitive paragraph conclusion was found.

### Tier 5 — word-level patterns

Zero findings. No material cluster of frequency-list vocabulary, ornamental intensifiers, superlative stacking, “delve,” “robust,” “nuanced,” “pivotal,” “landscape,” or similar padding occurs in the changed spans. Technical terms such as “subspace,” “principal angle,” “Tucker congruence,” “structural-NA,” and “global-median preprocessing” are domain-specific and necessary. Curly quotation marks, mathematical symbols, and Markdown emphasis appear in contexts that render or require them and are not treated as diagnostic.

## Grounding and coverage statement

This review read the supplied `/Users/talbert/Downloads/editorial-suite(1).zip` in full, including `SKILL.md`, all four reference documents, `.gitignore`, and `build.sh`. It followed only the LLM Artifact Tells stage. Stage 1 was not repeated, and Stage 3 calibration was not performed.

The review inspected:

- the complete diff `fc3056c4^..fc3056c4`;
- every changed release-facing field in `CORRECTION_PLAN.json`;
- the seven repaired records in `candidate/post_v5_corrected_successor_675/data/corpus_v2.json` (Iberia, Thutmose III, Amenhotep II Year 9, Nipur-Pasate, Nimme/Tummu-Habhu, Upper Tigris/Nirbu, and Zamua);
- `MODEL_COMPARISON_INTERPRETATION.md` in full;
- all changed post-v5 spans in `monograph/MONOGRAPH_DRAFT_v1.md`;
- `FACT_CHECK_FINDINGS.md` and `STAGE_1_ADJUDICATION.md` as provenance and boundary context;
- the seven corresponding rows in `editorial/eight_trait_cards.csv` and the editorial manifest only to confirm how repaired names propagate;
- the hard-artifact patterns required by the supplied Tells guideline across the scoped files and changed lines.

The review did not inspect unrelated corpus rows, unchanged monograph prose, original scholarly sources, external websites, deployment state, or statistical code outside what was needed to understand the changed language. It made no source-content verdict from memory. No browse, additional agent, target edit, staging action, or commit occurred.

## Concentration summary

The findings concentrate in one place: editorial controls that correctly protect event boundaries are still phrased as instructions inside three public corpus records. The statistical interpretation and monograph are otherwise comparatively clean; their two minor findings are administrative-sounding framing, not source-integrity defects. There is no hard-artifact cluster and no evidence of vocabulary-level laundering.

## Stage 2 self-audit

| Required audit item | Status | Result |
|---|---|---|
| Checklist vs. heuristic | PASS | Every candidate hit was tested for function. “Supports,” negative parallelism, technical symbols, lists, and semicolons were retained where they carry real evidentiary or technical distinctions. |
| False positives | PASS | The Iberia and Thutmose boundary sentences, the model memo's technical apparatus, and the Stage 1 process records were explicitly considered and not misclassified. |
| Hard artifacts | PASS | The mandatory mechanical searches were run in tier-first order. No hard artifact or newly introduced identifier string was found. Identifier resolution was not fabricated without browsing. |
| Tier coverage | PASS | Tiers 1 through 5 were audited in order; zero-finding categories above disclose the result for every tier. |
| Decay weighting | PASS | Structural process leakage receives the material finding; sentence phrasing receives minor findings; vocabulary and punctuation receive no standalone verdict. |
| Guideline vs. style sort | PASS | M-1 is marked style/presentation, not a source-policy violation. No SYNTH, significance-appending, or inflated-significance defect survived Stage 1 in the scoped material. |
| Introduced tells | PASS / N/A | Findings-only review: no target prose was rewritten, so this pass introduced no new tell into the candidate or monograph. Minimal proposed wording is clearly review apparatus, not adopted release prose. |
| Writer's voice | PASS | No idiosyncratic historical or statistical terminology was targeted. The proposals remove workflow commands, not disciplinary language. |
| Register homogenization | PASS | The review preserves technical, historical, evidentiary, and editorial registers where each is intentional; it only flags editorial commands placed inside public historical fields. |
| Quality tradeoffs | PASS | The proposed changes preserve every cohort distinction, uncertainty, and event boundary. No precision is traded for smoothness. |
| Editorial synthesis (SYNTH) | PASS | No rewrite was performed. Potential surface cues were checked against Stage 1's accepted grounding and were not upgraded into unsupported conclusions by this review. |
| Venue check | PASS | The venue is the project's own public working monograph/data/Latrian package; no external venue restriction or undisclosed-authorship claim is being evaded. |
| Provenance honesty | PASS | Model assistance remains explicit. This pass does not claim that cleaner prose changes authorship or that absence of tells proves human authorship. |

## Findings-only boundary

This is the sole bounded Stage 2 review. It records findings and minimal edits only. It does not reopen Stage 1, perform Stage 3, alter any target, grant promotion or deployment authority, or authorize another review round.
