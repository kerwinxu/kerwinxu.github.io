---
layout: post
title: "WPF TabControl-设置TabItems的样式"
date: "2024-08-25"
categories: 
  - "c"
---

# 范例1

```xml
<Window x:Class="WpfTutorialSamples.Misc_controls.StyledTabItemsSample"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="StyledTabItemsSample" Height="150" Width="250">
    <Grid>
        <TabControl Margin="10" BorderThickness="0" Background="LightGray">
            <TabControl.Resources>
                <Style TargetType="TabItem">
                    <Setter Property="Template">
                        <Setter.Value>
                            <ControlTemplate TargetType="TabItem">
                                <Grid Name="Panel">
                                    <ContentPresenter x:Name="ContentSite"
                                        VerticalAlignment="Center"
                                        HorizontalAlignment="Center"
                                        ContentSource="Header"
                                        Margin="10,2"/>
                                </Grid>
                                <ControlTemplate.Triggers>
                                    <Trigger Property="IsSelected" Value="True">
                                        <Setter TargetName="Panel" Property="Background" Value="LightSkyBlue" />
                                    </Trigger>
                                    <Trigger Property="IsSelected" Value="False">
                                        <Setter TargetName="Panel" Property="Background" Value="White" />
                                    </Trigger>
                                </ControlTemplate.Triggers>
                            </ControlTemplate>
                        </Setter.Value>
                    </Setter>
                </Style>
            </TabControl.Resources>
            <TabItem Header="General">
                <Label Content="Content goes here..." />
            </TabItem>
            <TabItem Header="Security" />
            <TabItem Header="Details" />
        </TabControl>
    </Grid>
</Window>
```

效果如下

[![](/assets/image/default/tabcontrol_styled_tab_simple.png)](http://127.0.0.1/?attachment_id=5329)

# 范例2

```xml
<Window x:Class="WpfTutorialSamples.Misc_controls.StyledTabItemsWithBorderSample"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="StyledTabItemsWithBorderSample" Height="150" Width="250">
    <Grid>
        <TabControl Margin="10" BorderBrush="Gainsboro">
            <TabControl.Resources>
                <Style TargetType="TabItem">
                    <Setter Property="Template">
                        <Setter.Value>
                            <ControlTemplate TargetType="TabItem">
                                <Border Name="Border" BorderThickness="1,1,1,0" BorderBrush="Gainsboro" CornerRadius="4,4,0,0" Margin="2,0">
                                    <ContentPresenter x:Name="ContentSite"
                                        VerticalAlignment="Center"
                                        HorizontalAlignment="Center"
                                        ContentSource="Header"
                                        Margin="10,2"/>
                                </Border>
                                <ControlTemplate.Triggers>
                                    <Trigger Property="IsSelected" Value="True">
                                        <Setter TargetName="Border" Property="Background" Value="LightSkyBlue" />
                                    </Trigger>
                                    <Trigger Property="IsSelected" Value="False">
                                        <Setter TargetName="Border" Property="Background" Value="GhostWhite" />
                                    </Trigger>
                                </ControlTemplate.Triggers>
                            </ControlTemplate>
                        </Setter.Value>
                    </Setter>
                </Style>
            </TabControl.Resources>
            <TabItem Header="General">
                <Label Content="Content goes here..." />
            </TabItem>
            <TabItem Header="Security" />
            <TabItem Header="Details" />
        </TabControl>
    </Grid>
</Window>
```

效果如下

[![](/assets/image/default/tabcontrol_styled_tab_borders.png)](http://127.0.0.1/?attachment_id=5330)
