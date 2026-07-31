# Importing from alldatasheet.com

A guide for turning an [alldatasheet.com](https://www.alldatasheet.com) search into a
conformant entry under `entries/`. alldatasheet is a third-party **aggregator/mirror** —
useful for *discovering* parts and locating a datasheet fast, but it is not the
manufacturer, and its metadata and rehosted PDFs should not be trusted or cited blindly.
This is a workflow document, not a spec — `SPEC.md` and `AUTHORING.md` are still the
contracts; this just explains how to get from an aggregator search to entries that satisfy
them.

---

## 1. Search, then disambiguate the manufacturer

A search like `view.jsp?Searchword=<part>` returns two tiers — "exact match" and
"broader" results — and for any part number that's been second-sourced (NE555, 74HC595,
op-amps, generic MOSFETs…) you'll get **one row per manufacturer**, each with its own PDF,
revision and date. alldatasheet does not consolidate these; it lists Texas Instruments,
STMicroelectronics, Diodes Inc., Renesas, etc. as independent records for what is
functionally the same part.

Before opening a single PDF, decide:

- **Which manufacturer's part are you actually documenting?** If the repo already has a
  part from one vendor and you're adding a pin-compatible second source, that is a
  **separate entry** (distinct `id`) linked with `references: [{ relation: variant-of }]`
  — never the same `id` with fields overwritten. See SPEC.md §4.2, "Variants vs revisions."
- **Is this actually a new revision of a part already in the repo**, not a different
  manufacturer? That's the `revisions/<id>/` axis, not a new entry (SPEC.md §4.1).
- If several manufacturers make an electrically-identical part and you only intend to
  document one, pick the one whose datasheet you can find a first-party source for (next
  section) — don't default to whichever aggregator row loads first.

## 2. Treat alldatasheet as discovery, not as the citation

The aggregator page for a specific document (`datasheet-pdf/pdf/<id>/<mfr>/<part>.html`)
usually shows a manufacturer link (e.g. `nxp.com`, `ti.com`) alongside its own rehosted
"Download Datasheet" button. **Follow that manufacturer link and locate the PDF on the
manufacturer's own site** for the `datasheet` asset URL. Reasons:

- alldatasheet's rehosted copy can be an **outdated revision** — the mfrc522 entry, for
  instance, cites `nxp.com/docs/en/data-sheet/MFRC522.pdf` directly rather than
  alldatasheet's mirrored copy, precisely so the link tracks NXP's current revision.
- The manufacturer is the copyright holder; a third-party mirror is not a stable or
  authoritative long-term link, and its URL layout/hosting can change independently of the
  part.
- alldatasheet's own PDF viewer/preview text is frequently OCR'd and can contain
  transcription errors — never copy a spec value from the aggregator's preview table
  without opening the actual PDF and reading the number in context (units, test
  conditions, min/typ/max column).

**Only fall back to linking alldatasheet's own hosted copy** (`location: { type: external,
url: "https://www.alldatasheet.com/datasheet-pdf/download/…" }`) when no first-party
manufacturer PDF can be found at all, and note in the entry (e.g. a `notes` line in the
body, or just accept the lower confidence) that the source is a third-party mirror. Never
download the PDF and commit it into `assets/` (`location: type: repo`) sourced from
alldatasheet — the datasheet's copyright belongs to the manufacturer, and `external`
already covers this case without vendoring the binary (SPEC.md §3 also generally prefers
`external` for anything beyond small in-repo binaries you actually have rights to ship).

## 3. Read the real PDF before filling in `fields`

Once you have the manufacturer's PDF open:

1. Skim the front page / feature list for the **category-defining numbers** — these
   usually become `highlights` (SPEC.md §1.3): the 3–5 values a reader checks first
   (frequency, voltage range, package, a key throughput/rating figure).
2. Pull the **Absolute Maximum Ratings** and **Electrical/Recommended Operating
   Conditions** tables — these feed both `fields` (flat scalars — see below) and the
   Min/Typ/Max tables in the body per `AUTHORING.md`.
3. Note the **revision/date** and whether the datasheet marks the part **NRND / obsolete /
   replaced by** anything — that maps to `status: deprecated` plus a `references`
   `relation: replaced-by` link to the successor entry (SPEC.md §4.2), and/or a `revisions/`
   entry if it's the same part's earlier silicon rev.
4. Note the **package(s)** offered — if a part ships in several packages that coexist
   today, that's the variants case again, not one entry with a list-valued package field.

### Mapping into `fields`

`fields` is an open, flat map (SPEC.md §1.2, §5) — resist the urge to nest what the
datasheet nests. Concretely:

| Datasheet section | `entry.yaml` location |
|---|---|
| Manufacturer, part number(s) | `fields.manufacturer`, `fields.ic_part_numbers` / equivalent |
| Package | `fields.package` (string) |
| Headline electrical figures (Vcc range, current, frequency…) | flat `fields.*_min_v` / `fields.*_max_v` / `fields.*_mhz` etc. — suffix with unit, not a nested `{min, max, unit}` object |
| Interfaces/protocols supported | `fields.interfaces` (array of scalars) |
| Operating temp range | `fields.operating_temp_min_c` / `_max_c` |
| NRND / obsolete notice | `fields.nrnd: true` and/or `status: deprecated` |
| The 3–5 numbers a reader checks first | `highlights: [...]` referencing the `fields` keys above |

Use the existing `entries/modules/rfid-nfc/mfrc522/entry.yaml` as the concrete template —
it's the only entry in the repo today and follows this shape exactly.

## 4. Write the body from AUTHORING.md, not from the aggregator's summary

The aggregator's own "quick specs" blurb is not a substitute for the layout in
`AUTHORING.md`. Pick the layout matching the part's shape (Module / IC / Transistor /
Diode & LED / Passive / Electromechanical / Default) and fill it from the real datasheet:
pinout table from the pin configuration diagram, register map from the register section
(if any), typical application circuit from the datasheet's own reference schematic, common
mistakes from the datasheet's own caution notes plus known real-world gotchas. Tables near
the top, prose below — same rule as always.

## 5. Assets checklist

- `datasheet` asset :i-lucide-move-right: manufacturer's own PDF URL (external), not alldatasheet's mirror,
  per §2 above.
- `product-page` asset (`kind: reference`) :i-lucide-move-right: the manufacturer's product page, often linked
  right next to the PDF on the aggregator page — useful for buy links / part status.
- Product photo, if used, still needs its own hosting (`kind: image`, first declared image
  asset becomes the primary image per SPEC.md §1.5) — alldatasheet doesn't provide usable
  product photography, only PDF thumbnails.

## 6. Before merging: run the conformance checklist

Same checklist as any other entry (SPEC.md §6 / CLAUDE.md) — nothing about sourcing from
alldatasheet changes it: unique `id` not colliding with anything in the repo, `references`
targets resolve, `repo` asset paths stay in-repo, revisions live under `revisions/<id>/` with
their own full `entry.yaml`. The only import-specific addition is: **the `datasheet` asset
URL should resolve to a manufacturer-hosted PDF**, verified by actually opening it, not by
trusting the aggregator's link text.
