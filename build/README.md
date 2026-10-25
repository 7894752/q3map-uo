# Building UO q3map

The standalone driver uses Python 3.8 or newer and its standard library. It compiles the 75-unit manifest with one compiler process,
creates `jpeg6.lib`, `cmdlib.lib` and `nvtristrip.lib`, then links normally. It never runs the output.
This snapshot reproduces the complete reference image; see [known differences](../docs/KNOWN_DIFFERENCES.md).

## Components

| Component | Pinned reference configuration |
| --- | --- |
| Compiler | Visual C++ 7.1, `cl.exe` 13.10.3077, retail Visual Studio .NET 2003 |
| Linker / librarian | 7.10.3077 from the same installation |
| CRT / STL | VC7.1 `/MT`, `libcmt.lib`, `libcpmt.lib`, `oldnames.lib` |
| SDK headers | February 2003 Platform SDK; all 958 header files are pinned |
| Most import libraries | February 2003 Platform SDK: GLU32, WSOCK32, OPENGL32, GDI32, ADVAPI32 |
| USER32 | July 2002 Platform SDK |
| KERNEL32 | VC7.1 `lib/kernel32.lib`, before the SDK library path |
| GlAux | Unmodified August 2002 SDK archive, compiler build 2179, SHA-256 `b6b1812fa5ae416107e8523ebc437f6fb2339989b689630fd4ce59613b598004` |

The SDK root has `include/` and `lib/`. Supply that component separately under its own license.
Microsoft binaries, headers and libraries are not distributed here. `toolchain_manifest.json` records file hashes and retrieval metadata.
The compiler searches the separate February 2003 header component before the compiler and SDK include directories.
Missing staged headers fail before compilation; `--strict` checks every one of the 958 header hashes as well as the selected compiler, CRT, SDK and GlAux files.

**February 2003 GlAux is not the pinned GlAux.** Its compiler provenance differs (build 2190 rather than 2179), changing the Rich header.
The older July 2002 GlAux also differs in SafeSEH feature information. Use the exact August 2002 archive, not a renamed replacement.
The explicit `/SAFESEH` link flag keeps incompatible archives from silently suppressing the load-configuration records.

## Installed toolchain

```bat
python -I build\fetch_toolchain.py --sdk-headers-only
python -I build\build.py --vc7 "C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7" --sdk "C:\SDK\uo" --glaux "C:\SDK\glaux_aug2002.lib" --jobs 1 --strict --identical
```

All manifest paths are relative to the source tree. The command can run from a different working directory.
`build.bat` forwards its arguments and exit status to the Python driver.

## Fetching the compiler, SDK headers and GlAux

```bat
python -I build\fetch_toolchain.py
python -I build\build.py --sdk "C:\SDK\uo" --jobs 1 --strict --identical
```

7-Zip is required for extraction (`--7z` or `SEVENZIP` can select it). The manifest identifies VS .NET 2003 Professional Disc 1, the matching Enterprise Architect Disc 2 support files,
and the Microsoft SDK cabinets. Downloads and extracted files are checked by SHA-256; installers are never executed.
The fetcher installs only its allow-listed compiler/CRT files, February 2003 SDK headers and August 2002 GlAux into the ignored `build/toolchain/` directory.
It does not fetch the separate mixed-version SDK import libraries. `--fetch-toolchain` on the build driver performs the first command automatically.

