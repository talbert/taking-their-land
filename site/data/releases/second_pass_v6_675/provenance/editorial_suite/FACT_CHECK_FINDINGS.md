# Stage 1 Fact-Check Findings

**Review type:** Editorial Suite Stage 1, findings only
**Candidate:** Taking Their Land post-v5 correction candidate
**Disposition:** Substantive blocker found; additional mechanical/editorial findings found; no numerical model-comparison blocker found.
**Authority boundary:** This report grants no release, atlas-change, correction-application, deployment, publication, or commit authority.

## Findings first

### Substantive blocker

#### SB-1 — The public candidate corpus retains legacy narrative fields that contradict the accepted Batch 19–22 limits

The newly added `post_v5_source_calibration`, date labels, identifier aliases, family overrides, and cell corrections are generally faithful to the adjudications. However, the same active candidate records continue to expose older reader-facing `name`, `mechanism`, `agents`, `victims`, `summary`, and `confidence` text. In several records that text states more than the accepted reviews permit. A downstream reader can therefore receive two incompatible accounts from one released row.

Examples checked in the candidate corpus:

- **Thutmose III / Megiddo:** the legacy mechanism still says “captive removal and coerced labor (provisional),” the agent field includes Egyptian estate institutions, and the confidence text refers to long-term labor disposition. Batch 20 permits estate institutions only as general system context; it does not establish the sampled cohort's labor assignment or final institutional destination.
- **Ashurnasirpal II / Nipur-Pasate and Tumme-Habhu:** the summaries continue to call the records “source-bounded 883 BCE,” although the accepted correction deliberately uses neutral successor identifiers and disputed 882/883 date labels. The Tumme-Habhu summary also allows movement “toward Assyria,” while Batch 22 leaves destination unknown and does not support that arrow.
- **Amenhotep II, Year 9:** the legacy mechanism says the cohort was transported to Memphis/Egypt. Batch 21 supports Memphis as the king's recorded return point, not as the demonstrated destination of every captive.
- **Prehistoric Iberia:** the active title says “male-lineage replacement”; `agents` treats R1b-M269 lineages as actors; `victims` converts residents into a demonstrated victim cohort; and the summary says male lineages were progressively eliminated with durable consequences “to present.” Batch 19 permits sex-biased ancestry and Y-chromosome lineage turnover. It does not establish a bounded victim/displaced cohort, intentional violence or expulsion, a genetic lineage as an actor, or the unqualified “to present” consequence.
- **Zamua:** “settlements fade or burn” is both vague and broader than the accepted posture, which permits attributed destruction/burning without implying durable depopulation.
- **Upper Tigris/Nirbu:** the legacy summary collapses distinct cohorts and outcomes that the new calibration field keeps separate.

This is substantive because the affected fields are in the proposed public statistical data package, not merely in an internal note. The candidate should not be represented as uniformly “source-supported” or “source-honest” while contradictory default narrative fields remain active. No statistical rerun is required for this finding; the defect is in public historical description and attribution.

### Mechanical/editorial blockers

#### ME-1 — The post-v5 model paragraph is followed by a source pointer to the earlier v5/676 analysis

The monograph's post-v5 paragraph reports the corrected 675-event comparison, but the following sentence binds “These current candidate claims” to `candidate_models_v2/MODEL_RESULTS_AUDIT_DISPOSITION.md`, an earlier v5/676 artifact. That file is real, but it is not the direct source for the new post-v5 values. The post-v5 claims should point to:

- `analysis/second_pass/v5/post_v5_correction_application_v1/results/post_v5_model_comparison_v1/MODEL_COMPARISON_SUMMARY.json`
- `analysis/second_pass/v5/post_v5_correction_application_v1/MODEL_COMPARISON_INTERPRETATION.md`

The older pointer can remain only if its scope is changed to “The preceding v5 candidate claims.” This is a citation-resolution defect, not evidence that the reported post-v5 numbers are wrong.

#### ME-2 — “Direct replication” overstates the independence of the post-v5 comparison

