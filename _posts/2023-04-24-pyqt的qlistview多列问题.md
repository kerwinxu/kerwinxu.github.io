---
layout: post
title: "pyqt的QListView多列问题"
date: "2023-04-24"
categories: 
  - "python"
---

关键的三个调用：

1\. setViewMode（QListView::IconMode)

2\. setLayout(QListView::LeftToRight)

3\. setResizeMode(QListView::Adjust)//重要的不要不要的

 

另外该属性可以通过方法isWrapping()、setWrapping(bool enable)来进行访问或设置。

比较奇怪的一点，我用isWrapping这就就可以设置

经过实验，如下数据

- 如果没有自适应布局，那么isWrapping就可以设置成多列了。
- 如果是自适应布局，那么需要设置setViewMode（QListView::IconMode), setLayout(QListView::LeftToRight)，setResizeMode(QListView::Adjust)
