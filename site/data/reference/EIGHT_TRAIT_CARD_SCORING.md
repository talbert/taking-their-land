# Eight-trait case-card scoring

**Checkpoint date:** 2026-08-20  
**Status:** evidence-aware card model v2 adopted as the working card data model;
seven bars use cross-snapshot factor anchors and one uses a direct evidence-
gated codebook trait; no atlas UI change, event activation, parent retirement,
or canonical-corpus change

## Decision in plain language

The public card should answer a direct question: **how strongly is each trait
demonstrated in this event?** It should not answer the different question,
“where does this event rank among whichever cases happen to be in the current
dataset?”

The working score is therefore a weighted 0–100 summary of source-coded
historical judgments. It travels with an evidence-coverage value and a
conservative unknown range. Unknown evidence is never silently treated as a
low trait value.

This decision preserves the approved editorial model:

1. one manually reviewed primary family;
2. several plain-language mechanism tags; and
3. a prominent eight-bar analytical profile.

The card is a set of interpretable lenses, not a claim that history contains
exactly eight natural kinds.

## Methods considered

### Re-running exploratory factor percentiles

The existing `results/eight_trait_card_values.csv` converts each exploratory
factor score to a percentile. That is useful for analysis, but adding cases can
rotate the factors and move an unchanged event's apparent card. It is not a
stable publication scale.

### Frozen regression projection

`29_build_frozen_eight_axis_scores.py` froze the active-490 medians,
standardization, regression weights, axis alignment, and percentile reference.
It succeeds technically:

- active scores reproduce to within `4.44e-16`;
- unchanged shared rows move by exactly zero;
- the active-490 and repaired-407 frozen references give full-candidate rank
  correlations of at least `0.913`; and
- full-candidate correlations with local exploratory solutions remain useful
  diagnostics.

It nevertheless fails as a public scale. Regression scores are latent
coordinates, median treatment pulls unknown dimensions toward the center, and
percentiles express corpus rank rather than substantive intensity. Praeneste's
documented massacre, for example, lands at the 12th percentile on lethal
coercion, with a source-uncertainty span from approximately the 0th to the 73rd
percentile. The ordering relative to non-lethal Volaterrae is technically
correct, but the absolute bar would communicate the wrong thing.

The frozen regression outputs are retained as a rejected diagnostic comparator
under `frozen_eight_axis/`. They must not drive reader-facing bars.

### Cross-snapshot consensus anchors and the direct F7 correction

`30_build_eight_trait_card_model.py` implements the adopted working method.
For seven factor-informed traits it selects dimensions that:

- load at an absolute value of at least `0.30` in both the repaired 407-event
  and active 490-event models;
- keep the same direction in both models; and
- rank among the ten strongest surviving dimensions for that trait.

Each selected dimension receives the mean of its two absolute loadings as its
weight. Dimensions with negative loadings are reversed so that a higher final
bar always means “more of the named trait.” The event's known applicable
judgments are averaged and rescaled from the codebook's 0–4 scale to 0–100.

The first version applied this rule to all eight factors. Manual Roman review
then exposed a face-validity failure in the statistical F7: it mixed relocation
distance and destination conditions with reversed land-conversion and frontier
dimensions. Volaterrae could therefore receive a high displacement bar even
though the source coding explicitly says that residents were not physically
removed. That was a data-model problem, not a wording problem.

Version 2 retains the statistical F7 only as a diagnostic. The public seventh
bar is now the direct codebook trait **Separation from homeland**, using equal
weights for displaced relocation distance and foreclosure of return. If
relocation distance is structurally not applicable because there was no
displaced population, the bar is suppressed rather than manufactured from
other factors.

This is not a new round of subjective recoding. All eight bars are transparent
summaries of the sixty already reviewed codebook judgments. Six preserve
cross-snapshot factor structure. F7 and F8 deliberately privilege literal
historical meaning over statistically mixed latent factors.

## The eight traits

| Trait | Reader-facing label | A high bar means | Anchors |
|---|---|---|---:|
| F1 | Government direction | More centralized, explicit, and continuously state-directed organization | 10 |
| F2 | Legal and property machinery | More formal expropriation, title transfer, surveying, registration, and legal instrumentation | 10 |
| F3 | Settler implantation | A larger, more family-complete, self-reproducing, and durable incoming resident population | 8 |
| F4 | Elimination over incorporation | More removal and demographic replacement, with less incorporation of the prior population | 7 |
| F5 | Lethal coercion | More killing, life-threatening coercion, confinement, and destruction of subsistence | 7 |
| F6 | Durability of outcome | A more persistent territorial, sovereign, and demographic result with less reversal or return | 7 |
| F7 | Separation from homeland | Displaced people were carried farther from home and return remained more completely blocked | 2 |
| F8 | Imported unfree labor | A larger distinct population was brought from elsewhere as enslaved, indentured, or otherwise unfree labor | 2, with an applicability gate |

