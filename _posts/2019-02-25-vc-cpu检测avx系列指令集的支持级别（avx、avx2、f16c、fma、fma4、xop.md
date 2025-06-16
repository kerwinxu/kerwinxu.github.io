---
layout: post
title: "[VC] cpu检测AVX系列指令集的支持级别（AVX、AVX2、F16C、FMA、FMA4、XOP）"
date: "2019-02-25"
categories: ["计算机语言", "asm"]
---

从2011年的Sandy Bridge微架构处理器开始，现在支持AVX系列指令集的处理器越来越多了。本文探讨如何用VC编写检测AVX系列指令集的程序，并利用了先前的CPUIDFIELD方案。

# AVX系列指令集简介

SSE5 指令：SSE5 是一个纸面上的指令集，并没有最终实现，AMD 在 2007 年 8 月公布 SSE5 指令集规范，在 2009 年 5 月 AMD 推出了 XOP，FMA4 以及 CVT16 来取代 SSE5 指令。 AVX 指令：2008 年 3 月 Intel 发布了 AVX（Advanced Vector Extensions）指令集规范，首次在 Sandy Bridge 微架构的处理器上使用。AMD 首次在 Bulldozer 微架构的处理器上加入 AVX 指令的支持。 FMA 指令：FMA 指令是 AVX 指令集中的一部分，Intel 将在 2013 年的 Haswell 微架构处理器上使用。据说AMD将在2012年的Piledriver微架构处理器上支持FMA。 XOP，FMA4 以及 CVT16 指令：AMD 在 2009 年 5 月发布了 XOP，FMA4 以及 CVT16 指令集规范，这些指令集取代了 SSE5 指令，在原有的 SSE5 指令基础上，使用了兼容 AVX 指令的设计方案重新进行了设计，因此，XOP，FMA4 以及 CVT16 在指令的编码方面是兼容于 AVX 的方案。这使得 AVX/FAM4/CVT16 指令与 AVX 指令同时存在，而不会产生冲突。AMD首次在 Bulldozer 微架构的处理器上使用。 F16C 指令：F16C指令就是AMD的CVT16指令，Intel换了一个名称，随后AMD也接收了这一称呼。Intel 首次在 2012 年的 Ivy Bridge 微架构处理器上使用。 AVX2 指令：2011 年 6 月，Intel 发布了 AVX2 指令集规范，将在 2013 年的 Haswell 微架构处理器上使用。

# 检测AVX、AVX2

2.1 应用程序如何检测AVX 在Intel手册第一卷的“13.5 DETECTION OF AVX INSTRUCTIONS”中介绍了AVX指令集的检测办法，具体步骤为—— 1) Detect CPUID.1:ECX.OSXSAVE\[bit 27\] = 1 (XGETBV enabled for application use) 2) Issue XGETBV and verify that XCR0\[2:1\] = ‘11b’ (XMM state and YMM state are enabled by OS). 3) detect CPUID.1:ECX.AVX\[bit 28\] = 1 (AVX instructions supported). (Step 3 can be done in any order relative to 1 and 2)

Intel还给出了汇编伪代码——

```
INT supports_AVX()
{	mov eax, 1
	cpuid
	and ecx, 018000000H
	cmp ecx, 018000000H; check both OSXSAVE and AVX feature flags
	jne not_supported
	; processor supports AVX instructions and XGETBV is enabled by OS
	mov ecx, 0; specify 0 for XCR0 register
	XGETBV ; result in EDX:EAX
	and eax, 06H
	cmp eax, 06H; check OS has enabled both XMM and YMM state support
	jne not_supported
	mov eax, 1
	jmp done
NOT_SUPPORTED:
	mov eax, 0
done:


```

解释一下它的检测步骤—— 1) 检测CPUID.1:ECX.OSXSAVE\[bit 27\] = 1。该位为1表示操作系统支持XSAVE系列指令，于是在应用程序中可以使用XGETBV等XSAVE系列指令。 2) 使用XGETBV指令获取XCR0寄存器的值，并检查第1位至第2位是否都为1。即检查操作系统是否支持XMM和YMM状态。 3) 检测CPUID.1:ECX.OSXSAVE\[bit 27\] = 1。该位为1表示硬件支持AVX指令集。

XCR0叫做XFEATURE\_ENABLED\_MASK寄存器，它是一个64位寄存器。它的第0位是x87 FPU/MMX状态，第1位是XMM状态，第2位是YMM状态。如果操作系统支持AVX指令集，它就会将XMM和YMM状态均置为1。详见Intel手册第3卷的“2.6 EXTENDED CONTROL REGISTERS (INCLUDING XCR0)”——

