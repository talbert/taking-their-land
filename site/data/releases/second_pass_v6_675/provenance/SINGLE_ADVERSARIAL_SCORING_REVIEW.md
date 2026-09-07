# Single adversarial scoring review and adjudication

**Completed:** 2026-08-28

**Reviewer:** bounded read-only subagent `01a04926-749c-7bb2-8e9c-014a89ab4aea`
(`Helmholtz the 2nd`)

## Scope

The reviewer received the fixed ten-event roster, the Batch 19–22 source
reviews and adjudications, the 60-dimension codebook, and the immutable v5
rows. It was forbidden to conduct new historical research, edit files, or
audit the source reviews recursively. Its task was only to challenge the
translation from accepted findings into exact score/unknown/N/A changes.

## Result

The review accepted the Indo-Aryan retirement, the two chronology-neutral
Assyrian successor IDs, all three family changes, and the 675-event arithmetic.
It proposed a narrower evidence-preserving cell ledger than the main draft.

The executable adjudicated ledger contains **117 changes across nine retained
events**:

- 104 values become evidence-unknown (`U`);
- one Iberian applicability value becomes structural N/A;
- eight campaign-tempo values become 3 rather than the overprecise 4;
- two captive-removal transfer-mode values become 1; and
- two Assyrian killing-plus-removal transfer-mode values become 2.

The tenth event, `atlas-indo-aryan-migration`, is retired from the active model
but preserved with its complete old row as inactive audit data.

## Reconciliation against the main draft

The first main proposal contained 153 changes. The final ledger and that draft
share 94 target cells; the final review removes 59 proposed changes, adds 23
better-targeted changes, and changes four proposed local-labor scores from 3
to `U`.

The 59 removals are deliberate evidence preservation, not unfinished work.
The first draft would have erased several raw facts merely to suppress a
misleading composite bar. The final adjudication instead retains, where the
codebook and bounded source findings support them:

- captive status in `pel_unfree_incomer_share` without claiming a labor
  assignment;
- contiguous imperial geography without claiming a captive destination;
- attested de facto seizure, tribute, booty, and conquest-title context
  without inventing cadastral machinery;
- direct sub-five-year demographic pulses without claiming long-term
  durability;
- score 0 for settler agency or sovereignty where the codebook explicitly
  permits the no-settler/no-sovereignty condition; and
- documented sex categories where the accepted review did not require the raw
  judgment itself to be withdrawn.

The 23 additions correct cells the first draft missed, most importantly:

- annual or two-season campaigns are acute (`3`), not demonstrated
  days-to-weeks operations removing most of a group (`4`);
- royal capture without destination assignment is not automatically a
  state-placed migrant stream;
- a commemorative royal inscription is not an operative legal instrument;
- the Thutmose cohort's later legal status is unknown; and
- killing plus physical prisoner removal are two documented transfer modes in
  the Nipur and Nimme/Tummu events.

The four local-labor disagreements are resolved to `U`. Tribute or corvée
shows an incorporation relationship, but the reviewed passages do not show
that prior-population labor was the principal workforce or the prize itself.
The case prose and primary family preserve incorporation without manufacturing
an economic share.

## F8 consequence

The reviewer correctly identified a model-label issue: a known unfree captive
share is not the same claim as a known coerced-labor assignment. The final
ledger therefore preserves directly supported `pel_unfree_incomer_share`
values. It removes unsupported household/third-population claims where the
review requires that action. Low evidence coverage prevents an F8 solid point.

This is a useful monograph example of why the eight traits are summaries rather
than interchangeable source facts. A future semantic review may add a direct
labor-evidence gate, but this finite correction cycle must not destroy known
evidence merely to force a label to behave.

## Closed gate

This is the one authorized adversarial scoring review. Its findings are
adjudicated in `build_cell_patch_ledger.py`, `CELL_PATCHES.csv`, and
`CELL_PATCH_SUMMARY.json`. No second scoring audit is required. Subsequent work
is deterministic application, model comparison, and one final Editorial Suite.
