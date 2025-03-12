---
layout: post
title: "\"RuntimeError: main thread is not in main loop\""
date: "2021-10-17"
categories: 
  - "python"
---

1. 多线程Threading问题，将多线程的代码设置到后台， .setDaemon(True) , 后台线程，关闭程序后会自动关掉。
2. matplotlib 问题，matplotlib的默认backend是TkAgg，而FltkAgg, GTK, GTKAgg, GTKCairo, TkAgg , Wx or WxAgg这几个backend都要求有GUI图形界面的，我运行的linux环境是没有图形界面的，所以报错，改成：指定不需要GUI的backend（Agg, Cairo, PS, PDF or SVG）,两种方法。
    1. ```
        import matplotlib 
        matplotlib.use("Agg")
        ```
        
         
    2. ```
        import matplotlib.pyplot as plt
        plt.switch_backend("agg")
        ```
