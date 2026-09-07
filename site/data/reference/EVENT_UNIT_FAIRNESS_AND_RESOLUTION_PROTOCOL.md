# Event-unit fairness and resolution protocol

Status: required pre-publication gate, adopted 2026-08-23; complete mechanical
intake and calibration sample built, substantive review not yet run

Execution amendment: the substantive burden is unchanged, but reviewer
packaging and verification now follow
`event_unit_fairness_v1/STREAMLINED_EXECUTION_PLAN.md` under the 2026-08-25
assurance-streamlining standard.

Applies to: the next promoted statistical release, monograph v2, and every
later release that adds, removes, splits, or merges events

## The question this protocol must answer

The project gives one statistical row to one bounded historical event. That is
only a fair design if equivalent editorial rules determine what receives a
row. Equal row weights do not correct a roster in which an archive-rich
campaign has been split into many children while an archive-poor process of
similar structure has been collapsed into one umbrella.

The defensible publication claim is not that event boundaries are objectively
or mathematically bias-free. Historical events are interpreted units. The
claim this project must earn is narrower and testable:

> Event boundaries were defined by a published causal and territorial rule,
> applied with era-appropriate evidence, independently reviewed for asymmetric
> splitting and collapsing, protected against parent/child double-counting,
> and tested under plausible alternative resolutions. Material sensitivity or
> unresolved disagreement is disclosed rather than hidden.

The monograph may not make that claim until every release gate below is
complete.

The audit distinguishes two layers. **Boundary fairness** asks whether each row
is one comparably reasoned event and whether any history is counted twice.
**Measurement fairness** asks whether the sixty traits can be scored from the
evidence available for that era without treating undocumented as absent. A
release must pass both. Strong era-aware coding cannot repair an inconsistently
split roster, and a clean roster cannot repair anachronistic coding anchors.

## Historical tempo: calendar duration is not the unit rule

No fixed number of days, years, decades, or generations defines an event. A
movement visible only as a centuries-wide archaeological horizon in 6000 BCE,
a campaign reported season by season in 338 BCE, and a removal documented day
by day in 2014 have different temporal resolution and different historically
possible tempos. Making each row cover the same number of years would create,
not remove, bias.

Chronology is therefore one diagnostic among several. A gap triggers review
when it may indicate a new actor, program, affected population, mechanism,
territory, or causal sequence. It does not force a split by itself. Conversely,
events close in calendar time may require separate rows when those other
features differ. Travel speed, communications, administrative capacity,
generational turnover, and the dating precision of the evidence belong in the
boundary rationale; none is a universal conversion factor.

## The event-unit test

A row represents one linked land or population transition. Every active event
must have an auditable disposition on the following questions:

1. **Actor or program continuity.** Is the organizing actor, institution, or
   population stream substantially continuous?
2. **Affected population and land.** Is there a bounded resident population,
   source community, or tract whose outcome can be described without borrowing
   evidence from a different place or group?
3. **Mechanism continuity.** Are conquest, flight, deportation, settlement,
   land transfer, labor removal, return, and other mechanisms parts of one
   causal transition, or separate processes merely adjacent in a narrative?
4. **Causal and institutional linkage.** Do the phases implement one decision,
   campaign, law, commission, settlement program, or connected transformation?
5. **Geographic coherence.** Can the affected land and routes be represented
   without making a regional umbrella stand in for independently varying local
   histories?
6. **Independent analytical profile.** Does a proposed child have enough
   evidence to support its own sixty-dimension profile? More surviving detail
   is not, by itself, evidence of a distinct event.
7. **Outcome and reversal.** Are removal, replacement, return, reoccupation,
   or reversal phases of the same transformation, or do they begin a new
   process with materially different actors or land outcomes?
8. **Supersession and overlap.** If a parent and children exist, is their scope
   explicitly disjoint, or is the parent inactive? Map phases and nodes never
   increase the statistical count.

A split is allowed only when the proposed child has a bounded coercive act or
land transfer, a distinct affected population or tract, enough local evidence
for an independent profile, and a no-double-count rule. A merge is allowed only
when the components are phases of one causal transition and the merged profile
does not conceal materially different actors, mechanisms, populations, or
outcomes.

## Symmetry across rich and sparse archives

The same evidentiary rule must operate in both directions:

- A rich archive may reveal genuine children, but named places, dates, or
  source passages do not automatically become rows.
- A sparse archive may justify a broader uncertainty-bounded unit, but lack of
  detail does not license the project to merge demonstrably different
  processes, infer continuity, or treat silence as absence.
- If the evidence cannot support a stable unit, the candidate is held or its
  dimensions are coded unknown. It is not made artificially broad to preserve
  a count and not split artificially to increase coverage.
- The test is unchanged by the identity of the actor or affected population,
  the event's familiarity or moral salience, and whether admission makes the
  project's thesis or statistical picture look cleaner.
