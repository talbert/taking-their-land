# Taking their land

A chronological atlas of documented land-taking and forced removal, with a
working monograph and versioned research data. By Craig Talbert.

This repository is initially private while preparation continues. It contains
a clean snapshot of the material already distributed on the project website,
not the private research repository or its history. Making this repository
public is a separate owner decision.

## What is here

- `site/index.html`: the self-contained atlas application and embedded content.
- `site/monograph/`: the working paper in HTML, Markdown, and PDF (v2).
- `site/data/`: frozen statistical data, results, selected evidence and decision
  ledgers, bibliography inventories, manifests, and the complete data ZIP.
- `site/reuse/`: component licensing and third-party notices.
- `EXPORT_MANIFEST.json`: the exact snapshot identifiers and per-file checksums.

This export is atlas build **20261006e** (540 cases, 552 playback stops) and
statistical release **second_pass_v7_676** (676 active statistical events).
Those are different products and counts: the atlas keeps adding reviewed cases
between statistical releases, and later atlas corrections do not silently
change the frozen model inputs. The first export (September 2026) was build
20260906a with release second_pass_v6_675. Bibliography metadata is an
explicitly unfinished inventory; the monograph is a working paper, not a final
validated conclusion about complete historical coverage or unbiased event
boundaries. The site also publishes a dated discovery-status report
(`site/discovery/`) describing where the search for missing histories stands
and its limits.

## Run locally

No frontend package installation is needed. From the repository root:

```sh
python3 -m http.server 8731 --directory site
```

Open `http://localhost:8731/`. The server-side feedback handler is deliberately
not included, so local feedback submission is not configured. Do not deploy
this copy as a functioning feedback service without configuring its backend.

Check the downloaded snapshot using:

```sh
python3 verify_snapshot.py
```

The complete internal analysis/build environment is not yet exported here;
this snapshot makes the application, paper, released inputs and results
available without promising that every research pipeline can be rerun from
this repository alone. Future releases can add reviewed runnable analysis
tools. Do not copy the private research Git history into this repository.

## Reuse and attribution

- Original software: **MIT**.
- Original structured research data: **CC BY 4.0**.
- Original prose, monograph, and explanatory graphics: **CC BY-SA 4.0**.

See [LICENSE.md](LICENSE.md) for component boundaries and full terms, and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for D3, map-data and quotation
exceptions. A mixed HTML or JSON file does not have just one license.
Copyrighted research PDFs, private source captures, raw model journals,
credentials, and scratch files are excluded. The monograph PDF is the
project's own licensed document, not a copied research source.

Suggested citation: Craig Talbert. 2026. *Taking their land: A chronological
atlas of settlement and displacement*. Identify the atlas build or statistical
release used, and the access date. No archival DOI has been issued for this
snapshot yet.

[Project website](https://latrian.dyndns.org/takingtheirland/)

## Updating

Each export must come from a verified publication bundle and retain its
snapshot identifiers. Do not overwrite a frozen statistical release with
unpromoted corrections. Review the full export, history and licenses before
changing visibility. GitHub Pages and automatic Zenodo publication are not
enabled as part of this private preparation.
