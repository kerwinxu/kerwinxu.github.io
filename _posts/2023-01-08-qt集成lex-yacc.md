---
layout: post
title: "qt集成lex/yacc"
date: "2023-01-08"
categories: 
  - "c-计算机"
---

上边的文件改一下，下边的不用动。

 

```
#flex/bison sources
FLEXSOURCES += calc.l

BISONSOURCES += calc.y


#bison
bison.input = BISONSOURCES
bison.output = $$PWD/${QMAKE_FILE_BASE}_yacc.c
bison.commands = bison -d -o ${QMAKE_FILE_OUT} -p ${QMAKE_FILE_BASE}   ${QMAKE_FILE_IN}
bison.clean = $$$$PWD/${QMAKE_FILE_BASE}_yacc.c $$$$PWD/${QMAKE_FILE_BASE}_yacc.h
bison.variable_out = SOURCES
bison.CONFIG = target_predeps
QMAKE_EXTRA_COMPILERS += bison

#flex
flex.input = FLEXSOURCES
flex.output = $$PWD/${QMAKE_FILE_BASE}_lex.c
flex.commands = flex -P ${QMAKE_FILE_BASE}   -o ${QMAKE_FILE_OUT} ${QMAKE_FILE_IN}
flex.clean = ${QMAKE_FILE_OUT}
flex.variable_out = SOURCES
flex.CONFIG = target_predeps
QMAKE_EXTRA_COMPILERS += flex

```

 

重点，这个支持多个lex和yacc，他们之间不冲突是通过设置-P ${QMAKE\_FILE\_BASE} 实现的，在编写代码的时候，要注意将所有的yy改成{QMAKE\_FILE\_BASE}所代表的名字，例子如下

calc.y  calc.l

将所有的yy改成calc
