# Stage 1 fact-check adjudication

Date: 2026-08-28
Stage: Editorial Suite 1 of 3
Disposition: all substantive and mechanical findings accepted and repaired once
Recursive review authority: none

## Decision

The Stage 1 report is accepted. Its central finding was correct: the candidate's
new calibration fields and cell corrections were source-adjudicated, but seven
records still exposed older default narrative fields that overstated or blurred
the accepted Batch 19-22 evidence limits. The numerical model comparison itself
had no Stage 1 blocker.

The repair was made at the reproducible source in `CORRECTION_PLAN.json`, not by
editing generated outputs. Immutable `second_pass_v5_676` remains unchanged and
therefore preserves the superseded wording for audit. The successor builder now
regenerates one internally consistent reader-facing account for each affected
record.

## Finding dispositions

### SB-1 - accepted and repaired

All public default `name`, `mechanism`, `agents`, `victims`, `summary`, and
`confidence` fields that conflicted with the accepted source calibration were
replaced for the seven records identified by the reviewer:

- Iberia now describes migration, coexistence, admixture, and sex-biased
  ancestry/Y-chromosome lineage turnover. It does not turn a lineage into an
  actor, manufacture a bounded victim cohort, or infer killing, expulsion, or
  residential displacement.
- Thutmose III now distinguishes the 340 living Megiddo battle prisoners from
  the separately attributed 2,503-person multi-town list. Its actors are the
  king and army; exact destination institutions and cohort-specific labor remain
  unknown.
- Amenhotep II Year 9 now treats Memphis only as the king's recorded return
  point, preserves the 89,600 versus 101,128 contradiction, and keeps the
  separate list non-additive.
- Nipur-Pasate and Nimme/Tummu-Habhu now state the ORACC 882/Sano 883
  disagreement, separate military claims, prisoners, submitters, and corvee,
  and leave prisoner destinations unknown.
- Upper Tigris/Nirbu now names killed cohorts, carried prisoners, Assyrian
  famine returnees at Tushha, local Nirbu returnees, hostages, and Ispilipria
  fugitives as distinct trajectories.
- Zamua now uses narrowly attributed killing, prisoner-taking, destruction, and
  vassal-incorporation language. It identifies every human number as military,
  `150` as a non-additive city count, and does not infer durable depopulation or
  settler implantation.

The one nonempty duplicate `event_json_summary` field, for Amenhotep II Year 9,
was corrected at the same time. No contradictory legacy default field remains
in the regenerated candidate records checked above.

### ME-1 - accepted, with path correction

The monograph now binds the post-v5 paragraph directly to the actual generated
paths:

- `analysis/second_pass/v5/post_v5_correction_application_v1/candidate/post_v5_corrected_successor_675/results/post_v5_model_comparison_v1/MODEL_COMPARISON_SUMMARY.json`
- `analysis/second_pass/v5/post_v5_correction_application_v1/MODEL_COMPARISON_INTERPRETATION.md`

The first path proposed in the report omitted the real `candidate/...` segment;
the adjudication uses the path that exists. The older v5 sources remain cited
only for the preceding v5 candidate claims.

### ME-2 - accepted and repaired

“Direct replication” was replaced with “additional bounded post-v5
perturbation check.” The comparison reuses the project's established machinery
and is not represented as an independent implementation.

### ME-3 - accepted and repaired

“No corrected event is individually material” was replaced with the result the
test actually establishes: none of the nine leave-one-corrected-event-out
scenarios crossed the declared materiality thresholds. The interpretation file
also states that this design does not isolate the effect of a correction from
the effect of omitting its event.

### Register finding - accepted and repaired

The changed monograph text now says “source-adjudicated roster and cell
corrections,” not the broader “source-supported” or “source-honest” wording.

## Regeneration and validation

After the source-plan repair:

- the 675-active-event / 748-row successor candidate rebuilt and reproduced;
- all 117 adjudicated cell patches and the Indo-Aryan retirement remained
  unchanged;
- candidate validation passed;
- the family and eight-trait editorial outputs rebuilt, reproduced, and passed;
- the bounded model comparison rebuilt and reproduced byte for byte;
- the deterministic model-relationship validator passed;
- factor counts, angles, family counts, and interpretation remained unchanged.

The model artifacts changed only where their manifests bind the corrected input
hashes. No statistical value was altered by this narrative repair.

## Closed boundary

Stage 1 is closed. These findings will not be sent through another fact-check
cycle. The repaired state proceeds once to Stage 2 (LLM-artifact tells), then
once to Stage 3 (calibration review), in the user-specified order. Neither stage
may reopen accepted historical source questions unless it identifies a concrete
contradiction in the repaired files.