The post-v5 run is a deterministic, bounded perturbation/robustness comparison using the project's established model machinery and shared helpers. It is not an independent replication by a separate implementation or independently assembled dataset. “Additional bounded post-v5 perturbation check” is accurate.

#### ME-3 — “No corrected event is individually material” is broader than the implemented influence test

The influence script leaves out each entire corrected event from the corrected reference and compares the resulting solution. It does not revert each event's corrections one at a time while holding the event in the corpus. The output supports: “None of the nine leave-one-corrected-event-out scenarios crossed the declared materiality thresholds.” It does not uniquely isolate the effect of each correction from the effect of omitting the event.

### Correct claims

The following load-bearing post-v5 claims are supported by the opened local evidence:

1. **Retirement and audit preservation:** `atlas-indo-aryan-migration` is inactive in the successor candidate, remains present for audit, and carries the `post_v5_retirement` basis. The correction plan and candidate state agree.
2. **Candidate size:** the immutable base contains 748 rows and 676 active events; the successor contains 748 rows, 675 active events, and 73 inactive rows. The corrected score matrix contains 675 event rows and 60 dimensions.
3. **Patch extent:** the ledger contains exactly 117 changed cells across nine events: 104 `U`, one `NA`, eight score-3 cells, two score-2 cells, and two score-1 cells.
4. **Identifier corrections:** the two Nipur-Pasate and Tumme-Habhu 883-bearing identifiers map to neutral successor identifiers without a year suffix, while aliases preserve traceability.
5. **Primary-family corrections:** the applied overrides and resulting counts agree across plan, corpus, summaries, and validators: conquest and incorporation 170; expulsion or flight without replacement 179; land clearance for state/project use 25; low-state durable expansion 44; settler replacement 111; state-directed demographic remaking 144. There are 673 classified active events and two holds.
6. **Retained dimensionality:** both the immutable v5 reference and corrected successor retain nine factors under the recorded criterion.
7. **Corrected-vs-v5 stability:** the corrected nine-dimensional subspace has maximum principal angle 2.7646054027 degrees, minimum cosine 0.998836, and best-matched minimum Tucker congruence 0.999271. The forced-eight comparison has maximum principal angle 6.6849568893 degrees and best-matched minimum Tucker congruence 0.997023.
8. **Interpretation of F2/F7/F8:** low same-name congruence for those axes, combined with high full-subspace and best-matched agreement, supports rotation/reallocation within a stable retained subspace. It does not support saying that the historical structure disappeared.
9. **Influence thresholds:** none of the nine leave-one-corrected-event-out rows crosses the declared materiality thresholds. The narrower wording in ME-3 is required.
10. **Sensitivity limits:** equal-era weighting, era-median imputation, KNN imputation, structural-zero imputation, and documentation/missingness subsets can materially change orientation, dimensionality, or named-axis behavior. The recorded corrected nine-dimensional angles include 26.987 degrees for equal-era weighting, 32.608 degrees for era-median imputation, 25.249 degrees for KNN, and 70.014 degrees for structural-zero imputation. The corresponding v5 values are 26.539, 36.124, 24.977, and 71.313 degrees. The at-most-40-missing subset returns a 4.742-degree nine-dimensional angle while still flagging named-axis instability.
11. **Immutable-v5 comparison context:** all 676 immutable-v5 event leave-outs stay below five degrees in the nine-dimensional subspace, with maximum 4.808 degrees. Of 138 program scenarios, seven exceed five degrees, with maximum 5.947 degrees. Across the ten alternate scenarios, the maximum is 71.313 degrees.
12. **Card/model distinction:** the candidate card summaries are evidence-aware weighted anchor summaries. They are not newly fitted forced-eight factor scores. The copied card-model artifact is explicitly identified as frozen provenance rather than presented as a new fit.
13. **Manifests and authority flags:** checked input/output hashes agree with the opened candidate, editorial, and comparison artifacts. Release, atlas-change, correction, and deployment authority flags remain false.
14. **Changed monograph metadata:** the updated version/date and 748-row/675-active/73-inactive counts agree with the successor candidate.

