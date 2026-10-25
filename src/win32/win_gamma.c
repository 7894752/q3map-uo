/*
===========================================================================
q3map (Call of Duty: United Offensive, 2004) - source reconstruction.

Reconstructed to compile to the original binary. Distributed under the terms in
COPYING (GPL version 3 or later, with id Software's additional terms).
===========================================================================
*/

// win_gamma.c -- restore the desktop display mode and an identity gamma ramp

#include <windows.h>

/*
=============
WG_ResetGamma
=============
*/
void WG_ResetGamma( void ) {
	unsigned short ramp[3][256];
	HWND hwnd;
	HDC hdc;
	unsigned short i;

	ChangeDisplaySettings( NULL, 0 );
	hwnd = GetDesktopWindow();
	hdc = GetDC( hwnd );
	for ( i = 0; i < 256; i++ ) {
		ramp[2][i] = ramp[1][i] = ramp[0][i] = i * 257;
	}
	SetDeviceGammaRamp( hdc, ramp );
	ReleaseDC( hwnd, hdc );
}
