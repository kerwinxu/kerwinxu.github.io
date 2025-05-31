---
layout: post
title:  LiveChart2图表
date:   2025-5-31 10:42:00 +0800
categories: ["c#", "图表"]
project: false
excerpt: TLiveChart2图表
lang: zh
published: true
tag:
- c#
- 图表
- wpf
---

# 安装
这个是预览版，还不是正式版，所以需要在nuget中选择包括预发行版，然后搜索"LiveChartsCore.SkiaSharpView.WPF"。

# 实时曲线1

## 代码1

这个是显示多少秒之前的版本

```csharp
using GalaSoft.MvvmLight;
using LiveChartsCore;
using LiveChartsCore.Defaults;
using LiveChartsCore.SkiaSharpView;
using LiveChartsCore.SkiaSharpView.Painting;
using SkiaSharp;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Runtime.Serialization;
using System.Threading.Tasks;

namespace LiveCharts.ViewModel
{
    /// <summary>
    /// This class contains properties that the main View can data bind to.
    /// <para>
    /// Use the <strong>mvvminpc</strong> snippet to add bindable properties to this ViewModel.
    /// </para>
    /// <para>
    /// You can also use Blend to data bind with the tool's support.
    /// </para>
    /// <para>
    /// See http://www.galasoft.ch/mvvm
    /// </para>
    /// </summary>
    public class MainViewModel : ViewModelBase
    {

        private readonly Random _random = new Random();                              // 随机数
        private readonly List<DateTimePoint> _values = new List<DateTimePoint>();    // 实时点的坐标
        private readonly DateTimeAxis _customAxis;                                   // 时间轴


        /// <summary>
        /// 数据是放在这里边的
        /// </summary>
        public ObservableCollection<ISeries> Series { get; set; }


        /// <summary>
        /// x周
        /// </summary>
        public Axis[] XAxes { get; set; }


        /// <summary>
        /// 多线程的锁，可能是避免界面和后台同时操作数据吧。
        /// </summary>
        public object Sync { get; } = new object();



        public bool IsReading { get; set; } = true;




        /// <summary>
        /// Initializes a new instance of the MainViewModel class.
        /// </summary>
        public MainViewModel()
        {
            ////if (IsInDesignMode)
            ////{
            ////    // Code runs in Blend --> create design time data.
            ////}
            ////else
            ////{
            ////    // Code runs "for real"
            ////}
            ///

            // 图表
            Series = new ObservableCollection<ISeries>{
            new LineSeries<DateTimePoint>    // 折线图，是实时点的坐标
            {
                Values = _values,            // 数据是这些数据
                Fill = null,
                GeometryFill = null,         // 几何学填充，大概是图表下的填充
                GeometryStroke = null
            }
            };

            _customAxis = new DateTimeAxis(TimeSpan.FromSeconds(1), Formatter)
            {
                CustomSeparators = GetSeparators(),                                   // 自定义分隔符
                AnimationsSpeed = TimeSpan.FromMilliseconds(0),                       // 动画的速率
                SeparatorsPaint = new SolidColorPaint(SKColors.Black.WithAlpha(100))  // 图板材料。
            };

            // 设置x轴
            XAxes = new Axis[] { _customAxis };

            _ = ReadData();


        }

        private async Task ReadData()
        {
            // to keep this sample simple, we run the next infinite loop 
            // in a real application you should stop the loop/task when the view is disposed 
            // 只要还在运行
            while (IsReading)
            {
                await Task.Delay(100);

                // Because we are updating the chart from a different thread 
                // we need to use a lock to access the chart data. 
                // this is not necessary if your changes are made on the UI thread. 
               lock (Sync)
                {
                    _values.Add(new DateTimePoint(DateTime.Now, _random.Next(0, 10)));

                    // 有了如下的MaxLimit和MinLimit，不需要手动删除了，当然也可以删除。
                    //if (_values.Count > 250) _values.RemoveAt(0);

                    // we need to update the separators every time we add a new point 
                    _customAxis.CustomSeparators = GetSeparators();


                    // 这里需要设置一下x轴的最左边是什么，添加这一段是为了，
                    // 不要一开始就填充整个图表，然后再慢慢缩放，
                    if ((DateTime.Now-time).TotalSeconds< 30)
                    {
                        XAxes[0].MaxLimit = time.AddSeconds(30).Ticks;
                        XAxes[0].MinLimit = time.Ticks;
                    }
                    else
                    {
                        XAxes[0].MaxLimit = DateTime.Now.Ticks;
                        XAxes[0].MinLimit = DateTime.Now.AddSeconds(-30).Ticks;
                    }
                }
            }
        }

        private static double[] GetSeparators()
        {
            var now = DateTime.Now;
            // 这里的分隔符显示多少秒前的数据
            return new double[] {
                now.AddSeconds(-30).Ticks,
                now.AddSeconds(-25).Ticks,
                now.AddSeconds(-20).Ticks,
                now.AddSeconds(-15).Ticks,
                now.AddSeconds(-10).Ticks,
                now.AddSeconds(-5).Ticks,
                now.Ticks
            };
        }

        /// <summary>
        /// 显示时间的格式。
        /// </summary>
        /// <param name="date"></param>
        /// <returns></returns>
        private static string Formatter(DateTime date)
        {
            var secsAgo = (DateTime.Now - date).TotalSeconds;

            return secsAgo < 1
                ? "now"
                : $"{secsAgo:N0}s ago";
        }




    }
}
```

## 代码2
这个是显示时分秒的版本

