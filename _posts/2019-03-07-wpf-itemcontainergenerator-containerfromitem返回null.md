---
layout: post
title: "WPF ItemContainerGenerator.ContainerFromItem返回Null"
date: "2019-03-07"
categories: 
  - "c"
---

ItemContainerGenerator.ContainerFromItem有一个问题，就是只能获得已经显示或者说new的item，问题是wpf有虚拟化，有不少控件不显示啊。

 

解决办法：

1、设置DataGrid 属性VirtualizingStackPanel.IsVirtualizing="False"

2、动态设置：如果后台代码返回null，例如，var row = dataGrid.ItemContainerGenerator.ContainerFromItem(dataGrid.Items\[i\]) as DataGridRow;

那么在这行代码之前加入一句：DataGrid.UpdateLayout();

3、如果是my:DataGrid 这种类型的控件，返回值也会为null，去掉"my:"才行