The exploratory statistical F7 and F8 remain available for diagnosis but are
not the reader-facing traits. The corrected public F8 is an applicability-
gated direct construct. Its frozen v2 comparison, eight-case adjudication
queue, and implementation audit are documented in
`v5/eight_trait_card_f8_review/F8_IMPORTED_UNFREE_REVIEW_v2.md`.

## Exact anchor set

The model JSON preserves weights, directions, and loadings. The selected
dimensions are:

- **F1 — Government direction:** `pel_organizing_agent_locus`,
  `ssi_carrier_centralization`, `gfm_perpetrator_state_centrality`,
  `scs_metropole_anchorage`, `gfm_intent_legibility`,
  `scs_settler_agency_locus` (reversed), `ssi_settler_polity_autonomy`
  (reversed), `pel_strategic_position_weight`, `gfm_displacement_tempo`, and
  `ssi_legibility_engineering`.
- **F2 — Legal and property machinery:**
  `pel_title_transfer_formalization`, `gfm_expropriation_formalization`,
  `ssi_legal_instrumentation_depth`, `pel_land_commodification`,
  `scs_land_tenure_extinguishment`, `ssi_legibility_engineering`,
  `pel_fixed_capital_intensity`, `ssi_legitimating_doctrine_codification`,
  `pel_export_orientation`, and `scs_transfer_mode_multiplicity`.
- **F3 — Settler implantation:** `hdem_migrant_stream_family_completeness`,
  `scs_settler_permanence_orientation`, `hdem_stream_coordination`,
  `hdem_settler_reproduction_engine`,
  `hdem_incomer_share_at_consolidation`, `scs_demographic_saturation`,
  `pel_frontier_land_labor_ratio`, and `scs_settler_agency_locus`.
- **F4 — Elimination over incorporation:**
  `hdem_prior_ancestry_in_successor_population` (reversed),
  `pel_native_labor_incorporation` (reversed),
  `hdem_prior_population_removal`, `scs_native_labor_articulation`,
  `gfm_displacement_tempo`, `hdem_transformation_tempo`, and
  `scs_demographic_saturation`.
- **F5 — Lethal coercion:** `gfm_lethality_of_process`,
  `hdem_mortality_share_of_prior_decline`, `gfm_subsistence_destruction`,
  `gfm_coercion_apex`, `gfm_survivor_confinement`,
  `scs_transfer_mode_multiplicity`, and `gfm_sex_differential_targeting`.
- **F6 — Durability of outcome:** `ssi_sovereignty_outcome_durability`,
  `scs_structural_persistence`, `hdem_present_day_endpoint`,
  `gfm_return_foreclosure`, `hdem_transformation_tempo`,
  `pel_incomer_influx_tempo`, and `scs_settler_sovereignty_capture`.
- **F7 — Separation from homeland:**
  `hdem_displaced_relocation_distance` and `gfm_return_foreclosure`, with
  equal weights. Structural N/A on relocation distance suppresses the bar.
- **F8 — Imported unfree labor:** `scs_exogenous_labor_triad` is the
  applicability gate. When applicable, it is combined with
  `pel_unfree_incomer_share`. Unknown applicability suppresses a solid point;
  structural N/A suppresses the bar. A source-bounded event whose defining
  mechanism is imported unfree labor may receive an explicit applicability
  exception when the triad is N/A solely because no settler population exists.

## Evidence and display rules

For F1–F7, and for F8 once applicability is established:

- **Intensity** is the weighted mean of known applicable anchors, shown on a
  0–100 scale and rounded to the nearest five for display.
- **Evidence coverage** is the known anchor weight divided by all applicable
  known-plus-unknown anchor weight.
- **Structural not applicable** is removed from the denominator. It is not
  uncertainty and is not scored as zero.
- **Unknown range** sets every unknown applicable anchor to zero for the lower
  bound and four for the upper bound. This is a conservative evidence range,
  not a statistical confidence interval.

The UI contract is:

| Coverage | Required treatment |
|---:|---|
| 80–100% | Show the rounded point bar; retain coverage in the detail/audit view |
| 60–<80% | Show a visibly uncertain range with the known-evidence estimate marked inside it |
| <60% | Do not show a solid point bar; show insufficient evidence and the bounded range |

The central estimate remains in the data for comparison and review even when
the UI is prohibited from rendering it as a confident point.

## Validation

The working model passes all current gates:

- all ten source-grounded semantic comparisons pass, together with two direct
  F7 applicability checks;
- minimum rank correlation with the validated active-490 factor scores is
  `0.847`;
- minimum rank correlation with the named axes in the full-candidate
  nine-factor diagnostic is `0.826`;
- minimum full-candidate correlation between anchor sets selected separately
  from the 407- and 490-event snapshots is `0.813`;
- all seven factor-informed validation families clear the predeclared `0.80`
  floor;
- unchanged active/full shared rows differ by exactly zero; and
- shared parent-only/full rows differ by exactly zero.

The direct F7 intentionally does not clear a factor-correlation gate, because
it replaces that statistical factor's mixed meaning. Its acceptance tests are
literal applicability and source-grounded case comparisons instead.

The case-level checks preserve distinctions the regression prototype blurred:

| Case | Settler implantation | Lethal coercion | Separation from homeland | Evidence treatment |
|---|---:|---:|---:|---|
| Carthage destruction, 149–146 BCE | 0 | 75 | 100 | F5 range required; F7 is a 50–100 bound with no solid point |
| Junonia allotments, 123–111 BCE | 75 | 10 | unknown | F3 range required; F7 remains wholly unknown rather than inheriting the earlier destruction |
| Praeneste, 82–80 BCE | 60 | 55 | 25 | F3/F5/F7 have insufficient evidence for solid bars |
| Volaterrae, 82–45 BCE | 0 | 10 | 0 | Supported points; legal confiscation is not mislabeled as displacement |
| Uganda Asian expulsion, 1972 | 0 | 30 | 90 | Supported point; long-distance expulsion and blocked return register strongly |
| Uninhabited Bermuda/Caymans | 85 | 45 | — | F7 is structurally not applicable because nobody was displaced |

## Coverage implications

The active 490-event corpus already has strong coverage for government
direction, legal/property machinery, and durability. It has fewer sufficiently
documented bars for elimination and lethal coercion:

| Trait | Active cases below 60% coverage | Roman 95 below 60% coverage | Active structural N/A |
|---|---:|---:|---:|
| F1 Government direction | 0 | 0 | 0 |
| F2 Legal/property machinery | 1 | 0 | 0 |
| F3 Settler implantation | 24 | 71 | 0 |
| F4 Elimination over incorporation | 59 | 59 | 0 |
| F5 Lethal coercion | 95 | 39 | 0 |
| F6 Durability | 0 | 4 | 0 |
| F7 Separation from homeland | 73 | 64 | 2 |
| F8 Coerced outside labor | 12 | 7 | 0 |

The Roman deficit is historically informative: many sources securely document
a colony, confiscation, or state act while not supporting household structure,
resident ancestry, population removal, or mortality shares. Those cases should
look evidentially incomplete until research fills the gap; they should not look
substantively mild.

## Artifacts and status

- `29_build_frozen_eight_axis_scores.py` and `frozen_eight_axis/` preserve the
  rejected regression diagnostic.
- `30_build_eight_trait_card_model.py` is the working card builder.
- `eight_trait_card/eight_trait_card_model.json` is the complete machine-
  readable scoring contract.
- `eight_trait_card/active_490_eight_trait_card.csv`,
  `parent_only_546_eight_trait_card.csv`, and
  `full_583_eight_trait_card.csv` are the versioned case tables.
- `trait_model_stability.csv`, `anchor_snapshot_sensitivity.csv`,
  `evidence_coverage_summary.csv`, and `case_semantic_checks.csv` preserve the
  validation record.
- `results_manifest.json` hashes every input and output.

This checkpoint freezes a working display-score rule only. The active corpus
remains 490. The Roman 546- and 583-event candidates remain inactive. No atlas
file has been changed.

## Subsequent release status

On 2026-08-20, the full 583-event card table was copied unchanged into active
statistical release `second_pass_v3_583`. Its scoring and evidence rules remain
the working UI contract. The atlas still has not been changed; see
`SECOND_PASS_V3_RELEASE.md`.
