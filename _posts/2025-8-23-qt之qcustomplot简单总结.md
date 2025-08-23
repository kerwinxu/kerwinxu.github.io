---
layout: post
title: "qt之qcustomplot简单总结"
date: "2025-08-23"
categories: ["计算机语言", "c"]
---

# 添加文件
将qcustomplot.h和qcustomplot.cpp保存到项目目录，然后添加现有文件，注意，需要修改qcustomplot.cpp文件，以设置自适应y轴，设置方法参考：[点击这里查看我的文章2025-8-22-qcustomplot自适应y轴]({% post_url 2025-8-22-qcustomplot自适应y轴 %})

# ui
在ui界面中添加一个widgets，然后提升为QCustomPlot类

# 初始化

初始化
```c
    // 这里创建图表
    //添加一条曲线
    //向绘图区域QCustomPlot(从widget提升来的)添加一条曲线
    ui->chart1->addGraph();
    //设置画笔
    ui->chart1->graph(0)->setPen(QPen(Qt::blue));
    //设置右上角图形标注名称
    ui->chart1->graph(0)->setName("曲线");
    //设置坐标轴标签名称
    ui->chart1->xAxis->setLabel("x");
    ui->chart1->yAxis->setLabel("y");
    // 启用交互功能：拖动 + 缩放
    ui->chart1->setInteractions(QCP::iRangeDrag | QCP::iRangeZoom);

```

# 数据源

我这里是在头文件中定义的，
```c
    QVector<double>datas;         // 接收到的y的数据
    QVector<double>xs;            // x的数据
```

# 绘图

```c
    // 已知个数，已知数值，需要绘图
    //传入数据，setData的两个参数类型为double
    ui->chart1->graph(0)->setData(xs,datas);
    // 显示全部
    ui->chart1->rescaleAxes();
    //曲线重绘，这里表示有时间再绘制，而不是立刻绘制。
    ui->chart1->replot(QCustomPlot::RefreshPriority::rpRefreshHint);

```
