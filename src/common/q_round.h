/*
===========================================================================
q3map (Call of Duty: United Offensive, 2004).

Distributed under the terms in
COPYING (GPL version 3 or later, with id Software's additional terms).
===========================================================================
*/

// q_round.h -- biased x87 float to int rounding helpers
//
// The bias constants are 0.5 - 2^-30 (floor, ceil) and 2^-30 (nearest); fistp
// rounds with the current mode (round to nearest even), so these are not C casts.

#ifndef Q_ROUND_H
#define Q_ROUND_H

__inline int FloorToInt( float value ) {
	double bias = 0.49999999906867743;
	int result;
	__asm {
		fld value
		fsub bias
		fistp result
	}
	return result;
}

__inline int CeilToInt( float value );
__inline int RoundToInt( float value ) {
	int result;
	double bias = 9.31322574615478515625e-10;
	__asm {
		fld value
		fadd bias
		fistp result
	}
	return result;
}

#endif
