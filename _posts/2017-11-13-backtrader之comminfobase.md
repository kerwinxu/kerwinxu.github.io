---
layout: post
title: "backtrader之CommInfoBase"
date: "2017-11-13"
categories: 
  - "python"
  - "回测交易"
---

1. 属性：
    1. commission ： (def: 0.0) 佣金，（百分比或者固定佣金）
    2. margin ： 保证金(def: None)
        1. 如果为None，commission 为比率
        2. 如果为数字，表示期货的保证金，期货的佣金就是固定的数字。
    3. automargin ：自动保证金(def: False):
        1. 如果automargin就使用margin
        2. 如果automargin < 0 ，佣金计算方法是mult \* price
        3. 如果automargin > 0 ，佣金计算方法是 automargin \* price
    4. mult ：乘数(def 1.0):
    5. commtype ： (def: None):
        1. CommInfoBase.COMM\_PERC ，为%
        2. CommInfoBase.COMM\_FIXED ，表示固定的数字。
    6. stocklike：(def: False)，表明这个是股票还是期货。
    7. percabs ： (def: False) ，当commtype 为CommInfoBase.COMM\_PERC 时，表明commission 参数是XX% or 0.XX 。
    8. interest ：年息，比如用绝对值表示， 比如说0.05，表示5%的年息。
    9. interest\_long ：
    10. leverage ： 杠杆，
