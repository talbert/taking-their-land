# Reproducing the two-event chronology addendum

This archive is sufficient for the numerical input/code path without the
private project or its research cache. It contains all99 original numerical
export members unchanged, plus a finite two-event metadata supplement and
storage adapter. Read the original `README.md`, licenses and third-party
notices first. The `.git` member is a plain-text root marker, not Git history.
Extract into a NEW empty owner-only directory, never over a working checkout.

Original software is MIT; original structured data is CC BY4.0; original prose
is CC BY-SA4.0. Embedded third-party excerpts retain their own rights. No source
PDFs, screenshots, raw coder journals, credentials, runtime binaries or research
caches are included. Metadata references to unshipped historical evidence do
not authorize recursively fetching or publishing it.

## Read-only check — no historical result/cache required

Install the exact six package versions from `requirements-reproduction.txt`
in a separate Python environment. The original run used CPython3.9.6, macOS
arm64, and the recorded numerical libraries. From the extracted root:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 BLIS_NUM_THREADS=1 PYTHONHASHSEED=0 python -B replay_date_addendum.py
```

Leave OMP_DYNAMIC and MKL_DYNAMIC unset, as in the original run. This command
checks both archive manifests, loads the accepted inputs, applies precisely
the La Gomera and West Bank date metadata, and reconstructs the two changed
matrix fingerprints. It checks629 eligible nominal onsets and0 measured
durations. It blocks writes, network, factor estimators and simulations. It
does NOT rerun the565 scenarios, compute fits, validate historical sources,
or pretend that a successful input check reproduces numerical results.

## Full reproduction — explicit, potentially expensive

The original run's unexported intermediates are factor scores and typed fitted
objects, not merely its public loadings. The addendum needs those to reproduce
date associations while reusing historical fits. They must first be recreated
locally by the unchanged original numerical runner; there is no private-cache
fallback and no hidden download. **Do not do this to resume our completed
project run. These commands are for a separate consumer reproduction.**

1. Optionally run `portable_preflight.py` as described in the original README.
   It checks all565 original matrix fingerprints without any numerical fits.
2. Reproduce the original cycle in the following fresh directory. Its accepted
   scores, missingness, dates and methods remain unchanged:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 BLIS_NUM_THREADS=1 PYTHONHASHSEED=0 python -B analysis/second_pass/v6/post_v6_correction_application_v1/model_execution_v1/run_successor.py --acceptance analysis/second_pass/v6/post_v6_correction_application_v1/complete_candidate_v1/complete/ACCEPTANCE.json --acceptance-sha256 404a93c084fc034f69caa187790ba6e4d12f8103b36e43568c9c2c2615ab8ba9 --execute --output analysis/second_pass/v6/post_v6_correction_application_v1/model_execution_v1/reproduced
```

3. Once that run is complete, explicitly execute the addendum:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 BLIS_NUM_THREADS=1 PYTHONHASHSEED=0 python -B replay_date_addendum.py --execute
```

The addendum verifies the completed historical result hash and typed cache
identity/payloads, reuses its fits, and computes only two new unique matrices
(fourteen scenario aliases) plus511 amended date records. It writes only
`analysis/second_pass/v6/post_v6_correction_application_v1/release_assembly/publication_integration/date_addendum/reproduced_addendum/`.
For either interrupted run, first confirm its prior writer stopped, then use
the SAME command/environment with `--resume`. Completed outputs are immutable.

The source adapter preserves the original scientific functions unchanged;
only root discovery, the finite metadata dependency, historical-fit storage
and the output directory differ. `DATE_ADDENDUM_EXPORT.json` binds every other
member and identifies the original runner. No fit/coding/admission/family
decision is made by assembling or testing this export.

## Comparison and limits

Expected historical `RESULTS.json` SHA256:
`91cd3d38aaf3bae80a4d7972c935d020bd48c56e4e78d0cada34104ecd5008f9`.

Expected addendum `RESULTS.json` SHA256:
`56a3a5db90f84c1e8691160ed6eb565b30df60f5f8062eb4bbb8a1d44c745287`.

New absolute paths/runtime metadata mean the new run MANIFEST/RUN_STATE hashes
will differ. The scientific result hashes above do not contain those paths.
All-platform bit identity is NOT established: transitive wheels, BLAS and OS
build chains are not fully locked. If a numerical result differs, preserve it
and report the environment/difference; do not relax hashes or substitute it
as the accepted result. The exact-match addendum adapter deliberately stops
on historical numerical drift. A new platform/tolerance study is separate.

This packaging check does not execute a second full565-scenario cycle. The
completed original run and accepted addendum remain separately published
evidence, not replaced by a successful portability/input check. Nothing here
activates a release, deploys a website, switches GitHub public or publishes the
unpublished Zenodo draft.
