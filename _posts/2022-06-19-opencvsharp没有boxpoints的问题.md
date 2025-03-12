---
layout: post
title: "opencvsharp没有BoxPoints的问题"
date: "2022-06-19"
categories: 
  - "c"
---

用这个是得到一个RotatedRect对象的4个顶点的坐标，我是用Cv2.MinAreaRect(轮廓)得到最小内接矩形，类型是RotatedRect，但opencvsharp中并没有Cv2.BoxPoints(rect,out sourcePoints) 这个函数。

解决：

RotatedRect有一个方法是 Points ， 得到的就是4个顶点的坐标。
