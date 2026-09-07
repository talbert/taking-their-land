# Post-v5 correction model comparison

Date: 2026-08-28
Status: bounded diagnostic complete and validated; successor promotion still
requires the final Editorial Suite and immutable-release build.

## Question

Do retirement of the broad Indo-Aryan wrapper and the 117 adjudicated cell
corrections materially change the structure reported in immutable
`second_pass_v5_676`?

## Answer

They do not change the retained factor count or the nine-dimensional factor
space materially. They do expose the already documented instability of
assigning fixed names to only eight axes when parallel analysis retains nine.

- Immutable v5 and the corrected 675-event candidate both retain **nine
  factors** under the canonical global-median preprocessing.
- The corrected candidate's ninth-factor Horn margin is `+0.064879`, compared
  with `+0.029928` in the recomputed immutable base. The correction therefore
  does not push the ninth factor below the line.
- The maximum principal angle between the v5 and corrected
  **nine-dimensional spaces is 2.765 degrees**; the minimum principal-angle
  cosine is `0.998836`. Best-matched nine-factor loading axes have minimum
  Tucker congruence `0.999271`.
- The corresponding forced-eight maximum angle is **6.685 degrees**. A
  comparison that insists on v5's eight historical labels consequently gives
  very low same-name scores for three factors even though best-matched
  eight-factor axes have minimum Tucker congruence `0.997023`.
- The six-cluster partition changes for 8 of 675 shared events (`1.19%`;
  adjusted Rand index `0.9772`).
- Retiring the Indo-Aryan wrapper by itself is negligible. It retains nine
  factors, has minimum named-axis Tucker `0.9997`, and produces a
  nine-dimensional maximum principal angle of `1.063` degrees.
- None of the nine leave-one-corrected-event-out scenarios crosses the
  declared materiality thresholds. This test does not isolate each correction
  from the effect of omitting its event.

The **nine-factor subspace remains stable, while forcing eight factors rotates
the axes**. The low same-name F2/F7/F8 comparisons are not
evidence that those historical constructs disappeared. They show that an
eight-axis solution can repartition a boundary-sensitive ninth direction.

## What this does and does not authorize

The source-adjudicated `U` and `NA` corrections should not be reversed to make old
factor names appear stable. In particular, known captive movement remains
coded where the source establishes it; unsupported labor use, permanence,
return, descendants, and demographic consolidation are not manufactured.

The public eight-trait card also should not be described as eight newly fitted
latent factors. Its traits are frozen, interpretable summaries built from the
sixty coded dimensions and evidence-coverage rules. The statistical model is
a diagnostic of covariance structure, while the card is a reviewed editorial
measurement interface.

This result does **not** establish a unique natural taxonomy or erase the
release's broader sensitivity to corpus composition and missing-data
treatment. The same sensitivities already present in v5 remain visible:

- equal-era weighting retains eight factors and moves the nine-dimensional
  space by `26.987` degrees;
- era-specific median imputation retains eight and moves it by `32.608`
  degrees;
- the unknown/structural-NA KNN alternative retains eight and moves it by
  `25.249` degrees;
- the structural-zero bound retains eight and moves it by `70.014` degrees;
  and
- strict documentation-complete subsets are structurally different samples,
  while the subset allowing up to forty missing cells returns within `4.742`
  degrees of v5 in nine dimensions.

These are not new defects caused by the ten-event correction queue. The
corresponding immutable-v5 sensitivity angles were `26.539`, `36.124`,
`24.977`, and `71.313` degrees for equal-era weighting and the three listed
imputation alternatives. The corrected release must retain the existing
qualification: the canonical covariance structure reproduces, but its factor
count and axis allocation remain entangled with corpus composition and what
the sources permit coders to know.

## Monograph consequence

The successor-release account should say all of the following together:

1. the source-driven corrections leave the canonical nine-factor result and
   nine-dimensional space intact;
2. same-name forced-eight diagnostics are misleading at the eight/nine
   boundary unless accompanied by a subspace comparison;
3. the public eight traits are interpretable summaries rather than a claim
   that the latest factor analysis discovered exactly eight natural kinds;
4. roster, weighting, missingness, and imputation alternatives remain material
   limitations; and
5. statistical stability is not what decides whether a historically warranted
   event is included, retired, split, or held.

## Reproducible record

- Builder: `run_model_comparison.py`
- Deterministic relationship validator: `validate_model_comparison.py`
- Results: `candidate/post_v5_corrected_successor_675/results/post_v5_model_comparison_v1/`
- Adjudicated scoring record: `SINGLE_ADVERSARIAL_SCORING_REVIEW.md`
- Patch ledger: `CELL_PATCHES.csv`

The model builder reproduces byte for byte under `--check`; the independent
relationship validator passes. Neither file grants release, atlas, or
deployment authority by itself.
