---
layout: post
title: "backtrader之cash,value"
date: "2017-12-18"
categories: ["金融", "回测交易"]
---

我首笔交易是个卖单，5000元原始资金，15%保证金，结果出现如下结果

2008-10-08, SELL EXECUTED, -1, Price: 2877.00, Value: -2877.00, Comm : 2.30 , current value : 4994.70 , current cash : 7874.70

value好像没问题，但cash出现问题了，cash差不多是5000+2877，

平仓的时候，

2008-12-22, BUY EXECUTED, 1, Price: 2460.00, Value: -2877.00, Comm : 45.12, current value : 5369.58, current cash : 5369.58

好像又正常了。

 

或许我要查看一下代码，看一下cash和value到底有什么区别。
