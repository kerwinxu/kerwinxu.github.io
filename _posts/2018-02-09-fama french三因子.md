---
layout: post
title: "Fama-French三因子"
date: "2018-02-09"
categories: ["金融", "回测交易"]
---

1. 公式：$latex R\_i=a\_i+b\_iR\_m+s\_iE(SMB)+h\_iE(HML)+\\varepsilon\_i$
2. 解析：
    1. 其中$latex R\_i=E(r\_i-r\_f)$，指股票i比起无风险投资的期望超额收益率
    2. $latex R\_M=E(r\_M-r\_f)$，为市场相对无风险投资的期望超额收益率
    3. E(SMB)是小市值公司相对大市值公司股票的期望超额收益率
    4. E(HML)则是高B/M公司股票比起低B/M的公司股票的期望超额收益率
    5. 而 $latex ε\_i$ 是回归残差项。