AMD对XCR0寄存器做了扩展，第62位是LWP状态。详见AMD手册第3卷的“11.5.2 XFEATURE\_ENABLED\_MASK”——

2.2 应用程序如何检测AVX2 在《Intel® Architecture Instruction Set Extensions Programming Reference》的“2.2.3 Detection of AVX2”中介绍了AVX2指令集的检测方法和汇编伪代码，摘录如下——

Hardware support for AVX2 is indicated by CPUID.(EAX=07H,ECX=0H):EBX.AVX2\[bit 5\]=1. Application Software must identify that hardware supports AVX as explained in Section 2.2, after that it must also detect support for AVX2 by checking CPUID.(EAX=07H, ECX=0H):EBX.AVX2\[bit 5\]. The recommended pseudocode sequence for detection of AVX2 is:

```
INT supports_avx2()
{	; result in eax
	mov eax, 1
	cpuid
	and ecx, 018000000H
	cmp ecx, 018000000H; check both OSXSAVE and AVX feature flags
	jne not_supported
	; processor supports AVX instructions and XGETBV is enabled by OS
	mov eax, 7
	mov ecx, 0
	cpuid
	and ebx, 20H
	cmp ebx, 20H; check AVX2 feature flags
	jne not_supported
	mov ecx, 0; specify 0 for XFEATURE_ENABLED_MASK register
	XGETBV; result in EDX:EAX
	and eax, 06H
	cmp eax, 06H; check OS has enabled both XMM and YMM state support
	jne not_supported
	mov eax, 1
	jmp done
NOT_SUPPORTED:
	mov eax, 0
done:
}


```

可以看出，它是通过三个步奏来检查AVX2指令集的—— 1) 使用cpuid指令的功能1，检测OSXSAVE和AVX标志。 2) 使用cpuid指令的功能7，检测AVX2标志。 3) 使用XGETBV指令获取XCR0寄存器的值，判断操作系统是否支持XMM和YMM状态。

 

2.3 如何获取XCR0寄存器的值 官方推荐使用XGETBV指令来获取XCR0寄存器的值。输入寄存器是ECX，是XCR系列寄存器的索引，对于XCR0来说应填0。输出寄存器是EDX和EAX，分别是高32位和低32位。 XGETBV指令是在任何访问级别均可调用的指令，即在Ring3的应用程序层也可使用XGETBV指令。 虽然应用程序层可以使用XGETBV指令，但在实际使用时会遇到问题。这是因为XGETBV是最近才出现的指令，大多数编译器还不支持XGETBV指令。 该怎么办呢？

cpuid的0Dh号功能（Processor Extended State Enumeration）就是为这种情况设计的。当使用功能号0Dh、子功能号0调用cpuid指令时，返回的EDX和EAX就是XCR0的值。

2.4 编写检测函数 前面我们看到了Intel的检测AVX与AVX2的汇编伪代码。虽然将其直接翻译为VC中的内嵌汇编并不复杂，但存在两个问题—— 1. VC在x64平台不支持内嵌汇编； 2. 使用不方便。它比较适合在编写汇编代码时使用，但对于C语言程序来说，我们希望能以更好的方式组织代码。

这时可以参考先前的simd\_sse\_level函数的设计，函数的返回值是操作系统对AVX指令集的支持级别，还提供一个指针参数来接收硬件对AVX指令集的支持级别。于是，定义了这些常数—— #define SIMD\_AVX\_NONE 0 // 不支持 #define SIMD\_AVX\_1 1 // AVX #define SIMD\_AVX\_2 2 // AVX2

我们可以利用先前的CPUIDFIELD方案来简化检测代码的编写。先定义好相关的常数—— #define CPUF\_AVX CPUIDFIELD\_MAKE(1,0,2,28,1) #define CPUF\_AVX2 CPUIDFIELD\_MAKE(7,0,1,5,1) #define CPUF\_XSAVE CPUIDFIELD\_MAKE(1,0,2,26,1) #define CPUF\_OSXSAVE CPUIDFIELD\_MAKE(1,0,2,27,1) #define CPUF\_XFeatureSupportedMaskLo CPUIDFIELD\_MAKE(0xD,0,0,0,32)

在编写具体的检测代码时，没必要拘泥于官方的那三个步骤，可以先检查硬件支持性，然后再检查操作系统支持性。函数代码如下——

