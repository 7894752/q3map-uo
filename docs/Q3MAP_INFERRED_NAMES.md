# q3map reconstruction spellings

The executable does not recover C identifier spellings. This conservative
inventory records every locally defined function, macro, enum constant, record
field and module variable found in the audited q3map sources. It includes names
inherited from released source as well as descriptive reconstruction names, so
an unverified spelling is never silently presented as a recovered studio name.
The stated reasons describe the data or behavior that motivated each name;
they do not establish that the historical UO source used that spelling.

Genuine released Quake III Arena, RTCW/ET and q3map2 source are style references.
No other reconstruction is evidence for a spelling. The machine inventory is
deliberately conservative: shared declarations and descriptive names can have
more than one module entry, and ordinary local counters are outside its scope.
Array dimensions and structure layouts follow the binary interfaces; names do
not imply that a legacy implementation quirk has been corrected.

## Enum Constants

| Name | Module / record | Reason |
| --- | --- | --- |
| `LIGHTMAP_BLOCK_SIZE` | lightmaps.c / local workspace | Names lightmap block size; its numeric value follows the recovered format or limit. |
| `LIGHTMAP_GROUP_BATCH_LIMIT` | lightmaps.c / local workspace | Names lightmap group batch limit; its numeric value follows the recovered format or limit. |
| `LIGHTMAP_POLYGON_POINTS` | lightmaps.c / local workspace | Names lightmap polygon points; its numeric value follows the recovered format or limit. |
| `LIGHTMAP_POLYGON_WORK_POINTS` | lightmaps.c / local workspace | Names lightmap polygon work points; its numeric value follows the recovered format or limit. |
| `MAX_LIGHTMAP_STORAGE` | lightmaps.c / local workspace | Names max lightmap storage; its numeric value follows the recovered format or limit. |
| `stat_done` | vis.h / vstatus_t | Names stat done; its numeric value follows the recovered format or limit. |
| `stat_none` | vis.h / vstatus_t | Names stat none; its numeric value follows the recovered format or limit. |
| `stat_working` | vis.h / vstatus_t | Names stat working; its numeric value follows the recovered format or limit. |

## Fields

