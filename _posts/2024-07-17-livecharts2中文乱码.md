---
layout: post
title: "LiveCharts2中文乱码"
date: "2024-07-17"
categories: ["计算机语言", "c#"]
---

```c#
public RectangularSection[] Sections { get; set; } =
{
new RectangularSection
{
    Xi = 8,
    Yi = 0,
    Xj = 8,
    Yj = 8,
    Label="测试横线",
    LabelSize=20,
    LabelPaint = new SolidColorPaint{
        Color=SKColors.Red,StrokeThickness=3,
        SKTypeface=SKFontManager.Default.MatchCharacter('汉'), // 添加这个，解决中文乱码，字体问题。
    },
    Stroke = new SolidColorPaint
    {
        Color = SKColors.Red,
        StrokeThickness = 3,
        PathEffect = new DashEffect(new float[] { 6, 6 })
    }
},
```
