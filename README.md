# q3map — Call of Duty: United Offensive BSP Map Compiler (Byte-Identical Source)

Compiles with Visual C++ 7.1 to the exact bytes of the original 2004 United Offensive `q3map.exe`.

A source reconstruction of `q3map.exe`, the BSP compiler that shipped with the 2004 Call of Duty: United Offensive map
tools (a Quake III Arena `q3map` derivative with Call of Duty changes: triangle soups, terrain, collision, fog, patch,
visibility and lightmap changes, and a different BSP format). The source is written so that Microsoft Visual C++ 7.1
(Visual Studio .NET 2003) reproduces the original machine code, function by function.

This project is not affiliated with or endorsed by Activision, Infinity Ward, Gray Matter Interactive, id Software,
ZeniMax or Microsoft. "Call of Duty", "Quake" and "Wolfenstein" are trademarks of their respective owners and are used
here only to describe what the code is. No game data, no original binary and no Microsoft software is part of this
repository.

## Status

- **990 of 990** project functions compile to the same bytes and relocations as the original, checked one by one.
- The linked image is **byte-identical** to the original `q3map.exe` (SHA-256 `edf423e0...e2fad`), except for three header
  fields that no build can produce: the link timestamp, the PDB GUID and the PDB age. `--identical` stamps the recorded
  original values onto a copy of the linked image, and that copy equals the original byte for byte.
- Byte identity proves the compiled image, not the source text: where several spellings compile to the same bytes, the
  choice among them is not evidence about the original.

Details: [docs/KNOWN_DIFFERENCES.md](docs/KNOWN_DIFFERENCES.md). Which parts of the source are choices rather
than proof: [docs/RECONSTRUCTION_NOTES.md](docs/RECONSTRUCTION_NOTES.md). Reconstructed names:
[docs/INFERRED_NAMES.md](docs/INFERRED_NAMES.md).

## Requirements

- Windows and Python 3.8 or newer (standard library only).
- Visual C++ 7.1, `cl.exe` 13.10.3077, with its static CRT, plus the Platform SDK mixture the original was built with:
  February 2003 SDK headers, the SDK import libraries and the August 2002 GlAux library. `--fetch-toolchain` downloads
  the pinned compiler, headers and GlAux archive (needs 7-Zip); the SDK import libraries are supplied separately. See
  [build/README.md](build/README.md); the build warns when toolchain files differ from the ones the result was verified with.

Other compilers do not give the same code.

## Build

```bat
python -I build\build.py --fetch-toolchain --sdk "C:\SDK\uo" --jobs 1 --strict --identical
```

or, with an installed Visual C++ 7.1:

```bat
python -I build\fetch_toolchain.py --sdk-headers-only
python -I build\build.py --vc7 "C:\Program Files\Microsoft Visual Studio .NET 2003\Vc7" --sdk "C:\SDK\uo" --glaux "C:\SDK\glaux_aug2002.lib" --jobs 1 --strict --identical
```

The build compiles the 75 translation units, builds the three static libraries (`jpeg6.lib`, `cmdlib.lib`,
`nvtristrip.lib`) and links the exe, then prints the SHA-256 of the result next to the SHA-256 of the original. It never
runs the program it builds. Add `--require-identical` to fail unless the image is identical, and `--original FILE` for
a byte and section comparison with your own copy. All options, the expected toolchain file hashes and the link-option
notes are in [build/README.md](build/README.md).

## Binaries

This repository contains no executables. The program it rebuilds is the original `q3map.exe` from the Call of Duty:
United Offensive mod tools; if you just need the tool, use the official mod tools. To verify the reconstruction, build it
with `--identical` and compare the printed SHA-256 with the original's
`edf423e0b7607c226bfe26bb591662a098a703a65459b91a53530923933e2fad` (561,152 bytes).

## How the match is established

Each function is compiled with the original compiler and flags and compared with the original: instruction
bytes, relocations and (for C++) unwind data must be equal. After that the whole image is linked and compared
against the original section by section. The per-function work was done with private tooling that is not part
of this repository; the result of it is the source in `src/` and the manifest in `build/sources.json`.
Where several spellings give identical bytes, the choice among them is not evidence about the original source.

## Repository layout

```
src/        the reconstruction (code/, common/, libs/, q3map/, universal/, win32/)
build/      build.py, build.bat, sources.json, fetch_toolchain.py, toolchain_manifest.json, stamp_meta.py, meta_stamp.json, compare_image.py
docs/       known differences, notes on what is proven and what is a choice, reconstructed names
COPYING     GPLv3 with id Software's additional terms
THIRD_PARTY_NOTICES.md
```

## License

GPL-3.0-or-later with the additional terms id Software applied to its Wolfenstein source releases: see
[COPYING](COPYING). Files that descend from the Quake III Arena source keep their original headers (GPL version 2 or,
at your option, any later version), which is used here under version 3. Third-party code (IJG jpeg-6b, zlib,
minizip, NvTriStrip) is under its own terms: see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
This software is based in part on the work of the Independent JPEG Group.

## Credits

- Reconstruction by Jane.
- Published by Rose.
- Thanks to Prawy (https://github.com/PrawyCoD1) for the idea for this project.

Evidence and sources:

- id Software: Quake III Arena (`q3map`, `common`, `qcommon`) and the Return to Castle Wolfenstein and Wolfenstein:
  Enemy Territory source releases, the base of the engine family.
- The Call of Duty (2003) `q3map.exe`, whose byte-identical reconstruction is the direct predecessor of this one.
- The GtkRadiant and q3map2 authors, whose published tools show the same family of code.
- Independent JPEG Group (libjpeg 6b), Jean-loup Gailly and Mark Adler (zlib 1.1.4), Gilles Vollant (minizip),
  NVIDIA (NvTriStrip).
- Function and variable names come from the published sources above and from the symbol tables and strings of other
  retail builds of the same game family, wherever the compiled image agrees; the rest are descriptive.

## Ports

This repository is the byte-identical reference build and stays that way. Ports to x64, to modern compilers or to other
platforms are welcome as forks; the hope is that someone takes this on.
