---
title: "WPF基础之Application"
date: "2017-08-10"
categories: 
  - "c"
---

1. Application介绍。
    1. 跟winform的类似，都是管理程序的
    2. 组成，由两部分组成 : App.xaml 和 App.xaml.cs，这有点类似于 Asp.Net WebForm，将定义和行为代码相分离。
2. 启动。
    1. 可以使用App.xaml文件定义启动应用程序。
    2. 也可以用类似winform的方式，用App.cs来启动。
3. 关闭
    1. 只有在Shutdown 方法被调用时，应用程序才停止运行。
