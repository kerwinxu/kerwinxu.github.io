---
layout: post
title: "WPF DatePicker默认显示当前日期"
date: "2019-05-18"
categories: ["计算机语言", "c"]
---

WPF的日历选择控件默认为当前日期，共有两种方法，一种静态，一种动态。

静态的当然写在DatePicker控件的属性里了，动态的写在对应的cs文件里，具体请看下面。

    1.方法一：

    myDatePicker.Text = DateTime.Today.ToLongDateString();

    2.方法二：

    先在窗体头部引入命名空间：

    xmlns:sys="clr-namespace:System;assembly=mscorlib"

    然后：

    <DatePicker SelectedDate="{x:Static sys:DateTime.Now}" />

 

    不过呢，建议用第二种方法，把UI和逻辑分开，不要再把它们放一起了！
