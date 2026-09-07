# Third-party notices and exclusions

This notice accompanies the component grants in [LICENSE.md](LICENSE.md).
The project's licenses cover only original material and rights the licensor
can grant. They do not supersede the terms below.

## D3-derived map code: ISC

The atlas's `neRaw` projection and smooth zoom interpolation are adaptations
of D3 source. The original copying version was not recorded. The relevant
formulas/source and permissions were checked on 2026-09-05 against the tagged
[d3-geo v3.1.1 projection](https://github.com/d3/d3-geo/blob/v3.1.1/src/projection/naturalEarth1.js)
and [d3-interpolate v3.0.1 zoom](https://github.com/d3/d3-interpolate/blob/v3.0.1/src/zoom.js).
These are verification references, not a claim to have recovered the original
download versions or to bundle all of D3.

Preserve [the complete d3-geo license file](LICENSES/d3-geo-LICENSE.txt) and
[the complete d3-interpolate license file](LICENSES/d3-interpolate-LICENSE.txt).
They include the ISC notices for Mike Bostock, respectively 2010-2024 and
2010-2021. The full d3-geo upstream file also contains a separate GeographicLib
notice; retaining it does not claim that this atlas incorporates GeographicLib.
The applicable ISC copyright, permission, and disclaimer text is also embedded
in the standalone atlas source so a copied HTML file retains it.

## Geography

**© OpenStreetMap contributors.** Simplified coastline geometry identified by
OpenStreetMap source comments in `taking-the-land-atlas.html` is derived from
[OpenStreetMap](https://www.openstreetmap.org/copyright) and is available under
the [Open Data Commons Open Database License 1.0](https://opendatacommons.org/licenses/odbl/1-0/).
Its embedded coordinate arrays remain machine-readable in the atlas source.
Preserve attribution and comply with applicable ODbL database and produced-work
obligations. The project's CC BY research-data grant does not relicense this
geography; it is not a claim that all original prose or software is ODbL.

**Natural Earth.** Modern coastlines, river/lake geography, and related base-map
material identified as Natural Earth use its
[public-domain raster/vector data](https://www.naturalearthdata.com/about/terms-of-use/).
The name of the Natural Earth projection does not change D3's code license.

The inspected atlas and publication stylesheet use local/system font stacks;
they do not bundle those font files. A reference to a locally installed font
does not grant permission to redistribute that font.

## Research sources, quotations, and external materials

Historical works, quotations, translations made by other authors, images,
source captures, and externally supplied documents/tools retain their own
copyright and licenses. Source URLs and passage locators identify that material;
our metadata and factual assertions are not a license to the underlying works.
This applies equally to third-party excerpts inside CSV/JSON evidence ledgers
and quotations inside Markdown or HTML. Existing public-domain status and
lawful exceptions remain unaffected.

The public builder excludes source PDFs, browser captures, raw model/coder
journals, private material, and scratch files. Do not expand those exclusions
into a general permission to upload them merely because the project is open.
If additional third-party material is incorporated, identify its license and
required notices before including it in a future distribution.
