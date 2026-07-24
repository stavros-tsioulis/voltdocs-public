# VoltDocs Public Library

A component library repository for VoltDocs, structured according to the
[VoltDocs repository spec](./SPEC.md) (`schemaVersion: 1`).

## Layout

```
voltdocs.config.yaml     # repository manifest
entries/                 # component entries, one folder per entry
  <category>/.../<slug>/
    entry.yaml            # entry manifest (required)
    index.md               # documentation body
    assets/                 # optional in-repo binaries
    versions/<versionId>/  # optional historical versions
```

See [`SPEC.md`](./SPEC.md) for the full contract, including asset handling, versioning, and
cross-referencing rules.