```
int	simd_avx_level(int* phwavx)
{
	int	rt = SIMD_AVX_NONE;	// result
 
	// check processor support
	if (0!=getcpuidfield(CPUF_AVX))
	{
		rt = SIMD_AVX_1;
		if (0!=getcpuidfield(CPUF_AVX2))
		{
			rt = SIMD_AVX_2;
		}
	}
	if (NULL!=phwavx)	*phwavx=rt;
 
	// check OS support
	if (0!=getcpuidfield(CPUF_OSXSAVE))	// XGETBV enabled for application use.
	{
		UINT32 n = getcpuidfield(CPUF_XFeatureSupportedMaskLo);	// XCR0: XFeatureSupportedMask register.
		if (6==(n&6))	// XCR0[2:1] = ‘11b’ (XMM state and YMM state are enabled by OS).
		{
			return rt;
		}
	}
	return SIMD_AVX_NONE;
}

```

# 检测F16C、FMA、FMA4、XOP

 

在《Intel® Architecture Instruction Set Extensions Programming Reference》的“2.2.1 Detection of FMA”中介绍了FMA指令的检测方法和汇编伪代码，摘录如下——

Hardware support for FMA is indicated by CPUID.1:ECX.FMA\[bit 12\]=1. Application Software must identify that hardware supports AVX as explained in Section 2.2, after that it must also detect s

```
INT supports_fma()
{	; result in eax
	mov eax, 1
	cpuid
	and ecx, 018001000H
	cmp ecx, 018001000H; check OSXSAVE, AVX, FMA feature flags
	jne not_supported
	; processor supports AVX,FMA instructions and XGETBV is enabled by OS
	mov ecx, 0; specify 0 for XFEATURE_ENABLED_MASK register
	XGETBV; result in EDX:EAX
	and eax, 06H
	cmp eax, 06H; check OS has enabled both XMM and YMM state support
	jne not_supported
	mov eax, 1
	jmp done
NOT_SUPPORTED:
	mov eax, 0
done:
}


```

Note that FMA comprises 256-bit and 128-bit SIMD instructions operating on YMM states. 可以看出上面的代码与AVX2的检测代码很相似，只是多了对FMA标志位的检查。 所以我们可以将其分解为两个步骤，先调用simd\_avx\_level检查AVX的支持性，然后再调用getcpuidfield检查硬件是否支持FMA，即这样的代码——

if (simd\_avx\_level(NULL)>0) { if (getcpuidfield(CPUF\_FMA)) { 支持FMA } }

这样就只需定义F16C、FMA、FMA4、XOP的常数就够了—— #define CPUF\_F16C CPUIDFIELD\_MAKE(1,0,2,29,1) #define CPUF\_FMA CPUIDFIELD\_MAKE(1,0,2,12,1) #define CPUF\_FMA4 CPUIDFIELD\_MAKE(0x80000001,0,2,16,1) #define CPUF\_XOP CPUIDFIELD\_MAKE(0x80000001,0,2,11,1) ---------------------

# 全部代码

 

