# Reconstruction notes

This snapshot rebuilds the 2004 Call of Duty: United Offensive BSP compiler with Visual C++ 7.1.
The complete reference image is reproduced; see [verification](BUILD_VERIFICATION.md) and the [metadata policy](KNOWN_DIFFERENCES.md).

## What matching proves

Instruction bytes, constants, strings, access widths, member offsets, calling behavior and relocation destinations constrain the implementation.
The equal image also constrains storage, imports, section layout, padding and exception metadata.
It does not recover names absent from surviving evidence or establish a unique spelling, declaration order or source-file arrangement.

The build manifest preserves the measured compiler flags, source order, library membership and link inputs.
VC7.1 private static calling conventions, inline expansion, x87 arithmetic scheduling and template emission are sensitive to source context.
Changing an apparently neutral declaration, alias or helper boundary can change code or linked placement.

## Retained forms and limits

- Geometry routines retain real pointer/index views and shared local roles where those affect observed code generation.
- Ear selection in `TesselateWinding` uses an ordinary jump to the next candidate after an unmatched-point failure.
  This preserves the target's allocation without introducing unused storage or fake operations.
- Some recursive geometry routines retain compiler-specific organization, and a few low-level routines use x86 assembly.
  These are part of the reference configuration, not a claim of portable C behavior.
- NvTriStrip uses target-era types and measured definition visibility. Template and constructor placement agree with the reference image.
- Descriptive identifiers and source boundaries are choices unless stronger evidence is stated in [inferred names](INFERRED_NAMES.md).

The source is preserved without replacing functions with binary patches.
Only timestamp/PDB signature metadata is stamped; code, data, import tables and Rich records come from compilation and linking.
The export excludes verification internals, unrelated inactive source files, SDK files and reference images.
