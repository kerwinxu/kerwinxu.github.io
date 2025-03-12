---
layout: post
title: "matplotlib 中文乱码"
date: "2019-03-04"
categories: 
  - "python"
---

进入目录 D:\\Anaconda3\\Lib\\site-packages\\matplotlib\\mpl-data

编辑matplotlibrc文件，去掉如下行的注释，并加上红色的字体。

font.sans-serif :SimHei,Microsoft Yahei UI, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
