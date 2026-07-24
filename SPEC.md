# VoltDocs Repository Specification

Version: **1** (`schemaVersion: 1`)

This document specifies how to structure a repository of components so it can be
consumed by the VoltDocs documentation software. Any repository that conforms to
this specification can be dropped in behind the
[`FsGitRepositoryAdapter`](./src/adapters/fs-git/index.ts) — or any adapter that
implements the [`RepositoryAdapter`](./src/types/adapter.ts) contract — with no
changes to the application.

The goal is **bring-your-own-repository**: an organisation can keep its patented
components and specifications in a private git repository and still use VoltDocs,
provided the repository follows the contract below.

---

## 1. The adapter contract (the seam)

VoltDocs never talks to a store directly. It talks to a `RepositoryAdapter`:

```ts
interface RepositoryAdapter {
  setup(): Promise<RepositoryInfo>;
  search(query: Query): Promise<SearchResult>;
  getEntry(id: EntryId, options?: GetEntryOptions): Promise<Entry | null>;
  listVersions(id: EntryId): Promise<readonly VersionInfo[]>;
  resolveAsset?(entryId, assetId, version?): Promise<AssetContent>;
  teardown?(): Promise<void>;
}
```

The three mandatory operations map onto the three tasks in the brief:

| Task | Operation |
|---|---|
| **Setup** | `setup()` — connect, validate, build the search index, report capabilities |
| **Search / filter** | `search(query)` — one `Query` model understood by every backend |
| **Get an entry by id** | `getEntry(id, { version? })` |

`search` returns lightweight `EntrySummary` projections; callers hydrate full
`Entry` objects (fields, body, assets) with `getEntry`. This keeps listing cheap
regardless of how large individual entries are.

Backends declare what they can do via `RepositoryInfo.capabilities`
(`versioning`, `fullTextSearch`, `assetResolution`, `writable`) so the
application can degrade gracefully rather than assume every store is equally
capable. Adapters that cannot evaluate a predicate natively fall back to the
shared [`runQuery`](./src/query-engine.ts) engine, so `text`, `tags` and
`fields` filtering behave **identically** across a git tree, a database or a
REST API.

---

## 2. Git repository layout

```
<repo-root>/
├── voltdocs.config.yaml            # repository manifest (required)
└── entries/                        # entriesDir from the config
    ├── passives/
    │   └── resistors/
    │       ├── _folder.yaml         # optional folder-level defaults
    │       └── rc0402-10k/          # ← an ENTRY (folder name is a slug, not the id)
    │           ├── entry.yaml       # entry manifest (required — the marker file)
    │           ├── index.md         # documentation body
    │           ├── assets/          # in-repo binaries (datasheets, images…)
    │           │   └── datasheet.pdf
    │           └── versions/        # optional historical versions
    │               └── 1.0.0/
    │                   ├── entry.yaml
    │                   └── index.md
    └── connectors/
        └── usb-c-16pin/
            ├── entry.yaml
            └── index.md
```

Folders are **organisational only**. They group entries for humans and provide
inheritable defaults; they carry no identity. See
[`examples/sample-repo`](./examples/sample-repo) for a complete, working tree.

### 2.1 Repository manifest — `voltdocs.config.yaml`

```yaml
schemaVersion: 1
name: Example Component Library
entriesDir: entries
```

### 2.2 Entry manifest — `entry.yaml`

The manifest is close to the [domain model](./src/types/model.ts) but is
validated defensively — a repository is user-authored and never trusted to be
well-formed.

```yaml
id: passive.resistor.rc0402-10k   # stable, repo-unique, decoupled from the path
version: "1.1.0"                   # the version THIS manifest represents
title: RC0402 10kΩ ±1% Thin-Film Resistor
category: passives/resistors       # optional; usually inherited from _folder.yaml
tags: ["0402", thin-film]          # merged with inherited tags
status: published                  # draft | published | deprecated | archived
summary: General-purpose 10 kΩ thin-film chip resistor.
updatedAt: "2024-03-12"
fields:                            # structured, category-specific parameters
  resistance_ohm: 10000
  tolerance_pct: 1
  package: "0402"
  power_w: 0.063
highlights: [resistance_ohm, power_w]  # headline `fields` keys; see §2.3
body: index.md                     # relative path to the body document
assets: [ … ]                      # see §4
references: [ … ]                  # typed links to other entries
guides: [ … ]                      # long-form articles; see §2.4
versions:                          # metadata for versions under versions/
  - id: "1.0.0"
    releasedAt: "2023-01-01"
    status: deprecated
```

