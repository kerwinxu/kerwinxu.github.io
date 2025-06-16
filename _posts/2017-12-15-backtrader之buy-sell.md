---
layout: post
title: "BackTrader之buy/sell"
date: "2017-12-15"
categories: ["金融", "回测交易"]
---

1. 属性：
    1. data ：如果为None，就用self.datas\[0\] or self.data0
    2. size ： 购买大小
    3. price ： 价格 ，如果为空，就用市价
    4. plimit ： 只有在止损单中适用
    5. exectype ，订单类型吧
        1. Order.Market or None 市价下单. A market order will be executed with the next available price. In backtesting it will be the opening price of the next bar
        2. Order.Limit ，限价单. An order which can only be executed at the given price or better
        3. Order.Stop. 止损单 An order which is triggered at price and executed like an Order.Market order
        4. Order.StopLimit 限价止损单. An order which is triggered at price and executed as an implicit Limit order with price given by pricelimit
        5. Order.Close. An order which can only be executed with the closing price of the session (usually during a closing auction)
        6. Order.StopTrail. An order which is triggered at price minus trailamount (or trailpercent) and which is updated if the price moves away from the stop
        7. Order.StopTrailLimit. An order which is triggered at price minus trailamount (or trailpercent) and which is updated if the price moves away from the stop
    6. valid ：单子有效性
        1. None: 不会失效 this generates an order that will not expire (aka Good til cancel) and remain in the market until matched or canceled. In reality brokers tend to impose a temporal limit, but this is usually so far away in time to consider it as not expiring
        2. datetime.datetime or datetime.date instance: 在有效范围内有效 the date will be used to generate an order valid until the given datetime (aka good til date)
        3. Order.DAY or 0 or timedelta(): 日内订单 a day valid until the End of the Session (aka day order) will be generated
        4. numeric value: This is assumed to be a value corresponding to a datetime in matplotlib coding (the one used by backtrader) and will used to generate an order valid until that time (good til date)
    7. tradeid ： 订单号
    8. parcent : 父订单
    9. transmit ：是否传输
    10. trailamount
    11. trailpercent
    12. \*\*kwargs ： 其他

如下是一些例子。

```
# buy the main date, with sizer default stake, Market order
order = self.buy()

# Market order - valid will be "IGNORED"
order = self.buy(valid=datetime.datetime.now() + datetime.timedelta(days=3))

# Market order - price will be IGNORED
order = self.buy(price=self.data.close[0] * 1.02)

# Market order - manual stake
order = self.buy(size=25)

# Limit order - want to set the price and can set a validity，限价单，想要一个更好的价格。
order = self.buy(exectype=Order.Limit,
                 price=self.data.close[0] * 1.02,
                 valid=datetime.datetime.now() + datetime.timedelta(days=3)))

# StopLimit order - want to set the price, price limit，止损限价单，比如说当价格跌到price，就触发一个限价订单，价格为plimit，最终成交的价格一般在price和plimit中间。
order = self.buy(exectype=Order.StopLimit,
                 price=self.data.close[0] * 1.02,
                 plimit=self.data.close[0] * 1.07)

# Canceling an existing order
self.broker.cancel(order)
```
