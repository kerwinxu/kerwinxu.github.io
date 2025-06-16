---
layout: post
title: "结合ItemsControl在Canvas中动态添加控件的最MVVM的方式"
date: "2023-03-04"
categories: ["计算机语言", "c"]
---

```xml
<Window x:Class="动态控件.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:动态控件"
        xmlns:model="clr-namespace:动态控件.Model"
        mc:Ignorable="d"
        DataContext="{Binding Source={StaticResource Locator}, Path=Main}"
        Title="MainWindow" Height="450" Width="800">

    <Grid>
        <!-- 这个控件可以容纳多个控件 -->
        <ItemsControl ItemsSource="{Binding ItemList}" >
            <ItemsControl.Resources>
                <!--这个定义放在资源中 -->
                <!-- 根据不同类型的对象，选择不同的显示-->
                <DataTemplate DataType="{x:Type model:MyItemViewModelBlue}">
                    <Border Width="120" Height="30" Background="Blue">
                        <TextBlock Text="{Binding Name}" />
                    </Border>
                </DataTemplate>
                <DataTemplate DataType="{x:Type model:MyItemViewModelRed}">
                    <Border Width="120" Height="30" Background="Red">
                        <TextBlock Text="{Binding Name}" />
                    </Border>
                </DataTemplate>
            </ItemsControl.Resources>
            <ItemsControl.ItemsPanel>
                <ItemsPanelTemplate>
                    <Canvas /> <!-- Item的画布 -->
                </ItemsPanelTemplate>
            </ItemsControl.ItemsPanel>
            <ItemsControl.ItemContainerStyle>
                <Style>
                    <!-- 这里设置一下坐标 ,数据是Model中取得的。-->
                    <Setter Property="Canvas.Left" Value="{Binding Left}"/>
                    <Setter Property="Canvas.Top" Value="{Binding Top}"/>
                </Style>
            </ItemsControl.ItemContainerStyle>
        </ItemsControl>
    </Grid>
</Window>

```

 

 

 

# 引用

- [结合ItemsControl在Canvas中动态添加控件的最MVVM的方式](https://www.cnblogs.com/ywei221/p/4570689.html)
- [Need multiple styles dependent on Listboxitem](https://stackoverflow.com/questions/20090798/need-multiple-styles-dependent-on-listboxitem)
