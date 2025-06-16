---
layout: post
title:  LiveChart2实时曲线
date:   2025-3-31 21:51:00 +0800
categories: ["计算机语言","c#"]
project: false
excerpt: LiveChart2实时曲线
lang: zh
published: true
tag:
- c#
- Live2Chart2
- 实时曲线
- wpf
---

# 安装
这个LiveChart2是预发行版，需要勾选，nuget中安装LiveChartsCore.SkiaSharpView.WPF
# xmal

```
xmlns:lvc="clr-namespace:LiveChartsCore.SkiaSharpView.WPF;assembly=LiveChartsCore.SkiaSharpView.WPF"
```
```
<lvc:CartesianChart
    Grid.Row="0"
    Grid.Column="1"
    Grid.RowSpan="2"
    Series="{Binding Series}" 
    XAxes="{Binding XAxes}"
    YAxes="{Binding YAxes}"
	LegendPosition="Right"
    />
```
# 代码
```c#
    private ISeries[]    series;
    /// <summary>
    /// 曲线图
    /// </summary>
    public ISeries[] Series
    {
        get { return series; }
        set { series = value; RaisePropertyChanged(() => Series); }
    }

    // 定义X轴的属性
    public Axis[] XAxes { get; set; } = {
    new Axis
    {
        // 设置X轴的最小值为当前时间减去60秒的Ticks，最大值为当前时间加上60秒的Ticks
        //MinLimit = DateTime.Now.AddDays(-1).Ticks,
        //MaxLimit = DateTime.Now.AddDays(1).Ticks,
        
        // 设置标签格式化器，以便每个刻度都显示为时间,注意，得是DateTime.FromBinary生成时间，不然会报错
        Labeler = value => DateTime.FromBinary((long)value).ToString("HH:mm:ss") ,
        LabelsRotation = 15,
        // 设置单位宽度为1秒
        UnitWidth = TimeSpan.FromSeconds(1).Ticks,

        // 设置最小步长为1秒，确保每秒都有刻度
        // MinStep = TimeSpan.FromSeconds(1).Ticks,

        // 显示分隔线
        ShowSeparatorLines = true,
        SeparatorsPaint = new SolidColorPaint(SKColors.LightSlateGray)
        {
            StrokeThickness = 2, // 分隔线的粗细
            PathEffect = new DashEffect(new float[] { 3, 3 }) // 分隔线的虚线效果
        },

        // 设置文本大小
        TextSize = 14,

        // 设置轴的位置（底部）
        Position = AxisPosition.Start,
    }
};

    // 定义Y轴的属性
    public Axis[] YAxes { get; set; } = {
        new Axis
        {
            //MinLimit = 0, // 设置最小值
            //MaxLimit = 300, // 设置最大值
            ShowSeparatorLines = true, // 显示分隔线
            SeparatorsPaint = new SolidColorPaint(new SkiaSharp.SKColor(0, 0, 0),1), // 分隔线的颜色和粗细
            TextSize = 20, // 设置文本大小
        }
    };

    /// <summary>
    /// 初始化图表，要绑定数据的。
    /// </summary>
    private void init_series()
    {
        Series = new LineSeries<DateTimePoint>[max_ids];
        Values = new ObservableCollection<DateTimePoint>[max_ids];
        // 动态的创建
        for (int i = 0; i < max_ids; i++)
        {
            Values[i] = new ObservableCollection<DateTimePoint>();
            Series[i] = new LineSeries<DateTimePoint>
            {
                Values= Values[i],
                Name = $"{CHP2000Models[i].SlaveId}",
                Fill = null,
                GeometryFill = null,
                GeometryStroke = null,
            };
        }
    }

    

    private ObservableCollection<DateTimePoint>[] values;
    /// <summary>
    /// 数据的数组
    /// </summary>
    public ObservableCollection<DateTimePoint>[] Values
    {
        get { return values; }
        set { values = value; RaisePropertyChanged(() => Values); }
    }


    private int max_points = 200;


    /// <summary>
    ///  添加到图表中。45
    /// </summary>
    private void append_series()
    {
        DateTime now = DateTime.Now;
        DispatcherHelper.CheckBeginInvokeOnUI(() => {
            for (global::System.Int32 i = 0; i < max_ids; i++)
            {
                DateTimePoint dateTimePoint = new DateTimePoint(
                    now,
                    CHP2000Models[i].Data == null ? 0 : CHP2000Models[i].Data
                    );
                Values[i].Add( dateTimePoint );
                // 不能超过值
                while (Values[i].Count > max_points)
                {
                    Values[i].RemoveAt(0);
                }
            }
        });

    }
```