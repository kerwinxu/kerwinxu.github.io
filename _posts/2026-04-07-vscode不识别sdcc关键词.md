---
layout: post
title: "vscode不识别sdcc关键词"
date: "2026-04-07"
categories: ["计算机语言", "单片机编程"]
math: true
---

我用vscode做单片机编程，插件是platformio，这个会调用sdcc编译器，但很多语法，vscoce不识别,这里给关键代码，vscode中会定义“__INTELLISENSE__”，就识别定义的一堆关键词，但sdcc没有定义“__INTELLISENSE__”，会略过。。。

```c
#ifndef __STC89C5xRC_RDP_H__
#define __STC89C5xRC_RDP_H__

/////////////////////////////////////////////////
// 为 IntelliSense 定义伪关键字
#ifdef __INTELLISENSE__
    // 定义 SDCC 特殊关键字为 IntelliSense 可理解的格式
    #define __sfr volatile unsigned char
    #define __at(x)
    #define __bit unsigned char
    #define __critical
    #define __code
    #define __data
    #define __xdata
    #define __pdata
    #define __sbit
    #define __interrupt(x)
#endif

#define _nop_  __asm nop __endasm  //定义_nop_() 用于nop


```
