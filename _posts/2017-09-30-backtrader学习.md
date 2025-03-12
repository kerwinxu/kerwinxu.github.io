---
title: "backtrader学习"
date: "2017-09-30"
categories: 
  - "回测交易"
---

backtrader分成如下几个部分：

1. Cerebro ： 字面意思是大脑，就是由这个来运行策略的。bt.Cerebro
2. Data Feed ： 数据，在这里可以是CSV文件，可以是本地，也可以是下载的。
    1. 这个数据读取操作是在"bt.feeds"中，可以读取很多数据。
        1. blaze
        2. btcsv
        3. chainer
        4. csvgeneric
        5. ibdata
        6. influxfeed
        7. mt4csv
        8. oanda
        9. pandafeed :  PandasData
        10. quandl
        11. rollover
        12. sierrachart
        13. vcdata
        14. vchart
        15. vchartcsv
        16. vchartfile
        17. yahoo : YahooFinanceCSVData
    2. 如下是读取数据
        
        ```
            # Create a Data Feed
            data = bt.feeds.YahooFinanceCSVData(
                dataname=datapath,
                # Do not pass values before this date
                fromdate=datetime.datetime(2000, 1, 1),
                # Do not pass values after this date
                todate=datetime.datetime(2000, 12, 31),
                reverse=False)
        
            # Add the Data Feed to Cerebro
            cerebro.adddata(data)
        ```
        
    3. 其他
3. Strategy ： 策略，
    1. 包含如下几个部分：
        1. \_\_init\_\_ ：这个所有的python都包含的，构造函数，
        2. next ： 每个周期都调用这个函数。
    2. 属性：
        1. `env`: the cerebro entity in which this Strategy lives 哪个策略在活跃。
            
        2. `datas`: array of data feeds which have been passed to cerebro 数据。
            
            - `data/data0` is an alias for datas\[0\]
            - `dataX` is an alias for datas\[X\]
            
            _data feeds_ can also be accessed by name (see the reference) if one has been assigned to it
        3. `dnames`: an alternative to reach the data feeds by name (either with `[name]` or with `.name` notation)
            
        4. `broker`: reference to the broker associated to this strategy (received from cerebro) ：经纪商
            
        5. `stats`: list/named tuple-like sequence holding the Observers created by cerebro for this strategy
            
        6. `analyzers`: list/named tuple-like sequence holding the Analyzers created by cerebro for this strategy
            
        7. `position`: actually a property which gives the current position for `data0`.
            
    3. 方法：
        1. next : 每个周期运行
        2. nextstart ： 每个周期后运行
        3. prenext ： 每个周期前运行
        4. start  ： 开始
        5. stop  ： 结束
        6. notify\_order(order) ： 当接收到订单变化状态的时候，调用这个回调函数。
        7. notify\_trade(trade) ： 当接收到交易变化状态的时候，调用这个回调函数。
        8. notify\_cashvalue(cash, value) ： 当接收到资金变化的时候，调用这个回调函数。
        9. notify\_fund(cash, value, fundvalue, shares) ：
        10. notify\_store(msg, \*args, \*\*kwargs)
        11. getsizer() ： 获得默认的购买数量
        12. setsizer(sizer) ： 设置默认的购买数量
        13. getsizing(data=None, isbuy=True) ： 。
        14. getposition(data=None, broker=None) ： 获得当前的财务状况。
        15. getpositionbyname(name=None, broker=None) ：
        16. getdatanames() ：获得数据名称列表
        17. getdatabyname(name) ： 获得指定名称的数据。
        18. add\_timer(when, offset=datetime.timedelta(0), repeat=datetime.timedelta(0), weekdays=\[\], weekcarry=False, monthdays=\[\], monthcarry=True, allow=None, tzdata=None, cheat=False, \*args, \*\*kwargs)
4. 下单
    1. 简单下单：
        1. buy :
        2. sell :
        3. close :
        4. cancel :
    2. 下单的参数：
        1. data (default: None) ：哪个品种的，默认self.datas\[0\] or self.data0
        2. size (default: None)
        3. price (default: None)
        4. plimit (default: None)：Only applicable to StopLimit orders. 只是在限价止损单
        5. exectype ：下单类型
            1. Order.Market or None. A market order will be executed with the next available price. In backtesting it will be the opening price of the next bar
            2. Order.Limit. An order which can only be executed at the given price or better
            3. Order.Stop. An order which is triggered at price and executed like an order.Market order
            4. Order.StopLimit. An order which is triggered at price and executed as an implicit Limit order with price given by pricelimit
        6. valid (default: None) 有效期
            1. None: this generates an order that will not expire (aka Good til cancel) and remain in the market until matched or canceled. In reality brokers tend to impose a temporal limit, but this is usually so far away in time to consider it as not expiring
            2. datetime.datetime or datetime.date instance: the date will be used to generate an order valid until the given datetime (aka good til date)
            3. Order.DAY or 0 or timedelta(): a day valid until the End of the Session (aka day order) will be generated
            4. numeric value: This is assumed to be a value corresponding to a datetime in matplotlib coding (the one used by backtrader) and will used to generate an order valid until that time (good til date)
        7. tradeid (default: 0)This is an internal value applied by backtrader to keep track of overlapping trades on the same asset. This tradeid is sent back to the strategy when notifying changes to the status of the orders.
        8. \*\*kwargs: additional broker implementations may support extra parameters. backtrader will pass the kwargs down to the created order objects
    3. 其他下单：
        1. buy\_bracket(data=None, size=None, price=None, plimit=None, exectype=2, valid=None, tradeid=0, trailamount=None, trailpercent=None, oargs={}, stopprice=None, stopexec=3, stopargs={}, limitprice=None, limitexec=2, limitargs={}, \*\*kwargs)
        2. sell\_bracket(data=None, size=None, price=None, plimit=None, exectype=2, valid=None, tradeid=0, trailamount=None, trailpercent=None, oargs={}, stopprice=None, stopexec=3, stopargs={}, limitprice=None, limitexec=2, limitargs={}, \*\*kwargs)
        3. order\_target\_size(data=None, target=0, \*\*kwargs) ：买指定大小的股份，如果当前的少于指定大小，则买入，如果当前的大于指定大小，则卖出。
        4. order\_target\_value(data=None, target=0.0, price=None, \*\*kwargs) ：买指定金额的部分。
        5. order\_target\_percent(data=None, target=0.0, \*\*kwargs) ： 买指定百分比的
5. Indicator ： 字面意思是指示器，其实就是指标。
6. 经纪费用，这里包含佣金，
    1. 佣金 ：
        
        ```
        cerebro.broker.setcommission(commission=0.001) # 0.1% ... divide by 100 to remove the %
        ```
        
    2. 杠杆 ： 在查找中。
7. 定制参数。
    1. ```
        params = (
                ('maperiod', 15),
            )
        ```
        
    2. 其实就是在策略类种添加如上的属性，然后在策略中像这样调用而已
        
        ```
        self.sma = bt.indicators.SimpleMovingAverage(
                    self.datas[0], period=self.params.maperiod)
        ```
        
    
8. 参数优化。
    1. ```
        strats = cerebro.optstrategy(
                TestStrategy,
                maperiod=range(10, 31))
        ```
        
    2. 接着如上的定制参数，在添加策略的时候，声明一下参数。