**Identity rule:** `id` is authoritative. The folder name is a human-readable
slug and may be renamed freely; links must use `id`, never the path. This is
what lets a repository be reorganised without breaking references.

### 2.3 Headline parameters — `highlights`

`fields` is an open, unordered map, so nothing in it says which parameters a
reader wants first. `highlights` is an ordered list of `fields` keys the
repository considers headline figures.

It is a **presentation hint only**: a renderer MAY surface these ahead of the
full specification table and MUST ignore keys that do not resolve, so pruning a
field can never break a manifest. Ordering is significant.

### 2.4 Guides — long-form articles

Where `body` is the reference documentation for a component, a guide is a
project-oriented walkthrough ("wire this to an ESP32 and read a tag"). Guides
are their own collection rather than an asset kind because they are editorial
content with their own prose, tags and reading metadata, and are rendered as
pages rather than downloaded.

```yaml
guides:
  - id: esp32-spi              # unique within the entry; used as the URL slug
    title: Reading a card UID with an ESP32
    summary: Wire the reader over SPI and read a tag from ESP-IDF.
    minutes: 25                # estimated reading time
    level: intermediate        # beginner | intermediate | advanced
    tags: [esp-idf, spi, c]
    body: guides/esp32-spi.md  # required; resolved like any repo path (§4)
```

`id` must be unique within the entry and `title` and `body` are required; the
rest are optional. A guide whose body file is missing keeps its metadata and
renders without content, matching how a missing entry `body` is handled.

---

## 3. Making every entry discoverable — regardless of depth

**Discovery is marker-based.** A directory *is* an entry if and only if it
contains an `entry.yaml`. The adapter walks the entire tree under `entriesDir`
and collects every marker file, so an entry twelve folders deep is indexed
exactly like a top-level one and participates in search and filtering on equal
footing.

Rules that keep this unambiguous:

- **Entries are leaves.** Once discovery finds an `entry.yaml` in a folder, it
  does not descend further looking for nested entries. Nesting is expressed
  through the *path*, not through nested entry folders.
- **Reserved subfolders** (`versions/`, `assets/`) inside an entry are never
  treated as entries.
- **Dot-folders** (`.git`, `.github`, …) are skipped.
- At `setup()`, all discovered entries are loaded into one flat index keyed by
  `id`. Search operates over that flat index, so folder depth has zero effect on
  whether an entry is found — it only affects the `category` used for grouping.

### 3.1 Folder defaults — `_folder.yaml`

To keep deeply-nested entries consistent **without repeating metadata in every
manifest**, any folder may carry an optional `_folder.yaml`:

```yaml
category: passives/resistors
tags: [passive, resistor]
```

Defaults accumulate down the path: `category` is overridable by a closer folder
or by the entry itself; `tags` are **merged** (union) all the way down. An entry
can always override its inherited category and add its own tags. This gives one
DRY place to declare shared structure per branch of the tree.

---

## 4. One structure for media, downloads and reference links

A component's supporting artefacts — a datasheet PDF, a schematic symbol, a "buy
it here" link, a 3D model — may live **inside** the repository, on an external
CDN/object store, or be embedded inline. Rather than a distinct rule per folder
or per kind, **every** artefact is one `Asset` with a discriminated `location`:

```ts
type AssetLocation =
  | { type: 'inline';   data: string; encoding: 'utf8' | 'base64' }
  | { type: 'repo';     path: string }      // tracked inside the repository
  | { type: 'external'; url: string };      // CDN, object store, vendor site
```

```yaml
assets:
  - id: datasheet
    kind: datasheet
    location: { type: repo, path: assets/datasheet.pdf }
  - id: buy-digikey
    kind: reference                          # a link is just an asset
    location: { type: external, url: https://www.digikey.com/… }
  - id: symbol
    kind: image
    location: { type: inline, encoding: utf8, data: "<svg…/>" }
```

Because the shape is uniform, media, downloads and links all flow through the
same indexing, rendering and `resolveAsset()` path — no folder needs a bespoke
case. `resolveAsset()` returns bytes for `inline`/`repo` locations and hands back
the URL for `external` ones (the caller decides whether to fetch or redirect).

**In-repo path resolution:** a `repo` path is relative to the entry folder by
default; a leading `/` makes it repo-root-relative (for shared assets). Paths
that escape the repository root are rejected.

