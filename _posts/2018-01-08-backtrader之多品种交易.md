---
layout: post
title: "backtrader之多品种交易"
date: "2018-01-08"
categories: ["金融", "回测交易"]
---

分如下几个不同

1. 数据获取
    1. 在Cerebro中，adddata(data, name=None)，这个是包含2个参数的，一个是数据，而另一个就是数据名称啦，可以区分不同的数据。
2. 数据计算，所有的数据都保存在策略的self.datas的列表，这个data是个复数，self.datas\[0\]表示第一个数据，.name属性有数据名
3. 不同品种的仓位区分，
    1. 这个是在策略的self.positions字典中，key是self.datas\[0\],value是position对象，里边有size，price之类的。
