---
layout: post
title: "BackTrader之Strategy"
date: "2017-11-05"
categories: ["计算机语言", "Python"]
---

1. 生存周期
    1. \_\_init\_\_ : 构造函数
    2. start : 开始策略
    3. prenext
    4. next
    5. stop
2. 通知
    1.  `notify_order(order)` of any status change in an order ，任何单子状态的变化
        
    2. `notify_trade(trade)` of any opening/updating/closing trade ， 开始/更新/关闭交易的通知
        
    3.  `notify_cashvalue(cash, value)` of the current cash and portfolio in the broker ，关于当前现金或者投资组合变化的通知
        
    4.  `notify_fund(cash, value, fundvalue, shares)` of the current cash and portfolio in the broker and tradeing of fundvalue and shares ，
        
    5. Events (implementation specific) via `notify_store(msg, *args, **kwargs)`
        
3. 交易方法
    1. the `buy` method to go long or reduce/close a short position ：买入开仓
    2. the `sell` method to go short or reduce/close a long position ： 卖出开仓
    3. the `close` method to obviously close an existing position ：平仓
    4. the `cancel` method to cancel a not yet executed order ：取消还没有生效的订单