```csharp
using GalaSoft.MvvmLight;
using LiveChartsCore;
using LiveChartsCore.Defaults;
using LiveChartsCore.SkiaSharpView;
using LiveChartsCore.SkiaSharpView.Painting;
using SkiaSharp;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Runtime.Serialization;
using System.Threading.Tasks;

namespace LiveCharts.ViewModel
{
    /// <summary>
    /// This class contains properties that the main View can data bind to.
    /// <para>
    /// Use the <strong>mvvminpc</strong> snippet to add bindable properties to this ViewModel.
    /// </para>
    /// <para>
    /// You can also use Blend to data bind with the tool's support.
    /// </para>
    /// <para>
    /// See http://www.galasoft.ch/mvvm
    /// </para>
    /// </summary>
    public class MainViewModel : ViewModelBase
    {

        private readonly Random _random = new Random();                              // 随机数
        private readonly List<DateTimePoint> _values = new List<DateTimePoint>();    // 实时点的坐标


        /// <summary>
        /// 数据是放在这里边的
        /// </summary>
        public ObservableCollection<ISeries> Series { get; set; }


        /// <summary>
        /// x周
        /// </summary>
        public Axis[] XAxes { get; set; }


        /// <summary>
        /// 多线程的锁，可能是避免界面和后台同时操作数据吧。
        /// </summary>
        public object Sync { get; } = new object();



        public bool IsReading { get; set; } = true;




        /// <summary>
        /// Initializes a new instance of the MainViewModel class.
        /// </summary>
        public MainViewModel()
        {
            ////if (IsInDesignMode)
            ////{
            ////    // Code runs in Blend --> create design time data.
            ////}
            ////else
            ////{
            ////    // Code runs "for real"
            ////}
            ///

            // 图表
            Series = new ObservableCollection<ISeries>{
            new LineSeries<DateTimePoint>    // 折线图，是实时点的坐标
            {
                Values = _values,            // 数据是这些数据
                Fill = null,                 // 大概是背景色的意思吧
                GeometryFill = null,
                GeometryStroke = null
            }
            };


            var xAxis = new Axis
            {
                Labeler = value => new DateTime((long)value).ToString("HH:mm:ss"),
                LabelsRotation = 15,
                // 自动调整范围，使图表随新数据滚动
                MinLimit = DateTime.Now.AddSeconds(-10).Ticks,
                MaxLimit = DateTime.Now.Ticks
            };


            // 设置x轴
            XAxes = new Axis[] { xAxis };

            _ = ReadData();


        }




        private async Task ReadData()
        {
            // to keep this sample simple, we run the next infinite loop 
            // in a real application you should stop the loop/task when the view is disposed 
            // 只要还在运行
            while (IsReading)
            {
                await Task.Delay(100);

                // Because we are updating the chart from a different thread 
                // we need to use a lock to access the chart data. 
                // this is not necessary if your changes are made on the UI thread. 
                lock (Sync)
                {
                    _values.Add(new DateTimePoint(DateTime.Now, _random.Next(0, 10)));

                    // 有了如下的MaxLimit和MinLimit，不需要手动删除了，当然也可以删除。
                    //if (_values.Count > 250) _values.RemoveAt(0);

                    // we need to update the separators every time we add a new point 
                    //_customAxis.CustomSeparators = GetSeparators();


                    // 这里需要设置一下x轴的最左边是什么，添加这一段是为了，
                    // 不要一开始就填充整个图表，然后再慢慢缩放，
                    DateTime now = DateTime.Now;
                    var xAxis = XAxes[0];
                    xAxis.MaxLimit = now.Ticks;
                    xAxis.MinLimit = now.AddSeconds(-10).Ticks;

                }
            }
        }

    }
}
```

## 界面

```xml

<Window x:Class="LiveCharts.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:local="clr-namespace:LiveCharts"
        mc:Ignorable="d"
        
        xmlns:lvc="clr-namespace:LiveChartsCore.SkiaSharpView.WPF;assembly=LiveChartsCore.SkiaSharpView.WPF"

        DataContext="{Binding Source={StaticResource Locator},Path=Main }"
        Title="MainWindow" Height="450" Width="800">
    <Grid>
        <lvc:CartesianChart
        SyncContext="{Binding Sync}"
        Series="{Binding Series}"
        XAxes="{Binding XAxes}">
        </lvc:CartesianChart>

    </Grid>
</Window>

```


# 折线图

## 代码
```csharp

using LiveChartsCore;
using LiveChartsCore.Defaults;
using LiveChartsCore.SkiaSharpView;

namespace ViewModelsSamples.Lines.XY;

public class ViewModel
{
    public ISeries[] Series { get; set; } = [
        new LineSeries<ObservablePoint>
        {
            Values = [
                new ObservablePoint(0, 4),
                new ObservablePoint(1, 3),
                new ObservablePoint(3, 8),
                new ObservablePoint(18, 6),
                new ObservablePoint(20, 12)
            ]
        }
  
}
```

## 界面

```xml
<UserControl x:Class="WPFSample.Lines.XY.View"
             xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
             xmlns:lvc="clr-namespace:LiveChartsCore.SkiaSharpView.WPF;assembly=LiveChartsCore.SkiaSharpView.WPF"
             xmlns:vms="clr-namespace:ViewModelsSamples.Lines.XY;assembly=ViewModelsSamples">
    <UserControl.DataContext>
        <vms:ViewModel/>
    </UserControl.DataContext>
    <lvc:CartesianChart Series="{Binding Series}"/>
</UserControl>

```




# 引用

更多的代码 [https://livecharts.dev/docs/wpf/2.0.0-rc5.4/gallery](https://livecharts.dev/docs/wpf/2.0.0-rc5.4/gallery) ,

