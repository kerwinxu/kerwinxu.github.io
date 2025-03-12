---
title: "lazarus的TChart图表"
date: "2024-11-28"
categories: 
  - "lazarus"
---

TChart控件相当于画布

各种ChartSource控件相当于x或者y轴的刻度。

TChart的下边可以添加

- AxisList:TChartAxisList , 刻度的，就是如上的各种ChartSource控件
- Chart1LineSerial1:TLineSerial : 各种图标，这个是折线图，从这里边添加数据。

 

ChartAxisTransformations : 轴变换的

ChartLiveView :  当active是true的时候，有新数据，自动跳回到最新的数据点，并且这个可以设置可视区域的宽度。

 

 

引用

- [Tchart with log scale and needed real time on X-axis](https://forum.lazarus.freepascal.org/index.php?topic=65595.0)
