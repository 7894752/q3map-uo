# Known differences

Reference: UO map-tools `q3map.exe`, dated 2004-09-24, **561,152 bytes**.
SHA-256: `edf423e0b7607c226bfe26bb591662a098a703a65459b91a53530923933e2fad`.

**990/990 project functions are accepted.** The stamped linked image equals the reference byte for byte.

No project function remains open.

The stamped export differs in **0 file bytes**, in 0 contiguous ranges.
Open project-function positions and alignment tails account for 0 text bytes; other text accounts for 0 bytes.
These are raw bytes at reference positions, not instruction-distance scores or semantic-error counts.

| Region | Different file bytes |
| --- | ---: |
| Headers | 0 |
| `.text` | 0 |
| `.rdata` | 0 |
| `.data` | 0 |

## Metadata policy

The normal link has a fresh timestamp and PDB signature. `--identical` writes a separate copy with only the recorded
COFF/debug timestamp, RSDS GUID and PDB age (6). The embedded PDB path is produced by the linker.
The stamp changes no code, data, imports, layout or Rich records. `--require-identical` fails unless the final hash equals the reference.

## Release gates

The complete reference SHA-256, all project-function acceptances and the source/file/notice/credit/leak audits passed for this snapshot.
Repeat a fresh build and audits after changing sources or dependencies.
No executables, toolchains, archives or private verification data belong in the published source tree.
