---
layout: post
title: "TextBox在MVVM中滚动到底部的方法"
date: "2024-07-16"
categories: ["计算机语言", "c#"]
---

如果是net4.6以上版本，需要安装 ： Microsoft.Xaml.Behaviors.Wpf ，如果是小于这个的版本，需要安装System.Windows.InterActivity.dll 和Microsoft.Expression.InterActions.dll

 

 

```xml
<Window x:Class="textbox在MVVM模式下滚动到底部.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:textbox在MVVM模式下滚动到底部"
        mc:Ignorable="d"
        xmlns:behaviors ="http://schemas.microsoft.com/xaml/behaviors"
        Title="MainWindow" Height="450" Width="800">
    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="30"/>
            <RowDefinition Height="3*"/>
        </Grid.RowDefinitions>
        <Button Content="增加一行" Click="Button_Click"/>
        <TextBox Grid.Row="1" Text="{Binding Message,Mode=TwoWay}" VerticalScrollBarVisibility="Auto">
            <behaviors:Interaction.Triggers> <!--触发器-->
                <!--下边是一个事件触发器，源是这个TextBox对象，，事件是文本更改事件 -->
                <behaviors:EventTrigger SourceObject="{Binding RelativeSource={RelativeSource AncestorType=TextBox}}" EventName="TextChanged"> 
                    <behaviors:CallMethodAction MethodName="ScrollToEnd" /> <!--调用方法-->
                </behaviors:EventTrigger>
            </behaviors:Interaction.Triggers>
        </TextBox>

    </Grid>
</Window>

```
