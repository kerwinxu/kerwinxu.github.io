---
title: "eclipse配置javafx项目"
date: "2021-08-02"
categories: 
  - "java"
---

# 安装

[http://download.eclipse.org/efxclipse/updates-nightly/site](http://download.eclipse.org/efxclipse/updates-nightly/site)

 

# 配置

## 导入javafx包

此时我们需要导入我们的javafx包：右键项目文件夹->Build Path->Add External Archives…：

找到javafx的lib文件目录，全选然后点击打开

## 添加VM 参数

这时我们需要在菜单栏找到Run->Coverage configurations，找到右侧的arguments（参数）选项卡：

在此处填写 –module-path “（javafx的lib路径）” --add-modules javafx.controls,javafx.fxml 比如我的javafx的lib路径为 C:\\Program Files\\Java\\javafx-sdk-13.0.2\\lib

之后点击Coverage，编译成功，程序正常执行
