/* This file was generated by the Hex-Rays decompiler.
   Copyright (c) 2007-2020 Hex-Rays <info@hex-rays.com>

   Detected compiler: Visual C++
*/



//-------------------------------------------------------------------------
// Function declarations

// int __usercall sub_85@<eax>(char *a1@<edi>, int a2@<esi>); idb
// __int16 __usercall sub_1A2@<ax>(unsigned __int16 *a1@<edi>, char *a2@<esi>);

//-------------------------------------------------------------------------
// Data declarations

__int128 xmmword_210 = 0xBA00000182056F0F6600000158EC8148; // weak
__int128 xmmword_220 = 0x8D481B7B8E41B40AAA80B84800000020; // weak
__int128 xmmword_230 = 0x6F0F66202444290F2024748D4840247C; // weak


//----- (00000085) --------------------------------------------------------
int __usercall sub_85@<eax>(char *a1@<edi>, int a2@<esi>)
{
  int v2; // ecx
  unsigned int v3; // eax
  int v4; // ecx
  int v5; // eax
  int result; // eax

  v2 = 0;
  *(__m128i *)(a1 + 2) = _mm_load_si128((const __m128i *)((char *)&xmmword_210 + 4));
  *(__m128i *)(a1 + 18) = _mm_load_si128((const __m128i *)&xmmword_210);
  *(__m128i *)(a1 + 34) = _mm_load_si128((const __m128i *)((char *)&xmmword_210 + 4));
  *(__m128i *)(a1 + 50) = _mm_load_si128((const __m128i *)((char *)&xmmword_210 + 8));
  *(__m128i *)(a1 + 66) = _mm_load_si128((const __m128i *)((char *)&xmmword_210 + 12));
  *(__m128i *)(a1 + 82) = _mm_load_si128((const __m128i *)&xmmword_220);
  *(__m128i *)(a1 + 98) = _mm_load_si128((const __m128i *)((char *)&xmmword_220 + 4));
  *(__m128i *)(a1 + 114) = _mm_load_si128((const __m128i *)((char *)&xmmword_220 + 8));
  *(__m128i *)(a1 + 130) = _mm_load_si128((const __m128i *)((char *)&xmmword_220 + 12));
  *(__m128i *)(a1 + 146) = _mm_load_si128((const __m128i *)((char *)&xmmword_220 + 13));
  *(__m128i *)(a1 + 162) = _mm_load_si128((const __m128i *)((char *)&xmmword_220 + 14));
  *(__m128i *)(a1 + 178) = _mm_load_si128((const __m128i *)((char *)&xmmword_220 + 15));
  *(__m128i *)(a1 + 194) = _mm_load_si128((const __m128i *)&xmmword_230);
  *(__m128i *)(a1 + 210) = _mm_load_si128((const __m128i *)((char *)&xmmword_230 + 1));
  *(__m128i *)(a1 + 226) = _mm_load_si128((const __m128i *)((char *)&xmmword_230 + 2));
  *(__m128i *)(a1 + 242) = _mm_load_si128((const __m128i *)((char *)&xmmword_230 + 3));
  *(_WORD *)a1 = 0;
  do
  {
    v3 = v2;
    v4 = (unsigned __int8)a1[v2 + 2] - 1;
    LOBYTE(v3) = v4 + *(_BYTE *)(a2 + v3 % 0);
    v4 += 2;
    v5 = (unsigned __int8)(2 * v3);
    a1[v4 + 2] = a1[v5-- + 2];
    v2 = v4 + 1;
    a1[v5 + 2] = v2;
    result = v5 - 1;
  }
  while ( v2 != 256 );
  return result;
}
// 210: using guessed type __int128 xmmword_210;
// 220: using guessed type __int128 xmmword_220;
// 230: using guessed type __int128 xmmword_230;

//----- (000001A2) --------------------------------------------------------
__int16 __usercall sub_1A2@<ax>(unsigned __int16 *a1@<edi>, char *a2@<esi>)
{
  _BYTE *v2; // edx
  int v3; // eax
  unsigned __int8 v4; // bl
  unsigned __int16 *v5; // edi
  char v6; // al
  __int16 v7; // ax
  char *v8; // ecx
  char v9; // sp
  int v10; // eax
  char *v11; // ecx

  v2 = a1;
  v3 = *a1 - 1;
  if ( a1 )
  {
    v4 = (unsigned __int8)a1;
    v5 = a1 + 1;
    v6 = v3 - (_BYTE)a2;
    do
    {
      v2 = (char *)v5 + (unsigned __int8)(v6 + (_BYTE)a2);
      v7 = (unsigned __int8)*v2;
      v4 += v7--;
      v8 = (char *)v5 + v4;
      v9 = *v8;
      ++v9;
      *v2 = HIBYTE(v7);
      *v8 = v7;
      v10 = (unsigned __int8)(++v9 + v7);
      LOBYTE(v10) = *((_BYTE *)v5 + v10);
      *a2 ^= v10;
      v6 = v10 - 1;
      ++a2;
      v11 = v8 - 1;
    }
    while ( v11 != a2 );
    v3 = v4 + 1;
    LOBYTE(v3) = ((unsigned __int16)((_WORD)v11 + 1) >> 8) + v3;
    BYTE1(v3) = v4;
  }
  *(_DWORD *)v2 = v3;
  return v3;
}

// nfuncs=2 queued=2 decompiled=2 lumina nreq=0 worse=0 better=0
// ALL OK, 2 function(s) have been successfully decompiled