The `sdk_headers` manifest entry contains all 958 file hashes. Its `sdk_headers_*` sources identify the genuine
[Microsoft February 2003 SDK cabinets](https://download.microsoft.com/download/platformsdk/sdk/update/win98mexp/en-us/3790.0/CoreSDK-common.2.0.cab),
with complete archive hashes and member names. `--sdk-headers-only` fetches just those headers.
An existing extracted Microsoft SDK Include directory can be staged without downloading or running an installer:

```bat
python -I build\fetch_toolchain.py --sdk-include-source "C:\SDK\February2003\Include" --sdk-headers-only
```

The entire supplied header component is verified before any copy. The default header destination is
`build/toolchain/psdk_feb2003/include/`; `--sdk-include DIR` selects another existing header directory for the build.
The header choice leaves `--sdk` import libraries and the pinned August 2002 GlAux unchanged.

`fetch_toolchain.py --verify-only` verifies an already fetched tree without networking.
`--dest DIR` selects another toolchain destination; pass its `vc7/`, `psdk_feb2003/include/` and `link_inputs/glaux_aug2002.lib` to the build explicitly.
`--archives-dir DIR` reuses hash-verified, correctly named local archives. `--keep` retains archives; default temporary work is removed.
The August 2002 GlAux cabinet is cached as `glaux_aug2002_CoreSDK-common.2.0.cab` to distinguish it from the
February 2003 header cabinet named `CoreSDK-common.2.0.cab`. The manifest retains each original Microsoft URL and archive hash.
The compiler/GlAux archives were checked using local cached archives. The February 2003 header cabinets were downloaded directly from Microsoft,
and their extracted file hashes matched all 958 pinned installed headers. No Microsoft software is included in this source export.

## Options and outputs

| Option | Meaning |
| --- | --- |
| `--vc7 DIR`, `--sdk DIR`, `--glaux FILE` | Explicit compiler, SDK and pinned GlAux inputs |
| `--sdk-include DIR` | Explicit February 2003 SDK header directory; all header hashes are checked by `--strict` |
| `--fetch-toolchain`, `--sdk-include-source DIR` | Fetch required components, optionally staging headers from an existing Microsoft SDK Include directory |
| `--strict` | Reject missing or differing selected file hashes |
| `--identical` | Keep ordinary `q3map.exe` and write a separate metadata-stamped `q3map_identical.exe` |
| `--original FILE` | Read a locally supplied reference and write full byte/section diagnostics to `diff_report.json` |
| `--require-identical` | Return exit code 3 unless the produced image equals the recorded reference SHA-256 |
| `--out DIR` | Output directory; default `build/out/` |
| `--jobs 1` | One compiler process |
| `--link-only` | Reuse existing objects; use a fresh full build after source or flag changes |
| `--keep-going` | Continue after compilation failures |
| `--dry-run` | Print commands without executing tools |
| `--clean` | Remove an output directory below `build/` first; other locations are refused |
| `--wine [COMMAND]` | Experimental, unverified Wine execution of compiler tools |

Outputs include `obj/`, `lib/`, `q3map.exe`, `q3map_identical.exe`, `q3map.map`, `q3map.pdb` and `link.log`.
Compiler diagnostics are saved under `work/<object>/compile.log`. No original executable is needed for compilation or linking.

## Metadata and comparison

`meta_stamp.json` records timestamp **1096060060**, RSDS GUID bytes `84a111d9e5cbee4fb984c3f21640a364`, and PDB age **6**.
The stamp changes only the COFF/debug timestamp and RSDS GUID/age in a copy. It never patches code, data or Rich records.
The linker produces the reference PDB path `c:\Cod\bin\q3map.pdb`; this is a historical image constant, not a developer workspace location.

The expected reference SHA-256 is `edf423e0b7607c226bfe26bb591662a098a703a65459b91a53530923933e2fad` (561,152 bytes).
The driver prints both actual and expected hashes. Without `--require-identical`, its zero exit code means build success.
For a release gate, use `--identical --strict --require-identical`, optionally adding `--original` for a complete JSON report.
`--strict` rejects a supplied reference with the wrong hash. Output/clean operations that could overwrite that reference are refused.

Compare a locally supplied reference without building or running either image:

```bat
python -I build\compare_image.py --candidate build\out\q3map_identical.exe --original "C:\Tools\q3map.exe" --report build\out\diff_report.json
```

The comparator returns 0 for complete equality, 1 for differences and 2 for invalid input. It reports every differing file range and per-section counts,
including appended bytes; zero-filled virtual storage is not allocated. `stamp_meta.py check` remains available for metadata diagnostics.
Use the final hash or comparison result to verify identity after any local change.
`tools/audit_sources.py` provides a read-only source/include audit. Source portability findings do not replace the target-compiler build check.
