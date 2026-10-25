# Evidence and verification

The reference is the Call of Duty: United Offensive map-tools `q3map.exe` dated 2004-09-24.
Its complete hash and current differences are recorded in [known differences](KNOWN_DIFFERENCES.md).
The executable and private verification data are not distributed.

## Evidence order

1. Reference executable instructions, relocation destinations, strings, constants, access widths and linked layout.
2. Published Quake III Arena q3map and shared engine/tool source.
3. Published Return to Castle Wolfenstein and Wolfenstein: Enemy Territory source.
4. GtkRadiant/q3map2 family algorithms and conventions, checked against this executable.
5. Symbols, strings and link maps from genuine related retail builds, where behavior and layout agree.
6. Descriptive implementation and naming choices where stronger evidence is absent.

Other reconstructions can help navigate an algorithm but cannot establish original spellings, operand order, macros or helper shapes.
Byte identity of a function does not establish a unique source representation.

The JPEG component retains the IJG release 6b notice and license. Compression retains zlib 1.1.4 notices.
Minizip follows the unzip 0.15 code published with the Quake-family source. NVIDIA's NvTriStrip is tracked separately from project functions.

## Static verification and limits

990 of 990 project functions currently match their complete bytes and relocation destinations under VC7.1.
Jump tables, referenced data and C++ exception contributions are checked where applicable.
The complete stamped image equals the reference.
Complete-file comparison establishes this result.

The release driver compiles only `build/sources.json`, creates its static libraries and links normally.
The metadata-only stamp changes the COFF/debug timestamp and RSDS GUID/age in a separate copy.
It supplies no missing code, data, imports, Rich records or library bodies from the reference.
No runtime testing is implied by these static checks.
