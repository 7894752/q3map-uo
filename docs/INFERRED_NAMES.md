# Inferred source names

Names below distinguish observed behavior from historical spelling. Local variables, parameters, file boundaries and record names
are descriptive unless published source, executable strings or related retail symbols provide stronger support.

| Area / current names | Evidence and limit |
| --- | --- |
| Shared Quake-family APIs | Published Quake III Arena, RTCW and ET source support names where the UO implementation agrees |
| BSP, portal, brush and patch records | Member offsets, access widths, serialized data and consumers constrain layout; unread fields and original type names remain uncertain |
| `ProjectionCoordsFromNormal` | Dominant-normal-component selection establishes the two projected axes and their ordering; the name is descriptive |
| `ComputeEdgeLine2D` | The routine constructs a projected edge line; behavior supports the role, not the exact historical identifier |
| `TriangleMinAngleCosine` | The triangle angle calculation establishes the operation; original spelling is not proven |
| `TesselateWinding` and winding helpers | Control flow and geometry accesses establish ear selection and removal; the spelling and source-level local roles are not uniquely determined |
| `LightmapPolygonAreaAndCentroid` | Polygon area and first moments establish the calculation; the function is accepted |
| `TrianglePairCanShareEdge`, `MergeConcaveWindingGroup` | These descriptive names identify triangle/winding operations; both are accepted; names do not establish historical spelling |
| NvTriStrip records, constructors and templates | NVIDIA library lineage and emitted code establish roles; header organization and definition visibility remain reconstruction choices |
| Inline copies, local aliases and helper boundaries | Emission and allocation constrain viable source contexts; identical code can have several source spellings |

See [evidence](EVIDENCE.md) and [reconstruction notes](RECONSTRUCTION_NOTES.md).