There is **no numerical or table-reconciliation finding** against the post-v5 comparison values listed above.

### Overstated claims

- **“Direct replication”** is overstated for the shared-pipeline bounded comparison. See ME-2.
- **“No corrected event is individually material”** overstates what the leave-one-event-out design isolates. See ME-3.
- **“Source-supported corrections” / “source-honest corrections”** is too broad while SB-1 remains in the active public corpus. The patch ledger and calibrations are source-adjudicated; the complete reader-facing rows are not yet internally source-consistent.

No other overstatement was found in the changed monograph spans that were checked.

### Wrong or unverifiable claims

- The legacy candidate-corpus statements identified in SB-1 are wrong or unverifiable at the specificity presented under the accepted Batch 19–22 evidence limits.
- The monograph source pointer in ME-1 is the wrong direct support for the immediately preceding post-v5 numbers, although it is a valid earlier-v5 artifact.
- Original-source funding, sponsor role, and conflict-of-interest disclosures were not available in the required local review packet and were not independently verified. This does not make the adjudicated claims false, but those disclosure dimensions remain unverified by this Stage 1 review.

There are **zero additional wrong/unverifiable numerical claims** in the checked post-v5 model paragraph and output summaries.

### Source-quality findings

- The local procedural evidence is strong for reproducibility within this repository: correction plans, row-level ledgers, deterministic builders, hashes, manifests, validators, and comparison tables agree.
- The model validator checks hashes, schema/table relationships, declared thresholds, and interpretation-output consistency. It does not constitute an independent refit by a separate implementation. “Validated” should therefore mean internally validated, not independently replicated.
- Historical calibration is mediated through the local Batch 19–22 reviews and adjudications named by the brief. Those documents are appropriate evidence for checking whether the candidate follows its accepted editorial decisions.
- The underlying scholarly source PDFs and their publisher disclosure statements were not part of the required local packet opened for this review. No web sources were used, as instructed. Accordingly, this review confirms adjudication fidelity, not a fresh source-from-origin literature audit.
- The frozen card-model provenance is adequately identified in the manifest. Its age and different event counts should remain visible wherever that artifact is distributed.

### Structural, register, and attribution findings

**Structural:**

- SB-1 creates duplicated, conflicting truth layers inside active records: corrected calibration fields coexist with unsuperseded legacy narrative fields.
- ME-1 creates ambiguous citation scope between the old v5 candidate analysis and the new post-v5 correction comparison.
- There is no structural finding in the changed atlas-count metadata or authority flags.

**Register:**

- “Direct replication” and, pending SB-1, “source-honest” are stronger than the evidence posture supports.
- There is no promotional/vendor register, synthetic consensus language, or partisan/political-spectrum contamination in the checked changed spans.

**Attribution:**

- The Thutmose III legacy fields convert system-level estate/labor context into cohort-specific mechanism, actor, and confidence claims. This is an attribution error.
- The Iberia legacy fields turn a genetic lineage into an actor and infer a victim cohort not established by the accepted evidence.
- There are zero quotation-attribution findings in the changed monograph spans; no changed span relies on a direct quotation.

## Minimal proposed edits

These are proposed corrections only. No target file was edited.

1. **Make every public default narrative field conform to the accepted calibration.** At minimum:
   - Thutmose III: remove cohort-specific “coerced labor,” remove estate institutions from the cohort-specific agent field, and state that long-term labor/institutional disposition is unknown.
   - Nipur-Pasate and Tumme-Habhu: replace unqualified 883 BCE wording with disputed 882/883 dating; remove Tumme-Habhu movement “toward Assyria.”
   - Amenhotep II Year 9: do not present Memphis as every captive's demonstrated destination; if retained, identify it only as the king's recorded return point.
   - Iberia: use sex-biased ancestry/Y-chromosome lineage turnover language; do not name a genetic lineage as an actor; do not assert a bounded victim/displaced cohort, violence, expulsion, “elimination,” or an unqualified “to present” consequence.
   - Zamua: replace “fade or burn” with narrowly attributed destruction/burning language and no implied durable depopulation.
   - Upper Tigris/Nirbu: preserve the reviewed separation of cohorts and outcomes.
   If historical legacy text must remain for audit, move it to clearly named `legacy_*` fields and mark it superseded; do not leave it as the default reader-facing account.
