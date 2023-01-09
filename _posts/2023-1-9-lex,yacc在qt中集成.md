---
lang: zh
author: Kerwin
layout: post
categories: ["编程", "Qt"]
title:  lex/yacc在Qt中集成，自动编译
date:   2023-1-9
excerpt: lex/yacc在Qt中集成，自动编译
tags: [Qt, lex/yacc]
---

```
#flex/bison sources
FLEXSOURCES += calc.l
BISONSOURCES += calc.y

#bison first
bison.input = BISONSOURCES
bison.output = $$PWD/${QMAKE_FILE_BASE}_yacc.c
bison.commands = bison -d -o ${QMAKE_FILE_OUT} -p ${QMAKE_FILE_BASE}   ${QMAKE_FILE_IN}
bison.clean = $$$$PWD/${QMAKE_FILE_BASE}_yacc.c $$$$PWD/${QMAKE_FILE_BASE}_yacc.h
bison.variable_out = SOURCES
bison.CONFIG = target_predeps
QMAKE_EXTRA_COMPILERS += bison

#flex second
flex.input = FLEXSOURCES
flex.output = $$PWD/${QMAKE_FILE_BASE}_lex.c
flex.commands = flex -P ${QMAKE_FILE_BASE}   -o ${QMAKE_FILE_OUT} ${QMAKE_FILE_IN}
flex.clean = ${QMAKE_FILE_OUT}
flex.variable_out = SOURCES
flex.CONFIG = target_predeps
QMAKE_EXTRA_COMPILERS += flex
```

只要修改FLEXSOURCES和BISONSOURCES就可以了，另外请注意，因为有"-p ${QMAKE_FILE_BASE}"设置，l和y文件中的yy要改成${QMAKE_FILE_BASE}的值，这个可以一个项目中同时存在多个词法和语法分析，以这个为区分。  
比如calc.y，calc,l文件中的yylval，要改成calclval。

我的一个计算器小项目用到了如上的词法语法分析，path中有flex和bison，编译的时候自动编译了l和y文件，  [https://github.com/kerwinxu/kerwinCalculator.git](https://github.com/kerwinxu/kerwinCalculator.git)