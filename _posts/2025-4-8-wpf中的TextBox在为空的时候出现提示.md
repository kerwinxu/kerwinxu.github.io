---
layout: post
title:  wpf中的TextBox在为空的时候提示文字
date:   2025-4-8 10:57:00 +0800
categories: ["c#", "Wpf"]
project: false
excerpt: wpf的TextBox在为空的时候提示文字
lang: zh
published: true
tag:
- c#
- wpf
- TextBox
---

如下，资源加上样式表。

```xml
<TextBox.Resources>
    <VisualBrush x:Key="HintText" TileMode="None" Opacity="0.5" Stretch="None" AlignmentX="Left">
        <VisualBrush.Visual>
            <TextBlock Text="新的员工名" Foreground="Gray"/>
        </VisualBrush.Visual>
    </VisualBrush>
</TextBox.Resources>
<TextBox.Style>
    <Style TargetType="TextBox">
        <Style.Triggers>
            <Trigger Property="Text" Value="{x:Null}">
                <Setter Property="Background" Value="{StaticResource HintText}"/>
            </Trigger>
            <Trigger Property="Text" Value="">
                <Setter Property="Background" Value="{StaticResource HintText}"/>
            </Trigger>
        </Style.Triggers>
    </Style>
</TextBox.Style>
```