2. Replace **“direct replication”** with **“additional bounded post-v5 perturbation check.”**
3. Replace **“No corrected event is individually material”** with **“None of the nine leave-one-corrected-event-out scenarios crossed the declared materiality thresholds.”**
4. Add the post-v5 summary and interpretation paths directly after the post-v5 numerical paragraph. Change the older source sentence to **“The preceding v5 candidate claims are bound to …”** if it is retained.
5. Until item 1 is complete, replace **“source-supported corrections”** and **“source-honest corrections”** with the narrower **“source-adjudicated roster and cell corrections.”** After the public narrative fields are reconciled, the stronger wording may be reassessed by a later authority-bearing review.

## Grounding statement

This review used only local evidence named by the brief. I opened and checked:

- `editorial_suite_final_v1/REVIEW_BRIEF.md` in full;
- the supplied `editorial-suite(1).zip` in full, including `SKILL.md`, `fact-check-and-revise.md`, `llm-artifact-tells.md`, `calibration-review.md`, `suite-pipeline.md`, `.gitignore`, and `build.sh`;
- `CORRECTION_PLAN.json`, all 117 rows of `CELL_PATCHES.csv`, `CELL_PATCH_SUMMARY.json`, and `SINGLE_ADVERSARIAL_SCORING_REVIEW.md`;
- the Batch 19, 20, 21, and 22 `REVIEW.md`, `INDEPENDENT_SOURCE_REVIEW.md`, and `ADJUDICATION.md` files;
- the successor candidate corpus/score outputs, `candidate_manifest.json`, `id_aliases.json`, editorial manifest, card summary, and primary-family summary;
- `bind_correction_inputs.py`, `build_cell_patch_ledger.py`, `build_successor_candidate.py`, `build_editorial_outputs.py`, `run_model_comparison.py`, `validate_successor_candidate.py`, `validate_editorial_outputs.py`, and `validate_model_comparison.py`;
- all post-v5 model-comparison summary, validation, manifest, core, factor, weighting, missingness, imputation, influence, and subspace outputs, plus `MODEL_COMPARISON_INTERPRETATION.md`;
- the immutable-v5 subspace-stability manifest, summary, validation, all 676 event leave-out rows, all 138 program rows, and all ten alternate-scenario rows;
- the relevant current-state portions of `CURRENT_WORK_STATE.md`, `PIPELINE_STATE.json`, the fairness scaffold, and the post-v5 README;
- every changed monograph span in the pinned correction candidate: version/date and atlas counts, the post-v5 checkpoint, the post-v5 model-comparison paragraph, its source-pointer paragraph, and the changed limitation text;
- all ten correction subjects: the nine patched events listed in the ledger plus the audit-preserved Indo-Aryan retirement.

The checked manifests' recorded hashes and authority flags were also compared with their local outputs. I did not use memory as evidence, browse the web, ask another agent, or rely on an external source not present in the opened local packet.

## Coverage and limits

### Explicitly covered

- All eleven load-bearing claim groups identified by the brief were checked: retirement, candidate counts, patch extent, aliases/dating, family changes, retained dimensionality, corrected-v5 geometry, factor interpretation, event influence, sensitivity/robustness limits, and card-model distinction/provenance.
- Every one of the 117 patch rows and every affected patch event was included in the ledger reconciliation.
- All changed monograph spans were compared against the exact local outputs named above.
- All required Batch 19–22 review, independent-review, and adjudication documents were included.
- Candidate records were checked not only for the new calibration fields but also for contradictory default narrative fields.
- Validators were read as code and their emitted validation outputs were checked; validation was not treated as proof of independent replication.

### Not opened or not re-reviewed

