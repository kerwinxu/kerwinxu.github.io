---
layout: post
title: "wpf中listboxItem显示序号"
date: "2017-08-18"
categories: 
  - "c"
---

原网址：http://blog.csdn.net/sanyuni/article/details/45575145

内容：

在显示出来的Item中显示出当前Item的index值

Xaml文件如下：

<Window.Resources> <Style x:Key="wrapalListBox" TargetType="ListBox"> <Setter Property="Template"> <Setter.Value> <ControlTemplate> <WrapPanel  Orientation="Horizontal" IsItemsHost="True" ScrollViewer.CanContentScroll="True"/> </ControlTemplate> </Setter.Value> </Setter> </Style>

<DataTemplate x:Key="listItemTempalte"> <Button  Width="40" Height="30" Content="{Binding RelativeSource={RelativeSource TemplatedParent}, Path=TemplatedParent.(ItemsControl.AlternationIndex)}"/> </DataTemplate> </Window.Resources> <Grid> <ListBox Style="{ StaticResource wrapalListBox}" ItemTemplate="{StaticResource listItemTempalte}" ItemsSource="{Binding Items}" AlternationCount="{Binding Path=Items.Count}" >

</ListBox> </Grid>

然后我更改的是

<ListBox x:Name="listBox\_garment\_stock\_process\_last" ItemsSource="{Binding DT}" Margin="1" Grid.Row="1" ItemTemplate="{DynamicResource garment\_stock\_progress\_last\_item}" VirtualizingStackPanel.IsVirtualizing="True" VirtualizingStackPanel.VirtualizationMode="Recycling" AlternationCount="{Binding Path=DT.Rows.Count}" >

然后显示的控件是：

<Label x:Name="label206" Grid.Row="1" Grid.Column="6" Content="{Binding RelativeSource={RelativeSource TemplatedParent}, Path=TemplatedParent.(ItemsControl.AlternationIndex)}"></Label>