| Name | Module / record | Reason |
| --- | --- | --- |
| `numpoints` | brush.c / double_winding_t | Stores numpoints in double_winding_t (int numpoints). |
| `p` | brush.c / double_winding_t | Stores p in double_winding_t (double p[4][3]). |
| `height` | lightmaps.c / lightmapBlock_s | Stores height in lightmapBlock_s (int width, height). |
| `lightmapNum` | lightmaps.c / lightmapBlock_s | Stores lightmap num in lightmapBlock_s (int lightmapNum). |
| `next` | lightmaps.c / lightmapBlock_s | Stores next in lightmapBlock_s (struct lightmapBlock_s *next, *prev). |
| `prev` | lightmaps.c / lightmapBlock_s | Stores prev in lightmapBlock_s (struct lightmapBlock_s *next, *prev). |
| `width` | lightmaps.c / lightmapBlock_s | Stores width in lightmapBlock_s (int width, height). |
| `x` | lightmaps.c / lightmapBlock_s | Stores x in lightmapBlock_s (int x, y). |
| `y` | lightmaps.c / lightmapBlock_s | Stores y in lightmapBlock_s (int x, y). |
| `axis` | lightmaps.c / lightmapDimension_t | Stores axis in lightmapDimension_t (int axis, size). |
| `size` | lightmaps.c / lightmapDimension_t | Stores size in lightmapDimension_t (int axis, size). |
| `count` | lightmaps.c / lightmapGroupCell_t | Stores count in lightmapGroupCell_t (int count). |
| `groups` | lightmaps.c / lightmapGroupCell_t | Stores groups in lightmapGroupCell_t (int groups[2]). |
| `lightmaps` | lightmaps.c / lightmapMaterial_t | Stores lightmaps in lightmapMaterial_t (lightmapRef_t *lightmaps). |
| `maxArea` | lightmaps.c / lightmapMaterial_t | Stores max area in lightmapMaterial_t (int maxArea). |
| `numSurfaces` | lightmaps.c / lightmapMaterial_t | Stores num surfaces in lightmapMaterial_t (int numSurfaces). |
| `surfaces` | lightmaps.c / lightmapMaterial_t | Stores surfaces in lightmapMaterial_t (mapDrawSurface_t *surfaces). |
| `lightmapNum` | lightmaps.c / lightmapRef_s | Stores lightmap num in lightmapRef_s (int lightmapNum). |
| `next` | lightmaps.c / lightmapRef_s | Stores next in lightmapRef_s (struct lightmapRef_s *next). |
| `mesh` | lightmaps.c / patchLightmapProjection_t | Stores mesh in patchLightmapProjection_t (mesh_t mesh). |
| `plane` | lightmaps.c / patchLightmapProjection_t | Stores plane in patchLightmapProjection_t (vec4_t plane). |
| `height` | mesh.h / mesh_t | Stores height in mesh_t (int width, height). |
| `lightmapSampleSize` | mesh.h / mesh_t | Stores lightmap sample size in mesh_t (int lightmapSampleSize). |
| `patchSubdivisions` | mesh.h / mesh_t | Stores patch subdivisions in mesh_t (int patchSubdivisions). |
| `terrainFlags` | mesh.h / mesh_t | Stores terrain flags in mesh_t (int *terrainFlags). |
| `verts` | mesh.h / mesh_t | Stores verts in mesh_t (drawVert_t *verts). |
| `width` | mesh.h / mesh_t | Stores width in mesh_t (int width, height). |
| `patch` | patch.c / terrainPatchEntry_t | Stores patch in terrainPatchEntry_t (parseMesh_t *patch). |
| `projectionAxis` | patch.c / terrainPatchEntry_t | Stores projection axis in terrainPatchEntry_t (int projectionAxis). |
| `next` | portals.c / cellPortal_s | Stores next in cellPortal_s (struct cellPortal_s *next). |
| `otherNode` | portals.c / cellPortal_s | Stores other node in cellPortal_s (node_t *otherNode). |
| `side` | portals.c / cellPortal_s | Stores side in cellPortal_s (side_t *side). |
| `brushnum` | qbsp.h / bspbrush_s | Stores brushnum in bspbrush_s (int brushnum). |
| `contentShader` | qbsp.h / bspbrush_s | Stores content shader in bspbrush_s (struct shaderInfo_s *contentShader). |
| `contents` | qbsp.h / bspbrush_s | Stores contents in bspbrush_s (int contents). |
| `cullgroup` | qbsp.h / bspbrush_s | Stores cullgroup in bspbrush_s (int cullgroup). |
| `detail` | qbsp.h / bspbrush_s | Stores detail in bspbrush_s (qboolean detail). |
| `entitynum` | qbsp.h / bspbrush_s | Stores entitynum in bspbrush_s (int entitynum). |
| `isOccluder` | qbsp.h / bspbrush_s | Stores is occluder in bspbrush_s (qboolean isOccluder). |
| `maxs` | qbsp.h / bspbrush_s | Stores maxs in bspbrush_s (vec3_t mins, maxs). |
| `mins` | qbsp.h / bspbrush_s | Stores mins in bspbrush_s (vec3_t mins, maxs). |
| `next` | qbsp.h / bspbrush_s | Stores next in bspbrush_s (struct bspbrush_s *next). |
| `noBspOutput` | qbsp.h / bspbrush_s | Stores no bsp output in bspbrush_s (qboolean noBspOutput). |
| `numsides` | qbsp.h / bspbrush_s | Stores numsides in bspbrush_s (int numsides). |
| `opaque` | qbsp.h / bspbrush_s | Stores opaque in bspbrush_s (qboolean opaque). |
| `original` | qbsp.h / bspbrush_s | Stores original in bspbrush_s (struct bspbrush_s *original). |
| `outputNumber` | qbsp.h / bspbrush_s | Stores output number in bspbrush_s (int outputNumber). |
| `portalareas` | qbsp.h / bspbrush_s | Stores portalareas in bspbrush_s (int portalareas[2]). |
| `sides` | qbsp.h / bspbrush_s | Stores sides in bspbrush_s (side_t sides[6]). |
| `checked` | qbsp.h / bspface_s | Stores checked in bspface_s (qboolean checked). |
| `hint` | qbsp.h / bspface_s | Stores hint in bspface_s (qboolean hint). |
| `next` | qbsp.h / bspface_s | Stores next in bspface_s (struct bspface_s *next). |
| `planenum` | qbsp.h / bspface_s | Stores planenum in bspface_s (int planenum). |
| `priority` | qbsp.h / bspface_s | Stores priority in bspface_s (int priority). |
| `w` | qbsp.h / bspface_s | Stores w in bspface_s (winding_t *w). |
| `dist` | qbsp.h / cplane_s | Stores dist in cplane_s (float dist). |
| `normal` | qbsp.h / cplane_s | Stores normal in cplane_s (vec3_t normal). |
| `pad` | qbsp.h / cplane_s | Stores pad in cplane_s (byte pad[2]). |
| `signbits` | qbsp.h / cplane_s | Stores signbits in cplane_s (byte signbits). |
| `type` | qbsp.h / cplane_s | Stores type in cplane_s (byte type). |
| `nextRef` | qbsp.h / drawSurfRef_s | Stores next ref in drawSurfRef_s (struct drawSurfRef_s *nextRef). |
| `outputNumber` | qbsp.h / drawSurfRef_s | Stores output number in drawSurfRef_s (int outputNumber). |
| `contents` | qbsp.h / drawsurf_s | Stores contents in drawsurf_s (int contents). |
| `cullgroup` | qbsp.h / drawsurf_s | Stores cullgroup in drawsurf_s (int cullgroup). |
| `flareSurface` | qbsp.h / drawsurf_s | Stores flare surface in drawsurf_s (qboolean flareSurface). |
| `fogNum` | qbsp.h / drawsurf_s | Stores fog num in drawsurf_s (int fogNum). |
| `indexes` | qbsp.h / drawsurf_s | Stores indexes in drawsurf_s (int *indexes). |
| `isTerrain` | qbsp.h / drawsurf_s | Stores is terrain in drawsurf_s (qboolean isTerrain). |
| `lightmapGroupNum` | qbsp.h / drawsurf_s | Stores lightmap group num in drawsurf_s (int lightmapGroupNum). |
| `lightmapGroupVisited` | qbsp.h / drawsurf_s | Stores lightmap group visited in drawsurf_s (qboolean lightmapGroupVisited). |
| `lightmapHeight` | qbsp.h / drawsurf_s | Stores lightmap height in drawsurf_s (int lightmapWidth, lightmapHeight). |
| `lightmapNum` | qbsp.h / drawsurf_s | Stores lightmap num in drawsurf_s (int lightmapNum). |
| `lightmapOrigin` | qbsp.h / drawsurf_s | Stores lightmap origin in drawsurf_s (vec3_t lightmapOrigin). |
| `lightmapPlaneNum` | qbsp.h / drawsurf_s | Stores lightmap plane num in drawsurf_s (int lightmapPlaneNum). |
| `lightmapSampleSize` | qbsp.h / drawsurf_s | Stores lightmap sample size in drawsurf_s (int lightmapSampleSize). |
| `lightmapVecs` | qbsp.h / drawsurf_s | Stores lightmap vecs in drawsurf_s (vec3_t lightmapVecs[3]). |
| `lightmapWidth` | qbsp.h / drawsurf_s | Stores lightmap width in drawsurf_s (int lightmapWidth, lightmapHeight). |
| `lightmapX` | qbsp.h / drawsurf_s | Stores lightmap x in drawsurf_s (int lightmapX, lightmapY). |
| `lightmapY` | qbsp.h / drawsurf_s | Stores lightmap y in drawsurf_s (int lightmapX, lightmapY). |
| `mapBrush` | qbsp.h / drawsurf_s | Stores map brush in drawsurf_s (bspbrush_t *mapBrush). |
| `maxs` | qbsp.h / drawsurf_s | Stores maxs in drawsurf_s (vec3_t mins, maxs). |
| `mins` | qbsp.h / drawsurf_s | Stores mins in drawsurf_s (vec3_t mins, maxs). |
| `miscModel` | qbsp.h / drawsurf_s | Stores misc model in drawsurf_s (qboolean miscModel). |
| `nextOnLightmapGroup` | qbsp.h / drawsurf_s | Stores next on lightmap group in drawsurf_s (struct drawsurf_s *nextOnLightmapGroup). |
| `nextOnShader` | qbsp.h / drawsurf_s | Stores next on shader in drawsurf_s (struct drawsurf_s *nextOnShader). |
| `numIndexes` | qbsp.h / drawsurf_s | Stores num indexes in drawsurf_s (int numIndexes). |
| `numVerts` | qbsp.h / drawsurf_s | Stores num verts in drawsurf_s (int numVerts). |
| `patch` | qbsp.h / drawsurf_s | Stores patch in drawsurf_s (qboolean patch). |
| `patchHeight` | qbsp.h / drawsurf_s | Stores patch height in drawsurf_s (int patchHeight). |
| `patchSubdivisions` | qbsp.h / drawsurf_s | Stores patch subdivisions in drawsurf_s (int patchSubdivisions). |
| `patchWidth` | qbsp.h / drawsurf_s | Stores patch width in drawsurf_s (int patchWidth). |
| `planar` | qbsp.h / drawsurf_s | Stores planar in drawsurf_s (qboolean planar). |
| `shaderInfo` | qbsp.h / drawsurf_s | Stores shader info in drawsurf_s (shaderInfo_t *shaderInfo). |
| `side` | qbsp.h / drawsurf_s | Stores side in drawsurf_s (side_t *side). |
| `triangleSoup` | qbsp.h / drawsurf_s | Stores triangle soup in drawsurf_s (qboolean triangleSoup). |
| `verts` | qbsp.h / drawsurf_s | Stores verts in drawsurf_s (drawVert_t *verts). |
| `area` | qbsp.h / node_s | Stores area in node_s (int area). |
| `areaportal` | qbsp.h / node_s | Stores areaportal in node_s (qboolean areaportal). |
| `brushlist` | qbsp.h / node_s | Stores brushlist in node_s (bspbrush_t *brushlist). |
| `bspCell` | qbsp.h / node_s | Stores bsp cell in node_s (int bspCell). |
| `children` | qbsp.h / node_s | Stores children in node_s (struct node_s *children[2]). |
| `cluster` | qbsp.h / node_s | Stores cluster in node_s (int cluster). |
| `collisionSurfReferences` | qbsp.h / node_s | Stores collision surf references in node_s (drawSurfRef_t *collisionSurfReferences). |
| `drawSurfReferences` | qbsp.h / node_s | Stores draw surf references in node_s (drawSurfRef_t *drawSurfReferences). |
| `hint` | qbsp.h / node_s | Stores hint in node_s (qboolean hint). |
| `maxs` | qbsp.h / node_s | Stores maxs in node_s (vec3_t mins, maxs). |
| `mins` | qbsp.h / node_s | Stores mins in node_s (vec3_t mins, maxs). |
| `occupant` | qbsp.h / node_s | Stores occupant in node_s (entity_t *occupant). |
| `occupied` | qbsp.h / node_s | Stores occupied in node_s (int occupied). |
| `opaque` | qbsp.h / node_s | Stores opaque in node_s (qboolean opaque). |
| `pad` | qbsp.h / node_s | Stores pad in node_s (int pad). |
| `parent` | qbsp.h / node_s | Stores parent in node_s (struct node_s *parent). |
| `planenum` | qbsp.h / node_s | Stores planenum in node_s (int planenum). |
| `portals` | qbsp.h / node_s | Stores portals in node_s (struct portal_s *portals). |
| `referencepoint` | qbsp.h / node_s | Stores referencepoint in node_s (vec3_t referencepoint). |
| `side` | qbsp.h / node_s | Stores side in node_s (side_t *side). |
| `tinyportals` | qbsp.h / node_s | Stores tinyportals in node_s (int tinyportals). |
| `volume` | qbsp.h / node_s | Stores volume in node_s (bspbrush_t *volume). |
| `brushnum` | qbsp.h / parseMesh_s | Stores brushnum in parseMesh_s (int brushnum). |
| `contents` | qbsp.h / parseMesh_s | Stores contents in parseMesh_s (int contents). |
| `cullgroup` | qbsp.h / parseMesh_s | Stores cullgroup in parseMesh_s (int cullgroup). |
| `entitynum` | qbsp.h / parseMesh_s | Stores entitynum in parseMesh_s (int entitynum). |
| `groupChain` | qbsp.h / parseMesh_s | Stores group chain in parseMesh_s (struct parseMesh_s *groupChain). |
| `grouped` | qbsp.h / parseMesh_s | Stores grouped in parseMesh_s (qboolean grouped). |
| `isTerrain` | qbsp.h / parseMesh_s | Stores is terrain in parseMesh_s (qboolean isTerrain). |
| `mesh` | qbsp.h / parseMesh_s | Stores mesh in parseMesh_s (mesh_t mesh). |
| `next` | qbsp.h / parseMesh_s | Stores next in parseMesh_s (struct parseMesh_s *next). |
| `shaderInfo` | qbsp.h / parseMesh_s | Stores shader info in parseMesh_s (shaderInfo_t *shaderInfo). |
| `dist` | qbsp.h / plane_s | Stores dist in plane_s (vec_t dist). |
| `hash_chain` | qbsp.h / plane_s | Stores hash chain in plane_s (struct plane_s *hash_chain). |
| `normal` | qbsp.h / plane_s | Stores normal in plane_s (vec3_t normal). |
| `type` | qbsp.h / plane_s | Stores type in plane_s (int type). |
| `used` | qbsp.h / plane_s | Stores used in plane_s (qboolean used). |
| `brush` | qbsp.h / portal_s | Stores brush in portal_s (bspbrush_t *brush). |
| `hint` | qbsp.h / portal_s | Stores hint in portal_s (qboolean hint). |
| `next` | qbsp.h / portal_s | Stores next in portal_s (struct portal_s *next[2]). |
| `nodes` | qbsp.h / portal_s | Stores nodes in portal_s (node_t *nodes[2]). |
| `onnode` | qbsp.h / portal_s | Stores onnode in portal_s (node_t *onnode). |
| `plane` | qbsp.h / portal_s | Stores plane in portal_s (plane_t plane). |
| `side` | qbsp.h / portal_s | Stores side in portal_s (side_t *side). |
| `sidefound` | qbsp.h / portal_s | Stores sidefound in portal_s (qboolean sidefound). |
| `winding` | qbsp.h / portal_s | Stores winding in portal_s (winding_t *winding). |
| `backSide` | qbsp.h / side_s | Stores back side in side_s (qboolean backSide). |
| `bevel` | qbsp.h / side_s | Stores bevel in side_s (qboolean bevel). |
| `contents` | qbsp.h / side_s | Stores contents in side_s (int contents). |
| `lightmapSampleSize` | qbsp.h / side_s | Stores lightmap sample size in side_s (int lightmapSampleSize). |
| `planenum` | qbsp.h / side_s | Stores planenum in side_s (int planenum). |
| `portalBrush` | qbsp.h / side_s | Stores portal brush in side_s (struct bspbrush_s *portalBrush). |
| `portalCellCount` | qbsp.h / side_s | Stores portal cell count in side_s (int portalCellCount[2]). |
| `portalIgnored` | qbsp.h / side_s | Stores portal ignored in side_s (qboolean portalIgnored). |
| `shaderInfo` | qbsp.h / side_s | Stores shader info in side_s (struct shaderInfo_s *shaderInfo). |
| `surfaceFlags` | qbsp.h / side_s | Stores surface flags in side_s (int surfaceFlags). |
| `texMat` | qbsp.h / side_s | Stores tex mat in side_s (float texMat[2][3]). |
| `value` | qbsp.h / side_s | Stores value in side_s (int value). |
| `vecs` | qbsp.h / side_s | Stores vecs in side_s (float vecs[2][4]). |
| `visible` | qbsp.h / side_s | Stores visible in side_s (qboolean visible). |
| `visibleHull` | qbsp.h / side_s | Stores visible hull in side_s (winding_t *visibleHull). |
| `winding` | qbsp.h / side_s | Stores winding in side_s (winding_t *winding). |
| `headnode` | qbsp.h / tree_t | Stores headnode in tree_t (node_t *headnode). |
| `maxs` | qbsp.h / tree_t | Stores maxs in tree_t (vec3_t mins, maxs). |
| `mins` | qbsp.h / tree_t | Stores mins in tree_t (vec3_t mins, maxs). |
| `outside_node` | qbsp.h / tree_t | Stores outside node in tree_t (node_t outside_node). |
| `clearSolid` | shaders.h / infoParm_t | Stores clear solid in infoParm_t (int clearSolid, surfaceFlags, contents). |
| `contents` | shaders.h / infoParm_t | Stores contents in infoParm_t (int clearSolid, surfaceFlags, contents). |
| `name` | shaders.h / infoParm_t | Stores name in infoParm_t (char *name). |
| `surfaceFlags` | shaders.h / infoParm_t | Stores surface flags in infoParm_t (int clearSolid, surfaceFlags, contents). |
| `autosprite` | shaders.h / shaderInfo_s | Stores autosprite in shaderInfo_s (qboolean autosprite). |
| `backShader` | shaders.h / shaderInfo_s | Stores back shader in shaderInfo_s (char backShader[MAX_QPATH]). |
| `backsplashDistance` | shaders.h / shaderInfo_s | Stores backsplash distance in shaderInfo_s (float backsplashDistance). |
| `backsplashFraction` | shaders.h / shaderInfo_s | Stores backsplash fraction in shaderInfo_s (float backsplashFraction). |
| `clampTexture` | shaders.h / shaderInfo_s | Stores clamp texture in shaderInfo_s (qboolean clampTexture). |
| `contents` | shaders.h / shaderInfo_s | Stores contents in shaderInfo_s (int contents). |
| `editorimage` | shaders.h / shaderInfo_s | Stores editorimage in shaderInfo_s (char editorimage[MAX_QPATH]). |
| `flap` | shaders.h / shaderInfo_s | Stores flap in shaderInfo_s (qboolean flap). |
| `flareShader` | shaders.h / shaderInfo_s | Stores flare shader in shaderInfo_s (char flareShader[MAX_QPATH]). |
| `forceSunLight` | shaders.h / shaderInfo_s | Stores force sun light in shaderInfo_s (qboolean forceSunLight). |
| `forceTraceLight` | shaders.h / shaderInfo_s | Stores force trace light in shaderInfo_s (qboolean forceTraceLight). |
| `forceVLight` | shaders.h / shaderInfo_s | Stores force vlight in shaderInfo_s (qboolean forceVLight). |
| `globalTexture` | shaders.h / shaderInfo_s | Stores global texture in shaderInfo_s (qboolean globalTexture). |
| `hasPasses` | shaders.h / shaderInfo_s | Stores has passes in shaderInfo_s (qboolean hasPasses). |
| `height` | shaders.h / shaderInfo_s | Stores height in shaderInfo_s (int width, height). |
| `isOccluder` | shaders.h / shaderInfo_s | Stores is occluder in shaderInfo_s (qboolean isOccluder). |
| `lightFilter` | shaders.h / shaderInfo_s | Stores light filter in shaderInfo_s (qboolean lightFilter). |
| `lightSubdivide` | shaders.h / shaderInfo_s | Stores light subdivide in shaderInfo_s (float lightSubdivide). |
| `lightimage` | shaders.h / shaderInfo_s | Stores lightimage in shaderInfo_s (char lightimage[MAX_QPATH]). |
| `lightmapSampleSize` | shaders.h / shaderInfo_s | Stores lightmap sample size in shaderInfo_s (int lightmapSampleSize). |
| `noVertexShadows` | shaders.h / shaderInfo_s | Stores no vertex shadows in shaderInfo_s (qboolean noVertexShadows). |
| `notjunc` | shaders.h / shaderInfo_s | Stores notjunc in shaderInfo_s (qboolean notjunc). |
| `patchShadows` | shaders.h / shaderInfo_s | Stores patch shadows in shaderInfo_s (qboolean patchShadows). |
| `shader` | shaders.h / shaderInfo_s | Stores shader in shaderInfo_s (char shader[MAX_QPATH]). |
| `smoothingGroup` | shaders.h / shaderInfo_s | Stores smoothing group in shaderInfo_s (int smoothingGroup). |
| `subdivisions` | shaders.h / shaderInfo_s | Stores subdivisions in shaderInfo_s (float subdivisions). |
| `sunDirection` | shaders.h / shaderInfo_s | Stores sun direction in shaderInfo_s (vec3_t sunDirection). |
| `sunLight` | shaders.h / shaderInfo_s | Stores sun light in shaderInfo_s (vec3_t sunLight). |
| `surfaceFlags` | shaders.h / shaderInfo_s | Stores surface flags in shaderInfo_s (int surfaceFlags). |
| `twoSided` | shaders.h / shaderInfo_s | Stores two sided in shaderInfo_s (qboolean twoSided). |
| `value` | shaders.h / shaderInfo_s | Stores value in shaderInfo_s (int value). |
| `vertexScale` | shaders.h / shaderInfo_s | Stores vertex scale in shaderInfo_s (float vertexScale). |
| `vertexShadows` | shaders.h / shaderInfo_s | Stores vertex shadows in shaderInfo_s (qboolean vertexShadows). |
| `width` | shaders.h / shaderInfo_s | Stores width in shaderInfo_s (int width, height). |
| `count` | surface.c / sideRef_t | Stores count in sideRef_t (int count). |
| `planenum` | surface.c / sideRef_t | Stores planenum in sideRef_t (int planenum). |
| `shaderInfo` | surface.c / sideRef_t | Stores shader info in sideRef_t (shaderInfo_t *shaderInfo). |
| `lightmapScale` | terrain.c / terrainFace_s | Stores lightmap scale in terrainFace_s (int lightmapScale). |
| `shaderInfo` | terrain.c / terrainFace_s | Stores shader info in terrainFace_s (shaderInfo_t *shaderInfo). |
| `vecs` | terrain.c / terrainFace_s | Stores vecs in terrainFace_s (float vecs[2][4]). |
| `height` | terrain.c / terrainMesh_s | Stores height in terrainMesh_s (int width, height). |
| `map` | terrain.c / terrainMesh_s | Stores map in terrainMesh_s (terrainVert_t *map). |
| `origin` | terrain.c / terrainMesh_s | Stores origin in terrainMesh_s (vec3_t origin). |
| `scale_x` | terrain.c / terrainMesh_s | Stores scale x in terrainMesh_s (float scale_x). |
| `scale_y` | terrain.c / terrainMesh_s | Stores scale y in terrainMesh_s (float scale_y). |
| `width` | terrain.c / terrainMesh_s | Stores width in terrainMesh_s (int width, height). |
| `indexes` | terrain.c / terrainSurf_s | Stores indexes in terrainSurf_s (int *indexes). |
| `maxIndexes` | terrain.c / terrainSurf_s | Stores max indexes in terrainSurf_s (int maxIndexes). |
| `maxVerts` | terrain.c / terrainSurf_s | Stores max verts in terrainSurf_s (int maxVerts). |
| `numIndexes` | terrain.c / terrainSurf_s | Stores num indexes in terrainSurf_s (int numIndexes). |
| `numVerts` | terrain.c / terrainSurf_s | Stores num verts in terrainSurf_s (int numVerts). |
| `shader` | terrain.c / terrainSurf_s | Stores shader in terrainSurf_s (shaderInfo_t *shader). |
| `verts` | terrain.c / terrainSurf_s | Stores verts in terrainSurf_s (drawVert_t *verts). |
| `x` | terrain.c / terrainSurf_s | Stores x in terrainSurf_s (int x, y). |
| `y` | terrain.c / terrainSurf_s | Stores y in terrainSurf_s (int x, y). |
| `tri` | terrain.c / terrainVert_s | Stores tri in terrainVert_s (terrainFace_t tri). |
| `xyz` | terrain.c / terrainVert_s | Stores xyz in terrainVert_s (vec3_t xyz). |
| `contents` | terrain_surface.h / terrainSurface_s | Stores contents in terrainSurface_s (int contents). |
| `cullgroup` | terrain_surface.h / terrainSurface_s | Stores cullgroup in terrainSurface_s (int cullgroup). |
| `indexes` | terrain_surface.h / terrainSurface_s | Stores indexes in terrainSurface_s (unsigned short *indexes). |
| `lightmapSampleSize` | terrain_surface.h / terrainSurface_s | Stores lightmap sample size in terrainSurface_s (int lightmapSampleSize). |
| `next` | terrain_surface.h / terrainSurface_s | Stores next in terrainSurface_s (struct terrainSurface_s *next). |
| `numIndexes` | terrain_surface.h / terrainSurface_s | Stores num indexes in terrainSurface_s (int numIndexes). |
| `numVerts` | terrain_surface.h / terrainSurface_s | Stores num verts in terrainSurface_s (int numVerts). |
| `shaderInfo` | terrain_surface.h / terrainSurface_s | Stores shader info in terrainSurface_s (shaderInfo_t *shaderInfo). |
| `verts` | terrain_surface.h / terrainSurface_s | Stores verts in terrainSurface_s (drawVert_t *verts). |
| `chain` | tjunction.c / edgeLine_s | Stores chain in edgeLine_s (edgePoint_t chain). |
| `dir` | tjunction.c / edgeLine_s | Stores dir in edgeLine_s (vec3_t dir). |
| `dist1` | tjunction.c / edgeLine_s | Stores dist1 in edgeLine_s (float dist1). |
| `dist2` | tjunction.c / edgeLine_s | Stores dist2 in edgeLine_s (float dist2). |
| `normal1` | tjunction.c / edgeLine_s | Stores normal1 in edgeLine_s (vec3_t normal1). |
| `normal2` | tjunction.c / edgeLine_s | Stores normal2 in edgeLine_s (vec3_t normal2). |
| `intercept` | tjunction.c / edgePoint_s | Stores intercept in edgePoint_s (float intercept). |
| `next` | tjunction.c / edgePoint_s | Stores next in edgePoint_s (struct edgePoint_s *prev, *next). |
| `prev` | tjunction.c / edgePoint_s | Stores prev in edgePoint_s (struct edgePoint_s *prev, *next). |
| `xyz` | tjunction.c / edgePoint_s | Stores xyz in edgePoint_s (vec3_t xyz). |
| `dv` | tjunction.c / originalEdge_t | Stores dv in originalEdge_t (drawVert_t *dv[2]). |
| `length` | tjunction.c / originalEdge_t | Stores length in originalEdge_t (float length). |
| `indices` | tris.c / local | Stores indices in local (int indices[TRI_AABB_LOCAL_ITEMS]). |
| `maxs` | tris.c / local | Stores maxs in local (vec3_t maxs[TRI_AABB_LOCAL_ITEMS]). |
| `mins` | tris.c / local | Stores mins in local (vec3_t mins[TRI_AABB_LOCAL_ITEMS]). |
| `sortEqual` | tris.c / local | Stores sort equal in local (float sortEqual[TRI_AABB_LOCAL_ITEMS]). |
| `sortMaxs` | tris.c / local | Stores sort maxs in local (float sortMaxs[TRI_AABB_LOCAL_ITEMS]). |
| `sortMins` | tris.c / local | Stores sort mins in local (float sortMins[TRI_AABB_LOCAL_ITEMS]). |
| `edgeIdx` | tris.c / tessSplitPoint_s | Stores edge idx in tessSplitPoint_s (int edgeIdx). |
| `position` | tris.c / tessSplitPoint_s | Stores position in tessSplitPoint_s (float position). |
| `vertIdx` | tris.c / tessSplitPoint_s | Stores vert idx in tessSplitPoint_s (int vertIdx). |
| `maxs` | tris.c / tjuncCellBounds_s | Stores maxs in tjuncCellBounds_s (vec3_t maxs). |
| `mins` | tris.c / tjuncCellBounds_s | Stores mins in tjuncCellBounds_s (vec3_t mins). |
| `direction` | tris.c / tjuncEdgeLine_s | Stores direction in tjuncEdgeLine_s (vec3_t direction). |
| `dist1` | tris.c / tjuncEdgeLine_s | Stores dist1 in tjuncEdgeLine_s (float dist1). |
| `dist2` | tris.c / tjuncEdgeLine_s | Stores dist2 in tjuncEdgeLine_s (float dist2). |
| `normal1` | tris.c / tjuncEdgeLine_s | Stores normal1 in tjuncEdgeLine_s (vec3_t normal1). |
| `normal2` | tris.c / tjuncEdgeLine_s | Stores normal2 in tjuncEdgeLine_s (vec3_t normal2). |
| `origin` | tris.c / tjuncEdgeLine_s | Stores origin in tjuncEdgeLine_s (vec3_t origin). |
| `sentinel` | tris.c / tjuncEdgeLine_s | Stores sentinel in tjuncEdgeLine_s (tjuncPoint_t sentinel). |
| `edgeLine` | tris.c / tjuncHashNode_s | Stores edge line in tjuncHashNode_s (tjuncEdgeLine_t *edgeLine). |
| `next` | tris.c / tjuncHashNode_s | Stores next in tjuncHashNode_s (struct tjuncHashNode_s *next). |
| `intercept` | tris.c / tjuncPoint_s | Stores intercept in tjuncPoint_s (float intercept). |
| `next` | tris.c / tjuncPoint_s | Stores next in tjuncPoint_s (struct tjuncPoint_s *next). |
| `prev` | tris.c / tjuncPoint_s | Stores prev in tjuncPoint_s (struct tjuncPoint_s *prev). |
| `xyz` | tris.c / tjuncPoint_s | Stores xyz in tjuncPoint_s (vec3_t xyz). |
| `colorVecs` | tris.c / triGroupRecord_s | Stores color vecs in triGroupRecord_s (float colorVecs[4][4]). |
| `cullGroupIdx` | tris.c / triGroupRecord_s | Stores cull group idx in triGroupRecord_s (int cullGroupIdx). |
| `drawOrder` | tris.c / triGroupRecord_s | Stores draw order in triGroupRecord_s (int drawOrder). |
| `edgeIdx` | tris.c / triGroupRecord_s | Stores edge idx in triGroupRecord_s (int edgeIdx[3]). |
| `groupId` | tris.c / triGroupRecord_s | Stores group id in triGroupRecord_s (int groupId). |
| `lightStyle` | tris.c / triGroupRecord_s | Stores light style in triGroupRecord_s (int lightStyle). |
| `lmapVecs` | tris.c / triGroupRecord_s | Stores lmap vecs in triGroupRecord_s (float lmapVecs[2][4]). |
| `removed` | tris.c / triGroupRecord_s | Stores removed in triGroupRecord_s (qboolean removed). |
| `shaderInfo` | tris.c / triGroupRecord_s | Stores shader info in triGroupRecord_s (triShaderInfo_t *shaderInfo). |
| `texVecs` | tris.c / triGroupRecord_s | Stores tex vecs in triGroupRecord_s (float texVecs[2][4]). |
| `vertIdx` | tris.c / triGroupRecord_s | Stores vert idx in triGroupRecord_s (int vertIdx[3]). |
| `color` | tris.c / triIntermediateVert_s | Stores color in triIntermediateVert_s (byte color[4]). |
| `hashNext` | tris.c / triIntermediateVert_s | Stores hash next in triIntermediateVert_s (int hashNext). |
| `lightmap` | tris.c / triIntermediateVert_s | Stores lightmap in triIntermediateVert_s (float lightmap[2]). |
| `normal` | tris.c / triIntermediateVert_s | Stores normal in triIntermediateVert_s (vec3_t normal). |
| `originalPos` | tris.c / triIntermediateVert_s | Stores original pos in triIntermediateVert_s (vec3_t originalPos). |
| `smoothAngle` | tris.c / triIntermediateVert_s | Stores smooth angle in triIntermediateVert_s (float smoothAngle). |
| `smoothNormal` | tris.c / triIntermediateVert_s | Stores smooth normal in triIntermediateVert_s (vec3_t smoothNormal). |
| `st` | tris.c / triIntermediateVert_s | Stores st in triIntermediateVert_s (float st[2]). |
| `xyz` | tris.c / triIntermediateVert_s | Stores xyz in triIntermediateVert_s (vec3_t xyz). |
| `firstTri` | tris.c / triSubgroup_s | Stores first tri in triSubgroup_s (int firstTri, triCount). |
| `maxs` | tris.c / triSubgroup_s | Stores maxs in triSubgroup_s (vec3_t mins, maxs). |
| `mins` | tris.c / triSubgroup_s | Stores mins in triSubgroup_s (vec3_t mins, maxs). |
| `triCount` | tris.c / triSubgroup_s | Stores tri count in triSubgroup_s (int firstTri, triCount). |
| `colorVecs` | tris.c / triSurfProps_s | Stores color vecs in triSurfProps_s (float colorVecs[4][4]). |
| `hashNext` | tris.c / triSurfProps_s | Stores hash next in triSurfProps_s (struct triSurfProps_s *hashNext). |
| `lightStyle` | tris.c / triSurfProps_s | Stores light style in triSurfProps_s (int lightStyle). |
| `lmapVecs` | tris.c / triSurfProps_s | Stores lmap vecs in triSurfProps_s (float lmapVecs[2][4]). |
| `plane` | tris.c / triSurfProps_s | Stores plane in triSurfProps_s (vec4_t plane). |
| `shaderInfo` | tris.c / triSurfProps_s | Stores shader info in triSurfProps_s (triShaderInfo_t *shaderInfo). |
| `smoothAngle` | tris.c / triSurfProps_s | Stores smooth angle in triSurfProps_s (float smoothAngle). |
| `texVecs` | tris.c / triSurfProps_s | Stores tex vecs in triSurfProps_s (float texVecs[2][4]). |
| `marked` | tris.c / triSurf_s | Stores marked in triSurf_s (qboolean marked). |
| `maxs` | tris.c / triSurf_s | Stores maxs in triSurf_s (vec3_t maxs). |
| `mins` | tris.c / triSurf_s | Stores mins in triSurf_s (vec3_t mins). |
| `next` | tris.c / triSurf_s | Stores next in triSurf_s (struct triSurf_s *next). |
| `originalWinding` | tris.c / triSurf_s | Stores original winding in triSurf_s (winding_t *originalWinding). |
| `props` | tris.c / triSurf_s | Stores props in triSurf_s (triSurfProps_t *props). |
| `winding` | tris.c / triSurf_s | Stores winding in triSurf_s (winding_t *winding). |
| `compatible` | tris.c / triangleEdge_s | Stores compatible in triangleEdge_s (byte compatible). |
| `hashNext` | tris.c / triangleEdge_s | Stores hash next in triangleEdge_s (int hashNext). |
| `lengthSquared` | tris.c / triangleEdge_s | Stores length squared in triangleEdge_s (float lengthSquared). |
| `nonmanifold` | tris.c / triangleEdge_s | Stores nonmanifold in triangleEdge_s (byte nonmanifold). |
| `removed` | tris.c / triangleEdge_s | Stores removed in triangleEdge_s (byte removed). |
| `triangle` | tris.c / triangleEdge_s | Stores triangle in triangleEdge_s (int triangle[2]). |
| `vertex` | tris.c / triangleEdge_s | Stores vertex in triangleEdge_s (int vertex[2]). |
| `indices` | tristrip.h / triangleIndexGroup_s | Stores indices in triangleIndexGroup_s (unsigned short *indices). |
| `numIndices` | tristrip.h / triangleIndexGroup_s | Stores num indices in triangleIndexGroup_s (unsigned int numIndices). |
| `merged` | vis.h / leaf_s | Stores merged in leaf_s (int merged). |
| `numportals` | vis.h / leaf_s | Stores numportals in leaf_s (int numportals). |
| `portals` | vis.h / leaf_s | Stores portals in leaf_s (vportal_t *portals[MAX_PORTALS_ON_LEAF]). |
| `cansee` | vis.h / passage_s | Stores cansee in passage_s (byte cansee[1]). |
| `next` | vis.h / passage_s | Stores next in passage_s (struct passage_s *next). |
| `dist` | vis.h / plane_t | Stores dist in plane_t (float dist). |
| `normal` | vis.h / plane_t | Stores normal in plane_t (vec3_t normal). |
| `depth` | vis.h / pstack_s | Stores depth in pstack_s (int depth). |
| `freewindings` | vis.h / pstack_s | Stores freewindings in pstack_s (int freewindings[3]). |
| `leaf` | vis.h / pstack_s | Stores leaf in pstack_s (leaf_t *leaf). |
| `mightsee` | vis.h / pstack_s | Stores mightsee in pstack_s (byte mightsee[MAX_PORTALS/8]). |
| `next` | vis.h / pstack_s | Stores next in pstack_s (struct pstack_s *next). |
| `numseperators` | vis.h / pstack_s | Stores numseperators in pstack_s (int numseperators[2]). |
| `pass` | vis.h / pstack_s | Stores pass in pstack_s (winding_t *pass). |
| `portal` | vis.h / pstack_s | Stores portal in pstack_s (vportal_t *portal). |
| `portalplane` | vis.h / pstack_s | Stores portalplane in pstack_s (plane_t portalplane). |
| `seperators` | vis.h / pstack_s | Stores seperators in pstack_s (#ifdef SEPERATORCACHE plane_t seperators[2][MAX_SEPERATORS]). |
| `source` | vis.h / pstack_s | Stores source in pstack_s (winding_t *source). |
| `windings` | vis.h / pstack_s | Stores windings in pstack_s (winding_t windings[3]). |
| `base` | vis.h / threaddata_t | Stores base in threaddata_t (vportal_t *base). |
| `c_chains` | vis.h / threaddata_t | Stores c chains in threaddata_t (int c_chains). |
| `pstack_head` | vis.h / threaddata_t | Stores pstack head in threaddata_t (pstack_t pstack_head). |
| `hint` | vis.h / vportal_t | Stores hint in vportal_t (qboolean hint). |
| `leaf` | vis.h / vportal_t | Stores leaf in vportal_t (int leaf). |
| `num` | vis.h / vportal_t | Stores num in vportal_t (int num). |
| `nummightsee` | vis.h / vportal_t | Stores nummightsee in vportal_t (int nummightsee). |
| `origin` | vis.h / vportal_t | Stores origin in vportal_t (vec3_t origin). |
| `passages` | vis.h / vportal_t | Stores passages in vportal_t (passage_t *passages). |
| `plane` | vis.h / vportal_t | Stores plane in vportal_t (plane_t plane). |
| `portalflood` | vis.h / vportal_t | Stores portalflood in vportal_t (byte *portalflood). |
| `portalfront` | vis.h / vportal_t | Stores portalfront in vportal_t (byte *portalfront). |
| `portalvis` | vis.h / vportal_t | Stores portalvis in vportal_t (byte *portalvis). |
| `radius` | vis.h / vportal_t | Stores radius in vportal_t (float radius). |
| `removed` | vis.h / vportal_t | Stores removed in vportal_t (qboolean removed). |
| `status` | vis.h / vportal_t | Stores status in vportal_t (vstatus_t status). |
| `winding` | vis.h / vportal_t | Stores winding in vportal_t (winding_t *winding). |
| `numpoints` | vis.h / winding_t | Stores numpoints in winding_t (int numpoints). |
| `points` | vis.h / winding_t | Stores points in winding_t (vec3_t points[MAX_POINTS_ON_FIXED_WINDING]). |

## Functions

| Name | Module / record | Reason |
| --- | --- | --- |
| `AllocBrush` | brush.c | Describes alloc brush in this module; chosen for the recovered behavior. |
| `AllocNode` | brush.c | Describes alloc node in this module; chosen for the recovered behavior. |
| `AllocTree` | brush.c | Describes alloc tree in this module; chosen for the recovered behavior. |
| `BoundBrush` | brush.c | Describes bound brush in this module; chosen for the recovered behavior. |
| `BrushFromBounds` | brush.c | Describes brush from bounds in this module; chosen for the recovered behavior. |
| `BrushMostlyOnSide` | brush.c | Describes brush mostly on side in this module; chosen for the recovered behavior. |
| `BrushVolume` | brush.c | Describes brush volume in this module; chosen for the recovered behavior. |
| `CopyBrush` | brush.c | Describes copy brush in this module; chosen for the recovered behavior. |
| `CountBrushList` | brush.c | Describes count brush list in this module; chosen for the recovered behavior. |
| `CreateBrushWindings` | brush.c | Describes create brush windings in this module; chosen for the recovered behavior. |
| `DrawBrushList` | brush.c | Describes draw brush list in this module; chosen for the recovered behavior. |
| `FilterBrushIntoTree_r` | brush.c | Describes filter brush into tree r in this module; chosen for the recovered behavior. |
| `FilterDetailBrushesIntoTree` | brush.c | Describes filter detail brushes into tree in this module; chosen for the recovered behavior. |
| `FilterStructuralBrushesIntoTree` | brush.c | Describes filter structural brushes into tree in this module; chosen for the recovered behavior. |
| `FreeBrush` | brush.c | Describes free brush in this module; chosen for the recovered behavior. |
| `FreeBrushList` | brush.c | Describes free brush list in this module; chosen for the recovered behavior. |
| `PrintBrush` | brush.c | Describes print brush in this module; chosen for the recovered behavior. |
| `SplitBrush` | brush.c | Describes split brush in this module; chosen for the recovered behavior. |
| `WindingIsHuge` | brush.c | Describes winding is huge in this module; chosen for the recovered behavior. |
| `WindingIsTiny` | brush.c | Describes winding is tiny in this module; chosen for the recovered behavior. |
| `WriteBrushList` | brush.c | Describes write brush list in this module; chosen for the recovered behavior. |
| `WriteBspBrushMap` | brush.c | Describes write bsp brush map in this module; chosen for the recovered behavior. |
| `ComputeAxisBase` | brush_primit.c | Describes compute axis base in this module; chosen for the recovered behavior. |
| `Bspinfo` | bsp.c | Describes bspinfo in this module; chosen for the recovered behavior. |
| `Com_DPrintf` | bsp.c | Describes com dprintf in this module; chosen for the recovered behavior. |
| `Com_Error` | bsp.c | Describes com error in this module; chosen for the recovered behavior. |
| `Com_Printf` | bsp.c | Describes com printf in this module; chosen for the recovered behavior. |
| `InitQ3MapFileSystem` | bsp.c | Describes init q3 map file system in this module; chosen for the recovered behavior. |
| `OnlyEnts` | bsp.c | Describes only ents in this module; chosen for the recovered behavior. |
| `OnlyTextures` | bsp.c | Describes only textures in this module; chosen for the recovered behavior. |
| `ParseSmoothAngle` | bsp.c | Describes parse smooth angle in this module; chosen for the recovered behavior. |
| `ProcessModels` | bsp.c | Describes process models in this module; chosen for the recovered behavior. |
| `ProcessSubModel` | bsp.c | Describes process sub model in this module; chosen for the recovered behavior. |
| `ProcessWorldModel` | bsp.c | Describes process world model in this module; chosen for the recovered behavior. |
| `Q3MapFatalError` | bsp.c | Describes q3 map fatal error in this module; chosen for the recovered behavior. |
| `SetQ3MapErrorHandler` | bsp.c | Describes set q3 map error handler in this module; chosen for the recovered behavior. |
| `main` | bsp.c | Describes main in this module; chosen for the recovered behavior. |
| `AllocBspFace` | facebsp.c | Describes alloc bsp face in this module; chosen for the recovered behavior. |
| `BspFaceForPortal` | facebsp.c | Describes bsp face for portal in this module; chosen for the recovered behavior. |
| `BuildFaceTree_r` | facebsp.c | Describes build face tree r in this module; chosen for the recovered behavior. |
| `CountFaceList` | facebsp.c | Describes count face list in this module; chosen for the recovered behavior. |
| `FaceBSP` | facebsp.c | Describes face bsp in this module; chosen for the recovered behavior. |
| `FreeBspFace` | facebsp.c | Describes free bsp face in this module; chosen for the recovered behavior. |
| `MakeStructuralBspFaceList` | facebsp.c | Describes make structural bsp face list in this module; chosen for the recovered behavior. |
| `MakeVisibleBspFaceList` | facebsp.c | Describes make visible bsp face list in this module; chosen for the recovered behavior. |
| `SelectSplitPlaneNum` | facebsp.c | Describes select split plane num in this module; chosen for the recovered behavior. |
| `ChopFaceByBrush` | fog.c | Describes chop face by brush in this module; chosen for the recovered behavior. |
| `ChopPatchByBrush` | fog.c | Describes chop patch by brush in this module; chosen for the recovered behavior. |
| `DrawSurfToMesh` | fog.c | Describes draw surf to mesh in this module; chosen for the recovered behavior. |
| `SplitMeshByPlane` | fog.c | Describes split mesh by plane in this module; chosen for the recovered behavior. |
| `WindingFromDrawSurf` | fog.c | Describes winding from draw surf in this module; chosen for the recovered behavior. |
| `DrawAuxWinding` | gldraw.c | Describes draw aux winding in this module; chosen for the recovered behavior. |
| `DrawWinding` | gldraw.c | Describes draw winding in this module; chosen for the recovered behavior. |
| `Draw_ClearWindow` | gldraw.c | Describes draw clear window in this module; chosen for the recovered behavior. |
| `Draw_SetBlack` | gldraw.c | Describes draw set black in this module; chosen for the recovered behavior. |
| `Draw_SetGrey` | gldraw.c | Describes draw set grey in this module; chosen for the recovered behavior. |
| `Draw_SetRed` | gldraw.c | Describes draw set red in this module; chosen for the recovered behavior. |
| `GLS_BeginScene` | gldraw.c | Describes gls begin scene in this module; chosen for the recovered behavior. |
| `GLS_EndScene` | gldraw.c | Describes gls end scene in this module; chosen for the recovered behavior. |
| `GLS_Winding` | gldraw.c | Describes gls winding in this module; chosen for the recovered behavior. |
| `InitWindow` | gldraw.c | Describes init window in this module; chosen for the recovered behavior. |
| `OutputPortal` | glfile.c | Describes output portal in this module; chosen for the recovered behavior. |
| `OutputWinding` | glfile.c | Describes output winding in this module; chosen for the recovered behavior. |
| `PortalVisibleSides` | glfile.c | Describes portal visible sides in this module; chosen for the recovered behavior. |
| `WriteGLView` | glfile.c | Describes write glview in this module; chosen for the recovered behavior. |
| `WriteGLView_r` | glfile.c | Describes write glview r in this module; chosen for the recovered behavior. |
| `LeakFile` | leakfile.c | Describes leak file in this module; chosen for the recovered behavior. |
| `LeakFileBetweenNodes` | leakfile.c | Describes leak file between nodes in this module; chosen for the recovered behavior. |
| `RecursiveLeakFileBetweenNodes` | leakfile.c | Describes recursive leak file between nodes in this module; chosen for the recovered behavior. |
| `AddLightmapToCurrentMaterial` | lightmaps.c | Describes add lightmap to current material in this module; chosen for the recovered behavior. |
| `AddSurfaceToLightmapGroups` | lightmaps.c | Describes add surface to lightmap groups in this module; chosen for the recovered behavior. |
| `AddSurfaceToOverlapGrid` | lightmaps.c | Describes add surface to overlap grid in this module; chosen for the recovered behavior. |
| `AllocBestFitBlock` | lightmaps.c | Describes alloc best fit block in this module; chosen for the recovered behavior. |
| `AllocLightmapBlock` | lightmaps.c | Describes alloc lightmap block in this module; chosen for the recovered behavior. |
| `AllocLightmapRectangle` | lightmaps.c | Describes alloc lightmap rectangle in this module; chosen for the recovered behavior. |
| `AllocateLightmapForPatch` | lightmaps.c | Describes allocate lightmap for patch in this module; chosen for the recovered behavior. |
| `AllocateLightmapForSurface` | lightmaps.c | Describes allocate lightmap for surface in this module; chosen for the recovered behavior. |
| `AllocateLightmapForTriangleSoup` | lightmaps.c | Describes allocate lightmap for triangle soup in this module; chosen for the recovered behavior. |
| `AllocateLightmaps` | lightmaps.c | Describes allocate lightmaps in this module; chosen for the recovered behavior. |
| `AllocateSharedLightmap` | lightmaps.c | Describes allocate shared lightmap in this module; chosen for the recovered behavior. |
| `AttachIsolatedLightmapGroups` | lightmaps.c | Describes attach isolated lightmap groups in this module; chosen for the recovered behavior. |
| `BuildLightmapCompatibilityGrid` | lightmaps.c | Describes build lightmap compatibility grid in this module; chosen for the recovered behavior. |
| `BuildLightmapGroups` | lightmaps.c | Describes build lightmap groups in this module; chosen for the recovered behavior. |
| `ClipLightmapPolygon` | lightmaps.c | Describes clip lightmap polygon in this module; chosen for the recovered behavior. |
| `ColorLightmapBlock` | lightmaps.c | Describes color lightmap block in this module; chosen for the recovered behavior. |
| `CompareLightmapSurfaces` | lightmaps.c | Describes compare lightmap surfaces in this module; chosen for the recovered behavior. |
| `CompareMaterialGroupsByArea` | lightmaps.c | Describes compare material groups by area in this module; chosen for the recovered behavior. |
| `ComputePatchLightmapSize` | lightmaps.c | Describes compute patch lightmap size in this module; chosen for the recovered behavior. |
| `CountAndFreeMaterialLightmaps` | lightmaps.c | Describes count and free material lightmaps in this module; chosen for the recovered behavior. |
| `FinalizeLightmapVectors` | lightmaps.c | Describes finalize lightmap vectors in this module; chosen for the recovered behavior. |
| `FitLightmapCoordinate` | lightmaps.c | Describes fit lightmap coordinate in this module; chosen for the recovered behavior. |
| `FreeLightmapBlock` | lightmaps.c | Describes free lightmap block in this module; chosen for the recovered behavior. |
| `LightmapAxisForSurface` | lightmaps.c | Describes lightmap axis for surface in this module; chosen for the recovered behavior. |
| `LightmapGroupBounds` | lightmaps.c | Describes lightmap group bounds in this module; chosen for the recovered behavior. |
| `LightmapGroupSurfacesShareVertex` | lightmaps.c | Describes lightmap group surfaces share vertex in this module; chosen for the recovered behavior. |
| `LightmapGroupsCompatible` | lightmaps.c | Describes lightmap groups compatible in this module; chosen for the recovered behavior. |
| `LightmapGroupsShareVertex` | lightmaps.c | Describes lightmap groups share vertex in this module; chosen for the recovered behavior. |
| `LightmapPolygonAreaAndCentroid` | lightmaps.c | Describes lightmap polygon area and centroid in this module; chosen for the recovered behavior. |
| `LightmapSurfaceBounds` | lightmaps.c | Describes lightmap surface bounds in this module; chosen for the recovered behavior. |
| `LightmapSurfaceBoundsSeparate` | lightmaps.c | Describes lightmap surface bounds separate in this module; chosen for the recovered behavior. |
| `MergeCompatibleLightmapGroups` | lightmaps.c | Describes merge compatible lightmap groups in this module; chosen for the recovered behavior. |
| `MergeCompatibleSurfaceBatch` | lightmaps.c | Describes merge compatible surface batch in this module; chosen for the recovered behavior. |
| `MergeLightmapBlock` | lightmaps.c | Describes merge lightmap block in this module; chosen for the recovered behavior. |
| `MergeOneCompatibleLightmapGroup` | lightmaps.c | Describes merge one compatible lightmap group in this module; chosen for the recovered behavior. |
| `MergeSortLightmapSurfaces` | lightmaps.c | Describes merge sort lightmap surfaces in this module; chosen for the recovered behavior. |
| `PrepareNewLightmap` | lightmaps.c | Describes prepare new lightmap in this module; chosen for the recovered behavior. |
| `ProjectSurfaceLightmap` | lightmaps.c | Describes project surface lightmap in this module; chosen for the recovered behavior. |
| `RoundLightmapBounds` | lightmaps.c | Describes round lightmap bounds in this module; chosen for the recovered behavior. |
| `RoundLightmapCoordinate` | lightmaps.c | Describes round lightmap coordinate in this module; chosen for the recovered behavior. |
| `ScanConvertLightmapPolygon` | lightmaps.c | Describes scan convert lightmap polygon in this module; chosen for the recovered behavior. |
| `ScanLightmapSurface` | lightmaps.c | Describes scan lightmap surface in this module; chosen for the recovered behavior. |
| `SetupLightmapGroupSurfaceBounds` | lightmaps.c | Describes setup lightmap group surface bounds in this module; chosen for the recovered behavior. |
| `SplitInvalidLightmapGroup` | lightmaps.c | Describes split invalid lightmap group in this module; chosen for the recovered behavior. |
| `SplitInvalidLightmapGroups` | lightmaps.c | Describes split invalid lightmap groups in this module; chosen for the recovered behavior. |
| `SplitLightmapBlock` | lightmaps.c | Describes split lightmap block in this module; chosen for the recovered behavior. |
| `SurfaceLightmapSampleSize` | lightmaps.c | Describes surface lightmap sample size in this module; chosen for the recovered behavior. |
| `AddBackSides` | map.c | Describes add back sides in this module; chosen for the recovered behavior. |
| `AddBrushBevels` | map.c | Describes add brush bevels in this module; chosen for the recovered behavior. |
| `AddPlaneToHash` | map.c | Describes add plane to hash in this module; chosen for the recovered behavior. |
| `AdjustBrushesForOrigin` | map.c | Describes adjust brushes for origin in this module; chosen for the recovered behavior. |
| `CreateNewFloatPlane` | map.c | Describes create new float plane in this module; chosen for the recovered behavior. |
| `FindFloatPlane` | map.c | Describes find float plane in this module; chosen for the recovered behavior. |
| `FinishBrush` | map.c | Describes finish brush in this module; chosen for the recovered behavior. |
| `LoadMapFile` | map.c | Describes load map file in this module; chosen for the recovered behavior. |
| `LoadModelCollMap` | map.c | Describes load model coll map in this module; chosen for the recovered behavior. |
| `MapPlaneFromPoints` | map.c | Describes map plane from points in this module; chosen for the recovered behavior. |
| `MoveBrushesToWorld` | map.c | Describes move brushes to world in this module; chosen for the recovered behavior. |
| `ParseBrush` | map.c | Describes parse brush in this module; chosen for the recovered behavior. |
| `ParseCollMapEntity` | map.c | Describes parse coll map entity in this module; chosen for the recovered behavior. |
| `ParseMapEntity` | map.c | Describes parse map entity in this module; chosen for the recovered behavior. |
| `ParseRawBrush` | map.c | Describes parse raw brush in this module; chosen for the recovered behavior. |
| `ParseVehicleCollMap` | map.c | Describes parse vehicle coll map in this module; chosen for the recovered behavior. |
| `PlaneEqual` | map.c | Describes plane equal in this module; chosen for the recovered behavior. |
| `ProcessMapModels` | map.c | Describes process map models in this module; chosen for the recovered behavior. |
| `ProcessVehicleCollisionMaps` | map.c | Describes process vehicle collision maps in this module; chosen for the recovered behavior. |
| `QuakeTextureVecs` | map.c | Describes quake texture vecs in this module; chosen for the recovered behavior. |
| `RemoveDuplicateBrushPlanes` | map.c | Describes remove duplicate brush planes in this module; chosen for the recovered behavior. |
| `SetBrushContents` | map.c | Describes set brush contents in this module; chosen for the recovered behavior. |
| `SnapPlane` | map.c | Describes snap plane in this module; chosen for the recovered behavior. |
| `SnapVector` | map.c | Describes snap vector in this module; chosen for the recovered behavior. |
| `TestExpandBrushes` | map.c | Describes test expand brushes in this module; chosen for the recovered behavior. |
| `TextureAxisFromPlane` | map.c | Describes texture axis from plane in this module; chosen for the recovered behavior. |
| `CopyMesh` | mesh.c | Describes copy mesh in this module; chosen for the recovered behavior. |
| `FreeMesh` | mesh.c | Describes free mesh in this module; chosen for the recovered behavior. |
| `GuessMeshPlane` | mesh.c | Describes guess mesh plane in this module; chosen for the recovered behavior. |
| `InvertMesh` | mesh.c | Describes invert mesh in this module; chosen for the recovered behavior. |
| `LerpDrawVert` | mesh.c | Describes lerp draw vert in this module; chosen for the recovered behavior. |
| `LerpDrawVertAmount` | mesh.c | Describes lerp draw vert amount in this module; chosen for the recovered behavior. |
| `MakeMeshNormals` | mesh.c | Describes make mesh normals in this module; chosen for the recovered behavior. |
| `PrintMesh` | mesh.c | Describes print mesh in this module; chosen for the recovered behavior. |
| `PutMeshOnCurve` | mesh.c | Describes put mesh on curve in this module; chosen for the recovered behavior. |
| `RemoveLinearMeshColumnsRows` | mesh.c | Describes remove linear mesh columns rows in this module; chosen for the recovered behavior. |
| `SubdivideMesh` | mesh.c | Describes subdivide mesh in this module; chosen for the recovered behavior. |
| `SubdivideMeshQuads` | mesh.c | Describes subdivide mesh quads in this module; chosen for the recovered behavior. |
| `TransposeMesh` | mesh.c | Describes transpose mesh in this module; chosen for the recovered behavior. |
| `AddPatchTriangle` | patch.c | Describes add patch triangle in this module; chosen for the recovered behavior. |
| `AllocStackOrHeap` | patch.c | Describes alloc stack or heap in this module; chosen for the recovered behavior. |
| `DrawSurfaceForMesh` | patch.c | Describes draw surface for mesh in this module; chosen for the recovered behavior. |
| `DrawSurfaceForTerrain` | patch.c | Describes draw surface for terrain in this module; chosen for the recovered behavior. |
| `EmitTerrainPatchGroup` | patch.c | Describes emit terrain patch group in this module; chosen for the recovered behavior. |
| `FindPatchDrawVert` | patch.c | Describes find patch draw vert in this module; chosen for the recovered behavior. |
| `FreeStackOrHeap` | patch.c | Describes free stack or heap in this module; chosen for the recovered behavior. |
| `GrowGroup_r` | patch.c | Describes grow group r in this module; chosen for the recovered behavior. |
| `GuessPatchProjectionAxis` | patch.c | Describes guess patch projection axis in this module; chosen for the recovered behavior. |
| `MarkPatchNormalAxes` | patch.c | Describes mark patch normal axes in this module; chosen for the recovered behavior. |
| `ParsePatch` | patch.c | Describes parse patch in this module; chosen for the recovered behavior. |
| `PatchGroupCompare` | patch.c | Describes patch group compare in this module; chosen for the recovered behavior. |
| `PatchMapDrawSurfs` | patch.c | Describes patch map draw surfs in this module; chosen for the recovered behavior. |
| `PrintCtrl` | patch.c | Describes print ctrl in this module; chosen for the recovered behavior. |
| `ProcessTerrainPatches` | patch.c | Describes process terrain patches in this module; chosen for the recovered behavior. |
| `RecenterPatchTexCoords` | patch.c | Describes recenter patch tex coords in this module; chosen for the recovered behavior. |
| `SubdivideTerrain` | patch.c | Describes subdivide terrain in this module; chosen for the recovered behavior. |
| `TriangulatePatch` | patch.c | Describes triangulate patch in this module; chosen for the recovered behavior. |
| `AddLeafCellPortals_r` | portals.c | Describes add leaf cell portals r in this module; chosen for the recovered behavior. |
| `AddOccluderEdge` | portals.c | Describes add occluder edge in this module; chosen for the recovered behavior. |
| `AddPortalToNodes` | portals.c | Describes add portal to nodes in this module; chosen for the recovered behavior. |
| `AllocPortal` | portals.c | Describes alloc portal in this module; chosen for the recovered behavior. |
| `AssignBspCells` | portals.c | Describes assign bsp cells in this module; chosen for the recovered behavior. |
| `AssignPortalBrushSide_r` | portals.c | Describes assign portal brush side r in this module; chosen for the recovered behavior. |
| `AssignPortalBrushSides` | portals.c | Describes assign portal brush sides in this module; chosen for the recovered behavior. |
| `BaseWindingForNode` | portals.c | Describes base winding for node in this module; chosen for the recovered behavior. |
| `BuildPortalsAndCells` | portals.c | Describes build portals and cells in this module; chosen for the recovered behavior. |
| `CalcNodeBounds` | portals.c | Describes calc node bounds in this module; chosen for the recovered behavior. |
| `CellPortalPlaneForLeaf` | portals.c | Describes cell portal plane for leaf in this module; chosen for the recovered behavior. |
| `CheckAreas_r` | portals.c | Describes check areas r in this module; chosen for the recovered behavior. |
| `EmitCellPortals` | portals.c | Describes emit cell portals in this module; chosen for the recovered behavior. |
| `EmitCellPortalsAndOccluders` | portals.c | Describes emit cell portals and occluders in this module; chosen for the recovered behavior. |
| `EmitOccluders` | portals.c | Describes emit occluders in this module; chosen for the recovered behavior. |
| `FillOutside` | portals.c | Describes fill outside in this module; chosen for the recovered behavior. |
| `FillOutside_r` | portals.c | Describes fill outside r in this module; chosen for the recovered behavior. |
| `FindAreas_r` | portals.c | Describes find areas r in this module; chosen for the recovered behavior. |
| `FloodAreas` | portals.c | Describes flood areas in this module; chosen for the recovered behavior. |
| `FloodAreas_r` | portals.c | Describes flood areas r in this module; chosen for the recovered behavior. |
| `FloodCell_r` | portals.c | Describes flood cell r in this module; chosen for the recovered behavior. |
| `FloodClassnameExcluded` | portals.c | Describes flood classname excluded in this module; chosen for the recovered behavior. |
| `FloodEntities` | portals.c | Describes flood entities in this module; chosen for the recovered behavior. |
| `FloodOutsideCells_r` | portals.c | Describes flood outside cells r in this module; chosen for the recovered behavior. |
| `FloodPortals_r` | portals.c | Describes flood portals r in this module; chosen for the recovered behavior. |
| `FreePortal` | portals.c | Describes free portal in this module; chosen for the recovered behavior. |
| `IgnoreSameCellPortals_r` | portals.c | Describes ignore same cell portals r in this module; chosen for the recovered behavior. |
| `InitNodeCells_r` | portals.c | Describes init node cells r in this module; chosen for the recovered behavior. |
| `LeafBoundaryPlaneOrientation` | portals.c | Describes leaf boundary plane orientation in this module; chosen for the recovered behavior. |
| `MakeHeadnodePortals` | portals.c | Describes make headnode portals in this module; chosen for the recovered behavior. |
| `MakeNodePortal` | portals.c | Describes make node portal in this module; chosen for the recovered behavior. |
| `MakeTreePortals` | portals.c | Describes make tree portals in this module; chosen for the recovered behavior. |
| `MakeTreePortals_r` | portals.c | Describes make tree portals r in this module; chosen for the recovered behavior. |
| `PlaceOccupant` | portals.c | Describes place occupant in this module; chosen for the recovered behavior. |
| `PointBehindPlanes` | portals.c | Describes point behind planes in this module; chosen for the recovered behavior. |
| `Portal_Passable` | portals.c | Describes portal passable in this module; chosen for the recovered behavior. |
| `PortalizeNode` | portals.c | Describes portalize node in this module; chosen for the recovered behavior. |
| `PrintPortal` | portals.c | Describes print portal in this module; chosen for the recovered behavior. |
| `PrintPortalWarning` | portals.c | Describes print portal warning in this module; chosen for the recovered behavior. |
| `PropagateNodeCells_r` | portals.c | Describes propagate node cells r in this module; chosen for the recovered behavior. |
| `RemapOccluderPlanes` | portals.c | Describes remap occluder planes in this module; chosen for the recovered behavior. |
| `RemapPortalPlanes` | portals.c | Describes remap portal planes in this module; chosen for the recovered behavior. |
| `RemovePortalFromNode` | portals.c | Describes remove portal from node in this module; chosen for the recovered behavior. |
| `SplitNodePortals` | portals.c | Describes split node portals in this module; chosen for the recovered behavior. |
| `NumberClusters` | prtfile.c | Describes number clusters in this module; chosen for the recovered behavior. |
| `NumberLeafs_r` | prtfile.c | Describes number leafs r in this module; chosen for the recovered behavior. |
| `WriteFaceFile_r` | prtfile.c | Describes write face file r in this module; chosen for the recovered behavior. |
| `WriteFloat` | prtfile.c | Describes write float in this module; chosen for the recovered behavior. |
| `WritePortalFile` | prtfile.c | Describes write portal file in this module; chosen for the recovered behavior. |
| `WritePortalFile_r` | prtfile.c | Describes write portal file r in this module; chosen for the recovered behavior. |
| `AllocShaderInfo` | shaders.c | Describes alloc shader info in this module; chosen for the recovered behavior. |
| `LoadShaderImage` | shaders.c | Describes load shader image in this module; chosen for the recovered behavior. |
| `LoadShaderImageFile` | shaders.c | Describes load shader image file in this module; chosen for the recovered behavior. |
| `LoadShaderInfo` | shaders.c | Describes load shader info in this module; chosen for the recovered behavior. |
| `ParseShader` | shaders.c | Describes parse shader in this module; chosen for the recovered behavior. |
| `ParseShaderFile` | shaders.c | Describes parse shader file in this module; chosen for the recovered behavior. |
| `ParseShaderTypeFile` | shaders.c | Describes parse shader type file in this module; chosen for the recovered behavior. |
| `ShaderInfoForShader` | shaders.c | Describes shader info for shader in this module; chosen for the recovered behavior. |
| `AddSideRef` | surface.c | Describes add side ref in this module; chosen for the recovered behavior. |
| `AllocDrawSurf` | surface.c | Describes alloc draw surf in this module; chosen for the recovered behavior. |
| `ClipSideIntoTree_r` | surface.c | Describes clip side into tree r in this module; chosen for the recovered behavior. |
| `ClipSidesIntoTree` | surface.c | Describes clip sides into tree in this module; chosen for the recovered behavior. |
| `ClosePolyFile` | surface.c | Describes close poly file in this module; chosen for the recovered behavior. |
| `DrawSurfaceForSide` | surface.c | Describes draw surface for side in this module; chosen for the recovered behavior. |
| `EmitPatchCollide` | surface.c | Describes emit patch collide in this module; chosen for the recovered behavior. |
| `EmitTerrainCollide` | surface.c | Describes emit terrain collide in this module; chosen for the recovered behavior. |
| `FilterCollisionSurfsIntoTree` | surface.c | Describes filter collision surfs into tree in this module; chosen for the recovered behavior. |
| `FilterMapDrawSurfIntoTree` | surface.c | Describes filter map draw surf into tree in this module; chosen for the recovered behavior. |
| `FilterMapDrawSurfIntoTree_r` | surface.c | Describes filter map draw surf into tree r in this module; chosen for the recovered behavior. |
| `FilterPatchSurfIntoTree` | surface.c | Describes filter patch surf into tree in this module; chosen for the recovered behavior. |
| `FilterSideIntoTree_r` | surface.c | Describes filter side into tree r in this module; chosen for the recovered behavior. |
| `FilterTriangleSoupIntoTree` | surface.c | Describes filter triangle soup into tree in this module; chosen for the recovered behavior. |
| `MergeSides` | surface.c | Describes merge sides in this module; chosen for the recovered behavior. |
| `OpenPolyFile` | surface.c | Describes open poly file in this module; chosen for the recovered behavior. |
| `SubdivideDrawSurf` | surface.c | Describes subdivide draw surf in this module; chosen for the recovered behavior. |
| `SubdivideDrawSurfs` | surface.c | Describes subdivide draw surfs in this module; chosen for the recovered behavior. |
| `WriteSideToPolyFile` | surface.c | Describes write side to poly file in this module; chosen for the recovered behavior. |
| `WriteTerrainSurfaceToPolyFile` | surface.c | Describes write terrain surface to poly file in this module; chosen for the recovered behavior. |
| `AddBrushSide` | terrain.c | Describes add brush side in this module; chosen for the recovered behavior. |
| `CalcTerrainSize` | terrain.c | Describes calc terrain size in this module; chosen for the recovered behavior. |
| `CompareVert` | terrain.c | Describes compare vert in this module; chosen for the recovered behavior. |
| `CreateTerrainSurface` | terrain.c | Describes create terrain surface in this module; chosen for the recovered behavior. |
| `EmitTerrainVerts` | terrain.c | Describes emit terrain verts in this module; chosen for the recovered behavior. |
| `EmitTerrainVerts2` | terrain.c | Describes emit terrain verts2 in this module; chosen for the recovered behavior. |
| `IsTriangleDegenerate` | terrain.c | Describes is triangle degenerate in this module; chosen for the recovered behavior. |
| `LayerForShader` | terrain.c | Describes layer for shader in this module; chosen for the recovered behavior. |
| `LoadAlphaMap` | terrain.c | Describes load alpha map in this module; chosen for the recovered behavior. |
| `MakeBrushFromTriangle` | terrain.c | Describes make brush from triangle in this module; chosen for the recovered behavior. |
| `MakeTerrainIntoBrushes` | terrain.c | Describes make terrain into brushes in this module; chosen for the recovered behavior. |
| `ParseTerrain` | terrain.c | Describes parse terrain in this module; chosen for the recovered behavior. |
| `SetTerrainTextures` | terrain.c | Describes set terrain textures in this module; chosen for the recovered behavior. |
| `ShaderForLayer` | terrain.c | Describes shader for layer in this module; chosen for the recovered behavior. |
| `SideAsTriFan` | terrain.c | Describes side as tri fan in this module; chosen for the recovered behavior. |
| `SideAsTristrip` | terrain.c | Describes side as tristrip in this module; chosen for the recovered behavior. |
| `SurfaceForShader` | terrain.c | Describes surface for shader in this module; chosen for the recovered behavior. |
| `Terrain_AddTexture` | terrain.c | Describes terrain add texture in this module; chosen for the recovered behavior. |
| `Terrain_GetTriangles` | terrain.c | Describes terrain get triangles in this module; chosen for the recovered behavior. |
| `Terrain_GetVert` | terrain.c | Describes terrain get vert in this module; chosen for the recovered behavior. |
| `Terrain_ParseFace` | terrain.c | Describes terrain parse face in this module; chosen for the recovered behavior. |
| `AddEdge` | tjunction.c | Describes add edge in this module; chosen for the recovered behavior. |
| `AddPatchEdges` | tjunction.c | Describes add patch edges in this module; chosen for the recovered behavior. |
| `AddSurfaceEdges` | tjunction.c | Describes add surface edges in this module; chosen for the recovered behavior. |
| `EdgeCompare` | tjunction.c | Describes edge compare in this module; chosen for the recovered behavior. |
| `FixSurfaceJunctions` | tjunction.c | Describes fix surface junctions in this module; chosen for the recovered behavior. |
| `FixTJunctions` | tjunction.c | Describes fix tjunctions in this module; chosen for the recovered behavior. |
| `InsertPointOnEdge` | tjunction.c | Describes insert point on edge in this module; chosen for the recovered behavior. |
| `FreeTree` | tree.c | Describes free tree in this module; chosen for the recovered behavior. |
| `FreeTreePortals_r` | tree.c | Describes free tree portals r in this module; chosen for the recovered behavior. |
| `FreeTree_r` | tree.c | Describes free tree r in this module; chosen for the recovered behavior. |
| `NodeForPoint` | tree.c | Describes node for point in this module; chosen for the recovered behavior. |
| `PrintTree_r` | tree.c | Describes print tree r in this module; chosen for the recovered behavior. |
| `AabbAddChildNodes` | tris.c | Describes aabb add child nodes in this module; chosen for the recovered behavior. |
| `AabbEnlargement` | tris.c | Describes aabb enlargement in this module; chosen for the recovered behavior. |
| `AabbSelectSplitPlane` | tris.c | Describes aabb select split plane in this module; chosen for the recovered behavior. |
| `AabbSplitItems` | tris.c | Describes aabb split items in this module; chosen for the recovered behavior. |
| `AabbSplitNode_r` | tris.c | Describes aabb split node r in this module; chosen for the recovered behavior. |
| `AddSoupVert` | tris.c | Describes add soup vert in this module; chosen for the recovered behavior. |
| `AddTriSurfToCell` | tris.c | Describes add tri surf to cell in this module; chosen for the recovered behavior. |
| `AddWindingWithoutOverlap_r` | tris.c | Describes add winding without overlap r in this module; chosen for the recovered behavior. |
| `AdjustTriangleUVs_r` | tris.c | Describes adjust triangle uvs r in this module; chosen for the recovered behavior. |
| `AlignNeighborUVs` | tris.c | Describes align neighbor uvs in this module; chosen for the recovered behavior. |
| `ApplyTriangleCollapse` | tris.c | Describes apply triangle collapse in this module; chosen for the recovered behavior. |
| `BoundsCoincideOnAxis` | tris.c | Describes bounds coincide on axis in this module; chosen for the recovered behavior. |
| `BuildSoupsAndAabbTrees` | tris.c | Describes build soups and aabb trees in this module; chosen for the recovered behavior. |
| `BuildTriSoupAABBTree` | tris.c | Describes build tri soup aabbtree in this module; chosen for the recovered behavior. |
| `BuildTriangleEdges` | tris.c | Describes build triangle edges in this module; chosen for the recovered behavior. |
| `BuildTriangleNeighbors` | tris.c | Describes build triangle neighbors in this module; chosen for the recovered behavior. |
| `BuildTriangleVertexRemap` | tris.c | Describes build triangle vertex remap in this module; chosen for the recovered behavior. |
| `CanSkipVertex` | tris.c | Describes can skip vertex in this module; chosen for the recovered behavior. |
| `CeilToInt` | tris.c | Describes ceil to int in this module; chosen for the recovered behavior. |
| `CheckCollapseAngles` | tris.c | Describes check collapse angles in this module; chosen for the recovered behavior. |
| `CheckTriangleUVCompatibility` | tris.c | Describes check triangle uvcompatibility in this module; chosen for the recovered behavior. |
| `CheckWindingSeparation` | tris.c | Describes check winding separation in this module; chosen for the recovered behavior. |
| `ClearTriSurfPropsHash` | tris.c | Describes clear tri surf props hash in this module; chosen for the recovered behavior. |
| `ClusterTriRecords` | tris.c | Describes cluster tri records in this module; chosen for the recovered behavior. |
| `CollapseCollinearVerts` | tris.c | Describes collapse collinear verts in this module; chosen for the recovered behavior. |
| `CollapseEdgesPass` | tris.c | Describes collapse edges pass in this module; chosen for the recovered behavior. |
| `CollectCollapseTriangles` | tris.c | Describes collect collapse triangles in this module; chosen for the recovered behavior. |
| `CompareFloats` | tris.c | Describes compare floats in this module; chosen for the recovered behavior. |
| `CompareSurfaces` | tris.c | Describes compare surfaces in this module; chosen for the recovered behavior. |
| `CompareTrisByGroupId` | tris.c | Describes compare tris by group id in this module; chosen for the recovered behavior. |
| `ComputeEdgeLine2D` | tris.c | Describes compute edge line2 d in this module; chosen for the recovered behavior. |
| `DeriveTextureVectors` | tris.c | Describes derive texture vectors in this module; chosen for the recovered behavior. |
| `DrawVertsEquivalent` | tris.c | Describes draw verts equivalent in this module; chosen for the recovered behavior. |
| `EdgeHashIndex` | tris.c | Describes edge hash index in this module; chosen for the recovered behavior. |
| `EdgesCross2D` | tris.c | Describes edges cross2 d in this module; chosen for the recovered behavior. |
| `EmitDrawSurfaces` | tris.c | Describes emit draw surfaces in this module; chosen for the recovered behavior. |
| `EmitSoupFromRecords` | tris.c | Describes emit soup from records in this module; chosen for the recovered behavior. |
| `EmitTriRecord` | tris.c | Describes emit tri record in this module; chosen for the recovered behavior. |
| `ExtractWindingArc` | tris.c | Describes extract winding arc in this module; chosen for the recovered behavior. |
| `FilterTriSurfIntoTree` | tris.c | Describes filter tri surf into tree in this module; chosen for the recovered behavior. |
| `FilterTriWindingIntoCells` | tris.c | Describes filter tri winding into cells in this module; chosen for the recovered behavior. |
| `FindOrAddTriVert` | tris.c | Describes find or add tri vert in this module; chosen for the recovered behavior. |
| `FindOrCreateTriSurfProps` | tris.c | Describes find or create tri surf props in this module; chosen for the recovered behavior. |
| `FindOrCreateTriangleEdge` | tris.c | Describes find or create triangle edge in this module; chosen for the recovered behavior. |
| `FindTriSurfCell` | tris.c | Describes find tri surf cell in this module; chosen for the recovered behavior. |
| `FixPinchedWinding` | tris.c | Describes fix pinched winding in this module; chosen for the recovered behavior. |
| `FixTriSurfaceTJunctions` | tris.c | Describes fix tri surface tjunctions in this module; chosen for the recovered behavior. |
| `FixWindingSelfTJunctions` | tris.c | Describes fix winding self tjunctions in this module; chosen for the recovered behavior. |
| `GenerateAllTriSurfVerts` | tris.c | Describes generate all tri surf verts in this module; chosen for the recovered behavior. |
| `GenerateWindingVerts` | tris.c | Describes generate winding verts in this module; chosen for the recovered behavior. |
| `HashVertexGridCell` | tris.c | Describes hash vertex grid cell in this module; chosen for the recovered behavior. |
| `HashVertexPosition` | tris.c | Describes hash vertex position in this module; chosen for the recovered behavior. |
| `LabelAdjacentTris` | tris.c | Describes label adjacent tris in this module; chosen for the recovered behavior. |
| `LabelSoupTriGroups` | tris.c | Describes label soup tri groups in this module; chosen for the recovered behavior. |
| `MapDrawVertexIndices` | tris.c | Describes map draw vertex indices in this module; chosen for the recovered behavior. |
| `MatchVertWithUVOffset` | tris.c | Describes match vert with uvoffset in this module; chosen for the recovered behavior. |
| `MergeCloseWindingVerts` | tris.c | Describes merge close winding verts in this module; chosen for the recovered behavior. |
| `MergeConcaveWindingGroup` | tris.c | Describes merge concave winding group in this module; chosen for the recovered behavior. |
| `MergeDuplicateVerts` | tris.c | Describes merge duplicate verts in this module; chosen for the recovered behavior. |
| `MergeNearbyTriGroups` | tris.c | Describes merge nearby tri groups in this module; chosen for the recovered behavior. |
| `MergeVertexClasses` | tris.c | Describes merge vertex classes in this module; chosen for the recovered behavior. |
| `MergeVisGroupCell` | tris.c | Describes merge vis group cell in this module; chosen for the recovered behavior. |
| `MergeVisGroupCells` | tris.c | Describes merge vis group cells in this module; chosen for the recovered behavior. |
| `PartitionSoup_r` | tris.c | Describes partition soup r in this module; chosen for the recovered behavior. |
| `PointOutsideTriSides` | tris.c | Describes point outside tri sides in this module; chosen for the recovered behavior. |
| `PointPairsCoincident2D` | tris.c | Describes point pairs coincident2 d in this module; chosen for the recovered behavior. |
| `PrepareTriSoupVertices` | tris.c | Describes prepare tri soup vertices in this module; chosen for the recovered behavior. |
| `ProjectionCoordsFromNormal` | tris.c | Describes projection coords from normal in this module; chosen for the recovered behavior. |
| `RebuildTriangleWindings` | tris.c | Describes rebuild triangle windings in this module; chosen for the recovered behavior. |
| `RecenterTexCoords` | tris.c | Describes recenter tex coords in this module; chosen for the recovered behavior. |
| `RemoveDegenerateTris` | tris.c | Describes remove degenerate tris in this module; chosen for the recovered behavior. |
| `RemoveEqualPoints` | tris.c | Describes remove equal points in this module; chosen for the recovered behavior. |
| `RemoveWindingVertex` | tris.c | Describes remove winding vertex in this module; chosen for the recovered behavior. |
| `ReorderVertsByFirstUse` | tris.c | Describes reorder verts by first use in this module; chosen for the recovered behavior. |
| `RetireTriangleEdge` | tris.c | Describes retire triangle edge in this module; chosen for the recovered behavior. |
| `SelectSurfaceTextureTriangle` | tris.c | Describes select surface texture triangle in this module; chosen for the recovered behavior. |
| `SimplifyTriangleMesh` | tris.c | Describes simplify triangle mesh in this module; chosen for the recovered behavior. |
| `SmoothTriangleNormals` | tris.c | Describes smooth triangle normals in this module; chosen for the recovered behavior. |
| `SnapMergedVerts` | tris.c | Describes snap merged verts in this module; chosen for the recovered behavior. |
| `SplitPointCompare` | tris.c | Describes split point compare in this module; chosen for the recovered behavior. |
| `SplitSoupByGroups` | tris.c | Describes split soup by groups in this module; chosen for the recovered behavior. |
| `SplitSoupOnAxis` | tris.c | Describes split soup on axis in this module; chosen for the recovered behavior. |
| `SubdivideThinWinding` | tris.c | Describes subdivide thin winding in this module; chosen for the recovered behavior. |
| `TJunc_AddEdgeLine` | tris.c | Describes tjunc add edge line in this module; chosen for the recovered behavior. |
| `TJunc_AddWindingEdge` | tris.c | Describes tjunc add winding edge in this module; chosen for the recovered behavior. |
| `TJunc_ClassifyEdgeAxis` | tris.c | Describes tjunc classify edge axis in this module; chosen for the recovered behavior. |
| `TJunc_ClearHash` | tris.c | Describes tjunc clear hash in this module; chosen for the recovered behavior. |
| `TJunc_EdgeLineMatches` | tris.c | Describes tjunc edge line matches in this module; chosen for the recovered behavior. |
| `TJunc_FindEdge` | tris.c | Describes tjunc find edge in this module; chosen for the recovered behavior. |
| `TJunc_FixAll` | tris.c | Describes tjunc fix all in this module; chosen for the recovered behavior. |
| `TJunc_FixWinding` | tris.c | Describes tjunc fix winding in this module; chosen for the recovered behavior. |
| `TJunc_HashForEdge` | tris.c | Describes tjunc hash for edge in this module; chosen for the recovered behavior. |
| `TJunc_InsertPoint` | tris.c | Describes tjunc insert point in this module; chosen for the recovered behavior. |
| `TJunc_MarkIntersecting` | tris.c | Describes tjunc mark intersecting in this module; chosen for the recovered behavior. |
| `TJunc_PrintEdgeLineUsage` | tris.c | Describes tjunc print edge line usage in this module; chosen for the recovered behavior. |
| `TJunc_ProcessBounds` | tris.c | Describes tjunc process bounds in this module; chosen for the recovered behavior. |
| `TJunc_ResetCounters` | tris.c | Describes tjunc reset counters in this module; chosen for the recovered behavior. |
| `TJunc_Unused0` | tris.c | Distinguishes two empty target routines; their former purpose and original names are unknown. |
| `TJunc_Unused1` | tris.c | Distinguishes two empty target routines; their former purpose and original names are unknown. |
| `TesselateWinding` | tris.c | Describes tesselate winding in this module; chosen for the recovered behavior. |
| `TexVecsEquivalent` | tris.c | Describes tex vecs equivalent in this module; chosen for the recovered behavior. |
| `TriRecordCompare` | tris.c | Describes tri record compare in this module; chosen for the recovered behavior. |
| `TriRecordsShareEdge` | tris.c | Describes tri records share edge in this module; chosen for the recovered behavior. |
| `TriSurfHashIndex` | tris.c | Describes tri surf hash index in this module; chosen for the recovered behavior. |
| `TriSurfPointerCompare` | tris.c | Describes tri surf pointer compare in this module; chosen for the recovered behavior. |
| `TriVertToDrawVert` | tris.c | Describes tri vert to draw vert in this module; chosen for the recovered behavior. |
| `TriangleCanSimplify` | tris.c | Describes triangle can simplify in this module; chosen for the recovered behavior. |
| `TriangleMinAngleCosine` | tris.c | Describes triangle min angle cosine in this module; chosen for the recovered behavior. |
| `TrianglePairCanShareEdge` | tris.c | Describes triangle pair can share edge in this module; chosen for the recovered behavior. |
| `TrianglesShareEdge` | tris.c | Describes triangles share edge in this module; chosen for the recovered behavior. |
| `TriangulateEntity` | tris.c | Describes triangulate entity in this module; chosen for the recovered behavior. |
| `TriangulateUnsplittableWinding` | tris.c | Describes triangulate unsplittable winding in this module; chosen for the recovered behavior. |
| `TrisAffineValue` | tris.c | Describes tris affine value in this module; chosen for the recovered behavior. |
| `TrisBridgeCutsWindingWedge` | tris.c | Describes tris bridge cuts winding wedge in this module; chosen for the recovered behavior. |
| `TrisCheckBothEdges` | tris.c | Describes tris check both edges in this module; chosen for the recovered behavior. |
| `TrisFindCoincidentRun` | tris.c | Describes tris find coincident run in this module; chosen for the recovered behavior. |
| `TrisGetCellListCount` | tris.c | Describes tris get cell list count in this module; chosen for the recovered behavior. |
| `TrisReconnectWindingArcs` | tris.c | Describes tris reconnect winding arcs in this module; chosen for the recovered behavior. |
| `Tris_EmitWindingAsDrawSurf` | tris.c | Describes tris emit winding as draw surf in this module; chosen for the recovered behavior. |
| `Tris_FindIndexedMeshWindings` | tris.c | Describes tris find indexed mesh windings in this module; chosen for the recovered behavior. |
| `Tris_FindPatchWindings` | tris.c | Describes tris find patch windings in this module; chosen for the recovered behavior. |
| `Tris_FindWindings` | tris.c | Describes tris find windings in this module; chosen for the recovered behavior. |
| `Tris_TriangulateWindings` | tris.c | Describes tris triangulate windings in this module; chosen for the recovered behavior. |
| `Tris_WindingFromBrushSide` | tris.c | Describes tris winding from brush side in this module; chosen for the recovered behavior. |
| `TryCollapseTriangleEdge` | tris.c | Describes try collapse triangle edge in this module; chosen for the recovered behavior. |
| `WindingHasCrossingEdge` | tris.c | Describes winding has crossing edge in this module; chosen for the recovered behavior. |
| `WindingIndexInArc` | tris.c | Describes winding index in arc in this module; chosen for the recovered behavior. |
| `WindingPointsNear` | tris.c | Describes winding points near in this module; chosen for the recovered behavior. |
| `WindingsCoplanar` | tris.c | Describes windings coplanar in this module; chosen for the recovered behavior. |
| `WindingsSeparated` | tris.c | Describes windings separated in this module; chosen for the recovered behavior. |
| `GenerateTriangleListGroups` | tristrip_nv.cpp | Describes generate triangle list groups in this module; chosen for the recovered behavior. |
| `GenerateTriangleStripGroups` | tristrip_nv.cpp | Describes generate triangle strip groups in this module; chosen for the recovered behavior. |
| `RemapTriangleListIndices` | tristrip_nv.cpp | Describes remap triangle list indices in this module; chosen for the recovered behavior. |
| `CalcFastVis` | vis.c | Describes calc fast vis in this module; chosen for the recovered behavior. |
| `CalcPHS` | vis.c | Describes calc phs in this module; chosen for the recovered behavior. |
| `CalcPassagePortalVis` | vis.c | Describes calc passage portal vis in this module; chosen for the recovered behavior. |
| `CalcPortalVis` | vis.c | Describes calc portal vis in this module; chosen for the recovered behavior. |
| `CalcVis` | vis.c | Describes calc vis in this module; chosen for the recovered behavior. |
| `ClusterMerge` | vis.c | Describes cluster merge in this module; chosen for the recovered behavior. |
| `CountActivePortals` | vis.c | Describes count active portals in this module; chosen for the recovered behavior. |
| `LeafVectorFromPortalVector` | vis.c | Describes leaf vector from portal vector in this module; chosen for the recovered behavior. |
| `LoadPortals` | vis.c | Describes load portals in this module; chosen for the recovered behavior. |
| `MergeLeafPortals` | vis.c | Describes merge leaf portals in this module; chosen for the recovered behavior. |
| `MergeLeaves` | vis.c | Describes merge leaves in this module; chosen for the recovered behavior. |
| `NewWinding` | vis.c | Describes new winding in this module; chosen for the recovered behavior. |
| `PComp` | vis.c | Describes pcomp in this module; chosen for the recovered behavior. |
| `PlaneFromWinding` | vis.c | Describes plane from winding in this module; chosen for the recovered behavior. |
| `SetPortalSphere` | vis.c | Describes set portal sphere in this module; chosen for the recovered behavior. |
| `SortPortals` | vis.c | Describes sort portals in this module; chosen for the recovered behavior. |
| `TryMergeLeaves` | vis.c | Describes try merge leaves in this module; chosen for the recovered behavior. |
| `TryMergeWinding` | vis.c | Describes try merge winding in this module; chosen for the recovered behavior. |
| `UpdatePortals` | vis.c | Describes update portals in this module; chosen for the recovered behavior. |
| `VisMain` | vis.c | Describes vis main in this module; chosen for the recovered behavior. |
| `Winding_PlanesConcave` | vis.c | Describes winding planes concave in this module; chosen for the recovered behavior. |
| `WritePortals` | vis.c | Describes write portals in this module; chosen for the recovered behavior. |
| `prl` | vis.c | Describes prl in this module; chosen for the recovered behavior. |
| `AddSeperators` | visflow.c | Describes add seperators in this module; chosen for the recovered behavior. |
| `AllocStackWinding` | visflow.c | Describes alloc stack winding in this module; chosen for the recovered behavior. |
| `BasePortalVis` | visflow.c | Describes base portal vis in this module; chosen for the recovered behavior. |
| `BetterPortalVis` | visflow.c | Describes better portal vis in this module; chosen for the recovered behavior. |
| `CheckStack` | visflow.c | Describes check stack in this module; chosen for the recovered behavior. |
| `ClipToSeperators` | visflow.c | Describes clip to seperators in this module; chosen for the recovered behavior. |
| `CountBits` | visflow.c | Describes count bits in this module; chosen for the recovered behavior. |
| `CreatePassages` | visflow.c | Describes create passages in this module; chosen for the recovered behavior. |
| `FreeStackWinding` | visflow.c | Describes free stack winding in this module; chosen for the recovered behavior. |
| `PassageChopWinding` | visflow.c | Describes passage chop winding in this module; chosen for the recovered behavior. |
| `PassageFlow` | visflow.c | Describes passage flow in this module; chosen for the recovered behavior. |
| `PassageMemory` | visflow.c | Describes passage memory in this module; chosen for the recovered behavior. |
| `PassagePortalFlow` | visflow.c | Describes passage portal flow in this module; chosen for the recovered behavior. |
| `PortalFlow` | visflow.c | Describes portal flow in this module; chosen for the recovered behavior. |
| `RecursiveLeafBitFlow` | visflow.c | Describes recursive leaf bit flow in this module; chosen for the recovered behavior. |
| `RecursiveLeafFlow` | visflow.c | Describes recursive leaf flow in this module; chosen for the recovered behavior. |
| `RecursivePassageFlow` | visflow.c | Describes recursive passage flow in this module; chosen for the recovered behavior. |
| `RecursivePassagePortalFlow` | visflow.c | Describes recursive passage portal flow in this module; chosen for the recovered behavior. |
| `SimpleFlood` | visflow.c | Describes simple flood in this module; chosen for the recovered behavior. |
| `VisChopWinding` | visflow.c | Describes vis chop winding in this module; chosen for the recovered behavior. |
| `BeginBSPFile` | writebsp.c | Describes begin bspfile in this module; chosen for the recovered behavior. |
| `BeginModel` | writebsp.c | Describes begin model in this module; chosen for the recovered behavior. |
| `EmitBrushes` | writebsp.c | Describes emit brushes in this module; chosen for the recovered behavior. |
| `EmitDrawNode_r` | writebsp.c | Describes emit draw node r in this module; chosen for the recovered behavior. |
| `EmitLeaf` | writebsp.c | Describes emit leaf in this module; chosen for the recovered behavior. |
| `EmitPlanes` | writebsp.c | Describes emit planes in this module; chosen for the recovered behavior. |
| `EmitShader` | writebsp.c | Describes emit shader in this module; chosen for the recovered behavior. |
| `EndBSPFile` | writebsp.c | Describes end bspfile in this module; chosen for the recovered behavior. |
| `EndModel` | writebsp.c | Describes end model in this module; chosen for the recovered behavior. |
| `RemapBrushPlanes` | writebsp.c | Describes remap brush planes in this module; chosen for the recovered behavior. |
| `RemapNodePlanes` | writebsp.c | Describes remap node planes in this module; chosen for the recovered behavior. |
| `SetCoronaCutoffs` | writebsp.c | Describes set corona cutoffs in this module; chosen for the recovered behavior. |
| `SetLightStyles` | writebsp.c | Describes set light styles in this module; chosen for the recovered behavior. |
| `SetModelNumbers` | writebsp.c | Describes set model numbers in this module; chosen for the recovered behavior. |

## Globals

| Name | Module / record | Reason |
| --- | --- | --- |
| `c_active_brushes` | brush.c | Tracks c active brushes for brush; int c_active_brushes. |
| `c_nodes` | brush.c | Tracks c nodes for brush; int c_nodes. |
| `g_bBrushPrimit` | brush_primit.c | Tracks g b brush primit for brush_primit; int g_bBrushPrimit. |
| `blockSize` | bsp.c | Tracks block size for bsp; float blockSize = 1024.0f. |
| `entity_num` | bsp.c | Tracks entity num for bsp; int entity_num. |
| `fakemap` | bsp.c | Tracks fakemap for bsp; qboolean fakemap. |
| `fulldetail` | bsp.c | Tracks fulldetail for bsp; qboolean fulldetail. |
| `glview` | bsp.c | Tracks glview for bsp; qboolean glview. |
| `leaktest` | bsp.c | Tracks leaktest for bsp; qboolean leaktest. |
| `microvolume` | bsp.c | Tracks microvolume for bsp; vec_t microvolume = 1.0f. |
| `name` | bsp.c | Tracks name for bsp; char name[1024]. |
| `noCurveBrushes` | bsp.c | Tracks no curve brushes for bsp; qboolean noCurveBrushes. |
| `nodetail` | bsp.c | Tracks nodetail for bsp; qboolean nodetail. |
| `nofill` | bsp.c | Tracks nofill for bsp; qboolean nofill. |
| `nofog` | bsp.c | Tracks nofog for bsp; qboolean nofog. |
| `nomerge` | bsp.c | Tracks nomerge for bsp; qboolean nomerge. |
| `noopt` | bsp.c | Tracks noopt for bsp; qboolean noopt. |
| `nosubdivide` | bsp.c | Tracks nosubdivide for bsp; qboolean nosubdivide. |
| `nowater` | bsp.c | Tracks nowater for bsp; qboolean nowater. |
| `onlyents` | bsp.c | Tracks onlyents for bsp; qboolean onlyents. |
| `onlytextures` | bsp.c | Tracks onlytextures for bsp; qboolean onlytextures. |
| `outbase` | bsp.c | Tracks outbase for bsp; char outbase[32]. |
| `showseams` | bsp.c | Tracks showseams for bsp; qboolean showseams. |
| `source` | bsp.c | Tracks source for bsp; char source[1024]. |
| `tempsource` | bsp.c | Tracks tempsource for bsp; char tempsource[1024]. |
| `testExpand` | bsp.c | Tracks test expand for bsp; qboolean testExpand. |
| `verboseentities` | bsp.c | Tracks verboseentities for bsp; qboolean verboseentities. |
| `c_faceLeafs` | facebsp.c | Tracks c face leafs for facebsp; int c_faceLeafs. |
| `hintsplit` | facebsp.c | Tracks hintsplit for facebsp; int hintsplit. |
| `c_fogFragment` | fog.c | Tracks c fog fragment for fog; int c_fogFragment. |
| `c_fogPatchFragments` | fog.c | Tracks c fog patch fragments for fog; int c_fogPatchFragments. |
| `draw_maxs` | gldraw.c | Tracks draw maxs for gldraw; vec3_t draw_mins, draw_maxs. |
| `draw_mins` | gldraw.c | Tracks draw mins for gldraw; vec3_t draw_mins, draw_maxs. |
| `draw_socket` | gldraw.c | Tracks draw socket for gldraw; int draw_socket. |
| `drawflag` | gldraw.c | Tracks drawflag for gldraw; qboolean drawflag. |
| `wins_init` | gldraw.c | Tracks wins init for gldraw; qboolean wins_init. |
| `c_glfaces` | glfile.c | Tracks c glfaces for glfile; int c_glfaces. |
| `leakFileWritten` | leakfile.c | Tracks leak file written for leakfile; static qboolean leakFileWritten. |
| `allocated` | lightmaps.c | Tracks allocated for lightmaps; int allocated[LIGHTMAP_BLOCK_SIZE]. |
| `bspLightmapGridHeight` | lightmaps.c | Tracks bsp lightmap grid height for lightmaps; int bspLightmapGridHeight. |
| `c_exactLightmap` | lightmaps.c | Tracks c exact lightmap for lightmaps; int c_exactLightmap. |
| `colorLightmaps` | lightmaps.c | Tracks color lightmaps for lightmaps; qboolean colorLightmaps = 0. |
| `currentMaterialSet` | lightmaps.c | Tracks current material set for lightmaps; lightmapMaterial_t *currentMaterialSet. |
| `lightmapBlocks` | lightmaps.c | Tracks lightmap blocks for lightmaps; static lightmapBlock_t *lightmapBlocks = NULL. |
| `lightmapBorder` | lightmaps.c | Tracks lightmap border for lightmaps; const int lightmapBorder = 2. |
| `lightmapCellsGroup` | lightmaps.c | Tracks lightmap cells group for lightmaps; int lightmapCellsGroup. |
| `lightmapEfficiency` | lightmaps.c | Tracks lightmap efficiency for lightmaps; float lightmapEfficiency = 0. |
| `lightmapGridMins` | lightmaps.c | Tracks lightmap grid mins for lightmaps; float lightmapGridMins[2]. |
| `lightmapGridWidth` | lightmaps.c | Tracks lightmap grid width for lightmaps; int lightmapGridWidth. |
| `lightmapGroupGrid` | lightmaps.c | Tracks lightmap group grid for lightmaps; lightmapGroupCell_t *lightmapGroupGrid. |
| `lightmapNormalDotThreshold` | lightmaps.c | Tracks lightmap normal dot threshold for lightmaps; float lightmapNormalDotThreshold = 0.9f. |
| `materialGroupSortArray` | lightmaps.c | Tracks material group sort array for lightmaps; lightmapMaterial_t materialGroupSortArray[MAX_MAP_SHADERS]. |
| `numLightmaps` | lightmaps.c | Tracks num lightmaps for lightmaps; int numLightmaps = 1. |
| `numSortShader` | lightmaps.c | Tracks num sort shader for lightmaps; int numSortShader. |
| `samplesize` | lightmaps.c | Tracks samplesize for lightmaps; int samplesize = 16. |
| `baseaxis` | map.c | Names the baseaxis table used by map. |
| `buildBrush` | map.c | Tracks build brush for map; bspbrush_t *buildBrush. |
| `c_areaportals` | map.c | Tracks c areaportals for map; int c_boxbevels, c_edgebevels, c_areaportals, c_detail, c_structural. |
| `c_boxbevels` | map.c | Tracks c boxbevels for map; int c_boxbevels, c_edgebevels, c_areaportals, c_detail, c_structural. |
| `c_detail` | map.c | Tracks c detail for map; int c_boxbevels, c_edgebevels, c_areaportals, c_detail, c_structural. |
| `c_edgebevels` | map.c | Tracks c edgebevels for map; int c_boxbevels, c_edgebevels, c_areaportals, c_detail, c_structural. |
| `c_structural` | map.c | Tracks c structural for map; int c_boxbevels, c_edgebevels, c_areaportals, c_detail, c_structural. |
| `currentEntNum` | map.c | Tracks current ent num for map; int currentEntNum. |
| `entitySourceBrushes` | map.c | Tracks entity source brushes for map; int entitySourceBrushes. |
| `mapIndexedShaders` | map.c | Tracks map indexed shaders for map; char mapIndexedShaders[MAX_MAP_BRUSHSIDES][MAX_QPATH]. |
| `map_maxs` | map.c | Tracks map maxs for map; vec3_t map_mins, map_maxs. |
| `map_mins` | map.c | Tracks map mins for map; vec3_t map_mins, map_maxs. |
| `mapent` | map.c | Tracks mapent for map; entity_t *mapent. |
| `mapplanes` | map.c | Tracks mapplanes for map; plane_t mapplanes[MAX_MAP_PLANES]. |
| `numMapIndexedShaders` | map.c | Tracks num map indexed shaders for map; int numMapIndexedShaders. |
| `numMapPatches` | map.c | Tracks num map patches for map; int numMapPatches. |
| `nummapplanes` | map.c | Tracks nummapplanes for map; int nummapplanes. |
| `planehash` | map.c | Tracks planehash for map; plane_t *planehash[PLANE_HASHES]. |
| `expand` | mesh.c | Tracks expand for mesh; static drawVert_t expand[MAX_EXPANDED_AXIS][MAX_EXPANDED_AXIS]. |
| `neighbors` | mesh.c | Names the neighbors table used by mesh. |
| `c_active_portals` | portals.c | Tracks c active portals for portals; int c_active_portals. |
| `c_areas` | portals.c | Tracks c areas for portals; int c_areas. |
| `c_boundary` | portals.c | Tracks c boundary for portals; int c_boundary. |
| `c_boundary_sides` | portals.c | Tracks c boundary sides for portals; int c_boundary_sides. |
| `c_floodedleafs` | portals.c | Tracks c floodedleafs for portals; int c_floodedleafs. |
| `c_inside` | portals.c | Tracks c inside for portals; int c_inside. |
| `c_outside` | portals.c | Tracks c outside for portals; int c_outside. |
| `c_peak_portals` | portals.c | Tracks c peak portals for portals; int c_peak_portals. |
| `c_solid` | portals.c | Tracks c solid for portals; int c_solid. |
| `c_tinyportals` | portals.c | Tracks c tinyportals for portals; int c_tinyportals. |
| `cellCullGroupBits` | portals.c | Tracks cell cull group bits for portals; unsigned char cellCullGroupBits[1048576]. |
| `cell_portals` | portals.c | Tracks cell portals for portals; cellPortal_t *cell_portals[MAX_MAP_CELLS]. |
| `num_solidfaces` | prtfile.c | Tracks num solidfaces for prtfile; int num_solidfaces. |
| `num_visclusters` | prtfile.c | Tracks num visclusters for prtfile; int num_visclusters. |
| `num_visportals` | prtfile.c | Tracks num visportals for prtfile; int num_visportals. |
| `pf` | prtfile.c | Tracks pf for prtfile; FILE *pf. |
| `buildBrush` | qbsp.h | Tracks build brush for qbsp; extern bspbrush_t *buildBrush. |
| `c_triangleIndexes` | qbsp.h | Tracks c triangle indexes for qbsp; extern int c_triangleIndexes. |
| `c_triangleModels` | qbsp.h | Tracks c triangle models for qbsp; extern int c_triangleModels. |
| `c_triangleSurfaces` | qbsp.h | Tracks c triangle surfaces for qbsp; extern int c_triangleSurfaces. |
| `c_triangleVertexes` | qbsp.h | Tracks c triangle vertexes for qbsp; extern int c_triangleVertexes. |
| `coplanar` | qbsp.h | Tracks coplanar for qbsp; extern qboolean coplanar. |
| `draw_maxs` | qbsp.h | Tracks draw maxs for qbsp; extern vec3_t draw_mins, draw_maxs. |
| `draw_mins` | qbsp.h | Tracks draw mins for qbsp; extern vec3_t draw_mins, draw_maxs. |
| `drawflag` | qbsp.h | Tracks drawflag for qbsp; extern qboolean drawflag. |
| `entitySourceBrushes` | qbsp.h | Tracks entity source brushes for qbsp; extern int entitySourceBrushes. |
| `entity_num` | qbsp.h | Tracks entity num for qbsp; extern int entity_num. |
| `fakemap` | qbsp.h | Tracks fakemap for qbsp; extern qboolean fakemap. |
| `fulldetail` | qbsp.h | Tracks fulldetail for qbsp; extern qboolean fulldetail. |
| `g_bBrushPrimit` | qbsp.h | Tracks g b brush primit for qbsp; extern int g_bBrushPrimit. |
| `mapDrawSurfs` | qbsp.h | Tracks map draw surfs for qbsp; extern mapDrawSurface_t mapDrawSurfs[MAX_MAP_DRAW_SURFS]. |
| `mapIndexedShaders` | qbsp.h | Tracks map indexed shaders for qbsp; extern char mapIndexedShaders[MAX_MAP_BRUSHSIDES][MAX_QPATH]. |
| `map_maxs` | qbsp.h | Tracks map maxs for qbsp; extern vec3_t map_mins, map_maxs. |
| `map_mins` | qbsp.h | Tracks map mins for qbsp; extern vec3_t map_mins, map_maxs. |
| `mapent` | qbsp.h | Tracks mapent for qbsp; extern entity_t *mapent. |
| `mapplanes` | qbsp.h | Tracks mapplanes for qbsp; extern plane_t mapplanes[MAX_MAP_PLANES]. |
| `microvolume` | qbsp.h | Tracks microvolume for qbsp; extern vec_t microvolume. |
| `noCurveBrushes` | qbsp.h | Tracks no curve brushes for qbsp; extern qboolean noCurveBrushes. |
| `nodetail` | qbsp.h | Tracks nodetail for qbsp; extern qboolean nodetail. |
| `nofog` | qbsp.h | Tracks nofog for qbsp; extern qboolean nofog. |
| `noprune` | qbsp.h | Tracks noprune for qbsp; extern qboolean noprune. |
| `nowater` | qbsp.h | Tracks nowater for qbsp; extern qboolean nowater. |
| `numMapDrawSurfs` | qbsp.h | Tracks num map draw surfs for qbsp; extern int numMapDrawSurfs. |
| `numMapIndexedShaders` | qbsp.h | Tracks num map indexed shaders for qbsp; extern int numMapIndexedShaders. |
| `numMapPatches` | qbsp.h | Tracks num map patches for qbsp; extern int numMapPatches. |
| `nummapplanes` | qbsp.h | Tracks nummapplanes for qbsp; extern int nummapplanes. |
| `outbase` | qbsp.h | Tracks outbase for qbsp; extern char outbase[32]. |
| `showseams` | qbsp.h | Tracks showseams for qbsp; extern qboolean showseams. |
| `source` | qbsp.h | Tracks source for qbsp; extern char source[1024]. |
| `testExpand` | qbsp.h | Tracks test expand for qbsp; extern qboolean testExpand. |
| `defaultInfo` | shaders.c | Tracks default info for shaders; shaderInfo_t defaultInfo. |
| `numShaderInfo` | shaders.c | Tracks num shader info for shaders; int numShaderInfo. |
| `shaderInfo` | shaders.c | Tracks shader info for shaders; shaderInfo_t shaderInfo[MAX_SURFACE_INFO]. |
| `debugPolyFile` | surface.c | Tracks debug poly file for surface; FILE *debugPolyFile = 0. |
| `mapDrawSurfs` | surface.c | Tracks map draw surfs for surface; mapDrawSurface_t mapDrawSurfs[MAX_MAP_DRAW_SURFS]. |
| `numMapDrawSurfs` | surface.c | Tracks num map draw surfs for surface; int numMapDrawSurfs. |
| `numSideRefs` | surface.c | Tracks num side refs for surface; int numSideRefs. |
| `sideRefs` | surface.c | Tracks side refs for surface; sideRef_t sideRefs[MAX_SIDE_REFS]. |
| `infoParms` | terrain.c | Names the info parms table used by terrain. |
| `lastSurface` | terrain.c | Tracks last surface for terrain; static terrainSurf_t *lastSurface = NULL. |
| `maxsurfaces` | terrain.c | Tracks maxsurfaces for terrain; static int maxsurfaces = 0. |
| `numsurfaces` | terrain.c | Tracks numsurfaces for terrain; static int numsurfaces = 0. |
| `numtextures` | terrain.c | Tracks numtextures for terrain; static int numtextures = 0. |
| `surfaces` | terrain.c | Tracks surfaces for terrain; static terrainSurf_t *surfaces = NULL. |
| `textures` | terrain.c | Tracks textures for terrain; static shaderInfo_t *textures[MAX_TERRAIN_TEXTURES]. |
| `c_addedVerts` | tjunction.c | Tracks c added verts for tjunction; int c_addedVerts. |
| `c_cant` | tjunction.c | Tracks c cant for tjunction; int c_natural, c_rotate, c_cant. |
| `c_degenerateEdges` | tjunction.c | Tracks c degenerate edges for tjunction; int c_degenerateEdges. |
| `c_natural` | tjunction.c | Tracks c natural for tjunction; int c_natural, c_rotate, c_cant. |
| `c_rotate` | tjunction.c | Tracks c rotate for tjunction; int c_natural, c_rotate, c_cant. |
| `c_totalVerts` | tjunction.c | Tracks c total verts for tjunction; int c_totalVerts. |
| `edgeLines` | tjunction.c | Tracks edge lines for tjunction; edgeLine_t edgeLines[MAX_EDGE_LINES]. |
| `numEdgeLines` | tjunction.c | Tracks num edge lines for tjunction; int numEdgeLines. |
| `numOriginalEdges` | tjunction.c | Tracks num original edges for tjunction; int numOriginalEdges. |
| `originalEdges` | tjunction.c | Tracks original edges for tjunction; originalEdge_t originalEdges[MAX_ORIGINAL_EDGES]. |
| `brushSmoothAngle` | tris.c | Tracks brush smooth angle for tris; float brushSmoothAngle = 1.0f. |
| `c_addedThinWindingPoints` | tris.c | Tracks c added thin winding points for tris; static int c_addedThinWindingPoints = 0. |
| `c_thinWindingInputPoints` | tris.c | Tracks c thin winding input points for tris; static int c_thinWindingInputPoints = 0. |
| `curveSmoothAngle` | tris.c | Tracks curve smooth angle for tris; float curveSmoothAngle = 0.01f. |
| `g_aabbSortEqual` | tris.c | Tracks g aabb sort equal for tris; float *g_aabbSortMin, *g_aabbSortMax, *g_aabbSortEqual. |
| `g_aabbSortMax` | tris.c | Tracks g aabb sort max for tris; float *g_aabbSortMin, *g_aabbSortMax, *g_aabbSortEqual. |
| `g_aabbSortMin` | tris.c | Tracks g aabb sort min for tris; float *g_aabbSortMin, *g_aabbSortMax, *g_aabbSortEqual. |
| `numDegenerateTriEdges` | tris.c | Tracks num degenerate tri edges for tris; static int numDegenerateTriEdges = 0. |
| `numOriginalDrawVerts` | tris.c | Tracks num original draw verts for tris; static int numOriginalDrawVerts = 0. |
| `numSimplifiedTriangles` | tris.c | Tracks num simplified triangles for tris; static int numSimplifiedTriangles = 0. |
| `numTJuncEdgeLines` | tris.c | Tracks num tjunc edge lines for tris; static int numTJuncEdgeLines = 0. |
| `numTJuncPoints` | tris.c | Tracks num tjunc points for tris; static int numTJuncPoints = 0. |
| `numTextureDirectionMismatches` | tris.c | Tracks num texture direction mismatches for tris; static int numTextureDirectionMismatches = 0. |
| `numTriIntermediateVerts` | tris.c | Tracks num tri intermediate verts for tris; static int numTriIntermediateVerts = 0. |
| `numTriSplitPoints` | tris.c | Tracks num tri split points for tris; static int numTriSplitPoints = 0. |
| `numTriangleEdges` | tris.c | Tracks num triangle edges for tris; static int numTriangleEdges = 0. |
| `numTriangles` | tris.c | Tracks num triangles for tris; static int numTriangles = 0. |
| `terrainSmoothAngle` | tris.c | Tracks terrain smooth angle for tris; float terrainSmoothAngle = 0.01f. |
| `tjuncCellBounds` | tris.c | Names the tjunc cell bounds table used by tris. |
| `tjuncEdgeLines` | tris.c | Names the tjunc edge lines table used by tris. |
| `tjuncHash` | tris.c | Names the tjunc hash table used by tris. |
| `tjuncPoints` | tris.c | Names the tjunc points table used by tris. |
| `tjuncTolerance` | tris.c | Tracks tjunc tolerance for tris; float tjuncTolerance = 0.25f. |
| `triIntermediateVerts` | tris.c | Names the tri intermediate verts table used by tris. |
| `triRecords` | tris.c | Names the tri records table used by tris. |
| `triangleEdgeHash` | tris.c | Names the triangle edge hash table used by tris. |
| `triangleEdges` | tris.c | Names the triangle edges table used by tris. |
| `triangleVertexHash` | tris.c | Names the triangle vertex hash table used by tris. |
| `triangleVertexRemap` | tris.c | Names the triangle vertex remap table used by tris. |
| `trisCurrentTree` | tris.c | Tracks tris current tree for tris; static tree_t *trisCurrentTree = 0. |
| `c_portalcheck` | vis.c | Tracks c portalcheck for vis; int c_portaltest, c_portalpass, c_portalcheck. |
| `c_portalpass` | vis.c | Tracks c portalpass for vis; int c_portaltest, c_portalpass, c_portalcheck. |
| `c_portaltest` | vis.c | Tracks c portaltest for vis; int c_portaltest, c_portalpass, c_portalcheck. |
| `faceleafs` | vis.c | Tracks faceleafs for vis; leaf_t *faceleafs. |
| `faces` | vis.c | Tracks faces for vis; vportal_t *faces. |
| `fastvis` | vis.c | Tracks fastvis for vis; qboolean fastvis. |
| `inbase` | vis.c | Tracks inbase for vis; char inbase[32]. |
| `leafbytes` | vis.c | Tracks leafbytes for vis; int leafbytes. |
| `leaflongs` | vis.c | Tracks leaflongs for vis; int leaflongs. |
| `leafs` | vis.c | Tracks leafs for vis; leaf_t *leafs. |
| `mergevis` | vis.c | Tracks mergevis for vis; qboolean mergevis. |
| `nopassagevis` | vis.c | Tracks nopassagevis for vis; qboolean nopassagevis. |
| `nosort` | vis.c | Tracks nosort for vis; qboolean nosort. |
| `numfaces` | vis.c | Tracks numfaces for vis; int numfaces. |
| `numportals` | vis.c | Tracks numportals for vis; int numportals. |
| `outbase` | vis.c | Tracks outbase for vis; extern char outbase[32]. |
| `portalbytes` | vis.c | Tracks portalbytes for vis; int portalbytes, portallongs. |
| `portalclusters` | vis.c | Tracks portalclusters for vis; int portalclusters. |
| `portallongs` | vis.c | Tracks portallongs for vis; int portalbytes, portallongs. |
| `portals` | vis.c | Tracks portals for vis; vportal_t *portals. |
| `saveprt` | vis.c | Tracks saveprt for vis; qboolean saveprt. |
| `sorted_portals` | vis.c | Tracks sorted portals for vis; vportal_t *sorted_portals[MAX_MAP_PORTALS*2]. |
| `testlevel` | vis.c | Tracks testlevel for vis; int testlevel = 2. |
| `totalvis` | vis.c | Tracks totalvis for vis; int totalvis. |
| `c_chains` | vis.h | Tracks c chains for vis; extern int c_chains. |
| `c_leafskip` | vis.h | Tracks c leafskip for vis; extern int c_portalskip, c_leafskip. |
| `c_mighttest` | vis.h | Tracks c mighttest for vis; extern int c_vistest, c_mighttest. |
| `c_portalcheck` | vis.h | Tracks c portalcheck for vis; extern int c_portaltest, c_portalpass, c_portalcheck. |
| `c_portalpass` | vis.h | Tracks c portalpass for vis; extern int c_portaltest, c_portalpass, c_portalcheck. |
| `c_portalskip` | vis.h | Tracks c portalskip for vis; extern int c_portalskip, c_leafskip. |
| `c_portaltest` | vis.h | Tracks c portaltest for vis; extern int c_portaltest, c_portalpass, c_portalcheck. |
| `c_vistest` | vis.h | Tracks c vistest for vis; extern int c_vistest, c_mighttest. |
| `leafbytes` | vis.h | Tracks leafbytes for vis; extern int leafbytes, leaflongs. |
| `leaflongs` | vis.h | Tracks leaflongs for vis; extern int leafbytes, leaflongs. |
| `leafs` | vis.h | Tracks leafs for vis; extern leaf_t *leafs. |
| `numportals` | vis.h | Tracks numportals for vis; extern int numportals. |
| `portalbytes` | vis.h | Tracks portalbytes for vis; extern int portalbytes, portallongs. |
| `portalclusters` | vis.h | Tracks portalclusters for vis; extern int portalclusters. |
| `portallongs` | vis.h | Tracks portallongs for vis; extern int portalbytes, portallongs. |
| `portals` | vis.h | Tracks portals for vis; extern vportal_t *portals. |
| `sorted_portals` | vis.h | Tracks sorted portals for vis; extern vportal_t *sorted_portals[MAX_MAP_PORTALS*2]. |
| `testlevel` | vis.h | Tracks testlevel for vis; extern int testlevel. |
| `uncompressed` | vis.h | Tracks uncompressed for vis; extern byte *uncompressed. |
| `vismap` | vis.h | Tracks vismap for vis; extern byte *vismap, *vismap_p, *vismap_end. |
| `vismap_end` | vis.h | Tracks vismap end for vis; extern byte *vismap, *vismap_p, *vismap_end. |
| `vismap_p` | vis.h | Tracks vismap p for vis; extern byte *vismap, *vismap_p, *vismap_end. |
| `active` | visflow.c | Tracks active for visflow; int active. |
| `c_chop` | visflow.c | Tracks c chop for visflow; int c_chop, c_nochop. |
| `c_flood` | visflow.c | Tracks c flood for visflow; int c_flood, c_vis. |
| `c_fullskip` | visflow.c | Tracks c fullskip for visflow; int c_fullskip. |
| `c_leafskip` | visflow.c | Tracks c leafskip for visflow; int c_portalskip, c_leafskip. |
| `c_mighttest` | visflow.c | Tracks c mighttest for visflow; int c_vistest, c_mighttest. |
| `c_nochop` | visflow.c | Tracks c nochop for visflow; int c_chop, c_nochop. |
| `c_portalskip` | visflow.c | Tracks c portalskip for visflow; int c_portalskip, c_leafskip. |
| `c_vis` | visflow.c | Tracks c vis for visflow; int c_flood, c_vis. |
| `c_vistest` | visflow.c | Tracks c vistest for visflow; int c_vistest, c_mighttest. |

## Macros

| Name | Module / record | Reason |
| --- | --- | --- |
| `EDGE_LENGTH` | brush.c | Names edge length. Definition: #define EDGE_LENGTH 0.2 |
| `PLANESIDE_EPSILON` | brush.c | Names planeside epsilon. Definition: // if a brush just barely pokes onto the other side, // let it slide by without chopping #define PLANESIDE_EPSILON 0.001 |
| `SMOOTH_ANGLE_COSINE_EPSILON` | bsp.c | Names smooth angle cosine epsilon. Definition: #define SMOOTH_ANGLE_COSINE_EPSILON 0.001f |
| `SMOOTH_ANGLE_RADIANS_PER_DEGREE` | bsp.c | Names smooth angle radians per degree. Definition: #define SMOOTH_ANGLE_RADIANS_PER_DEGREE ( (float) ( Q_PI / 180.0 ) ) |
| `ON_EPSILON` | fog.c | Names on epsilon. Definition: /* =========================================================================== Copyright (C) 1999-2005 Id Software, Inc. This file is part of Quake III Arena source code. Quake III Arena source code i |
| `GLSERV_PORT` | gldraw.c | Names glserv port. Definition: //============================================================ #define GLSERV_PORT 25001 |
| `WIN_SIZE` | gldraw.c | Names win size. Definition: #define WIN_SIZE 512 |
| `CONTENTS_CLIP_MASK` | map.c | Names contents clip mask. Definition: #define CONTENTS_CLIP_MASK (CONTENTS_MISSILECLIP &#124; CONTENTS_VEHICLECLIP &#124; CONTENTS_AI_NOSIGHT &#124; CONTENTS_CLIPSHOT &#124; CONTENTS_PLAYERCLIP &#124; CONTENTS_MONSTERCLIP) |
| `DIST_EPSILON` | map.c | Names dist epsilon. Definition: #define DIST_EPSILON 0.001 |
| `MODEL_SCALE_EPSILON` | map.c | Names model scale epsilon. Definition: #define MODEL_SCALE_EPSILON 0.001f |
| `MapVectorLength` | map.c | Names map vector length. Definition: #define MapVectorLength(v) ( (vec_t)sqrt( (v)[0] * (v)[0] + (v)[1] * (v)[1] + (v)[2] * (v)[2] ) ) |
| `NORMAL_EPSILON` | map.c | Names normal epsilon. Definition: #define NORMAL_EPSILON 0.0000001 |
| `PLANE_HASHES` | map.c | Names plane hashes. Definition: #define PLANE_HASHES 1024 |
| `TEXTURE_SCALE_EPSILON` | map.c | Names texture scale epsilon. Definition: #define TEXTURE_SCALE_EPSILON 0.000001f |
| `MAX_EXPANDED_AXIS` | mesh.h | Names max expanded axis. Definition: #define MAX_EXPANDED_AXIS 512 |
| `MAX_PATCH_TRIANGULATION_AXIS` | patch.c | Names max patch triangulation axis. Definition: #define MAX_PATCH_TRIANGULATION_AXIS 512 |
| `MAX_TERRAIN_GROUP_TRIANGLES` | patch.c | Names max terrain group triangles. Definition: #define MAX_TERRAIN_GROUP_TRIANGLES 16384 |
| `MAX_TERRAIN_GROUP_VERTS` | patch.c | Names max terrain group verts. Definition: #define MAX_TERRAIN_GROUP_VERTS 4096 |
| `MAX_TERRAIN_PATCHES` | patch.c | Names max terrain patches. Definition: #define MAX_TERRAIN_PATCHES 1024 |
| `PATCH_ST_EPSILON` | patch.c | Names patch st epsilon. Definition: #define PATCH_ST_EPSILON ( 0.01f * 0.001f ) |
| `Q3MAP_PLANE_REMAP_H` | plane_remap.h | Names q3 map plane remap h. Definition: #define Q3MAP_PLANE_REMAP_H |
| `BASE_WINDING_EPSILON` | portals.c | Names base winding epsilon. Definition: //=================================================== #define BASE_WINDING_EPSILON 0.001 |
| `MAX_MAP_OCCLUDER_INDEXES` | portals.c | Names max map occluder indexes. Definition: #define MAX_MAP_OCCLUDER_INDEXES 0x18000 |
| `MAX_OCCLUDER_FACE_VERTS` | portals.c | Names max occluder face verts. Definition: #define MAX_OCCLUDER_FACE_VERTS 256 |
| `SIDESPACE` | portals.c | Names sidespace. Definition: /* ================ MakeHeadnodePortals The created portals will face the global outside_node ================ */ #define SIDESPACE 8 |
| `SPLIT_WINDING_EPSILON` | portals.c | Names split winding epsilon. Definition: #define SPLIT_WINDING_EPSILON 0.001 |
| `PORTALFILE` | prtfile.c | Names portalfile. Definition: /* ============================================================================== PORTAL FILE GENERATION Save out name.prt for qvis to read ============================================================ |
| `BPRIMIT_NEWBRUSHES` | qbsp.h | Names bprimit newbrushes. Definition: #define BPRIMIT_NEWBRUSHES 2 |
| `BPRIMIT_OLDBRUSHES` | qbsp.h | Names bprimit oldbrushes. Definition: #define BPRIMIT_OLDBRUSHES 1 |
| `BPRIMIT_UNDEFINED` | qbsp.h | Names bprimit undefined. Definition: //============================================================================== // brush_primit.c #define BPRIMIT_UNDEFINED 0 |
| `CLIP_EPSILON` | qbsp.h | Names clip epsilon. Definition: #define CLIP_EPSILON 0.1 |
| `HINT_PRIORITY` | qbsp.h | Names hint priority. Definition: #define HINT_PRIORITY 1000 |
| `MAX_BRUSH_SIDES` | qbsp.h | Names max brush sides. Definition: #define MAX_BRUSH_SIDES 1024 |
| `MAX_BUILD_SIDES` | qbsp.h | Names max build sides. Definition: #define MAX_BUILD_SIDES 300 |
| `MAX_PATCH_SIZE` | qbsp.h | Names max patch size. Definition: #define MAX_PATCH_SIZE 32 |
| `PLANENUM_LEAF` | qbsp.h | Names planenum leaf. Definition: #define PLANENUM_LEAF -1 |
| `PSIDE_BACK` | qbsp.h | Names pside back. Definition: #define PSIDE_BACK 2 |
| `PSIDE_BOTH` | qbsp.h | Names pside both. Definition: #define PSIDE_BOTH (PSIDE_FRONT&#124;PSIDE_BACK) |
| `PSIDE_FACING` | qbsp.h | Names pside facing. Definition: #define PSIDE_FACING 4 |
| `PSIDE_FRONT` | qbsp.h | Names pside front. Definition: //============================================================================= // brushbsp #define PSIDE_FRONT 1 |
| `MAX_SURFACE_INFO` | shaders.c | Names max surface info. Definition: #define MAX_SURFACE_INFO 4096 |
| `MAX_MAP_COLLISIONVERTS` | surface.c | Names max map collisionverts. Definition: #define MAX_MAP_COLLISIONVERTS 0x20000 |
| `MAX_MAP_PATCHCOLLIDES` | surface.c | Names max map patchcollides. Definition: #define MAX_MAP_PATCHCOLLIDES 0x2000 |
| `MAX_SIDE_REFS` | surface.c | Names max side refs. Definition: #define MAX_SIDE_REFS MAX_MAP_PLANES |
| `COLINEAR_AREA` | terrain.c | Names colinear area. Definition: #define COLINEAR_AREA 10 |
| `CONTENTS_HMG_CROUCHING` | terrain.c | Names contents hmg crouching. Definition: #define CONTENTS_HMG_CROUCHING 0x400000 |
| `CONTENTS_HMG_STANDING` | terrain.c | Names contents hmg standing. Definition: #define CONTENTS_HMG_STANDING 0x4000 |
| `GROW_INDICES` | terrain.c | Names grow indices. Definition: #define GROW_INDICES 512 |
| `GROW_SURFACES` | terrain.c | Names grow surfaces. Definition: #define GROW_SURFACES 128 |
| `GROW_VERTS` | terrain.c | Names grow verts. Definition: #define GROW_VERTS 512 |
| `MAX_INDICES` | terrain.c | Names max indices. Definition: #define MAX_INDICES 1024 |
| `MAX_TERRAIN_TEXTURES` | terrain.c | Names max terrain textures. Definition: #define MAX_TERRAIN_TEXTURES 128 |
| `MAX_TERRAIN_WINDING_POINTS` | terrain.c | Names max terrain winding points. Definition: #define MAX_TERRAIN_WINDING_POINTS 1024 |
| `SURF_HEIGHT` | terrain.c | Names surf height. Definition: #define SURF_HEIGHT 2048 |
| `SURF_WIDTH` | terrain.c | Names surf width. Definition: #define SURF_WIDTH 2048 |
| `VectorSet` | terrain.c | Names vector set. Definition: /* Vector initialization macro from Quake III. */ #define VectorSet(v, x, y, z) ((v)[0]=(x), (v)[1]=(y), (v)[2]=(z)) |
| `Q3MAP_TERRAIN_SURFACE_H` | terrain_surface.h | Names q3 map terrain surface h. Definition: #define Q3MAP_TERRAIN_SURFACE_H |
| `LINE_POSITION_EPSILON` | tjunction.c | Names line position epsilon. Definition: // these should be whatever epsilon we actually expect, // plus SNAP_INT_TO_FLOAT #define LINE_POSITION_EPSILON 0.025f |
| `MAX_EDGE_LINES` | tjunction.c | Names max edge lines. Definition: #define MAX_EDGE_LINES 0x20000 |
| `MAX_ORIGINAL_EDGES` | tjunction.c | Names max original edges. Definition: #define MAX_ORIGINAL_EDGES 0x20000 |
| `MAX_SURFACE_VERTS` | tjunction.c | Names max surface verts. Definition: #define MAX_SURFACE_VERTS 1024 |
| `POINT_ON_LINE_EPSILON` | tjunction.c | Names point on line epsilon. Definition: #define POINT_ON_LINE_EPSILON 0.025f |
| `MAX_NATIVE_TRIANGLE_SOUPS` | tris.c | Names max native triangle soups. Definition: #define MAX_NATIVE_TRIANGLE_SOUPS 131072 |
| `MAX_POINTS_ON_CONCAVE_WINDING` | tris.c | Names max points on concave winding. Definition: #define MAX_POINTS_ON_CONCAVE_WINDING 0x4000 |
| `MAX_THIN_WINDING_POINTS` | tris.c | Names max thin winding points. Definition: #define MAX_THIN_WINDING_POINTS 16384 |
| `MAX_TJUNC_EDGE_LINES` | tris.c | Names max tjunc edge lines. Definition: #define MAX_TJUNC_EDGE_LINES 0x10000 |
| `MAX_TJUNC_POINTS` | tris.c | Names max tjunc points. Definition: #define MAX_TJUNC_POINTS 0x40000 |
| `MAX_TRIANGLE_EDGES` | tris.c | Names max triangle edges. Definition: #define MAX_TRIANGLE_EDGES 0x80000 |
| `MAX_TRI_SOUP_INDICES` | tris.c | Names max tri soup indices. Definition: #define MAX_TRI_SOUP_INDICES 0x60000 |
| `MAX_TRI_SOUP_VERTS` | tris.c | Names max tri soup verts. Definition: #define MAX_TRI_SOUP_VERTS 0x10000 |
| `MAX_WINDINGS_PER_CELL` | tris.c | Names max windings per cell. Definition: /* The cell merger owns its winding repair and shader-dependent geometry. */ #define MAX_WINDINGS_PER_CELL 0x20000 |
| `MAX_WINDINGS_PER_CONCAVE_GROUP` | tris.c | Names max windings per concave group. Definition: #define MAX_WINDINGS_PER_CONCAVE_GROUP 16384 |
| `MAX_WINDINGS_PER_GROUP` | tris.c | Names max windings per group. Definition: #define MAX_WINDINGS_PER_GROUP 0x2000 |
| `MERGE_BOUNDS_EPSILON` | tris.c | Names merge bounds epsilon. Definition: #define MERGE_BOUNDS_EPSILON 0.001f |
| `TJUNC_BOUNDS_INTERSECT` | tris.c | Names tjunc bounds intersect. Definition: #define TJUNC_BOUNDS_INTERSECT( minsA, maxsA, minsB, maxsB ) \ |
| `TJUNC_HASH_AXES` | tris.c | Names tjunc hash axes. Definition: #define TJUNC_HASH_AXES 3 |
| `TJUNC_HASH_AXIS_SIZE` | tris.c | Names tjunc hash axis size. Definition: #define TJUNC_HASH_AXIS_SIZE 256 |
| `TJUNC_OCTREE_MAX_SURFACES` | tris.c | Names tjunc octree max surfaces. Definition: #define TJUNC_OCTREE_MAX_SURFACES 256 |
| `TJUNC_OCTREE_MIN_EXTENT` | tris.c | Names tjunc octree min extent. Definition: #define TJUNC_OCTREE_MIN_EXTENT 8.0f |
| `TJUNC_SKIP_SURFACE_FLAGS` | tris.c | Names tjunc skip surface flags. Definition: #define TJUNC_SKIP_SURFACE_FLAGS ( SURF_SKY &#124; SURF_NODRAW ) |
| `TRIANGLE_DETERMINANT_EPSILON` | tris.c | Names triangle determinant epsilon. Definition: #define TRIANGLE_DETERMINANT_EPSILON 0.001f |
| `TRIANGLE_EDGE_HASH_SIZE` | tris.c | Names triangle edge hash size. Definition: #define TRIANGLE_EDGE_HASH_SIZE 4096 |
| `TRIANGLE_PLANE_EPSILON_SQ` | tris.c | Names triangle plane epsilon sq. Definition: /* Geometric and texture continuity between adjacent triangle records. */ #define TRIANGLE_PLANE_EPSILON_SQ ( 0.001f * 0.001f ) |
| `TRISOUP_AABB_LEAF_LIMIT` | tris.c | Names trisoup aabb leaf limit. Definition: //=========================================================================== // constants and macros //=========================================================================== #define TRISOUP_AABB |
| `TRIS_AFFINE_COMPONENTS` | tris.c | Names tris affine components. Definition: #define TRIS_AFFINE_COMPONENTS( row, point ) \ |
| `TRIS_COLLAPSE_COLOR` | tris.c | Names tris collapse color. Definition: #define TRIS_COLLAPSE_COLOR(row, point) \ |
| `TRIS_COPY4` | tris.c | Names tris copy4. Definition: #define TRIS_COPY4(from, to) \ |
| `TRIS_DEBUG_COLLAPSE` | tris.c | Names tris debug collapse. Definition: #define TRIS_DEBUG_COLLAPSE 0 |
| `TRIS_DISCOVERY_CORNER` | tris.c | Names tris discovery corner. Definition: #define TRIS_DISCOVERY_CORNER(verts, index, winding, corner) \ |
| `TRIS_MAX` | tris.c | Names tris max. Definition: #define TRIS_MAX(a,b) ((a) > (b) ? (a) : (b)) |
| `TRIS_MERGECONCAVE_COLLINEAR_VERTEX_EPSILON` | tris.c | Names tris mergeconcave collinear vertex epsilon. Definition: #define TRIS_MERGECONCAVE_COLLINEAR_VERTEX_EPSILON tjuncTolerance |
| `TRIS_MIN` | tris.c | Names tris min. Definition: #define TRIS_MIN(a,b) ((a) < (b) ? (a) : (b)) |
| `TRIS_PLANE_VALUE` | tris.c | Names tris plane value. Definition: /* ============= FindOrCreateTriSurfProps ============= */ #define TRIS_PLANE_VALUE( v, p ) ( ( ( ( v )[2] * ( p )[2] + ( v )[1] * ( p )[1] ) + ( v )[0] * ( p )[0] ) + ( v )[3] ) |
| `TRI_AABB_LOCAL_ITEMS` | tris.c | Names tri aabb local items. Definition: #define TRI_AABB_LOCAL_ITEMS 32768 |
| `TRI_SURF_PROPS_HASH_BUCKETS` | tris.c | Names tri surf props hash buckets. Definition: #define TRI_SURF_PROPS_HASH_BUCKETS 16384 |
| `WINDING_INTERSECT_EPSILON` | tris.c | Names winding intersect epsilon. Definition: #define WINDING_INTERSECT_EPSILON 0.001f |
| `WINDING_INTERSECT_EPSILON_SQ` | tris.c | Names winding intersect epsilon sq. Definition: #define WINDING_INTERSECT_EPSILON_SQ \ |
| `CONTINUOUS_EPSILON` | vis.c | Names continuous epsilon. Definition: /* ============ TryMergeWinding ============ */ #define CONTINUOUS_EPSILON 0.005 |
| `VIS_HEADER_SIZE` | vis.c | Names vis header size. Definition: #define VIS_HEADER_SIZE 8 |
| `WCONVEX_EPSILON` | vis.c | Names wconvex epsilon. Definition: /* ============= Winding_PlanesConcave ============= */ #define WCONVEX_EPSILON 0.2 |
| `MAX_POINTS_ON_FIXED_WINDING` | vis.h | Names max points on fixed winding. Definition: #define MAX_POINTS_ON_FIXED_WINDING 12 |
| `MAX_POINTS_ON_WINDING` | vis.h | Names max points on winding. Definition: #define MAX_POINTS_ON_WINDING 1024 |
| `MAX_PORTALS` | vis.h | Names max portals. Definition: #define MAX_PORTALS 32768 |
| `MAX_PORTALS_ON_LEAF` | vis.h | Names max portals on leaf. Definition: #define MAX_PORTALS_ON_LEAF 128 |
| `MAX_SEPERATORS` | vis.h | Names max seperators. Definition: // can't have more seperators than the max number of points on a winding #define MAX_SEPERATORS 64 |
| `ON_EPSILON` | vis.h | Names on epsilon. Definition: #define ON_EPSILON 0.1f |
| `PORTALFILE` | vis.h | Names portalfile. Definition: #define PORTALFILE "PRT1" |
| `SEPERATORCACHE` | vis.h | Names seperatorcache. Definition: //#define MREDEBUG // seperator caching helps a bit #define SEPERATORCACHE |
| `MAX_SWITCHED_LIGHTS` | writebsp.c | Names max switched lights. Definition: #define MAX_SWITCHED_LIGHTS 32 |

## Static Locals

| Name | Module / record | Reason |
| --- | --- | --- |
| `init` | gldraw.c / Draw_ClearWindow | Retains init between calls of Draw_ClearWindow; static int init. |
| `level` | glfile.c / OutputWinding | Retains level between calls of OutputWinding; static int level = 128. |
| `numtimes` | terrain.c / EmitTerrainVerts | Retains numtimes between calls of EmitTerrainVerts; static int numtimes = 0. |

## Types

| Name | Module / record | Reason |
| --- | --- | --- |
| `double_winding_t` | brush.c / double_winding_t | Names the double winding t record used by this module. |
| `lightmapBlock_t` | lightmaps.c / lightmapBlock_s | Names the lightmap block t record used by this module. |
| `lightmapDimension_t` | lightmaps.c / lightmapDimension_t | Names the lightmap dimension t record used by this module. |
| `lightmapGroupCell_t` | lightmaps.c / lightmapGroupCell_t | Names the lightmap group cell t record used by this module. |
| `lightmapMaterial_t` | lightmaps.c / lightmapMaterial_t | Names the lightmap material t record used by this module. |
| `lightmapRef_t` | lightmaps.c / lightmapRef_s | Names the lightmap ref t record used by this module. |
| `patchLightmapProjection_t` | lightmaps.c / patchLightmapProjection_t | Names the patch lightmap projection t record used by this module. |
| `mesh_t` | mesh.h / mesh_t | Names the mesh t record used by this module. |
| `terrainPatchEntry_t` | patch.c / terrainPatchEntry_t | Names the terrain patch entry t record used by this module. |
| `cellPortal_t` | portals.c / cellPortal_s | Names the cell portal t record used by this module. |
| `bspbrush_t` | qbsp.h / bspbrush_s | Names the bspbrush t record used by this module. |
| `bspface_t` | qbsp.h / bspface_s | Names the bspface t record used by this module. |
| `cplane_t` | qbsp.h / cplane_s | Names the cplane t record used by this module. |
| `drawSurfRef_t` | qbsp.h / drawSurfRef_s | Names the draw surf ref t record used by this module. |
| `mapDrawSurface_t` | qbsp.h / drawsurf_s | Names the map draw surface t record used by this module. |
| `node_t` | qbsp.h / node_s | Names the node t record used by this module. |
| `parseMesh_t` | qbsp.h / parseMesh_s | Names the parse mesh t record used by this module. |
| `plane_t` | qbsp.h / plane_s | Names the plane t record used by this module. |
| `portal_t` | qbsp.h / portal_s | Names the portal t record used by this module. |
| `side_t` | qbsp.h / side_s | Names the side t record used by this module. |
| `tree_t` | qbsp.h / tree_t | Names the tree t record used by this module. |
| `infoParm_t` | shaders.h / infoParm_t | Names the info parm t record used by this module. |
| `shaderInfo_t` | shaders.h / shaderInfo_s | Names the shader info t record used by this module. |
| `sideRef_t` | surface.c / sideRef_t | Names the side ref t record used by this module. |
| `terrainFace_t` | terrain.c / terrainFace_s | Names the terrain face t record used by this module. |
| `terrainMesh_t` | terrain.c / terrainMesh_s | Names the terrain mesh t record used by this module. |
| `terrainSurf_t` | terrain.c / terrainSurf_s | Names the terrain surf t record used by this module. |
| `terrainVert_t` | terrain.c / terrainVert_s | Names the terrain vert t record used by this module. |
| `terrainSurface_t` | terrain_surface.h / terrainSurface_s | Names the terrain surface t record used by this module. |
| `edgeLine_t` | tjunction.c / edgeLine_s | Names the edge line t record used by this module. |
| `edgePoint_t` | tjunction.c / edgePoint_s | Names the edge point t record used by this module. |
| `originalEdge_t` | tjunction.c / originalEdge_t | Names the original edge t record used by this module. |
| `tessSplitPoint_t` | tris.c / tessSplitPoint_s | Names the tess split point t record used by this module. |
| `tjuncCellBounds_t` | tris.c / tjuncCellBounds_s | Names the tjunc cell bounds t record used by this module. |
| `tjuncEdgeLine_t` | tris.c / tjuncEdgeLine_s | Names the tjunc edge line t record used by this module. |
| `tjuncHashNode_t` | tris.c / tjuncHashNode_s | Names the tjunc hash node t record used by this module. |
| `tjuncPoint_t` | tris.c / tjuncPoint_s | Names the tjunc point t record used by this module. |
| `triGroupRecord_t` | tris.c / triGroupRecord_s | Names the tri group record t record used by this module. |
| `triIntermediateVert_t` | tris.c / triIntermediateVert_s | Names the tri intermediate vert t record used by this module. |
| `triSubgroup_t` | tris.c / triSubgroup_s | Names the tri subgroup t record used by this module. |
| `triSurfProps_t` | tris.c / triSurfProps_s | Names the tri surf props t record used by this module. |
| `triSurf_t` | tris.c / triSurf_s | Names the tri surf t record used by this module. |
| `triangleEdge_t` | tris.c / triangleEdge_s | Names the triangle edge t record used by this module. |
| `triangleIndexGroup_t` | tristrip.h / triangleIndexGroup_s | Names the triangle index group t record used by this module. |
| `leaf_t` | vis.h / leaf_s | Names the leaf t record used by this module. |
| `passage_t` | vis.h / passage_s | Names the passage t record used by this module. |
| `plane_t` | vis.h / plane_t | Names the plane t record used by this module. |
| `pstack_t` | vis.h / pstack_s | Names the pstack t record used by this module. |
| `threaddata_t` | vis.h / threaddata_t | Names the threaddata t record used by this module. |
| `vportal_t` | vis.h / vportal_t | Names the vportal t record used by this module. |
| `vstatus_t` | vis.h / vstatus_t | Names the vstatus t record used by this module. |
| `winding_t` | vis.h / winding_t | Names the winding t record used by this module. |