```
#include 
#include 
#include 
#include 
 
#if _MSC_VER >=1400	// VC2005才支持intrin.h
#include 	// 所有Intrinsics函数
#else
#include 	// MMX, SSE, SSE2
#endif
 
 
// CPUIDFIELD
typedef INT32 CPUIDFIELD;
 
#define  CPUIDFIELD_MASK_POS	0x0000001F	// 位偏移. 0~31.
#define  CPUIDFIELD_MASK_LEN	0x000003E0	// 位长. 1~32
#define  CPUIDFIELD_MASK_REG	0x00000C00	// 寄存器. 0=EAX, 1=EBX, 2=ECX, 3=EDX.
#define  CPUIDFIELD_MASK_FIDSUB	0x000FF000	// 子功能号(低8位).
#define  CPUIDFIELD_MASK_FID	0xFFF00000	// 功能号(最高4位 和 低8位).
 
#define CPUIDFIELD_SHIFT_POS	0
#define CPUIDFIELD_SHIFT_LEN	5
#define CPUIDFIELD_SHIFT_REG	10
#define CPUIDFIELD_SHIFT_FIDSUB	12
#define CPUIDFIELD_SHIFT_FID	20
 
#define CPUIDFIELD_MAKE(fid,fidsub,reg,pos,len)	(((fid)&0xF0000000) \
	| ((fid)<>CPUIDFIELD_SHIFT_FID) )
#define CPUIDFIELD_FIDSUB(cpuidfield)	( ((cpuidfield) & CPUIDFIELD_MASK_FIDSUB)>>CPUIDFIELD_SHIFT_FIDSUB )
#define CPUIDFIELD_REG(cpuidfield)	( ((cpuidfield) & CPUIDFIELD_MASK_REG)>>CPUIDFIELD_SHIFT_REG )
#define CPUIDFIELD_POS(cpuidfield)	( ((cpuidfield) & CPUIDFIELD_MASK_POS)>>CPUIDFIELD_SHIFT_POS )
#define CPUIDFIELD_LEN(cpuidfield)	( (((cpuidfield) & CPUIDFIELD_MASK_LEN)>>CPUIDFIELD_SHIFT_LEN) + 1 )
 
// 取得位域
#ifndef __GETBITS32
#define __GETBITS32(src,pos,len)	( ((src)>>(pos)) & (((UINT32)-1)>>(32-len)) )
#endif
 
 
#define CPUF_SSE4A	CPUIDFIELD_MAKE(0x80000001,0,2,6,1)
#define CPUF_AES	CPUIDFIELD_MAKE(1,0,2,25,1)
#define CPUF_PCLMULQDQ	CPUIDFIELD_MAKE(1,0,2,1,1)
 
#define CPUF_AVX	CPUIDFIELD_MAKE(1,0,2,28,1)
#define CPUF_AVX2	CPUIDFIELD_MAKE(7,0,1,5,1)
#define CPUF_OSXSAVE	CPUIDFIELD_MAKE(1,0,2,27,1)
#define CPUF_XFeatureSupportedMaskLo	CPUIDFIELD_MAKE(0xD,0,0,0,32)
#define CPUF_F16C	CPUIDFIELD_MAKE(1,0,2,29,1)
#define CPUF_FMA	CPUIDFIELD_MAKE(1,0,2,12,1)
#define CPUF_FMA4	CPUIDFIELD_MAKE(0x80000001,0,2,16,1)
#define CPUF_XOP	CPUIDFIELD_MAKE(0x80000001,0,2,11,1)
 
 
// SSE系列指令集的支持级别. simd_sse_level 函数的返回值。
#define SIMD_SSE_NONE	0	// 不支持
#define SIMD_SSE_1	1	// SSE
#define SIMD_SSE_2	2	// SSE2
#define SIMD_SSE_3	3	// SSE3
#define SIMD_SSE_3S	4	// SSSE3
#define SIMD_SSE_41	5	// SSE4.1
#define SIMD_SSE_42	6	// SSE4.2
 
const char*	simd_sse_names[] = {
	"None",
	"SSE",
	"SSE2",
	"SSE3",
	"SSSE3",
	"SSE4.1",
	"SSE4.2",
};
 
 
// AVX系列指令集的支持级别. simd_avx_level 函数的返回值。
#define SIMD_AVX_NONE	0	// 不支持
#define SIMD_AVX_1	1	// AVX
#define SIMD_AVX_2	2	// AVX2
 
const char*	simd_avx_names[] = {
	"None",
	"AVX",
	"AVX2"
};
 
 
 
char szBuf[64];
INT32 dwBuf[4];
 
#if defined(_WIN64)
// 64位下不支持内联汇编. 应使用__cpuid、__cpuidex等Intrinsics函数。
#else
#if _MSC_VER < 1600	// VS2010. 据说VC2008 SP1之后才支持__cpuidex
void __cpuidex(INT32 CPUInfo[4], INT32 InfoType, INT32 ECXValue)
{
	if (NULL==CPUInfo)	return;
	_asm{
		// load. 读取参数到寄存器
		mov edi, CPUInfo;	// 准备用edi寻址CPUInfo
		mov eax, InfoType;
		mov ecx, ECXValue;
		// CPUID
		cpuid;
		// save. 将寄存器保存到CPUInfo
		mov	[edi], eax;
		mov	[edi+4], ebx;
		mov	[edi+8], ecx;
		mov	[edi+12], edx;
	}
}
#endif	// #if _MSC_VER < 1600	// VS2010. 据说VC2008 SP1之后才支持__cpuidex
 
#if _MSC_VER < 1400	// VC2005才支持__cpuid
void __cpuid(INT32 CPUInfo[4], INT32 InfoType)
{
	__cpuidex(CPUInfo, InfoType, 0);
}
#endif	// #if _MSC_VER < 1400	// VC2005才支持__cpuid
 
#endif	// #if defined(_WIN64)
 
// 根据CPUIDFIELD从缓冲区中获取字段.
UINT32	getcpuidfield_buf(const INT32 dwBuf[4], CPUIDFIELD cpuf)
{
	return __GETBITS32(dwBuf[CPUIDFIELD_REG(cpuf)], CPUIDFIELD_POS(cpuf), CPUIDFIELD_LEN(cpuf));
}
 
// 根据CPUIDFIELD获取CPUID字段.
UINT32	getcpuidfield(CPUIDFIELD cpuf)
{
	INT32 dwBuf[4];
	__cpuidex(dwBuf, CPUIDFIELD_FID(cpuf), CPUIDFIELD_FIDSUB(cpuf));
	return getcpuidfield_buf(dwBuf, cpuf);
}
 
// 取得CPU厂商（Vendor）
//
// result: 成功时返回字符串的长度（一般为12）。失败时返回0。
// pvendor: 接收厂商信息的字符串缓冲区。至少为13字节。
int cpu_getvendor(char* pvendor)
{
	INT32 dwBuf[4];
	if (NULL==pvendor)	return 0;
	// Function 0: Vendor-ID and Largest Standard Function
	__cpuid(dwBuf, 0);
	// save. 保存到pvendor
	*(INT32*)&pvendor[0] = dwBuf[1];	// ebx: 前四个字符
	*(INT32*)&pvendor[4] = dwBuf[3];	// edx: 中间四个字符
	*(INT32*)&pvendor[8] = dwBuf[2];	// ecx: 最后四个字符
	pvendor[12] = '\0';
	return 12;
}
 
// 取得CPU商标（Brand）
//
// result: 成功时返回字符串的长度（一般为48）。失败时返回0。
// pbrand: 接收商标信息的字符串缓冲区。至少为49字节。
int cpu_getbrand(char* pbrand)
{
	INT32 dwBuf[4];
	if (NULL==pbrand)	return 0;
	// Function 0x80000000: Largest Extended Function Number
	__cpuid(dwBuf, 0x80000000);
	if (dwBuf[0] < 0x80000004)	return 0;
	// Function 80000002h,80000003h,80000004h: Processor Brand String
	__cpuid((INT32*)&pbrand[0], 0x80000002);	// 前16个字符
	__cpuid((INT32*)&pbrand[16], 0x80000003);	// 中间16个字符
	__cpuid((INT32*)&pbrand[32], 0x80000004);	// 最后16个字符
	pbrand[48] = '\0';
	return 48;
}
 
 
// 是否支持MMX指令集
BOOL	simd_mmx(BOOL* phwmmx)
{
	const INT32	BIT_D_MMX = 0x00800000;	// bit 23
	BOOL	rt = FALSE;	// result
	INT32 dwBuf[4];
 
	// check processor support
	__cpuid(dwBuf, 1);	// Function 1: Feature Information
	if ( dwBuf[3] & BIT_D_MMX )	rt=TRUE;
	if (NULL!=phwmmx)	*phwmmx=rt;
 
	// check OS support
	if ( rt )
	{
#if defined(_WIN64)
		// VC编译器不支持64位下的MMX。
		rt=FALSE;
#else
		__try 
		{
			_mm_empty();	// MMX instruction: emms
		}
		__except (EXCEPTION_EXECUTE_HANDLER)
		{
			rt=FALSE;
		}
#endif	// #if defined(_WIN64)
	}
 
	return rt;
}
 
// 检测SSE系列指令集的支持级别
int	simd_sse_level(int* phwsse)
{
	const INT32	BIT_D_SSE = 0x02000000;	// bit 25
	const INT32	BIT_D_SSE2 = 0x04000000;	// bit 26
	const INT32	BIT_C_SSE3 = 0x00000001;	// bit 0
	const INT32	BIT_C_SSSE3 = 0x00000100;	// bit 9
	const INT32	BIT_C_SSE41 = 0x00080000;	// bit 19
	const INT32	BIT_C_SSE42 = 0x00100000;	// bit 20
	int	rt = SIMD_SSE_NONE;	// result
	INT32 dwBuf[4];
 
	// check processor support
	__cpuid(dwBuf, 1);	// Function 1: Feature Information
	if ( dwBuf[3] & BIT_D_SSE )
	{
		rt = SIMD_SSE_1;
		if ( dwBuf[3] & BIT_D_SSE2 )
		{
			rt = SIMD_SSE_2;
			if ( dwBuf[2] & BIT_C_SSE3 )
			{
				rt = SIMD_SSE_3;
				if ( dwBuf[2] & BIT_C_SSSE3 )
				{
					rt = SIMD_SSE_3S;
					if ( dwBuf[2] & BIT_C_SSE41 )
					{
						rt = SIMD_SSE_41;
						if ( dwBuf[2] & BIT_C_SSE42 )
						{
							rt = SIMD_SSE_42;
						}
					}
				}
			}
		}
	}
	if (NULL!=phwsse)	*phwsse=rt;
 
	// check OS support
	__try 
	{
		__m128 xmm1 = _mm_setzero_ps();	// SSE instruction: xorps
		if (0!=*(int*)&xmm1)	rt = SIMD_SSE_NONE;	// 避免Release模式编译优化时剔除上一条语句
	}
	__except (EXCEPTION_EXECUTE_HANDLER)
	{
		rt = SIMD_SSE_NONE;
	}
 
	return rt;
}
 
// 检测AVX系列指令集的支持级别.
int	simd_avx_level(int* phwavx)
{
	int	rt = SIMD_AVX_NONE;	// result
 
	// check processor support
	if (0!=getcpuidfield(CPUF_AVX))
	{
		rt = SIMD_AVX_1;
		if (0!=getcpuidfield(CPUF_AVX2))
		{
			rt = SIMD_AVX_2;
		}
	}
	if (NULL!=phwavx)	*phwavx=rt;
 
	// check OS support
	if (0!=getcpuidfield(CPUF_OSXSAVE))	// XGETBV enabled for application use.
	{
		UINT32 n = getcpuidfield(CPUF_XFeatureSupportedMaskLo);	// XCR0: XFeatureSupportedMask register.
		if (6==(n&6))	// XCR0[2:1] = ‘11b’ (XMM state and YMM state are enabled by OS).
		{
			return rt;
		}
	}
	return SIMD_AVX_NONE;
}
 
 
 
int _tmain(int argc, _TCHAR* argv[])
{
	int i;
 
	//__cpuidex(dwBuf, 0,0);
	//__cpuid(dwBuf, 0);
	//printf("%.8X\t%.8X\t%.8X\t%.8X\n", dwBuf[0],dwBuf[1],dwBuf[2],dwBuf[3]);
 
	cpu_getvendor(szBuf);
	printf("CPU Vendor:\t%s\n", szBuf);
 
	cpu_getbrand(szBuf);
	printf("CPU Name:\t%s\n", szBuf);
 
	BOOL bhwmmx;	// 硬件支持MMX.
	BOOL bmmx;	// 操作系统支持MMX.
	bmmx = simd_mmx(&bhwmmx);
	printf("MMX: %d\t// hw: %d\n", bmmx, bhwmmx);
 
	int	nhwsse;	// 硬件支持SSE.
	int	nsse;	// 操作系统支持SSE.
	nsse = simd_sse_level(&nhwsse);
	printf("SSE: %d\t// hw: %d\n", nsse, nhwsse);
	for(i=1; i<sizeof(simd_sse_names)/sizeof(simd_sse_names[0]); ++i) { if (nhwsse>=i)	printf("\t%s\n", simd_sse_names[i]);
	}
 
	// test SSE4A/AES/PCLMULQDQ
	printf("SSE4A: %d\n", getcpuidfield(CPUF_SSE4A));
	printf("AES: %d\n", getcpuidfield(CPUF_AES));
	printf("PCLMULQDQ: %d\n", getcpuidfield(CPUF_PCLMULQDQ));
 
	// test AVX
	int	nhwavx;	// 硬件支持AVX.
	int	navx;	// 操作系统支持AVX.
	navx = simd_avx_level(&nhwavx);
	printf("AVX: %d\t// hw: %d\n", navx, nhwavx);
	for(i=1; i<sizeof(simd_avx_names)/sizeof(simd_avx_names[0]); ++i) { if (nhwavx>=i)	printf("\t%s\n", simd_avx_names[i]);
	}
 
	// test F16C/FMA/FMA4/XOP
	printf("F16C: %d\n", getcpuidfield(CPUF_F16C));
	printf("FMA: %d\n", getcpuidfield(CPUF_FMA));
	printf("FMA4: %d\n", getcpuidfield(CPUF_FMA4));
	printf("XOP: %d\n", getcpuidfield(CPUF_XOP));
 
	return 0;
}

```
