# Reproduction packaging sidecar

Ownership: model implementation owner, **not** independent verifier of this
artifact. The closed model_verification_v1 review is unchanged. This is bounded
packaging, not a new historical/scientific gate. No fits, commits, public deposit,
activation, global-state change or promotion are performed here.

All source files are selected from the completed run's explicit bindings plus
the small direct-loader/notices supplement. No glob-copy or nested evidence-path
chase occurs. Bound bytes/project-relative paths remain unchanged. The existing
mixed-license notices govern originals; third-party quotations are excepted.

Artifacts:

- SOURCE_MAP.json: explicit source paths, roles, sizes and SHA256; unshipped
  build-only RESULT/closed-verification receipt bindings.
- EXPECTED_FINGERPRINTS.json: compact expectations for the actual565 matrix
  records, including row/authority/date hashes; not another numerical fit result.
- numerical_reproduction_20260907a.zip: owner-only deterministic private export.
- BUILD_RECEIPT.json and TEST_RESULTS.json: finite packaging/isolated-test receipts.
- EXPORT_README.md and LOADER_DEPENDENCIES.md: consumer directions and inspected
  loader/root boundaries. ZIP README.md is an exact copy of EXPORT_README.md.
- build_export.py, portable_preflight.py and test_export.py: implementation.

Builder commands from this source sidecar: `python -B build_export.py --plan`
prints generated plans; save those text outputs explicitly after inspection.
`--build` writes only the allowlisted ZIP inside this directory and refuses to
overwrite a differing ZIP. `--check` regenerates it in memory and checks exact
bytes/0600 mode. It never imports the historical runner or numerical libraries.
Replacing an unaccepted development ZIP requires the explicit
`--replace-existing-sha256` matching that exact owned file; it is not a general
overwrite switch and never targets consumed inputs.
The isolated test uses temporary extraction directories under this owned lane,
not OS-only tmp, and removes those temporary copies when finished.

The ZIP excludes full RESULTS/cache bodies and runtime binaries. Consumer setup
is in EXPORT_README.md. Exact consumed input/loader closure and565 fingerprints
are the test target; numerical refits, all-platform bitwise reproducibility and
reproduction of upstream historical research are explicitly outside this task.

## Completed implementation handoff

PACKAGING_TESTS_PASS:91 unchanged source files,99 ZIP members,7,559,024 bytes,
owner-only0600. Isolated63-input loading/all255 preflights and all565 matrix
fingerprints (536 unique cases) match. Zero factor/Horn/cluster fits; prescribed
KNN preprocessing only. The temporary extraction is removed. Deterministic byte
regeneration and malformed-path/hash/missing-dependency/root-marker tests pass.

ZIP SHA256:
`036f1e6937eb315208dd25512a707168b6adf4b1fd82e5b3e33be2e3a4bca229`

The original-project read guard permits the explicitly selected numerical
Python software prefix when it lives under project tmp; no research-input
fallback is permitted. Python's read-only platform probe is initialized before
the strict side-effect guard. This launcher-only adjustment superseded the
unaccepted first ZIP, without touching any consumed file or closed verification.
