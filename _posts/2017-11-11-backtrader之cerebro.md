---
layout: post
title: "backtrader之Cerebro"
date: "2017-11-11"
categories: 
  - "python"
  - "回测交易"
---

3. 总体
4. 整理输入：
    1. 添加金融数据。adddata
    2. 添加策略，可以添加策略的参数，cerebro.addstrategy(MyStrategy, myparam1=value1, myparam2=value2)
    3. addwriter ？
    4. 添加分析师，分析结果的。addanalyzer
    5. addobserver (or addobservermulti)
    6. 添加证券商经纪人，不用默认。
    7. 接收通知，方法：
        1. 通过addnotifycallback(callback)添加回调函数。
        2. 重载策略的notify\_store 方法
        3. 重载Cerebro的notify\_store 方法。
5. 运行，result = cerebro.run(\*\*kwargs)
6. 显示图表，cerebro.plot()
7. 参数：
8. 方法：
    1. addstorecb(callback)，
    2. notify\_store(msg, \*args, \*\*kwargs)，
    3. adddatacb(callback)
    4. notify\_data(data, status, \*args, \*\*kwargs)
    5. adddata(data, name=None)，添加数据
    6. resampledata(dataname, name=None, \*\*kwargs)，重新取样的数据。
    7. replaydata(dataname, name=None, \*\*kwargs)
    8. chaindata(\*args, \*\*kwargs)，、
    9. rolloverdata(\*args, \*\*kwargs)
    10. addstrategy(strategy, \*args, \*\*kwargs) ，添加策略。
    11. optstrategy(strategy, \*args, \*\*kwargs) ，添加寻找最优参数。
    12. optcallback(cb) ，
    13.  addindicator(indcls, \*args, \*\*kwargs)，添加指标。
    14. addobserver(obscls, \*args, \*\*kwargs)，添加观察者。
    15. addobservermulti(obscls, \*args, \*\*kwargs)
    16. addanalyzer(ancls, \*args, \*\*kwargs) ，添加分析师
    17. addwriter(wrtcls, \*args, \*\*kwargs)
    18. run(\*\*kwargs)
    19. runstop()
    20. setbroker(broker) ，设置经纪人。
    21. getbroker() ，获取经纪人。
    22. plot(plotter=None, numfigs=1, iplot=True, start=None, end=None, width=16, height=9, dpi=300, tight=True, use=None, \*\*kwargs) 图表啦
    23. addsizer(sizercls, \*args, \*\*kwargs) ，交易尺寸
    24. addsizer\_byidx(idx, sizercls, \*args, \*\*kwargs)
    25. add\_signal(sigtype, sigcls, \*sigargs, \*\*sigkwargs)
    26. signal\_concurrent(onoff)
    27. signal\_accumulate(onoff)
    28. signal\_strategy(stratcls, \*args, \*\*kwargs)
    29. addcalendar(cal)
    30. addtz(tz)
    31. add\_timer(when, offset=datetime.timedelta(0), repeat=datetime.timedelta(0), weekdays=\[\], weekcarry=False, monthdays=\[\], monthcarry=True, allow=None, tzdata=None, cheat=False, \*args, \*\*kwargs)
    32. notify\_timer(timer, when, \*args, \*\*kwargs)
    33. add\_order\_history(orders, notify=True)
