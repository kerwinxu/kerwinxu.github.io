---
layout: post
title:  wpf的Listbox做成网格布局有边框
date:   2025-4-1 11:02:00 +0800
categories: ["计算机语言","c#"]
project: false
excerpt: wpf的ListBox做成网格布局有边框
lang: zh
published: true
tag:
- c#
- wpf
- Listbox
- 边框
- 网格
---

分解：   
   - 需要横向排列
   - 横向到头后要换行，也就是禁止横向滚动条
   - 有表格,实际上是单元格样式表里边有边框

```xml
<ListBox Grid.Row="2" ItemsSource="{Binding AlarmMessages}"
ScrollViewer.HorizontalScrollBarVisibility="Disabled"
>
	<ListBox.ItemContainerStyle>
		<Style TargetType="{x:Type ListBoxItem}">
			<Setter Property="Margin" Value="0,0,0,0" />
			<Setter Property="Padding" Value="0" />
			<Setter Property="Template">
				<Setter.Value>
					<ControlTemplate TargetType="{x:Type ListBoxItem}">
						<!-- 边框 -->
						<Border 
							BorderBrush="Gray" 
							BorderThickness="1"
							Width="210"
							>
							<ContentPresenter />
						</Border>
					</ControlTemplate>
				</Setter.Value>
			</Setter>
		</Style>
	</ListBox.ItemContainerStyle>
	<ListBox.ItemsPanel>
		<ItemsPanelTemplate>
			<WrapPanel Orientation="Horizontal" IsItemsHost="True" />
		</ItemsPanelTemplate>
	</ListBox.ItemsPanel>
	<ListBox.ItemTemplate>
		<DataTemplate>
			<StackPanel Orientation="Horizontal" >
				<TextBlock Text="{Binding Name}" Background="{Binding Data, Converter={StaticResource IntToBrushConverter}}" Width="180"/>
				<TextBlock Text="{Binding Data, Converter={StaticResource DataToStatusConverter}}"  Background="{Binding Data, Converter={StaticResource IntToBrushConverter}}" Width="20" />
			</StackPanel>
		</DataTemplate>
	</ListBox.ItemTemplate>
</ListBox>
```