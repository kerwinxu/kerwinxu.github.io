---
layout: post
title: "wpf的ui框架Material Design theme和Dragablz做到TabControl"
date: "2021-11-12"
categories: 
  - "c"
---

# 步骤

1. 安装 ： Material Design theme 和 Dragablz都可以通过nuget安装。
2. 设置app.xml
    1. 关于Material Design theme 部分：
        1. 添加 xmlns:materialDesign="http://materialdesigninxaml.net/winfx/xaml/themes"
        2. ```
            <Application.Resources>
                <ResourceDictionary>
                    <ResourceDictionary.MergedDictionaries>
                            <ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesignTheme.Dark.xaml" />
                            <ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesignTheme.Defaults.xaml" />
                            <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/Recommended/Primary/MaterialDesignColor.DeepPurple.xaml" />
                            <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/Recommended/Accent/MaterialDesignColor.Lime.xaml" />
                    </ResourceDictionary.MergedDictionaries>
                </ResourceDictionary>
            </Application.Resources>
            
            ```
            
    2.  关于Dragablz部分
        1. 添加 xmlns:dragablz="clr-namespace:Dragablz;assembly=Dragablz
        2. ```
            <Application x:Class="MaterialDesignColors.WpfExample.App"
                         xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
                         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                         xmlns:dragablz="clr-namespace:Dragablz;assembly=Dragablz"
                         StartupUri="MainWindow.xaml">
                <Application.Resources>
                    <ResourceDictionary>
                        <ResourceDictionary.MergedDictionaries>
                            <!-- primary color -->
                            <ResourceDictionary>
                                <!-- include your primary palette -->
                                <ResourceDictionary.MergedDictionaries>
                                    <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/MaterialDesignColor.Indigo.xaml" />
                                </ResourceDictionary.MergedDictionaries>
                                <!--
                                        include three hues from the primary palette (and the associated forecolours).
                                        Do not rename, keep in sequence; light to dark.
                                    -->
                                <SolidColorBrush x:Key="PrimaryHueLightBrush" Color="{StaticResource Primary100}"/>
                                <SolidColorBrush x:Key="PrimaryHueLightForegroundBrush" Color="{StaticResource Primary100Foreground}"/>
                                <SolidColorBrush x:Key="PrimaryHueMidBrush" Color="{StaticResource Primary500}"/>
                                <SolidColorBrush x:Key="PrimaryHueMidForegroundBrush" Color="{StaticResource Primary500Foreground}"/>
                                <SolidColorBrush x:Key="PrimaryHueDarkBrush" Color="{StaticResource Primary700}"/>
                                <SolidColorBrush x:Key="PrimaryHueDarkForegroundBrush" Color="{StaticResource Primary700Foreground}"/>
                            </ResourceDictionary>
             
                            <!-- secondary colour -->
                            <ResourceDictionary>
                                <!-- include your secondary pallette -->
                                <ResourceDictionary.MergedDictionaries>
                                    <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/MaterialDesignColor.Yellow.xaml" />
                                </ResourceDictionary.MergedDictionaries>
             
                                <!-- include a single secondary accent color (and the associated forecolour) -->
                                <SolidColorBrush x:Key="SecondaryAccentBrush" Color="{StaticResource Accent200}"/>
                                <SolidColorBrush x:Key="SecondaryAccentForegroundBrush" Color="{StaticResource Accent200Foreground}"/>
                            </ResourceDictionary>
             
                            <!-- Include the Dragablz Material Design style -->
                            <ResourceDictionary Source="pack://application:,,,/Dragablz;component/Themes/materialdesign.xaml"/>                
             
                        </ResourceDictionary.MergedDictionaries>
             
                        <!-- tell Dragablz tab control to use the Material Design theme -->
                        <Style TargetType="{x:Type dragablz:TabablzControl}" BasedOn="{StaticResource MaterialDesignTabablzControlStyle}" />
                    </ResourceDictionary>
                </Application.Resources>
            </Application>
            ```
            
            请注意，如上的是粘贴自官方，实际上<style ... >的这个只能放在窗口中，而不能放在app.xml中
    3. 两个合并起来是如下的
        
        ```
        <Application x:Class="变电站智能辅助控制系统.App" 
                     xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
                     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
                     xmlns:materialDesign="http://materialdesigninxaml.net/winfx/xaml/themes"
                     xmlns:local="clr-namespace:变电站智能辅助控制系统"
                     StartupUri="LoginView.xaml" 
                     xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
                     xmlns:dragablz="clr-namespace:Dragablz;assembly=Dragablz"
                     d1p1:Ignorable="d" 
                     xmlns:d1p1="http://schemas.openxmlformats.org/markup-compatibility/2006">
          <Application.Resources>
                <ResourceDictionary>
                    <vm:ViewModelLocator x:Key="Locator" d:IsDataSource="True" xmlns:vm="clr-namespace:变电站智能辅助控制系统.ViewModel" />
        
                    <ResourceDictionary.MergedDictionaries>
                        <ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesignTheme.Dark.xaml" />
                        <ResourceDictionary Source="pack://application:,,,/MaterialDesignThemes.Wpf;component/Themes/MaterialDesignTheme.Defaults.xaml" />
                        <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/Recommended/Primary/MaterialDesignColor.DeepPurple.xaml" />
                        <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/Recommended/Accent/MaterialDesignColor.Lime.xaml" />
        
                        <!-- primary color -->
                        <ResourceDictionary>
                            <!-- include your primary palette -->
                            <ResourceDictionary.MergedDictionaries>
                                <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/MaterialDesignColor.Indigo.xaml" />
                            </ResourceDictionary.MergedDictionaries>
                            <!--
                                    include three hues from the primary palette (and the associated forecolours).
                                    Do not rename, keep in sequence; light to dark.
                                -->
                            <SolidColorBrush x:Key="PrimaryHueLightBrush" Color="{StaticResource Primary100}"/>
                            <SolidColorBrush x:Key="PrimaryHueLightForegroundBrush" Color="{StaticResource Primary100Foreground}"/>
                            <SolidColorBrush x:Key="PrimaryHueMidBrush" Color="{StaticResource Primary500}"/>
                            <SolidColorBrush x:Key="PrimaryHueMidForegroundBrush" Color="{StaticResource Primary500Foreground}"/>
                            <SolidColorBrush x:Key="PrimaryHueDarkBrush" Color="{StaticResource Primary700}"/>
                            <SolidColorBrush x:Key="PrimaryHueDarkForegroundBrush" Color="{StaticResource Primary700Foreground}"/>
                        </ResourceDictionary>
        
                        <!-- secondary colour -->
                        <ResourceDictionary>
                            <!-- include your secondary pallette -->
                            <ResourceDictionary.MergedDictionaries>
                                <ResourceDictionary Source="pack://application:,,,/MaterialDesignColors;component/Themes/MaterialDesignColor.Yellow.xaml" />
                            </ResourceDictionary.MergedDictionaries>
        
                            <!-- include a single secondary accent color (and the associated forecolour) -->
                            <SolidColorBrush x:Key="SecondaryAccentBrush" Color="{StaticResource Accent200}"/>
                            <SolidColorBrush x:Key="SecondaryAccentForegroundBrush" Color="{StaticResource Accent200Foreground}"/>
                        </ResourceDictionary>
        
                        <!-- Include the Dragablz Material Design style -->
                        <ResourceDictionary Source="pack://application:,,,/Dragablz;component/Themes/materialdesign.xaml"/>
        
                    </ResourceDictionary.MergedDictionaries>
        
                    <!-- tell Dragablz tab control to use the Material Design theme -->
                </ResourceDictionary>
              
            </Application.Resources>
            
        </Application>
        ```
        
         
3.  窗口的xml，在3部分添加
    1. ```
        xmlns:dragablz="clr-namespace:Dragablz;assembly=Dragablz"
        ```
        
    2. ```
        <Window.Resources>
            <ResourceDictionary>
                <Style TargetType="{x:Type dragablz:TabablzControl}" BasedOn="{StaticResource MaterialDesignTabablzControlStyle}" />
        
            </ResourceDictionary>
        </Window.Resources>
        ```
        
    3. 然后写控件的时候是类似这样写
        
        ```
        <dragablz:TabablzControl>
               <dragablz:TabablzControl.InterTabController>
                   <dragablz:InterTabController />
               </dragablz:TabablzControl.InterTabController>
               <TabItem Header="HELLO">
                   <TextBlock HorizontalAlignment="Center" VerticalAlignment="Center">Hello World</TextBlock>
               </TabItem>
               <TabItem Header="MATERIAL">
                   <TextBlock HorizontalAlignment="Center" VerticalAlignment="Center">Material Design</TextBlock>
               </TabItem>
               <TabItem Header="DESIGN">
                   <TextBlock HorizontalAlignment="Center" VerticalAlignment="Center">Looks Quite Nice</TextBlock>
               </TabItem>
           </dragablz:TabablzControl>
        ```
