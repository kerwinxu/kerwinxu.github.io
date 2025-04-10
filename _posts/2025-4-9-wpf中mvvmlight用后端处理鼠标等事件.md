---
layout: post
title:  wpf中mvvmlight用后端处理鼠标等事件.
date:   2025-4-9 10:48:00 +0800
categories: ["c#", "Wpf"]
project: false
excerpt: wpf中mvvmlight用后端处理鼠标等事件.
lang: zh
published: true
tag:
- c#
- wpf
- mvvmlight
- 鼠标事件
---

声明namespace
```
xmlns:i="clr-namespace:System.Windows.Interactivity;assembly=System.Windows.Interactivity"
xmlns:cmd="http://www.galasoft.ch/mvvmlight"
```

```xml
<ComboBox Width="60"  ItemsSource="{Binding PortNames}" SelectedItem="{Binding PortName}">
    <!-- 绑定下拉框弹出事件-->
    <i:Interaction.Triggers>
        <!--wpf的弹出下拉框是DropDownOpened-->
        <i:EventTrigger EventName="DropDownOpened">
            <cmd:EventToCommand Command="{Binding ShowPortNames}" PassEventArgsToCommand="True" />
    </i:EventTrigger>
    </i:Interaction.Triggers>
</ComboBox>
```

后端
```c#
private void _show_portnames(EventArgs args)
{
    PortNames = SerialPort.GetPortNames();
    Debug.WriteLine($"显示串口:{string.Join(",",PortNames)}");
}

private RelayCommand<EventArgs> showPortNames;
/// <summary>
/// 
/// </summary>
public RelayCommand<EventArgs> ShowPortNames
{
    get
    {
        if (showPortNames == null) showPortNames = new RelayCommand<EventArgs>(_show_portnames);
        return showPortNames;
    }
}
```