**Large binaries** (STEP models, gerbers, high-res renders) should prefer
`external` object storage or **Git LFS**; keeping multi-megabyte binaries in git
history bloats every clone. The `bytes` and `checksum` fields let the UI show
sizes and verify integrity without downloading.

---

## 5. Versioning

Two independent axes of history exist; the spec keeps them distinct:

1. **Component version / revision** (user-facing, semantic): silicon rev, spec
   change, errata. Modelled explicitly with `version` + `versions/<id>/`.
2. **Editorial history** (who fixed a typo when): this is *git's* job — commit
   history — and is deliberately **not** modelled in the manifest.

### 5.1 Component versions on disk

- The entry folder's `entry.yaml` is the **current / default** version. Its
  `version:` field names that version id.
- Historical versions live under `versions/<versionId>/`, each with its own full
  `entry.yaml` (and body/assets). `getEntry(id, { version })` loads from there.
- `listVersions(id)` unions three sources: the current version, the manifest's
  declared `versions:` list, and any `versions/*` directories present on disk.
- Version ids are opaque strings (`"1.1.0"`, `"rev-C"`, `"2024-05"`); ordering
  uses `releasedAt` when present, otherwise the id.

### 5.2 Non-trivial cases the spec must (and does) account for

| Case | Handling |
|---|---|
| **Variants vs versions** — a part sold in several packages / tolerance grades that coexist *at the same time* | These are **separate entries** (distinct ids), optionally linked with `references` (`relation: variant-of`). Versions are a *time* axis; variants are a *selection* axis — conflating them breaks search. |
| **Deprecation & supersession** | `status: deprecated \| archived` plus `VersionInfo.supersedes` forms a revision chain; a `references` link with `relation: replaced-by` points to the successor entry. |
| **Cross-references between components** | `references: [{ targetId, relation, version? }]` — typed, id-based, optionally version-pinned (e.g. `recommended-footprint`, `see-also`). |
| **Path renames / reorganisation** | Identity is `id`, never the path, so moving a folder never breaks links or search. |
| **Duplicate ids** | Detected at `setup()` and rejected with a clear error — ids must be unique across the whole repo. |
| **Draft / unpublished work** | `status: draft`; callers filter with `Query.status`. |
| **Deleted entries** | Removing the folder removes the entry at the next `setup()`. Where downstream indexes must learn of deletions, keep a tombstone entry with `status: archived` rather than deleting outright. |
| **Localisation (i18n)** | Out of scope for v1; the reserved approach is per-locale body files (`index.<locale>.md`) resolved by the adapter. Flagged here so it is not designed *out*. |
| **Schema evolution** | `schemaVersion` in the config lets adapters migrate or refuse an unknown version rather than mis-parse it. |
| **Private / access-controlled repos** | Handled *below* the adapter: the git checkout is produced with the caller's credentials. Per-entry visibility can be layered via `fields`/`status` and a filtering wrapper adapter. |

---

## 6. Other considerations captured by the spec

- **Structured data in a free-form store.** Freedom of folder layout is
  preserved, but every entry must still provide a validated `entry.yaml`. The
  open `fields` map carries category-specific parameters through one channel, so
  search and filtering work generically without the software knowing about
  "resistors" vs "connectors".
- **Field schemas (optional, forward-looking).** A repository may ship JSON
  Schemas per category (e.g. `schemas/resistor.schema.json`) to validate
  `fields`. v1 treats `fields` as an open map; schema validation is an additive,
  non-breaking future step.
- **Capabilities over assumptions.** `RepositoryInfo.capabilities` lets a
  read-only or search-less backend advertise its limits instead of failing at
  call time.
- **Consistent query semantics.** Because every adapter can defer to
  `runQuery`, a query written against a git repo behaves the same against an API
  adapter — essential when organisations mix private and shared sources.
- **Revision pinning.** `RepositoryInfo.revision` records the connected snapshot
  (e.g. a git commit sha), so a rendered site is reproducible.

---

## 7. Conformance checklist

A repository conforms to `schemaVersion: 1` when:

1. A valid `voltdocs.config.yaml` exists at the root.
2. Every entry folder contains an `entry.yaml` with a non-empty, unique `id`,
   `title`, and `version`.
3. Entry folders are leaves (no entry nested inside another entry).
4. All `assets[].location` values are one of `inline` | `repo` | `external`,
   and every `repo` path stays within the repository root.
5. `references[].targetId` values refer to ids that exist in the repository.
6. Historical versions, if any, live under `versions/<id>/` with their own
   `entry.yaml`.
