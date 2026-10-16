# Bibliography inventory — 8 September 2026

This dated inventory repairs the declared input coverage while preserving the
August bibliography and its work IDs. It is a tiered working dataset, not a
claim that every access record is a unique work or a publication-ready citation.

## What is covered

The input manifest names and hashes 71 files: the preserved August URL
inventory; v7's model-input and publication source arrays; every source join
for the 370 published atlas cases; the atlas and audit source registries;
reviewed negative findings; historical gap-scan dispositions; the current
authoring partition and identifier correction ledger; and 61 named authoring source-note files.

The output preserves all 851 reviewed August work groups and all fourteen
duplicate/relationship decisions. It records 5,875 source occurrences and
1,374 distinct access URLs, grouped into 1,366 conservative work or access
records. **These are not 1,366 verified unique works.** Of the records, 515 are
new to this inventory. New title-only similarities do not cause automatic
merges. DOI equality and a preserved access URL can establish an existing ID;
book/chapter distinctions and URL passage fragments remain explicit.

The URL rule lowercases the host and treats HTTP/HTTPS as access variants,
while preserving path case, query parameters and fragments. August decisions
remain exactly as reviewed, even when their earlier normalization was broader.

Sources for active events, family holds, authoring holds, inactive rows,
negative findings and published cases are separate occurrence scopes. A work
can legitimately appear in more than one scope. Counts across those scopes
must not be added as counts of unique works or events. Unused source-registry
entries and source-note links do not become manuscript citations by inference.

## Metadata and citations

- `anchor_reference_usage.json`, `cited_references.md` and
  `background_reading.md`: the preserved 41-entry manuscript list separates
  into 27 cited works and 14 background entries after an author/year and
  citation-context review. The prior thirteen-background claim is superseded.
- `typed_metadata.json`: retains the 30-row reviewed pilot, adds DOI-deposited
  metadata with field provenance, and explicitly leaves remaining records
  unresolved. The pilot's substantive edition and issue-year judgments take
  precedence over newly retrieved deposits.
- `IDENTIFIER_CORRECTIONS.json`: two incorrect article links are corrected
  against the publishers, and one De Gruyter viewer suffix is removed from a
  parsed DOI. Original IDs and release inputs remain intact. Public atlas link
  corrections are pending the next publication checkpoint.
- `source_occurrences.json`: exact source title, URL, input locator, event or
  case identity, and disposition scope. Source-note locators identify the
  project note, not a claim of having newly opened the underlying passage.
- `unresolved_access_records.json`: 388 occurrences with 73 distinct recorded
  titles but no HTTP access URL. Many are project review/ledger pointers or
  local PDF references; they are retained without presenting those pointers
  as independent scholarly works. Their underlying edition/locus resolution
  remains a bounded research task.

Crossref supplies publisher-deposited metadata, not a historical validity
guarantee. Authors, issue years, editions and publisher names can still need
review. Raw abstracts, references, article bodies and captured source PDFs are
excluded from the metadata cache. Retrieval method:
[Crossref REST API documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).

`METADATA_STATUS.json` states the current tier counts and unresolved boundary.
The old August 854/851 figures remain historical facts; they are not globally
replaced throughout earlier publications.

## Reproduction

Run the three current bibliography scripts and the reference-usage review
from the project root. `build_current_bibliography.py` harvests only declared
inputs; `collect_bibliography_metadata.py` uses its saved responses unless an
explicit retry is requested; `assemble_bibliography_metadata.py` joins the
tiers. `review_reference_usage.py` reproduces the reviewed v1.6 citation-use
split. The older census builders are preserved for historical reproduction.

This release is bounded to the listed inputs. It does not claim to harvest
every document ever consulted. Source bodies, private browser captures,
deployment/QA URLs and raw coder journals are outside this dataset.
