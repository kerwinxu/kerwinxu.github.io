---
layout: post
title: "ADX: 平均趋向指标 average directional indicator"
date: "2018-01-12"
categories: ["金融", "技术指标"]
math: true
---

1. 计算 ：
    1. 计算动量变化值，Directioanl movement
        1. +DM : 当日最高价比昨日最高价高，并且当日最低价比昨日最低价高，即为上上动向+DM，上升幅度为：当日最高价减去昨日最高价。
        2. \-DM :  当日最高价比昨日最高价底，并且当日最低价比昨日最低价低，即为下降动向-DM，下降福步为：昨日最低价减去今日最低价。
    2. 计算真实波幅，TR = ∣最高价-最低价∣，∣最高价-昨收∣，∣昨收-最低价∣ 三者之中的最高值
    3. 计算动向指数，Directional Movement Index
        1. +DI(14) = +DM(14)/TR(14)\*100
        2.  -DI(14) = -DM(14)/TR(14)\*100
    4. ADX
        1. DX＝\[(+DI14)-(-DI14)\]/\[(+DI14)+(-DI14)\]\*100
        2. ADX = SMA(DX, 14) .
