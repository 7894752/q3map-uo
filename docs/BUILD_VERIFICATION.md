# Standalone export verification

Snapshot checked on 2026-10-25. Project status: **990/990 accepted**.
The stamped linked image equals the reference byte for byte. See [known differences](KNOWN_DIFFERENCES.md).

## Build and inputs

The refreshed export compiled all 75 translation units with one compiler process, created the manifest's static libraries,
linked normally and stamped only the documented timestamp/PDB signature fields. No built program was executed.
All 1128 fetched compiler/support/SDK-header/GlAux files were hash-verified, including every one of the 958 February 2003 SDK headers.
The separate SDK import-library fingerprints are pinned in the toolchain manifest.
The export preserves 136 source/header/IJG notice snapshot files and includes two public component integration notes.

## Complete-file result

| Item | Result |
| --- | --- |
| Reference size | 561,152 bytes |
| Stamped export size | 561,152 bytes |
| Reference SHA-256 | `edf423e0b7607c226bfe26bb591662a098a703a65459b91a53530923933e2fad` |
| Stamped export SHA-256 | `edf423e0b7607c226bfe26bb591662a098a703a65459b91a53530923933e2fad` |
| Different file bytes | 0 |
| Differing ranges | 0 |
| Section layouts equal | True |
| Byte-identical | True |

The exported `compare_image.py` writes every differing range and per-section counts without executing images.
`--require-identical` makes mismatch a failing build gate (exit 3); ordinary build success is not identity.
The audit checks exact source hashes, current canonical drift, unlisted source files, binaries/archives, private leaks, credits and local links.
Source-only include warnings are reviewed alongside the actual successful compiler include resolution.

## Limits

Static byte checks do not establish runtime behavior, portability or unique historical source spelling.
Source/object/library order and compiler-sensitive definition visibility remain part of the measured reference configuration.
Re-run the refresh/build/audit command after changing sources, flags or dependencies.