- The original scholarly source PDFs, publisher pages, and original-source funding/COI statements were not included in the required local evidence packet and were not opened. The review therefore tests fidelity to the local adjudications, not the underlying literature de novo.
- Unchanged monograph prose outside the changed spans was not re-fact-checked line by line. It was consulted only where necessary to establish the scope of a changed passage.
- Historical current-state archives not named by the brief were not exhaustively re-read; the current state files and relevant fairness material named above were checked.
- No release artifact, atlas build, deployment, publication package, or external website was inspected or authorized.

No skipped item above changes the blocker determination: SB-1 is demonstrated by conflicts between the active candidate records and the accepted local adjudications themselves.

## Fact-Check self-audit

| Audit item | Status | Emitted audit result |
|---|---|---|
| Grounding | PASS | Every finding is tied to opened local evidence named in the grounding statement; no memory or web evidence was used. |
| Claims | FINDING | SB-1, ME-2, and ME-3 identify unsupported or overbroad claims; checked numerical claims otherwise reconcile. |
| Deletions | PASS | No evidentiary qualifier needed by the accepted adjudications was silently deleted in this report's proposed wording. |
| Criticisms | PASS | Findings identify the exact field, sentence function, evidence limit, and minimum correction; no generalized criticism is substituted for evidence. |
| Internal consistency | FINDING | Active candidate records contain corrected calibration alongside contradictory legacy narrative fields. |
| Register discipline | FINDING | “Direct replication” and “source-honest” exceed the demonstrated posture. |
| Moral framework register | PASS — ZERO FINDINGS | No changed span introduces moral labeling in place of historical or statistical description. |
| Political-spectrum contamination | PASS — ZERO FINDINGS | No checked changed span imports partisan or political-spectrum framing. |
| Attribution posture | FINDING | Thutmose estate/labor context and Iberian genetic-lineage language are attributed at an unsupported cohort/actor level. |
| Quotations | PASS — ZERO FINDINGS | No direct quotation in the changed spans required correction; no quotation was used as a substitute for analysis. |
| Causal reasoning | PASS | The checked statistical text distinguishes subspace stability, axis rotation, and sensitivity; the proposed corpus edits remove unsupported causal implications. |
| Categorical vs dimensional | PASS | The report preserves the difference between family labels, trait scores, factor orientation, and subspace geometry. |
| Denotation/connotation/convenient layer | FINDING | Reader-facing legacy summaries connote demonstrated destinations, actors, victim cohorts, or durability beyond the denotational evidence in the calibrations. |
| Proper-name variants | PASS — ZERO FINDINGS | The two Assyrian identifier aliases preserve traceability while neutral successor identifiers avoid pretending the disputed year is settled. |
| Engagement posture | PASS | Accepted reviews and adjudications were tested against outputs rather than merely repeated; disagreements are stated directly. |
| Confidence calibration | FINDING | Thutmose and several other legacy fields express more confidence/specificity than the accepted evidence permits; model-comparison confidence is otherwise bounded appropriately once ME-2/ME-3 are edited. |
| Fetched-source disclosures | LIMITATION | No source was fetched. Original-source funding/COI disclosures were not in the local packet and remain unverified; this limitation is explicit. |
| Citation resolution | FINDING | The source pointer immediately following the post-v5 paragraph resolves to the earlier v5/676 analysis instead of the direct post-v5 outputs. |
| Adopted reviewer text | PASS | No target text was changed and no reviewer prose was silently adopted; all wording appears only as clearly labeled minimal proposals. |
| Editorial synthesis (SYNTH) | PASS — ZERO FINDINGS | No unsupported synthesis, artificial consensus, or cross-source conclusion beyond the opened adjudications and outputs was introduced. |

## Final findings-only boundary

This Stage 1 report records evidence findings and minimum proposed edits only. It does not approve the candidate, resolve SB-1, alter any target, authorize release or atlas changes, authorize deployment, stage files, or create a commit.

## Sole file changed

`/Users/talbert/settler colonalism visualization/analysis/second_pass/v5/post_v5_correction_application_v1/editorial_suite_final_v1/FACT_CHECK_FINDINGS.md`
