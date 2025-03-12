---
title: "wpf中ListView中的按钮"
date: "2022-06-18"
categories: 
  - "c"
---

```
<Button Content="增加照片" Grid.Row="2" Command="{Binding RelativeSource={RelativeSource AncestorType={x:Type local:MainWindow}}, Path=DataContext.AddImg}" CommandParameter="{Binding}" />
```

这个RelativeSource 表示相对源，local:MainWindow，表示这个视图的窗体类名称，而DataContext是这个窗体的数据源，AddImg是真正的操作。CommandParameter="{Binding}"  表示这个ListView中的项目。
