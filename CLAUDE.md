# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **data repository, not an application** — a component library conforming to the
VoltDocs repository spec (`SPEC.md`, `schemaVersion: 1`). It is consumed by external VoltDocs
documentation software; there is no build, lint, or test tooling here. All work in this repo is
authoring/editing YAML manifests and Markdown bodies under `entries/`.

`SPEC.md` is the authoritative contract — read it before restructuring anything. The notes below
are the parts of it that are easy to get wrong, not a substitute for it.

## Repository layout

```
voltdocs.config.yaml     # repo manifest: schemaVersion, name, entriesDir
entries/                 # everything below is discovered from here
  <category>/.../<slug>/ # one ENTRY per folder (folder name is a human slug, not the id)
    entry.yaml            # required marker file — a folder is an entry iff this exists
    index.md               # body referenced by entry.yaml's `body:` field
    assets/                 # optional in-repo binaries (datasheets, images…)
    revisions/<revisionId>/ # optional historical revisions, each a full mini-entry
  _folder.yaml            # optional, per-folder inheritable defaults (category, tags)
```

Worked example: `entries/wireless/rfid-nfc/mfrc522/` — a current entry (`revision: "2.0"`) plus a
historical `revisions/1.0/`, using only `external` assets (no `assets/` folder needed since nothing
is vendored in-repo).

## Non-obvious rules from SPEC.md

- **Identity is `id`, never the path.** Folders can be renamed/reorganized freely; every
  cross-reference (`references[].targetId`) must use the manifest's `id`, not a path.
- **Entries are leaves.** Discovery is marker-based (walks for `entry.yaml`) and stops descending
  once it finds one — never nest one entry's folder inside another's.
- **`revisions/` and `assets/` are reserved** subfolder names inside an entry; they are never
  themselves treated as entries even if they contain YAML.
- **Folder defaults (`_folder.yaml`) inherit down the tree**: `category` is overridden by the
  closest one; `tags` are merged (union) at every level. An entry can still override its own
  category/tags.
- **Revisions vs. variants — do not conflate.** `revisions/<id>/` is the *time* axis for one part
  (silicon rev, errata) under the same `id`. A part that coexists in multiple packages/tolerances
  *at the same time* is a **separate entry** (distinct `id`), linked via
  `references: [{ relation: variant-of }]` instead.
- **Deprecation chains use two mechanisms together**: `status: deprecated | archived` on the old
  entry/revision, plus a `references` link with `relation: replaced-by` pointing at the successor
  **entry** (different `id`). Do not use `replaced-by` to point from an old revision to a newer
  revision of the *same* entry — that's already expressed by `revisions/`.
- **Assets are one discriminated type** (`Asset` with `location.type`: `repo` | `external` |
  `inline`) regardless of whether it's a datasheet, an image, or a "buy it here" link — a
  `reference`-kind asset is just a link, not a special case. `repo` paths resolve relative to the
  entry folder unless prefixed with `/` (repo-root-relative), and can never escape the repo root.
  Prefer `external` for large binaries (STEP files, gerbers, high-res renders).
- **`fields` is an open, category-specific map** — no fixed schema in v1. Keep it flat scalars/
  arrays (see the mfrc522 example) rather than inventing nested structures, so generic
  search/filtering keeps working across unrelated categories.
- **Duplicate `id`s across the whole repo are invalid**, not just within a folder — check for
  collisions when adding an entry.

## Conformance checklist (SPEC.md §7)

Before considering an entry "done": valid `voltdocs.config.yaml` at root; every entry has a
non-empty unique `id`, `title`, `revision`; entries are leaves; every `assets[].location` is one of
`inline`/`repo`/`external` and `repo` paths stay in-repo; every `references[].targetId` resolves to
a real entry `id`; historical revisions live under `revisions/<id>/` with their own full `entry.yaml`.
