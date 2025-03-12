---
layout: post
title: "opencv连接摄像头读取MJPEG流"
date: "2022-07-13"
categories: 
  - "c"
---

顺序很重要

```
var capture = new VideoCapture();

capture.FourCC = "mjpg";  // 这个得在设置分辨率前面。
capture.Fps = 10;
int width = int.Parse(txt_width.Text);
int height = int.Parse(txt_height.Text);
capture.Set(CaptureProperty.FrameWidth, width);
capture.Set(CaptureProperty.FrameHeight, height);

capture.Open(0);
```
