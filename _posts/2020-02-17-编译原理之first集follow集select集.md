---
layout: post
title: "编译原理之First集,Follow集,Select集"
date: "2020-02-17"
categories: 
  - "编译原理"
---

# First 集

## 定义

First(X) ： 可以从X推导出的串首终结符构成的集合，如果 $latex X \\Rightarrow^\* \\epsilon $，那么$latex \\epsilon \\in First(X)$

## 算法

- 不断的应用下列规则，直到没有新的终结符或$latex \\epsilon$可以被加入任何First集合为止。
    - 如果X是一个终结符，那么First(X) = {X}
    - 如果X是一个非终结符，且 $latex X \\rightarrow Y\_1\\cdots Y\_k \\in P (k\\ge 1)$，那么对于某个i，a在$latex First(Y\_i)$中，且 $latex \\epsilon$在所有的$latex First(Y\_1),\\cdots,First(Y\_{i-1})中（即Y\_1\\cdots Y\_{i-1}\\Rightarrow^\* \\epsilon)$,就将a加入到First(X)中，
        - 如果对于所有的$latex j = 1,2,\\cdots,k$,$latex \\epsilon$在$latex First(Y\_j)$中，就将 $latex \\epsilon $加入到 First(X)中
    - 如果 $latex X \\rightarrow \\epsilon \\in P$,那么就将$latex \\epsilon$加入到 First(X)中。
        - 意思是X存在空产生式。

# Follow集

## 定义

Follow（A）：可能在某个句型中紧跟着A后边的终结符a的集合

$latex Follow(A) = \\{a | S \\Rightarrow^\* \\alpha A a \\beta , a\\in V\_T,\\alpha,\\beta \\in (V\_T\\cup V\_N)^\*\\}$

如果A是某个句型的最右符号，则将结束符 "$"添加到Follow(A)中。

## 算法

- 不断应用下列规则，直到没有新的终结符可以被加入到任何Follow集合中为止。
    - 将 $ 放入 Follow(S)中，
        - S是开始符号
        - $是输入右端的结束标记
    - 如果存在一个产生式  $latex A \\rightarrow \\alpha B \\beta$，那么$latex First(\\beta)$中除了$latex \\epsilon$之外的所有符号都在Follow(B)中。
    - 如果存在一个产生式 $latex A \\rightarrow \\alpha B$，或存在产生式  $latex A\\rightarrow \\alpha B \\ beta 且 First(\\beta)包含 \\epsilon$，那么Follow(A)中的所有符号都在Follow(B)中。
