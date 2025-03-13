---
layout: post
title: "wpf中listbox等控件隔行换色"
date: "2023-11-05"
categories: 
  - "c"
---

建立一个样式。

```xml
<Style x:Key="NormalListBoxItemContainerStyle" TargetType="{x:Type ListBoxItem}">
        <Setter Property="SnapsToDevicePixels" Value="True"/>
        <Setter Property="HorizontalContentAlignment" Value="Stretch"/>
        <Setter Property="VerticalContentAlignment" Value="{Binding VerticalContentAlignment, RelativeSource={RelativeSource FindAncestor, AncestorLevel=1, AncestorType={x:Type ItemsControl}}}"/>
        <Setter Property="Background" Value="Transparent" />
        <Setter Property="BorderBrush" Value="Transparent"/>
        <Setter Property="BorderThickness" Value="0"/>
        <Setter Property="IsTabStop" Value="False"/>
        <Setter Property="Template">
            <Setter.Value>
                <ControlTemplate TargetType="{x:Type ListBoxItem}">
                    <Border x:Name="Bd" BorderBrush="{TemplateBinding BorderBrush}" BorderThickness="{TemplateBinding BorderThickness}" Background="{TemplateBinding Background}"  SnapsToDevicePixels="True">
                        <ContentPresenter ContentTemplate="{TemplateBinding ContentTemplate}" Content="{TemplateBinding Content}" ContentStringFormat="{TemplateBinding ContentStringFormat}" HorizontalAlignment="{TemplateBinding HorizontalContentAlignment}" SnapsToDevicePixels="{TemplateBinding SnapsToDevicePixels}" VerticalAlignment="{TemplateBinding VerticalContentAlignment}"/>
                    </Border>
                    <ControlTemplate.Triggers>
                        <Trigger Property="ItemsControl.AlternationIndex" Value="0">
                            <Setter TargetName="Bd" Property="Background" Value="Red"/>
                        </Trigger>
                        <Trigger Property="ItemsControl.AlternationIndex" Value="1">
                            <Setter TargetName="Bd" Property="Background" Value="Green"/>
                        </Trigger>
                    </ControlTemplate.Triggers>
                </ControlTemplate>
            </Setter.Value>
        </Setter>
    </Style>
```

然后应用样式

```xml
<ListBox x:Name="lst_StocklotProcesses" Grid.Row="1" ItemsSource="{Binding StocklotProcesses}"
                             ScrollViewer.HorizontalScrollBarVisibility="Disabled"
                             ItemContainerStyle="{StaticResource NormalListBoxItemContainerStyle}"
                             AlternationCount="2"
                             >
```

- 表示应用样式
- AlternationCount表示多少行一个循环。
