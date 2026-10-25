# Shared-code reconstruction spellings

This conservative inventory discloses declarations in common/, universal/,
code/qcommon/ and code/game/, including locals and parameters. All spellings
are unconfirmed for UO unless separate binary or symbol evidence establishes
their binding. A token in published source establishes lineage, not its use
for the same role in the historical UO source.

The references are published Quake III Arena, RTCW, Enemy Territory and
GtkRadiant source. Declaration text and the containing operation explain
each descriptive name. Equal bytes constrain behavior and layout, not spelling.

## code/game/q_math.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 11 | `Q3MAP_GAME_Q_MATH_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_GAME_Q_MATH_H` |
| 16 | `Q_rand` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_rand( int *seed );` |
| 16 | `seed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_rand( int *seed );` |
| 17 | `Q_random` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float Q_random( int *seed );` |
| 17 | `seed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_random( int *seed );` |
| 18 | `AngleNormalize360` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float AngleNormalize360( float angle );` |
| 18 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize360( float angle );` |
| 19 | `AngleNormalize180` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float AngleNormalize180( float angle );` |
| 19 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize180( float angle );` |
| 20 | `PerpendicularVector` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void PerpendicularVector( vec3_t dst, const vec3_t src );` |
| 20 | `dst` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PerpendicularVector( vec3_t dst, const vec3_t src );` |
| 20 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PerpendicularVector( vec3_t dst, const vec3_t src );` |
| 21 | `RotateAroundDirection` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void RotateAroundDirection( vec3_t axis[3], float yaw );` |
| 21 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateAroundDirection( vec3_t axis[3], float yaw );` |
| 21 | `yaw` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateAroundDirection( vec3_t axis[3], float yaw );` |

## code/game/surfaceflags.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 31 | `CONTENTS_SOLID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_SOLID			1		// an eye is never valid in a solid` |
| 32 | `CONTENTS_LAVA` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_LAVA			8` |
| 33 | `CONTENTS_SLIME` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_SLIME			16` |
| 34 | `CONTENTS_WATER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_WATER			32` |
| 35 | `CONTENTS_FOG` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_FOG			64` |
| 37 | `CONTENTS_NOTTEAM1` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_NOTTEAM1		0x0080` |
| 38 | `CONTENTS_NOTTEAM2` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_NOTTEAM2		0x0100` |
| 39 | `CONTENTS_NOBOTCLIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_NOBOTCLIP		0x0200` |
| 44 | `CONTENTS_FOLIAGE` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_FOLIAGE		0x0002` |
| 45 | `CONTENTS_NONCOLLIDING` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_NONCOLLIDING	0x0004` |
| 46 | `CONTENTS_GLASS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_GLASS			0x0010` |
| 47 | `CONTENTS_CANSHOOTCLIP` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_CANSHOOTCLIP	0x0040` |
| 48 | `CONTENTS_MISSILECLIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_MISSILECLIP		0x0080` |
| 49 | `CONTENTS_VEHICLECLIP` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_VEHICLECLIP		0x0200` |
| 50 | `CONTENTS_ITEMCLIP` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_ITEMCLIP		0x0400` |
| 51 | `CONTENTS_SKY` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_SKY			0x0800` |
| 52 | `CONTENTS_AI_NOSIGHT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_AI_NOSIGHT		0x1000` |
| 53 | `CONTENTS_CLIPSHOT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_CLIPSHOT			0x2000` |
| 55 | `CONTENTS_AREAPORTAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_AREAPORTAL		0x8000` |
| 57 | `CONTENTS_PLAYERCLIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_PLAYERCLIP		0x10000` |
| 58 | `CONTENTS_MONSTERCLIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_MONSTERCLIP	0x20000` |
| 60 | `CONTENTS_TELEPORTER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_TELEPORTER		0x40000` |
| 61 | `CONTENTS_JUMPPAD` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_JUMPPAD		0x80000` |
| 62 | `CONTENTS_CLUSTERPORTAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_CLUSTERPORTAL	0x100000` |
| 63 | `CONTENTS_DONOTENTER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_DONOTENTER		0x200000` |
| 64 | `CONTENTS_BOTCLIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_BOTCLIP		0x400000` |
| 65 | `CONTENTS_MOVER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CONTENTS_MOVER			0x800000` |
| 67 | `CONTENTS_ORIGIN` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_ORIGIN			0x1000000	// removed before bsping an entity` |
| 69 | `CONTENTS_BODY` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_BODY			0x2000000	// should never be on a brush, only in game` |
| 70 | `CONTENTS_CORPSE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_CORPSE			0x4000000` |
| 71 | `CONTENTS_DETAIL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_DETAIL			0x8000000	// brushes not used for the bsp` |
| 72 | `CONTENTS_STRUCTURAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_STRUCTURAL		0x10000000	// brushes used for the bsp` |
| 73 | `CONTENTS_TRANSLUCENT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_TRANSLUCENT	0x20000000	// don't consume surface fragments inside` |
| 74 | `CONTENTS_TRIGGER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_TRIGGER		0x40000000` |
| 75 | `CONTENTS_NODROP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	CONTENTS_NODROP			0x80000000	// don't leave bodies or items (death fog, lava)` |
| 77 | `SURF_NODAMAGE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NODAMAGE			0x1		// never give falling damage` |
| 78 | `SURF_SLICK` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_SLICK				0x2		// effects game physics` |
| 79 | `SURF_SKY` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_SKY				0x4		// lighting from environment map` |
| 80 | `SURF_LADDER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_LADDER				0x8` |
| 81 | `SURF_NOIMPACT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NOIMPACT			0x10	// don't make missile explosions` |
| 82 | `SURF_NOMARKS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NOMARKS			0x20	// don't leave missile marks` |
| 83 | `SURF_FLESH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_FLESH				0x40	// make flesh sounds and effects` |
| 84 | `SURF_NODRAW` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NODRAW				0x80	// don't generate a drawsurface at all` |
| 85 | `SURF_HINT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_HINT				0x100	// make a primary bsp splitter` |
| 86 | `SURF_SKIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_SKIP				0x200	// completely ignore, allowing non-closed brushes` |
| 87 | `SURF_NOLIGHTMAP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NOLIGHTMAP			0x400	// surface doesn't need a lightmap` |
| 88 | `SURF_POINTLIGHT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_POINTLIGHT			0x800	// generate lighting info at vertexes` |
| 89 | `SURF_METALSTEPS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_METALSTEPS			0x1000	// clanking footsteps` |
| 90 | `SURF_NOSTEPS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NOSTEPS			0x2000	// no footstep sounds` |
| 91 | `SURF_NONSOLID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NONSOLID			0x4000	// don't collide against curves with this set` |
| 92 | `SURF_LIGHTFILTER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_LIGHTFILTER		0x8000	// act as a light filter during q3map -light` |
| 93 | `SURF_ALPHASHADOW` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_ALPHASHADOW		0x10000	// do per-pixel light shadow casting in q3map` |
| 94 | `SURF_NODLIGHT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SURF_NODLIGHT			0x20000	// don't dlight even if solid (solid lava, skies)` |
| 95 | `SURF_DUST` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_DUST				0x40000 // leave a dust trail when walking on this surface` |
| 96 | `SURF_CASTSHADOW` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_CASTSHADOW			0x40000	// "castshadow" in the surfaceparm table (same bit as SURF_DUST)` |
| 97 | `SURF_PORTAL` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_PORTAL				0x80000000` |
| 100 | `SURF_TYPE_SHIFT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_SHIFT			20` |
| 101 | `SURF_TYPE_MASK` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_MASK			0x01F00000` |
| 102 | `SURF_TYPE_BARK` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_BARK			( 1 << SURF_TYPE_SHIFT )` |
| 103 | `SURF_TYPE_BRICK` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_BRICK			( 2 << SURF_TYPE_SHIFT )` |
| 104 | `SURF_TYPE_CARPET` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_CARPET		( 3 << SURF_TYPE_SHIFT )` |
| 105 | `SURF_TYPE_CLOTH` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_CLOTH			( 4 << SURF_TYPE_SHIFT )` |
| 106 | `SURF_TYPE_CONCRETE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_CONCRETE		( 5 << SURF_TYPE_SHIFT )` |
| 107 | `SURF_TYPE_DIRT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_DIRT			( 6 << SURF_TYPE_SHIFT )` |
| 108 | `SURF_TYPE_FLESH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_FLESH			( 7 << SURF_TYPE_SHIFT )` |
| 109 | `SURF_TYPE_FOLIAGE` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_FOLIAGE		( 8 << SURF_TYPE_SHIFT )` |
| 110 | `SURF_TYPE_GLASS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_GLASS			( 9 << SURF_TYPE_SHIFT )` |
| 111 | `SURF_TYPE_GRASS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_GRASS			( 10 << SURF_TYPE_SHIFT )` |
| 112 | `SURF_TYPE_GRAVEL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_GRAVEL		( 11 << SURF_TYPE_SHIFT )` |
| 113 | `SURF_TYPE_ICE` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_ICE			( 12 << SURF_TYPE_SHIFT )` |
| 114 | `SURF_TYPE_METAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_METAL			( 13 << SURF_TYPE_SHIFT )` |
| 115 | `SURF_TYPE_MUD` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_MUD			( 14 << SURF_TYPE_SHIFT )` |
| 116 | `SURF_TYPE_PAPER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_PAPER			( 15 << SURF_TYPE_SHIFT )` |
| 117 | `SURF_TYPE_PLASTER` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_PLASTER		( 16 << SURF_TYPE_SHIFT )` |
| 118 | `SURF_TYPE_ROCK` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_ROCK			( 17 << SURF_TYPE_SHIFT )` |
| 119 | `SURF_TYPE_SAND` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_SAND			( 18 << SURF_TYPE_SHIFT )` |
| 120 | `SURF_TYPE_SNOW` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_SNOW			( 19 << SURF_TYPE_SHIFT )` |
| 121 | `SURF_TYPE_WATER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_WATER			( 20 << SURF_TYPE_SHIFT )` |
| 122 | `SURF_TYPE_WOOD` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_WOOD			( 21 << SURF_TYPE_SHIFT )` |
| 123 | `SURF_TYPE_ASPHALT` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_ASPHALT		( 22 << SURF_TYPE_SHIFT )` |
| 124 | `SURF_TYPE_OPAQUEGLASS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define SURF_TYPE_OPAQUEGLASS	SURF_TYPE_GLASS` |

## code/qcommon/common.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 26 | `MAX_QPATH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_QPATH 64` |
| 27 | `MAX_TOKEN_CHARS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_TOKEN_CHARS 1024` |
| 29 | `com_fullyInitialized` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int com_fullyInitialized;` |
| 36 | `Com_StringContains` | function / Com_StringContains | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_StringContains( char *str1, char *str2, int casesensitive ) {` |
| 36 | `str1` | parameter / Com_StringContains | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_StringContains( char *str1, char *str2, int casesensitive ) {` |
| 36 | `str2` | parameter / Com_StringContains | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_StringContains( char *str1, char *str2, int casesensitive ) {` |
| 36 | `casesensitive` | parameter / Com_StringContains | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_StringContains( char *str1, char *str2, int casesensitive ) {` |
| 37 | `len` | local / Com_StringContains | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len, i, j;` |
| 37 | `i` | local / Com_StringContains | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len, i, j;` |
| 37 | `j` | local / Com_StringContains | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len, i, j;` |
| 64 | `Com_Filter` | function / Com_Filter | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_Filter( char *filter, char *name, int casesensitive ) {` |
| 64 | `filter` | parameter / Com_Filter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Filter( char *filter, char *name, int casesensitive ) {` |
| 64 | `name` | parameter / Com_Filter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Filter( char *filter, char *name, int casesensitive ) {` |
| 64 | `casesensitive` | parameter / Com_Filter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Filter( char *filter, char *name, int casesensitive ) {` |
| 65 | `buf` | local / Com_Filter | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char buf[MAX_TOKEN_CHARS];` |
| 66 | `ptr` | local / Com_Filter | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *ptr;` |
| 67 | `i` | local / Com_Filter | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, found;` |
| 67 | `found` | local / Com_Filter | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, found;` |
| 136 | `Com_FilterPath` | function / Com_FilterPath | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_FilterPath( char *filter, char *name, int casesensitive ) {` |
| 136 | `filter` | parameter / Com_FilterPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_FilterPath( char *filter, char *name, int casesensitive ) {` |
| 136 | `name` | parameter / Com_FilterPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_FilterPath( char *filter, char *name, int casesensitive ) {` |
| 136 | `casesensitive` | parameter / Com_FilterPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_FilterPath( char *filter, char *name, int casesensitive ) {` |
| 137 | `i` | local / Com_FilterPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 138 | `new_filter` | local / Com_FilterPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char new_filter[MAX_QPATH];` |
| 139 | `new_name` | local / Com_FilterPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char new_name[MAX_QPATH];` |
| 165 | `Com_HashKey` | function / Com_HashKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_HashKey( char *string, int maxlen ) {` |
| 165 | `string` | parameter / Com_HashKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_HashKey( char *string, int maxlen ) {` |
| 165 | `maxlen` | parameter / Com_HashKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_HashKey( char *string, int maxlen ) {` |
| 166 | `hash` | local / Com_HashKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int hash, i;` |
| 166 | `i` | local / Com_HashKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int hash, i;` |

## code/qcommon/files.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 31 | `LittleLong` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define LittleLong( x ) ( x )` |
| 33 | `MAX_OSPATH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_OSPATH 256` |
| 34 | `MAX_SEARCH_PATHS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_SEARCH_PATHS 1024` |
| 35 | `MAX_FILEHASH_SIZE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_FILEHASH_SIZE 1024` |
| 36 | `MAX_FOUND_FILES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_FOUND_FILES 4096` |
| 38 | `fs_homepath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_homepath;` |
| 39 | `fs_debug` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_debug;` |
| 40 | `fs_gamedir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char fs_gamedir[MAX_OSPATH];` |
| 41 | `fs_ignoreLozalized` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `cvar_t *fs_ignoreLozalized;` |
| 42 | `fs_numServerPaks` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_numServerPaks;` |
| 43 | `Z_MallocInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void *Z_MallocInternal( int size );` |
| 43 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Z_MallocInternal( int size );` |
| 44 | `Z_FreeInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Z_FreeInternal( void *ptr );` |
| 44 | `ptr` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Z_FreeInternal( void *ptr );` |
| 45 | `Com_Memcpy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 45 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 45 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 45 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 46 | `Q_strncmp` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_strncmp( const char *s1, const char *s2, int n );` |
| 46 | `s1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncmp( const char *s1, const char *s2, int n );` |
| 46 | `s2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncmp( const char *s1, const char *s2, int n );` |
| 46 | `n` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncmp( const char *s1, const char *s2, int n );` |
| 47 | `va` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *va( const char *format, ... );` |
| 47 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *va( const char *format, ... );` |
| 48 | `Com_Memset` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Memset( void *dest, int val, size_t count );` |
| 48 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset( void *dest, int val, size_t count );` |
| 48 | `val` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset( void *dest, int val, size_t count );` |
| 48 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset( void *dest, int val, size_t count );` |
| 49 | `unzCloseCurrentFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzCloseCurrentFile( unzFile file );` |
| 49 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzCloseCurrentFile( unzFile file );` |
| 50 | `unzClose` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzClose( unzFile file );` |
| 50 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzClose( unzFile file );` |
| 56 | `fileData_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} fileData_t;` |
| 52 | `fileData_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `typedef struct fileData_s {` |
| 53 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *name;` |
| 54 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `void *data;` |
| 55 | `clearCallback` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `void ( *clearCallback )( struct fileData_s * );` |
| 55 | `fileData_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `void ( *clearCallback )( struct fileData_s * );` |
| 63 | `fileInPack_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} fileInPack_t;` |
| 58 | `fileInPack_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct fileInPack_s {` |
| 59 | `zipPosition` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long zipPosition;` |
| 60 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `fileData_t data;` |
| 61 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *name;` |
| 62 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct fileInPack_s *next;` |
| 62 | `fileInPack_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct fileInPack_s *next;` |
| 75 | `pack_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} pack_t;` |
| 66 | `pakFilename` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char pakFilename[MAX_OSPATH];` |
| 67 | `pakBasename` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char pakBasename[MAX_OSPATH];` |
| 68 | `pakGamename` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char pakGamename[MAX_OSPATH];` |
| 69 | `handle` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unzFile handle;` |
| 70 | `numfiles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int numfiles;` |
| 71 | `referenced` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte referenced[4];` |
| 72 | `hashSize` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int hashSize;` |
| 73 | `hashTable` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `fileInPack_t **hashTable;` |
| 74 | `buildBuffer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `fileInPack_t *buildBuffer;` |
| 80 | `fs_dirFile_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} fs_dirFile_t;` |
| 77 | `fs_dirFile_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `typedef struct fs_dirFile_s {` |
| 78 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `fileData_t data;` |
| 79 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct fs_dirFile_s *next;` |
| 79 | `fs_dirFile_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `struct fs_dirFile_s *next;` |
| 89 | `fs_dirFileList_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} fs_dirFileList_t;` |
| 82 | `fs_dirFileList_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `typedef struct fs_dirFileList_s {` |
| 83 | `dir` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char dir[MAX_OSPATH];` |
| 84 | `numFiles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int numFiles;` |
| 85 | `hashSize` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int hashSize;` |
| 86 | `hashTable` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `fs_dirFile_t **hashTable;` |
| 87 | `buildBuffer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `fs_dirFile_t *buildBuffer;` |
| 88 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct fs_dirFileList_s *next;` |
| 88 | `fs_dirFileList_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `struct fs_dirFileList_s *next;` |
| 91 | `FS_HashFileName` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `long FS_HashFileName( const char *fname, int hashSize );` |
| 91 | `fname` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `long FS_HashFileName( const char *fname, int hashSize );` |
| 91 | `hashSize` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `long FS_HashFileName( const char *fname, int hashSize );` |
| 92 | `FS_FilenameCompare` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean FS_FilenameCompare( const char *s1, const char *s2 );` |
| 92 | `s1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FilenameCompare( const char *s1, const char *s2 );` |
| 92 | `s2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FilenameCompare( const char *s1, const char *s2 );` |
| 97 | `directory_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} directory_t;` |
| 95 | `path` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char path[MAX_OSPATH];` |
| 96 | `gamedir` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char gamedir[MAX_OSPATH];` |
| 105 | `searchpath_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} searchpath_t;` |
| 99 | `searchpath_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct searchpath_s {` |
| 100 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct searchpath_s *next;` |
| 100 | `searchpath_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct searchpath_s *next;` |
| 101 | `pack` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `pack_t *pack;` |
| 102 | `dir` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `directory_t *dir;` |
| 103 | `localized` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean localized;` |
| 104 | `language` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int language;` |
| 107 | `fs_searchpaths` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `searchpath_t *fs_searchpaths = 0;` |
| 108 | `fs_dirFileLists` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `fs_dirFileList_t *fs_dirFileLists = 0;` |
| 109 | `FS_UseSearchPath` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `qboolean FS_UseSearchPath( searchpath_t *search );` |
| 109 | `search` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_UseSearchPath( searchpath_t *search );` |
| 110 | `FS_PakIsPure` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean FS_PakIsPure( pack_t *pack );` |
| 110 | `pack` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_PakIsPure( pack_t *pack );` |
| 112 | `FS_HandleForFileStreamed` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `fileHandle_t FS_HandleForFileStreamed( int streamed );` |
| 112 | `streamed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileHandle_t FS_HandleForFileStreamed( int streamed );` |
| 114 | `FS_BuildOSPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path );` |
| 114 | `base` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path );` |
| 114 | `game` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path );` |
| 114 | `qpath` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path );` |
| 114 | `fs_path` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path );` |
| 115 | `FS_CreatePath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean FS_CreatePath( char *OSPath );` |
| 115 | `OSPath` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_CreatePath( char *OSPath );` |
| 116 | `Q_strncpyz` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 116 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 116 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 116 | `destsize` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 117 | `Sys_Mkdir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Sys_Mkdir( const char *path );` |
| 117 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Sys_Mkdir( const char *path );` |
| 119 | `fsh` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `fileHandleData_t fsh[MAX_FILE_HANDLES];` |
| 120 | `fs_loadStack` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_loadStack;` |
| 122 | `FS_FOpenFileRead` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int FS_FOpenFileRead( const char *filename, fileHandle_t *file, qboolean uniqueFILE );` |
| 122 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileRead( const char *filename, fileHandle_t *file, qboolean uniqueFILE );` |
| 122 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileRead( const char *filename, fileHandle_t *file, qboolean uniqueFILE );` |
| 122 | `uniqueFILE` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileRead( const char *filename, fileHandle_t *file, qboolean uniqueFILE );` |
| 123 | `Hunk_AllocateTempMemoryInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void *Hunk_AllocateTempMemoryInternal( int size );` |
| 123 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocateTempMemoryInternal( int size );` |
| 124 | `Hunk_FreeTempMemory` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Hunk_FreeTempMemory( void *buffer );` |
| 124 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Hunk_FreeTempMemory( void *buffer );` |
| 125 | `FS_FileForHandle` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `FILE *FS_FileForHandle( fileHandle_t f );` |
| 125 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `FILE *FS_FileForHandle( fileHandle_t f );` |
| 127 | `com_fullyInitialized` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int com_fullyInitialized;` |
| 128 | `fs_copyfiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_copyfiles;` |
| 129 | `fs_cdpath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_cdpath;` |
| 130 | `fs_basepath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_basepath;` |
| 131 | `fs_restrict` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_restrict;` |
| 132 | `FS_CopyFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_CopyFile( char *fromOSPath, char *toOSPath );` |
| 132 | `fromOSPath` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_CopyFile( char *fromOSPath, char *toOSPath );` |
| 132 | `toOSPath` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_CopyFile( char *fromOSPath, char *toOSPath );` |
| 133 | `fs_loadingModeNum` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int fs_loadingModeNum;` |
| 134 | `fs_fakeChkSum` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_fakeChkSum;` |
| 135 | `unzReOpen` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `unzFile unzReOpen( const char *path, unzFile file );` |
| 135 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unzFile unzReOpen( const char *path, unzFile file );` |
| 135 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unzFile unzReOpen( const char *path, unzFile file );` |
| 136 | `unzSetCurrentFileInfoPosition` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzSetCurrentFileInfoPosition( unzFile file, unsigned long position );` |
| 136 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzSetCurrentFileInfoPosition( unzFile file, unsigned long position );` |
| 136 | `position` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzSetCurrentFileInfoPosition( unzFile file, unsigned long position );` |
| 137 | `unzOpenCurrentFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzOpenCurrentFile( unzFile file );` |
| 137 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzOpenCurrentFile( unzFile file );` |
| 138 | `FS_UseSearchPath` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `qboolean FS_UseSearchPath( searchpath_t *search );` |
| 138 | `search` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_UseSearchPath( searchpath_t *search );` |
| 139 | `FS_filelength` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int FS_filelength( fileHandle_t f );` |
| 139 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_filelength( fileHandle_t f );` |
| 141 | `CopyStringInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `char *CopyStringInternal( const char *in );` |
| 141 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *CopyStringInternal( const char *in );` |
| 142 | `Com_FilterPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean Com_FilterPath( const char *filter, const char *name, int casesensitive );` |
| 142 | `filter` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Com_FilterPath( const char *filter, const char *name, int casesensitive );` |
| 142 | `name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Com_FilterPath( const char *filter, const char *name, int casesensitive );` |
| 142 | `casesensitive` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Com_FilterPath( const char *filter, const char *name, int casesensitive );` |
| 143 | `Q_stricmpn` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 143 | `s1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 143 | `s2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 143 | `n` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 144 | `fs_restrict` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern cvar_t *fs_restrict;` |
| 145 | `Sys_ListFiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char **Sys_ListFiles( const char *directory, const char *extension,` |
| 145 | `directory` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **Sys_ListFiles( const char *directory, const char *extension,` |
| 145 | `extension` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **Sys_ListFiles( const char *directory, const char *extension,` |
| 146 | `filter` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles, int wantsubs );` |
| 146 | `numfiles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles, int wantsubs );` |
| 146 | `wantsubs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles, int wantsubs );` |
| 147 | `Sys_FreeFileList` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Sys_FreeFileList( char **list );` |
| 147 | `list` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Sys_FreeFileList( char **list );` |
| 149 | `unzOpen` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `unzFile unzOpen( const char *filename );` |
| 149 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unzFile unzOpen( const char *filename );` |
| 150 | `unzGetGlobalInfo` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzGetGlobalInfo( unzFile file, unz_global_info *info );` |
| 150 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetGlobalInfo( unzFile file, unz_global_info *info );` |
| 150 | `info` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetGlobalInfo( unzFile file, unz_global_info *info );` |
| 151 | `unzGoToFirstFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzGoToFirstFile( unzFile file );` |
| 151 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGoToFirstFile( unzFile file );` |
| 152 | `unzGoToNextFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzGoToNextFile( unzFile file );` |
| 152 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGoToNextFile( unzFile file );` |
| 153 | `unzGetCurrentFileInfo` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info, char *filename,` |
| 153 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info, char *filename,` |
| 153 | `info` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info, char *filename,` |
| 153 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info, char *filename,` |
| 154 | `filenameSize` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `unsigned long filenameSize, void *extra, unsigned long extraSize,` |
| 154 | `extra` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned long filenameSize, void *extra, unsigned long extraSize,` |
| 154 | `extraSize` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `unsigned long filenameSize, void *extra, unsigned long extraSize,` |
| 155 | `comment` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *comment, unsigned long commentSize );` |
| 155 | `commentSize` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *comment, unsigned long commentSize );` |
| 156 | `unzGetCurrentFileInfoPosition` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzGetCurrentFileInfoPosition( unzFile file, unsigned long *position );` |
| 156 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfoPosition( unzFile file, unsigned long *position );` |
| 156 | `position` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfoPosition( unzFile file, unsigned long *position );` |
| 157 | `Q_strlwr` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *Q_strlwr( char *s );` |
| 157 | `s` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Q_strlwr( char *s );` |
| 158 | `fs_packFiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_packFiles = 0;` |
| 160 | `Sys_ListFiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char **Sys_ListFiles( const char *directory, const char *extension,` |
| 160 | `directory` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **Sys_ListFiles( const char *directory, const char *extension,` |
| 160 | `extension` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **Sys_ListFiles( const char *directory, const char *extension,` |
| 161 | `filter` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles, int wantsubs );` |
| 161 | `numfiles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles, int wantsubs );` |
| 161 | `wantsubs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles, int wantsubs );` |
| 162 | `Sys_FreeFileList` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Sys_FreeFileList( char **list );` |
| 162 | `list` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Sys_FreeFileList( char **list );` |
| 164 | `fs_checksumFeed` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_checksumFeed;` |
| 165 | `lastValidBase` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char lastValidBase[MAX_OSPATH];` |
| 166 | `lastValidGame` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char lastValidGame[MAX_OSPATH];` |
| 167 | `fs_currentLevelGame` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `char fs_currentLevelGame[MAX_OSPATH];` |
| 168 | `fs_basepath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern cvar_t *fs_basepath;` |
| 169 | `fs_gamedirvar` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_gamedirvar;` |
| 170 | `FS_Startup` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_Startup( const char *gameName );` |
| 170 | `gameName` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Startup( const char *gameName );` |
| 171 | `FS_Shutdown` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_Shutdown( qboolean closemfp );` |
| 171 | `closemfp` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Shutdown( qboolean closemfp );` |
| 178 | `fsMode_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} fsMode_t;` |
| 174 | `FS_READ` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `FS_READ,` |
| 175 | `FS_WRITE` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `FS_WRITE,` |
| 176 | `FS_APPEND` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `FS_APPEND,` |
| 177 | `FS_APPEND_SYNC` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `FS_APPEND_SYNC` |
| 180 | `FS_UNSET_FILE_LENGTH` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define FS_UNSET_FILE_LENGTH 6969` |
| 181 | `unztell` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `long unztell( unzFile file );` |
| 181 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `long unztell( unzFile file );` |
| 183 | `CVAR_SYSTEMINFO` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_SYSTEMINFO 8` |
| 184 | `fs_copyfiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern cvar_t *fs_copyfiles;` |
| 185 | `fs_cdpath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern cvar_t *fs_cdpath;` |
| 186 | `fs_basegame` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *fs_basegame;` |
| 187 | `Sys_DefaultCDPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const char *Sys_DefaultCDPath( void );` |
| 188 | `Sys_DefaultInstallPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const char *Sys_DefaultInstallPath( void );` |
| 189 | `Sys_DefaultHomePath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const char *Sys_DefaultHomePath( void );` |
| 190 | `Sys_DirectoryHasContents` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `qboolean Sys_DirectoryHasContents( const char *path );` |
| 190 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Sys_DirectoryHasContents( const char *path );` |
| 191 | `FS_DisplayPath` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void FS_DisplayPath( qboolean showAll );` |
| 191 | `showAll` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_DisplayPath( qboolean showAll );` |
| 194 | `fs_serverPaks` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_serverPaks[MAX_SERVER_PAKS];` |
| 195 | `fs_serverPakNames` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *fs_serverPakNames[MAX_SERVER_PAKS];` |
| 196 | `fs_numServerReferencedPaks` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_numServerReferencedPaks;` |
| 197 | `fs_serverReferencedPaks` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int fs_serverReferencedPaks[MAX_SERVER_PAKS];` |
| 198 | `fs_serverReferencedPakNames` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *fs_serverReferencedPakNames[MAX_SERVER_PAKS];` |
| 200 | `FS_SEEK_CUR` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define FS_SEEK_CUR 0` |
| 201 | `FS_SEEK_END` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define FS_SEEK_END 1` |
| 202 | `FS_SEEK_SET` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define FS_SEEK_SET 2` |
| 209 | `FS_Initialized` | function / FS_Initialized | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_Initialized( void ) {` |
| 218 | `FS_CheckFileSystemStarted` | function / FS_CheckFileSystemStarted | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_CheckFileSystemStarted( void ) {` |
| 229 | `FS_PakIsPure` | function / FS_PakIsPure | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_PakIsPure( pack_t *pack ) {` |
| 229 | `pack` | parameter / FS_PakIsPure | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_PakIsPure( pack_t *pack ) {` |
| 239 | `FS_LoadStack` | function / FS_LoadStack | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_LoadStack( void ) {` |
| 248 | `FS_UseSearchPath` | function / FS_UseSearchPath | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_UseSearchPath( searchpath_t *search ) {` |
| 248 | `search` | parameter / FS_UseSearchPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_UseSearchPath( searchpath_t *search ) {` |
| 260 | `FS_LanguageHasAssets` | function / FS_LanguageHasAssets | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_LanguageHasAssets( int language ) {` |
| 260 | `language` | parameter / FS_LanguageHasAssets | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_LanguageHasAssets( int language ) {` |
| 261 | `sp` | local / FS_LanguageHasAssets | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *sp;` |
| 276 | `FS_HashFileName` | function / FS_HashFileName | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `long FS_HashFileName( const char *fname, int hashSize ) {` |
| 276 | `fname` | parameter / FS_HashFileName | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `long FS_HashFileName( const char *fname, int hashSize ) {` |
| 276 | `hashSize` | parameter / FS_HashFileName | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `long FS_HashFileName( const char *fname, int hashSize ) {` |
| 277 | `i` | local / FS_HashFileName | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 278 | `hash` | local / FS_HashFileName | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 279 | `letter` | local / FS_HashFileName | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int letter;` |
| 304 | `FS_HandleForFileStreamed` | function / FS_HandleForFileStreamed | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `fileHandle_t FS_HandleForFileStreamed( int streamed ) {` |
| 304 | `streamed` | parameter / FS_HandleForFileStreamed | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileHandle_t FS_HandleForFileStreamed( int streamed ) {` |
| 305 | `i` | local / FS_HandleForFileStreamed | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 306 | `start` | local / FS_HandleForFileStreamed | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int start, count;` |
| 306 | `count` | local / FS_HandleForFileStreamed | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int start, count;` |
| 332 | `FS_FileForHandle` | function / FS_FileForHandle | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `FILE *FS_FileForHandle( fileHandle_t f ) {` |
| 332 | `f` | parameter / FS_FileForHandle | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `FILE *FS_FileForHandle( fileHandle_t f ) {` |
| 341 | `FS_ForceFlush` | function / FS_ForceFlush | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ForceFlush( fileHandle_t f ) {` |
| 341 | `f` | parameter / FS_ForceFlush | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_ForceFlush( fileHandle_t f ) {` |
| 342 | `file` | local / FS_ForceFlush | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *file;` |
| 357 | `FS_filelength` | function / FS_filelength | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_filelength( fileHandle_t f ) {` |
| 357 | `f` | parameter / FS_filelength | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_filelength( fileHandle_t f ) {` |
| 358 | `h` | local / FS_filelength | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *h;` |
| 359 | `pos` | local / FS_filelength | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int pos, end;` |
| 359 | `end` | local / FS_filelength | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int pos, end;` |
| 380 | `FS_ReplaceSeparators` | function / FS_ReplaceSeparators | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_ReplaceSeparators( char *path ) {` |
| 380 | `path` | parameter / FS_ReplaceSeparators | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_ReplaceSeparators( char *path ) {` |
| 381 | `s` | local / FS_ReplaceSeparators | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 395 | `FS_BuildOSPath3` | function / FS_BuildOSPath3 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_BuildOSPath3( const char *base, const char *game, const char *qpath,` |
| 395 | `base` | parameter / FS_BuildOSPath3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_BuildOSPath3( const char *base, const char *game, const char *qpath,` |
| 395 | `game` | parameter / FS_BuildOSPath3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_BuildOSPath3( const char *base, const char *game, const char *qpath,` |
| 395 | `qpath` | parameter / FS_BuildOSPath3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_BuildOSPath3( const char *base, const char *game, const char *qpath,` |
| 396 | `fs_path` | parameter / FS_BuildOSPath3 | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *fs_path, int allowOverflow ) {` |
| 396 | `allowOverflow` | parameter / FS_BuildOSPath3 | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *fs_path, int allowOverflow ) {` |
| 397 | `baseLen` | local / FS_BuildOSPath3 | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int baseLen, gameLen, qLen;` |
| 397 | `gameLen` | local / FS_BuildOSPath3 | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int baseLen, gameLen, qLen;` |
| 397 | `qLen` | local / FS_BuildOSPath3 | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int baseLen, gameLen, qLen;` |
| 420 | `FS_NoOp` | function / FS_NoOp | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_NoOp( void ) {` |
| 430 | `FS_BuildOSPath` | function / FS_BuildOSPath | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path ) {` |
| 430 | `base` | parameter / FS_BuildOSPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path ) {` |
| 430 | `game` | parameter / FS_BuildOSPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path ) {` |
| 430 | `qpath` | parameter / FS_BuildOSPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path ) {` |
| 430 | `fs_path` | parameter / FS_BuildOSPath | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_BuildOSPath( const char *base, const char *game, const char *qpath, char *fs_path ) {` |
| 441 | `FS_CreatePath` | function / FS_CreatePath | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_CreatePath( char *OSPath ) {` |
| 441 | `OSPath` | parameter / FS_CreatePath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_CreatePath( char *OSPath ) {` |
| 442 | `ofs` | local / FS_CreatePath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *ofs;` |
| 465 | `FS_CopyFile` | function / FS_CopyFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_CopyFile( char *fromOSPath, char *toOSPath ) {` |
| 465 | `fromOSPath` | parameter / FS_CopyFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_CopyFile( char *fromOSPath, char *toOSPath ) {` |
| 465 | `toOSPath` | parameter / FS_CopyFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_CopyFile( char *fromOSPath, char *toOSPath ) {` |
| 466 | `f` | local / FS_CopyFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *f;` |
| 467 | `len` | local / FS_CopyFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 468 | `buf` | local / FS_CopyFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf;` |
| 506 | `FS_CopyFiles` | function / FS_CopyFiles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_CopyFiles( const char *fromDir, const char *toDir, const char *ext ) {` |
| 506 | `fromDir` | parameter / FS_CopyFiles | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_CopyFiles( const char *fromDir, const char *toDir, const char *ext ) {` |
| 506 | `toDir` | parameter / FS_CopyFiles | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_CopyFiles( const char *fromDir, const char *toDir, const char *ext ) {` |
| 506 | `ext` | parameter / FS_CopyFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_CopyFiles( const char *fromDir, const char *toDir, const char *ext ) {` |
| 507 | `fromOSPath` | local / FS_CopyFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char fromOSPath[MAX_OSPATH];` |
| 508 | `toOSPath` | local / FS_CopyFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char toOSPath[MAX_OSPATH];` |
| 509 | `f` | local / FS_CopyFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *f;` |
| 510 | `len` | local / FS_CopyFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 511 | `buf` | local / FS_CopyFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf;` |
| 553 | `FS_Remove` | function / FS_Remove | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Remove( const char *osPath ) {` |
| 553 | `osPath` | parameter / FS_Remove | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Remove( const char *osPath ) {` |
| 567 | `FS_FileExists` | function / FS_FileExists | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_FileExists( const char *file ) {` |
| 567 | `file` | parameter / FS_FileExists | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FileExists( const char *file ) {` |
| 568 | `f` | local / FS_FileExists | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *f;` |
| 569 | `testpath` | local / FS_FileExists | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char testpath[MAX_OSPATH];` |
| 586 | `FS_Rename` | function / FS_Rename | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Rename( const char *from, const char *to ) {` |
| 586 | `from` | parameter / FS_Rename | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Rename( const char *from, const char *to ) {` |
| 586 | `to` | parameter / FS_Rename | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Rename( const char *from, const char *to ) {` |
| 587 | `fromOSPath` | local / FS_Rename | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char fromOSPath[MAX_OSPATH];` |
| 588 | `toOSPath` | local / FS_Rename | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char toOSPath[MAX_OSPATH];` |
| 615 | `FS_FCloseFile` | function / FS_FCloseFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_FCloseFile( fileHandle_t f ) {` |
| 615 | `f` | parameter / FS_FCloseFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_FCloseFile( fileHandle_t f ) {` |
| 637 | `FS_FOpenFileWrite` | function / FS_FOpenFileWrite | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `fileHandle_t FS_FOpenFileWrite( const char *filename ) {` |
| 637 | `filename` | parameter / FS_FOpenFileWrite | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileHandle_t FS_FOpenFileWrite( const char *filename ) {` |
| 638 | `f` | local / FS_FOpenFileWrite | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileHandle_t f;` |
| 639 | `ospath` | local / FS_FOpenFileWrite | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char ospath[MAX_OSPATH];` |
| 665 | `FS_FOpenTextFileWrite` | function / FS_FOpenTextFileWrite | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `fileHandle_t FS_FOpenTextFileWrite( const char *filename ) {` |
| 665 | `filename` | parameter / FS_FOpenTextFileWrite | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileHandle_t FS_FOpenTextFileWrite( const char *filename ) {` |
| 666 | `f` | local / FS_FOpenTextFileWrite | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileHandle_t f;` |
| 667 | `ospath` | local / FS_FOpenTextFileWrite | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char ospath[MAX_OSPATH];` |
| 694 | `FS_FOpenFileAppend` | function / FS_FOpenFileAppend | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `fileHandle_t FS_FOpenFileAppend( const char *filename ) {` |
| 694 | `filename` | parameter / FS_FOpenFileAppend | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileHandle_t FS_FOpenFileAppend( const char *filename ) {` |
| 695 | `f` | local / FS_FOpenFileAppend | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileHandle_t f;` |
| 696 | `ospath` | local / FS_FOpenFileAppend | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char ospath[MAX_OSPATH];` |
| 724 | `FS_FilenameCompare` | function / FS_FilenameCompare | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_FilenameCompare( const char *s1, const char *s2 ) {` |
| 724 | `s1` | parameter / FS_FilenameCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FilenameCompare( const char *s1, const char *s2 ) {` |
| 724 | `s2` | parameter / FS_FilenameCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FilenameCompare( const char *s1, const char *s2 ) {` |
| 725 | `c1` | local / FS_FilenameCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 725 | `c2` | local / FS_FilenameCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 756 | `FS_FileCompare` | function / FS_FileCompare | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_FileCompare( const char *s1, const char *s2 ) {` |
| 756 | `s1` | parameter / FS_FileCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FileCompare( const char *s1, const char *s2 ) {` |
| 756 | `s2` | parameter / FS_FileCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_FileCompare( const char *s1, const char *s2 ) {` |
| 757 | `f1` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *f1, *f2;` |
| 757 | `f2` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *f1, *f2;` |
| 758 | `len1` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len1, len2, pos, i;` |
| 758 | `len2` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len1, len2, pos, i;` |
| 758 | `pos` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len1, len2, pos, i;` |
| 758 | `i` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len1, len2, pos, i;` |
| 759 | `buf1` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf1, *buf2, *p1, *p2;` |
| 759 | `buf2` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf1, *buf2, *p1, *p2;` |
| 759 | `p1` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf1, *buf2, *p1, *p2;` |
| 759 | `p2` | local / FS_FileCompare | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf1, *buf2, *p1, *p2;` |
| 810 | `FS_ShiftedStrStr` | function / FS_ShiftedStrStr | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *FS_ShiftedStrStr( const char *string, const char *substring, int shift ) {` |
| 810 | `string` | parameter / FS_ShiftedStrStr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *FS_ShiftedStrStr( const char *string, const char *substring, int shift ) {` |
| 810 | `substring` | parameter / FS_ShiftedStrStr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *FS_ShiftedStrStr( const char *string, const char *substring, int shift ) {` |
| 810 | `shift` | parameter / FS_ShiftedStrStr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *FS_ShiftedStrStr( const char *string, const char *substring, int shift ) {` |
| 811 | `buf` | local / FS_ShiftedStrStr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char buf[MAX_OSPATH];` |
| 812 | `i` | local / FS_ShiftedStrStr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 826 | `FS_GetExtensionSubString` | function / FS_GetExtensionSubString | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `const char *FS_GetExtensionSubString( const char *name ) {` |
| 826 | `name` | parameter / FS_GetExtensionSubString | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *FS_GetExtensionSubString( const char *name ) {` |
| 827 | `extension` | local / FS_GetExtensionSubString | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *extension;` |
| 846 | `FS_PureIgnoresExtension` | function / FS_PureIgnoresExtension | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_PureIgnoresExtension( const char *extension ) {` |
| 846 | `extension` | parameter / FS_PureIgnoresExtension | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_PureIgnoresExtension( const char *extension ) {` |
| 867 | `FS_FOpenFileRead_Internal` | function / FS_FOpenFileRead_Internal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int FS_FOpenFileRead_Internal( const char *qpath, fileHandle_t *file,` |
| 867 | `qpath` | parameter / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_FOpenFileRead_Internal( const char *qpath, fileHandle_t *file,` |
| 867 | `file` | parameter / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_FOpenFileRead_Internal( const char *qpath, fileHandle_t *file,` |
| 868 | `uniqueFILE` | parameter / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean uniqueFILE, int filter_flag ) {` |
| 868 | `filter_flag` | parameter / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean uniqueFILE, int filter_flag ) {` |
| 869 | `search` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 870 | `pak` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `pack_t *pak;` |
| 871 | `pakFile` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileInPack_t *pakFile;` |
| 872 | `dir` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `directory_t *dir;` |
| 873 | `hash` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 874 | `netpath` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char netpath[MAX_OSPATH];` |
| 875 | `copyPath` | local / FS_FOpenFileRead_Internal | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char copyPath[MAX_OSPATH];` |
| 876 | `len` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 877 | `zfi` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *zfi;` |
| 877 | `unz_s` | tag / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *zfi;` |
| 878 | `temp` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *temp;` |
| 879 | `extension` | local / FS_FOpenFileRead_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *extension;` |
| 1024 | `FS_FOpenFileReadStream` | function / FS_FOpenFileReadStream | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_FOpenFileReadStream( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1024 | `qpath` | parameter / FS_FOpenFileReadStream | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileReadStream( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1024 | `file` | parameter / FS_FOpenFileReadStream | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileReadStream( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1024 | `uniqueFILE` | parameter / FS_FOpenFileReadStream | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileReadStream( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1038 | `FS_FOpenFileRead` | function / FS_FOpenFileRead | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_FOpenFileRead( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1038 | `qpath` | parameter / FS_FOpenFileRead | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileRead( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1038 | `file` | parameter / FS_FOpenFileRead | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileRead( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1038 | `uniqueFILE` | parameter / FS_FOpenFileRead | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileRead( const char *qpath, fileHandle_t *file, qboolean uniqueFILE ) {` |
| 1048 | `FS_TouchFile` | function / FS_TouchFile | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_TouchFile( const char *qpath ) {` |
| 1048 | `qpath` | parameter / FS_TouchFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_TouchFile( const char *qpath ) {` |
| 1049 | `f` | local / FS_TouchFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileHandle_t f;` |
| 1064 | `FS_ShortOSFilePath` | function / FS_ShortOSFilePath | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *FS_ShortOSFilePath( const char *fullpath ) {` |
| 1064 | `fullpath` | parameter / FS_ShortOSFilePath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *FS_ShortOSFilePath( const char *fullpath ) {` |
| 1065 | `search` | local / FS_ShortOSFilePath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 1066 | `dir` | local / FS_ShortOSFilePath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `directory_t *dir;` |
| 1067 | `file` | local / FS_ShortOSFilePath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *file;` |
| 1068 | `netpath` | local / FS_ShortOSFilePath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char netpath[MAX_OSPATH];` |
| 1094 | `FS_Delete` | function / FS_Delete | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_Delete( const char *filename ) {` |
| 1094 | `filename` | parameter / FS_Delete | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Delete( const char *filename ) {` |
| 1095 | `osPath` | local / FS_Delete | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char osPath[MAX_OSPATH];` |
| 1096 | `c` | local / FS_Delete | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c;` |
| 1116 | `FS_MakeReadOnly` | function / FS_MakeReadOnly | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_MakeReadOnly( const char *filename, qboolean readOnly ) {` |
| 1116 | `filename` | parameter / FS_MakeReadOnly | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_MakeReadOnly( const char *filename, qboolean readOnly ) {` |
| 1116 | `readOnly` | parameter / FS_MakeReadOnly | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `qboolean FS_MakeReadOnly( const char *filename, qboolean readOnly ) {` |
| 1117 | `osPath` | local / FS_MakeReadOnly | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char osPath[MAX_OSPATH];` |
| 1118 | `attr` | local / FS_MakeReadOnly | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `DWORD attr, newAttr;` |
| 1118 | `newAttr` | local / FS_MakeReadOnly | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `DWORD attr, newAttr;` |
| 1142 | `FS_Read` | function / FS_Read | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_Read( void *buffer, int len, fileHandle_t f ) {` |
| 1142 | `buffer` | parameter / FS_Read | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Read( void *buffer, int len, fileHandle_t f ) {` |
| 1142 | `len` | parameter / FS_Read | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Read( void *buffer, int len, fileHandle_t f ) {` |
| 1142 | `f` | parameter / FS_Read | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Read( void *buffer, int len, fileHandle_t f ) {` |
| 1143 | `block` | local / FS_Read | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int block, remaining;` |
| 1143 | `remaining` | local / FS_Read | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int block, remaining;` |
| 1144 | `read` | local / FS_Read | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int read;` |
| 1145 | `buf` | local / FS_Read | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf;` |
| 1146 | `tries` | local / FS_Read | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int tries;` |
| 1186 | `FS_Write` | function / FS_Write | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_Write( const void *buffer, int len, fileHandle_t f ) {` |
| 1186 | `buffer` | parameter / FS_Write | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Write( const void *buffer, int len, fileHandle_t f ) {` |
| 1186 | `len` | parameter / FS_Write | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Write( const void *buffer, int len, fileHandle_t f ) {` |
| 1186 | `f` | parameter / FS_Write | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Write( const void *buffer, int len, fileHandle_t f ) {` |
| 1187 | `remaining` | local / FS_Write | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int remaining, written, tries;` |
| 1187 | `written` | local / FS_Write | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int remaining, written, tries;` |
| 1187 | `tries` | local / FS_Write | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int remaining, written, tries;` |
| 1188 | `buf` | local / FS_Write | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const byte *buf;` |
| 1189 | `file` | local / FS_Write | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *file;` |
| 1225 | `FS_Printf` | function / FS_Printf | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Printf( fileHandle_t f, const char *fmt, ... ) {` |
| 1225 | `f` | parameter / FS_Printf | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Printf( fileHandle_t f, const char *fmt, ... ) {` |
| 1225 | `fmt` | parameter / FS_Printf | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Printf( fileHandle_t f, const char *fmt, ... ) {` |
| 1226 | `argptr` | local / FS_Printf | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `va_list argptr;` |
| 1227 | `msg` | local / FS_Printf | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char msg[4096];` |
| 1242 | `FS_Seek` | function / FS_Seek | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_Seek( fileHandle_t f, int offset, int origin ) {` |
| 1242 | `f` | parameter / FS_Seek | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Seek( fileHandle_t f, int offset, int origin ) {` |
| 1242 | `offset` | parameter / FS_Seek | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Seek( fileHandle_t f, int offset, int origin ) {` |
| 1242 | `origin` | parameter / FS_Seek | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Seek( fileHandle_t f, int offset, int origin ) {` |
| 1243 | `buffer` | local / FS_Seek | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte buffer[65536];` |
| 1244 | `remaining` | local / FS_Seek | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int remaining, read;` |
| 1244 | `read` | local / FS_Seek | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int remaining, read;` |
| 1245 | `pos` | local / FS_Seek | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int pos;` |
| 1246 | `fseek_origin` | local / FS_Seek | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int fseek_origin;` |
| 1305 | `file` | local / FS_Seek | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *file = FS_FileForHandle( f );` |
| 1331 | `FS_ReadFile` | function / FS_ReadFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_ReadFile( const char *qpath, void **buffer ) {` |
| 1331 | `qpath` | parameter / FS_ReadFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_ReadFile( const char *qpath, void **buffer ) {` |
| 1331 | `buffer` | parameter / FS_ReadFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_ReadFile( const char *qpath, void **buffer ) {` |
| 1332 | `h` | local / FS_ReadFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileHandle_t h;` |
| 1333 | `buf` | local / FS_ReadFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf;` |
| 1334 | `len` | local / FS_ReadFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 1335 | `isConfig` | local / FS_ReadFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean isConfig;` |
| 1369 | `FS_ResetFiles` | function / FS_ResetFiles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ResetFiles( void ) {` |
| 1378 | `FS_FreeFile` | function / FS_FreeFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_FreeFile( void *buffer ) {` |
| 1378 | `buffer` | parameter / FS_FreeFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_FreeFile( void *buffer ) {` |
| 1394 | `FS_WriteFile` | function / FS_WriteFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_WriteFile( const char *qpath, const void *buffer, int size ) {` |
| 1394 | `qpath` | parameter / FS_WriteFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_WriteFile( const char *qpath, const void *buffer, int size ) {` |
| 1394 | `buffer` | parameter / FS_WriteFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_WriteFile( const char *qpath, const void *buffer, int size ) {` |
| 1394 | `size` | parameter / FS_WriteFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_WriteFile( const char *qpath, const void *buffer, int size ) {` |
| 1395 | `f` | local / FS_WriteFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileHandle_t f;` |
| 1418 | `FS_LoadZipFile` | function / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static pack_t *FS_LoadZipFile( char *zipfile, const char *basename ) {` |
| 1418 | `zipfile` | parameter / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static pack_t *FS_LoadZipFile( char *zipfile, const char *basename ) {` |
| 1418 | `basename` | parameter / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static pack_t *FS_LoadZipFile( char *zipfile, const char *basename ) {` |
| 1419 | `pack` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `pack_t *pack;` |
| 1420 | `uf` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unzFile uf;` |
| 1421 | `gi` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_global_info gi;` |
| 1422 | `info` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_file_info info;` |
| 1423 | `i` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, len, k, headerLen;` |
| 1423 | `len` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, len, k, headerLen;` |
| 1423 | `k` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, len, k, headerLen;` |
| 1423 | `headerLen` | local / FS_LoadZipFile | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int i, len, k, headerLen;` |
| 1424 | `buildBuffer` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileInPack_t *buildBuffer;` |
| 1425 | `namePtr` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *namePtr;` |
| 1426 | `filename` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char filename[MAX_ZPATH];` |
| 1427 | `headerLongs` | local / FS_LoadZipFile | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int *headerLongs;` |
| 1428 | `hash` | local / FS_LoadZipFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 1501 | `FS_ReturnPath` | function / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int FS_ReturnPath( const char *zname, char *zpath, int *depth ) {` |
| 1501 | `zname` | parameter / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_ReturnPath( const char *zname, char *zpath, int *depth ) {` |
| 1501 | `zpath` | parameter / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_ReturnPath( const char *zname, char *zpath, int *depth ) {` |
| 1501 | `depth` | parameter / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_ReturnPath( const char *zname, char *zpath, int *depth ) {` |
| 1502 | `len` | local / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len, at, newdep;` |
| 1502 | `at` | local / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len, at, newdep;` |
| 1502 | `newdep` | local / FS_ReturnPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len, at, newdep;` |
| 1529 | `FS_AddFileToList` | function / FS_AddFileToList | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int FS_AddFileToList( const char *name, char *list[MAX_FOUND_FILES], int nfiles ) {` |
| 1529 | `name` | parameter / FS_AddFileToList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_AddFileToList( const char *name, char *list[MAX_FOUND_FILES], int nfiles ) {` |
| 1529 | `list` | parameter / FS_AddFileToList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_AddFileToList( const char *name, char *list[MAX_FOUND_FILES], int nfiles ) {` |
| 1529 | `nfiles` | parameter / FS_AddFileToList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int FS_AddFileToList( const char *name, char *list[MAX_FOUND_FILES], int nfiles ) {` |
| 1530 | `i` | local / FS_AddFileToList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1552 | `FS_ListFilteredFiles` | function / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char **FS_ListFilteredFiles( const char *path, const char *extension,` |
| 1552 | `path` | parameter / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFilteredFiles( const char *path, const char *extension,` |
| 1552 | `extension` | parameter / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFilteredFiles( const char *path, const char *extension,` |
| 1553 | `filter` | parameter / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles ) {` |
| 1553 | `numfiles` | parameter / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *filter, int *numfiles ) {` |
| 1554 | `nfiles` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nfiles, i, pathLength, extensionLength;` |
| 1554 | `i` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nfiles, i, pathLength, extensionLength;` |
| 1554 | `pathLength` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nfiles, i, pathLength, extensionLength;` |
| 1554 | `extensionLength` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nfiles, i, pathLength, extensionLength;` |
| 1555 | `length` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int length, pathDepth, temp;` |
| 1555 | `pathDepth` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int length, pathDepth, temp;` |
| 1555 | `temp` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int length, pathDepth, temp;` |
| 1556 | `listCopy` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char **listCopy;` |
| 1557 | `name` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *name;` |
| 1558 | `list` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *list[MAX_FOUND_FILES];` |
| 1559 | `search` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 1560 | `pak` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `pack_t *pak;` |
| 1561 | `buildBuffer` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileInPack_t *buildBuffer;` |
| 1562 | `wantSubs` | local / FS_ListFilteredFiles | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `qboolean wantSubs;` |
| 1563 | `zpath` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char zpath[MAX_ZPATH];` |
| 1564 | `dirName` | local / FS_ListFilteredFiles | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char dirName[64];` |
| 1565 | `netpath` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char netpath[MAX_OSPATH];` |
| 1600 | `zpathLen` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int zpathLen, depth;` |
| 1600 | `depth` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int zpathLen, depth;` |
| 1638 | `numSysFiles` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int numSysFiles;` |
| 1639 | `sysFiles` | local / FS_ListFilteredFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char **sysFiles;` |
| 1670 | `FS_ListFiles` | function / FS_ListFiles | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles ) {` |
| 1670 | `path` | parameter / FS_ListFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles ) {` |
| 1670 | `extension` | parameter / FS_ListFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles ) {` |
| 1670 | `numfiles` | parameter / FS_ListFiles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles ) {` |
| 1679 | `FS_FreeFileList` | function / FS_FreeFileList | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_FreeFileList( char **list ) {` |
| 1679 | `list` | parameter / FS_FreeFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_FreeFileList( char **list ) {` |
| 1680 | `i` | local / FS_FreeFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1697 | `FS_GetFileList` | function / FS_GetFileList | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_GetFileList( const char *path, const char *extension, char *listbuf, int bufsize ) {` |
| 1697 | `path` | parameter / FS_GetFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_GetFileList( const char *path, const char *extension, char *listbuf, int bufsize ) {` |
| 1697 | `extension` | parameter / FS_GetFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_GetFileList( const char *path, const char *extension, char *listbuf, int bufsize ) {` |
| 1697 | `listbuf` | parameter / FS_GetFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_GetFileList( const char *path, const char *extension, char *listbuf, int bufsize ) {` |
| 1697 | `bufsize` | parameter / FS_GetFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_GetFileList( const char *path, const char *extension, char *listbuf, int bufsize ) {` |
| 1698 | `nFiles` | local / FS_GetFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nFiles, i, nTotal, nLen;` |
| 1698 | `i` | local / FS_GetFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nFiles, i, nTotal, nLen;` |
| 1698 | `nTotal` | local / FS_GetFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nFiles, i, nTotal, nLen;` |
| 1698 | `nLen` | local / FS_GetFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nFiles, i, nTotal, nLen;` |
| 1699 | `pFiles` | local / FS_GetFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char **pFiles;` |
| 1725 | `FS_ConvertPath` | function / FS_ConvertPath | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ConvertPath( char *s ) {` |
| 1725 | `s` | parameter / FS_ConvertPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_ConvertPath( char *s ) {` |
| 1741 | `FS_PathCmp` | function / FS_PathCmp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_PathCmp( const char *s1, const char *s2 ) {` |
| 1741 | `s1` | parameter / FS_PathCmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_PathCmp( const char *s1, const char *s2 ) {` |
| 1741 | `s2` | parameter / FS_PathCmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_PathCmp( const char *s1, const char *s2 ) {` |
| 1742 | `c1` | local / FS_PathCmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 1742 | `c2` | local / FS_PathCmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 1774 | `FS_SortFileList` | function / FS_SortFileList | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_SortFileList( char **filelist, int numfiles ) {` |
| 1774 | `filelist` | parameter / FS_SortFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_SortFileList( char **filelist, int numfiles ) {` |
| 1774 | `numfiles` | parameter / FS_SortFileList | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_SortFileList( char **filelist, int numfiles ) {` |
| 1775 | `sortedlist` | local / FS_SortFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char **sortedlist;` |
| 1776 | `i` | local / FS_SortFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 1776 | `j` | local / FS_SortFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 1787 | `k` | local / FS_SortFileList | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int k;` |
| 1803 | `FS_DisplayPath` | function / FS_DisplayPath | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_DisplayPath( qboolean showAll ) {` |
| 1803 | `showAll` | parameter / FS_DisplayPath | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_DisplayPath( qboolean showAll ) {` |
| 1804 | `s` | local / FS_DisplayPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *s;` |
| 1805 | `i` | local / FS_DisplayPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1845 | `FS_Path_f` | function / FS_Path_f | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Path_f( void ) {` |
| 1854 | `FS_FullPath_f` | function / FS_FullPath_f | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_FullPath_f( void ) {` |
| 1863 | `PakFileLanguage` | function / PakFileLanguage | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static char *PakFileLanguage( const char *pakName ) {` |
| 1863 | `pakName` | parameter / PakFileLanguage | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `static char *PakFileLanguage( const char *pakName ) {` |
| 1864 | `buffers` | local / PakFileLanguage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static char buffers[2][64];` |
| 1865 | `index` | local / PakFileLanguage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static int index = 0;` |
| 1866 | `i` | local / PakFileLanguage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1891 | `paksort` | function / paksort | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int paksort( const void *a, const void *b ) {` |
| 1891 | `a` | parameter / paksort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int paksort( const void *a, const void *b ) {` |
| 1891 | `b` | parameter / paksort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int paksort( const void *a, const void *b ) {` |
| 1892 | `pa` | local / paksort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *const *pa = a;` |
| 1893 | `pb` | local / paksort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *const *pb = b;` |
| 1894 | `aa` | local / paksort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *aa = *pa;` |
| 1895 | `bb` | local / paksort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *bb = *pb;` |
| 1896 | `langA` | local / paksort | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char *langA, *langB;` |
| 1896 | `langB` | local / paksort | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char *langA, *langB;` |
| 1918 | `FS_AddSearchPath` | function / FS_AddSearchPath | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_AddSearchPath( searchpath_t *sp ) {` |
| 1918 | `sp` | parameter / FS_AddSearchPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddSearchPath( searchpath_t *sp ) {` |
| 1919 | `s` | local / FS_AddSearchPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *s;` |
| 1944 | `FS_AddPakFilesForGameDirectory` | function / FS_AddPakFilesForGameDirectory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_AddPakFilesForGameDirectory( const char *path, const char *dir,` |
| 1944 | `path` | parameter / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddPakFilesForGameDirectory( const char *path, const char *dir,` |
| 1944 | `dir` | parameter / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddPakFilesForGameDirectory( const char *path, const char *dir,` |
| 1945 | `localized` | parameter / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean localized, int language ) {` |
| 1945 | `language` | parameter / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean localized, int language ) {` |
| 1946 | `pakfile` | local / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char pakfile[MAX_OSPATH];` |
| 1947 | `pakfiles` | local / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char **pakfiles;` |
| 1948 | `sortedfiles` | local / FS_AddPakFilesForGameDirectory | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char *sortedfiles[MAX_SEARCH_PATHS];` |
| 1949 | `numfiles` | local / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int numfiles, i;` |
| 1949 | `i` | local / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int numfiles, i;` |
| 1950 | `search` | local / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 1951 | `pak` | local / FS_AddPakFilesForGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `pack_t *pak;` |
| 1952 | `pakLocalized` | local / FS_AddPakFilesForGameDirectory | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `qboolean pakLocalized;` |
| 1953 | `lang` | local / FS_AddPakFilesForGameDirectory | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char *lang;` |
| 2010 | `FS_AddGameDirectory` | function / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_AddGameDirectory( const char *path, const char *gameName,` |
| 2010 | `path` | parameter / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddGameDirectory( const char *path, const char *gameName,` |
| 2010 | `gameName` | parameter / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddGameDirectory( const char *path, const char *gameName,` |
| 2011 | `localized` | parameter / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean localized, int language ) {` |
| 2011 | `language` | parameter / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean localized, int language ) {` |
| 2012 | `sp` | local / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *sp;` |
| 2013 | `search` | local / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 2014 | `folder` | local / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char folder[64];` |
| 2015 | `netpath` | local / FS_AddGameDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char netpath[MAX_OSPATH];` |
| 2059 | `FS_AddLocalizedGameDirectory` | function / FS_AddLocalizedGameDirectory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_AddLocalizedGameDirectory( const char *path, const char *gameName ) {` |
| 2059 | `path` | parameter / FS_AddLocalizedGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddLocalizedGameDirectory( const char *path, const char *gameName ) {` |
| 2059 | `gameName` | parameter / FS_AddLocalizedGameDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_AddLocalizedGameDirectory( const char *path, const char *gameName ) {` |
| 2069 | `FS_AddNonPackFileDirectory_Internal` | function / FS_AddNonPackFileDirectory_Internal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_AddNonPackFileDirectory_Internal( const char *path, const char *gamedir,` |
| 2069 | `path` | parameter / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_AddNonPackFileDirectory_Internal( const char *path, const char *gamedir,` |
| 2069 | `gamedir` | parameter / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_AddNonPackFileDirectory_Internal( const char *path, const char *gamedir,` |
| 2070 | `dir` | parameter / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *dir, const char *extension ) {` |
| 2070 | `extension` | parameter / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *dir, const char *extension ) {` |
| 2071 | `folder` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char folder[MAX_OSPATH];` |
| 2072 | `netpath` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char netpath[MAX_OSPATH];` |
| 2073 | `files` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char **files;` |
| 2074 | `numFiles` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int numFiles, len, i;` |
| 2074 | `len` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int numFiles, len, i;` |
| 2074 | `i` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int numFiles, len, i;` |
| 2075 | `hash` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 2076 | `list` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFileList_t *list;` |
| 2077 | `buildBuffer` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFile_t *buildBuffer;` |
| 2078 | `file` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFile_t *file;` |
| 2079 | `namePtr` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *namePtr;` |
| 2108 | `filename` | local / FS_AddNonPackFileDirectory_Internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *filename = files[i];` |
| 2129 | `FS_AddNonPackFileDirectory` | function / FS_AddNonPackFileDirectory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_AddNonPackFileDirectory( const char *dir, const char *extension ) {` |
| 2129 | `dir` | parameter / FS_AddNonPackFileDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_AddNonPackFileDirectory( const char *dir, const char *extension ) {` |
| 2129 | `extension` | parameter / FS_AddNonPackFileDirectory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_AddNonPackFileDirectory( const char *dir, const char *extension ) {` |
| 2130 | `search` | local / FS_AddNonPackFileDirectory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 2146 | `FS_GetDataForFile` | function / FS_GetDataForFile | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `fileData_t *FS_GetDataForFile( const char *dir, const char *name, const char *ext ) {` |
| 2146 | `dir` | parameter / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileData_t *FS_GetDataForFile( const char *dir, const char *name, const char *ext ) {` |
| 2146 | `name` | parameter / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileData_t *FS_GetDataForFile( const char *dir, const char *name, const char *ext ) {` |
| 2146 | `ext` | parameter / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileData_t *FS_GetDataForFile( const char *dir, const char *name, const char *ext ) {` |
| 2147 | `filename` | local / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char filename[1024];` |
| 2148 | `search` | local / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 2149 | `pakFile` | local / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileInPack_t *pakFile;` |
| 2150 | `list` | local / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFileList_t *list;` |
| 2151 | `file` | local / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFile_t *file;` |
| 2152 | `hash` | local / FS_GetDataForFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 2187 | `FS_ClearDataForFiles` | function / FS_ClearDataForFiles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ClearDataForFiles( void *lowEnd, void *highEnd ) {` |
| 2187 | `lowEnd` | parameter / FS_ClearDataForFiles | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_ClearDataForFiles( void *lowEnd, void *highEnd ) {` |
| 2187 | `highEnd` | parameter / FS_ClearDataForFiles | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_ClearDataForFiles( void *lowEnd, void *highEnd ) {` |
| 2188 | `search` | local / FS_ClearDataForFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 2189 | `pakFile` | local / FS_ClearDataForFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fileInPack_t *pakFile;` |
| 2190 | `list` | local / FS_ClearDataForFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFileList_t *list;` |
| 2191 | `entry` | local / FS_ClearDataForFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFile_t *entry;` |
| 2192 | `i` | local / FS_ClearDataForFiles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2232 | `FS_ShutdownSearchPaths` | function / FS_ShutdownSearchPaths | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_ShutdownSearchPaths( searchpath_t *paths ) {` |
| 2232 | `paths` | parameter / FS_ShutdownSearchPaths | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_ShutdownSearchPaths( searchpath_t *paths ) {` |
| 2233 | `p` | local / FS_ShutdownSearchPaths | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *p, *next;` |
| 2233 | `next` | local / FS_ShutdownSearchPaths | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *p, *next;` |
| 2254 | `FS_ShutdownFileLists` | function / FS_ShutdownFileLists | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void FS_ShutdownFileLists( fs_dirFileList_t *lists ) {` |
| 2254 | `lists` | parameter / FS_ShutdownFileLists | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void FS_ShutdownFileLists( fs_dirFileList_t *lists ) {` |
| 2255 | `list` | local / FS_ShutdownFileLists | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFileList_t *list, *next;` |
| 2255 | `next` | local / FS_ShutdownFileLists | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `fs_dirFileList_t *list, *next;` |
| 2269 | `FS_ClearMemory` | function / FS_ClearMemory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ClearMemory( void ) {` |
| 2277 | `FS_ShutdownServerPakNames` | function / FS_ShutdownServerPakNames | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ShutdownServerPakNames( void ) {` |
| 2278 | `i` | local / FS_ShutdownServerPakNames | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2294 | `FS_ShutdownServerReferencedPaks` | function / FS_ShutdownServerReferencedPaks | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ShutdownServerReferencedPaks( void ) {` |
| 2295 | `i` | local / FS_ShutdownServerReferencedPaks | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2313 | `FS_Shutdown` | function / FS_Shutdown | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Shutdown( qboolean closemfp ) {` |
| 2313 | `closemfp` | parameter / FS_Shutdown | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Shutdown( qboolean closemfp ) {` |
| 2314 | `i` | local / FS_Shutdown | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2332 | `FS_Startup` | function / FS_Startup | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Startup( const char *gameName ) {` |
| 2332 | `gameName` | parameter / FS_Startup | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Startup( const char *gameName ) {` |
| 2333 | `homePath` | local / FS_Startup | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *homePath;` |
| 2402 | `FS_ClearPakReferences` | function / FS_ClearPakReferences | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_ClearPakReferences( int flags ) {` |
| 2402 | `flags` | parameter / FS_ClearPakReferences | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_ClearPakReferences( int flags ) {` |
| 2403 | `search` | local / FS_ClearPakReferences | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `searchpath_t *search;` |
| 2426 | `FS_InitFilesystem` | function / FS_InitFilesystem | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_InitFilesystem( void ) {` |
| 2448 | `FS_Restart` | function / FS_Restart | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Restart( int checksumFeed ) {` |
| 2448 | `checksumFeed` | parameter / FS_Restart | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Restart( int checksumFeed ) {` |
| 2476 | `FS_ConditionalRestart` | function / FS_ConditionalRestart | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean FS_ConditionalRestart( int checksumFeed ) {` |
| 2476 | `checksumFeed` | parameter / FS_ConditionalRestart | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean FS_ConditionalRestart( int checksumFeed ) {` |
| 2489 | `FS_FOpenFileByMode` | function / FS_FOpenFileByMode | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_FOpenFileByMode( const char *qpath, fileHandle_t *f, fsMode_t mode ) {` |
| 2489 | `qpath` | parameter / FS_FOpenFileByMode | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileByMode( const char *qpath, fileHandle_t *f, fsMode_t mode ) {` |
| 2489 | `f` | parameter / FS_FOpenFileByMode | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileByMode( const char *qpath, fileHandle_t *f, fsMode_t mode ) {` |
| 2489 | `mode` | parameter / FS_FOpenFileByMode | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FOpenFileByMode( const char *qpath, fileHandle_t *f, fsMode_t mode ) {` |
| 2490 | `r` | local / FS_FOpenFileByMode | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int r = FS_UNSET_FILE_LENGTH;` |
| 2491 | `sync` | local / FS_FOpenFileByMode | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean sync = qfalse;` |
| 2538 | `FS_FTell` | function / FS_FTell | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int FS_FTell( fileHandle_t f ) {` |
| 2538 | `f` | parameter / FS_FTell | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_FTell( fileHandle_t f ) {` |
| 2539 | `pos` | local / FS_FTell | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int pos;` |
| 2554 | `FS_Flush` | function / FS_Flush | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FS_Flush( fileHandle_t f ) {` |
| 2554 | `f` | parameter / FS_Flush | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Flush( fileHandle_t f ) {` |

## code/qcommon/files_local.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 24 | `Q3MAP_FILES_LOCAL_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_FILES_LOCAL_H` |
| 29 | `MAX_FILE_HANDLES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_FILE_HANDLES 64` |
| 30 | `MAX_SERVER_PAKS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_SERVER_PAKS 4096` |
| 31 | `MAX_ZPATH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_ZPATH 256` |
| 32 | `ERR_FATAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ERR_FATAL 0` |
| 34 | `fileHandle_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef int fileHandle_t;` |
| 35 | `unzFile` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef struct unz_s *unzFile;` |
| 35 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct unz_s *unzFile;` |
| 40 | `qfile_gut` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} qfile_gut;` |
| 38 | `o` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `FILE *o;` |
| 39 | `z` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unzFile z;` |
| 45 | `qfile_ut` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} qfile_ut;` |
| 43 | `file` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qfile_gut file;` |
| 44 | `unique` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean unique;` |
| 56 | `fileHandleData_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} fileHandleData_t;` |
| 48 | `handleFiles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qfile_ut handleFiles;` |
| 49 | `handleSync` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean handleSync;` |
| 50 | `baseOffset` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int baseOffset;` |
| 51 | `fileSize` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int fileSize;` |
| 52 | `zipFilePos` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int zipFilePos;` |
| 53 | `zipFile` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `void *zipFile;` |
| 54 | `streamed` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean streamed;` |
| 55 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char name[MAX_ZPATH];` |
| 58 | `file_handle_size_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char file_handle_size_check[sizeof( fileHandleData_t ) == 288 ? 1 : -1];` |
| 59 | `file_handle_zip_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char file_handle_zip_offset_check[offsetof( fileHandleData_t, zipFile ) == 24 ? 1 : -1];` |
| 60 | `file_handle_name_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char file_handle_name_offset_check[offsetof( fileHandleData_t, name ) == 32 ? 1 : -1];` |
| 62 | `fsh` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern fileHandleData_t fsh[MAX_FILE_HANDLES];` |
| 64 | `Com_Printf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Printf( const char *format, ... );` |
| 64 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Printf( const char *format, ... );` |
| 65 | `FS_CheckFileSystemStarted` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void FS_CheckFileSystemStarted( void );` |
| 66 | `FS_FOpenFileWrite` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `fileHandle_t FS_FOpenFileWrite( const char *filename );` |
| 66 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `fileHandle_t FS_FOpenFileWrite( const char *filename );` |
| 67 | `FS_FCloseFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_FCloseFile( fileHandle_t f );` |
| 67 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_FCloseFile( fileHandle_t f );` |
| 68 | `FS_Write` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int FS_Write( const void *buffer, int len, fileHandle_t f );` |
| 68 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Write( const void *buffer, int len, fileHandle_t f );` |
| 68 | `len` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Write( const void *buffer, int len, fileHandle_t f );` |
| 68 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Write( const void *buffer, int len, fileHandle_t f );` |
| 69 | `unzReadCurrentFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int unzReadCurrentFile( unzFile file, void *buf, unsigned int len );` |
| 69 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzReadCurrentFile( unzFile file, void *buf, unsigned int len );` |
| 69 | `buf` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzReadCurrentFile( unzFile file, void *buf, unsigned int len );` |
| 69 | `len` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzReadCurrentFile( unzFile file, void *buf, unsigned int len );` |
| 70 | `FS_ListFilteredFiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char **FS_ListFilteredFiles( const char *path, const char *extension, const char *filter, int *numfiles );` |
| 70 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFilteredFiles( const char *path, const char *extension, const char *filter, int *numfiles );` |
| 70 | `extension` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFilteredFiles( const char *path, const char *extension, const char *filter, int *numfiles );` |
| 70 | `filter` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFilteredFiles( const char *path, const char *extension, const char *filter, int *numfiles );` |
| 70 | `numfiles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFilteredFiles( const char *path, const char *extension, const char *filter, int *numfiles );` |
| 72 | `FS_Read` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int FS_Read( void *buffer, int len, fileHandle_t f );` |
| 72 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Read( void *buffer, int len, fileHandle_t f );` |
| 72 | `len` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Read( void *buffer, int len, fileHandle_t f );` |
| 72 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int FS_Read( void *buffer, int len, fileHandle_t f );` |
| 73 | `FS_WriteFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_WriteFile( const char *qpath, const void *buffer, int size );` |
| 73 | `qpath` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_WriteFile( const char *qpath, const void *buffer, int size );` |
| 73 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_WriteFile( const char *qpath, const void *buffer, int size );` |
| 73 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_WriteFile( const char *qpath, const void *buffer, int size );` |
| 74 | `FS_ListFiles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles );` |
| 74 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles );` |
| 74 | `extension` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles );` |
| 74 | `numfiles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char **FS_ListFiles( const char *path, const char *extension, int *numfiles );` |
| 75 | `FS_Flush` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void FS_Flush( fileHandle_t f );` |
| 75 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FS_Flush( fileHandle_t f );` |

## code/qcommon/qfiles.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 24 | `__QFILES_H__` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define __QFILES_H__` |
| 32 | `SHADER_MAX_VERTEXES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SHADER_MAX_VERTEXES	1000` |
| 33 | `SHADER_MAX_INDEXES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SHADER_MAX_INDEXES	(6*SHADER_MAX_VERTEXES)` |
| 37 | `MAX_QPATH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_QPATH		64` |
| 47 | `VM_MAGIC` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	VM_MAGIC	0x12721444` |
| 60 | `vmHeader_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} vmHeader_t;` |
| 49 | `vmMagic` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		vmMagic;` |
| 51 | `instructionCount` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		instructionCount;` |
| 53 | `codeOffset` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		codeOffset;` |
| 54 | `codeLength` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		codeLength;` |
| 56 | `dataOffset` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		dataOffset;` |
| 57 | `dataLength` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		dataLength;` |
| 58 | `litLength` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		litLength;			// ( dataLength - litLength ) should be byteswapped on load` |
| 59 | `bssLength` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		bssLength;			// zero filled memory appended to datalength` |
| 85 | `pcx_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} pcx_t;` |
| 72 | `manufacturer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	manufacturer;` |
| 73 | `version` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	version;` |
| 74 | `encoding` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	encoding;` |
| 75 | `bits_per_pixel` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	bits_per_pixel;` |
| 76 | `xmin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 76 | `ymin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 76 | `xmax` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 76 | `ymax` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 77 | `hres` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	hres,vres;` |
| 77 | `vres` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	hres,vres;` |
| 78 | `palette` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	palette[48];` |
| 79 | `reserved` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	reserved;` |
| 80 | `color_planes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	color_planes;` |
| 81 | `bytes_per_line` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	bytes_per_line;` |
| 82 | `palette_type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	palette_type;` |
| 83 | `filler` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	filler[58];` |
| 84 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	data;			// unbounded` |
| 102 | `TargaHeader` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} TargaHeader;` |
| 96 | `_TargaHeader` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct _TargaHeader {` |
| 97 | `id_length` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char 	id_length, colormap_type, image_type;` |
| 97 | `colormap_type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char 	id_length, colormap_type, image_type;` |
| 97 | `image_type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char 	id_length, colormap_type, image_type;` |
| 98 | `colormap_index` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	colormap_index, colormap_length;` |
| 98 | `colormap_length` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	colormap_index, colormap_length;` |
| 99 | `colormap_size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	colormap_size;` |
| 100 | `x_origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	x_origin, y_origin, width, height;` |
| 100 | `y_origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	x_origin, y_origin, width, height;` |
| 100 | `width` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	x_origin, y_origin, width, height;` |
| 100 | `height` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	x_origin, y_origin, width, height;` |
| 101 | `pixel_size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	pixel_size, attributes;` |
| 101 | `attributes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	pixel_size, attributes;` |
| 114 | `MD3_IDENT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_IDENT			(('3'<<24)+('P'<<16)+('D'<<8)+'I')` |
| 115 | `MD3_VERSION` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_VERSION			15` |
| 118 | `MD3_MAX_LODS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_MAX_LODS		3` |
| 119 | `MD3_MAX_TRIANGLES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MD3_MAX_TRIANGLES	8192	// per surface` |
| 120 | `MD3_MAX_VERTS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_MAX_VERTS		4096	// per surface` |
| 121 | `MD3_MAX_SHADERS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_MAX_SHADERS		256		// per surface` |
| 122 | `MD3_MAX_FRAMES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_MAX_FRAMES		1024	// per model` |
| 123 | `MD3_MAX_SURFACES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MD3_MAX_SURFACES	32		// per model` |
| 124 | `MD3_MAX_TAGS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD3_MAX_TAGS		16		// per frame` |
| 127 | `MD3_XYZ_SCALE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MD3_XYZ_SCALE		(1.0/64)` |
| 134 | `md3Frame_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3Frame_t;` |
| 129 | `md3Frame_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct md3Frame_s {` |
| 130 | `bounds` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		bounds[2];` |
| 131 | `localOrigin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		localOrigin;` |
| 132 | `radius` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		radius;` |
| 133 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		name[16];` |
| 140 | `md3Tag_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3Tag_t;` |
| 136 | `md3Tag_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct md3Tag_s {` |
| 137 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		name[MAX_QPATH];	// tag name` |
| 138 | `origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		origin;` |
| 139 | `axis` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		axis[3];` |
| 171 | `md3Surface_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3Surface_t;` |
| 153 | `ident` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		ident;				//` |
| 155 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	name[MAX_QPATH];	// polyset name` |
| 157 | `flags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		flags;` |
| 158 | `numFrames` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		numFrames;			// all surfaces in a model should have the same` |
| 160 | `numShaders` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		numShaders;			// all surfaces in a model should have the same` |
| 161 | `numVerts` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		numVerts;` |
| 163 | `numTriangles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		numTriangles;` |
| 164 | `ofsTriangles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		ofsTriangles;` |
| 166 | `ofsShaders` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		ofsShaders;			// offset from start of md3Surface_t` |
| 167 | `ofsSt` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		ofsSt;				// texture coords are common for all frames` |
| 168 | `ofsXyzNormals` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		ofsXyzNormals;		// numVerts * numFrames` |
| 170 | `ofsEnd` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		ofsEnd;				// next surface follows` |
| 176 | `md3Shader_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3Shader_t;` |
| 174 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char			name[MAX_QPATH];` |
| 175 | `shaderIndex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int				shaderIndex;	// for in-game use` |
| 180 | `md3Triangle_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3Triangle_t;` |
| 179 | `indexes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			indexes[3];` |
| 184 | `md3St_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3St_t;` |
| 183 | `st` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		st[2];` |
| 189 | `md3XyzNormal_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3XyzNormal_t;` |
| 187 | `xyz` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		xyz[3];` |
| 188 | `normal` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		normal;` |
| 210 | `md3Header_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md3Header_t;` |
| 192 | `ident` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ident;` |
| 193 | `version` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			version;` |
| 195 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		name[MAX_QPATH];	// model name` |
| 197 | `flags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			flags;` |
| 199 | `numFrames` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numFrames;` |
| 200 | `numTags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numTags;` |
| 201 | `numSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numSurfaces;` |
| 203 | `numSkins` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numSkins;` |
| 205 | `ofsFrames` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsFrames;			// offset for first frame` |
| 206 | `ofsTags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsTags;			// numFrames * numTags` |
| 207 | `ofsSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsSurfaces;		// first surface, others follow` |
| 209 | `ofsEnd` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsEnd;				// end of file` |
| 220 | `MD4_IDENT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD4_IDENT			(('4'<<24)+('P'<<16)+('D'<<8)+'I')` |
| 221 | `MD4_VERSION` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MD4_VERSION			1` |
| 222 | `MD4_MAX_BONES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MD4_MAX_BONES		128` |
| 228 | `md4Weight_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Weight_t;` |
| 225 | `boneIndex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			boneIndex;		// these are indexes into the boneReferences,` |
| 226 | `boneWeight` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		   boneWeight;		// not the global per-frame bone list` |
| 227 | `offset` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		offset;` |
| 235 | `md4Vertex_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Vertex_t;` |
| 231 | `normal` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		normal;` |
| 232 | `texCoords` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec2_t		texCoords;` |
| 233 | `numWeights` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numWeights;` |
| 234 | `weights` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `md4Weight_t	weights[1];		// variable sized` |
| 239 | `md4Triangle_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Triangle_t;` |
| 238 | `indexes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			indexes[3];` |
| 265 | `md4Surface_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Surface_t;` |
| 242 | `ident` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ident;` |
| 244 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		name[MAX_QPATH];	// polyset name` |
| 245 | `shader` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		shader[MAX_QPATH];` |
| 246 | `shaderIndex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			shaderIndex;		// for in-game use` |
| 248 | `ofsHeader` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsHeader;			// this will be a negative number` |
| 250 | `numVerts` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numVerts;` |
| 251 | `ofsVerts` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsVerts;` |
| 253 | `numTriangles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numTriangles;` |
| 254 | `ofsTriangles` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsTriangles;` |
| 261 | `numBoneReferences` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numBoneReferences;` |
| 262 | `ofsBoneReferences` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsBoneReferences;` |
| 264 | `ofsEnd` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsEnd;				// next surface follows` |
| 269 | `md4Bone_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Bone_t;` |
| 268 | `matrix` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		matrix[3][4];` |
| 276 | `md4Frame_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Frame_t;` |
| 272 | `bounds` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		bounds[2];			// bounds of all surfaces of all LOD's for this frame` |
| 273 | `localOrigin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		localOrigin;		// midpoint of bounds, used for sphere cull` |
| 274 | `radius` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		radius;				// dist from localOrigin to corner` |
| 275 | `bones` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `md4Bone_t	bones[1];			// [numBones]` |
| 282 | `md4LOD_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4LOD_t;` |
| 279 | `numSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numSurfaces;` |
| 280 | `ofsSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsSurfaces;		// first surface, others follow` |
| 281 | `ofsEnd` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsEnd;				// next lod follows` |
| 301 | `md4Header_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} md4Header_t;` |
| 285 | `ident` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ident;` |
| 286 | `version` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			version;` |
| 288 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		name[MAX_QPATH];	// model name` |
| 291 | `numFrames` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numFrames;` |
| 292 | `numBones` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numBones;` |
| 293 | `ofsBoneNames` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsBoneNames;		// char	name[ MAX_QPATH ]` |
| 294 | `ofsFrames` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsFrames;			// md4Frame_t[numFrames]` |
| 297 | `numLODs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numLODs;` |
| 298 | `ofsLODs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsLODs;` |
| 300 | `ofsEnd` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ofsEnd;				// end of file` |
| 313 | `BSP_IDENT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define BSP_IDENT	(('P'<<24)+('S'<<16)+('B'<<8)+'I')` |
| 316 | `BSP_VERSION` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define BSP_VERSION			46` |
| 321 | `MAX_MAP_MODELS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_MODELS		0x800` |
| 322 | `MAX_MAP_BRUSHES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_BRUSHES		0x8000` |
| 323 | `MAX_MAP_ENTITIES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_ENTITIES	0x2000` |
| 324 | `MAX_MAP_ENTSTRING` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_ENTSTRING	0x100000` |
| 325 | `MAX_MAP_SHADERS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_SHADERS		0x400` |
| 327 | `MAX_MAP_AREAS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_AREAS		0x100	// MAX_MAP_AREA_BYTES in q_shared must match!` |
| 328 | `MAX_MAP_FOGS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_FOGS		0x100` |
| 329 | `MAX_MAP_PLANES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_PLANES		0x60000` |
| 330 | `MAX_MAP_NODES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_NODES		0x20000` |
| 331 | `MAX_MAP_BRUSHSIDES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_BRUSHSIDES	0x60000` |
| 332 | `MAX_MAP_LEAFS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_LEAFS		0x20000` |
| 333 | `MAX_MAP_LEAFFACES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_LEAFFACES	0x20000` |
| 334 | `MAX_MAP_LEAFBRUSHES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_LEAFBRUSHES 0x40000` |
| 335 | `MAX_MAP_PORTALS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_PORTALS		0x20000` |
| 336 | `MAX_MAP_LIGHTING` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_LIGHTING	0x1000000` |
| 337 | `MAX_MAP_LIGHTGRID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_LIGHTGRID	0x800000` |
| 338 | `MAX_MAP_VISIBILITY` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_VISIBILITY	0x300000` |
| 340 | `MAX_MAP_DRAW_SURFS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_DRAW_SURFS	0x20000` |
| 341 | `MAX_MAP_DRAW_VERTS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_DRAW_VERTS	0x80000` |
| 342 | `MAX_MAP_DRAW_INDEXES` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_MAP_DRAW_INDEXES	0x80000` |
| 345 | `MAX_MAP_TRISOUPS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_TRISOUPS             0x20000` |
| 346 | `MAX_MAP_CELLS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_CELLS                0x1000` |
| 347 | `MAX_MAP_CULLGROUPS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_CULLGROUPS           0x800` |
| 348 | `MAX_MAP_CULLGROUP_INDEXES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_CULLGROUP_INDEXES    0x1000` |
| 349 | `MAX_MAP_BSP_PORTALS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_BSP_PORTALS          0x2000` |
| 350 | `MAX_MAP_PORTAL_VERTS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_PORTAL_VERTS         0x10000` |
| 351 | `MAX_MAP_LIGHTS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_LIGHTS               0x800` |
| 352 | `MAX_MAP_LIGHT_INDEXES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_LIGHT_INDEXES        0x10000` |
| 353 | `MAX_MAP_COLLISION_INDEXES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_COLLISION_INDEXES    0x40000` |
| 354 | `MAX_MAP_OCCLUDERS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_OCCLUDERS            0x2000` |
| 355 | `MAX_MAP_OCCLUDER_EDGES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_OCCLUDER_EDGES        0x20000` |
| 356 | `MAX_MAP_OCCLUDER_PLANES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_OCCLUDER_PLANES       0x10000` |
| 357 | `MAX_MAP_AABBTREES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_AABBTREES            0x100000` |
| 358 | `MAX_MAP_TRIANGLE_EDGES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_TRIANGLE_EDGES       0x80000` |
| 361 | `MAX_MAP_CELL_LISTS` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define MAX_MAP_CELL_LISTS           ( MAX_MAP_CELLS + MAX_MAP_CULLGROUPS )` |
| 365 | `MAX_KEY` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_KEY				32` |
| 366 | `MAX_VALUE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_VALUE			1024` |
| 369 | `ANGLE_UP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	ANGLE_UP			-1` |
| 370 | `ANGLE_DOWN` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	ANGLE_DOWN			-2` |
| 372 | `LIGHTMAP_WIDTH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	LIGHTMAP_WIDTH		128` |
| 373 | `LIGHTMAP_HEIGHT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	LIGHTMAP_HEIGHT		128` |
| 375 | `MAX_WORLD_COORD` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_WORLD_COORD		( 128*1024 )` |
| 376 | `MIN_WORLD_COORD` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MIN_WORLD_COORD		( -128*1024 )` |
| 377 | `WORLD_SIZE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define WORLD_SIZE			( MAX_WORLD_COORD - MIN_WORLD_COORD )` |
| 386 | `lump_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} lump_t;` |
| 385 | `filelen` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		filelen, fileofs;` |
| 385 | `fileofs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		filelen, fileofs;` |
| 388 | `HEADER_LUMPS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	HEADER_LUMPS		33` |
| 395 | `dheader_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dheader_t;` |
| 391 | `ident` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			ident;` |
| 392 | `version` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			version;` |
| 394 | `lumps` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `lump_t		lumps[HEADER_LUMPS];` |
| 402 | `dmodel_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dmodel_t;` |
| 398 | `mins` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		mins[3], maxs[3];` |
| 398 | `maxs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		mins[3], maxs[3];` |
| 399 | `firstSurface` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstSurface, numSurfaces;` |
| 399 | `numSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstSurface, numSurfaces;` |
| 400 | `firstLeafSurface` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstLeafSurface, numLeafSurfaces;` |
| 400 | `numLeafSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstLeafSurface, numLeafSurfaces;` |
| 401 | `firstBrush` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstBrush, numBrushes;` |
| 401 | `numBrushes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstBrush, numBrushes;` |
| 408 | `dshader_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dshader_t;` |
| 405 | `shader` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		shader[MAX_QPATH];` |
| 406 | `surfaceFlags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			surfaceFlags;` |
| 407 | `contentFlags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			contentFlags;` |
| 415 | `dplane_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dplane_t;` |
| 413 | `normal` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		normal[3];` |
| 414 | `dist` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		dist;` |
| 422 | `dnode_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dnode_t;` |
| 418 | `planeNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			planeNum;` |
| 419 | `children` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			children[2];	// negative numbers are -(leafs+1), not nodes` |
| 420 | `mins` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			mins[3];		// for frustom culling` |
| 421 | `maxs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			maxs[3];` |
| 434 | `dleaf_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dleaf_t;` |
| 425 | `cluster` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int cluster;` |
| 426 | `area` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int area;` |
| 427 | `firstLeafSurface` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstLeafSurface;` |
| 428 | `numLeafSurfaces` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int numLeafSurfaces;` |
| 429 | `firstLeafBrush` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstLeafBrush;` |
| 430 | `numLeafBrushes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int numLeafBrushes;` |
| 431 | `cellIndex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int cellIndex;` |
| 432 | `firstLightIndex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstLightIndex;` |
| 433 | `numLightIndexes` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int numLightIndexes;` |
| 439 | `dbrushsidePlane_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} dbrushsidePlane_t;` |
| 437 | `planeNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			planeNum;` |
| 438 | `planeDist` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		planeDist;` |
| 444 | `dbrushside_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dbrushside_t;` |
| 442 | `plane` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `dbrushsidePlane_t plane;	// axial sides store distance; others store plane index` |
| 443 | `shaderNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			shaderNum;` |
| 449 | `dbrush_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dbrush_t;` |
| 447 | `numSides` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		numSides;` |
| 448 | `shaderNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		shaderNum;		// the shader that determines the contents flags` |
| 455 | `dfog_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dfog_t;` |
| 452 | `shader` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char		shader[MAX_QPATH];` |
| 453 | `brushNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			brushNum;` |
| 454 | `visibleSide` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			visibleSide;	// the brush side that ray tests need to clip against (-1 == none)` |
| 463 | `drawVert_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} drawVert_t;` |
| 458 | `xyz` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		xyz;` |
| 459 | `st` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		st[2];` |
| 460 | `lightmap` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float		lightmap[2];` |
| 461 | `normal` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		normal;` |
| 462 | `color` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte		color[4];` |
| 471 | `mapSurfaceType_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} mapSurfaceType_t;` |
| 466 | `MST_BAD` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `MST_BAD,` |
| 467 | `MST_PLANAR` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `MST_PLANAR,` |
| 468 | `MST_PATCH` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `MST_PATCH,` |
| 469 | `MST_TRIANGLE_SOUP` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `MST_TRIANGLE_SOUP,` |
| 470 | `MST_FLARE` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `MST_FLARE` |
| 493 | `dsurface_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} dsurface_t;` |
| 474 | `shaderNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			shaderNum;` |
| 475 | `fogNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			fogNum;` |
| 476 | `surfaceType` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			surfaceType;` |
| 478 | `firstVert` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstVert;` |
| 479 | `numVerts` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numVerts;` |
| 481 | `firstIndex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstIndex;` |
| 482 | `numIndexes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			numIndexes;` |
| 484 | `lightmapNum` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			lightmapNum;` |
| 485 | `lightmapX` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			lightmapX, lightmapY;` |
| 485 | `lightmapY` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			lightmapX, lightmapY;` |
| 486 | `lightmapWidth` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			lightmapWidth, lightmapHeight;` |
| 486 | `lightmapHeight` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			lightmapWidth, lightmapHeight;` |
| 488 | `lightmapOrigin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		lightmapOrigin;` |
| 489 | `lightmapVecs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		lightmapVecs[3];	// for patches, [0] and [1] are lodbounds` |
| 491 | `patchWidth` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			patchWidth;` |
| 492 | `patchHeight` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			patchHeight;` |

## code/qcommon/unzip.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 27 | `LittleShort` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define LittleShort( x ) ( x )` |
| 28 | `LittleLong` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define LittleLong( x ) ( x )` |
| 30 | `unz_copyright` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `const char unz_copyright[] =` |
| 33 | `unzFile` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef struct unz_s *unzFile;` |
| 33 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct unz_s *unzFile;` |
| 35 | `Com_Memcpy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 35 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 35 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 35 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy( void *dest, const void *src, size_t count );` |
| 37 | `unz_s` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef struct unz_s unz_s;` |
| 37 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct unz_s unz_s;` |
| 38 | `UNZ_OK` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_OK 0` |
| 39 | `UNZ_ERRNO` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_ERRNO (-1)` |
| 40 | `UNZ_BADZIPFILE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_BADZIPFILE (-103)` |
| 41 | `UNZ_INTERNALERROR` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_INTERNALERROR (-104)` |
| 42 | `UNZ_BUFSIZE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_BUFSIZE 16384` |
| 43 | `SIZEZIPLOCALHEADER` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SIZEZIPLOCALHEADER 30` |
| 44 | `ALLOC` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ALLOC(size) malloc(size)` |
| 45 | `TRYFREE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define TRYFREE(ptr) free(ptr)` |
| 49 | `CASESENSITIVITYDEFAULT_NO` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CASESENSITIVITYDEFAULT_NO` |
| 55 | `CASESENSITIVITYDEFAULTVALUE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CASESENSITIVITYDEFAULTVALUE 2` |
| 57 | `CASESENSITIVITYDEFAULTVALUE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CASESENSITIVITYDEFAULTVALUE 1` |
| 61 | `STRCMPCASENOSENTIVEFUNCTION` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define STRCMPCASENOSENTIVEFUNCTION strcmpcasenosensitive_internal` |
| 75 | `UNZ_OK` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_OK 0` |
| 76 | `UNZ_PARAMERROR` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_PARAMERROR (-102)` |
| 77 | `UNZ_CRCERROR` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_CRCERROR (-105)` |
| 79 | `unzlocal_GetCurrentFileInfoInternal` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static int unzlocal_GetCurrentFileInfoInternal( unzFile file,` |
| 79 | `file` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_GetCurrentFileInfoInternal( unzFile file,` |
| 80 | `file_info` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unz_file_info *file_info, unz_file_info_internal *file_info_internal,` |
| 80 | `file_info_internal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unz_file_info *file_info, unz_file_info_internal *file_info_internal,` |
| 81 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *filename, unsigned long filename_size,` |
| 81 | `filename_size` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *filename, unsigned long filename_size,` |
| 82 | `extra_field` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void *extra_field, unsigned long extra_field_size,` |
| 82 | `extra_field_size` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void *extra_field, unsigned long extra_field_size,` |
| 83 | `comment` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *comment, unsigned long comment_size );` |
| 83 | `comment_size` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *comment, unsigned long comment_size );` |
| 86 | `BUFREADCOMMENT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define BUFREADCOMMENT 0x400` |
| 87 | `SIZECENTRALDIRITEM` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define SIZECENTRALDIRITEM 46` |
| 88 | `UNZ_MAXFILENAMEINZIP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_MAXFILENAMEINZIP 256` |
| 89 | `UNZ_END_OF_LIST_OF_FILE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_END_OF_LIST_OF_FILE (-100)` |
| 90 | `UNZ_EOF` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define UNZ_EOF 0` |
| 97 | `strcmpcasenosensitive_internal` | function / strcmpcasenosensitive_internal | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int strcmpcasenosensitive_internal (const char* fileName1,const char* fileName2)` |
| 97 | `fileName1` | parameter / strcmpcasenosensitive_internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int strcmpcasenosensitive_internal (const char* fileName1,const char* fileName2)` |
| 97 | `fileName2` | parameter / strcmpcasenosensitive_internal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int strcmpcasenosensitive_internal (const char* fileName1,const char* fileName2)` |
| 101 | `c1` | local / strcmpcasenosensitive_internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c1=*(fileName1++);` |
| 102 | `c2` | local / strcmpcasenosensitive_internal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c2=*(fileName2++);` |
| 123 | `unzStringFileNameCompare` | function / unzStringFileNameCompare | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern  int unzStringFileNameCompare (const char* fileName1,const char* fileName2,int iCaseSensitivity)` |
| 123 | `fileName1` | parameter / unzStringFileNameCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern  int unzStringFileNameCompare (const char* fileName1,const char* fileName2,int iCaseSensitivity)` |
| 123 | `fileName2` | parameter / unzStringFileNameCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern  int unzStringFileNameCompare (const char* fileName1,const char* fileName2,int iCaseSensitivity)` |
| 123 | `iCaseSensitivity` | parameter / unzStringFileNameCompare | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern  int unzStringFileNameCompare (const char* fileName1,const char* fileName2,int iCaseSensitivity)` |
| 139 | `unzlocal_SearchCentralDir` | function / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern uLong unzlocal_SearchCentralDir(FILE *fin)` |
| 139 | `fin` | parameter / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern uLong unzlocal_SearchCentralDir(FILE *fin)` |
| 141 | `buf` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char* buf;` |
| 142 | `uSizeFile` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uSizeFile;` |
| 143 | `uBackRead` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uBackRead;` |
| 144 | `uMaxBack` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uMaxBack=0xffff; /* maximum size of global comment */` |
| 145 | `uPosFound` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uPosFound=0;` |
| 163 | `uReadSize` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uReadSize,uReadPos ;` |
| 163 | `uReadPos` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uReadSize,uReadPos ;` |
| 164 | `i` | local / unzlocal_SearchCentralDir | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 199 | `unzReOpen` | function / unzReOpen | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `unzFile unzReOpen( const char *path, unzFile file ) {` |
| 199 | `path` | parameter / unzReOpen | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unzFile unzReOpen( const char *path, unzFile file ) {` |
| 199 | `file` | parameter / unzReOpen | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unzFile unzReOpen( const char *path, unzFile file ) {` |
| 200 | `s` | local / unzReOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 200 | `unz_s` | tag / unzReOpen | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 201 | `fin` | local / unzReOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *fin;` |
| 207 | `unz_s` | tag / unzReOpen | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `s = (struct unz_s *)malloc( sizeof( *s ) );` |
| 214 | `unzNoOp` | function / unzNoOp | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void unzNoOp( void ) {` |
| 222 | `unzGetGlobalInfo` | function / unzGetGlobalInfo | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzGetGlobalInfo( unzFile file, unz_global_info *info ) {` |
| 222 | `file` | parameter / unzGetGlobalInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetGlobalInfo( unzFile file, unz_global_info *info ) {` |
| 222 | `info` | parameter / unzGetGlobalInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetGlobalInfo( unzFile file, unz_global_info *info ) {` |
| 223 | `s` | local / unzGetGlobalInfo | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 223 | `unz_s` | tag / unzGetGlobalInfo | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 232 | `unzNoOpAlternate` | function / unzNoOpAlternate | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void unzNoOpAlternate( void ) {` |
| 240 | `unzlocal_DosDateToTmuDate` | function / unzlocal_DosDateToTmuDate | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static void unzlocal_DosDateToTmuDate (uLong ulDosDate, tm_unz* ptm)` |
| 240 | `ulDosDate` | parameter / unzlocal_DosDateToTmuDate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void unzlocal_DosDateToTmuDate (uLong ulDosDate, tm_unz* ptm)` |
| 240 | `ptm` | parameter / unzlocal_DosDateToTmuDate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static void unzlocal_DosDateToTmuDate (uLong ulDosDate, tm_unz* ptm)` |
| 242 | `uDate` | local / unzlocal_DosDateToTmuDate | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uDate;` |
| 258 | `unzGetCurrentFileInfoPosition` | function / unzGetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzGetCurrentFileInfoPosition( unzFile file, unsigned long *position ) {` |
| 258 | `file` | parameter / unzGetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfoPosition( unzFile file, unsigned long *position ) {` |
| 258 | `position` | parameter / unzGetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfoPosition( unzFile file, unsigned long *position ) {` |
| 259 | `s` | local / unzGetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 259 | `unz_s` | tag / unzGetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 274 | `unzReadCurrentFile` | function / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzReadCurrentFile  (unzFile file, void *buf, unsigned len)` |
| 274 | `file` | parameter / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzReadCurrentFile  (unzFile file, void *buf, unsigned len)` |
| 274 | `buf` | parameter / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzReadCurrentFile  (unzFile file, void *buf, unsigned len)` |
| 274 | `len` | parameter / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzReadCurrentFile  (unzFile file, void *buf, unsigned len)` |
| 276 | `err` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err=UNZ_OK;` |
| 277 | `iRead` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt iRead = 0;` |
| 278 | `s` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 279 | `pfile_in_zip_read_info` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `file_in_zip_read_info_s* pfile_in_zip_read_info;` |
| 307 | `uReadThis` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt uReadThis = UNZ_BUFSIZE;` |
| 331 | `uDoCopy` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt uDoCopy,i ;` |
| 331 | `i` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt uDoCopy,i ;` |
| 355 | `uTotalOutBefore` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uTotalOutBefore,uTotalOutAfter;` |
| 355 | `uTotalOutAfter` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uTotalOutBefore,uTotalOutAfter;` |
| 356 | `bufBefore` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const Byte *bufBefore;` |
| 357 | `uOutThis` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uOutThis;` |
| 358 | `flush` | local / unzReadCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int flush=Z_SYNC_FLUSH;` |
| 400 | `unztell` | function / unztell | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `long unztell( unzFile file ) {` |
| 400 | `file` | parameter / unztell | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `long unztell( unzFile file ) {` |
| 401 | `s` | local / unztell | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 401 | `unz_s` | tag / unztell | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 402 | `read_info` | local / unztell | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `file_in_zip_read_info_s *read_info;` |
| 419 | `unzeof` | function / unzeof | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzeof (unzFile file)` |
| 419 | `file` | parameter / unzeof | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzeof (unzFile file)` |
| 421 | `s` | local / unzeof | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 422 | `pfile_in_zip_read_info` | local / unzeof | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `file_in_zip_read_info_s* pfile_in_zip_read_info;` |
| 442 | `unzGetLocalExtrafield` | function / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzGetLocalExtrafield (unzFile file,void *buf,unsigned len)` |
| 442 | `file` | parameter / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGetLocalExtrafield (unzFile file,void *buf,unsigned len)` |
| 442 | `buf` | parameter / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGetLocalExtrafield (unzFile file,void *buf,unsigned len)` |
| 442 | `len` | parameter / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGetLocalExtrafield (unzFile file,void *buf,unsigned len)` |
| 444 | `s` | local / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 445 | `pfile_in_zip_read_info` | local / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `file_in_zip_read_info_s* pfile_in_zip_read_info;` |
| 446 | `read_now` | local / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt read_now;` |
| 447 | `size_to_read` | local / unzGetLocalExtrafield | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong size_to_read;` |
| 487 | `unzCloseCurrentFile` | function / unzCloseCurrentFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzCloseCurrentFile( unzFile file ) {` |
| 487 | `file` | parameter / unzCloseCurrentFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzCloseCurrentFile( unzFile file ) {` |
| 488 | `err` | local / unzCloseCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err = UNZ_OK;` |
| 489 | `s` | local / unzCloseCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 489 | `unz_s` | tag / unzCloseCurrentFile | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 490 | `pfile_in_zip_read_info` | local / unzCloseCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `file_in_zip_read_info_s *pfile_in_zip_read_info;` |
| 520 | `unzGetGlobalComment` | function / unzGetGlobalComment | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzGetGlobalComment (unzFile file, char *szComment, uLong uSizeBuf)` |
| 520 | `file` | parameter / unzGetGlobalComment | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGetGlobalComment (unzFile file, char *szComment, uLong uSizeBuf)` |
| 520 | `szComment` | parameter / unzGetGlobalComment | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGetGlobalComment (unzFile file, char *szComment, uLong uSizeBuf)` |
| 520 | `uSizeBuf` | parameter / unzGetGlobalComment | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGetGlobalComment (unzFile file, char *szComment, uLong uSizeBuf)` |
| 522 | `s` | local / unzGetGlobalComment | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 523 | `uReadThis` | local / unzGetGlobalComment | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uReadThis ;` |
| 552 | `unzlocal_getShort` | function / unzlocal_getShort | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int unzlocal_getShort (FILE* fin, uLong *pX)` |
| 552 | `fin` | parameter / unzlocal_getShort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_getShort (FILE* fin, uLong *pX)` |
| 552 | `pX` | parameter / unzlocal_getShort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_getShort (FILE* fin, uLong *pX)` |
| 554 | `v` | local / unzlocal_getShort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `short	v;` |
| 569 | `unzlocal_getLong` | function / unzlocal_getLong | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int unzlocal_getLong (FILE *fin, uLong *pX)` |
| 569 | `fin` | parameter / unzlocal_getLong | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_getLong (FILE *fin, uLong *pX)` |
| 569 | `pX` | parameter / unzlocal_getLong | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_getLong (FILE *fin, uLong *pX)` |
| 571 | `v` | local / unzlocal_getLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		v;` |
| 586 | `unzClose` | function / unzClose | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzClose( unzFile file ) {` |
| 586 | `file` | parameter / unzClose | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzClose( unzFile file ) {` |
| 587 | `s` | local / unzClose | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 587 | `unz_s` | tag / unzClose | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 605 | `unzlocal_GetCurrentFileInfoInternal` | function / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int unzlocal_GetCurrentFileInfoInternal (unzFile file,` |
| 605 | `file` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_GetCurrentFileInfoInternal (unzFile file,` |
| 606 | `pfile_info` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unz_file_info *pfile_info,` |
| 608 | `pfile_info_internal` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `*pfile_info_internal,` |
| 609 | `szFileName` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *szFileName,` |
| 610 | `fileNameBufferSize` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `uLong fileNameBufferSize,` |
| 611 | `extraField` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *extraField,` |
| 612 | `extraFieldBufferSize` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `uLong extraFieldBufferSize,` |
| 613 | `szComment` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *szComment,` |
| 614 | `commentBufferSize` | parameter / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `uLong commentBufferSize)` |
| 616 | `s` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 617 | `file_info` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_file_info file_info;` |
| 618 | `file_info_internal` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_file_info_internal file_info_internal;` |
| 619 | `err` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err=UNZ_OK;` |
| 620 | `uMagic` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uMagic;` |
| 621 | `lSeek` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long lSeek=0;` |
| 687 | `uSizeRead` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uSizeRead ;` |
| 705 | `uSizeRead` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uSizeRead ;` |
| 729 | `uSizeRead` | local / unzlocal_GetCurrentFileInfoInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uSizeRead ;` |
| 767 | `unzGetCurrentFileInfo` | function / unzGetCurrentFileInfo | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info,` |
| 767 | `file` | parameter / unzGetCurrentFileInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info,` |
| 767 | `info` | parameter / unzGetCurrentFileInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGetCurrentFileInfo( unzFile file, unz_file_info *info,` |
| 768 | `filename` | parameter / unzGetCurrentFileInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *filename, unsigned long filename_size,` |
| 768 | `filename_size` | parameter / unzGetCurrentFileInfo | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *filename, unsigned long filename_size,` |
| 769 | `extra` | parameter / unzGetCurrentFileInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *extra, unsigned long extra_size,` |
| 769 | `extra_size` | parameter / unzGetCurrentFileInfo | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void *extra, unsigned long extra_size,` |
| 770 | `comment` | parameter / unzGetCurrentFileInfo | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *comment, unsigned long comment_size ) {` |
| 770 | `comment_size` | parameter / unzGetCurrentFileInfo | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `char *comment, unsigned long comment_size ) {` |
| 780 | `unzGoToFirstFile` | function / unzGoToFirstFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzGoToFirstFile( unzFile file ) {` |
| 780 | `file` | parameter / unzGoToFirstFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzGoToFirstFile( unzFile file ) {` |
| 781 | `err` | local / unzGoToFirstFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err = UNZ_OK;` |
| 782 | `s` | local / unzGoToFirstFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 782 | `unz_s` | tag / unzGoToFirstFile | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 800 | `unzGoToNextFile` | function / unzGoToNextFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzGoToNextFile (unzFile file)` |
| 800 | `file` | parameter / unzGoToNextFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzGoToNextFile (unzFile file)` |
| 802 | `s` | local / unzGoToNextFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 803 | `err` | local / unzGoToNextFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err;` |
| 828 | `unzSetCurrentFileInfoPosition` | function / unzSetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int unzSetCurrentFileInfoPosition( unzFile file, unsigned long position ) {` |
| 828 | `file` | parameter / unzSetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzSetCurrentFileInfoPosition( unzFile file, unsigned long position ) {` |
| 828 | `position` | parameter / unzSetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int unzSetCurrentFileInfoPosition( unzFile file, unsigned long position ) {` |
| 829 | `s` | local / unzSetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct unz_s *s;` |
| 829 | `unz_s` | tag / unzSetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s *s;` |
| 830 | `err` | local / unzSetCurrentFileInfoPosition | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err;` |
| 848 | `unzLocateFile` | function / unzLocateFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzLocateFile (unzFile file, const char *szFileName, int iCaseSensitivity)` |
| 848 | `file` | parameter / unzLocateFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzLocateFile (unzFile file, const char *szFileName, int iCaseSensitivity)` |
| 848 | `szFileName` | parameter / unzLocateFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzLocateFile (unzFile file, const char *szFileName, int iCaseSensitivity)` |
| 848 | `iCaseSensitivity` | parameter / unzLocateFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzLocateFile (unzFile file, const char *szFileName, int iCaseSensitivity)` |
| 850 | `s` | local / unzLocateFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 851 | `err` | local / unzLocateFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err;` |
| 854 | `num_fileSaved` | local / unzLocateFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong num_fileSaved;` |
| 855 | `pos_in_central_dirSaved` | local / unzLocateFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong pos_in_central_dirSaved;` |
| 875 | `szCurrentFileName` | local / unzLocateFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char szCurrentFileName[UNZ_MAXFILENAMEINZIP+1];` |
| 895 | `unzlocal_CheckCurrentFileCoherencyHeader` | function / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static int unzlocal_CheckCurrentFileCoherencyHeader (unz_s* s, uInt* piSizeVar,` |
| 895 | `s` | parameter / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_CheckCurrentFileCoherencyHeader (unz_s* s, uInt* piSizeVar,` |
| 895 | `piSizeVar` | parameter / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int unzlocal_CheckCurrentFileCoherencyHeader (unz_s* s, uInt* piSizeVar,` |
| 896 | `poffset_local_extrafield` | parameter / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `uLong *poffset_local_extrafield,` |
| 897 | `psize_local_extrafield` | parameter / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `uInt *psize_local_extrafield)` |
| 899 | `uMagic` | local / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uMagic,uData,uFlags;` |
| 899 | `uData` | local / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uMagic,uData,uFlags;` |
| 899 | `uFlags` | local / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong uMagic,uData,uFlags;` |
| 900 | `size_filename` | local / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong size_filename;` |
| 901 | `size_extra_field` | local / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong size_extra_field;` |
| 902 | `err` | local / unzlocal_CheckCurrentFileCoherencyHeader | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err=UNZ_OK;` |
| 979 | `unzOpenCurrentFile` | function / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern int unzOpenCurrentFile (unzFile file)` |
| 979 | `file` | parameter / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int unzOpenCurrentFile (unzFile file)` |
| 981 | `err` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err=UNZ_OK;` |
| 982 | `Store` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int Store;` |
| 983 | `iSizeVar` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt iSizeVar;` |
| 984 | `s` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s* s;` |
| 985 | `pfile_in_zip_read_info` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `file_in_zip_read_info_s* pfile_in_zip_read_info;` |
| 986 | `offset_local_extrafield` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong offset_local_extrafield;` |
| 987 | `size_local_extrafield` | local / unzOpenCurrentFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uInt  size_local_extrafield;` |
| 1067 | `unzOpen` | function / unzOpen | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `extern unzFile unzOpen (const char* path)` |
| 1067 | `path` | parameter / unzOpen | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern unzFile unzOpen (const char* path)` |
| 1069 | `us` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s us;` |
| 1070 | `s` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unz_s *s;` |
| 1071 | `central_pos` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong central_pos,uL;` |
| 1071 | `uL` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong central_pos,uL;` |
| 1072 | `fin` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE * fin ;` |
| 1074 | `number_disk` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong number_disk;          /* number of the current dist, used for` |
| 1076 | `number_disk_with_CD` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong number_disk_with_CD;  /* number the the disk with central dir, used` |
| 1078 | `number_entry_CD` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `uLong number_entry_CD;      /* total number of entries in` |
| 1082 | `err` | local / unzOpen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int err=UNZ_OK;` |

## code/qcommon/unzip_layout.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 24 | `Q3MAP_UNZIP_LAYOUT_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_UNZIP_LAYOUT_H` |
| 37 | `tm_unz` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} tm_unz;` |
| 30 | `tm_unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct tm_unz_s {` |
| 31 | `tm_sec` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int tm_sec;` |
| 32 | `tm_min` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int tm_min;` |
| 33 | `tm_hour` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int tm_hour;` |
| 34 | `tm_mday` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int tm_mday;` |
| 35 | `tm_mon` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int tm_mon;` |
| 36 | `tm_year` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int tm_year;` |
| 42 | `unz_global_info` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} unz_global_info;` |
| 39 | `unz_global_info_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct unz_global_info_s {` |
| 40 | `number_entry` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long number_entry;` |
| 41 | `size_comment` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long size_comment;` |
| 60 | `unz_file_info` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} unz_file_info;` |
| 44 | `unz_file_info_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct unz_file_info_s {` |
| 45 | `version` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long version;` |
| 46 | `version_needed` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long version_needed;` |
| 47 | `flag` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long flag;` |
| 48 | `compression_method` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long compression_method;` |
| 49 | `dosDate` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long dosDate;` |
| 50 | `crc` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long crc;` |
| 51 | `compressed_size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long compressed_size;` |
| 52 | `uncompressed_size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long uncompressed_size;` |
| 53 | `size_filename` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long size_filename;` |
| 54 | `size_file_extra` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long size_file_extra;` |
| 55 | `size_file_comment` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long size_file_comment;` |
| 56 | `disk_num_start` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long disk_num_start;` |
| 57 | `internal_fa` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long internal_fa;` |
| 58 | `external_fa` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long external_fa;` |
| 59 | `tmu_date` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `tm_unz tmu_date;` |
| 64 | `unz_file_info_internal` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} unz_file_info_internal;` |
| 62 | `unz_file_info_internal_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct unz_file_info_internal_s {` |
| 63 | `offset_curfile` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long offset_curfile;` |
| 81 | `file_in_zip_read_info_s` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} file_in_zip_read_info_s;` |
| 66 | `file_in_zip_read_info_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct file_in_zip_read_info_s {` |
| 67 | `read_buffer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *read_buffer;` |
| 68 | `stream` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `z_stream stream;` |
| 69 | `pos_in_zipfile` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long pos_in_zipfile;` |
| 70 | `stream_initialised` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long stream_initialised;` |
| 71 | `offset_local_extrafield` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long offset_local_extrafield;` |
| 72 | `size_local_extrafield` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size_local_extrafield;` |
| 73 | `pos_local_extrafield` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long pos_local_extrafield;` |
| 74 | `crc32` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long crc32;` |
| 75 | `crc32_wait` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long crc32_wait;` |
| 76 | `rest_read_compressed` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long rest_read_compressed;` |
| 77 | `rest_read_uncompressed` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long rest_read_uncompressed;` |
| 78 | `file` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `FILE *file;` |
| 79 | `compression_method` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long compression_method;` |
| 80 | `byte_before_the_zipfile` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long byte_before_the_zipfile;` |
| 83 | `unz_read_crc_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_read_crc_offset_check[(offsetof(file_in_zip_read_info_s, crc32) == 80) ? 1 : -1];` |
| 84 | `unz_read_remaining_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_read_remaining_offset_check[(offsetof(file_in_zip_read_info_s, rest_read_uncompressed) == 92) ? 1 : -1];` |
| 86 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct unz_s {` |
| 87 | `file` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `FILE *file;` |
| 88 | `gi` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unz_global_info gi;` |
| 89 | `byte_before_the_zipfile` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long byte_before_the_zipfile;` |
| 90 | `num_file` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long num_file;` |
| 91 | `pos_in_central_dir` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long pos_in_central_dir;` |
| 92 | `current_file_ok` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long current_file_ok;` |
| 93 | `central_pos` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long central_pos;` |
| 94 | `size_central_dir` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long size_central_dir;` |
| 95 | `offset_central_dir` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned long offset_central_dir;` |
| 96 | `cur_file_info` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unz_file_info cur_file_info;` |
| 97 | `cur_file_info_internal` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unz_file_info_internal cur_file_info_internal;` |
| 98 | `pfile_in_zip_read` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct file_in_zip_read_info_s *pfile_in_zip_read;` |
| 98 | `file_in_zip_read_info_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct file_in_zip_read_info_s *pfile_in_zip_read;` |
| 101 | `unz_file_info_size_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_file_info_size_check[(sizeof(unz_file_info) == 80) ? 1 : -1];` |
| 102 | `unz_state_size_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_state_size_check[(sizeof(struct unz_s) == 128) ? 1 : -1];` |
| 102 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef char unz_state_size_check[(sizeof(struct unz_s) == 128) ? 1 : -1];` |
| 103 | `unz_file_info_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_file_info_offset_check[(offsetof(struct unz_s, cur_file_info) == 40) ? 1 : -1];` |
| 103 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef char unz_file_info_offset_check[(offsetof(struct unz_s, cur_file_info) == 40) ? 1 : -1];` |
| 104 | `unz_length_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_length_offset_check[(offsetof(struct unz_s, cur_file_info) + offsetof(unz_file_info, uncompressed_size) == 68) ? 1 : -1];` |
| 104 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef char unz_length_offset_check[(offsetof(struct unz_s, cur_file_info) + offsetof(unz_file_info, uncompressed_size) == 68) ? 1 : -1];` |
| 105 | `unz_internal_info_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_internal_info_offset_check[(offsetof(struct unz_s, cur_file_info_internal) == 120) ? 1 : -1];` |
| 105 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef char unz_internal_info_offset_check[(offsetof(struct unz_s, cur_file_info_internal) == 120) ? 1 : -1];` |
| 106 | `unz_read_state_offset_check` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef char unz_read_state_offset_check[(offsetof(struct unz_s, pfile_in_zip_read) == 124) ? 1 : -1];` |
| 106 | `unz_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef char unz_read_state_offset_check[(offsetof(struct unz_s, pfile_in_zip_read) == 124) ? 1 : -1];` |

## common/bsp_light_disk.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 15 | `BSP_LIGHT_DISK_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define BSP_LIGHT_DISK_H` |
| 25 | `bspLightType_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspLightType_t;` |
| 18 | `BSP_LIGHT_SUN` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_SUN = 1,` |
| 19 | `BSP_LIGHT_POINT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_POINT,` |
| 20 | `BSP_LIGHT_LINEAR` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_LINEAR,` |
| 21 | `BSP_LIGHT_ADJUSTED_POINT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_ADJUSTED_POINT,` |
| 22 | `BSP_LIGHT_SPOT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_SPOT,` |
| 23 | `BSP_LIGHT_AREA` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_AREA,` |
| 24 | `BSP_LIGHT_ADJUSTED_SPOT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `BSP_LIGHT_ADJUSTED_SPOT` |
| 31 | `bspAreaLight_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspAreaLight_t;` |
| 28 | `axis` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float axis[2][3];` |
| 29 | `width` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float width;` |
| 30 | `height` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float height;` |
| 35 | `bspLinearLight_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspLinearLight_t;` |
| 34 | `inverseRange` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float inverseRange;` |
| 40 | `bspAdjustedPointLight_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspAdjustedPointLight_t;` |
| 38 | `quadratic` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float quadratic;` |
| 39 | `constant` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float constant;` |
| 45 | `bspSpotLight_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspSpotLight_t;` |
| 43 | `coneCosine` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float coneCosine;` |
| 44 | `exponent` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int exponent;` |
| 52 | `bspAdjustedSpotLight_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspAdjustedSpotLight_t;` |
| 48 | `quadratic` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float quadratic;` |
| 49 | `constant` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float constant;` |
| 50 | `coneCosine` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float coneCosine;` |
| 51 | `exponent` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int exponent;` |
| 66 | `bspLight_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} bspLight_t;` |
| 55 | `type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int type;` |
| 56 | `color` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float color[3];` |
| 57 | `origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float origin[3];` |
| 58 | `direction` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float direction[3];` |
| 65 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `} data;` |
| 60 | `area` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `bspAreaLight_t area;` |
| 61 | `linear` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `bspLinearLight_t linear;` |
| 62 | `adjustedPoint` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `bspAdjustedPointLight_t adjustedPoint;` |
| 63 | `spot` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `bspSpotLight_t spot;` |
| 64 | `adjustedSpot` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `bspAdjustedSpotLight_t adjustedSpot;` |

## common/bspfile.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 30 | `lightBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `byte lightBytes[MAX_MAP_LIGHTING];` |
| 31 | `dportals` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `DiskGfxPortal dportals[MAX_MAP_BSP_PORTALS];` |
| 32 | `dportalVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `cod_bsp_vertex_t dportalVerts[MAX_MAP_PORTAL_VERTS];` |
| 33 | `cullGroupIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int cullGroupIndexes[MAX_MAP_CULLGROUP_INDEXES];` |
| 34 | `dlights` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `bspLight_t dlights[MAX_MAP_LIGHTS];` |
| 35 | `triangleSurfaces` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `cod_bsp_tri_soup_t triangleSurfaces[MAX_MAP_TRISOUPS];` |
| 36 | `collisionIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `unsigned short collisionIndexes[MAX_MAP_COLLISION_INDEXES];` |
| 37 | `cullGroups` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `DiskGfxCullGroup cullGroups[MAX_MAP_CULLGROUPS];` |
| 38 | `triangleSoupData` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `drawVert_t triangleSoupData[MAX_MAP_DRAW_VERTS];` |
| 39 | `dcells` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `DiskGfxCell dcells[MAX_MAP_CELLS];` |
| 40 | `bspOccluderEdges` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `cod_bsp_occluder_edge_t bspOccluderEdges[MAX_MAP_OCCLUDER_EDGES];` |
| 41 | `bspLightIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `unsigned short bspLightIndexes[MAX_MAP_LIGHT_INDEXES];` |
| 42 | `occluderPlane` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int occluderPlane[MAX_MAP_OCCLUDER_PLANES];` |
| 43 | `daabbtrees` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `DiskGfxAabbTree daabbtrees[MAX_MAP_AABBTREES];` |
| 44 | `drawIndexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `unsigned short drawIndexes[MAX_MAP_DRAW_INDEXES];` |
| 45 | `doccluders` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `DiskGfxOccluder doccluders[MAX_MAP_OCCLUDERS];` |
| 46 | `numnodes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numnodes;` |
| 47 | `numCollisionIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numCollisionIndexes;` |
| 48 | `dmodels` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dmodel_t dmodels[MAX_MAP_MODELS];` |
| 49 | `numleafsurfaces` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numleafsurfaces;` |
| 50 | `dleafs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dleaf_t dleafs[MAX_MAP_LEAFS];` |
| 51 | `dplanes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dplane_t dplanes[MAX_MAP_PLANES];` |
| 52 | `numaabbtreenodes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numaabbtreenodes;` |
| 53 | `numShaders` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numShaders;` |
| 54 | `dshaders` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dshader_t dshaders[MAX_MAP_SHADERS];` |
| 55 | `numCells` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numCells;` |
| 56 | `nummodels` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int nummodels;` |
| 57 | `dbrushsides` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dbrushside_t dbrushsides[MAX_MAP_BRUSHSIDES];` |
| 58 | `numLightBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numLightBytes;` |
| 59 | `numOccluders` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numOccluders;` |
| 60 | `numleafbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numleafbrushes;` |
| 61 | `numVisBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numVisBytes;` |
| 62 | `numplanes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numplanes;` |
| 63 | `numleafs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numleafs;` |
| 64 | `numPortals` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numPortals;` |
| 65 | `numLights` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numLights;` |
| 66 | `visBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `byte visBytes[MAX_MAP_VISIBILITY];` |
| 67 | `numCullGroupIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numCullGroupIndexes;` |
| 68 | `numCullGroups` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numCullGroups;` |
| 69 | `numPatchCollides` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numPatchCollides;` |
| 70 | `patchCollides` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `cod_bsp_collision_surface_t patchCollides[0x2000];` |
| 71 | `numCollisionVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numCollisionVerts;` |
| 72 | `collisionVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `cod_bsp_vertex_t collisionVerts[0x20000];` |
| 73 | `numOccluderPlanes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numOccluderPlanes;` |
| 74 | `numLightIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numLightIndexes;` |
| 75 | `numPortalVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numPortalVerts;` |
| 76 | `numDrawIndexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numDrawIndexes;` |
| 77 | `numDrawVerts` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numDrawVerts;` |
| 78 | `occluderIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `unsigned short occluderIndexes[0x18000];` |
| 79 | `numOccluderIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numOccluderIndexes;` |
| 80 | `numOccluderEdges` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numOccluderEdges;` |
| 81 | `dleafsurfaces` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int dleafsurfaces[MAX_MAP_LEAFFACES];` |
| 82 | `dfogs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dfog_t dfogs[MAX_MAP_FOGS];` |
| 83 | `numTriangleSurfaces` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int numTriangleSurfaces;` |
| 84 | `numbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numbrushes;` |
| 85 | `numFogs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numFogs;` |
| 86 | `dleafbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int dleafbrushes[MAX_MAP_LEAFBRUSHES];` |
| 87 | `dnodes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dnode_t dnodes[MAX_MAP_NODES];` |
| 88 | `numbrushsides` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numbrushsides;` |
| 89 | `entdatasize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int entdatasize;` |
| 90 | `dbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `dbrush_t dbrushes[MAX_MAP_BRUSHES];` |
| 91 | `dEntstring` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `char dEntstring[MAX_MAP_ENTSTRING];` |
| 94 | `num_entities` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int num_entities;` |
| 95 | `entities` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `entity_t entities[MAX_MAP_ENTITIES];` |
| 99 | `COD_BSP_MODEL_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_MODEL_BYTES = 48,` |
| 100 | `COD_BSP_LEAF_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_LEAF_BYTES = 36,` |
| 101 | `COD_BSP_PATCH_COLLISION_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_PATCH_COLLISION_BYTES = 16,` |
| 102 | `COD_BSP_COLLISION_VERTEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_COLLISION_VERTEX_BYTES = 12,` |
| 103 | `COD_BSP_COLLISION_INDEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_COLLISION_INDEX_BYTES = 2,` |
| 104 | `COD_BSP_DRAW_INDEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_DRAW_INDEX_BYTES = 2,` |
| 105 | `COD_BSP_LIGHT_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_LIGHT_BYTES = 72,` |
| 106 | `COD_BSP_LIGHT_INDEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_LIGHT_INDEX_BYTES = 2,` |
| 107 | `COD_BSP_PORTAL_VERTEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_PORTAL_VERTEX_BYTES = 12,` |
| 108 | `COD_BSP_OCCLUDER_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_OCCLUDER_BYTES = 20,` |
| 109 | `COD_BSP_OCCLUDER_PLANE_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_OCCLUDER_PLANE_BYTES = 4,` |
| 110 | `COD_BSP_OCCLUDER_EDGE_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_OCCLUDER_EDGE_BYTES = 4,` |
| 111 | `COD_BSP_OCCLUDER_INDEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_OCCLUDER_INDEX_BYTES = 2,` |
| 112 | `COD_BSP_AABB_TREE_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_AABB_TREE_BYTES = 12,` |
| 113 | `COD_BSP_CELL_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_CELL_BYTES = 52,` |
| 114 | `COD_BSP_PORTAL_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_PORTAL_BYTES = 16,` |
| 115 | `COD_BSP_CULL_GROUP_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_CULL_GROUP_BYTES = 32,` |
| 116 | `COD_BSP_CULL_GROUP_INDEX_BYTES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_CULL_GROUP_INDEX_BYTES = 4,` |
| 117 | `COD_BSP_LIGHTMAP_WIDTH` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_LIGHTMAP_WIDTH = 512,` |
| 118 | `COD_BSP_LIGHTMAP_HEIGHT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_LIGHTMAP_HEIGHT = 512` |
| 128 | `CopyLump` | function / CopyLump | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int CopyLump(dheader_t *header, int lump, void *dest, int size)` |
| 128 | `header` | parameter / CopyLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int CopyLump(dheader_t *header, int lump, void *dest, int size)` |
| 128 | `lump` | parameter / CopyLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int CopyLump(dheader_t *header, int lump, void *dest, int size)` |
| 128 | `dest` | parameter / CopyLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int CopyLump(dheader_t *header, int lump, void *dest, int size)` |
| 128 | `size` | parameter / CopyLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int CopyLump(dheader_t *header, int lump, void *dest, int size)` |
| 130 | `length` | local / CopyLump | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int length, ofs;` |
| 130 | `ofs` | local / CopyLump | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int length, ofs;` |
| 140 | `BspFile_NoOp` | function / BspFile_NoOp | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void BspFile_NoOp(void)` |
| 144 | `BspFile_NoOpAlternate` | function / BspFile_NoOpAlternate | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void BspFile_NoOpAlternate(void)` |
| 148 | `BspFile_FloatIdentity` | function / BspFile_FloatIdentity | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float BspFile_FloatIdentity(float f)` |
| 148 | `f` | parameter / BspFile_FloatIdentity | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float BspFile_FloatIdentity(float f)` |
| 158 | `PrintLumpUsage` | function / PrintLumpUsage | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void PrintLumpUsage(const char *name, int count, int size, float pctMultiplier)` |
| 158 | `name` | parameter / PrintLumpUsage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PrintLumpUsage(const char *name, int count, int size, float pctMultiplier)` |
| 158 | `count` | parameter / PrintLumpUsage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PrintLumpUsage(const char *name, int count, int size, float pctMultiplier)` |
| 158 | `size` | parameter / PrintLumpUsage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PrintLumpUsage(const char *name, int count, int size, float pctMultiplier)` |
| 158 | `pctMultiplier` | parameter / PrintLumpUsage | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void PrintLumpUsage(const char *name, int count, int size, float pctMultiplier)` |
| 160 | `buffer` | local / PrintLumpUsage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char buffer[16];` |
| 174 | `StripTrailing` | function / StripTrailing | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void StripTrailing(char *e)` |
| 174 | `e` | parameter / StripTrailing | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void StripTrailing(char *e)` |
| 176 | `s` | local / StripTrailing | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 191 | `ParseEpair` | function / ParseEpair | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `epair_t *ParseEpair(char *key, char **data_p)` |
| 191 | `key` | parameter / ParseEpair | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `epair_t *ParseEpair(char *key, char **data_p)` |
| 191 | `data_p` | parameter / ParseEpair | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `epair_t *ParseEpair(char *key, char **data_p)` |
| 193 | `ep` | local / ParseEpair | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep;` |
| 194 | `value` | local / ParseEpair | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *value;` |
| 228 | `ParseEntity` | function / ParseEntity | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int ParseEntity(char **data_p)` |
| 228 | `data_p` | parameter / ParseEntity | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int ParseEntity(char **data_p)` |
| 230 | `token` | local / ParseEntity | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *token;` |
| 231 | `ep` | local / ParseEntity | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep;` |
| 232 | `mapent` | local / ParseEntity | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `entity_t *mapent;` |
| 259 | `ParseEntities` | function / ParseEntities | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ParseEntities(void)` |
| 261 | `data` | local / ParseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *data;` |
| 270 | `UnparseEntities` | function / UnparseEntities | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void UnparseEntities(void)` |
| 272 | `buf` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *buf, *end;` |
| 272 | `end` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *buf, *end;` |
| 273 | `ep` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep;` |
| 274 | `line` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char line[2048];` |
| 275 | `i` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 276 | `key` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char key[1024], value[1024];` |
| 276 | `value` | local / UnparseEntities | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char key[1024], value[1024];` |
| 311 | `UnparseEntitiesWithOrigins` | function / UnparseEntitiesWithOrigins | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void UnparseEntitiesWithOrigins(void)` |
| 313 | `buf` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *buf, *end;` |
| 313 | `end` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *buf, *end;` |
| 314 | `ep` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep, *first;` |
| 314 | `first` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep, *first;` |
| 315 | `line` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char line[2048];` |
| 316 | `i` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 317 | `key` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char key[1024], value[1024];` |
| 317 | `value` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char key[1024], value[1024];` |
| 318 | `origin` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char origin[32], search[256], originCopy[256];` |
| 318 | `search` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char origin[32], search[256], originCopy[256];` |
| 318 | `originCopy` | local / UnparseEntitiesWithOrigins | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char origin[32], search[256], originCopy[256];` |
| 319 | `length` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int length = 0;` |
| 320 | `found` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *found;` |
| 321 | `j` | local / UnparseEntitiesWithOrigins | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int j;` |
| 322 | `originPair` | local / UnparseEntitiesWithOrigins | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `epair_t *originPair;` |
| 386 | `PrintEntity` | function / PrintEntity | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void PrintEntity( const entity_t *ent ) {` |
| 386 | `ent` | parameter / PrintEntity | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PrintEntity( const entity_t *ent ) {` |
| 387 | `ep` | local / PrintEntity | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep;` |
| 400 | `SetKeyValue` | function / SetKeyValue | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SetKeyValue(entity_t *ent, const char *key, const char *value)` |
| 400 | `ent` | parameter / SetKeyValue | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SetKeyValue(entity_t *ent, const char *key, const char *value)` |
| 400 | `key` | parameter / SetKeyValue | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SetKeyValue(entity_t *ent, const char *key, const char *value)` |
| 400 | `value` | parameter / SetKeyValue | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SetKeyValue(entity_t *ent, const char *key, const char *value)` |
| 402 | `ep` | local / SetKeyValue | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep;` |
| 425 | `ValueForKey` | function / ValueForKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `const char *ValueForKey(const entity_t *ent, const char *key)` |
| 425 | `ent` | parameter / ValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *ValueForKey(const entity_t *ent, const char *key)` |
| 425 | `key` | parameter / ValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *ValueForKey(const entity_t *ent, const char *key)` |
| 427 | `ep` | local / ValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `epair_t *ep;` |
| 442 | `FloatForKey` | function / FloatForKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `vec_t FloatForKey(const entity_t *ent, const char *key)` |
| 442 | `ent` | parameter / FloatForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t FloatForKey(const entity_t *ent, const char *key)` |
| 442 | `key` | parameter / FloatForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t FloatForKey(const entity_t *ent, const char *key)` |
| 444 | `k` | local / FloatForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *k;` |
| 455 | `GetVectorForKey` | function / GetVectorForKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void GetVectorForKey(const entity_t *ent, const char *key, vec3_t vec)` |
| 455 | `ent` | parameter / GetVectorForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void GetVectorForKey(const entity_t *ent, const char *key, vec3_t vec)` |
| 455 | `key` | parameter / GetVectorForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void GetVectorForKey(const entity_t *ent, const char *key, vec3_t vec)` |
| 455 | `vec` | parameter / GetVectorForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void GetVectorForKey(const entity_t *ent, const char *key, vec3_t vec)` |
| 457 | `k` | local / GetVectorForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *k;` |
| 458 | `v1` | local / GetVectorForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double v1, v2, v3;` |
| 458 | `v2` | local / GetVectorForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double v1, v2, v3;` |
| 458 | `v3` | local / GetVectorForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double v1, v2, v3;` |
| 459 | `count` | local / GetVectorForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int count;` |
| 479 | `SwapBlock` | function / SwapBlock | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SwapBlock(int *block, int sizeOfBlock)` |
| 479 | `block` | parameter / SwapBlock | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SwapBlock(int *block, int sizeOfBlock)` |
| 479 | `sizeOfBlock` | parameter / SwapBlock | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SwapBlock(int *block, int sizeOfBlock)` |
| 481 | `i` | local / SwapBlock | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 493 | `SwapBSPBrush` | function / SwapBSPBrush | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SwapBSPBrush(cod_bsp_brush_t *brush)` |
| 493 | `brush` | parameter / SwapBSPBrush | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SwapBSPBrush(cod_bsp_brush_t *brush)` |
| 504 | `SwapTriangleSurface` | function / SwapTriangleSurface | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SwapTriangleSurface(cod_bsp_tri_soup_t *surface)` |
| 504 | `surface` | parameter / SwapTriangleSurface | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SwapTriangleSurface(cod_bsp_tri_soup_t *surface)` |
| 521 | `SwapBSPFile` | function / SwapBSPFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SwapBSPFile( void ) {` |
| 522 | `i` | local / SwapBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 523 | `swaptest` | local / SwapBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte swaptest[2] = { 1, 0 };` |
| 634 | `LoadBSPFile` | function / LoadBSPFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadBSPFile( const char *filename ) {` |
| 634 | `filename` | parameter / LoadBSPFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadBSPFile( const char *filename ) {` |
| 635 | `header` | local / LoadBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `dheader_t *header;` |
| 690 | `AddLump` | function / AddLump | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AddLump(FILE *bspfile, dheader_t *header, int lumpnum,` |
| 690 | `bspfile` | parameter / AddLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLump(FILE *bspfile, dheader_t *header, int lumpnum,` |
| 690 | `header` | parameter / AddLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLump(FILE *bspfile, dheader_t *header, int lumpnum,` |
| 690 | `lumpnum` | parameter / AddLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLump(FILE *bspfile, dheader_t *header, int lumpnum,` |
| 691 | `data` | parameter / AddLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const void *data, int len)` |
| 691 | `len` | parameter / AddLump | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const void *data, int len)` |
| 693 | `lump` | local / AddLump | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `lump_t *lump;` |
| 701 | `WriteBSPFile` | function / WriteBSPFile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void WriteBSPFile( const char *filename ) {` |
| 701 | `filename` | parameter / WriteBSPFile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteBSPFile( const char *filename ) {` |
| 702 | `outheader` | local / WriteBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `dheader_t outheader, *header;` |
| 702 | `header` | local / WriteBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `dheader_t outheader, *header;` |
| 703 | `bspfile` | local / WriteBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *bspfile;` |
| 704 | `attributes` | local / WriteBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `DWORD attributes;` |
| 705 | `text` | local / WriteBSPFile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char text[MAX_OS_PATH];` |
| 806 | `PrintBSPFileSizes` | function / PrintBSPFileSizes | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void PrintBSPFileSizes(int fileSize)` |
| 806 | `fileSize` | parameter / PrintBSPFileSizes | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PrintBSPFileSizes(int fileSize)` |
| 808 | `pct` | local / PrintBSPFileSizes | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float pct;` |

## common/bspfile.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 33 | `nummodels` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			nummodels;` |
| 34 | `dmodels` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dmodel_t	dmodels[MAX_MAP_MODELS];` |
| 36 | `numShaders` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numShaders;` |
| 37 | `dshaders` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dshader_t	dshaders[MAX_MAP_SHADERS];` |
| 39 | `entdatasize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			entdatasize;` |
| 40 | `dEntstring` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern	char		dEntstring[MAX_MAP_ENTSTRING];` |
| 42 | `numleafs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numleafs;` |
| 43 | `dleafs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dleaf_t		dleafs[MAX_MAP_LEAFS];` |
| 45 | `numplanes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numplanes;` |
| 46 | `dplanes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dplane_t	dplanes[MAX_MAP_PLANES];` |
| 48 | `numnodes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numnodes;` |
| 49 | `dnodes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dnode_t		dnodes[MAX_MAP_NODES];` |
| 51 | `numleafsurfaces` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numleafsurfaces;` |
| 52 | `dleafsurfaces` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			dleafsurfaces[MAX_MAP_LEAFFACES];` |
| 54 | `numleafbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numleafbrushes;` |
| 55 | `dleafbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			dleafbrushes[MAX_MAP_LEAFBRUSHES];` |
| 57 | `numbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numbrushes;` |
| 58 | `dbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dbrush_t	dbrushes[MAX_MAP_BRUSHES];` |
| 60 | `numbrushsides` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numbrushsides;` |
| 61 | `dbrushsides` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dbrushside_t	dbrushsides[MAX_MAP_BRUSHSIDES];` |
| 63 | `numLightBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numLightBytes;` |
| 64 | `lightBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	byte		lightBytes[];` |
| 66 | `numGridPoints` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numGridPoints;` |
| 67 | `gridData` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	byte		gridData[MAX_MAP_LIGHTGRID];` |
| 69 | `numVisBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numVisBytes;` |
| 70 | `visBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	byte		visBytes[MAX_MAP_VISIBILITY];` |
| 72 | `numDrawVerts` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numDrawVerts;` |
| 74 | `numDrawIndexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numDrawIndexes;` |
| 76 | `numTriangleSurfaces` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern	int			numTriangleSurfaces;` |
| 78 | `numFogs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			numFogs;` |
| 79 | `dfogs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	dfog_t		dfogs[MAX_MAP_FOGS];` |
| 81 | `LoadBSPFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	LoadBSPFile( const char *filename );` |
| 81 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	LoadBSPFile( const char *filename );` |
| 82 | `WriteBSPFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	WriteBSPFile( const char *filename );` |
| 82 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WriteBSPFile( const char *filename );` |
| 83 | `PrintBSPFileSizes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void PrintBSPFileSizes( int fileSize );` |
| 83 | `fileSize` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PrintBSPFileSizes( int fileSize );` |
| 92 | `epair_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} epair_t;` |
| 88 | `epair_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct epair_s {` |
| 89 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct epair_s	*next;` |
| 89 | `epair_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct epair_s	*next;` |
| 90 | `key` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	*key;` |
| 91 | `value` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	*value;` |
| 101 | `entity_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} entity_t;` |
| 95 | `origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t		origin;` |
| 96 | `brushes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct bspbrush_s	*brushes;` |
| 96 | `bspbrush_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct bspbrush_s	*brushes;` |
| 97 | `patches` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct parseMesh_s	*patches;` |
| 97 | `parseMesh_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct parseMesh_s	*patches;` |
| 98 | `terrainSurfaces` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct terrainSurface_s *terrainSurfaces;	// intermediate terrain meshes, emitted by SubdivideTerrain` |
| 98 | `terrainSurface_s` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `struct terrainSurface_s *terrainSurfaces;	// intermediate terrain meshes, emitted by SubdivideTerrain` |
| 99 | `firstDrawSurf` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int			firstDrawSurf;` |
| 100 | `epairs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `epair_t		*epairs;` |
| 103 | `num_entities` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int			num_entities;` |
| 104 | `entities` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	entity_t	entities[MAX_MAP_ENTITIES];` |
| 106 | `ParseEntities` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	ParseEntities( void );` |
| 107 | `UnparseEntities` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	UnparseEntities( void );` |
| 108 | `UnparseEntitiesWithOrigins` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void UnparseEntitiesWithOrigins( void );` |
| 110 | `SetKeyValue` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	SetKeyValue( entity_t *ent, const char *key, const char *value );` |
| 110 | `ent` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	SetKeyValue( entity_t *ent, const char *key, const char *value );` |
| 110 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	SetKeyValue( entity_t *ent, const char *key, const char *value );` |
| 110 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	SetKeyValue( entity_t *ent, const char *key, const char *value );` |
| 111 | `ValueForKey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const char 	*ValueForKey( const entity_t *ent, const char *key );` |
| 111 | `ent` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char 	*ValueForKey( const entity_t *ent, const char *key );` |
| 111 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char 	*ValueForKey( const entity_t *ent, const char *key );` |
| 114 | `FloatForKey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t	FloatForKey( const entity_t *ent, const char *key );` |
| 114 | `ent` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t	FloatForKey( const entity_t *ent, const char *key );` |
| 114 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t	FloatForKey( const entity_t *ent, const char *key );` |
| 115 | `GetVectorForKey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	GetVectorForKey( const entity_t *ent, const char *key, vec3_t vec );` |
| 115 | `ent` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	GetVectorForKey( const entity_t *ent, const char *key, vec3_t vec );` |
| 115 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	GetVectorForKey( const entity_t *ent, const char *key, vec3_t vec );` |
| 115 | `vec` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	GetVectorForKey( const entity_t *ent, const char *key, vec3_t vec );` |
| 119 | `ParseEpair` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `epair_t *ParseEpair( char *key, char **data_p );` |
| 119 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `epair_t *ParseEpair( char *key, char **data_p );` |
| 119 | `data_p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `epair_t *ParseEpair( char *key, char **data_p );` |
| 121 | `PrintEntity` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	PrintEntity( const entity_t *ent );` |
| 121 | `ent` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	PrintEntity( const entity_t *ent );` |

## common/cmdlib.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 26 | `__CMDLIB__` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define __CMDLIB__` |
| 57 | `__BYTEBOOL__` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define __BYTEBOOL__` |
| 58 | `qboolean` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef enum { qfalse, qtrue } qboolean;` |
| 58 | `qfalse` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `typedef enum { qfalse, qtrue } qboolean;` |
| 58 | `qtrue` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `typedef enum { qfalse, qtrue } qboolean;` |
| 59 | `byte` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef unsigned char byte;` |
| 62 | `MAX_OS_PATH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_OS_PATH		1024` |
| 63 | `MEM_BLOCKSIZE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MEM_BLOCKSIZE 4096` |
| 66 | `myoffsetof` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define myoffsetof(type,identifier) ((size_t)&((type *)0)->identifier)` |
| 70 | `myargc` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int myargc;` |
| 71 | `myargv` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern char **myargv;` |
| 73 | `strupr` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *strupr (char *in);` |
| 73 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *strupr (char *in);` |
| 74 | `strlower` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *strlower (char *in);` |
| 74 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *strlower (char *in);` |
| 75 | `Q_strncasecmp` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_strncasecmp( const char *s1, const char *s2, int n );` |
| 75 | `s1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncasecmp( const char *s1, const char *s2, int n );` |
| 75 | `s2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncasecmp( const char *s1, const char *s2, int n );` |
| 75 | `n` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncasecmp( const char *s1, const char *s2, int n );` |
| 76 | `Q_stricmp` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_stricmp( const char *s1, const char *s2 );` |
| 76 | `s1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmp( const char *s1, const char *s2 );` |
| 76 | `s2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmp( const char *s1, const char *s2 );` |
| 77 | `Q_getwd` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Q_getwd( char *out );` |
| 77 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_getwd( char *out );` |
| 79 | `Q_filelength` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_filelength (FILE *f);` |
| 79 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_filelength (FILE *f);` |
| 80 | `FileTime` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	FileTime( const char *path );` |
| 80 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int	FileTime( const char *path );` |
| 82 | `Q_mkdir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	Q_mkdir( const char *path );` |
| 82 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	Q_mkdir( const char *path );` |
| 84 | `qdir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char		qdir[1024];` |
| 85 | `gamedir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char		gamedir[1024];` |
| 86 | `writedir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern  char		writedir[1024];` |
| 87 | `SetQdirFromPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void SetQdirFromPath( const char *path, const char *baseDir );` |
| 87 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SetQdirFromPath( const char *path, const char *baseDir );` |
| 87 | `baseDir` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void SetQdirFromPath( const char *path, const char *baseDir );` |
| 88 | `ExpandArg` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *ExpandArg( const char *path );	// from cmd line` |
| 88 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *ExpandArg( const char *path );	// from cmd line` |
| 89 | `ExpandPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *ExpandPath( const char *path );	// from scripts` |
| 89 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *ExpandPath( const char *path );	// from scripts` |
| 90 | `ExpandGamePath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *ExpandGamePath (const char *path);` |
| 90 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *ExpandGamePath (const char *path);` |
| 91 | `ExpandPathAndArchive` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *ExpandPathAndArchive( const char *path );` |
| 91 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *ExpandPathAndArchive( const char *path );` |
| 94 | `I_FloatTime` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `double I_FloatTime( void );` |
| 96 | `Error` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	Error( const char *error, ... );` |
| 96 | `error` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	Error( const char *error, ... );` |
| 97 | `CheckParm` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int		CheckParm( const char *check );` |
| 97 | `check` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		CheckParm( const char *check );` |
| 99 | `SafeOpenWrite` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `FILE	*SafeOpenWrite( const char *filename );` |
| 99 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `FILE	*SafeOpenWrite( const char *filename );` |
| 100 | `SafeOpenRead` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `FILE	*SafeOpenRead( const char *filename );` |
| 100 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `FILE	*SafeOpenRead( const char *filename );` |
| 101 | `SafeRead` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	SafeRead (FILE *f, void *buffer, int count);` |
| 101 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SafeRead (FILE *f, void *buffer, int count);` |
| 101 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SafeRead (FILE *f, void *buffer, int count);` |
| 101 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SafeRead (FILE *f, void *buffer, int count);` |
| 102 | `SafeWrite` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	SafeWrite (FILE *f, const void *buffer, int count);` |
| 102 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SafeWrite (FILE *f, const void *buffer, int count);` |
| 102 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SafeWrite (FILE *f, const void *buffer, int count);` |
| 102 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SafeWrite (FILE *f, const void *buffer, int count);` |
| 104 | `LoadFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int		LoadFile( const char *filename, void **bufferptr );` |
| 104 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		LoadFile( const char *filename, void **bufferptr );` |
| 104 | `bufferptr` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		LoadFile( const char *filename, void **bufferptr );` |
| 105 | `LoadFileBlock` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int   LoadFileBlock( const char *filename, void **bufferptr );` |
| 105 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int   LoadFileBlock( const char *filename, void **bufferptr );` |
| 105 | `bufferptr` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int   LoadFileBlock( const char *filename, void **bufferptr );` |
| 106 | `TryLoadFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int		TryLoadFile( const char *filename, void **bufferptr );` |
| 106 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		TryLoadFile( const char *filename, void **bufferptr );` |
| 106 | `bufferptr` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		TryLoadFile( const char *filename, void **bufferptr );` |
| 107 | `SaveFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	SaveFile( const char *filename, const void *buffer, int count );` |
| 107 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SaveFile( const char *filename, const void *buffer, int count );` |
| 107 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SaveFile( const char *filename, const void *buffer, int count );` |
| 107 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	SaveFile( const char *filename, const void *buffer, int count );` |
| 108 | `FileExists` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean	FileExists( const char *filename );` |
| 108 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean	FileExists( const char *filename );` |
| 110 | `DefaultExtension` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	DefaultExtension( char *path, const char *extension );` |
| 110 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	DefaultExtension( char *path, const char *extension );` |
| 110 | `extension` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	DefaultExtension( char *path, const char *extension );` |
| 111 | `DefaultPath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	DefaultPath( char *path, const char *basepath );` |
| 111 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	DefaultPath( char *path, const char *basepath );` |
| 111 | `basepath` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	DefaultPath( char *path, const char *basepath );` |
| 112 | `StripFilename` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	StripFilename( char *path );` |
| 112 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	StripFilename( char *path );` |
| 113 | `StripExtension` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	StripExtension( char *path );` |
| 113 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	StripExtension( char *path );` |
| 115 | `ExtractFilePath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	ExtractFilePath( const char *path, char *dest );` |
| 115 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	ExtractFilePath( const char *path, char *dest );` |
| 115 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	ExtractFilePath( const char *path, char *dest );` |
| 116 | `ExtractFileBase` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void 	ExtractFileBase( const char *path, char *dest );` |
| 116 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	ExtractFileBase( const char *path, char *dest );` |
| 116 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void 	ExtractFileBase( const char *path, char *dest );` |
| 117 | `ExtractFileExtension` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	ExtractFileExtension( const char *path, char *dest );` |
| 117 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ExtractFileExtension( const char *path, char *dest );` |
| 117 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ExtractFileExtension( const char *path, char *dest );` |
| 119 | `ParseNum` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int 	ParseNum (const char *str);` |
| 119 | `str` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int 	ParseNum (const char *str);` |
| 121 | `BigShort` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `short	BigShort (short l);` |
| 121 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `short	BigShort (short l);` |
| 122 | `LittleShort` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define LittleShort( x ) ( x )` |
| 123 | `BigLong` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int		BigLong (int l);` |
| 123 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		BigLong (int l);` |
| 124 | `LittleLong` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define LittleLong( x ) ( x )` |
| 125 | `BigFloat` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float	BigFloat (float l);` |
| 125 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float	BigFloat (float l);` |
| 126 | `LittleFloat` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define LittleFloat( x ) ( x )` |
| 129 | `COM_Parse` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *COM_Parse (char *data);` |
| 129 | `data` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *COM_Parse (char *data);` |
| 131 | `com_token` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char		com_token[1024];` |
| 132 | `com_eof` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	qboolean	com_eof;` |
| 134 | `copystring` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *copystring(const char *s);` |
| 134 | `s` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *copystring(const char *s);` |
| 137 | `CRC_Init` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void CRC_Init(unsigned short *crcvalue);` |
| 137 | `crcvalue` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CRC_Init(unsigned short *crcvalue);` |
| 138 | `CRC_ProcessByte` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void CRC_ProcessByte(unsigned short *crcvalue, byte data);` |
| 138 | `crcvalue` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CRC_ProcessByte(unsigned short *crcvalue, byte data);` |
| 138 | `data` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CRC_ProcessByte(unsigned short *crcvalue, byte data);` |
| 139 | `CRC_Value` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `unsigned short CRC_Value(unsigned short crcvalue);` |
| 139 | `crcvalue` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned short CRC_Value(unsigned short crcvalue);` |
| 141 | `CreatePath` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	CreatePath( const char *path );` |
| 141 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	CreatePath( const char *path );` |
| 142 | `QCopyFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	QCopyFile( const char *from, const char *to );` |
| 142 | `from` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	QCopyFile( const char *from, const char *to );` |
| 142 | `to` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	QCopyFile( const char *from, const char *to );` |
| 144 | `archive` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	qboolean		archive;` |
| 145 | `archivedir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char			archivedir[1024];` |
| 148 | `verbose` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	qboolean verbose;` |
| 149 | `qprintf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void qprintf( const char *format, ... );` |
| 149 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void qprintf( const char *format, ... );` |
| 150 | `_printf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _printf( const char *format, ... );` |
| 150 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _printf( const char *format, ... );` |
| 152 | `ExpandWildcards` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ExpandWildcards( int *argc, char ***argv );` |
| 152 | `argc` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandWildcards( int *argc, char ***argv );` |
| 152 | `argv` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandWildcards( int *argc, char ***argv );` |
| 160 | `cblock_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} cblock_t;` |
| 158 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `void	*data;` |
| 159 | `count` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		count, width, height;` |
| 159 | `width` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		count, width, height;` |
| 159 | `height` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		count, width, height;` |

## common/cmdlib_path.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 11 | `__CMDLIB_PATH__` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define __CMDLIB_PATH__` |
| 18 | `ExtractFileName` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ExtractFileName( const char *path, char *dest );` |
| 18 | `path` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExtractFileName( const char *path, char *dest );` |
| 18 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExtractFileName( const char *path, char *dest );` |

## common/cod_bsp_disk_records.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 14 | `COD_BSP_DISK_RECORDS_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define COD_BSP_DISK_RECORDS_H` |
| 15 | `cod_bsp_brush_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef dbrush_t cod_bsp_brush_t;` |
| 16 | `cod_bsp_vertex_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `typedef float cod_bsp_vertex_t[3];` |
| 24 | `cod_bsp_tri_soup_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} cod_bsp_tri_soup_t;` |
| 18 | `material` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short material;` |
| 19 | `lightStyle` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short lightStyle;` |
| 20 | `firstVert` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstVert;` |
| 21 | `numVerts` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short numVerts;` |
| 22 | `numIndices` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short numIndices;` |
| 23 | `firstIndex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstIndex;` |
| 30 | `DiskGfxCullGroup` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} DiskGfxCullGroup;` |
| 26 | `mins` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float mins[3];` |
| 27 | `maxs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float maxs[3];` |
| 28 | `firstSurface` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstSurface;` |
| 29 | `surfaceCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int surfaceCount;` |
| 35 | `DiskGfxAabbTree` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} DiskGfxAabbTree;` |
| 32 | `firstSurface` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstSurface;` |
| 33 | `surfaceCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int surfaceCount;` |
| 34 | `childCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int childCount;` |
| 46 | `DiskGfxCell` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} DiskGfxCell;` |
| 37 | `mins` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float mins[3];` |
| 38 | `maxs` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float maxs[3];` |
| 39 | `aabbTreeIndex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int aabbTreeIndex;` |
| 40 | `firstPortal` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstPortal;` |
| 41 | `portalCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int portalCount;` |
| 42 | `firstCullGroup` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstCullGroup;` |
| 43 | `cullGroupCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int cullGroupCount;` |
| 44 | `firstOccluder` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstOccluder;` |
| 45 | `occluderCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int occluderCount;` |
| 52 | `DiskGfxPortal` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} DiskGfxPortal;` |
| 48 | `planeIndex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int planeIndex;` |
| 49 | `cellIndex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int cellIndex;` |
| 50 | `firstPortalVertex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstPortalVertex;` |
| 51 | `portalVertexCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int portalVertexCount;` |
| 60 | `DiskGfxOccluder` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} DiskGfxOccluder;` |
| 54 | `firstPlane` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstPlane;` |
| 55 | `planeCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short planeCount;` |
| 56 | `edgeCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short edgeCount;` |
| 57 | `firstEdge` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstEdge;` |
| 58 | `firstPortalVertex` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstPortalVertex;` |
| 59 | `portalVertexCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short portalVertexCount;` |
| 64 | `cod_bsp_occluder_edge_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} cod_bsp_occluder_edge_t;` |
| 62 | `plane` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char plane[2];` |
| 63 | `vertex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char vertex[2];` |
| 82 | `cod_bsp_collision_surface_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} cod_bsp_collision_surface_t;` |
| 66 | `material` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short material;` |
| 67 | `isTerrain` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char isTerrain;` |
| 81 | `geometry` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `} geometry;` |
| 74 | `patch` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `} patch;` |
| 70 | `width` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short width;` |
| 71 | `height` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short height;` |
| 72 | `subdivisions` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int subdivisions;` |
| 73 | `firstVertex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstVertex;` |
| 80 | `terrain` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `} terrain;` |
| 76 | `numVerts` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short numVerts;` |
| 77 | `numIndices` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short numIndices;` |
| 78 | `firstVertex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstVertex;` |
| 79 | `firstIndex` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int firstIndex;` |

## common/cod_bsp_load_storage.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 12 | `COD_BSP_LOAD_STORAGE_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define COD_BSP_LOAD_STORAGE_H` |
| 17 | `COD_BSP_MAX_TRIANGLE_SURFACES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_MAX_TRIANGLE_SURFACES = 131072,` |
| 18 | `COD_BSP_MAX_LIGHTS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_MAX_LIGHTS = 2048,` |
| 19 | `COD_BSP_MAX_LIGHT_INDEXES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_BSP_MAX_LIGHT_INDEXES = 65536` |
| 21 | `numShaders` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numShaders;` |
| 22 | `dshaders` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dshader_t dshaders[];` |
| 23 | `numLightBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numLightBytes;` |
| 24 | `lightBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern byte lightBytes[];` |
| 25 | `numplanes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numplanes;` |
| 26 | `dplanes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dplane_t dplanes[];` |
| 27 | `numbrushsides` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numbrushsides;` |
| 28 | `dbrushsides` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dbrushside_t dbrushsides[];` |
| 29 | `numbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numbrushes;` |
| 30 | `dbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dbrush_t dbrushes[];` |
| 31 | `numFogs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numFogs;` |
| 32 | `dfogs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dfog_t dfogs[];` |
| 33 | `numTriangleSurfaces` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numTriangleSurfaces;` |
| 34 | `triangleSurfaces` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern cod_bsp_tri_soup_t triangleSurfaces[];` |
| 35 | `numDrawVerts` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numDrawVerts;` |
| 36 | `triangleSoupData` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern drawVert_t triangleSoupData[];` |
| 37 | `numDrawIndexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numDrawIndexes;` |
| 38 | `drawIndexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern unsigned short drawIndexes[];` |
| 39 | `numCullGroups` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numCullGroups;` |
| 40 | `cullGroups` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern DiskGfxCullGroup cullGroups[];` |
| 41 | `numCullGroupIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numCullGroupIndexes;` |
| 42 | `cullGroupIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int cullGroupIndexes[];` |
| 43 | `numPortalVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numPortalVerts;` |
| 44 | `dportalVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern cod_bsp_vertex_t dportalVerts[];` |
| 45 | `numOccluders` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numOccluders;` |
| 46 | `doccluders` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern DiskGfxOccluder doccluders[];` |
| 47 | `numOccluderPlanes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numOccluderPlanes;` |
| 48 | `occluderPlane` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int occluderPlane[];` |
| 49 | `numOccluderEdges` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numOccluderEdges;` |
| 50 | `bspOccluderEdges` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern cod_bsp_occluder_edge_t bspOccluderEdges[];` |
| 51 | `numOccluderIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numOccluderIndexes;` |
| 52 | `occluderIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern unsigned short occluderIndexes[];` |
| 53 | `numaabbtreenodes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numaabbtreenodes;` |
| 54 | `daabbtrees` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern DiskGfxAabbTree daabbtrees[];` |
| 55 | `numCells` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numCells;` |
| 56 | `dcells` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern DiskGfxCell dcells[];` |
| 57 | `numPortals` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numPortals;` |
| 58 | `dportals` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern DiskGfxPortal dportals[];` |
| 59 | `numLightIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numLightIndexes;` |
| 60 | `bspLightIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern unsigned short bspLightIndexes[];` |
| 61 | `numnodes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numnodes;` |
| 62 | `dnodes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dnode_t dnodes[];` |
| 63 | `numleafs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numleafs;` |
| 64 | `dleafs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dleaf_t dleafs[];` |
| 65 | `numleafbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numleafbrushes;` |
| 66 | `dleafbrushes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int dleafbrushes[];` |
| 67 | `numleafsurfaces` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numleafsurfaces;` |
| 68 | `dleafsurfaces` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int dleafsurfaces[];` |
| 69 | `numPatchCollides` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numPatchCollides;` |
| 70 | `patchCollides` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern cod_bsp_collision_surface_t patchCollides[];` |
| 71 | `numCollisionVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numCollisionVerts;` |
| 72 | `collisionVerts` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern cod_bsp_vertex_t collisionVerts[];` |
| 73 | `numCollisionIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern int numCollisionIndexes;` |
| 74 | `collisionIndexes` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern unsigned short collisionIndexes[];` |
| 75 | `nummodels` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int nummodels;` |
| 76 | `dmodels` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern dmodel_t dmodels[];` |
| 77 | `numLights` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numLights;` |
| 78 | `dlights` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern bspLight_t dlights[];` |
| 79 | `numVisBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numVisBytes;` |
| 80 | `visBytes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern byte visBytes[];` |
| 81 | `entdatasize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int entdatasize;` |
| 82 | `dEntstring` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern char dEntstring[];` |
| 83 | `SwapBSPFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void SwapBSPFile( void );` |

## common/cod_bsp_lump_indices.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 13 | `COD_BSP_LUMP_INDICES_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define COD_BSP_LUMP_INDICES_H` |
| 14 | `COD_BSP_IDENT` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define COD_BSP_IDENT 0x50534249` |
| 15 | `COD_BSP_VERSION` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define COD_BSP_VERSION 59` |
| 48 | `cod_bsp_lump_index_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} cod_bsp_lump_index_t;` |
| 17 | `COD_LUMP_SHADERS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_SHADERS,` |
| 18 | `COD_LUMP_LIGHTMAPS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_LIGHTMAPS,` |
| 19 | `COD_LUMP_PLANES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_PLANES,` |
| 20 | `COD_LUMP_BRUSHSIDES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_BRUSHSIDES,` |
| 21 | `COD_LUMP_BRUSHES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_BRUSHES,` |
| 22 | `COD_LUMP_FOGS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_FOGS,` |
| 23 | `COD_LUMP_TRIANGLE_SOUPS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_TRIANGLE_SOUPS,` |
| 24 | `COD_LUMP_DRAWVERTS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_DRAWVERTS,` |
| 25 | `COD_LUMP_DRAWINDEXES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_DRAWINDEXES,` |
| 26 | `COD_LUMP_CULLGROUPS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_CULLGROUPS,` |
| 27 | `COD_LUMP_CULLGROUPINDEXES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_CULLGROUPINDEXES,` |
| 28 | `COD_LUMP_PORTALVERTS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_PORTALVERTS,` |
| 29 | `COD_LUMP_OCCLUDERS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_OCCLUDERS,` |
| 30 | `COD_LUMP_OCCLUDERPLANES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_OCCLUDERPLANES,` |
| 31 | `COD_LUMP_OCCLUDEREDGES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_OCCLUDEREDGES,` |
| 32 | `COD_LUMP_OCCLUDERINDEXES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_OCCLUDERINDEXES,` |
| 33 | `COD_LUMP_AABBTREES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_AABBTREES,` |
| 34 | `COD_LUMP_CELLS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_CELLS,` |
| 35 | `COD_LUMP_PORTALS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_PORTALS,` |
| 36 | `COD_LUMP_LIGHTINDEXES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_LIGHTINDEXES,` |
| 37 | `COD_LUMP_NODES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_NODES,` |
| 38 | `COD_LUMP_LEAFS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_LEAFS,` |
| 39 | `COD_LUMP_LEAFBRUSHES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_LEAFBRUSHES,` |
| 40 | `COD_LUMP_LEAFSURFACES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_LEAFSURFACES,` |
| 41 | `COD_LUMP_COLLISION_SURFACES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_COLLISION_SURFACES,` |
| 42 | `COD_LUMP_COLLISION_VERTICES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_COLLISION_VERTICES,` |
| 43 | `COD_LUMP_COLLISION_INDICES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_COLLISION_INDICES,` |
| 44 | `COD_LUMP_MODELS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_MODELS,` |
| 45 | `COD_LUMP_VISIBILITY` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_VISIBILITY,` |
| 46 | `COD_LUMP_ENTITIES` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_ENTITIES,` |
| 47 | `COD_LUMP_LIGHTS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `COD_LUMP_LIGHTS` |

## common/imagelib.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 36 | `UBYTE` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef unsigned char	UBYTE;` |
| 38 | `UWORD` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef unsigned short	UWORD;` |
| 39 | `LONG` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef long			LONG;` |
| 47 | `mask_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} mask_t;` |
| 43 | `ms_none` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `ms_none,` |
| 44 | `ms_mask` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `ms_mask,` |
| 45 | `ms_transcolor` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `ms_transcolor,` |
| 46 | `ms_lasso` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `ms_lasso` |
| 53 | `compress_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} compress_t;` |
| 51 | `cm_none` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `cm_none,` |
| 52 | `cm_rle1` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `cm_rle1` |
| 66 | `bmhd_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} bmhd_t;` |
| 57 | `w` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UWORD		w,h;` |
| 57 | `h` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UWORD		w,h;` |
| 58 | `x` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		x,y;` |
| 58 | `y` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		x,y;` |
| 59 | `nPlanes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UBYTE		nPlanes;` |
| 60 | `masking` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UBYTE		masking;` |
| 61 | `compression` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UBYTE		compression;` |
| 62 | `pad1` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UBYTE		pad1;` |
| 63 | `transparentColor` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UWORD		transparentColor;` |
| 64 | `xAspect` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UBYTE		xAspect,yAspect;` |
| 64 | `yAspect` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `UBYTE		xAspect,yAspect;` |
| 65 | `pageWidth` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		pageWidth,pageHeight;` |
| 65 | `pageHeight` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `short		pageWidth,pageHeight;` |
| 68 | `bmhd` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	bmhd_t	bmhd;						// will be in native byte order` |
| 70 | `FORMID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define FORMID ('F'+('O'<<8)+((int)'R'<<16)+((int)'M'<<24))` |
| 71 | `ILBMID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ILBMID ('I'+('L'<<8)+((int)'B'<<16)+((int)'M'<<24))` |
| 72 | `PBMID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define PBMID  ('P'+('B'<<8)+((int)'M'<<16)+((int)' '<<24))` |
| 73 | `BMHDID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define BMHDID ('B'+('M'<<8)+((int)'H'<<16)+((int)'D'<<24))` |
| 74 | `BODYID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define BODYID ('B'+('O'<<8)+((int)'D'<<16)+((int)'Y'<<24))` |
| 75 | `CMAPID` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CMAPID ('C'+('M'<<8)+((int)'A'<<16)+((int)'P'<<24))` |
| 77 | `bmhd` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `bmhd_t  bmhd;` |
| 110 | `pcx_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} pcx_t;` |
| 97 | `manufacturer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	manufacturer;` |
| 98 | `version` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	version;` |
| 99 | `encoding` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	encoding;` |
| 100 | `bits_per_pixel` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	bits_per_pixel;` |
| 101 | `xmin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 101 | `ymin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 101 | `xmax` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 101 | `ymax` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	xmin,ymin,xmax,ymax;` |
| 102 | `hres` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	hres,vres;` |
| 102 | `vres` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	hres,vres;` |
| 103 | `palette` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	palette[48];` |
| 104 | `reserved` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	reserved;` |
| 105 | `color_planes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	color_planes;` |
| 106 | `bytes_per_line` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	bytes_per_line;` |
| 107 | `palette_type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short	palette_type;` |
| 108 | `filler` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char	filler[58];` |
| 109 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char	data;			// unbounded` |
| 123 | `TargaHeader` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} TargaHeader;` |
| 117 | `_TargaHeader` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct _TargaHeader {` |
| 118 | `id_length` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char id_length, colormap_type, image_type;` |
| 118 | `colormap_type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char id_length, colormap_type, image_type;` |
| 118 | `image_type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char id_length, colormap_type, image_type;` |
| 119 | `colormap_index` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short colormap_index, colormap_length;` |
| 119 | `colormap_length` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short colormap_index, colormap_length;` |
| 120 | `colormap_size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char colormap_size;` |
| 121 | `x_origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short x_origin, y_origin, width, height;` |
| 121 | `y_origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short x_origin, y_origin, width, height;` |
| 121 | `width` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short x_origin, y_origin, width, height;` |
| 121 | `height` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned short x_origin, y_origin, width, height;` |
| 122 | `pixel_size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char pixel_size, attributes;` |
| 122 | `attributes` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned char pixel_size, attributes;` |
| 127 | `ddsColorKey_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} ddsColorKey_t;` |
| 126 | `colorSpaceLowValue` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int colorSpaceLowValue, colorSpaceHighValue;` |
| 126 | `colorSpaceHighValue` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int colorSpaceLowValue, colorSpaceHighValue;` |
| 132 | `ddsPixelFormat_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} ddsPixelFormat_t;` |
| 130 | `size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, fourCC, rgbBitCount;` |
| 130 | `flags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, fourCC, rgbBitCount;` |
| 130 | `fourCC` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, fourCC, rgbBitCount;` |
| 130 | `rgbBitCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, fourCC, rgbBitCount;` |
| 131 | `rBitMask` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int rBitMask, gBitMask, bBitMask, rgbAlphaBitMask;` |
| 131 | `gBitMask` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int rBitMask, gBitMask, bBitMask, rgbAlphaBitMask;` |
| 131 | `bBitMask` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int rBitMask, gBitMask, bBitMask, rgbAlphaBitMask;` |
| 131 | `rgbAlphaBitMask` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int rBitMask, gBitMask, bBitMask, rgbAlphaBitMask;` |
| 136 | `ddsCaps_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} ddsCaps_t;` |
| 135 | `caps1` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int caps1, caps2, caps3, caps4;` |
| 135 | `caps2` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int caps1, caps2, caps3, caps4;` |
| 135 | `caps3` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int caps1, caps2, caps3, caps4;` |
| 135 | `caps4` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int caps1, caps2, caps3, caps4;` |
| 149 | `ddsBuffer_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} ddsBuffer_t;` |
| 139 | `magic` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int magic;` |
| 140 | `size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, height, width;` |
| 140 | `flags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, height, width;` |
| 140 | `height` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, height, width;` |
| 140 | `width` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int size, flags, height, width;` |
| 141 | `pitch` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int pitch;` |
| 142 | `backBufferCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int backBufferCount, mipMapCount, alphaBitDepth, reserved;` |
| 142 | `mipMapCount` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int backBufferCount, mipMapCount, alphaBitDepth, reserved;` |
| 142 | `alphaBitDepth` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int backBufferCount, mipMapCount, alphaBitDepth, reserved;` |
| 142 | `reserved` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int backBufferCount, mipMapCount, alphaBitDepth, reserved;` |
| 143 | `surface` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `void *surface;` |
| 144 | `ckDestOverlay` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `ddsColorKey_t ckDestOverlay, ckDestBlt, ckSrcOverlay, ckSrcBlt;` |
| 144 | `ckDestBlt` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `ddsColorKey_t ckDestOverlay, ckDestBlt, ckSrcOverlay, ckSrcBlt;` |
| 144 | `ckSrcOverlay` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `ddsColorKey_t ckDestOverlay, ckDestBlt, ckSrcOverlay, ckSrcBlt;` |
| 144 | `ckSrcBlt` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `ddsColorKey_t ckDestOverlay, ckDestBlt, ckSrcOverlay, ckSrcBlt;` |
| 145 | `pixelFormat` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `ddsPixelFormat_t pixelFormat;` |
| 146 | `ddsCaps` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `ddsCaps_t ddsCaps;` |
| 147 | `textureStage` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int textureStage;` |
| 148 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte data[4];` |
| 151 | `DDS_FOURCC` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define DDS_FOURCC(a,b,c,d) ((unsigned int)(a) &#124; ((unsigned int)(b) << 8) &#124; ((unsigned int)(c) << 16) &#124; ((unsigned int)(d) << 24))` |
| 152 | `GL_COMPRESSED_RGBA_S3TC_DXT1_EXT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define GL_COMPRESSED_RGBA_S3TC_DXT1_EXT 0x83F1` |
| 153 | `GL_COMPRESSED_RGBA_S3TC_DXT3_EXT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define GL_COMPRESSED_RGBA_S3TC_DXT3_EXT 0x83F2` |
| 154 | `GL_COMPRESSED_RGBA_S3TC_DXT5_EXT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define GL_COMPRESSED_RGBA_S3TC_DXT5_EXT 0x83F3` |
| 161 | `fgetLittleShort` | function / fgetLittleShort | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int fgetLittleShort (FILE *f)` |
| 161 | `f` | parameter / fgetLittleShort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int fgetLittleShort (FILE *f)` |
| 163 | `b1` | local / fgetLittleShort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	b1, b2;` |
| 163 | `b2` | local / fgetLittleShort | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	b1, b2;` |
| 176 | `fgetLittleLong` | function / fgetLittleLong | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int fgetLittleLong (FILE *f)` |
| 176 | `f` | parameter / fgetLittleLong | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int fgetLittleLong (FILE *f)` |
| 178 | `b1` | local / fgetLittleLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	b1, b2, b3, b4;` |
| 178 | `b2` | local / fgetLittleLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	b1, b2, b3, b4;` |
| 178 | `b3` | local / fgetLittleLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	b1, b2, b3, b4;` |
| 178 | `b4` | local / fgetLittleLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	b1, b2, b3, b4;` |
| 193 | `Align` | function / Align | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int    Align (int l)` |
| 193 | `l` | parameter / Align | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int    Align (int l)` |
| 205 | `LBMRLEDecompress` | function / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `byte  *LBMRLEDecompress (byte *source,byte *unpacked, int bpwidth)` |
| 205 | `source` | parameter / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `byte  *LBMRLEDecompress (byte *source,byte *unpacked, int bpwidth)` |
| 205 | `unpacked` | parameter / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `byte  *LBMRLEDecompress (byte *source,byte *unpacked, int bpwidth)` |
| 205 | `bpwidth` | parameter / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `byte  *LBMRLEDecompress (byte *source,byte *unpacked, int bpwidth)` |
| 207 | `count` | local / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int     count;` |
| 208 | `b` | local / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    b,rept;` |
| 208 | `rept` | local / LBMRLEDecompress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    b,rept;` |
| 249 | `WriteLBMfile` | function / WriteLBMfile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void WriteLBMfile (const char *filename, byte *data,` |
| 249 | `filename` | parameter / WriteLBMfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteLBMfile (const char *filename, byte *data,` |
| 249 | `data` | parameter / WriteLBMfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteLBMfile (const char *filename, byte *data,` |
| 250 | `width` | parameter / WriteLBMfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height, byte *palette)` |
| 250 | `height` | parameter / WriteLBMfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height, byte *palette)` |
| 250 | `palette` | parameter / WriteLBMfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height, byte *palette)` |
| 252 | `lbm` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *lbm, *lbmptr;` |
| 252 | `lbmptr` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *lbm, *lbmptr;` |
| 253 | `formlength` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    *formlength, *bmhdlength, *cmaplength, *bodylength;` |
| 253 | `bmhdlength` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    *formlength, *bmhdlength, *cmaplength, *bodylength;` |
| 253 | `cmaplength` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    *formlength, *bmhdlength, *cmaplength, *bodylength;` |
| 253 | `bodylength` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    *formlength, *bmhdlength, *cmaplength, *bodylength;` |
| 254 | `length` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    length;` |
| 255 | `basebmhd` | local / WriteLBMfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `bmhd_t  basebmhd;` |
| 361 | `ImageLib_NoOp` | function / ImageLib_NoOp | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ImageLib_NoOp( void )` |
| 365 | `ImageLib_NoOpAlternate` | function / ImageLib_NoOpAlternate | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ImageLib_NoOpAlternate( void )` |
| 374 | `LoadPCX` | function / LoadPCX | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadPCX (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 374 | `filename` | parameter / LoadPCX | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 374 | `pic` | parameter / LoadPCX | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 374 | `palette` | parameter / LoadPCX | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 374 | `width` | parameter / LoadPCX | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 374 | `height` | parameter / LoadPCX | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 376 | `raw` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	*raw;` |
| 377 | `pcx` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `pcx_t	*pcx;` |
| 378 | `x` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		x, y;` |
| 378 | `y` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		x, y;` |
| 379 | `len` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		len;` |
| 380 | `dataByte` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		dataByte, runLength;` |
| 380 | `runLength` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		dataByte, runLength;` |
| 381 | `out` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	*out, *pix;` |
| 381 | `pix` | local / LoadPCX | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	*out, *pix;` |
| 470 | `WritePCXfile` | function / WritePCXfile | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void WritePCXfile (const char *filename, byte *data,` |
| 470 | `filename` | parameter / WritePCXfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WritePCXfile (const char *filename, byte *data,` |
| 470 | `data` | parameter / WritePCXfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WritePCXfile (const char *filename, byte *data,` |
| 471 | `width` | parameter / WritePCXfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height, byte *palette)` |
| 471 | `height` | parameter / WritePCXfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height, byte *palette)` |
| 471 | `palette` | parameter / WritePCXfile | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height, byte *palette)` |
| 473 | `i` | local / WritePCXfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j, length;` |
| 473 | `j` | local / WritePCXfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j, length;` |
| 473 | `length` | local / WritePCXfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j, length;` |
| 474 | `pcx` | local / WritePCXfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `pcx_t	*pcx;` |
| 475 | `pack` | local / WritePCXfile | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte		*pack;` |
| 528 | `LoadDDSBuffer` | function / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `buffer` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `length` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `pic` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `width` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `height` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `format` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 528 | `name` | parameter / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadDDSBuffer(byte *buffer, unsigned int length, byte **pic, int *width, int *height, int *format, const char *name)` |
| 530 | `dds` | local / LoadDDSBuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `ddsBuffer_t *dds;` |
| 565 | `LoadBMP` | function / LoadBMP | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadBMP (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 565 | `filename` | parameter / LoadBMP | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadBMP (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 565 | `pic` | parameter / LoadBMP | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadBMP (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 565 | `palette` | parameter / LoadBMP | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadBMP (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 565 | `width` | parameter / LoadBMP | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadBMP (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 565 | `height` | parameter / LoadBMP | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadBMP (const char *filename, byte **pic, byte **palette, int *width, int *height)` |
| 567 | `out` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *out;` |
| 568 | `fin` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE *fin;` |
| 569 | `i` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, bfSize, bfOffBits, structSize;` |
| 569 | `bfSize` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, bfSize, bfOffBits, structSize;` |
| 569 | `bfOffBits` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, bfSize, bfOffBits, structSize;` |
| 569 | `structSize` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, bfSize, bfOffBits, structSize;` |
| 570 | `bcWidth` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int bcWidth, bcHeight, bcPlanes, bcBitCount;` |
| 570 | `bcHeight` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int bcWidth, bcHeight, bcPlanes, bcBitCount;` |
| 570 | `bcPlanes` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int bcWidth, bcHeight, bcPlanes, bcBitCount;` |
| 570 | `bcBitCount` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int bcWidth, bcHeight, bcPlanes, bcBitCount;` |
| 571 | `bcPalette` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte bcPalette[1024];` |
| 572 | `flipped` | local / LoadBMP | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean flipped;` |
| 657 | `Save256Image` | function / Save256Image | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Save256Image (const char *name, byte *pixels, byte *palette, int width, int height)` |
| 657 | `name` | parameter / Save256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette, int width, int height)` |
| 657 | `pixels` | parameter / Save256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette, int width, int height)` |
| 657 | `palette` | parameter / Save256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette, int width, int height)` |
| 657 | `width` | parameter / Save256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette, int width, int height)` |
| 657 | `height` | parameter / Save256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette, int width, int height)` |
| 659 | `ext` | local / Save256Image | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char ext[128];` |
| 683 | `LoadTGABuffer` | function / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadTGABuffer(byte *buffer, byte **pic, int *width, int *height, const char *name)` |
| 683 | `buffer` | parameter / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer(byte *buffer, byte **pic, int *width, int *height, const char *name)` |
| 683 | `pic` | parameter / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer(byte *buffer, byte **pic, int *width, int *height, const char *name)` |
| 683 | `width` | parameter / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer(byte *buffer, byte **pic, int *width, int *height, const char *name)` |
| 683 | `height` | parameter / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer(byte *buffer, byte **pic, int *width, int *height, const char *name)` |
| 683 | `name` | parameter / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer(byte *buffer, byte **pic, int *width, int *height, const char *name)` |
| 685 | `columns` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int columns, rows, numPixels;` |
| 685 | `rows` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int columns, rows, numPixels;` |
| 685 | `numPixels` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int columns, rows, numPixels;` |
| 686 | `pixbuf` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *pixbuf;` |
| 687 | `row` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int row, column;` |
| 687 | `column` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int row, column;` |
| 688 | `buf_p` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buf_p;` |
| 689 | `targa_header` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `TargaHeader targa_header;` |
| 690 | `targa_rgba` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *targa_rgba;` |
| 745 | `red` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte;` |
| 745 | `green` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte;` |
| 745 | `blue` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte;` |
| 745 | `alphabyte` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte;` |
| 784 | `red` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 784 | `green` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 784 | `blue` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 784 | `alphabyte` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 784 | `packetHeader` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 784 | `packetSize` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 784 | `j` | local / LoadTGABuffer | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char red, green, blue, alphabyte, packetHeader, packetSize, j;` |
| 891 | `LoadTGA` | function / LoadTGA | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadTGA (const char *name, byte **pixels, int *width, int *height)` |
| 891 | `name` | parameter / LoadTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *name, byte **pixels, int *width, int *height)` |
| 891 | `pixels` | parameter / LoadTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *name, byte **pixels, int *width, int *height)` |
| 891 | `width` | parameter / LoadTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *name, byte **pixels, int *width, int *height)` |
| 891 | `height` | parameter / LoadTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *name, byte **pixels, int *width, int *height)` |
| 893 | `buffer` | local / LoadTGA | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *buffer;` |
| 894 | `nLen` | local / LoadTGA | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int nLen;` |
| 908 | `WriteTGA` | function / WriteTGA | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void WriteTGA (const char *filename, byte *data, int width, int height) {` |
| 908 | `filename` | parameter / WriteTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height) {` |
| 908 | `data` | parameter / WriteTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height) {` |
| 908 | `width` | parameter / WriteTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height) {` |
| 908 | `height` | parameter / WriteTGA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height) {` |
| 909 | `buffer` | local / WriteTGA | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte	*buffer;` |
| 910 | `i` | local / WriteTGA | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i;` |
| 911 | `c` | local / WriteTGA | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		c;` |
| 912 | `f` | local / WriteTGA | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `FILE	*f;` |
| 945 | `LoadLBM` | function / LoadLBM | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void LoadLBM (const char *filename, byte **picture, byte **palette)` |
| 945 | `filename` | parameter / LoadLBM | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadLBM (const char *filename, byte **picture, byte **palette)` |
| 945 | `picture` | parameter / LoadLBM | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadLBM (const char *filename, byte **picture, byte **palette)` |
| 945 | `palette` | parameter / LoadLBM | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadLBM (const char *filename, byte **picture, byte **palette)` |
| 947 | `LBMbuffer` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *LBMbuffer, *picbuffer, *cmapbuffer;` |
| 947 | `picbuffer` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *LBMbuffer, *picbuffer, *cmapbuffer;` |
| 947 | `cmapbuffer` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *LBMbuffer, *picbuffer, *cmapbuffer;` |
| 948 | `y` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int             y;` |
| 949 | `LBM_P` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *LBM_P, *LBMEND_P;` |
| 949 | `LBMEND_P` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *LBM_P, *LBMEND_P;` |
| 950 | `pic_p` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *pic_p;` |
| 951 | `body_p` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte    *body_p;` |
| 953 | `formtype` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    formtype,formlength;` |
| 953 | `formlength` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    formtype,formlength;` |
| 954 | `chunktype` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    chunktype,chunklength;` |
| 954 | `chunklength` | local / LoadLBM | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int    chunktype,chunklength;` |
| 1056 | `Load256Image` | function / Load256Image | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Load256Image (const char *name, byte **pixels, byte **palette, int *width, int *height)` |
| 1056 | `name` | parameter / Load256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette, int *width, int *height)` |
| 1056 | `pixels` | parameter / Load256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette, int *width, int *height)` |
| 1056 | `palette` | parameter / Load256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette, int *width, int *height)` |
| 1056 | `width` | parameter / Load256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette, int *width, int *height)` |
| 1056 | `height` | parameter / Load256Image | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette, int *width, int *height)` |
| 1058 | `ext` | local / Load256Image | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char ext[128];` |
| 1084 | `Load32BitImage` | function / Load32BitImage | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height)` |
| 1084 | `name` | parameter / Load32BitImage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height)` |
| 1084 | `pixels` | parameter / Load32BitImage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height)` |
| 1084 | `width` | parameter / Load32BitImage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height)` |
| 1084 | `height` | parameter / Load32BitImage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height)` |
| 1086 | `ext` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char ext[128];` |
| 1087 | `palette` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *palette, *pixels8, *pixels32;` |
| 1087 | `pixels8` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *palette, *pixels8, *pixels32;` |
| 1087 | `pixels32` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *palette, *pixels8, *pixels32;` |
| 1088 | `size` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, i, v;` |
| 1088 | `i` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, i, v;` |
| 1088 | `v` | local / Load32BitImage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, i, v;` |

## common/imagelib.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 26 | `LoadLBM` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void LoadLBM (const char *filename, byte **picture, byte **palette);` |
| 26 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadLBM (const char *filename, byte **picture, byte **palette);` |
| 26 | `picture` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadLBM (const char *filename, byte **picture, byte **palette);` |
| 26 | `palette` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadLBM (const char *filename, byte **picture, byte **palette);` |
| 27 | `WriteLBMfile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void WriteLBMfile (const char *filename, byte *data, int width, int height` |
| 27 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteLBMfile (const char *filename, byte *data, int width, int height` |
| 27 | `data` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteLBMfile (const char *filename, byte *data, int width, int height` |
| 27 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteLBMfile (const char *filename, byte *data, int width, int height` |
| 27 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteLBMfile (const char *filename, byte *data, int width, int height` |
| 28 | `palette` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `, byte *palette);` |
| 29 | `LoadPCX` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void LoadPCX (const char *filename, byte **picture, byte **palette, int *width, int *height);` |
| 29 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **picture, byte **palette, int *width, int *height);` |
| 29 | `picture` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **picture, byte **palette, int *width, int *height);` |
| 29 | `palette` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **picture, byte **palette, int *width, int *height);` |
| 29 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **picture, byte **palette, int *width, int *height);` |
| 29 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadPCX (const char *filename, byte **picture, byte **palette, int *width, int *height);` |
| 30 | `WritePCXfile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void WritePCXfile (const char *filename, byte *data, int width, int height` |
| 30 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WritePCXfile (const char *filename, byte *data, int width, int height` |
| 30 | `data` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WritePCXfile (const char *filename, byte *data, int width, int height` |
| 30 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WritePCXfile (const char *filename, byte *data, int width, int height` |
| 30 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WritePCXfile (const char *filename, byte *data, int width, int height` |
| 31 | `palette` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `, byte *palette);` |
| 34 | `Load256Image` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Load256Image (const char *name, byte **pixels, byte **palette,` |
| 34 | `name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette,` |
| 34 | `pixels` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette,` |
| 34 | `palette` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load256Image (const char *name, byte **pixels, byte **palette,` |
| 35 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int *width, int *height);` |
| 35 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int *width, int *height);` |
| 36 | `Save256Image` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Save256Image (const char *name, byte *pixels, byte *palette,` |
| 36 | `name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette,` |
| 36 | `pixels` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette,` |
| 36 | `palette` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Save256Image (const char *name, byte *pixels, byte *palette,` |
| 37 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height);` |
| 37 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int width, int height);` |
| 40 | `LoadTGA` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void LoadTGA (const char *filename, byte **pixels, int *width, int *height);` |
| 40 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *filename, byte **pixels, int *width, int *height);` |
| 40 | `pixels` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *filename, byte **pixels, int *width, int *height);` |
| 40 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *filename, byte **pixels, int *width, int *height);` |
| 40 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGA (const char *filename, byte **pixels, int *width, int *height);` |
| 41 | `LoadTGABuffer` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void LoadTGABuffer ( byte *buffer, byte **pic, int *width, int *height, const char *name);` |
| 41 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer ( byte *buffer, byte **pic, int *width, int *height, const char *name);` |
| 41 | `pic` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer ( byte *buffer, byte **pic, int *width, int *height, const char *name);` |
| 41 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer ( byte *buffer, byte **pic, int *width, int *height, const char *name);` |
| 41 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer ( byte *buffer, byte **pic, int *width, int *height, const char *name);` |
| 41 | `name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadTGABuffer ( byte *buffer, byte **pic, int *width, int *height, const char *name);` |
| 42 | `WriteTGA` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void WriteTGA (const char *filename, byte *data, int width, int height);` |
| 42 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height);` |
| 42 | `data` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height);` |
| 42 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height);` |
| 42 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WriteTGA (const char *filename, byte *data, int width, int height);` |
| 44 | `Load32BitImage` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height);` |
| 44 | `name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height);` |
| 44 | `pixels` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height);` |
| 44 | `width` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height);` |
| 44 | `height` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Load32BitImage (const char *name, unsigned **pixels, int *width, int *height);` |

## common/mathlib.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 24 | `__MATHLIB__` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define __MATHLIB__` |
| 31 | `vec_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef double vec_t;` |
| 33 | `vec_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef float vec_t;` |
| 35 | `vec2_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef vec_t vec2_t[2];` |
| 36 | `vec3_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef vec_t vec3_t[3];` |
| 37 | `vec4_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef vec_t vec4_t[4];` |
| 39 | `SIDE_FRONT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SIDE_FRONT		0` |
| 40 | `SIDE_ON` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SIDE_ON			2` |
| 41 | `SIDE_BACK` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SIDE_BACK		1` |
| 42 | `SIDE_CROSS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	SIDE_CROSS		-2` |
| 44 | `Q_PI` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	Q_PI	3.14159265358979323846` |
| 45 | `DEG2RAD` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define DEG2RAD( a ) ( ( (a) * Q_PI ) / 180.0F )` |
| 46 | `RAD2DEG` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define RAD2DEG( a ) ( ( (a) * 180.0f ) / Q_PI )` |
| 48 | `vec3_origin` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern const vec3_t vec3_origin;` |
| 50 | `EQUAL_EPSILON` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	EQUAL_EPSILON	0.001` |
| 54 | `PLANE_X` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	PLANE_X			0` |
| 55 | `PLANE_Y` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	PLANE_Y			1` |
| 56 | `PLANE_Z` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	PLANE_Z			2` |
| 57 | `PLANE_NON_AXIAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	PLANE_NON_AXIAL	3` |
| 59 | `VectorCompare` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean VectorCompare( const vec3_t v1, const vec3_t v2 );` |
| 59 | `v1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompare( const vec3_t v1, const vec3_t v2 );` |
| 59 | `v2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompare( const vec3_t v1, const vec3_t v2 );` |
| 61 | `DotProduct` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define DotProduct(x,y) (x[0]*y[0]+x[1]*y[1]+x[2]*y[2])` |
| 62 | `VectorSubtract` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorSubtract(a,b,c) {c[0]=a[0]-b[0];c[1]=a[1]-b[1];c[2]=a[2]-b[2];}` |
| 63 | `VectorAdd` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorAdd(a,b,c) {c[0]=a[0]+b[0];c[1]=a[1]+b[1];c[2]=a[2]+b[2];}` |
| 64 | `VectorCopy` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorCopy(a,b) {b[0]=a[0];b[1]=a[1];b[2]=a[2];}` |
| 65 | `VectorScale` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorScale(a,b,c) {c[0]=b*a[0];c[1]=b*a[1];c[2]=b*a[2];}` |
| 66 | `VectorClear` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorClear(x) {x[0] = x[1] = x[2] = 0;}` |
| 67 | `VectorNegate` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	VectorNegate(x) {x[0]=-x[0];x[1]=-x[1];x[2]=-x[2];}` |
| 68 | `Vec10Copy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Vec10Copy( vec_t *in, vec_t *out );` |
| 68 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vec10Copy( vec_t *in, vec_t *out );` |
| 68 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vec10Copy( vec_t *in, vec_t *out );` |
| 70 | `Q_rint` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t Q_rint (vec_t in);` |
| 70 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t Q_rint (vec_t in);` |
| 71 | `_DotProduct` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t _DotProduct (vec3_t v1, vec3_t v2);` |
| 71 | `v1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t _DotProduct (vec3_t v1, vec3_t v2);` |
| 71 | `v2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t _DotProduct (vec3_t v1, vec3_t v2);` |
| 72 | `_VectorSubtract` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 72 | `va` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 72 | `vb` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 72 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 73 | `_VectorAdd` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 73 | `va` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 73 | `vb` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 73 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 74 | `_VectorCopy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorCopy (vec3_t in, vec3_t out);` |
| 74 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorCopy (vec3_t in, vec3_t out);` |
| 74 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorCopy (vec3_t in, vec3_t out);` |
| 75 | `_VectorScale` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 75 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 75 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 75 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 77 | `_VectorLength` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float _VectorLength( const vec3_t v );` |
| 77 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float _VectorLength( const vec3_t v );` |
| 79 | `VectorMA` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorMA( const vec3_t va, double scale, const vec3_t vb, vec3_t vc );` |
| 79 | `va` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorMA( const vec3_t va, double scale, const vec3_t vb, vec3_t vc );` |
| 79 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorMA( const vec3_t va, double scale, const vec3_t vb, vec3_t vc );` |
| 79 | `vb` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorMA( const vec3_t va, double scale, const vec3_t vb, vec3_t vc );` |
| 79 | `vc` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorMA( const vec3_t va, double scale, const vec3_t vb, vec3_t vc );` |
| 81 | `CrossProduct` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 81 | `v1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 81 | `v2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 81 | `cross` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 82 | `VectorNormalize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t VectorNormalize( vec3_t v );` |
| 82 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t VectorNormalize( vec3_t v );` |
| 83 | `ColorNormalize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t ColorNormalize( const vec3_t in, vec3_t out );` |
| 83 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t ColorNormalize( const vec3_t in, vec3_t out );` |
| 83 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t ColorNormalize( const vec3_t in, vec3_t out );` |
| 84 | `VectorInverse` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorInverse (vec3_t v);` |
| 84 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorInverse (vec3_t v);` |
| 86 | `ClearBounds` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ClearBounds (vec3_t mins, vec3_t maxs);` |
| 86 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ClearBounds (vec3_t mins, vec3_t maxs);` |
| 86 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ClearBounds (vec3_t mins, vec3_t maxs);` |
| 87 | `AddPointToBounds` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 87 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 87 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 87 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 89 | `PlaneFromPoints` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 89 | `plane` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 89 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 89 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 89 | `c` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 91 | `NormalToLatLong` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] );` |
| 91 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] );` |
| 91 | `bytes` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] );` |
| 93 | `PlaneTypeForNormal` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	PlaneTypeForNormal (vec3_t normal);` |
| 93 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int	PlaneTypeForNormal (vec3_t normal);` |
| 95 | `RotatePointAroundVector` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 95 | `dst` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 95 | `dir` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 95 | `point` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 96 | `degrees` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float degrees );` |

## common/mutex.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 32 | `MutexLock` | function / MutexLock | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MutexLock(void *m)` |
| 32 | `m` | parameter / MutexLock | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MutexLock(void *m)` |
| 34 | `crit` | local / MutexLock | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `CRITICAL_SECTION *crit;` |
| 47 | `MutexUnlock` | function / MutexUnlock | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MutexUnlock(void *m)` |
| 47 | `m` | parameter / MutexUnlock | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MutexUnlock(void *m)` |
| 49 | `crit` | local / MutexUnlock | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `CRITICAL_SECTION *crit;` |
| 62 | `MutexAlloc` | function / MutexAlloc | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *MutexAlloc(void)` |
| 64 | `crit` | local / MutexAlloc | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `CRITICAL_SECTION *crit;` |

## common/polylib.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 25 | `ON_EPSILON` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ON_EPSILON 0.1f` |
| 30 | `numthreads` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int numthreads;` |
| 34 | `c_active_windings` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	c_active_windings;` |
| 35 | `c_peak_windings` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	c_peak_windings;` |
| 36 | `c_winding_allocs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	c_winding_allocs;` |
| 37 | `c_winding_points` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	c_winding_points;` |
| 39 | `BOGUS_RANGE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	BOGUS_RANGE	WORLD_SIZE` |
| 41 | `c_removed` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	c_removed;` |
| 43 | `MAX_HULL_POINTS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_HULL_POINTS		128` |
| 48 | `double_winding_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} double_winding_t;` |
| 46 | `numpoints` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int numpoints;` |
| 47 | `p` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `double p[4][3];` |
| 52 | `VectorCompareEpsilon` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern qboolean VectorCompareEpsilon(const vec3_t a, const vec3_t b);` |
| 52 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern qboolean VectorCompareEpsilon(const vec3_t a, const vec3_t b);` |
| 52 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern qboolean VectorCompareEpsilon(const vec3_t a, const vec3_t b);` |
| 60 | `pw` | function / pw | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void pw(winding_t *w)` |
| 60 | `w` | parameter / pw | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void pw(winding_t *w)` |
| 62 | `i` | local / pw | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i;` |
| 72 | `AllocWinding` | function / AllocWinding | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `winding_t	*AllocWinding (int points)` |
| 72 | `points` | parameter / AllocWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*AllocWinding (int points)` |
| 74 | `w` | local / AllocWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*w;` |
| 75 | `s` | local / AllocWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			s;` |
| 96 | `AllocDoubleWinding` | function / AllocDoubleWinding | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *AllocDoubleWinding (int points)` |
| 96 | `points` | parameter / AllocDoubleWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *AllocDoubleWinding (int points)` |
| 98 | `w` | local / AllocDoubleWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `void	*w;` |
| 99 | `s` | local / AllocDoubleWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		s;` |
| 120 | `FreeWinding` | function / FreeWinding | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FreeWinding (winding_t *w)` |
| 120 | `w` | parameter / FreeWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FreeWinding (winding_t *w)` |
| 136 | `FreeDoubleWinding` | function / FreeDoubleWinding | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void FreeDoubleWinding(double_winding_t *w)` |
| 136 | `w` | parameter / FreeDoubleWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void FreeDoubleWinding(double_winding_t *w)` |
| 151 | `RemoveColinearPoints` | function / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void	RemoveColinearPoints (winding_t *w)` |
| 151 | `w` | parameter / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	RemoveColinearPoints (winding_t *w)` |
| 153 | `i` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j, k;` |
| 153 | `j` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j, k;` |
| 153 | `k` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j, k;` |
| 154 | `v1` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	v1, v2;` |
| 154 | `v2` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	v1, v2;` |
| 155 | `nump` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		nump;` |
| 156 | `p` | local / RemoveColinearPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	p[MAX_POINTS_ON_WINDING];` |
| 190 | `WindingPlane` | function / WindingPlane | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void WindingPlane (winding_t *w, vec3_t normal, vec_t *dist)` |
| 190 | `w` | parameter / WindingPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WindingPlane (winding_t *w, vec3_t normal, vec_t *dist)` |
| 190 | `normal` | parameter / WindingPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WindingPlane (winding_t *w, vec3_t normal, vec_t *dist)` |
| 190 | `dist` | parameter / WindingPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WindingPlane (winding_t *w, vec3_t normal, vec_t *dist)` |
| 192 | `v1` | local / WindingPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	v1, v2;` |
| 192 | `v2` | local / WindingPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	v1, v2;` |
| 207 | `WindingPlaneAverage` | function / WindingPlaneAverage | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void WindingPlaneAverage(winding_t *w, vec3_t normal, vec_t *dist)` |
| 207 | `w` | parameter / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WindingPlaneAverage(winding_t *w, vec3_t normal, vec_t *dist)` |
| 207 | `normal` | parameter / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WindingPlaneAverage(winding_t *w, vec3_t normal, vec_t *dist)` |
| 207 | `dist` | parameter / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void WindingPlaneAverage(winding_t *w, vec3_t normal, vec_t *dist)` |
| 209 | `i` | local / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 210 | `v1` | local / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v1, v2, cross;` |
| 210 | `v2` | local / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v1, v2, cross;` |
| 210 | `cross` | local / WindingPlaneAverage | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v1, v2, cross;` |
| 229 | `WindingArea` | function / WindingArea | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `vec_t	WindingArea (winding_t *w)` |
| 229 | `w` | parameter / WindingArea | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t	WindingArea (winding_t *w)` |
| 231 | `i` | local / WindingArea | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i;` |
| 232 | `d1` | local / WindingArea | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	d1, d2, cross;` |
| 232 | `d2` | local / WindingArea | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	d1, d2, cross;` |
| 232 | `cross` | local / WindingArea | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	d1, d2, cross;` |
| 233 | `total` | local / WindingArea | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	total;` |
| 251 | `WindingBounds` | function / WindingBounds | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs)` |
| 251 | `w` | parameter / WindingBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs)` |
| 251 | `mins` | parameter / WindingBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs)` |
| 251 | `maxs` | parameter / WindingBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs)` |
| 253 | `v` | local / WindingBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	v;` |
| 254 | `i` | local / WindingBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i,j;` |
| 254 | `j` | local / WindingBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i,j;` |
| 277 | `WindingCenter` | function / WindingCenter | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void	WindingCenter (winding_t *w, vec3_t center)` |
| 277 | `w` | parameter / WindingCenter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingCenter (winding_t *w, vec3_t center)` |
| 277 | `center` | parameter / WindingCenter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingCenter (winding_t *w, vec3_t center)` |
| 279 | `i` | local / WindingCenter | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i;` |
| 280 | `scale` | local / WindingCenter | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	scale;` |
| 295 | `BaseWindingForPlane` | function / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `winding_t *BaseWindingForPlane (vec3_t normal, vec_t dist)` |
| 295 | `normal` | parameter / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t *BaseWindingForPlane (vec3_t normal, vec_t dist)` |
| 295 | `dist` | parameter / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t *BaseWindingForPlane (vec3_t normal, vec_t dist)` |
| 297 | `i` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, x;` |
| 297 | `x` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, x;` |
| 298 | `max` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	max, v;` |
| 298 | `v` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	max, v;` |
| 299 | `org` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	org, vright, vup;` |
| 299 | `vright` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	org, vright, vup;` |
| 299 | `vup` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	org, vright, vup;` |
| 300 | `w` | local / BaseWindingForPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*w;` |
| 368 | `BaseWindingForPlaneDouble` | function / BaseWindingForPlaneDouble | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `double_winding_t *BaseWindingForPlaneDouble(vec3_t normal, vec_t dist)` |
| 368 | `normal` | parameter / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `double_winding_t *BaseWindingForPlaneDouble(vec3_t normal, vec_t dist)` |
| 368 | `dist` | parameter / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `double_winding_t *BaseWindingForPlaneDouble(vec3_t normal, vec_t dist)` |
| 370 | `i` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, x;` |
| 370 | `x` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, x;` |
| 371 | `max` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t max, v;` |
| 371 | `v` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t max, v;` |
| 372 | `org` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t org, vright, vup;` |
| 372 | `vright` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t org, vright, vup;` |
| 372 | `vup` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t org, vright, vup;` |
| 373 | `w` | local / BaseWindingForPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double_winding_t *w;` |
| 430 | `WindingFromDouble` | function / WindingFromDouble | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `winding_t *WindingFromDouble(const double_winding_t *in)` |
| 430 | `in` | parameter / WindingFromDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t *WindingFromDouble(const double_winding_t *in)` |
| 432 | `out` | local / WindingFromDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t *out;` |
| 433 | `i` | local / WindingFromDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, num;` |
| 433 | `num` | local / WindingFromDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, num;` |
| 460 | `CopyWinding` | function / CopyWinding | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `winding_t	*CopyWinding (winding_t *w)` |
| 460 | `w` | parameter / CopyWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*CopyWinding (winding_t *w)` |
| 462 | `size` | local / CopyWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			size;` |
| 463 | `c` | local / CopyWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*c;` |
| 476 | `ReverseWinding` | function / ReverseWinding | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `winding_t	*ReverseWinding (winding_t *w)` |
| 476 | `w` | parameter / ReverseWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ReverseWinding (winding_t *w)` |
| 478 | `i` | local / ReverseWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			i;` |
| 479 | `c` | local / ReverseWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*c;` |
| 495 | `ClipWindingEpsilon` | function / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 495 | `in` | parameter / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 495 | `normal` | parameter / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 495 | `dist` | parameter / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 496 | `epsilon` | parameter / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn)` |
| 496 | `front` | parameter / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn)` |
| 496 | `back` | parameter / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn)` |
| 496 | `keepOn` | parameter / ClipWindingEpsilon | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn)` |
| 498 | `dists` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	dists[MAX_POINTS_ON_WINDING+4];` |
| 499 | `sides` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		sides[MAX_POINTS_ON_WINDING+4];` |
| 500 | `counts` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		counts[3];` |
| 501 | `dot` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	dot;` |
| 502 | `i` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 502 | `j` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 503 | `p1` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	*p1, *p2;` |
| 503 | `p2` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	*p1, *p2;` |
| 504 | `mid` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	mid;` |
| 505 | `f` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*f, *b;` |
| 505 | `b` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*f, *b;` |
| 506 | `maxpts` | local / ClipWindingEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		maxpts;` |
| 607 | `ChopWindingInPlace` | function / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ChopWindingInPlace (winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 607 | `inout` | parameter / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlace (winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 607 | `normal` | parameter / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlace (winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 607 | `dist` | parameter / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlace (winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 607 | `epsilon` | parameter / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlace (winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 609 | `in` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*in;` |
| 610 | `dists` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	dists[MAX_POINTS_ON_WINDING+4];` |
| 611 | `sides` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		sides[MAX_POINTS_ON_WINDING+4];` |
| 612 | `counts` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		counts[3];` |
| 613 | `dot` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	dot;` |
| 614 | `i` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 614 | `j` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 615 | `p1` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	*p1, *p2;` |
| 615 | `p2` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	*p1, *p2;` |
| 616 | `mid` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	mid;` |
| 617 | `f` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*f;` |
| 618 | `maxpts` | local / ChopWindingInPlace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		maxpts;` |
| 707 | `ChopWindingInPlaceDouble` | function / ChopWindingInPlaceDouble | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ChopWindingInPlaceDouble(double_winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 707 | `inout` | parameter / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlaceDouble(double_winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 707 | `normal` | parameter / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlaceDouble(double_winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 707 | `dist` | parameter / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlaceDouble(double_winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 707 | `epsilon` | parameter / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ChopWindingInPlaceDouble(double_winding_t **inout, vec3_t normal, vec_t dist, vec_t epsilon)` |
| 709 | `in` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double_winding_t	*in;` |
| 710 | `dists` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double	dists[MAX_POINTS_ON_WINDING+4];` |
| 711 | `sides` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		sides[MAX_POINTS_ON_WINDING+4];` |
| 712 | `counts` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		counts[3];` |
| 713 | `dot` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double	dot;` |
| 714 | `i` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 714 | `j` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 715 | `p1` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double	*p1, *p2;` |
| 715 | `p2` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double	*p1, *p2;` |
| 716 | `mid` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double	mid[3];` |
| 717 | `f` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double_winding_t	*f;` |
| 718 | `maxpts` | local / ChopWindingInPlaceDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		maxpts;` |
| 810 | `ChopWinding` | function / ChopWinding | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist)` |
| 810 | `in` | parameter / ChopWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist)` |
| 810 | `normal` | parameter / ChopWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist)` |
| 810 | `dist` | parameter / ChopWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist)` |
| 812 | `f` | local / ChopWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*f, *b;` |
| 812 | `b` | local / ChopWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `winding_t	*f, *b;` |
| 827 | `CheckWinding` | function / CheckWinding | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void CheckWinding (winding_t *w)` |
| 827 | `w` | parameter / CheckWinding | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CheckWinding (winding_t *w)` |
| 829 | `i` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 829 | `j` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int		i, j;` |
| 830 | `p1` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	*p1, *p2;` |
| 830 | `p2` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	*p1, *p2;` |
| 831 | `d` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	d, edgedist;` |
| 831 | `edgedist` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	d, edgedist;` |
| 832 | `dir` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	dir, edgenormal, facenormal;` |
| 832 | `edgenormal` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	dir, edgenormal, facenormal;` |
| 832 | `facenormal` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t	dir, edgenormal, facenormal;` |
| 833 | `area` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	area;` |
| 834 | `facedist` | local / CheckWinding | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t	facedist;` |
| 889 | `WindingOnPlaneSide` | function / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist)` |
| 889 | `w` | parameter / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist)` |
| 889 | `normal` | parameter / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist)` |
| 889 | `dist` | parameter / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist)` |
| 891 | `front` | local / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean	front, back;` |
| 891 | `back` | local / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean	front, back;` |
| 892 | `i` | local / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			i;` |
| 893 | `d` | local / WindingOnPlaneSide | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t		d;` |
| 930 | `AddWindingToConvexHull` | function / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal ) {` |
| 930 | `w` | parameter / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal ) {` |
| 930 | `hull` | parameter / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal ) {` |
| 930 | `normal` | parameter / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal ) {` |
| 931 | `i` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			i, j, k;` |
| 931 | `j` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			i, j, k;` |
| 931 | `k` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			i, j, k;` |
| 932 | `p` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float		*p, *copy;` |
| 932 | `copy` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float		*p, *copy;` |
| 933 | `dir` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t		dir;` |
| 934 | `d` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float		d;` |
| 935 | `numHullPoints` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			numHullPoints, numNew;` |
| 935 | `numNew` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int			numHullPoints, numNew;` |
| 936 | `hullPoints` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t		hullPoints[MAX_HULL_POINTS];` |
| 937 | `newHullPoints` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t		newHullPoints[MAX_HULL_POINTS];` |
| 938 | `hullDirs` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t		hullDirs[MAX_HULL_POINTS];` |
| 939 | `hullSide` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean	hullSide[MAX_HULL_POINTS];` |
| 940 | `outside` | local / AddWindingToConvexHull | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean	outside;` |
| 1021 | `SnapWindingToPlaneDouble` | function / SnapWindingToPlaneDouble | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SnapWindingToPlaneDouble( double_winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1021 | `w` | parameter / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SnapWindingToPlaneDouble( double_winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1021 | `normal` | parameter / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SnapWindingToPlaneDouble( double_winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1021 | `dist` | parameter / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SnapWindingToPlaneDouble( double_winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1022 | `i` | local / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 1022 | `j` | local / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 1023 | `point` | local / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double point[3], rounded, oldDist, newDist, distance;` |
| 1023 | `rounded` | local / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double point[3], rounded, oldDist, newDist, distance;` |
| 1023 | `oldDist` | local / SnapWindingToPlaneDouble | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `double point[3], rounded, oldDist, newDist, distance;` |
| 1023 | `newDist` | local / SnapWindingToPlaneDouble | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `double point[3], rounded, oldDist, newDist, distance;` |
| 1023 | `distance` | local / SnapWindingToPlaneDouble | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double point[3], rounded, oldDist, newDist, distance;` |
| 1053 | `CheckWindingPlane` | function / CheckWindingPlane | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void CheckWindingPlane( winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1053 | `w` | parameter / CheckWindingPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CheckWindingPlane( winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1053 | `normal` | parameter / CheckWindingPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CheckWindingPlane( winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1053 | `dist` | parameter / CheckWindingPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CheckWindingPlane( winding_t *w, vec3_t normal, vec_t dist ) {` |
| 1061 | `ColinearEdge` | function / ColinearEdge | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int ColinearEdge( vec3_t pointA, vec3_t pointB, vec3_t lineEnd, vec_t tolerance ) {` |
| 1061 | `pointA` | parameter / ColinearEdge | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `int ColinearEdge( vec3_t pointA, vec3_t pointB, vec3_t lineEnd, vec_t tolerance ) {` |
| 1061 | `pointB` | parameter / ColinearEdge | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `int ColinearEdge( vec3_t pointA, vec3_t pointB, vec3_t lineEnd, vec_t tolerance ) {` |
| 1061 | `lineEnd` | parameter / ColinearEdge | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `int ColinearEdge( vec3_t pointA, vec3_t pointB, vec3_t lineEnd, vec_t tolerance ) {` |
| 1061 | `tolerance` | parameter / ColinearEdge | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int ColinearEdge( vec3_t pointA, vec3_t pointB, vec3_t lineEnd, vec_t tolerance ) {` |
| 1062 | `delta` | local / ColinearEdge | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t delta, direction, projected;` |
| 1062 | `direction` | local / ColinearEdge | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t delta, direction, projected;` |
| 1062 | `projected` | local / ColinearEdge | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t delta, direction, projected;` |
| 1063 | `projection` | local / ColinearEdge | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t projection, distance, length;` |
| 1063 | `distance` | local / ColinearEdge | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t projection, distance, length;` |
| 1063 | `length` | local / ColinearEdge | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec_t projection, distance, length;` |

## common/polylib.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 27 | `winding_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} winding_t;` |
| 25 | `numpoints` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int		numpoints;` |
| 26 | `p` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t	p[4];		// variable sized` |
| 29 | `MAX_POINTS_ON_WINDING` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAX_POINTS_ON_WINDING	1024` |
| 33 | `ON_EPSILON` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	ON_EPSILON	0.1` |
| 36 | `AllocWinding` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `winding_t	*AllocWinding (int points);` |
| 36 | `points` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*AllocWinding (int points);` |
| 37 | `WindingArea` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t	WindingArea (winding_t *w);` |
| 37 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t	WindingArea (winding_t *w);` |
| 38 | `WindingCenter` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	WindingCenter (winding_t *w, vec3_t center);` |
| 38 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingCenter (winding_t *w, vec3_t center);` |
| 38 | `center` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingCenter (winding_t *w, vec3_t center);` |
| 39 | `ClipWindingEpsilon` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 39 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 39 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 39 | `dist` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ClipWindingEpsilon (winding_t *in, vec3_t normal, vec_t dist,` |
| 40 | `epsilon` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn);` |
| 40 | `front` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn);` |
| 40 | `back` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn);` |
| 40 | `keepOn` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `vec_t epsilon, winding_t **front, winding_t **back, qboolean keepOn);` |
| 41 | `ChopWinding` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist);` |
| 41 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist);` |
| 41 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist);` |
| 41 | `dist` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ChopWinding (winding_t *in, vec3_t normal, vec_t dist);` |
| 42 | `CopyWinding` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `winding_t	*CopyWinding (winding_t *w);` |
| 42 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*CopyWinding (winding_t *w);` |
| 43 | `ReverseWinding` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `winding_t	*ReverseWinding (winding_t *w);` |
| 43 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*ReverseWinding (winding_t *w);` |
| 44 | `BaseWindingForPlane` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `winding_t	*BaseWindingForPlane (vec3_t normal, vec_t dist);` |
| 44 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*BaseWindingForPlane (vec3_t normal, vec_t dist);` |
| 44 | `dist` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `winding_t	*BaseWindingForPlane (vec3_t normal, vec_t dist);` |
| 45 | `CheckWinding` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	CheckWinding (winding_t *w);` |
| 45 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	CheckWinding (winding_t *w);` |
| 46 | `WindingPlane` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	WindingPlane (winding_t *w, vec3_t normal, vec_t *dist);` |
| 46 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingPlane (winding_t *w, vec3_t normal, vec_t *dist);` |
| 46 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingPlane (winding_t *w, vec3_t normal, vec_t *dist);` |
| 46 | `dist` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingPlane (winding_t *w, vec3_t normal, vec_t *dist);` |
| 47 | `RemoveColinearPoints` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	RemoveColinearPoints (winding_t *w);` |
| 47 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	RemoveColinearPoints (winding_t *w);` |
| 48 | `WindingOnPlaneSide` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist);` |
| 48 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist);` |
| 48 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist);` |
| 48 | `dist` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int		WindingOnPlaneSide (winding_t *w, vec3_t normal, vec_t dist);` |
| 49 | `FreeWinding` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	FreeWinding (winding_t *w);` |
| 49 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	FreeWinding (winding_t *w);` |
| 50 | `WindingBounds` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs);` |
| 50 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs);` |
| 50 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs);` |
| 50 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	WindingBounds (winding_t *w, vec3_t mins, vec3_t maxs);` |
| 52 | `AddWindingToConvexHull` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal );` |
| 52 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal );` |
| 52 | `hull` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal );` |
| 52 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	AddWindingToConvexHull( winding_t *w, winding_t **hull, vec3_t normal );` |
| 54 | `ChopWindingInPlace` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void	ChopWindingInPlace (winding_t **w, vec3_t normal, vec_t dist, vec_t epsilon);` |
| 54 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ChopWindingInPlace (winding_t **w, vec3_t normal, vec_t dist, vec_t epsilon);` |
| 54 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ChopWindingInPlace (winding_t **w, vec3_t normal, vec_t dist, vec_t epsilon);` |
| 54 | `dist` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ChopWindingInPlace (winding_t **w, vec3_t normal, vec_t dist, vec_t epsilon);` |
| 54 | `epsilon` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void	ChopWindingInPlace (winding_t **w, vec3_t normal, vec_t dist, vec_t epsilon);` |
| 57 | `pw` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void pw(winding_t *w);` |
| 57 | `w` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void pw(winding_t *w);` |

## common/q_round.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 16 | `Q_ROUND_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q_ROUND_H` |
| 18 | `FloorToInt` | function / FloorToInt | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `__inline int FloorToInt( float value ) {` |
| 18 | `value` | parameter / FloorToInt | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline int FloorToInt( float value ) {` |
| 19 | `bias` | local / FloorToInt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double bias = 0.49999999906867743;` |
| 20 | `result` | local / FloorToInt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int result;` |
| 29 | `CeilToInt` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `__inline int CeilToInt( float value );` |
| 29 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline int CeilToInt( float value );` |
| 30 | `RoundToInt` | function / RoundToInt | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `__inline int RoundToInt( float value ) {` |
| 30 | `value` | parameter / RoundToInt | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline int RoundToInt( float value ) {` |
| 31 | `result` | local / RoundToInt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int result;` |
| 33 | `bias` | local / RoundToInt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double bias = 9.31322574615478515625e-10;` |

## common/q_shared.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 25 | `colorBlack` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorBlack     = { 0.00f, 0.00f, 0.00f, 1.0f };` |
| 26 | `colorRed` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorRed       = { 1.00f, 0.00f, 0.00f, 1.0f };` |
| 27 | `colorGreen` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorGreen     = { 0.00f, 1.00f, 0.00f, 1.0f };` |
| 28 | `colorLtGreen` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `const vec4_t colorLtGreen   = { 0.00f, 0.70f, 0.00f, 1.0f };` |
| 29 | `colorBlue` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorBlue      = { 0.00f, 0.00f, 1.00f, 1.0f };` |
| 30 | `colorYellow` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorYellow    = { 1.00f, 1.00f, 0.00f, 1.0f };` |
| 31 | `colorLtYellow` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `const vec4_t colorLtYellow  = { 0.75f, 0.75f, 0.00f, 1.0f };` |
| 32 | `colorMdYellow` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorMdYellow  = { 0.50f, 0.50f, 0.00f, 1.0f };` |
| 33 | `colorMagenta` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorMagenta   = { 1.00f, 0.00f, 1.00f, 1.0f };` |
| 34 | `colorCyan` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorCyan      = { 0.00f, 1.00f, 1.00f, 1.0f };` |
| 35 | `colorLtCyan` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `const vec4_t colorLtCyan    = { 0.00f, 0.75f, 0.75f, 1.0f };` |
| 36 | `colorMdCyan` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorMdCyan    = { 0.00f, 0.50f, 0.50f, 1.0f };` |
| 37 | `colorDkCyan` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `const vec4_t colorDkCyan    = { 0.00f, 0.25f, 0.25f, 1.0f };` |
| 38 | `colorWhite` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorWhite     = { 1.00f, 1.00f, 1.00f, 1.0f };` |
| 39 | `colorLtGrey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorLtGrey    = { 0.75f, 0.75f, 0.75f, 1.0f };` |
| 40 | `colorMdGrey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorMdGrey    = { 0.50f, 0.50f, 0.50f, 1.0f };` |
| 41 | `colorDkGrey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorDkGrey    = { 0.25f, 0.25f, 0.25f, 1.0f };` |
| 42 | `colorOrange` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec4_t colorOrange    = { 1.00f, 0.70f, 0.00f, 1.0f };` |
| 43 | `colorLtOrange` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `const vec4_t colorLtOrange  = { 0.75f, 0.525f, 0.00f, 1.0f };` |
| 45 | `ERR_FATAL` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { ERR_FATAL = 0 };` |
| 46 | `BIG_INFO_STRING` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { BIG_INFO_STRING = 8192, BIG_INFO_KEY = 8192, BIG_INFO_VALUE = 8192 };` |
| 46 | `BIG_INFO_KEY` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { BIG_INFO_STRING = 8192, BIG_INFO_KEY = 8192, BIG_INFO_VALUE = 8192 };` |
| 46 | `BIG_INFO_VALUE` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { BIG_INFO_STRING = 8192, BIG_INFO_KEY = 8192, BIG_INFO_VALUE = 8192 };` |
| 47 | `MAX_VA_STRING` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { MAX_VA_STRING = 32000 };` |
| 48 | `MAX_INFO_KEY` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { MAX_INFO_KEY = 1024, MAX_INFO_VALUE = 1024 };` |
| 48 | `MAX_INFO_VALUE` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { MAX_INFO_KEY = 1024, MAX_INFO_VALUE = 1024 };` |
| 49 | `MAX_QPATH` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { MAX_QPATH = 64 };` |
| 54 | `orientation_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} orientation_t;` |
| 52 | `origin` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t origin;` |
| 53 | `axis` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t axis[3];` |
| 56 | `_BigShort` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static short ( *_BigShort )( short l );` |
| 56 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static short ( *_BigShort )( short l );` |
| 57 | `_LittleShort` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static short ( *_LittleShort )( short l );` |
| 57 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static short ( *_LittleShort )( short l );` |
| 58 | `_BigLong` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static int ( *_BigLong )( int l );` |
| 58 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int ( *_BigLong )( int l );` |
| 59 | `_LittleLong` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static int ( *_LittleLong )( int l );` |
| 59 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static int ( *_LittleLong )( int l );` |
| 60 | `_BigLong64` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static qint64 ( *_BigLong64 )( qint64 l );` |
| 60 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static qint64 ( *_BigLong64 )( qint64 l );` |
| 61 | `_LittleLong64` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static qint64 ( *_LittleLong64 )( qint64 l );` |
| 61 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static qint64 ( *_LittleLong64 )( qint64 l );` |
| 62 | `_BigFloat` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static float ( *_BigFloat )( float l );` |
| 62 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static float ( *_BigFloat )( float l );` |
| 63 | `_LittleFloat` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static float ( *_LittleFloat )( float l );` |
| 63 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static float ( *_LittleFloat )( float l );` |
| 65 | `LongNoSwap` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int LongNoSwap( int l );` |
| 65 | `l` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int LongNoSwap( int l );` |
| 76 | `csFieldType_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} csFieldType_t;` |
| 68 | `CS_FIELD_CUSTOM` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_CUSTOM = 0,` |
| 69 | `CS_FIELD_STRING1024` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_STRING1024 = 1,` |
| 70 | `CS_FIELD_STRING64` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_STRING64 = 2,` |
| 71 | `CS_FIELD_STRING256` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_STRING256 = 3,` |
| 72 | `CS_FIELD_INT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_INT = 4,` |
| 73 | `CS_FIELD_QBOOLEAN` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_QBOOLEAN = 5,` |
| 74 | `CS_FIELD_FLOAT` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_FLOAT = 6,` |
| 75 | `CS_FIELD_MILLISECONDS` | enum value | inferred/unconfirmed spelling. Names the displayed numeric case of the containing enumeration. | `CS_FIELD_MILLISECONDS = 7` |
| 82 | `csField_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} csField_t;` |
| 79 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `const char *name;` |
| 80 | `offset` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int offset;` |
| 81 | `type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int type;` |
| 89 | `ColorIndex` | function / ColorIndex | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int ColorIndex( char c ) {` |
| 89 | `c` | parameter / ColorIndex | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int ColorIndex( char c ) {` |
| 90 | `index` | local / ColorIndex | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned char index;` |
| 104 | `Com_Clamp` | function / Com_Clamp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Com_Clamp( float min, float max, float value ) {` |
| 104 | `min` | parameter / Com_Clamp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_Clamp( float min, float max, float value ) {` |
| 104 | `max` | parameter / Com_Clamp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_Clamp( float min, float max, float value ) {` |
| 104 | `value` | parameter / Com_Clamp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_Clamp( float min, float max, float value ) {` |
| 119 | `Com_SkipPath` | function / Com_SkipPath | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_SkipPath( char *pathname ) {` |
| 119 | `pathname` | parameter / Com_SkipPath | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_SkipPath( char *pathname ) {` |
| 120 | `last` | local / Com_SkipPath | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *last;` |
| 137 | `Com_StripExtension` | function / Com_StripExtension | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_StripExtension( const char *in, char *out ) {` |
| 137 | `in` | parameter / Com_StripExtension | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_StripExtension( const char *in, char *out ) {` |
| 137 | `out` | parameter / Com_StripExtension | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_StripExtension( const char *in, char *out ) {` |
| 149 | `Q_fabs` | function / Q_fabs | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Q_fabs( float f ) {` |
| 149 | `f` | parameter / Q_fabs | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_fabs( float f ) {` |
| 150 | `tmp` | local / Q_fabs | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int tmp = * ( int * ) &f;` |
| 160 | `Com_BitCheck` | function / Com_BitCheck | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean Com_BitCheck( const int array[], int bitNum ) {` |
| 160 | `array` | parameter / Com_BitCheck | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Com_BitCheck( const int array[], int bitNum ) {` |
| 160 | `bitNum` | parameter / Com_BitCheck | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Com_BitCheck( const int array[], int bitNum ) {` |
| 169 | `Com_BitSet` | function / Com_BitSet | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_BitSet( int array[], int bitNum ) {` |
| 169 | `array` | parameter / Com_BitSet | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BitSet( int array[], int bitNum ) {` |
| 169 | `bitNum` | parameter / Com_BitSet | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BitSet( int array[], int bitNum ) {` |
| 178 | `Com_BitClear` | function / Com_BitClear | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_BitClear( int array[], int bitNum ) {` |
| 178 | `array` | parameter / Com_BitClear | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BitClear( int array[], int bitNum ) {` |
| 178 | `bitNum` | parameter / Com_BitClear | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BitClear( int array[], int bitNum ) {` |
| 187 | `BigShort` | function / BigShort | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `short BigShort( short l ) {` |
| 187 | `l` | parameter / BigShort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `short BigShort( short l ) {` |
| 196 | `BigLong` | function / BigLong | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int BigLong( int l ) {` |
| 196 | `l` | parameter / BigLong | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BigLong( int l ) {` |
| 205 | `BigLong64` | function / BigLong64 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qint64 BigLong64( qint64 l ) {` |
| 205 | `l` | parameter / BigLong64 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qint64 BigLong64( qint64 l ) {` |
| 214 | `LittleLong64` | function / LittleLong64 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qint64 LittleLong64( qint64 l ) {` |
| 214 | `l` | parameter / LittleLong64 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qint64 LittleLong64( qint64 l ) {` |
| 223 | `BigFloat` | function / BigFloat | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float BigFloat( float l ) {` |
| 223 | `l` | parameter / BigFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float BigFloat( float l ) {` |
| 232 | `ShortSwap` | function / ShortSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `short ShortSwap( short l ) {` |
| 232 | `l` | parameter / ShortSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `short ShortSwap( short l ) {` |
| 233 | `b1` | local / ShortSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte b1, b2;` |
| 233 | `b2` | local / ShortSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte b1, b2;` |
| 246 | `ShortNoSwap` | function / ShortNoSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `short ShortNoSwap( short l ) {` |
| 246 | `l` | parameter / ShortNoSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `short ShortNoSwap( short l ) {` |
| 255 | `LongSwap` | function / LongSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int LongSwap( int l ) {` |
| 255 | `l` | parameter / LongSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int LongSwap( int l ) {` |
| 256 | `b1` | local / LongSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte b1, b2, b3, b4;` |
| 256 | `b2` | local / LongSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte b1, b2, b3, b4;` |
| 256 | `b3` | local / LongSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte b1, b2, b3, b4;` |
| 256 | `b4` | local / LongSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte b1, b2, b3, b4;` |
| 271 | `LongNoSwap` | function / LongNoSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int LongNoSwap( int l ) {` |
| 271 | `l` | parameter / LongNoSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int LongNoSwap( int l ) {` |
| 280 | `Long64Swap` | function / Long64Swap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qint64 Long64Swap( qint64 ll ) {` |
| 280 | `ll` | parameter / Long64Swap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qint64 Long64Swap( qint64 ll ) {` |
| 281 | `result` | local / Long64Swap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qint64 result;` |
| 300 | `Long64NoSwap` | function / Long64NoSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qint64 Long64NoSwap( qint64 ll ) {` |
| 300 | `ll` | parameter / Long64NoSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qint64 Long64NoSwap( qint64 ll ) {` |
| 309 | `FloatSwap` | function / FloatSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float FloatSwap( float f ) {` |
| 309 | `f` | parameter / FloatSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float FloatSwap( float f ) {` |
| 313 | `dat1` | local / FloatSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `} dat1, dat2;` |
| 313 | `dat2` | local / FloatSwap | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `} dat1, dat2;` |
| 311 | `f` | field / FloatSwap | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float f;` |
| 312 | `b` | field / FloatSwap | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b[4];` |
| 328 | `FloatNoSwap` | function / FloatNoSwap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float FloatNoSwap( float f ) {` |
| 328 | `f` | parameter / FloatNoSwap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float FloatNoSwap( float f ) {` |
| 337 | `Swap_Init` | function / Swap_Init | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Swap_Init( void ) {` |
| 338 | `swaptest` | local / Swap_Init | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte swaptest[2] = { 1, 0 };` |
| 366 | `Q_isprint` | function / Q_isprint | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_isprint( int c ) {` |
| 366 | `c` | parameter / Q_isprint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_isprint( int c ) {` |
| 378 | `Q_islower` | function / Q_islower | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_islower( int c ) {` |
| 378 | `c` | parameter / Q_islower | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_islower( int c ) {` |
| 390 | `Q_isupper` | function / Q_isupper | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_isupper( int c ) {` |
| 390 | `c` | parameter / Q_isupper | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_isupper( int c ) {` |
| 402 | `Q_isalpha` | function / Q_isalpha | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_isalpha( int c ) {` |
| 402 | `c` | parameter / Q_isalpha | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_isalpha( int c ) {` |
| 414 | `Q_isnumeric` | function / Q_isnumeric | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_isnumeric( int c ) {` |
| 414 | `c` | parameter / Q_isnumeric | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_isnumeric( int c ) {` |
| 426 | `Q_isalphanumeric` | function / Q_isalphanumeric | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_isalphanumeric( int c ) {` |
| 426 | `c` | parameter / Q_isalphanumeric | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_isalphanumeric( int c ) {` |
| 438 | `Q_isnamechar` | function / Q_isnamechar | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_isnamechar( int c ) {` |
| 438 | `c` | parameter / Q_isnamechar | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_isnamechar( int c ) {` |
| 452 | `Q_strrchr` | function / Q_strrchr | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Q_strrchr( const char *string, int c ) {` |
| 452 | `string` | parameter / Q_strrchr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Q_strrchr( const char *string, int c ) {` |
| 452 | `c` | parameter / Q_strrchr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Q_strrchr( const char *string, int c ) {` |
| 453 | `cc` | local / Q_strrchr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char cc = c;` |
| 454 | `s` | local / Q_strrchr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 455 | `sp` | local / Q_strrchr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *sp = NULL;` |
| 477 | `Q_strncpyz` | function / Q_strncpyz | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Q_strncpyz( char *dest, const char *src, int destsize ) {` |
| 477 | `dest` | parameter / Q_strncpyz | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize ) {` |
| 477 | `src` | parameter / Q_strncpyz | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize ) {` |
| 477 | `destsize` | parameter / Q_strncpyz | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize ) {` |
| 487 | `Q_stricmpn` | function / Q_stricmpn | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_stricmpn( const char *s1, const char *s2, int n ) {` |
| 487 | `s1` | parameter / Q_stricmpn | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n ) {` |
| 487 | `s2` | parameter / Q_stricmpn | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n ) {` |
| 487 | `n` | parameter / Q_stricmpn | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n ) {` |
| 488 | `c1` | local / Q_stricmpn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 488 | `c2` | local / Q_stricmpn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 518 | `Q_strncmp` | function / Q_strncmp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_strncmp( const char *s1, const char *s2, int n ) {` |
| 518 | `s1` | parameter / Q_strncmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncmp( const char *s1, const char *s2, int n ) {` |
| 518 | `s2` | parameter / Q_strncmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncmp( const char *s1, const char *s2, int n ) {` |
| 518 | `n` | parameter / Q_strncmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncmp( const char *s1, const char *s2, int n ) {` |
| 519 | `c1` | local / Q_strncmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 519 | `c2` | local / Q_strncmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 541 | `Q_stricmp` | function / Q_stricmp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_stricmp( const char *s1, const char *s2 ) {` |
| 541 | `s1` | parameter / Q_stricmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmp( const char *s1, const char *s2 ) {` |
| 541 | `s2` | parameter / Q_stricmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmp( const char *s1, const char *s2 ) {` |
| 550 | `Q_strlwr` | function / Q_strlwr | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Q_strlwr( char *s1 ) {` |
| 550 | `s1` | parameter / Q_strlwr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Q_strlwr( char *s1 ) {` |
| 551 | `s` | local / Q_strlwr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 566 | `Q_strupr` | function / Q_strupr | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Q_strupr( char *s1 ) {` |
| 566 | `s1` | parameter / Q_strupr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Q_strupr( char *s1 ) {` |
| 567 | `s` | local / Q_strupr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 582 | `Q_strcat` | function / Q_strcat | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Q_strcat( char *dest, int size, const char *src ) {` |
| 582 | `dest` | parameter / Q_strcat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strcat( char *dest, int size, const char *src ) {` |
| 582 | `size` | parameter / Q_strcat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strcat( char *dest, int size, const char *src ) {` |
| 582 | `src` | parameter / Q_strcat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strcat( char *dest, int size, const char *src ) {` |
| 583 | `l1` | local / Q_strcat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int l1;` |
| 597 | `Q_PrintStrlen` | function / Q_PrintStrlen | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_PrintStrlen( const char *string ) {` |
| 597 | `string` | parameter / Q_PrintStrlen | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_PrintStrlen( const char *string ) {` |
| 598 | `len` | local / Q_PrintStrlen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 599 | `p` | local / Q_PrintStrlen | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *p;` |
| 619 | `Q_CleanStr` | function / Q_CleanStr | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Q_CleanStr( char *string ) {` |
| 619 | `string` | parameter / Q_CleanStr | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Q_CleanStr( char *string ) {` |
| 620 | `d` | local / Q_CleanStr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *d;` |
| 621 | `s` | local / Q_CleanStr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 622 | `c` | local / Q_CleanStr | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c;` |
| 643 | `Q_CleanCharacter` | function / Q_CleanCharacter | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char Q_CleanCharacter( char c ) {` |
| 643 | `c` | parameter / Q_CleanCharacter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char Q_CleanCharacter( char c ) {` |
| 652 | `Com_sprintf` | function / Com_sprintf | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_sprintf( char *dest, int size, const char *fmt, ... ) {` |
| 652 | `dest` | parameter / Com_sprintf | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_sprintf( char *dest, int size, const char *fmt, ... ) {` |
| 652 | `size` | parameter / Com_sprintf | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_sprintf( char *dest, int size, const char *fmt, ... ) {` |
| 652 | `fmt` | parameter / Com_sprintf | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_sprintf( char *dest, int size, const char *fmt, ... ) {` |
| 653 | `len` | local / Com_sprintf | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 654 | `argptr` | local / Com_sprintf | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `va_list argptr;` |
| 669 | `Q_strncasecmp` | function / Q_strncasecmp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_strncasecmp( const char *s1, const char *s2, int n ) {` |
| 669 | `s1` | parameter / Q_strncasecmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncasecmp( const char *s1, const char *s2, int n ) {` |
| 669 | `s2` | parameter / Q_strncasecmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncasecmp( const char *s1, const char *s2, int n ) {` |
| 669 | `n` | parameter / Q_strncasecmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strncasecmp( const char *s1, const char *s2, int n ) {` |
| 670 | `c1` | local / Q_strncasecmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 670 | `c2` | local / Q_strncasecmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c1, c2;` |
| 700 | `Q_strcasecmp` | function / Q_strcasecmp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_strcasecmp( char *s1, char *s2 ) {` |
| 700 | `s1` | parameter / Q_strcasecmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strcasecmp( char *s1, char *s2 ) {` |
| 700 | `s2` | parameter / Q_strcasecmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_strcasecmp( char *s1, char *s2 ) {` |
| 713 | `va` | function / va | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *va( char *format, ... ) {` |
| 713 | `format` | parameter / va | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *va( char *format, ... ) {` |
| 714 | `argptr` | local / va | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `va_list argptr;` |
| 715 | `buffer` | local / va | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static char buffer[MAX_VA_STRING];` |
| 716 | `vabuf` | local / va | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `static char vabuf[MAX_VA_STRING];` |
| 717 | `index` | local / va | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static int index = 0;` |
| 718 | `buf` | local / va | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *buf;` |
| 719 | `len` | local / va | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 744 | `tv` | function / tv | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float *tv( float x, float y, float z ) {` |
| 744 | `x` | parameter / tv | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float *tv( float x, float y, float z ) {` |
| 744 | `y` | parameter / tv | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float *tv( float x, float y, float z ) {` |
| 744 | `z` | parameter / tv | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float *tv( float x, float y, float z ) {` |
| 745 | `index` | local / tv | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static int index;` |
| 746 | `vecs` | local / tv | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static vec3_t vecs[8];` |
| 747 | `v` | local / tv | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float *v;` |
| 768 | `Info_ValueForKey` | function / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Info_ValueForKey( const char *s, const char *key ) {` |
| 768 | `s` | parameter / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Info_ValueForKey( const char *s, const char *key ) {` |
| 768 | `key` | parameter / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Info_ValueForKey( const char *s, const char *key ) {` |
| 769 | `pkey` | local / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char pkey[BIG_INFO_KEY];` |
| 770 | `buf` | local / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static char buf[2][BIG_INFO_VALUE];` |
| 771 | `valueindex` | local / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static int valueindex = 0;` |
| 772 | `o` | local / Info_ValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *o;` |
| 820 | `Info_NextPair` | function / Info_NextPair | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Info_NextPair( const char **head, char *key, char *value ) {` |
| 820 | `head` | parameter / Info_NextPair | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_NextPair( const char **head, char *key, char *value ) {` |
| 820 | `key` | parameter / Info_NextPair | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_NextPair( const char **head, char *key, char *value ) {` |
| 820 | `value` | parameter / Info_NextPair | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_NextPair( const char **head, char *key, char *value ) {` |
| 821 | `o` | local / Info_NextPair | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *o;` |
| 822 | `s` | local / Info_NextPair | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char *s;` |
| 856 | `Info_RemoveKey` | function / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Info_RemoveKey( char *s, const char *key ) {` |
| 856 | `s` | parameter / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_RemoveKey( char *s, const char *key ) {` |
| 856 | `key` | parameter / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_RemoveKey( char *s, const char *key ) {` |
| 857 | `start` | local / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *start;` |
| 858 | `pkey` | local / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char pkey[MAX_INFO_KEY];` |
| 859 | `value` | local / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char value[MAX_INFO_VALUE];` |
| 860 | `o` | local / Info_RemoveKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *o;` |
| 908 | `Info_RemoveKey_Big` | function / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Info_RemoveKey_Big( char *s, const char *key ) {` |
| 908 | `s` | parameter / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_RemoveKey_Big( char *s, const char *key ) {` |
| 908 | `key` | parameter / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_RemoveKey_Big( char *s, const char *key ) {` |
| 909 | `start` | local / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *start;` |
| 910 | `pkey` | local / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char pkey[BIG_INFO_KEY];` |
| 911 | `value` | local / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char value[BIG_INFO_VALUE];` |
| 912 | `o` | local / Info_RemoveKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *o;` |
| 963 | `Info_Validate` | function / Info_Validate | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean Info_Validate( const char *s ) {` |
| 963 | `s` | parameter / Info_Validate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Info_Validate( const char *s ) {` |
| 980 | `Info_SetValueForKey` | function / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Info_SetValueForKey( char *s, const char *key, const char *value ) {` |
| 980 | `s` | parameter / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey( char *s, const char *key, const char *value ) {` |
| 980 | `key` | parameter / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey( char *s, const char *key, const char *value ) {` |
| 980 | `value` | parameter / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey( char *s, const char *key, const char *value ) {` |
| 981 | `newi` | local / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char newi[MAX_INFO_STRING];` |
| 982 | `cleanValue` | local / Info_SetValueForKey | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char cleanValue[MAX_INFO_STRING];` |
| 983 | `i` | local / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 983 | `j` | local / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 992 | `c` | local / Info_SetValueForKey | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c = value[i];` |
| 1043 | `Info_SetValueForKey_Big` | function / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Info_SetValueForKey_Big( char *s, const char *key, const char *value ) {` |
| 1043 | `s` | parameter / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey_Big( char *s, const char *key, const char *value ) {` |
| 1043 | `key` | parameter / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey_Big( char *s, const char *key, const char *value ) {` |
| 1043 | `value` | parameter / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey_Big( char *s, const char *key, const char *value ) {` |
| 1044 | `newi` | local / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char newi[BIG_INFO_STRING];` |
| 1045 | `cleanValue` | local / Info_SetValueForKey_Big | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `char cleanValue[BIG_INFO_STRING];` |
| 1046 | `i` | local / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 1046 | `j` | local / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i, j;` |
| 1055 | `c` | local / Info_SetValueForKey_Big | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c = value[i];` |
| 1104 | `ParseConfigStringToStruct` | function / ParseConfigStringToStruct | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean ParseConfigStringToStruct( void *structBase, const csField_t *fields, int numFields,` |
| 1104 | `structBase` | parameter / ParseConfigStringToStruct | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `qboolean ParseConfigStringToStruct( void *structBase, const csField_t *fields, int numFields,` |
| 1104 | `fields` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean ParseConfigStringToStruct( void *structBase, const csField_t *fields, int numFields,` |
| 1104 | `numFields` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean ParseConfigStringToStruct( void *structBase, const csField_t *fields, int numFields,` |
| 1105 | `s` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *s, int numCustomTypes,` |
| 1105 | `numCustomTypes` | parameter / ParseConfigStringToStruct | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `const char *s, int numCustomTypes,` |
| 1106 | `customHandler` | parameter / ParseConfigStringToStruct | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `qboolean ( *customHandler )( void *base, const char *value, int type ),` |
| 1106 | `base` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean ( *customHandler )( void *base, const char *value, int type ),` |
| 1106 | `value` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean ( *customHandler )( void *base, const char *value, int type ),` |
| 1106 | `type` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean ( *customHandler )( void *base, const char *value, int type ),` |
| 1107 | `vectorHandler` | parameter / ParseConfigStringToStruct | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ( *vectorHandler )( void *dest, const char *value ) ) {` |
| 1107 | `dest` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ( *vectorHandler )( void *dest, const char *value ) ) {` |
| 1107 | `value` | parameter / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ( *vectorHandler )( void *dest, const char *value ) ) {` |
| 1108 | `i` | local / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1109 | `value` | local / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *value;` |
| 1110 | `base` | local / ParseConfigStringToStruct | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte *base = (byte *)structBase;` |
| 1163 | `GetLeanFraction` | function / GetLeanFraction | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float GetLeanFraction( float f ) {` |
| 1163 | `f` | parameter / GetLeanFraction | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float GetLeanFraction( float f ) {` |
| 1164 | `g` | local / GetLeanFraction | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float g = f;` |
| 1165 | `tmp` | local / GetLeanFraction | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int tmp = * ( int * ) &g;` |
| 1166 | `r` | local / GetLeanFraction | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float r;` |
| 1177 | `UnGetLeanFraction` | function / UnGetLeanFraction | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float UnGetLeanFraction( float f ) {` |
| 1177 | `f` | parameter / UnGetLeanFraction | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float UnGetLeanFraction( float f ) {` |
| 1186 | `AddLeanToPosition` | function / AddLeanToPosition | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale ) {` |
| 1186 | `pos` | parameter / AddLeanToPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale ) {` |
| 1186 | `yaw` | parameter / AddLeanToPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale ) {` |
| 1186 | `leanFrac` | parameter / AddLeanToPosition | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale ) {` |
| 1186 | `leanDist` | parameter / AddLeanToPosition | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale ) {` |
| 1186 | `scale` | parameter / AddLeanToPosition | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale ) {` |
| 1187 | `frac` | local / AddLeanToPosition | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float frac;` |
| 1188 | `angles` | local / AddLeanToPosition | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t angles;` |
| 1189 | `right` | local / AddLeanToPosition | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t right;` |
| 1210 | `OrientationPosToWorldPos` | function / OrientationPosToWorldPos | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void OrientationPosToWorldPos( const orientation_t *orient, const vec3_t pos, vec3_t out ) {` |
| 1210 | `orient` | parameter / OrientationPosToWorldPos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationPosToWorldPos( const orientation_t *orient, const vec3_t pos, vec3_t out ) {` |
| 1210 | `pos` | parameter / OrientationPosToWorldPos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationPosToWorldPos( const orientation_t *orient, const vec3_t pos, vec3_t out ) {` |
| 1210 | `out` | parameter / OrientationPosToWorldPos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationPosToWorldPos( const orientation_t *orient, const vec3_t pos, vec3_t out ) {` |
| 1221 | `OrientationDirToWorldDir` | function / OrientationDirToWorldDir | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void OrientationDirToWorldDir( const orientation_t *orient, const vec3_t dir, vec3_t out ) {` |
| 1221 | `orient` | parameter / OrientationDirToWorldDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationDirToWorldDir( const orientation_t *orient, const vec3_t dir, vec3_t out ) {` |
| 1221 | `dir` | parameter / OrientationDirToWorldDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationDirToWorldDir( const orientation_t *orient, const vec3_t dir, vec3_t out ) {` |
| 1221 | `out` | parameter / OrientationDirToWorldDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationDirToWorldDir( const orientation_t *orient, const vec3_t dir, vec3_t out ) {` |
| 1232 | `OrientationPosFromWorldPos` | function / OrientationPosFromWorldPos | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void OrientationPosFromWorldPos( const orientation_t *orient, const vec3_t worldPos, vec3_t out ) {` |
| 1232 | `orient` | parameter / OrientationPosFromWorldPos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationPosFromWorldPos( const orientation_t *orient, const vec3_t worldPos, vec3_t out ) {` |
| 1232 | `worldPos` | parameter / OrientationPosFromWorldPos | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void OrientationPosFromWorldPos( const orientation_t *orient, const vec3_t worldPos, vec3_t out ) {` |
| 1232 | `out` | parameter / OrientationPosFromWorldPos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationPosFromWorldPos( const orientation_t *orient, const vec3_t worldPos, vec3_t out ) {` |
| 1233 | `delta` | local / OrientationPosFromWorldPos | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t delta;` |
| 1246 | `OrientationDirFromWorldDir` | function / OrientationDirFromWorldDir | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void OrientationDirFromWorldDir( const orientation_t *orient, const vec3_t worldDir, vec3_t out ) {` |
| 1246 | `orient` | parameter / OrientationDirFromWorldDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationDirFromWorldDir( const orientation_t *orient, const vec3_t worldDir, vec3_t out ) {` |
| 1246 | `worldDir` | parameter / OrientationDirFromWorldDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationDirFromWorldDir( const orientation_t *orient, const vec3_t worldDir, vec3_t out ) {` |
| 1246 | `out` | parameter / OrientationDirFromWorldDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void OrientationDirFromWorldDir( const orientation_t *orient, const vec3_t worldDir, vec3_t out ) {` |
| 1257 | `Q_DecimalPoint` | function / Q_DecimalPoint | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char Q_DecimalPoint( int language ) {` |
| 1257 | `language` | parameter / Q_DecimalPoint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char Q_DecimalPoint( int language ) {` |
| 1269 | `Q_FormatFloat` | function / Q_FormatFloat | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Q_FormatFloat( float value, char *buffer, unsigned int size, int digits, int language ) {` |
| 1269 | `value` | parameter / Q_FormatFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_FormatFloat( float value, char *buffer, unsigned int size, int digits, int language ) {` |
| 1269 | `buffer` | parameter / Q_FormatFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_FormatFloat( float value, char *buffer, unsigned int size, int digits, int language ) {` |
| 1269 | `size` | parameter / Q_FormatFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_FormatFloat( float value, char *buffer, unsigned int size, int digits, int language ) {` |
| 1269 | `digits` | parameter / Q_FormatFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_FormatFloat( float value, char *buffer, unsigned int size, int digits, int language ) {` |
| 1269 | `language` | parameter / Q_FormatFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_FormatFloat( float value, char *buffer, unsigned int size, int digits, int language ) {` |
| 1270 | `i` | local / Q_FormatFloat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned int i;` |
| 1289 | `Com_StripFilename` | function / Com_StripFilename | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_StripFilename( char *in, char *out ) {` |
| 1289 | `in` | parameter / Com_StripFilename | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_StripFilename( char *in, char *out ) {` |
| 1289 | `out` | parameter / Com_StripFilename | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_StripFilename( char *in, char *out ) {` |
| 1290 | `end` | local / Com_StripFilename | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *end;` |
| 1302 | `Com_DefaultExtension` | function / Com_DefaultExtension | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_DefaultExtension( char *path, int maxSize, const char *extension ) {` |
| 1302 | `path` | parameter / Com_DefaultExtension | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_DefaultExtension( char *path, int maxSize, const char *extension ) {` |
| 1302 | `maxSize` | parameter / Com_DefaultExtension | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_DefaultExtension( char *path, int maxSize, const char *extension ) {` |
| 1302 | `extension` | parameter / Com_DefaultExtension | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_DefaultExtension( char *path, int maxSize, const char *extension ) {` |
| 1303 | `oldPath` | local / Com_DefaultExtension | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char oldPath[MAX_QPATH];` |
| 1304 | `src` | local / Com_DefaultExtension | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *src;` |

## common/q_shared.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 24 | `Q3MAP_Q_SHARED_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_Q_SHARED_H` |
| 39 | `qint64` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} qint64;` |
| 31 | `b0` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b0;` |
| 32 | `b1` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b1;` |
| 33 | `b2` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b2;` |
| 34 | `b3` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b3;` |
| 35 | `b4` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b4;` |
| 36 | `b5` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b5;` |
| 37 | `b6` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b6;` |
| 38 | `b7` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte b7;` |
| 41 | `Com_BitSet` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Com_BitSet( int array[], int bitNum );` |
| 41 | `array` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BitSet( int array[], int bitNum );` |
| 41 | `bitNum` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BitSet( int array[], int bitNum );` |
| 42 | `Long64Swap` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qint64 Long64Swap( qint64 ll );` |
| 42 | `ll` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qint64 Long64Swap( qint64 ll );` |
| 43 | `Q_islower` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_islower( int c );` |
| 43 | `c` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_islower( int c );` |
| 44 | `Q_stricmpn` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 44 | `s1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 44 | `s2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 44 | `n` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_stricmpn( const char *s1, const char *s2, int n );` |
| 45 | `Q_CleanCharacter` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `char Q_CleanCharacter( char c );` |
| 45 | `c` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char Q_CleanCharacter( char c );` |
| 46 | `tv` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float *tv( float x, float y, float z );` |
| 46 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float *tv( float x, float y, float z );` |
| 46 | `y` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float *tv( float x, float y, float z );` |
| 46 | `z` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float *tv( float x, float y, float z );` |
| 48 | `MAX_INFO_STRING` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_INFO_STRING 1024` |
| 49 | `ERR_DROP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ERR_DROP 1` |
| 51 | `Com_Error` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Error( int code, const char *format, ... );` |
| 51 | `code` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Error( int code, const char *format, ... );` |
| 51 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Error( int code, const char *format, ... );` |
| 52 | `Com_Printf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Printf( const char *format, ... );` |
| 52 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Printf( const char *format, ... );` |
| 53 | `Com_sprintf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 53 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 53 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 53 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 54 | `Info_RemoveKey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Info_RemoveKey( char *s, const char *key );` |
| 54 | `s` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_RemoveKey( char *s, const char *key );` |
| 54 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_RemoveKey( char *s, const char *key );` |
| 55 | `Info_SetValueForKey` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Info_SetValueForKey( char *s, const char *key, const char *value );` |
| 55 | `s` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey( char *s, const char *key, const char *value );` |
| 55 | `key` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey( char *s, const char *key, const char *value );` |
| 55 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Info_SetValueForKey( char *s, const char *key, const char *value );` |

## common/q_shared_vectors.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 11 | `Q3MAP_Q_SHARED_VECTORS_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_Q_SHARED_VECTORS_H` |
| 15 | `VectorSet` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorSet( v, x, y, z ) ( (v)[0] = (x), (v)[1] = (y), (v)[2] = (z) )` |
| 17 | `GetLeanFraction` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float GetLeanFraction( float f );` |
| 17 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float GetLeanFraction( float f );` |
| 18 | `AngleVectors` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 18 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 18 | `forward` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 18 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 18 | `up` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 19 | `AddLeanToPosition` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale );` |
| 19 | `pos` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale );` |
| 19 | `yaw` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale );` |
| 19 | `leanFrac` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale );` |
| 19 | `leanDist` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale );` |
| 19 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddLeanToPosition( float *pos, float yaw, float leanFrac, float leanDist, float scale );` |

## common/scriplib.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 32 | `MAXTOKEN` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define	MAXTOKEN	1024` |
| 34 | `token` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char	token[MAXTOKEN];` |
| 35 | `scriptbuffer` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char	*scriptbuffer,*script_p,*scriptend_p;` |
| 35 | `script_p` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char	*scriptbuffer,*script_p,*scriptend_p;` |
| 35 | `scriptend_p` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	char	*scriptbuffer,*script_p,*scriptend_p;` |
| 36 | `grabbed` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int		grabbed;` |
| 37 | `scriptline` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int		scriptline;` |
| 38 | `endofscript` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	qboolean	endofscript;` |
| 41 | `LoadScriptFile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void LoadScriptFile( const char *filename );` |
| 41 | `filename` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void LoadScriptFile( const char *filename );` |
| 42 | `ParseFromMemory` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ParseFromMemory (char *buffer, int size);` |
| 42 | `buffer` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ParseFromMemory (char *buffer, int size);` |
| 42 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ParseFromMemory (char *buffer, int size);` |
| 44 | `GetToken` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean GetToken (qboolean crossline);` |
| 44 | `crossline` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean GetToken (qboolean crossline);` |
| 45 | `UnGetToken` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void UnGetToken (void);` |
| 46 | `TokenAvailable` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean TokenAvailable (void);` |
| 48 | `MatchToken` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void MatchToken( char *match );` |
| 48 | `match` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatchToken( char *match );` |
| 50 | `Parse1DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Parse1DMatrix (int x, vec_t *m);` |
| 50 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse1DMatrix (int x, vec_t *m);` |
| 50 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse1DMatrix (int x, vec_t *m);` |
| 51 | `Parse2DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Parse2DMatrix (int y, int x, vec_t *m);` |
| 51 | `y` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse2DMatrix (int y, int x, vec_t *m);` |
| 51 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse2DMatrix (int y, int x, vec_t *m);` |
| 51 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse2DMatrix (int y, int x, vec_t *m);` |
| 52 | `Parse3DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Parse3DMatrix (int z, int y, int x, vec_t *m);` |
| 52 | `z` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse3DMatrix (int z, int y, int x, vec_t *m);` |
| 52 | `y` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse3DMatrix (int z, int y, int x, vec_t *m);` |
| 52 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse3DMatrix (int z, int y, int x, vec_t *m);` |
| 52 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Parse3DMatrix (int z, int y, int x, vec_t *m);` |
| 54 | `Write1DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Write1DMatrix (FILE *f, int x, vec_t *m);` |
| 54 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write1DMatrix (FILE *f, int x, vec_t *m);` |
| 54 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write1DMatrix (FILE *f, int x, vec_t *m);` |
| 54 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write1DMatrix (FILE *f, int x, vec_t *m);` |
| 55 | `Write2DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Write2DMatrix (FILE *f, int y, int x, vec_t *m);` |
| 55 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write2DMatrix (FILE *f, int y, int x, vec_t *m);` |
| 55 | `y` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write2DMatrix (FILE *f, int y, int x, vec_t *m);` |
| 55 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write2DMatrix (FILE *f, int y, int x, vec_t *m);` |
| 55 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write2DMatrix (FILE *f, int y, int x, vec_t *m);` |
| 56 | `Write3DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Write3DMatrix (FILE *f, int z, int y, int x, vec_t *m);` |
| 56 | `f` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write3DMatrix (FILE *f, int z, int y, int x, vec_t *m);` |
| 56 | `z` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write3DMatrix (FILE *f, int z, int y, int x, vec_t *m);` |
| 56 | `y` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write3DMatrix (FILE *f, int z, int y, int x, vec_t *m);` |
| 56 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write3DMatrix (FILE *f, int z, int y, int x, vec_t *m);` |
| 56 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Write3DMatrix (FILE *f, int z, int y, int x, vec_t *m);` |

## common/threads.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 27 | `threaded` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean threaded;` |
| 28 | `crit` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `CRITICAL_SECTION crit;` |
| 29 | `enter` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static int enter;` |
| 31 | `MAX_THREADS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_THREADS 64` |
| 33 | `numthreads` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int numthreads = -1;` |
| 34 | `dispatch` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int dispatch;` |
| 35 | `workcount` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int workcount;` |
| 36 | `oldf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int oldf;` |
| 37 | `pacifier` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean pacifier;` |
| 38 | `workfunction` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void (*workfunction)(int);` |
| 45 | `ThreadSetDefault` | function / ThreadSetDefault | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ThreadSetDefault(void)` |
| 47 | `info` | local / ThreadSetDefault | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `SYSTEM_INFO info;` |
| 64 | `ThreadLock` | function / ThreadLock | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ThreadLock(void)` |
| 79 | `ThreadUnlock` | function / ThreadUnlock | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ThreadUnlock(void)` |
| 94 | `RunThreadsOn` | function / RunThreadsOn | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void RunThreadsOn(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 94 | `workcnt` | parameter / RunThreadsOn | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOn(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 94 | `showpacifier` | parameter / RunThreadsOn | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOn(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 94 | `func` | parameter / RunThreadsOn | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOn(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 96 | `threadid` | local / RunThreadsOn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `DWORD threadid[MAX_THREADS];` |
| 97 | `threadhandle` | local / RunThreadsOn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `HANDLE threadhandle[MAX_THREADS];` |
| 98 | `i` | local / RunThreadsOn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 99 | `start` | local / RunThreadsOn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int start, end;` |
| 99 | `end` | local / RunThreadsOn | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int start, end;` |
| 135 | `GetThreadWork` | function / GetThreadWork | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int GetThreadWork(void)` |
| 137 | `r` | local / GetThreadWork | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int r;` |
| 138 | `f` | local / GetThreadWork | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int f;` |
| 164 | `ThreadWorkerFunction` | function / ThreadWorkerFunction | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ThreadWorkerFunction(int threadnum)` |
| 164 | `threadnum` | parameter / ThreadWorkerFunction | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ThreadWorkerFunction(int threadnum)` |
| 166 | `work` | local / ThreadWorkerFunction | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int work;` |
| 182 | `RunThreadsOnIndividual` | function / RunThreadsOnIndividual | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void RunThreadsOnIndividual(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 182 | `workcnt` | parameter / RunThreadsOnIndividual | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOnIndividual(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 182 | `showpacifier` | parameter / RunThreadsOnIndividual | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOnIndividual(int workcnt, qboolean showpacifier, void (*func)(int))` |
| 182 | `func` | parameter / RunThreadsOnIndividual | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOnIndividual(int workcnt, qboolean showpacifier, void (*func)(int))` |

## common/threads.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 23 | `numthreads` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern	int		numthreads;` |
| 25 | `ThreadSetDefault` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ThreadSetDefault (void);` |
| 26 | `GetThreadWork` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int	GetThreadWork (void);` |
| 27 | `RunThreadsOnIndividual` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void RunThreadsOnIndividual (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 27 | `workcnt` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOnIndividual (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 27 | `showpacifier` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOnIndividual (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 27 | `func` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOnIndividual (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 28 | `RunThreadsOn` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void RunThreadsOn (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 28 | `workcnt` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOn (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 28 | `showpacifier` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOn (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 28 | `func` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RunThreadsOn (int workcnt, qboolean showpacifier, void(*func)(int));` |
| 29 | `ThreadLock` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ThreadLock (void);` |
| 30 | `ThreadUnlock` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ThreadUnlock (void);` |

## universal/com_math.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 32 | `cplane_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} cplane_t;` |
| 26 | `cplane_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct cplane_s {` |
| 27 | `normal` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `vec3_t normal;` |
| 28 | `dist` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float dist;` |
| 29 | `type` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte type;` |
| 30 | `signbits` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte signbits;` |
| 31 | `pad` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte pad[2];` |
| 35 | `ERR_DROP` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ERR_DROP 1` |
| 36 | `Com_Error` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Error( int code, const char *fmt, ... );` |
| 36 | `code` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Error( int code, const char *fmt, ... );` |
| 36 | `fmt` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Error( int code, const char *fmt, ... );` |
| 38 | `M_PI` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define M_PI 3.14159265358979323846f /* matches value in gcc v2 math.h */` |
| 42 | `DEG2RAD` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define DEG2RAD( a ) ( ( (a) * M_PI ) / 180.0F )` |
| 43 | `RAD2DEG` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define RAD2DEG( a ) ( ( (a) * 180.0f ) / M_PI )` |
| 44 | `VectorMA` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define VectorMA( v, s, b, o )     ((o)[0]=(v)[0]+(b)[0]*(s),      (o)[1]=(v)[1]+(b)[1]*(s),      (o)[2]=(v)[2]+(b)[2]*(s))` |
| 51 | `vec3_origin` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `const vec3_t vec3_origin = {0, 0, 0};` |
| 52 | `vec5_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef vec_t vec5_t[5];` |
| 53 | `NUMVERTEXNORMALS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define NUMVERTEXNORMALS 162` |
| 55 | `bytedirs` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec3_t bytedirs[NUMVERTEXNORMALS] =` |
| 220 | `com_randSeed` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int com_randSeed = 0x89ABCDEF;` |
| 222 | `Q_rand` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_rand( int *seed );` |
| 222 | `seed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_rand( int *seed );` |
| 223 | `Q_random` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float Q_random( int *seed );` |
| 223 | `seed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_random( int *seed );` |
| 224 | `AngleNormalize360` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float AngleNormalize360( float angle );` |
| 224 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize360( float angle );` |
| 225 | `AngleNormalize180` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float AngleNormalize180( float angle );` |
| 225 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize180( float angle );` |
| 226 | `RotateAroundDirection` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void RotateAroundDirection( vec3_t axis[3], float yaw );` |
| 226 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateAroundDirection( vec3_t axis[3], float yaw );` |
| 226 | `yaw` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateAroundDirection( vec3_t axis[3], float yaw );` |
| 227 | `NormalizeColor` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float NormalizeColor( const vec3_t in, vec3_t out );` |
| 227 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float NormalizeColor( const vec3_t in, vec3_t out );` |
| 227 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float NormalizeColor( const vec3_t in, vec3_t out );` |
| 228 | `LerpAngle` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float LerpAngle( float from, float to, float frac );` |
| 228 | `from` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float LerpAngle( float from, float to, float frac );` |
| 228 | `to` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float LerpAngle( float from, float to, float frac );` |
| 228 | `frac` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float LerpAngle( float from, float to, float frac );` |
| 229 | `AngleSubtract` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float AngleSubtract( float a1, float a2 );` |
| 229 | `a1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleSubtract( float a1, float a2 );` |
| 229 | `a2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleSubtract( float a1, float a2 );` |
| 230 | `AnglesSubtract` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 );` |
| 230 | `v1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 );` |
| 230 | `v2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 );` |
| 230 | `v3` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 );` |
| 231 | `AngleNormalize360Accurate` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float AngleNormalize360Accurate( float angle );` |
| 231 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize360Accurate( float angle );` |
| 232 | `AngleNormalize180Accurate` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float AngleNormalize180Accurate( float angle );` |
| 232 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize180Accurate( float angle );` |
| 233 | `Q_crandom` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float Q_crandom( int *seed );` |
| 233 | `seed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_crandom( int *seed );` |
| 234 | `Q_log2` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int Q_log2( int val );` |
| 234 | `val` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_log2( int val );` |
| 235 | `Q_acos` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float Q_acos( float c );` |
| 235 | `c` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_acos( float c );` |
| 236 | `ClampChar` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `signed char ClampChar( int i );` |
| 236 | `i` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `signed char ClampChar( int i );` |
| 237 | `ClampShort` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `signed short ClampShort( int i );` |
| 237 | `i` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `signed short ClampShort( int i );` |
| 238 | `RadiusFromBounds` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float RadiusFromBounds( const vec3_t mins, const vec3_t maxs );` |
| 238 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RadiusFromBounds( const vec3_t mins, const vec3_t maxs );` |
| 238 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RadiusFromBounds( const vec3_t mins, const vec3_t maxs );` |
| 239 | `NormalToLatLong` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] );` |
| 239 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] );` |
| 239 | `bytes` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] );` |
| 240 | `MakeNormalVectors` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up );` |
| 240 | `forward` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up );` |
| 240 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up );` |
| 240 | `up` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up );` |
| 241 | `Vec10Copy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Vec10Copy( vec_t *in, vec_t *out );` |
| 241 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vec10Copy( vec_t *in, vec_t *out );` |
| 241 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vec10Copy( vec_t *in, vec_t *out );` |
| 242 | `VectorRotate3x3` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d );` |
| 242 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d );` |
| 242 | `r` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d );` |
| 242 | `d` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d );` |
| 243 | `_VectorLength` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float _VectorLength( const vec3_t v );` |
| 243 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float _VectorLength( const vec3_t v );` |
| 244 | `Q_rint` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t Q_rint (vec_t in);` |
| 244 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t Q_rint (vec_t in);` |
| 245 | `CrossProduct` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 245 | `v1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 245 | `v2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 245 | `cross` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross );` |
| 246 | `_DotProduct` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t _DotProduct (vec3_t v1, vec3_t v2);` |
| 246 | `v1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t _DotProduct (vec3_t v1, vec3_t v2);` |
| 246 | `v2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t _DotProduct (vec3_t v1, vec3_t v2);` |
| 247 | `_VectorSubtract` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 247 | `va` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 247 | `vb` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 247 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out);` |
| 248 | `_VectorAdd` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 248 | `va` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 248 | `vb` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 248 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out);` |
| 249 | `_VectorCopy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorCopy (vec3_t in, vec3_t out);` |
| 249 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorCopy (vec3_t in, vec3_t out);` |
| 249 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorCopy (vec3_t in, vec3_t out);` |
| 250 | `_VectorScale` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 250 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 250 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 250 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out);` |
| 251 | `ColorNormalize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t ColorNormalize( const vec3_t in, vec3_t out );` |
| 251 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t ColorNormalize( const vec3_t in, vec3_t out );` |
| 251 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t ColorNormalize( const vec3_t in, vec3_t out );` |
| 252 | `VectorInverse` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorInverse (vec3_t v);` |
| 252 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorInverse (vec3_t v);` |
| 253 | `ClearBounds` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ClearBounds (vec3_t mins, vec3_t maxs);` |
| 253 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ClearBounds (vec3_t mins, vec3_t maxs);` |
| 253 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ClearBounds (vec3_t mins, vec3_t maxs);` |
| 254 | `AddPointToBounds` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 254 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 254 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 254 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs );` |
| 255 | `ExpandBounds` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs );` |
| 255 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs );` |
| 255 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs );` |
| 255 | `outMins` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs );` |
| 255 | `outMaxs` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs );` |
| 256 | `MatrixMultiply` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]);` |
| 256 | `in1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]);` |
| 256 | `in2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]);` |
| 256 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]);` |
| 257 | `ProjectPointOnPlane` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal );` |
| 257 | `dst` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal );` |
| 257 | `p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal );` |
| 257 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal );` |
| 258 | `PerpendicularVector` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void PerpendicularVector( vec3_t dst, const vec3_t src );` |
| 258 | `dst` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PerpendicularVector( vec3_t dst, const vec3_t src );` |
| 258 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PerpendicularVector( vec3_t dst, const vec3_t src );` |
| 259 | `RotatePointAroundVector` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 259 | `dst` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 259 | `dir` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 259 | `point` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 260 | `degrees` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float degrees );` |
| 261 | `_Vector5Add` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out);` |
| 261 | `va` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out);` |
| 261 | `vb` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out);` |
| 261 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out);` |
| 262 | `_Vector5Scale` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out);` |
| 262 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out);` |
| 262 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out);` |
| 262 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out);` |
| 263 | `SinCos` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `__inline void SinCos( float radians, float *sinOut, float *cosOut );` |
| 263 | `radians` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline void SinCos( float radians, float *sinOut, float *cosOut );` |
| 263 | `sinOut` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos( float radians, float *sinOut, float *cosOut );` |
| 263 | `cosOut` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos( float radians, float *sinOut, float *cosOut );` |
| 264 | `SinCos_double` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut );` |
| 264 | `radians` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut );` |
| 264 | `sinOut` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut );` |
| 264 | `cosOut` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut );` |
| 265 | `VectorCompareEpsilon` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 );` |
| 265 | `p1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 );` |
| 265 | `p2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 );` |
| 266 | `YawVectors` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void YawVectors( float yaw, vec3_t forward, vec3_t right );` |
| 266 | `yaw` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawVectors( float yaw, vec3_t forward, vec3_t right );` |
| 266 | `forward` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawVectors( float yaw, vec3_t forward, vec3_t right );` |
| 266 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawVectors( float yaw, vec3_t forward, vec3_t right );` |
| 267 | `RotateVector2D` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void RotateVector2D( vec3_t v, float degrees );` |
| 267 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateVector2D( vec3_t v, float degrees );` |
| 267 | `degrees` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateVector2D( vec3_t v, float degrees );` |
| 268 | `VectorPolar` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorPolar( vec3_t out, float radius, float angle );` |
| 268 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorPolar( vec3_t out, float radius, float angle );` |
| 268 | `radius` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorPolar( vec3_t out, float radius, float angle );` |
| 268 | `angle` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorPolar( vec3_t out, float radius, float angle );` |
| 269 | `RollToQuaternion` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void RollToQuaternion( float degrees, vec4_t q );` |
| 269 | `degrees` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RollToQuaternion( float degrees, vec4_t q );` |
| 269 | `q` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RollToQuaternion( float degrees, vec4_t q );` |
| 270 | `gunrandom` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void gunrandom( float *outX, float *outY );` |
| 270 | `outX` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void gunrandom( float *outX, float *outY );` |
| 270 | `outY` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void gunrandom( float *outX, float *outY );` |
| 271 | `MatrixMultiplyEquals` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixMultiplyEquals( const float left[3][3], float inout[3][3] );` |
| 271 | `left` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiplyEquals( const float left[3][3], float inout[3][3] );` |
| 271 | `inout` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiplyEquals( const float left[3][3], float inout[3][3] );` |
| 272 | `vectopitch` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float vectopitch( const vec3_t vec );` |
| 272 | `vec` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectopitch( const vec3_t vec );` |
| 273 | `vectosignedpitch` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float vectosignedpitch( const vec3_t vec );` |
| 273 | `vec` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectosignedpitch( const vec3_t vec );` |
| 274 | `vectosignedangles` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void vectosignedangles( const vec3_t value, vec3_t angles );` |
| 274 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectosignedangles( const vec3_t value, vec3_t angles );` |
| 274 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectosignedangles( const vec3_t value, vec3_t angles );` |
| 275 | `vectoangles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void vectoangles( const vec3_t value, vec3_t angles );` |
| 275 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectoangles( const vec3_t value, vec3_t angles );` |
| 275 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectoangles( const vec3_t value, vec3_t angles );` |
| 276 | `VectorNormalize2D` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float VectorNormalize2D( float v[2] );` |
| 276 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2D( float v[2] );` |
| 277 | `VectorNormalize4D` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float VectorNormalize4D( vec4_t v );` |
| 277 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize4D( vec4_t v );` |
| 278 | `VectorNormalize2` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float VectorNormalize2( const vec3_t v, vec3_t out );` |
| 278 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2( const vec3_t v, vec3_t out );` |
| 278 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2( const vec3_t v, vec3_t out );` |
| 279 | `RoundToPrecision` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float RoundToPrecision( float value, int places );` |
| 279 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RoundToPrecision( float value, int places );` |
| 279 | `places` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RoundToPrecision( float value, int places );` |
| 280 | `QuatEigenTrace` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float QuatEigenTrace( const vec4_t q );` |
| 280 | `q` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float QuatEigenTrace( const vec4_t q );` |
| 281 | `QuatInverse` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void QuatInverse( const vec4_t in, vec4_t out );` |
| 281 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatInverse( const vec4_t in, vec4_t out );` |
| 281 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatInverse( const vec4_t in, vec4_t out );` |
| 282 | `ConvertQuatToMat` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void ConvertQuatToMat( float quatAndMatrix[9] );` |
| 282 | `quatAndMatrix` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ConvertQuatToMat( float quatAndMatrix[9] );` |
| 283 | `MatrixTransposeTransformVector` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out );` |
| 283 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out );` |
| 283 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out );` |
| 283 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out );` |
| 284 | `MatrixTranspose` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixTranspose( const float in[3][3], float out[3][3] );` |
| 284 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTranspose( const float in[3][3], float out[3][3] );` |
| 284 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTranspose( const float in[3][3], float out[3][3] );` |
| 285 | `MatrixInverseOrthogonal43` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixInverseOrthogonal43( const float in[4][3], float out[4][3] );` |
| 285 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverseOrthogonal43( const float in[4][3], float out[4][3] );` |
| 285 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverseOrthogonal43( const float in[4][3], float out[4][3] );` |
| 286 | `VectorNormalize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t VectorNormalize( vec3_t v );` |
| 286 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t VectorNormalize( vec3_t v );` |
| 287 | `VectorRotateAnglesAroundPoint` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 287 | `point` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 287 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 288 | `pivot` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t pivot, vec3_t out );` |
| 288 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t pivot, vec3_t out );` |
| 289 | `PlaneFromPoints` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 289 | `plane` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 289 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 289 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 289 | `c` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c );` |
| 290 | `VectorDistance` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float VectorDistance( const vec3_t p1, const vec3_t p2 );` |
| 290 | `p1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance( const vec3_t p1, const vec3_t p2 );` |
| 290 | `p2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance( const vec3_t p1, const vec3_t p2 );` |
| 291 | `VectorDistanceSquared` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float VectorDistanceSquared( const vec3_t p1, const vec3_t p2 );` |
| 291 | `p1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared( const vec3_t p1, const vec3_t p2 );` |
| 291 | `p2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared( const vec3_t p1, const vec3_t p2 );` |
| 292 | `VectorDistance2D` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float VectorDistance2D( const vec3_t p1, const vec3_t p2 );` |
| 292 | `p1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance2D( const vec3_t p1, const vec3_t p2 );` |
| 292 | `p2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance2D( const vec3_t p1, const vec3_t p2 );` |
| 293 | `VectorDistanceSquared2D` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float VectorDistanceSquared2D( const vec3_t p1, const vec3_t p2 );` |
| 293 | `p1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared2D( const vec3_t p1, const vec3_t p2 );` |
| 293 | `p2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared2D( const vec3_t p1, const vec3_t p2 );` |
| 294 | `MatrixMultiply34` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] );` |
| 294 | `left` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] );` |
| 294 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] );` |
| 294 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] );` |
| 295 | `MatrixMultiply43` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] );` |
| 295 | `left` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] );` |
| 295 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] );` |
| 295 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] );` |
| 296 | `DObjSkelMatrixMultiply43` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] );` |
| 296 | `left` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] );` |
| 296 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] );` |
| 296 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] );` |
| 297 | `DObjSkel2MatrixMultiply43` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] );` |
| 297 | `left` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] );` |
| 297 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] );` |
| 297 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] );` |
| 298 | `MatrixTransformVector33` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out );` |
| 298 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out );` |
| 298 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out );` |
| 298 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out );` |
| 299 | `MatrixTransformVector43` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out );` |
| 299 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out );` |
| 299 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out );` |
| 299 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out );` |
| 300 | `MatrixTransformVector44` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out );` |
| 300 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out );` |
| 300 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out );` |
| 300 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out );` |
| 301 | `VectorSnap` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorSnap( vec3_t v );` |
| 301 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorSnap( vec3_t v );` |
| 302 | `NormalFromPoints` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void NormalFromPoints( const vec3_t a, const vec3_t origin,` |
| 302 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalFromPoints( const vec3_t a, const vec3_t origin,` |
| 302 | `origin` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalFromPoints( const vec3_t a, const vec3_t origin,` |
| 303 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t b, vec3_t normal );` |
| 303 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t b, vec3_t normal );` |
| 304 | `ProjectPointOntoVector` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 304 | `point` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 304 | `origin` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 305 | `linePoint` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `const vec3_t linePoint, vec3_t out );` |
| 305 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t linePoint, vec3_t out );` |
| 306 | `AxisClear` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AxisClear( vec3_t axis[3] );` |
| 306 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisClear( vec3_t axis[3] );` |
| 307 | `QuatRatioEigenTrace` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float QuatRatioEigenTrace( const vec4_t a, const vec4_t b );` |
| 307 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float QuatRatioEigenTrace( const vec4_t a, const vec4_t b );` |
| 307 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float QuatRatioEigenTrace( const vec4_t a, const vec4_t b );` |
| 308 | `AngleEigenTrace` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float AngleEigenTrace( float degrees );` |
| 308 | `degrees` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleEigenTrace( float degrees );` |
| 309 | `DirToByte` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `byte DirToByte( vec3_t dir );` |
| 309 | `dir` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `byte DirToByte( vec3_t dir );` |
| 310 | `ByteToDir` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ByteToDir( int b, vec3_t dir );` |
| 310 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ByteToDir( int b, vec3_t dir );` |
| 310 | `dir` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ByteToDir( int b, vec3_t dir );` |
| 311 | `SetPlaneSignbits` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void SetPlaneSignbits( cplane_t *out );` |
| 311 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SetPlaneSignbits( cplane_t *out );` |
| 312 | `AnglesToAxis` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AnglesToAxis( const vec3_t angles, vec3_t axis[3] );` |
| 312 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesToAxis( const vec3_t angles, vec3_t axis[3] );` |
| 312 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesToAxis( const vec3_t angles, vec3_t axis[3] );` |
| 313 | `YawToAxis` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void YawToAxis( float yaw, vec3_t axis[3] );` |
| 313 | `yaw` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawToAxis( float yaw, vec3_t axis[3] );` |
| 313 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawToAxis( float yaw, vec3_t axis[3] );` |
| 314 | `PitchForYawOnNormal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float PitchForYawOnNormal( float yaw, const vec3_t normal );` |
| 314 | `yaw` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float PitchForYawOnNormal( float yaw, const vec3_t normal );` |
| 314 | `normal` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float PitchForYawOnNormal( float yaw, const vec3_t normal );` |
| 315 | `Com_SRand` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Com_SRand( int seed );` |
| 315 | `seed` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_SRand( int seed );` |
| 316 | `Com_RandFloatRange` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float Com_RandFloatRange( float lo, float hi );` |
| 316 | `lo` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_RandFloatRange( float lo, float hi );` |
| 316 | `hi` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_RandFloatRange( float lo, float hi );` |
| 317 | `Com_RandIntRange` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int Com_RandIntRange( int lo, int hi );` |
| 317 | `lo` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_RandIntRange( int lo, int hi );` |
| 317 | `hi` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_RandIntRange( int lo, int hi );` |
| 318 | `BoxDistSqrdExceeds` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd );` |
| 318 | `absmin` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd );` |
| 318 | `absmax` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd );` |
| 318 | `origin` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd );` |
| 318 | `distSqrd` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd );` |
| 319 | `SinCosWave` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float SinCosWave( float freqA, float freqB, float t );` |
| 319 | `freqA` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `float SinCosWave( float freqA, float freqB, float t );` |
| 319 | `freqB` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `float SinCosWave( float freqA, float freqB, float t );` |
| 319 | `t` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float SinCosWave( float freqA, float freqB, float t );` |
| 320 | `Vector4Scale` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out );` |
| 320 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out );` |
| 320 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out );` |
| 320 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out );` |
| 321 | `_VectorMA` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out );` |
| 321 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out );` |
| 321 | `scale` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out );` |
| 321 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out );` |
| 321 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out );` |
| 322 | `VectorMax` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float VectorMax( const vec3_t v );` |
| 322 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorMax( const vec3_t v );` |
| 323 | `QuatMultiply` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out );` |
| 323 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out );` |
| 323 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out );` |
| 323 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out );` |
| 324 | `MatrixInverse44` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixInverse44( const float in[16], float out[16] );` |
| 324 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse44( const float in[16], float out[16] );` |
| 324 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse44( const float in[16], float out[16] );` |
| 325 | `MatrixTransformVector43Equals` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixTransformVector43Equals( vec3_t v, const float matrix[4][3] );` |
| 325 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43Equals( vec3_t v, const float matrix[4][3] );` |
| 325 | `matrix` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43Equals( vec3_t v, const float matrix[4][3] );` |
| 326 | `_Vector53Copy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void _Vector53Copy( const vec3_t in, vec3_t out );` |
| 326 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector53Copy( const vec3_t in, vec3_t out );` |
| 326 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector53Copy( const vec3_t in, vec3_t out );` |
| 327 | `VectorRotate` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out );` |
| 327 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out );` |
| 327 | `matrix` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out );` |
| 327 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out );` |
| 328 | `AxisCopy` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AxisCopy( vec3_t in[3], vec3_t out[3] );` |
| 328 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisCopy( vec3_t in[3], vec3_t out[3] );` |
| 328 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisCopy( vec3_t in[3], vec3_t out[3] );` |
| 329 | `AngleDelta` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float AngleDelta( float angle1, float angle2 );` |
| 329 | `angle1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleDelta( float angle1, float angle2 );` |
| 329 | `angle2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleDelta( float angle1, float angle2 );` |
| 330 | `vectoyaw` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float vectoyaw( const vec3_t vec );` |
| 330 | `vec` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectoyaw( const vec3_t vec );` |
| 331 | `vectosignedyaw` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float vectosignedyaw( const vec3_t vec );` |
| 331 | `vec` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectosignedyaw( const vec3_t vec );` |
| 332 | `ColorBytes3` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `unsigned ColorBytes3( float r, float g, float b );` |
| 332 | `r` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes3( float r, float g, float b );` |
| 332 | `g` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes3( float r, float g, float b );` |
| 332 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes3( float r, float g, float b );` |
| 333 | `ColorBytes4` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `unsigned ColorBytes4( float r, float g, float b, float a );` |
| 333 | `r` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a );` |
| 333 | `g` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a );` |
| 333 | `b` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a );` |
| 333 | `a` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a );` |
| 334 | `RotationToYaw` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `float RotationToYaw( const float v[2] );` |
| 334 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RotationToYaw( const float v[2] );` |
| 335 | `VectorNormalizeFast` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void VectorNormalizeFast( vec3_t v );` |
| 335 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorNormalizeFast( vec3_t v );` |
| 336 | `Perp2D` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Perp2D( const vec3_t in, vec3_t out );` |
| 336 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Perp2D( const vec3_t in, vec3_t out );` |
| 336 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Perp2D( const vec3_t in, vec3_t out );` |
| 337 | `AngleVectors` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 337 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 337 | `forward` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 337 | `right` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 337 | `up` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up );` |
| 338 | `MatrixInverse` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void MatrixInverse( const float in[9], float out[9] );` |
| 338 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse( const float in[9], float out[9] );` |
| 338 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse( const float in[9], float out[9] );` |
| 339 | `AxisToAngles` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void AxisToAngles( const vec3_t axis[3], vec3_t angles );` |
| 339 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToAngles( const vec3_t axis[3], vec3_t angles );` |
| 339 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToAngles( const vec3_t axis[3], vec3_t angles );` |
| 340 | `Axis4ToAngles` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Axis4ToAngles( const float matrix[3][4], vec3_t angles );` |
| 340 | `matrix` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Axis4ToAngles( const float matrix[3][4], vec3_t angles );` |
| 340 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Axis4ToAngles( const float matrix[3][4], vec3_t angles );` |
| 341 | `AxisToSignedAngles` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void AxisToSignedAngles( const vec3_t axis[3], vec3_t angles );` |
| 341 | `axis` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToSignedAngles( const vec3_t axis[3], vec3_t angles );` |
| 341 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToSignedAngles( const vec3_t axis[3], vec3_t angles );` |
| 342 | `VectorRotateAngles` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 342 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 342 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 342 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 343 | `BoxOnPlaneSide` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p );` |
| 343 | `emins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p );` |
| 343 | `emaxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p );` |
| 343 | `p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p );` |
| 343 | `cplane_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p );` |
| 350 | `Q_rand` | function / Q_rand | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_rand( int *seed ) {` |
| 350 | `seed` | parameter / Q_rand | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_rand( int *seed ) {` |
| 360 | `Q_random` | function / Q_random | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Q_random( int *seed ) {` |
| 360 | `seed` | parameter / Q_random | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_random( int *seed ) {` |
| 369 | `Q_crandom` | function / Q_crandom | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Q_crandom( int *seed ) {` |
| 369 | `seed` | parameter / Q_crandom | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_crandom( int *seed ) {` |
| 378 | `Q_log2` | function / Q_log2 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Q_log2( int val ) {` |
| 378 | `val` | parameter / Q_log2 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Q_log2( int val ) {` |
| 379 | `answer` | local / Q_log2 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int answer;` |
| 402 | `Q_acos` | function / Q_acos | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Q_acos( float c ) {` |
| 402 | `c` | parameter / Q_acos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Q_acos( float c ) {` |
| 403 | `angle` | local / Q_acos | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle;` |
| 420 | `ClampChar` | function / ClampChar | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `signed char ClampChar( int i ) {` |
| 420 | `i` | parameter / ClampChar | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `signed char ClampChar( int i ) {` |
| 436 | `__fsqrt` | function / __fsqrt | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `__inline float __fsqrt( float number ) {` |
| 436 | `number` | parameter / __fsqrt | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline float __fsqrt( float number ) {` |
| 437 | `i` | local / __fsqrt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long i;` |
| 438 | `x2` | local / __fsqrt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float x2, y;` |
| 438 | `y` | local / __fsqrt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float x2, y;` |
| 456 | `ClampShort` | function / ClampShort | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `signed short ClampShort( int i ) {` |
| 456 | `i` | parameter / ClampShort | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `signed short ClampShort( int i ) {` |
| 471 | `DirToByte` | function / DirToByte | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `byte DirToByte( vec3_t dir ) {` |
| 471 | `dir` | parameter / DirToByte | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `byte DirToByte( vec3_t dir ) {` |
| 472 | `i` | local / DirToByte | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte i, best;` |
| 472 | `best` | local / DirToByte | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte i, best;` |
| 473 | `d` | local / DirToByte | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float d, bestd;` |
| 473 | `bestd` | local / DirToByte | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float d, bestd;` |
| 497 | `ByteToDir` | function / ByteToDir | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ByteToDir( int b, vec3_t dir ) {` |
| 497 | `b` | parameter / ByteToDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ByteToDir( int b, vec3_t dir ) {` |
| 497 | `dir` | parameter / ByteToDir | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ByteToDir( int b, vec3_t dir ) {` |
| 510 | `_DotProduct` | function / _DotProduct | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `vec_t _DotProduct (vec3_t v1, vec3_t v2)` |
| 510 | `v1` | parameter / _DotProduct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t _DotProduct (vec3_t v1, vec3_t v2)` |
| 510 | `v2` | parameter / _DotProduct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t _DotProduct (vec3_t v1, vec3_t v2)` |
| 520 | `_VectorSubtract` | function / _VectorSubtract | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out)` |
| 520 | `va` | parameter / _VectorSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out)` |
| 520 | `vb` | parameter / _VectorSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out)` |
| 520 | `out` | parameter / _VectorSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorSubtract (vec3_t va, vec3_t vb, vec3_t out)` |
| 532 | `_VectorAdd` | function / _VectorAdd | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out)` |
| 532 | `va` | parameter / _VectorAdd | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out)` |
| 532 | `vb` | parameter / _VectorAdd | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out)` |
| 532 | `out` | parameter / _VectorAdd | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorAdd (vec3_t va, vec3_t vb, vec3_t out)` |
| 544 | `SinCos` | function / SinCos | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `__inline void SinCos( float radians, float *sinOut, float *cosOut ) {` |
| 544 | `radians` | parameter / SinCos | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline void SinCos( float radians, float *sinOut, float *cosOut ) {` |
| 544 | `sinOut` | parameter / SinCos | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos( float radians, float *sinOut, float *cosOut ) {` |
| 544 | `cosOut` | parameter / SinCos | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos( float radians, float *sinOut, float *cosOut ) {` |
| 564 | `_VectorCopy` | function / _VectorCopy | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _VectorCopy (vec3_t in, vec3_t out)` |
| 564 | `in` | parameter / _VectorCopy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorCopy (vec3_t in, vec3_t out)` |
| 564 | `out` | parameter / _VectorCopy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorCopy (vec3_t in, vec3_t out)` |
| 576 | `SinCos_double` | function / SinCos_double | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut ) {` |
| 576 | `radians` | parameter / SinCos_double | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut ) {` |
| 576 | `sinOut` | parameter / SinCos_double | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut ) {` |
| 576 | `cosOut` | parameter / SinCos_double | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `__inline void SinCos_double( double radians, double *sinOut, double *cosOut ) {` |
| 596 | `_VectorScale` | function / _VectorScale | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out)` |
| 596 | `v` | parameter / _VectorScale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out)` |
| 596 | `scale` | parameter / _VectorScale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out)` |
| 596 | `out` | parameter / _VectorScale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorScale (vec3_t v, vec_t scale, vec3_t out)` |
| 608 | `_VectorMA` | function / _VectorMA | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out ) {` |
| 608 | `a` | parameter / _VectorMA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out ) {` |
| 608 | `scale` | parameter / _VectorMA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out ) {` |
| 608 | `b` | parameter / _VectorMA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out ) {` |
| 608 | `out` | parameter / _VectorMA | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _VectorMA( const vec3_t a, float scale, const vec3_t b, vec3_t out ) {` |
| 619 | `VectorCompareEpsilon` | function / VectorCompareEpsilon | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 ) {` |
| 619 | `p1` | parameter / VectorCompareEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 ) {` |
| 619 | `p2` | parameter / VectorCompareEpsilon | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 ) {` |
| 620 | `i` | local / VectorCompareEpsilon | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 632 | `_VectorLength` | function / _VectorLength | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float _VectorLength( const vec3_t v ) {` |
| 632 | `v` | parameter / _VectorLength | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float _VectorLength( const vec3_t v ) {` |
| 641 | `VectorDistance` | function / VectorDistance | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorDistance( const vec3_t p1, const vec3_t p2 ) {` |
| 641 | `p1` | parameter / VectorDistance | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance( const vec3_t p1, const vec3_t p2 ) {` |
| 641 | `p2` | parameter / VectorDistance | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance( const vec3_t p1, const vec3_t p2 ) {` |
| 642 | `delta` | local / VectorDistance | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t delta;` |
| 653 | `VectorDistanceSquared` | function / VectorDistanceSquared | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorDistanceSquared( const vec3_t p1, const vec3_t p2 ) {` |
| 653 | `p1` | parameter / VectorDistanceSquared | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared( const vec3_t p1, const vec3_t p2 ) {` |
| 653 | `p2` | parameter / VectorDistanceSquared | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared( const vec3_t p1, const vec3_t p2 ) {` |
| 654 | `delta` | local / VectorDistanceSquared | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t delta;` |
| 665 | `VectorDistance2D` | function / VectorDistance2D | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorDistance2D( const vec3_t p1, const vec3_t p2 ) {` |
| 665 | `p1` | parameter / VectorDistance2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance2D( const vec3_t p1, const vec3_t p2 ) {` |
| 665 | `p2` | parameter / VectorDistance2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistance2D( const vec3_t p1, const vec3_t p2 ) {` |
| 666 | `delta` | local / VectorDistance2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float delta[2];` |
| 678 | `VectorDistanceSquared2D` | function / VectorDistanceSquared2D | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorDistanceSquared2D( const vec3_t p1, const vec3_t p2 ) {` |
| 678 | `p1` | parameter / VectorDistanceSquared2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared2D( const vec3_t p1, const vec3_t p2 ) {` |
| 678 | `p2` | parameter / VectorDistanceSquared2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorDistanceSquared2D( const vec3_t p1, const vec3_t p2 ) {` |
| 679 | `delta` | local / VectorDistanceSquared2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float delta[2];` |
| 691 | `CrossProduct` | function / CrossProduct | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross ) {` |
| 691 | `v1` | parameter / CrossProduct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross ) {` |
| 691 | `v2` | parameter / CrossProduct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross ) {` |
| 691 | `cross` | parameter / CrossProduct | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void CrossProduct( const vec3_t v1, const vec3_t v2, vec3_t cross ) {` |
| 702 | `Perp2D` | function / Perp2D | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Perp2D( const vec3_t in, vec3_t out ) {` |
| 702 | `in` | parameter / Perp2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Perp2D( const vec3_t in, vec3_t out ) {` |
| 702 | `out` | parameter / Perp2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Perp2D( const vec3_t in, vec3_t out ) {` |
| 713 | `VectorNormalize` | function / VectorNormalize | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `vec_t VectorNormalize( vec3_t v ) {` |
| 713 | `v` | parameter / VectorNormalize | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t VectorNormalize( vec3_t v ) {` |
| 714 | `length` | local / VectorNormalize | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 714 | `ilength` | local / VectorNormalize | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 733 | `VectorNormalize2D` | function / VectorNormalize2D | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorNormalize2D( float v[2] ) {` |
| 733 | `v` | parameter / VectorNormalize2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2D( float v[2] ) {` |
| 734 | `length` | local / VectorNormalize2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 734 | `ilength` | local / VectorNormalize2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 751 | `VectorNormalize4D` | function / VectorNormalize4D | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorNormalize4D( vec4_t v ) {` |
| 751 | `v` | parameter / VectorNormalize4D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize4D( vec4_t v ) {` |
| 752 | `length` | local / VectorNormalize4D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 752 | `ilength` | local / VectorNormalize4D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 771 | `VectorNormalizeFast` | function / VectorNormalizeFast | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorNormalizeFast( vec3_t v ) {` |
| 771 | `v` | parameter / VectorNormalizeFast | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorNormalizeFast( vec3_t v ) {` |
| 772 | `ilength` | local / VectorNormalizeFast | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float ilength;` |
| 785 | `VectorNormalize2` | function / VectorNormalize2 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorNormalize2( const vec3_t v, vec3_t out ) {` |
| 785 | `v` | parameter / VectorNormalize2 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2( const vec3_t v, vec3_t out ) {` |
| 785 | `out` | parameter / VectorNormalize2 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2( const vec3_t v, vec3_t out ) {` |
| 786 | `length` | local / VectorNormalize2 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 786 | `ilength` | local / VectorNormalize2 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float length, ilength;` |
| 804 | `VectorInverse` | function / VectorInverse | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorInverse (vec3_t v)` |
| 804 | `v` | parameter / VectorInverse | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorInverse (vec3_t v)` |
| 816 | `Vector4Scale` | function / Vector4Scale | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out ) {` |
| 816 | `in` | parameter / Vector4Scale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out ) {` |
| 816 | `scale` | parameter / Vector4Scale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out ) {` |
| 816 | `out` | parameter / Vector4Scale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vector4Scale( const vec4_t in, float scale, vec4_t out ) {` |
| 828 | `VectorMax` | function / VectorMax | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float VectorMax( const vec3_t v ) {` |
| 828 | `v` | parameter / VectorMax | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorMax( const vec3_t v ) {` |
| 829 | `m` | local / VectorMax | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float m;` |
| 840 | `VectorRotate` | function / VectorRotate | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out ) {` |
| 840 | `in` | parameter / VectorRotate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out ) {` |
| 840 | `matrix` | parameter / VectorRotate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out ) {` |
| 840 | `out` | parameter / VectorRotate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate( vec3_t in, vec3_t matrix[3], vec3_t out ) {` |
| 854 | `MakeNormalVectors` | function / MakeNormalVectors | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up ) {` |
| 854 | `forward` | parameter / MakeNormalVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up ) {` |
| 854 | `right` | parameter / MakeNormalVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up ) {` |
| 854 | `up` | parameter / MakeNormalVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MakeNormalVectors( const vec3_t forward, vec3_t right, vec3_t up ) {` |
| 855 | `d` | local / MakeNormalVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float d;` |
| 871 | `vectoyaw` | function / vectoyaw | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float vectoyaw( const vec3_t vec ) {` |
| 871 | `vec` | parameter / vectoyaw | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectoyaw( const vec3_t vec ) {` |
| 872 | `yaw` | local / vectoyaw | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float yaw;` |
| 890 | `vectosignedyaw` | function / vectosignedyaw | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float vectosignedyaw( const vec3_t vec ) {` |
| 890 | `vec` | parameter / vectosignedyaw | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectosignedyaw( const vec3_t vec ) {` |
| 891 | `yaw` | local / vectosignedyaw | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float yaw;` |
| 906 | `vectopitch` | function / vectopitch | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float vectopitch( const vec3_t vec ) {` |
| 906 | `vec` | parameter / vectopitch | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectopitch( const vec3_t vec ) {` |
| 907 | `forward` | local / vectopitch | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, pitch;` |
| 907 | `pitch` | local / vectopitch | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, pitch;` |
| 930 | `vectosignedpitch` | function / vectosignedpitch | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float vectosignedpitch( const vec3_t vec ) {` |
| 930 | `vec` | parameter / vectosignedpitch | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float vectosignedpitch( const vec3_t vec ) {` |
| 931 | `forward` | local / vectosignedpitch | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, pitch;` |
| 931 | `pitch` | local / vectosignedpitch | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, pitch;` |
| 951 | `vectoangles` | function / vectoangles | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void vectoangles( const vec3_t value, vec3_t angles ) {` |
| 951 | `value` | parameter / vectoangles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectoangles( const vec3_t value, vec3_t angles ) {` |
| 951 | `angles` | parameter / vectoangles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectoangles( const vec3_t value, vec3_t angles ) {` |
| 952 | `forward` | local / vectoangles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, yaw, pitch;` |
| 952 | `yaw` | local / vectoangles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, yaw, pitch;` |
| 952 | `pitch` | local / vectoangles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, yaw, pitch;` |
| 978 | `vectosignedangles` | function / vectosignedangles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void vectosignedangles( const vec3_t value, vec3_t angles ) {` |
| 978 | `value` | parameter / vectosignedangles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectosignedangles( const vec3_t value, vec3_t angles ) {` |
| 978 | `angles` | parameter / vectosignedangles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void vectosignedangles( const vec3_t value, vec3_t angles ) {` |
| 979 | `forward` | local / vectosignedangles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, yaw, pitch;` |
| 979 | `yaw` | local / vectosignedangles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, yaw, pitch;` |
| 979 | `pitch` | local / vectosignedangles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float forward, yaw, pitch;` |
| 999 | `AngleVectors` | function / AngleVectors | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up ) {` |
| 999 | `angles` | parameter / AngleVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up ) {` |
| 999 | `forward` | parameter / AngleVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up ) {` |
| 999 | `right` | parameter / AngleVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up ) {` |
| 999 | `up` | parameter / AngleVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AngleVectors( const vec3_t angles, vec3_t forward, vec3_t right, vec3_t up ) {` |
| 1000 | `angle` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle;` |
| 1001 | `sr` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float sr, sp, sy, cr, cp, cy;` |
| 1001 | `sp` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float sr, sp, sy, cr, cp, cy;` |
| 1001 | `sy` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float sr, sp, sy, cr, cp, cy;` |
| 1001 | `cr` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float sr, sp, sy, cr, cp, cy;` |
| 1001 | `cp` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float sr, sp, sy, cr, cp, cy;` |
| 1001 | `cy` | local / AngleVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float sr, sp, sy, cr, cp, cy;` |
| 1040 | `YawVectors` | function / YawVectors | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void YawVectors( float yaw, vec3_t forward, vec3_t right ) {` |
| 1040 | `yaw` | parameter / YawVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawVectors( float yaw, vec3_t forward, vec3_t right ) {` |
| 1040 | `forward` | parameter / YawVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawVectors( float yaw, vec3_t forward, vec3_t right ) {` |
| 1040 | `right` | parameter / YawVectors | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawVectors( float yaw, vec3_t forward, vec3_t right ) {` |
| 1041 | `angle` | local / YawVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c;` |
| 1041 | `s` | local / YawVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c;` |
| 1041 | `c` | local / YawVectors | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c;` |
| 1061 | `NormalFromPoints` | function / NormalFromPoints | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void NormalFromPoints( const vec3_t a, const vec3_t origin,` |
| 1061 | `a` | parameter / NormalFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalFromPoints( const vec3_t a, const vec3_t origin,` |
| 1061 | `origin` | parameter / NormalFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalFromPoints( const vec3_t a, const vec3_t origin,` |
| 1062 | `b` | parameter / NormalFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t b, vec3_t normal ) {` |
| 1062 | `normal` | parameter / NormalFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t b, vec3_t normal ) {` |
| 1063 | `v1` | local / NormalFromPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v1, v2;` |
| 1063 | `v2` | local / NormalFromPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v1, v2;` |
| 1078 | `ProjectPointOntoVector` | function / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 1078 | `point` | parameter / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 1078 | `origin` | parameter / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 1079 | `linePoint` | parameter / ProjectPointOntoVector | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `const vec3_t linePoint, vec3_t out ) {` |
| 1079 | `out` | parameter / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t linePoint, vec3_t out ) {` |
| 1080 | `rel` | local / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t rel, dir;` |
| 1080 | `dir` | local / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t rel, dir;` |
| 1081 | `d` | local / ProjectPointOntoVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float d;` |
| 1095 | `MatrixMultiply` | function / MatrixMultiply | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]) {` |
| 1095 | `in1` | parameter / MatrixMultiply | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]) {` |
| 1095 | `in2` | parameter / MatrixMultiply | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]) {` |
| 1095 | `out` | parameter / MatrixMultiply | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply(float in1[3][3], float in2[3][3], float out[3][3]) {` |
| 1121 | `MatrixMultiplyEquals` | function / MatrixMultiplyEquals | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixMultiplyEquals( const float left[3][3], float inout[3][3] ) {` |
| 1121 | `left` | parameter / MatrixMultiplyEquals | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiplyEquals( const float left[3][3], float inout[3][3] ) {` |
| 1121 | `inout` | parameter / MatrixMultiplyEquals | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiplyEquals( const float left[3][3], float inout[3][3] ) {` |
| 1122 | `rows` | local / MatrixMultiplyEquals | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t rows[2];` |
| 1151 | `MatrixMultiply34` | function / MatrixMultiply34 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] ) {` |
| 1151 | `left` | parameter / MatrixMultiply34 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] ) {` |
| 1151 | `right` | parameter / MatrixMultiply34 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] ) {` |
| 1151 | `out` | parameter / MatrixMultiply34 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply34( const float left[3][4], const float right[3][4], float out[3][4] ) {` |
| 1183 | `MatrixMultiply43` | function / MatrixMultiply43 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] ) {` |
| 1183 | `left` | parameter / MatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] ) {` |
| 1183 | `right` | parameter / MatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] ) {` |
| 1183 | `out` | parameter / MatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixMultiply43( const float left[4][3], const float right[4][3], float out[4][3] ) {` |
| 1215 | `DObjSkelMatrixMultiply43` | function / DObjSkelMatrixMultiply43 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] ) {` |
| 1215 | `left` | parameter / DObjSkelMatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] ) {` |
| 1215 | `right` | parameter / DObjSkelMatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] ) {` |
| 1215 | `out` | parameter / DObjSkelMatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkelMatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][3] ) {` |
| 1247 | `DObjSkel2MatrixMultiply43` | function / DObjSkel2MatrixMultiply43 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] ) {` |
| 1247 | `left` | parameter / DObjSkel2MatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] ) {` |
| 1247 | `right` | parameter / DObjSkel2MatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] ) {` |
| 1247 | `out` | parameter / DObjSkel2MatrixMultiply43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void DObjSkel2MatrixMultiply43( const float left[4][4], const float right[4][3], float out[4][4] ) {` |
| 1283 | `MatrixTranspose` | function / MatrixTranspose | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixTranspose( const float in[3][3], float out[3][3] ) {` |
| 1283 | `in` | parameter / MatrixTranspose | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTranspose( const float in[3][3], float out[3][3] ) {` |
| 1283 | `out` | parameter / MatrixTranspose | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTranspose( const float in[3][3], float out[3][3] ) {` |
| 1300 | `MatrixInverse` | function / MatrixInverse | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixInverse( const float in[9], float out[9] ) {` |
| 1300 | `in` | parameter / MatrixInverse | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse( const float in[9], float out[9] ) {` |
| 1300 | `out` | parameter / MatrixInverse | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse( const float in[9], float out[9] ) {` |
| 1301 | `determinant` | local / MatrixInverse | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float determinant, inverseDeterminant;` |
| 1301 | `inverseDeterminant` | local / MatrixInverse | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float determinant, inverseDeterminant;` |
| 1324 | `MatrixInverse44` | function / MatrixInverse44 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixInverse44( const float in[16], float out[16] ) {` |
| 1324 | `in` | parameter / MatrixInverse44 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse44( const float in[16], float out[16] ) {` |
| 1324 | `out` | parameter / MatrixInverse44 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverse44( const float in[16], float out[16] ) {` |
| 1325 | `pair` | local / MatrixInverse44 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float pair[12];` |
| 1326 | `transposed` | local / MatrixInverse44 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float transposed[16];` |
| 1327 | `determinant` | local / MatrixInverse44 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float determinant;` |
| 1328 | `i` | local / MatrixInverse44 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1410 | `VectorRotate3x3` | function / VectorRotate3x3 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d )` |
| 1410 | `v` | parameter / VectorRotate3x3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d )` |
| 1410 | `r` | parameter / VectorRotate3x3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d )` |
| 1410 | `d` | parameter / VectorRotate3x3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotate3x3( vec3_t v, float r[3][3], vec3_t d )` |
| 1422 | `MatrixTransformVector33` | function / MatrixTransformVector33 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out ) {` |
| 1422 | `in` | parameter / MatrixTransformVector33 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out ) {` |
| 1422 | `m` | parameter / MatrixTransformVector33 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out ) {` |
| 1422 | `out` | parameter / MatrixTransformVector33 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector33( const vec3_t in, const float m[3][3], vec3_t out ) {` |
| 1433 | `MatrixTransformVector43` | function / MatrixTransformVector43 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1433 | `in` | parameter / MatrixTransformVector43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1433 | `m` | parameter / MatrixTransformVector43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1433 | `out` | parameter / MatrixTransformVector43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1444 | `MatrixTransformVector44` | function / MatrixTransformVector44 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out ) {` |
| 1444 | `in` | parameter / MatrixTransformVector44 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out ) {` |
| 1444 | `m` | parameter / MatrixTransformVector44 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out ) {` |
| 1444 | `out` | parameter / MatrixTransformVector44 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector44( const vec3_t in, const float m[4][4], vec3_t out ) {` |
| 1455 | `MatrixTransposeTransformVector` | function / MatrixTransposeTransformVector | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1455 | `in` | parameter / MatrixTransposeTransformVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1455 | `m` | parameter / MatrixTransposeTransformVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1455 | `out` | parameter / MatrixTransposeTransformVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransposeTransformVector( const vec3_t in, const float m[4][3], vec3_t out ) {` |
| 1456 | `local` | local / MatrixTransposeTransformVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t local;` |
| 1469 | `MatrixTransformVector43Equals` | function / MatrixTransformVector43Equals | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixTransformVector43Equals( vec3_t v, const float matrix[4][3] ) {` |
| 1469 | `v` | parameter / MatrixTransformVector43Equals | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43Equals( vec3_t v, const float matrix[4][3] ) {` |
| 1469 | `matrix` | parameter / MatrixTransformVector43Equals | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixTransformVector43Equals( vec3_t v, const float matrix[4][3] ) {` |
| 1470 | `transformed` | local / MatrixTransformVector43Equals | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec2_t transformed;` |
| 1487 | `RotateVector2D` | function / RotateVector2D | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void RotateVector2D( vec3_t v, float degrees ) {` |
| 1487 | `v` | parameter / RotateVector2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateVector2D( vec3_t v, float degrees ) {` |
| 1487 | `degrees` | parameter / RotateVector2D | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateVector2D( vec3_t v, float degrees ) {` |
| 1488 | `angle` | local / RotateVector2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, x;` |
| 1488 | `s` | local / RotateVector2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, x;` |
| 1488 | `c` | local / RotateVector2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, x;` |
| 1488 | `x` | local / RotateVector2D | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, x;` |
| 1501 | `QuatMultiply` | function / QuatMultiply | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out ) {` |
| 1501 | `a` | parameter / QuatMultiply | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out ) {` |
| 1501 | `b` | parameter / QuatMultiply | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out ) {` |
| 1501 | `out` | parameter / QuatMultiply | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatMultiply( const vec4_t a, const vec4_t b, vec4_t out ) {` |
| 1513 | `QuatInverse` | function / QuatInverse | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void QuatInverse( const vec4_t in, vec4_t out ) {` |
| 1513 | `in` | parameter / QuatInverse | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatInverse( const vec4_t in, vec4_t out ) {` |
| 1513 | `out` | parameter / QuatInverse | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void QuatInverse( const vec4_t in, vec4_t out ) {` |
| 1525 | `ConvertQuatToMat` | function / ConvertQuatToMat | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ConvertQuatToMat( float quatAndMatrix[9] ) {` |
| 1525 | `quatAndMatrix` | parameter / ConvertQuatToMat | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ConvertQuatToMat( float quatAndMatrix[9] ) {` |
| 1526 | `xx` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, len2, s;` |
| 1526 | `yy` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, len2, s;` |
| 1526 | `zz` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, len2, s;` |
| 1526 | `len2` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, len2, s;` |
| 1526 | `s` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, len2, s;` |
| 1527 | `xs` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xs, ys;` |
| 1527 | `ys` | local / ConvertQuatToMat | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float xs, ys;` |
| 1528 | `xy` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xy, xz, xw, yz, yw, zw;` |
| 1528 | `xz` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xy, xz, xw, yz, yw, zw;` |
| 1528 | `xw` | local / ConvertQuatToMat | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float xy, xz, xw, yz, yw, zw;` |
| 1528 | `yz` | local / ConvertQuatToMat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xy, xz, xw, yz, yw, zw;` |
| 1528 | `yw` | local / ConvertQuatToMat | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float xy, xz, xw, yz, yw, zw;` |
| 1528 | `zw` | local / ConvertQuatToMat | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float xy, xz, xw, yz, yw, zw;` |
| 1580 | `QuatEigenTrace` | function / QuatEigenTrace | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float QuatEigenTrace( const vec4_t q ) {` |
| 1580 | `q` | parameter / QuatEigenTrace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float QuatEigenTrace( const vec4_t q ) {` |
| 1581 | `xx` | local / QuatEigenTrace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, lengthSquared;` |
| 1581 | `yy` | local / QuatEigenTrace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, lengthSquared;` |
| 1581 | `zz` | local / QuatEigenTrace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, yy, zz, lengthSquared;` |
| 1581 | `lengthSquared` | local / QuatEigenTrace | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `float xx, yy, zz, lengthSquared;` |
| 1602 | `AngleEigenTrace` | function / AngleEigenTrace | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleEigenTrace( float degrees ) {` |
| 1602 | `degrees` | parameter / AngleEigenTrace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleEigenTrace( float degrees ) {` |
| 1603 | `s` | local / AngleEigenTrace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double s = sin( degrees * ( M_PI / 180.0f ) );` |
| 1613 | `QuatRatioEigenTrace` | function / QuatRatioEigenTrace | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float QuatRatioEigenTrace( const vec4_t a, const vec4_t b ) {` |
| 1613 | `a` | parameter / QuatRatioEigenTrace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float QuatRatioEigenTrace( const vec4_t a, const vec4_t b ) {` |
| 1613 | `b` | parameter / QuatRatioEigenTrace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float QuatRatioEigenTrace( const vec4_t a, const vec4_t b ) {` |
| 1614 | `conj` | local / QuatRatioEigenTrace | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `vec4_t conj, delta;` |
| 1614 | `delta` | local / QuatRatioEigenTrace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec4_t conj, delta;` |
| 1626 | `RotationToYaw` | function / RotationToYaw | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float RotationToYaw( const float v[2] ) {` |
| 1626 | `v` | parameter / RotationToYaw | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RotationToYaw( const float v[2] ) {` |
| 1627 | `xx` | local / RotationToYaw | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, scale;` |
| 1627 | `scale` | local / RotationToYaw | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float xx, scale;` |
| 1642 | `PitchToQuaternion` | function / PitchToQuaternion | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void PitchToQuaternion( float degrees, vec4_t q ) {` |
| 1642 | `degrees` | parameter / PitchToQuaternion | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PitchToQuaternion( float degrees, vec4_t q ) {` |
| 1642 | `q` | parameter / PitchToQuaternion | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PitchToQuaternion( float degrees, vec4_t q ) {` |
| 1654 | `YawToQuaternion` | function / YawToQuaternion | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void YawToQuaternion( float degrees, vec4_t q ) {` |
| 1654 | `degrees` | parameter / YawToQuaternion | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawToQuaternion( float degrees, vec4_t q ) {` |
| 1654 | `q` | parameter / YawToQuaternion | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawToQuaternion( float degrees, vec4_t q ) {` |
| 1666 | `RollToQuaternion` | function / RollToQuaternion | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void RollToQuaternion( float degrees, vec4_t q ) {` |
| 1666 | `degrees` | parameter / RollToQuaternion | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RollToQuaternion( float degrees, vec4_t q ) {` |
| 1666 | `q` | parameter / RollToQuaternion | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RollToQuaternion( float degrees, vec4_t q ) {` |
| 1678 | `ColorBytes3` | function / ColorBytes3 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `unsigned ColorBytes3( float r, float g, float b ) {` |
| 1678 | `r` | parameter / ColorBytes3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes3( float r, float g, float b ) {` |
| 1678 | `g` | parameter / ColorBytes3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes3( float r, float g, float b ) {` |
| 1678 | `b` | parameter / ColorBytes3 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes3( float r, float g, float b ) {` |
| 1679 | `i` | local / ColorBytes3 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned i;` |
| 1694 | `ColorBytes4` | function / ColorBytes4 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `unsigned ColorBytes4( float r, float g, float b, float a ) {` |
| 1694 | `r` | parameter / ColorBytes4 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a ) {` |
| 1694 | `g` | parameter / ColorBytes4 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a ) {` |
| 1694 | `b` | parameter / ColorBytes4 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a ) {` |
| 1694 | `a` | parameter / ColorBytes4 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `unsigned ColorBytes4( float r, float g, float b, float a ) {` |
| 1695 | `i` | local / ColorBytes4 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned i;` |
| 1710 | `NormalizeColor` | function / NormalizeColor | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float NormalizeColor( const vec3_t in, vec3_t out ) {` |
| 1710 | `in` | parameter / NormalizeColor | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float NormalizeColor( const vec3_t in, vec3_t out ) {` |
| 1710 | `out` | parameter / NormalizeColor | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float NormalizeColor( const vec3_t in, vec3_t out ) {` |
| 1711 | `max` | local / NormalizeColor | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float max;` |
| 1735 | `AngleMod` | function / AngleMod | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleMod( float a ) {` |
| 1735 | `a` | parameter / AngleMod | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleMod( float a ) {` |
| 1745 | `LerpAngle` | function / LerpAngle | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float LerpAngle( float from, float to, float frac ) {` |
| 1745 | `from` | parameter / LerpAngle | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float LerpAngle( float from, float to, float frac ) {` |
| 1745 | `to` | parameter / LerpAngle | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float LerpAngle( float from, float to, float frac ) {` |
| 1745 | `frac` | parameter / LerpAngle | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float LerpAngle( float from, float to, float frac ) {` |
| 1746 | `a` | local / LerpAngle | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float a;` |
| 1766 | `AngleSubtract` | function / AngleSubtract | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleSubtract( float a1, float a2 ) {` |
| 1766 | `a1` | parameter / AngleSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleSubtract( float a1, float a2 ) {` |
| 1766 | `a2` | parameter / AngleSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleSubtract( float a1, float a2 ) {` |
| 1767 | `a` | local / AngleSubtract | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float a;` |
| 1784 | `AnglesSubtract` | function / AnglesSubtract | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 ) {` |
| 1784 | `v1` | parameter / AnglesSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 ) {` |
| 1784 | `v2` | parameter / AnglesSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 ) {` |
| 1784 | `v3` | parameter / AnglesSubtract | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesSubtract( const vec3_t v1, const vec3_t v2, vec3_t v3 ) {` |
| 1797 | `AngleNormalize360` | function / AngleNormalize360 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleNormalize360( float angle ) {` |
| 1797 | `angle` | parameter / AngleNormalize360 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize360( float angle ) {` |
| 1808 | `AngleNormalize180` | function / AngleNormalize180 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleNormalize180( float angle ) {` |
| 1808 | `angle` | parameter / AngleNormalize180 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize180( float angle ) {` |
| 1809 | `normalized` | local / AngleNormalize180 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float normalized;` |
| 1823 | `AngleNormalize360Accurate` | function / AngleNormalize360Accurate | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleNormalize360Accurate( float angle ) {` |
| 1823 | `angle` | parameter / AngleNormalize360Accurate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize360Accurate( float angle ) {` |
| 1841 | `AngleNormalize180Accurate` | function / AngleNormalize180Accurate | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleNormalize180Accurate( float angle ) {` |
| 1841 | `angle` | parameter / AngleNormalize180Accurate | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleNormalize180Accurate( float angle ) {` |
| 1861 | `AngleDelta` | function / AngleDelta | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float AngleDelta( float angle1, float angle2 ) {` |
| 1861 | `angle1` | parameter / AngleDelta | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleDelta( float angle1, float angle2 ) {` |
| 1861 | `angle2` | parameter / AngleDelta | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float AngleDelta( float angle1, float angle2 ) {` |
| 1870 | `RadiusFromBounds` | function / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float RadiusFromBounds( const vec3_t mins, const vec3_t maxs ) {` |
| 1870 | `mins` | parameter / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RadiusFromBounds( const vec3_t mins, const vec3_t maxs ) {` |
| 1870 | `maxs` | parameter / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RadiusFromBounds( const vec3_t mins, const vec3_t maxs ) {` |
| 1871 | `i` | local / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1872 | `corner` | local / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t corner;` |
| 1873 | `a` | local / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float a, b;` |
| 1873 | `b` | local / RadiusFromBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float a, b;` |
| 1888 | `ClearBounds` | function / ClearBounds | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ClearBounds (vec3_t mins, vec3_t maxs)` |
| 1888 | `mins` | parameter / ClearBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ClearBounds (vec3_t mins, vec3_t maxs)` |
| 1888 | `maxs` | parameter / ClearBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ClearBounds (vec3_t mins, vec3_t maxs)` |
| 1899 | `AddPointToBounds` | function / AddPointToBounds | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs ) {` |
| 1899 | `v` | parameter / AddPointToBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs ) {` |
| 1899 | `mins` | parameter / AddPointToBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs ) {` |
| 1899 | `maxs` | parameter / AddPointToBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AddPointToBounds( const vec3_t v, vec3_t mins, vec3_t maxs ) {` |
| 1925 | `ExpandBounds` | function / ExpandBounds | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs ) {` |
| 1925 | `mins` | parameter / ExpandBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs ) {` |
| 1925 | `maxs` | parameter / ExpandBounds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs ) {` |
| 1925 | `outMins` | parameter / ExpandBounds | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs ) {` |
| 1925 | `outMaxs` | parameter / ExpandBounds | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs, vec3_t outMins, vec3_t outMaxs ) {` |
| 1926 | `i` | local / ExpandBounds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 1943 | `AxisClear` | function / AxisClear | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AxisClear( vec3_t axis[3] ) {` |
| 1943 | `axis` | parameter / AxisClear | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisClear( vec3_t axis[3] ) {` |
| 1960 | `AxisCopy` | function / AxisCopy | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AxisCopy( vec3_t in[3], vec3_t out[3] ) {` |
| 1960 | `in` | parameter / AxisCopy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisCopy( vec3_t in[3], vec3_t out[3] ) {` |
| 1960 | `out` | parameter / AxisCopy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisCopy( vec3_t in[3], vec3_t out[3] ) {` |
| 1971 | `AnglesToAxis` | function / AnglesToAxis | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AnglesToAxis( const vec3_t angles, vec3_t axis[3] ) {` |
| 1971 | `angles` | parameter / AnglesToAxis | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesToAxis( const vec3_t angles, vec3_t axis[3] ) {` |
| 1971 | `axis` | parameter / AnglesToAxis | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AnglesToAxis( const vec3_t angles, vec3_t axis[3] ) {` |
| 1972 | `right` | local / AnglesToAxis | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t right;` |
| 1983 | `YawToAxis` | function / YawToAxis | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void YawToAxis( float yaw, vec3_t axis[3] ) {` |
| 1983 | `yaw` | parameter / YawToAxis | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawToAxis( float yaw, vec3_t axis[3] ) {` |
| 1983 | `axis` | parameter / YawToAxis | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void YawToAxis( float yaw, vec3_t axis[3] ) {` |
| 1984 | `right` | local / YawToAxis | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t right;` |
| 2003 | `AxisToAngles` | function / AxisToAngles | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AxisToAngles( const vec3_t axis[3], vec3_t angles ) {` |
| 2003 | `axis` | parameter / AxisToAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToAngles( const vec3_t axis[3], vec3_t angles ) {` |
| 2003 | `angles` | parameter / AxisToAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToAngles( const vec3_t axis[3], vec3_t angles ) {` |
| 2004 | `right` | local / AxisToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t right;` |
| 2005 | `angle` | local / AxisToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2005 | `s` | local / AxisToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2005 | `c` | local / AxisToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2005 | `t` | local / AxisToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2005 | `roll` | local / AxisToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2036 | `Axis4ToAngles` | function / Axis4ToAngles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Axis4ToAngles( const float matrix[3][4], vec3_t angles ) {` |
| 2036 | `matrix` | parameter / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Axis4ToAngles( const float matrix[3][4], vec3_t angles ) {` |
| 2036 | `angles` | parameter / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Axis4ToAngles( const float matrix[3][4], vec3_t angles ) {` |
| 2037 | `right` | local / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t right;` |
| 2038 | `angle` | local / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2038 | `s` | local / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2038 | `c` | local / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2038 | `t` | local / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2038 | `roll` | local / Axis4ToAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2069 | `AxisToSignedAngles` | function / AxisToSignedAngles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void AxisToSignedAngles( const vec3_t axis[3], vec3_t angles ) {` |
| 2069 | `axis` | parameter / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToSignedAngles( const vec3_t axis[3], vec3_t angles ) {` |
| 2069 | `angles` | parameter / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void AxisToSignedAngles( const vec3_t axis[3], vec3_t angles ) {` |
| 2070 | `right` | local / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t right;` |
| 2071 | `angle` | local / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2071 | `s` | local / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2071 | `c` | local / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2071 | `t` | local / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2071 | `roll` | local / AxisToSignedAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float angle, s, c, t, roll;` |
| 2105 | `PlaneFromPoints` | function / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c ) {` |
| 2105 | `plane` | parameter / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c ) {` |
| 2105 | `a` | parameter / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c ) {` |
| 2105 | `b` | parameter / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c ) {` |
| 2105 | `c` | parameter / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean PlaneFromPoints( vec4_t plane, const vec3_t a, const vec3_t b, const vec3_t c ) {` |
| 2106 | `d1` | local / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t d1, d2;` |
| 2106 | `d2` | local / PlaneFromPoints | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t d1, d2;` |
| 2124 | `ProjectPointOnPlane` | function / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal )` |
| 2124 | `dst` | parameter / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal )` |
| 2124 | `p` | parameter / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal )` |
| 2124 | `normal` | parameter / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOnPlane( vec3_t dst, const vec3_t p, const vec3_t normal )` |
| 2126 | `d` | local / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float d;` |
| 2127 | `n` | local / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t n;` |
| 2128 | `inv_denom` | local / ProjectPointOnPlane | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float inv_denom;` |
| 2149 | `SetPlaneSignbits` | function / SetPlaneSignbits | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void SetPlaneSignbits( cplane_t *out ) {` |
| 2149 | `out` | parameter / SetPlaneSignbits | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void SetPlaneSignbits( cplane_t *out ) {` |
| 2150 | `bits` | local / SetPlaneSignbits | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte bits;` |
| 2151 | `j` | local / SetPlaneSignbits | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int j;` |
| 2204 | `BoxOnPlaneSide` | function / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `__declspec( naked ) int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p )` |
| 2204 | `emins` | parameter / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__declspec( naked ) int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p )` |
| 2204 | `emaxs` | parameter / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__declspec( naked ) int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p )` |
| 2204 | `p` | parameter / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `__declspec( naked ) int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p )` |
| 2204 | `cplane_s` | tag / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `__declspec( naked ) int BoxOnPlaneSide( vec3_t emins, vec3_t emaxs, struct cplane_s *p )` |
| 2206 | `bops_initialized` | local / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static int bops_initialized;` |
| 2207 | `Ljmptab` | local / BoxOnPlaneSide | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `static int Ljmptab[8];` |
| 2442 | `BoxDistSqrdExceeds` | function / BoxDistSqrdExceeds | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd ) {` |
| 2442 | `absmin` | parameter / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd ) {` |
| 2442 | `absmax` | parameter / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd ) {` |
| 2442 | `origin` | parameter / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd ) {` |
| 2442 | `distSqrd` | parameter / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int BoxDistSqrdExceeds( const vec3_t absmin, const vec3_t absmax, const vec3_t origin, float distSqrd ) {` |
| 2443 | `d` | local / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t d[2];` |
| 2444 | `dist` | local / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float dist;` |
| 2445 | `i` | local / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2454 | `a` | local / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float a, b;` |
| 2454 | `b` | local / BoxDistSqrdExceeds | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float a, b;` |
| 2468 | `NormalToLatLong` | function / NormalToLatLong | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] ) {` |
| 2468 | `normal` | parameter / NormalToLatLong | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] ) {` |
| 2468 | `bytes` | parameter / NormalToLatLong | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void NormalToLatLong( const vec3_t normal, byte bytes[2] ) {` |
| 2479 | `a` | local / NormalToLatLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte a, b;` |
| 2479 | `b` | local / NormalToLatLong | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `byte a, b;` |
| 2495 | `Vec10Copy` | function / Vec10Copy | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Vec10Copy( vec_t *in, vec_t *out ) {` |
| 2495 | `in` | parameter / Vec10Copy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vec10Copy( vec_t *in, vec_t *out ) {` |
| 2495 | `out` | parameter / Vec10Copy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Vec10Copy( vec_t *in, vec_t *out ) {` |
| 2513 | `Q_rint` | function / Q_rint | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `vec_t Q_rint (vec_t in)` |
| 2513 | `in` | parameter / Q_rint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t Q_rint (vec_t in)` |
| 2523 | `ColorNormalize` | function / ColorNormalize | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `vec_t ColorNormalize( const vec3_t in, vec3_t out ) {` |
| 2523 | `in` | parameter / ColorNormalize | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t ColorNormalize( const vec3_t in, vec3_t out ) {` |
| 2523 | `out` | parameter / ColorNormalize | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t ColorNormalize( const vec3_t in, vec3_t out ) {` |
| 2524 | `max` | local / ColorNormalize | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	max, scale;` |
| 2524 | `scale` | local / ColorNormalize | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	max, scale;` |
| 2549 | `VectorRotateAngles` | function / VectorRotateAngles | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out ) {` |
| 2549 | `in` | parameter / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out ) {` |
| 2549 | `angles` | parameter / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out ) {` |
| 2549 | `out` | parameter / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out ) {` |
| 2550 | `v` | local / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v, r;` |
| 2550 | `r` | local / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t v, r;` |
| 2551 | `pair` | local / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int pair[3][2];` |
| 2552 | `s` | local / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double s, c;` |
| 2552 | `c` | local / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double s, c;` |
| 2553 | `i` | local / VectorRotateAngles | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2579 | `VectorRotateAnglesAroundPoint` | function / VectorRotateAnglesAroundPoint | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 2579 | `point` | parameter / VectorRotateAnglesAroundPoint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 2579 | `angles` | parameter / VectorRotateAnglesAroundPoint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 2580 | `pivot` | parameter / VectorRotateAnglesAroundPoint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t pivot, vec3_t out ) {` |
| 2580 | `out` | parameter / VectorRotateAnglesAroundPoint | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t pivot, vec3_t out ) {` |
| 2581 | `rel` | local / VectorRotateAnglesAroundPoint | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t rel, res;` |
| 2581 | `res` | local / VectorRotateAnglesAroundPoint | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t rel, res;` |
| 2593 | `VectorPolar` | function / VectorPolar | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorPolar( vec3_t out, float radius, float angle ) {` |
| 2593 | `out` | parameter / VectorPolar | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorPolar( vec3_t out, float radius, float angle ) {` |
| 2593 | `radius` | parameter / VectorPolar | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorPolar( vec3_t out, float radius, float angle ) {` |
| 2593 | `angle` | parameter / VectorPolar | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorPolar( vec3_t out, float radius, float angle ) {` |
| 2594 | `s1` | local / VectorPolar | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float s1, c1, s2, c2;` |
| 2594 | `c1` | local / VectorPolar | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float s1, c1, s2, c2;` |
| 2594 | `s2` | local / VectorPolar | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float s1, c1, s2, c2;` |
| 2594 | `c2` | local / VectorPolar | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float s1, c1, s2, c2;` |
| 2607 | `VectorSnap` | function / VectorSnap | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void VectorSnap( vec3_t v ) {` |
| 2607 | `v` | parameter / VectorSnap | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorSnap( vec3_t v ) {` |
| 2618 | `_Vector5Add` | function / _Vector5Add | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out)` |
| 2618 | `va` | parameter / _Vector5Add | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out)` |
| 2618 | `vb` | parameter / _Vector5Add | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out)` |
| 2618 | `out` | parameter / _Vector5Add | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Add (vec5_t va, vec5_t vb, vec5_t out)` |
| 2632 | `_Vector5Scale` | function / _Vector5Scale | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out)` |
| 2632 | `v` | parameter / _Vector5Scale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out)` |
| 2632 | `scale` | parameter / _Vector5Scale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out)` |
| 2632 | `out` | parameter / _Vector5Scale | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector5Scale (vec5_t v, vec_t scale, vec5_t out)` |
| 2646 | `_Vector53Copy` | function / _Vector53Copy | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _Vector53Copy( const vec3_t in, vec3_t out ) {` |
| 2646 | `in` | parameter / _Vector53Copy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector53Copy( const vec3_t in, vec3_t out ) {` |
| 2646 | `out` | parameter / _Vector53Copy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _Vector53Copy( const vec3_t in, vec3_t out ) {` |
| 2655 | `RoundToPrecision` | function / RoundToPrecision | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float RoundToPrecision( float value, int places ) {` |
| 2655 | `value` | parameter / RoundToPrecision | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RoundToPrecision( float value, int places ) {` |
| 2655 | `places` | parameter / RoundToPrecision | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float RoundToPrecision( float value, int places ) {` |
| 2656 | `scaled` | local / RoundToPrecision | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double scaled, frac;` |
| 2656 | `frac` | local / RoundToPrecision | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double scaled, frac;` |
| 2673 | `PitchForYawOnNormal` | function / PitchForYawOnNormal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float PitchForYawOnNormal( float yaw, const vec3_t normal ) {` |
| 2673 | `yaw` | parameter / PitchForYawOnNormal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float PitchForYawOnNormal( float yaw, const vec3_t normal ) {` |
| 2673 | `normal` | parameter / PitchForYawOnNormal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float PitchForYawOnNormal( float yaw, const vec3_t normal ) {` |
| 2674 | `forward` | local / PitchForYawOnNormal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t forward, projected;` |
| 2674 | `projected` | local / PitchForYawOnNormal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t forward, projected;` |
| 2686 | `Com_SRand` | function / Com_SRand | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_SRand( int seed ) {` |
| 2686 | `seed` | parameter / Com_SRand | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_SRand( int seed ) {` |
| 2695 | `Com_RandFloatRange` | function / Com_RandFloatRange | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Com_RandFloatRange( float lo, float hi ) {` |
| 2695 | `lo` | parameter / Com_RandFloatRange | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_RandFloatRange( float lo, float hi ) {` |
| 2695 | `hi` | parameter / Com_RandFloatRange | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_RandFloatRange( float lo, float hi ) {` |
| 2696 | `value` | local / Com_RandFloatRange | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float value;` |
| 2709 | `Com_RandIntRange` | function / Com_RandIntRange | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_RandIntRange( int lo, int hi ) {` |
| 2709 | `lo` | parameter / Com_RandIntRange | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_RandIntRange( int lo, int hi ) {` |
| 2709 | `hi` | parameter / Com_RandIntRange | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_RandIntRange( int lo, int hi ) {` |
| 2719 | `SinCosWave` | function / SinCosWave | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float SinCosWave( float freqA, float freqB, float t ) {` |
| 2719 | `freqA` | parameter / SinCosWave | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `float SinCosWave( float freqA, float freqB, float t ) {` |
| 2719 | `freqB` | parameter / SinCosWave | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `float SinCosWave( float freqA, float freqB, float t ) {` |
| 2719 | `t` | parameter / SinCosWave | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float SinCosWave( float freqA, float freqB, float t ) {` |
| 2720 | `x` | local / SinCosWave | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `double x = t / 1000.0;` |
| 2730 | `gunrandom` | function / gunrandom | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void gunrandom( float *outX, float *outY ) {` |
| 2730 | `outX` | parameter / gunrandom | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void gunrandom( float *outX, float *outY ) {` |
| 2730 | `outY` | parameter / gunrandom | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void gunrandom( float *outX, float *outY ) {` |
| 2731 | `degrees` | local / gunrandom | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float degrees, radius, s, c;` |
| 2731 | `radius` | local / gunrandom | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float degrees, radius, s, c;` |
| 2731 | `s` | local / gunrandom | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float degrees, radius, s, c;` |
| 2731 | `c` | local / gunrandom | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float degrees, radius, s, c;` |
| 2744 | `PerpendicularVector` | function / PerpendicularVector | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void PerpendicularVector( vec3_t dst, const vec3_t src )` |
| 2744 | `dst` | parameter / PerpendicularVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PerpendicularVector( vec3_t dst, const vec3_t src )` |
| 2744 | `src` | parameter / PerpendicularVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void PerpendicularVector( vec3_t dst, const vec3_t src )` |
| 2746 | `pos` | local / PerpendicularVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int	pos;` |
| 2747 | `i` | local / PerpendicularVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 2748 | `minelem` | local / PerpendicularVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float minelem = 1.0F;` |
| 2749 | `tempvec` | local / PerpendicularVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t tempvec;` |
| 2781 | `MatrixInverseOrthogonal43` | function / MatrixInverseOrthogonal43 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void MatrixInverseOrthogonal43( const float in[4][3], float out[4][3] ) {` |
| 2781 | `in` | parameter / MatrixInverseOrthogonal43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverseOrthogonal43( const float in[4][3], float out[4][3] ) {` |
| 2781 | `out` | parameter / MatrixInverseOrthogonal43 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void MatrixInverseOrthogonal43( const float in[4][3], float out[4][3] ) {` |
| 2782 | `translation` | local / MatrixInverseOrthogonal43 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t translation;` |
| 2796 | `RotatePointAroundVector` | function / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 2796 | `dst` | parameter / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 2796 | `dir` | parameter / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 2796 | `point` | parameter / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotatePointAroundVector( vec3_t dst, const vec3_t dir, const vec3_t point,` |
| 2797 | `degrees` | parameter / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float degrees ) {` |
| 2798 | `m` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	m[3][3];` |
| 2799 | `im` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	im[3][3];` |
| 2800 | `zrot` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	zrot[3][3];` |
| 2801 | `tmpmat` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	tmpmat[3][3];` |
| 2802 | `rot` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	rot[3][3];` |
| 2803 | `i` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int	i;` |
| 2804 | `vr` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t vr, vup, vf;` |
| 2804 | `vup` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t vr, vup, vf;` |
| 2804 | `vf` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t vr, vup, vf;` |
| 2805 | `rad` | local / RotatePointAroundVector | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `float	rad;` |
| 2856 | `RotateAroundDirection` | function / RotateAroundDirection | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void RotateAroundDirection( vec3_t axis[3], float yaw ) {` |
| 2856 | `axis` | parameter / RotateAroundDirection | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateAroundDirection( vec3_t axis[3], float yaw ) {` |
| 2856 | `yaw` | parameter / RotateAroundDirection | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void RotateAroundDirection( vec3_t axis[3], float yaw ) {` |
| 2860 | `temp` | local / RotateAroundDirection | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `vec3_t temp;` |

## universal/com_math.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 11 | `Q3MAP_COM_MATH_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_COM_MATH_H` |
| 17 | `VectorNormalize` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `vec_t VectorNormalize( vec3_t v );` |
| 17 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `vec_t VectorNormalize( vec3_t v );` |
| 18 | `VectorNormalize2` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `float VectorNormalize2( const vec3_t v, vec3_t out );` |
| 18 | `v` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2( const vec3_t v, vec3_t out );` |
| 18 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float VectorNormalize2( const vec3_t v, vec3_t out );` |
| 19 | `VectorCompareEpsilon` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 );` |
| 19 | `p1` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 );` |
| 19 | `p2` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean VectorCompareEpsilon( const vec3_t p1, const vec3_t p2 );` |
| 20 | `ExpandBounds` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs,` |
| 20 | `mins` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs,` |
| 20 | `maxs` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ExpandBounds( const vec3_t mins, const vec3_t maxs,` |
| 21 | `outMins` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `vec3_t outMins, vec3_t outMaxs );` |
| 21 | `outMaxs` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `vec3_t outMins, vec3_t outMaxs );` |
| 22 | `ProjectPointOntoVector` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 22 | `point` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 22 | `origin` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void ProjectPointOntoVector( const vec3_t point, const vec3_t origin,` |
| 23 | `linePoint` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `const vec3_t linePoint, vec3_t out );` |
| 23 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t linePoint, vec3_t out );` |
| 24 | `VectorRotateAngles` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 24 | `in` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 24 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 24 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAngles( const vec3_t in, const vec3_t angles, vec3_t out );` |
| 25 | `VectorRotateAnglesAroundPoint` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 25 | `point` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 25 | `angles` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void VectorRotateAnglesAroundPoint( const vec3_t point, const vec3_t angles,` |
| 26 | `pivot` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t pivot, vec3_t out );` |
| 26 | `out` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const vec3_t pivot, vec3_t out );` |

## universal/com_memory.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 28 | `HUNK_MAGIC` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_MAGIC 0x89537892U` |
| 29 | `HUNK_FREE_MAGIC` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_FREE_MAGIC 0x89537893U` |
| 30 | `HUNK_TEMP_HEADER_SIZE` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_TEMP_HEADER_SIZE 16` |
| 31 | `HUNK_TEMP_ALIGNMENT` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_TEMP_ALIGNMENT 16` |
| 32 | `HUNK_MIN_MEGABYTES` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_MIN_MEGABYTES 80` |
| 33 | `HUNK_BYTES_PER_MEGABYTE` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_BYTES_PER_MEGABYTE ( 1024 * 1024 )` |
| 34 | `HUNK_CACHELINE_ALIGNMENT` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_CACHELINE_ALIGNMENT 32` |
| 35 | `HUNK_CVAR_ARCHIVE` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define HUNK_CVAR_ARCHIVE 1` |
| 36 | `ERR_FATAL` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define ERR_FATAL 0` |
| 41 | `hunkHeader_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} hunkHeader_t;` |
| 39 | `magic` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `unsigned int magic;` |
| 40 | `size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int size;` |
| 48 | `e_prefetch` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} e_prefetch;` |
| 45 | `PRE_READ` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `PRE_READ,									// prefetch assuming that buffer is used for reading only` |
| 46 | `PRE_WRITE` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `PRE_WRITE,									// prefetch assuming that buffer is used for writing only` |
| 47 | `PRE_READ_WRITE` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `PRE_READ_WRITE								// prefetch assuming that buffer is used for both reading and writing` |
| 60 | `qtime_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} qtime_t;` |
| 50 | `qtime_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct qtime_s {` |
| 51 | `tm_sec` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_sec;` |
| 52 | `tm_min` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_min;` |
| 53 | `tm_hour` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_hour;` |
| 54 | `tm_mday` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_mday;` |
| 55 | `tm_mon` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_mon;` |
| 56 | `tm_year` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_year;` |
| 57 | `tm_wday` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_wday;` |
| 58 | `tm_yday` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_yday;` |
| 59 | `tm_isdst` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tm_isdst;` |
| 69 | `hunkblock_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} hunkblock_t;` |
| 62 | `hunkblock_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct hunkblock_s {` |
| 63 | `size` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int size;` |
| 64 | `printed` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `byte printed;` |
| 65 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct hunkblock_s *next;` |
| 65 | `hunkblock_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct hunkblock_s *next;` |
| 66 | `label` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *label;` |
| 67 | `file` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *file;` |
| 68 | `line` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int line;` |
| 76 | `hunkUsed_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} hunkUsed_t;` |
| 72 | `mark` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int mark;` |
| 73 | `tempMark` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int tempMark;` |
| 74 | `permanent` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int permanent;` |
| 75 | `temp` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int temp;` |
| 78 | `s_hunkTotal` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static int s_hunkTotal = 0;` |
| 79 | `s_zoneTotal` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int s_zoneTotal = 0;` |
| 80 | `hunk_high` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static hunkUsed_t hunk_high = { 0 };` |
| 81 | `hunkblocks` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `hunkblock_t *hunkblocks = 0;` |
| 82 | `logfile` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `fileHandle_t logfile = 0;` |
| 83 | `hunk_low` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static hunkUsed_t hunk_low = { 0 };` |
| 84 | `s_hunkData` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static byte *s_hunkData = 0;` |
| 85 | `s_hunkOriginal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `byte *s_hunkOriginal = 0;` |
| 87 | `FS_ClearDataForFiles` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void FS_ClearDataForFiles( void *lowEnd, void *highEnd );` |
| 87 | `lowEnd` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_ClearDataForFiles( void *lowEnd, void *highEnd );` |
| 87 | `highEnd` | parameter | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `void FS_ClearDataForFiles( void *lowEnd, void *highEnd );` |
| 88 | `FS_Initialized` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `qboolean FS_Initialized( void );` |
| 89 | `FS_LoadStack` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int FS_LoadStack( void );` |
| 90 | `FS_ClearMemory` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void FS_ClearMemory( void );` |
| 91 | `va` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *va( const char *format, ... );` |
| 91 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *va( const char *format, ... );` |
| 92 | `Z_FreeInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Z_FreeInternal( void *block );` |
| 92 | `block` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Z_FreeInternal( void *block );` |
| 93 | `Z_MallocInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void *Z_MallocInternal( int size );` |
| 93 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Z_MallocInternal( int size );` |
| 94 | `Hunk_Clear` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Hunk_Clear( void );` |
| 95 | `Com_Meminfo_f` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Meminfo_f( void );` |
| 96 | `Com_Memset` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Memset( void *dest, const int val, const size_t count );` |
| 96 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset( void *dest, const int val, const size_t count );` |
| 96 | `val` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset( void *dest, const int val, const size_t count );` |
| 96 | `count` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset( void *dest, const int val, const size_t count );` |
| 97 | `Com_Prefetch` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Prefetch( const void *s, const unsigned int bytes, e_prefetch type );` |
| 97 | `s` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Prefetch( const void *s, const unsigned int bytes, e_prefetch type );` |
| 97 | `bytes` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Prefetch( const void *s, const unsigned int bytes, e_prefetch type );` |
| 97 | `type` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Prefetch( const void *s, const unsigned int bytes, e_prefetch type );` |
| 104 | `Com_RealTime` | function / Com_RealTime | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_RealTime( qtime_t *qtime ) {` |
| 104 | `qtime` | parameter / Com_RealTime | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_RealTime( qtime_t *qtime ) {` |
| 105 | `t` | local / Com_RealTime | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `time_t t;` |
| 106 | `tms` | local / Com_RealTime | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `struct tm *tms;` |
| 106 | `tm` | tag / Com_RealTime | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct tm *tms;` |
| 132 | `Z_FreeInternal` | function / Z_FreeInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Z_FreeInternal( void *block ) {` |
| 132 | `block` | parameter / Z_FreeInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Z_FreeInternal( void *block ) {` |
| 141 | `Com_Meminfo_f` | function / Com_Meminfo_f | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Meminfo_f( void ) {` |
| 142 | `totalHunkInUse` | local / Com_Meminfo_f | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int totalHunkInUse;` |
| 169 | `Com_InitZoneMemory` | function / Com_InitZoneMemory | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_InitZoneMemory( void ) {` |
| 177 | `Hunk_Log` | function / Hunk_Log | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_Log( void ) {` |
| 178 | `block` | local / Hunk_Log | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `hunkblock_t *block;` |
| 179 | `buf` | local / Hunk_Log | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char buf[4096];` |
| 180 | `size` | local / Hunk_Log | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, numBlocks;` |
| 180 | `numBlocks` | local / Hunk_Log | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, numBlocks;` |
| 205 | `Hunk_SmallLog` | function / Hunk_SmallLog | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_SmallLog( void ) {` |
| 206 | `block` | local / Hunk_SmallLog | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `hunkblock_t *block, *block2;` |
| 206 | `block2` | local / Hunk_SmallLog | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `hunkblock_t *block, *block2;` |
| 207 | `buf` | local / Hunk_SmallLog | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char buf[4096];` |
| 208 | `size` | local / Hunk_SmallLog | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, numBlocks;` |
| 208 | `numBlocks` | local / Hunk_SmallLog | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size, numBlocks;` |
| 249 | `Hunk_MemoryRemaining` | function / Hunk_MemoryRemaining | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_MemoryRemaining( void ) {` |
| 258 | `Hunk_ClearData` | function / Hunk_ClearData | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_ClearData( void ) {` |
| 268 | `Hunk_SetMark2` | function / Hunk_SetMark2 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_SetMark2( void ) {` |
| 278 | `Hunk_SetHighTempMark` | function / Hunk_SetHighTempMark | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_SetHighTempMark( void )` |
| 289 | `Hunk_CheckMark` | function / Hunk_CheckMark | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean Hunk_CheckMark( const void *ptr ) {` |
| 289 | `ptr` | parameter / Hunk_CheckMark | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `qboolean Hunk_CheckMark( const void *ptr ) {` |
| 298 | `Hunk_ClearToMark2` | function / Hunk_ClearToMark2 | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_ClearToMark2( void ) {` |
| 309 | `Hunk_ClearToHighTempMark` | function / Hunk_ClearToHighTempMark | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_ClearToHighTempMark( void ) {` |
| 320 | `Hunk_HighMarkIsSet` | function / Hunk_HighMarkIsSet | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `qboolean Hunk_HighMarkIsSet( void )` |
| 330 | `Hunk_SetMarkLow` | function / Hunk_SetMarkLow | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_SetMarkLow( void )` |
| 341 | `Hunk_ClearToMarkLow` | function / Hunk_ClearToMarkLow | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_ClearToMarkLow( void ) {` |
| 352 | `Hunk_ClearToStart` | function / Hunk_ClearToStart | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_ClearToStart( void ) {` |
| 373 | `Hunk_Clear` | function / Hunk_Clear | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_Clear( void ) {` |
| 382 | `Com_ShutdownHunkMemory` | function / Com_ShutdownHunkMemory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_ShutdownHunkMemory( void ) {` |
| 393 | `Hunk_AllocAlignInternal` | function / Hunk_AllocAlignInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_AllocAlignInternal( int size, int align ) {` |
| 393 | `size` | parameter / Hunk_AllocAlignInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocAlignInternal( int size, int align ) {` |
| 393 | `align` | parameter / Hunk_AllocAlignInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocAlignInternal( int size, int align ) {` |
| 394 | `mark` | local / Hunk_AllocAlignInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int mark;` |
| 395 | `block` | local / Hunk_AllocAlignInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `void *block;` |
| 421 | `Hunk_AllocateTempMemoryHighInternal` | function / Hunk_AllocateTempMemoryHighInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_AllocateTempMemoryHighInternal( int size ) {` |
| 421 | `size` | parameter / Hunk_AllocateTempMemoryHighInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocateTempMemoryHighInternal( int size ) {` |
| 436 | `Hunk_ClearTempMemoryHigh` | function / Hunk_ClearTempMemoryHigh | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_ClearTempMemoryHigh( void )` |
| 447 | `Hunk_AllocLowAlignInternal` | function / Hunk_AllocLowAlignInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_AllocLowAlignInternal( int size, int align ) {` |
| 447 | `size` | parameter / Hunk_AllocLowAlignInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocLowAlignInternal( int size, int align ) {` |
| 447 | `align` | parameter / Hunk_AllocLowAlignInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocLowAlignInternal( int size, int align ) {` |
| 448 | `block` | local / Hunk_AllocLowAlignInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `void *block;` |
| 470 | `Hunk_CommitTempMemory` | function / Hunk_CommitTempMemory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_CommitTempMemory( void )` |
| 481 | `Hunk_ReallocateTempMemory` | function / Hunk_ReallocateTempMemory | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_ReallocateTempMemory( int size ) {` |
| 481 | `size` | parameter / Hunk_ReallocateTempMemory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_ReallocateTempMemory( int size ) {` |
| 495 | `Hunk_ClearToMarkTemp` | function / Hunk_ClearToMarkTemp | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_ClearToMarkTemp( void ) {` |
| 505 | `Hunk_SetMarkTemp` | function / Hunk_SetMarkTemp | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_SetMarkTemp( void )` |
| 516 | `Hunk_FreeTempMemory` | function / Hunk_FreeTempMemory | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_FreeTempMemory( void *buf ) {` |
| 516 | `buf` | parameter / Hunk_FreeTempMemory | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Hunk_FreeTempMemory( void *buf ) {` |
| 517 | `hdr` | local / Hunk_FreeTempMemory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `hunkHeader_t *hdr;` |
| 541 | `Hunk_ClearTempMemory` | function / Hunk_ClearTempMemory | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_ClearTempMemory( void )` |
| 552 | `Hunk_ConvertTempToPermLowInternal` | function / Hunk_ConvertTempToPermLowInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_ConvertTempToPermLowInternal( void )` |
| 554 | `old` | local / Hunk_ConvertTempToPermLowInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int old;` |
| 566 | `Hunk_SetLowUsedInternal` | function / Hunk_SetLowUsedInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Hunk_SetLowUsedInternal( int lowUsed )` |
| 566 | `lowUsed` | parameter / Hunk_SetLowUsedInternal | inferred/unconfirmed spelling. Describes an input/output role in the containing function. | `int Hunk_SetLowUsedInternal( int lowUsed )` |
| 577 | `Hunk_Trash` | function / Hunk_Trash | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Hunk_Trash( void )` |
| 586 | `_copyDWord` | function / _copyDWord | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void _copyDWord (unsigned int* dest, const unsigned int constant, const unsigned int count) {` |
| 586 | `dest` | parameter / _copyDWord | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _copyDWord (unsigned int* dest, const unsigned int constant, const unsigned int count) {` |
| 586 | `constant` | parameter / _copyDWord | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _copyDWord (unsigned int* dest, const unsigned int constant, const unsigned int count) {` |
| 586 | `count` | parameter / _copyDWord | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void _copyDWord (unsigned int* dest, const unsigned int constant, const unsigned int count) {` |
| 642 | `Com_Memset` | function / Com_Memset | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Memset (void* dest, const int val, const size_t count)` |
| 642 | `dest` | parameter / Com_Memset | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset (void* dest, const int val, const size_t count)` |
| 642 | `val` | parameter / Com_Memset | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset (void* dest, const int val, const size_t count)` |
| 642 | `count` | parameter / Com_Memset | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memset (void* dest, const int val, const size_t count)` |
| 644 | `fillval` | local / Com_Memset | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned int fillval;` |
| 713 | `Com_Memcmp` | function / Com_Memcmp | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_Memcmp( const void *src0, const void *src1, const unsigned int count ) {` |
| 713 | `src0` | parameter / Com_Memcmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Memcmp( const void *src0, const void *src1, const unsigned int count ) {` |
| 713 | `src1` | parameter / Com_Memcmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Memcmp( const void *src0, const void *src1, const unsigned int count ) {` |
| 713 | `count` | parameter / Com_Memcmp | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Memcmp( const void *src0, const void *src1, const unsigned int count ) {` |
| 714 | `i` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned int i;` |
| 717 | `dw` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const unsigned int *dw = src0;` |
| 718 | `sw` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const unsigned int *sw = src1;` |
| 719 | `nm2` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned int nm2 = count / 16;` |
| 722 | `tmp` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned int tmp = ( dw[i + 0] - sw[i + 0] )` |
| 732 | `d` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const byte *d = src0;` |
| 733 | `s` | local / Com_Memcmp | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const byte *s = src1;` |
| 749 | `Com_Prefetch` | function / Com_Prefetch | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Prefetch (const void *s, const unsigned int bytes, e_prefetch type)` |
| 749 | `s` | parameter / Com_Prefetch | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Prefetch (const void *s, const unsigned int bytes, e_prefetch type)` |
| 749 | `bytes` | parameter / Com_Prefetch | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Prefetch (const void *s, const unsigned int bytes, e_prefetch type)` |
| 749 | `type` | parameter / Com_Prefetch | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Prefetch (const void *s, const unsigned int bytes, e_prefetch type)` |
| 791 | `Z_MallocInternal` | function / Z_MallocInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Z_MallocInternal( int size ) {` |
| 791 | `size` | parameter / Z_MallocInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Z_MallocInternal( int size ) {` |
| 792 | `block` | local / Z_MallocInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `void *block;` |
| 808 | `CopyStringInternal` | function / CopyStringInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *CopyStringInternal( const char *in ) {` |
| 808 | `in` | parameter / CopyStringInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *CopyStringInternal( const char *in ) {` |
| 809 | `out` | local / CopyStringInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *out;` |
| 821 | `Com_InitHunkMemory` | function / Com_InitHunkMemory | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_InitHunkMemory( void ) {` |
| 822 | `cv` | local / Com_InitHunkMemory | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t *cv;` |
| 853 | `Hunk_AllocInternal` | function / Hunk_AllocInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_AllocInternal( int size )` |
| 853 | `size` | parameter / Hunk_AllocInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocInternal( int size )` |
| 863 | `Hunk_AllocLowInternal` | function / Hunk_AllocLowInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_AllocLowInternal( int size )` |
| 863 | `size` | parameter / Hunk_AllocLowInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocLowInternal( int size )` |
| 873 | `Hunk_AllocateTempMemoryInternal` | function / Hunk_AllocateTempMemoryInternal | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void *Hunk_AllocateTempMemoryInternal( int size ) {` |
| 873 | `size` | parameter / Hunk_AllocateTempMemoryInternal | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void *Hunk_AllocateTempMemoryInternal( int size ) {` |
| 874 | `hdr` | local / Hunk_AllocateTempMemoryInternal | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `hunkHeader_t *hdr;` |
| 875 | `previousLowTemp` | local / Hunk_AllocateTempMemoryInternal | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int previousLowTemp;` |
| 903 | `Com_Memcpy` | function / Com_Memcpy | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Memcpy (void* dest, const void* src, const size_t count) {` |
| 903 | `dest` | parameter / Com_Memcpy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy (void* dest, const void* src, const size_t count) {` |
| 903 | `src` | parameter / Com_Memcpy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy (void* dest, const void* src, const size_t count) {` |
| 903 | `count` | parameter / Com_Memcpy | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Memcpy (void* dest, const void* src, const size_t count) {` |

## universal/cvar.c

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 25 | `Z_FreeInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Z_FreeInternal( void *block );` |
| 25 | `block` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Z_FreeInternal( void *block );` |
| 27 | `FILE_HASH_SIZE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define FILE_HASH_SIZE 256` |
| 28 | `CVAR_UNSAFE` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_UNSAFE 0x1000` |
| 29 | `ERR_FATAL` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { ERR_FATAL, ERR_DROP };` |
| 29 | `ERR_DROP` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { ERR_FATAL, ERR_DROP };` |
| 31 | `cvar_vars` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *cvar_vars;` |
| 32 | `cvar_cheats` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *cvar_cheats = NULL;` |
| 33 | `cvar_modifiedFlags` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int cvar_modifiedFlags;` |
| 34 | `cvar_indexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t cvar_indexes[MAX_CVARS] = {0};` |
| 35 | `cvar_numIndexes` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `int cvar_numIndexes;` |
| 36 | `cvar_hashTable` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static cvar_t *cvar_hashTable[FILE_HASH_SIZE] = {0};` |
| 38 | `Com_Error` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern void Com_Error( int code, const char *format, ... );` |
| 38 | `code` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Com_Error( int code, const char *format, ... );` |
| 38 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Com_Error( int code, const char *format, ... );` |
| 39 | `Com_Printf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern void Com_Printf( const char *format, ... );` |
| 39 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Com_Printf( const char *format, ... );` |
| 40 | `Com_DPrintf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern void Com_DPrintf( const char *format, ... );` |
| 40 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Com_DPrintf( const char *format, ... );` |
| 41 | `va` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern char *va( const char *format, ... );` |
| 41 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern char *va( const char *format, ... );` |
| 42 | `CopyStringInternal` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `extern char *CopyStringInternal( const char *string );` |
| 42 | `string` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern char *CopyStringInternal( const char *string );` |
| 44 | `CVAR_SYSTEMINFO` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `enum { CVAR_SYSTEMINFO = 8 };` |
| 51 | `generateHashValue` | function / generateHashValue | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static long generateHashValue( const char *fname ) {` |
| 51 | `fname` | parameter / generateHashValue | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static long generateHashValue( const char *fname ) {` |
| 52 | `i` | local / generateHashValue | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 53 | `hash` | local / generateHashValue | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 54 | `letter` | local / generateHashValue | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int letter;` |
| 75 | `Cvar_ValidateString` | function / Cvar_ValidateString | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static qboolean Cvar_ValidateString( const char *s ) {` |
| 75 | `s` | parameter / Cvar_ValidateString | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static qboolean Cvar_ValidateString( const char *s ) {` |
| 96 | `Cvar_FindVar` | function / Cvar_FindVar | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `cvar_t *Cvar_FindVar( const char *var_name ) {` |
| 96 | `var_name` | parameter / Cvar_FindVar | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_FindVar( const char *var_name ) {` |
| 97 | `var` | local / Cvar_FindVar | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t  *var;` |
| 98 | `hash` | local / Cvar_FindVar | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 116 | `Cvar_Shutdown` | function / Cvar_Shutdown | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_Shutdown( void ) {` |
| 117 | `i` | local / Cvar_Shutdown | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `unsigned int i;` |
| 118 | `var` | local / Cvar_Shutdown | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t  *var;` |
| 150 | `Cvar_Set2` | function / Cvar_Set2 | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force ) {` |
| 150 | `var_name` | parameter / Cvar_Set2 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force ) {` |
| 150 | `value` | parameter / Cvar_Set2 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force ) {` |
| 150 | `force` | parameter / Cvar_Set2 | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force ) {` |
| 151 | `var` | local / Cvar_Set2 | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t  *var;` |
| 244 | `Cvar_Set` | function / Cvar_Set | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_Set( const char *var_name, const char *value ) {` |
| 244 | `var_name` | parameter / Cvar_Set | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Set( const char *var_name, const char *value ) {` |
| 244 | `value` | parameter / Cvar_Set | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Set( const char *var_name, const char *value ) {` |
| 253 | `Cvar_SetLatched` | function / Cvar_SetLatched | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_SetLatched( const char *var_name, const char *value ) {` |
| 253 | `var_name` | parameter / Cvar_SetLatched | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_SetLatched( const char *var_name, const char *value ) {` |
| 253 | `value` | parameter / Cvar_SetLatched | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_SetLatched( const char *var_name, const char *value ) {` |
| 262 | `Cvar_SetValue` | function / Cvar_SetValue | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_SetValue( const char *var_name, float value ) {` |
| 262 | `var_name` | parameter / Cvar_SetValue | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_SetValue( const char *var_name, float value ) {` |
| 262 | `value` | parameter / Cvar_SetValue | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_SetValue( const char *var_name, float value ) {` |
| 263 | `val` | local / Cvar_SetValue | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char val[32];` |
| 278 | `Cvar_Reset` | function / Cvar_Reset | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_Reset( const char *var_name ) {` |
| 278 | `var_name` | parameter / Cvar_Reset | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Reset( const char *var_name ) {` |
| 289 | `Cvar_Update` | function / Cvar_Update | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void    Cvar_Update( vmCvar_t *vmCvar ) {` |
| 289 | `vmCvar` | parameter / Cvar_Update | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void    Cvar_Update( vmCvar_t *vmCvar ) {` |
| 290 | `cv` | local / Cvar_Update | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t  *cv;` |
| 324 | `Cvar_Get` | function / Cvar_Get | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags ) {` |
| 324 | `var_name` | parameter / Cvar_Get | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags ) {` |
| 324 | `var_value` | parameter / Cvar_Get | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags ) {` |
| 324 | `flags` | parameter / Cvar_Get | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags ) {` |
| 325 | `var` | local / Cvar_Get | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t  *var;` |
| 326 | `hash` | local / Cvar_Get | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `long hash;` |
| 327 | `prev` | local / Cvar_Get | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t  **prev;` |
| 359 | `s` | local / Cvar_Get | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *s;` |
| 415 | `Cvar_VMSet` | function / Cvar_VMSet | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_VMSet( vmCvar_t *vmCvar, const char *value ) {` |
| 415 | `vmCvar` | parameter / Cvar_VMSet | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_VMSet( vmCvar_t *vmCvar, const char *value ) {` |
| 415 | `value` | parameter / Cvar_VMSet | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_VMSet( vmCvar_t *vmCvar, const char *value ) {` |
| 427 | `Cvar_Register` | function / Cvar_Register | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_Register( vmCvar_t *vmCvar, const char *varName,` |
| 427 | `vmCvar` | parameter / Cvar_Register | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Register( vmCvar_t *vmCvar, const char *varName,` |
| 427 | `varName` | parameter / Cvar_Register | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Register( vmCvar_t *vmCvar, const char *varName,` |
| 428 | `defaultValue` | parameter / Cvar_Register | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *defaultValue, int flags ) {` |
| 428 | `flags` | parameter / Cvar_Register | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `const char *defaultValue, int flags ) {` |
| 429 | `cv` | local / Cvar_Register | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `cvar_t *cv;` |
| 447 | `Cvar_Init` | function / Cvar_Init | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Cvar_Init( void ) {` |

## universal/cvar.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 24 | `Q3MAP_CVAR_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_CVAR_H` |
| 28 | `CVAR_INIT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_INIT         16` |
| 29 | `CVAR_LATCH` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_LATCH        32` |
| 30 | `CVAR_ROM` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_ROM          64` |
| 31 | `CVAR_USER_CREATED` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_USER_CREATED 128` |
| 32 | `CVAR_CHEAT` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define CVAR_CHEAT        512` |
| 46 | `cvar_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} cvar_t;` |
| 34 | `cvar_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct cvar_s {` |
| 35 | `name` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *name;` |
| 36 | `string` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *string;` |
| 37 | `resetString` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *resetString;` |
| 38 | `latchedString` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *latchedString;` |
| 39 | `flags` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int flags;` |
| 40 | `modified` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean modified;` |
| 41 | `modificationCount` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int modificationCount;` |
| 42 | `value` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float value;` |
| 43 | `integer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int integer;` |
| 44 | `next` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct cvar_s *next;` |
| 44 | `cvar_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct cvar_s *next;` |
| 45 | `hashNext` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `struct cvar_s *hashNext;` |
| 45 | `cvar_s` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `struct cvar_s *hashNext;` |
| 48 | `Cvar_FindVar` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *Cvar_FindVar( const char *var_name );` |
| 48 | `var_name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_FindVar( const char *var_name );` |
| 49 | `Cvar_Get` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags );` |
| 49 | `var_name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags );` |
| 49 | `var_value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags );` |
| 49 | `flags` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Get( const char *var_name, const char *var_value, int flags );` |
| 50 | `Cvar_Set2` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force );` |
| 50 | `var_name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force );` |
| 50 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force );` |
| 50 | `force` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `cvar_t *Cvar_Set2( const char *var_name, const char *value, qboolean force );` |
| 51 | `Cvar_Set` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Cvar_Set( const char *var_name, const char *value );` |
| 51 | `var_name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Set( const char *var_name, const char *value );` |
| 51 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Set( const char *var_name, const char *value );` |

## universal/cvar_vm.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 25 | `Q3MAP_CVAR_VM_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_CVAR_VM_H` |
| 29 | `MAX_CVARS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_CVARS 1024` |
| 30 | `MAX_CVAR_VALUE_STRING` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_CVAR_VALUE_STRING 256` |
| 32 | `cvarHandle_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `typedef int cvarHandle_t;` |
| 39 | `vmCvar_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} vmCvar_t;` |
| 34 | `handle` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `cvarHandle_t handle;` |
| 35 | `modificationCount` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int modificationCount;` |
| 36 | `value` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `float value;` |
| 37 | `integer` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int integer;` |
| 38 | `string` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char string[MAX_CVAR_VALUE_STRING];` |
| 41 | `Cvar_Shutdown` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `void Cvar_Shutdown( void );` |
| 42 | `Cvar_SetValue` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Cvar_SetValue( const char *var_name, float value );` |
| 42 | `var_name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_SetValue( const char *var_name, float value );` |
| 42 | `value` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_SetValue( const char *var_name, float value );` |
| 43 | `Cvar_Reset` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Cvar_Reset( const char *var_name );` |
| 43 | `var_name` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Reset( const char *var_name );` |
| 44 | `Cvar_Update` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Cvar_Update( vmCvar_t *vmCvar );` |
| 44 | `vmCvar` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Cvar_Update( vmCvar_t *vmCvar );` |
| 46 | `Com_sprintf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 46 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 46 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 46 | `format` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern int Com_sprintf( char *dest, int size, const char *format, ... );` |
| 47 | `Q_strncpyz` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `extern void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 47 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 47 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 47 | `destsize` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `extern void Q_strncpyz( char *dest, const char *src, int destsize );` |

## universal/q_parse.cpp

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 39 | `parseInfo_t` | typedef | lineage token; UO binding unconfirmed. Names the declared data representation; a descriptive alias is needed in source. | `} parseInfo_t;` |
| 28 | `parseInfo_t` | tag | lineage token; UO binding unconfirmed. Names the declared record or enumeration. | `typedef struct parseInfo_t` |
| 30 | `token` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char token[1024];` |
| 31 | `currentLine` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int currentLine;` |
| 32 | `ungetReady` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean ungetReady;` |
| 33 | `spaceDelimited` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean spaceDelimited;` |
| 34 | `csv` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean csv;` |
| 35 | `parseNegativeNumbers` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean parseNegativeNumbers;` |
| 36 | `ungetLineSave` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int ungetLineSave;` |
| 37 | `ungetTokenSave` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *ungetTokenSave;` |
| 38 | `filename` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char filename[64];` |
| 48 | `parseMark_t` | typedef | inferred/unconfirmed spelling. Names the declared data representation; a descriptive alias is needed in source. | `} parseMark_t;` |
| 41 | `parseMark_t` | tag | inferred/unconfirmed spelling. Names the declared record or enumeration. | `typedef struct parseMark_t` |
| 43 | `currentLine` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int currentLine;` |
| 44 | `data` | field | lineage token; UO binding unconfirmed. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *data;` |
| 45 | `ungetReady` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `qboolean ungetReady;` |
| 46 | `ungetLineSave` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `int ungetLineSave;` |
| 47 | `ungetTokenSave` | field | inferred/unconfirmed spelling. Describes one member of the containing record; layout/behavior constrains the role, not its spelling. | `char *ungetTokenSave;` |
| 52 | `ERR_FATAL` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `ERR_FATAL = 0,` |
| 53 | `ERR_DROP` | enum value | lineage token; UO binding unconfirmed. Names the displayed numeric case of the containing enumeration. | `ERR_DROP = 1` |
| 56 | `Com_Error` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Error( int code, const char *fmt, ... );` |
| 56 | `code` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Error( int code, const char *fmt, ... );` |
| 56 | `fmt` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Error( int code, const char *fmt, ... );` |
| 57 | `Com_Printf` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Printf( const char *fmt, ... );` |
| 57 | `fmt` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Printf( const char *fmt, ... );` |
| 58 | `Q_strcat` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Q_strcat( char *dest, int size, const char *src );` |
| 58 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strcat( char *dest, int size, const char *src );` |
| 58 | `size` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strcat( char *dest, int size, const char *src );` |
| 58 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strcat( char *dest, int size, const char *src );` |
| 59 | `Q_strncpyz` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 59 | `dest` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 59 | `src` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 59 | `destsize` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Q_strncpyz( char *dest, const char *src, int destsize );` |
| 62 | `MAX_TOKEN_CHARS` | macro | lineage token; UO binding unconfirmed. Names a constant, operation or include guard in its displayed definition. | `#define MAX_TOKEN_CHARS 1024` |
| 64 | `com_parseSeparators` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static const char *com_parseSeparators[] = {` |
| 70 | `parseInfo_stack` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static parseInfo_t parseInfo_stack[16] = {` |
| 73 | `parseInfo` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `static parseInfo_t *parseInfo = parseInfo_stack;` |
| 74 | `parseInfo_level` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static int parseInfo_level;` |
| 75 | `com_lineBuffer` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static char com_lineBuffer[MAX_TOKEN_CHARS] = {0};` |
| 76 | `prevTokenPos` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static char *prevTokenPos = NULL;` |
| 77 | `lastTokenPos` | global/prototype | inferred/unconfirmed spelling. Names the declared storage or callable interface used by this file. | `static char *lastTokenPos = NULL;` |
| 86 | `Com_BeginParseSession` | function / Com_BeginParseSession | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_BeginParseSession( const char *name ) {` |
| 86 | `name` | parameter / Com_BeginParseSession | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_BeginParseSession( const char *name ) {` |
| 104 | `Com_EndParseSession` | function / Com_EndParseSession | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_EndParseSession( void ) {` |
| 117 | `Com_ResetParseSessions` | function / Com_ResetParseSessions | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_ResetParseSessions( void ) {` |
| 127 | `Com_SetSpaceDelimited` | function / Com_SetSpaceDelimited | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_SetSpaceDelimited( qboolean enabled ) {` |
| 127 | `enabled` | parameter / Com_SetSpaceDelimited | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_SetSpaceDelimited( qboolean enabled ) {` |
| 136 | `Com_SetCSV` | function / Com_SetCSV | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_SetCSV( qboolean enabled ) {` |
| 136 | `enabled` | parameter / Com_SetCSV | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_SetCSV( qboolean enabled ) {` |
| 145 | `Com_SetParseNegativeNumbers` | function / Com_SetParseNegativeNumbers | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_SetParseNegativeNumbers( qboolean enabled ) {` |
| 145 | `enabled` | parameter / Com_SetParseNegativeNumbers | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_SetParseNegativeNumbers( qboolean enabled ) {` |
| 154 | `Com_GetCurrentParseLine` | function / Com_GetCurrentParseLine | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_GetCurrentParseLine( void ) {` |
| 165 | `Com_ScriptError` | function / Com_ScriptError | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_ScriptError( const char *fmt, ... ) {` |
| 165 | `fmt` | parameter / Com_ScriptError | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_ScriptError( const char *fmt, ... ) {` |
| 166 | `argptr` | local / Com_ScriptError | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `va_list argptr;` |
| 167 | `string` | local / Com_ScriptError | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char string[32000];` |
| 181 | `Com_ScriptWarning` | function / Com_ScriptWarning | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_ScriptWarning( const char *fmt, ... ) {` |
| 181 | `fmt` | parameter / Com_ScriptWarning | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_ScriptWarning( const char *fmt, ... ) {` |
| 182 | `argptr` | local / Com_ScriptWarning | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `va_list argptr;` |
| 183 | `string` | local / Com_ScriptWarning | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char string[32000];` |
| 200 | `Com_UngetToken` | function / Com_UngetToken | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_UngetToken( void ) {` |
| 213 | `Com_ParseSetMark` | function / Com_ParseSetMark | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_ParseSetMark( char **data_p, parseMark_t *mark ) {` |
| 213 | `data_p` | parameter / Com_ParseSetMark | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_ParseSetMark( char **data_p, parseMark_t *mark ) {` |
| 213 | `mark` | parameter / Com_ParseSetMark | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_ParseSetMark( char **data_p, parseMark_t *mark ) {` |
| 226 | `Com_ParseReturnToMark` | function / Com_ParseReturnToMark | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_ParseReturnToMark( char **data_p, const parseMark_t *mark ) {` |
| 226 | `data_p` | parameter / Com_ParseReturnToMark | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_ParseReturnToMark( char **data_p, const parseMark_t *mark ) {` |
| 226 | `mark` | parameter / Com_ParseReturnToMark | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_ParseReturnToMark( char **data_p, const parseMark_t *mark ) {` |
| 246 | `SkipWhitespace` | function / SkipWhitespace | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static char *SkipWhitespace( char *data, qboolean *hasNewLines ) {` |
| 246 | `data` | parameter / SkipWhitespace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static char *SkipWhitespace( char *data, qboolean *hasNewLines ) {` |
| 246 | `hasNewLines` | parameter / SkipWhitespace | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static char *SkipWhitespace( char *data, qboolean *hasNewLines ) {` |
| 247 | `c` | local / SkipWhitespace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c;` |
| 248 | `pi` | local / SkipWhitespace | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `parseInfo_t *pi;` |
| 273 | `Com_Compress` | function / Com_Compress | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_Compress( char *data_p ) {` |
| 273 | `data_p` | parameter / Com_Compress | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_Compress( char *data_p ) {` |
| 274 | `datai` | local / Com_Compress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *datai, *datao;` |
| 274 | `datao` | local / Com_Compress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *datai, *datao;` |
| 275 | `c` | local / Com_Compress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c;` |
| 276 | `size` | local / Com_Compress | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int size;` |
| 321 | `Com_GetLastTokenPos` | function / Com_GetLastTokenPos | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_GetLastTokenPos( void ) {` |
| 330 | `Com_ParseCSV` | function / Com_ParseCSV | inferred/unconfirmed spelling. Describes the recovered operation; exact instructions do not establish the historical identifier. | `static char *Com_ParseCSV( char **data_p, qboolean allowLineBreaks ) {` |
| 330 | `data_p` | parameter / Com_ParseCSV | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static char *Com_ParseCSV( char **data_p, qboolean allowLineBreaks ) {` |
| 330 | `allowLineBreaks` | parameter / Com_ParseCSV | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `static char *Com_ParseCSV( char **data_p, qboolean allowLineBreaks ) {` |
| 331 | `pi` | local / Com_ParseCSV | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `parseInfo_t *pi;` |
| 332 | `data` | local / Com_ParseCSV | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char *data;` |
| 333 | `len` | local / Com_ParseCSV | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 334 | `c` | local / Com_ParseCSV | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c;` |
| 416 | `Com_ParseExt` | function / Com_ParseExt | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_ParseExt( char **data_p, qboolean allowLineBreaks ) {` |
| 416 | `data_p` | parameter / Com_ParseExt | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_ParseExt( char **data_p, qboolean allowLineBreaks ) {` |
| 416 | `allowLineBreaks` | parameter / Com_ParseExt | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_ParseExt( char **data_p, qboolean allowLineBreaks ) {` |
| 417 | `c` | local / Com_ParseExt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char c;` |
| 418 | `len` | local / Com_ParseExt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int len;` |
| 419 | `hasNewLines` | local / Com_ParseExt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean hasNewLines = qfalse;` |
| 420 | `data` | local / Com_ParseExt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *data;` |
| 567 | `sep` | local / Com_ParseExt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `const char **sep = com_parseSeparators;` |
| 570 | `seplen` | local / Com_ParseExt | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int seplen = strlen( *sep );` |
| 571 | `i` | local / Com_ParseExt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 605 | `Com_Parse` | function / Com_Parse | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_Parse( char **data_p ) {` |
| 605 | `data_p` | parameter / Com_Parse | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_Parse( char **data_p ) {` |
| 619 | `Com_ParseOnLine` | function / Com_ParseOnLine | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_ParseOnLine( char **data_p ) {` |
| 619 | `data_p` | parameter / Com_ParseOnLine | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_ParseOnLine( char **data_p ) {` |
| 636 | `Com_MatchToken` | function / Com_MatchToken | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_MatchToken( char **data_p, const char *match, int warn ) {` |
| 636 | `data_p` | parameter / Com_MatchToken | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_MatchToken( char **data_p, const char *match, int warn ) {` |
| 636 | `match` | parameter / Com_MatchToken | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_MatchToken( char **data_p, const char *match, int warn ) {` |
| 636 | `warn` | parameter / Com_MatchToken | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_MatchToken( char **data_p, const char *match, int warn ) {` |
| 637 | `token` | local / Com_MatchToken | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *token;` |
| 659 | `Com_SkipBracedSection` | function / Com_SkipBracedSection | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_SkipBracedSection( char **data_p, int depth ) {` |
| 659 | `data_p` | parameter / Com_SkipBracedSection | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_SkipBracedSection( char **data_p, int depth ) {` |
| 659 | `depth` | parameter / Com_SkipBracedSection | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_SkipBracedSection( char **data_p, int depth ) {` |
| 660 | `token` | local / Com_SkipBracedSection | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *token;` |
| 661 | `braceLevel` | local / Com_SkipBracedSection | inferred/unconfirmed spelling. Describes a value or temporary used by the containing function. | `int braceLevel;` |
| 662 | `found` | local / Com_SkipBracedSection | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `qboolean found;` |
| 688 | `Com_SkipRestOfLine` | function / Com_SkipRestOfLine | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_SkipRestOfLine( char **data_p ) {` |
| 688 | `data_p` | parameter / Com_SkipRestOfLine | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_SkipRestOfLine( char **data_p ) {` |
| 689 | `p` | local / Com_SkipRestOfLine | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *p;` |
| 690 | `c` | local / Com_SkipRestOfLine | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int c;` |
| 711 | `Com_ParseRestOfLine` | function / Com_ParseRestOfLine | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `char *Com_ParseRestOfLine( char **data_p ) {` |
| 711 | `data_p` | parameter / Com_ParseRestOfLine | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_ParseRestOfLine( char **data_p ) {` |
| 712 | `token` | local / Com_ParseRestOfLine | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *token;` |
| 733 | `Com_ParseFloat` | function / Com_ParseFloat | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `float Com_ParseFloat( char **data_p ) {` |
| 733 | `data_p` | parameter / Com_ParseFloat | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `float Com_ParseFloat( char **data_p ) {` |
| 734 | `token` | local / Com_ParseFloat | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *token;` |
| 748 | `Com_ParseInt` | function / Com_ParseInt | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `int Com_ParseInt( char **data_p ) {` |
| 748 | `data_p` | parameter / Com_ParseInt | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `int Com_ParseInt( char **data_p ) {` |
| 749 | `token` | local / Com_ParseInt | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `char    *token;` |
| 763 | `Com_Parse1DMatrix` | function / Com_Parse1DMatrix | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Parse1DMatrix( char **data_p, int x, float *m ) {` |
| 763 | `data_p` | parameter / Com_Parse1DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse1DMatrix( char **data_p, int x, float *m ) {` |
| 763 | `x` | parameter / Com_Parse1DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse1DMatrix( char **data_p, int x, float *m ) {` |
| 763 | `m` | parameter / Com_Parse1DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse1DMatrix( char **data_p, int x, float *m ) {` |
| 764 | `i` | local / Com_Parse1DMatrix | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 778 | `Com_Parse2DMatrix` | function / Com_Parse2DMatrix | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m ) {` |
| 778 | `data_p` | parameter / Com_Parse2DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m ) {` |
| 778 | `y` | parameter / Com_Parse2DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m ) {` |
| 778 | `x` | parameter / Com_Parse2DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m ) {` |
| 778 | `m` | parameter / Com_Parse2DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m ) {` |
| 779 | `i` | local / Com_Parse2DMatrix | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |
| 795 | `Com_Parse3DMatrix` | function / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes the recovered operation; exact instructions do not establish the historical identifier. | `void Com_Parse3DMatrix( char **data_p, int z, int y, int x, float *m ) {` |
| 795 | `data_p` | parameter / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse3DMatrix( char **data_p, int z, int y, int x, float *m ) {` |
| 795 | `z` | parameter / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse3DMatrix( char **data_p, int z, int y, int x, float *m ) {` |
| 795 | `y` | parameter / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse3DMatrix( char **data_p, int z, int y, int x, float *m ) {` |
| 795 | `x` | parameter / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse3DMatrix( char **data_p, int z, int y, int x, float *m ) {` |
| 795 | `m` | parameter / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse3DMatrix( char **data_p, int z, int y, int x, float *m ) {` |
| 796 | `i` | local / Com_Parse3DMatrix | lineage token; UO binding unconfirmed. Describes a value or temporary used by the containing function. | `int i;` |

## universal/q_parse.h

| Line | Name | Kind / owner | Disclosure / reason | Declaration |
| ---: | --- | --- | --- | --- |
| 11 | `Q3MAP_Q_PARSE_H` | macro | inferred/unconfirmed spelling. Names a constant, operation or include guard in its displayed definition. | `#define Q3MAP_Q_PARSE_H` |
| 14 | `Com_ParseOnLine` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `char *Com_ParseOnLine( char **data_p );` |
| 14 | `data_p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `char *Com_ParseOnLine( char **data_p );` |
| 15 | `Com_MatchToken` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_MatchToken( char **data_p, const char *match, int warn );` |
| 15 | `data_p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_MatchToken( char **data_p, const char *match, int warn );` |
| 15 | `match` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_MatchToken( char **data_p, const char *match, int warn );` |
| 15 | `warn` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_MatchToken( char **data_p, const char *match, int warn );` |
| 16 | `Com_Parse1DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Parse1DMatrix( char **data_p, int x, float *m );` |
| 16 | `data_p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse1DMatrix( char **data_p, int x, float *m );` |
| 16 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse1DMatrix( char **data_p, int x, float *m );` |
| 16 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse1DMatrix( char **data_p, int x, float *m );` |
| 17 | `Com_Parse2DMatrix` | global/prototype | lineage token; UO binding unconfirmed. Names the declared storage or callable interface used by this file. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m );` |
| 17 | `data_p` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m );` |
| 17 | `y` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m );` |
| 17 | `x` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m );` |
| 17 | `m` | parameter | lineage token; UO binding unconfirmed. Describes an input/output role in the containing function. | `void Com_Parse2DMatrix( char **data_p, int y, int x, float *m );` |
