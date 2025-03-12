---
layout: post
title: "wsl中gnucash的工具栏只显示文字，不显示图片问题解决"
date: "2023-10-27"
categories: 
  - "linux"
---

1. 安装GNOME Tweaks工具：打开WSL终端，运行以下命令来安装GNOME Tweaks工具：
    
    ```
    sudo apt update
    sudo apt install gnome-tweaks
    
    ```
    
2. 打开GNOME Tweaks并选择图标主题：在WSL终端中运行gnome-tweaks命令来打开GNOME Tweaks工具。在GNOME Tweaks的界面中，找到"Appearance"（外观）选项卡，在"Icons"（图标）部分，选择您喜欢的图标主题。
3. 重新登录

我估计是因为GTK主题设置：GNUGcash使用GTK库来绘制用户界面。请确保您的系统上已正确设置了GTK主题。您可以在系统设置或GNOME Tweak Tool中进行调整。

安装这个后，也可以将输入法放在自动启动中。