- Event admission and boundary review must be completed without using the
  event's effect on factor counts, clusters, family totals, or narrative
  balance as a reason for the decision.

The Neo-Assyrian archive-density experiment shows why this safeguard matters:
separately defensible rows can still give one surviving archive disproportionate
statistical influence. Event validity and statistical leverage are related but
different questions, and both must be reported.

## Required release-wide audit

Before the next statistical promotion, produce a machine-readable audit row for
every active event and every inactive parent that has active children. The
template is `event_unit_fairness_audit_template.csv`. The completed register
must record the eight tests above, evidence locators, historical-tempo and
date-resolution notes, parent/child relations, source-resolution stratum, and
the final split/merge/retain/hold decision.

The deterministic intake is now
`event_unit_fairness_v1/event_unit_fairness_intake.csv`. It expands the original
single-parent template with aligned multi-parent fields because sixteen active
events already have more than one recorded parent. Its 592-row denominator
contains all 591 release-corpus rows plus the retired Salinas district wrapper,
which remains a recorded parent of active successors despite being outside the
release corpus. All 592 substantive decisions remain explicitly pending.

The release gate requires:

1. **Complete coverage:** every active row has a boundary disposition; no
   unexplained blanks or uncatalogued wrappers.
2. **Zero unresolved double-counting:** every parent/child and sibling overlap
   has an explicit supersession, disjoint-residual, same-event, or hold ruling.
3. **Independent calibration:** all known boundary cases plus a stratified
   sample across era, region, mechanism, event duration, geographic and
   population scale, and source resolution are reviewed without access to the
   candidate model's desired outcome.
   Exact agreement and chance-corrected agreement are reported; every
   disagreement is preserved and adjudicated rather than averaged.
4. **Matched-case review:** reviewers compare unlike archives describing
   structurally similar processes, including archive-dense ancient programs,
   sparse prehistoric transitions, long frontier expansions, short modern
   orders, temporary removals, and reversal/return cases.
5. **Alternative-resolution sensitivity:** rerun the analysis with, at
   minimum, equal-event rows, grouped parent/program series, parent-only and
   successor-only variants, era-balanced weights, region/mechanism-balanced
   summaries, and documentation/missingness strata.
6. **Influence diagnostics:** report whether duration, date precision,
   geographic or population scale, source density, number of children per
   parent, era, region, or mechanism predicts unusual leverage on factor count,
   loading congruence, factor scores, family shares, or exploratory clusters.
7. **Claim narrowing:** if a principal conclusion changes under a historically
   plausible resolution, the monograph must present it as resolution-sensitive
   rather than select the preferred roster silently.

Population size, death toll, moral severity, source count, and atlas screen
time do not change an event's ordinary row weight. Because one-row-per-event
is itself a resolution choice, grouped and balanced results must accompany the
equal-event baseline.

## Existing evidence and remaining work

The project already contains strong pieces of this audit: the written
event-unit rule; parent/child supersession ledgers; overlap crosswalks; retired
wrapper rows; sixty-dimension era-coverage rules; explicit unknown and
structural-not-applicable codes; grouped Roman and Hellenistic sensitivity
tests; era reweighting; and the Neo-Assyrian archive-density experiment.
Examples include the retired Roman-colonies wrapper, the Neo-Assyrian ruler
series, the retired Southern Athabaskan umbrella and bounded Southwest
successors, and the district-wide Salinas split.

The mechanical consolidation is now complete: 592 review units and 98 known
relationships are hash-bound and reproducible. A deterministic calibration
intake adds every 83 known boundary row and 64 stratified active controls, for
147 review rows and 24 proposed matched comparisons. Its controls cover all
eight eras, six families, six duration bins, three documentation-resolution
proxy strata, 56 region labels, and both atlas and non-atlas status. The
inactive regional Jewish-departures research-index gap is now bounded as an
eleven-row relationship review queue rather than silently filled; chronology
and country-scope differences remain for independent disposition. Three
deliberately external relationship targets also remain visible: a semantic
fixture, the held Abó candidate, and the separately active 1953 Inughuit case
named from a contextual relation. What remains is to run two independent
calibration reviews, adjudicate disagreements once, apply the calibrated rule
to the final candidate roster, complete every final-roster disposition,
perform one independent verification of exceptional decisions plus a
stratified retain sample, run the full alternative-resolution and influence
suite, and carry the results into monograph v2. Until then, the event-by-event
fairness claim is **in progress**, not complete.

## Monograph placement

Monograph v2 must contain:

- a plain-language subsection immediately after the event-unit rule;
- the completed audit coverage and reviewer-agreement results in Methods;
- alternative-resolution and influence results beside the other sensitivity
  analyses;
- a limitation stating that fairness means auditable consistency and tested
  robustness, not objective historical atomization; and
- an appendix table or deposited dataset containing every boundary
  disposition and overlap ruling.
