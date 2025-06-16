---
layout: post
title: "wpf中TextBox和TextBlock自动换行问题。"
date: "2018-10-01"
categories: ["计算机语言", "c#"]
---

简单，设置属性

<TextBlock x:Name="textBlock" ?Height="150" HorizontalAlignment="Center" VerticalAlignment="Top" Width="250" Textwrapping = "Wrap"\>Jack|Tom</TextBlock>

Textwrapping = "Wrap"就可以了。
