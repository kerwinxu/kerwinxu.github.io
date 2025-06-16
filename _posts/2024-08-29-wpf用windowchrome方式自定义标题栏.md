---
layout: post
title: "wpf用WindowChrome方式自定义标题栏"
date: "2024-08-29"
categories: ["计算机语言", "c"]
---

如果是net4.6以上版本，需要安装 ： Microsoft.Xaml.Behaviors.Wpf ，

代码如下：

```xml
<Window x:Class="自定义标题栏.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:自定义标题栏"
        mc:Ignorable="d"
        xmlns:behaviors ="http://schemas.microsoft.com/xaml/behaviors"
        Title="MainWindow" Height="450" Width="800">
    <Window.Template>
        <ControlTemplate TargetType="{x:Type Window}"> <!-- 模板 -->
            <Border> <!-- 最外边的边框 -->
                <Grid> <!--内部，包括非客户区域和客户区域-->
                    <Grid.RowDefinitions>
                        <RowDefinition Height="32" /> <!-- 非客户区域-->
                        <RowDefinition Height="1*" /> <!-- 客户区域-->
                    </Grid.RowDefinitions>
                    <!-- 如下方非客户区域-->
                    <Grid >
                        <!-- 左右区域 左边是窗体图标文字 右边是操作按钮、最小化、最大化、关闭  -->
                        <Grid.ColumnDefinitions>
                            <ColumnDefinition />
                            <ColumnDefinition Width="Auto" />
                        </Grid.ColumnDefinitions>
                        <StackPanel Orientation="Horizontal" 
                                    Grid.Column="0"
                                    Background="LightGray"
                                >
                            <TextBlock Text="自定义标题" FontSize="20" />
                            <!--下边可以放一些别的东西。-->

                        </StackPanel>
                        <!-- 操作按钮-->
                        <StackPanel Orientation="Horizontal"
                                HorizontalAlignment="Right"
                                    Grid.Column="1"       
                                >

                            <!--最小化按钮-->
                            <Button  WindowChrome.IsHitTestVisibleInChrome="True">
                                <behaviors:Interaction.Triggers>
                                    <behaviors:EventTrigger SourceObject="{Binding RelativeSource={RelativeSource AncestorType=Button}}" EventName="Click">
                                        <behaviors:ChangePropertyAction 
                                            TargetObject="{Binding RelativeSource={RelativeSource AncestorType=Window}}" 
                                            PropertyName="WindowState"
                                            Value="1"
                                            />
                                        <!--调用方法-->
                                    </behaviors:EventTrigger>
                                </behaviors:Interaction.Triggers>
                                
                                <Path
                                    Width="32"
                                    Height="10"
                                    Data="M0,4 L10,4 L10,5 L0,5 z"
                                    Fill="{Binding (TextBlock.Foreground), RelativeSource={RelativeSource AncestorType=Button}}"
                                    RenderTransformOrigin="0.5,0.5"
                                    Stretch="Uniform" />
                            </Button>
                            <!--最大化按钮-->
                            <Button WindowChrome.IsHitTestVisibleInChrome="True">
                                <behaviors:Interaction.Triggers>
                                    <behaviors:EventTrigger SourceObject="{Binding RelativeSource={RelativeSource AncestorType=Button}}" EventName="Click">
                                        <behaviors:ChangePropertyAction 
                                            TargetObject="{Binding RelativeSource={RelativeSource AncestorType=Window}}" 
                                            PropertyName="WindowState"
                                            Value="2"
                                            />
                                        <!--调用方法-->
                                    </behaviors:EventTrigger>
                                </behaviors:Interaction.Triggers>
                                <Path
                                    Width="32"
                                    Height="10"
                                    Data="M1,1 L1,9 L9,9 L9,1 z M0,0 L10,0 L10,10 L0,10 z"
                                    Fill="{Binding (TextBlock.Foreground), RelativeSource={RelativeSource AncestorType=Button}}"
                                    RenderTransformOrigin="0.5,0.5"
                                    Stretch="Uniform" />
                            </Button>
                            <!--关闭按钮-->
                            <Button WindowChrome.IsHitTestVisibleInChrome="True">
                                <behaviors:Interaction.Triggers>
                                    <behaviors:EventTrigger SourceObject="{Binding RelativeSource={RelativeSource AncestorType=Button}}" EventName="Click">
                                        <behaviors:CallMethodAction TargetObject="{Binding RelativeSource={RelativeSource AncestorType=Window}}" MethodName="Close" />
                                        <!--调用方法-->
                                    </behaviors:EventTrigger>
                                </behaviors:Interaction.Triggers>
                                <Path
                                    Width="32"
                                    Height="10"
                                    Data="M0.7,0 L5,4.3 L9.3,0 L10,0.7 L5.7,5 L10,9.3 L9.3,10 L5,5.7 L0.7,10 L0,9.3 L4.3,5 L0,0.7 z"
                                    Fill="{Binding (TextBlock.Foreground), RelativeSource={RelativeSource AncestorType=ContentPresenter}}"
                                    RenderTransformOrigin="0.5,0.5"
                                    Stretch="Uniform" />
                            </Button>
                        </StackPanel>
                    </Grid>
                    

                  
                    <!-- 客户区  -->
                    <AdornerDecorator Grid.Row="1">
                        <ContentPresenter ClipToBounds="True" />
                    </AdornerDecorator>
                </Grid>
            </Border>
        </ControlTemplate>
    </Window.Template>
    <WindowChrome.WindowChrome>
        <!--用这个代替原始的window-->
        <WindowChrome 
            CaptionHeight="32"
            GlassFrameThickness="-1"
            UseAeroCaptionButtons="False"
            />
    </WindowChrome.WindowChrome>
    <Grid Background="#0078D4">
        <TextBlock
            HorizontalAlignment="Center"
            VerticalAlignment="Center"
            FontSize="50"
            FontWeight="Bold"
            Foreground="White"
            Text="丑萌气质狗" />
        
    </Grid>
</Window>

```
