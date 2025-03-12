---
layout: post
title: "WPF的DrawingVisual绘制高性能曲线图"
date: "2024-07-19"
categories: 
  - "c"
---

1.  写主机容器
    
    ```
    using System;
    using System.Collections.Generic;
    using System.Globalization;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;
    using System.Windows.Media;
    using System.Windows;
    
    namespace DrawingVisual绘制高性能曲线图
    {
    
        /// <summary>
        /// 主机容器，容纳Visual的
        /// </summary>
        public class CruveChartDrawingVisual : FrameworkElement
        {
            private List<Visual> visuals = new List<Visual>();
            private DrawingVisual Layer;
    
            private double offset_x = 0;//滑动条偏移值
            private double y_scale;//y轴方向缩放比例
    
            private List<int> list_points;//曲线数据
    
            private static int Top_Val_Max = 100;//y轴最大值
            private static int Top_Val_Min = 0;//y轴最小值
            private static int X_Sex = 20;//x轴分度值
            private static int Y_Sex = 20;//y轴分度值
            private static int Bottom = 30;//底部x轴坐标显示高度
    
            Pen pen = new Pen(Brushes.Green, 2);
            Pen primarygrid_pen = new Pen(Brushes.Black, 1);
            Pen secondgrid_pen = new Pen(Brushes.Gray, 1);
    
            public CruveChartDrawingVisual()
            {
                pen.Freeze();//冻结笔，提高性能关键所在
                primarygrid_pen.Freeze();
                secondgrid_pen.Freeze();
    
                Layer = new DrawingVisual();
    
                visuals.Add(Layer);
            }
    
            public void SetupData(List<int> points)
            {
                list_points = points;
                offset_x = 0;
                DrawContent();
            }
    
            public void OffsetX(double offset)
            {
                offset_x = offset;
                DrawContent();
                InvalidateVisual();
            }
    
            private void DrawContent()
            {
                var dc = Layer.RenderOpen();
                y_scale = (RenderSize.Height - Bottom) / (Top_Val_Max - Top_Val_Min);
    
                var mat = new Matrix();
                mat.ScaleAt(1, -1, 0, RenderSize.Height / 2);
    
                mat.OffsetX = -offset_x;
                dc.PushTransform(new MatrixTransform(mat));
    
                //横线
                for (int y = 0; y <= Top_Val_Max - Top_Val_Min; y += 10)
                {
                    Point point1 = new Point(offset_x, y * y_scale + Bottom);
                    Point point2 = new Point(offset_x + RenderSize.Width, y * y_scale + Bottom);
                    if (y % Y_Sex == 0)
                    {
                        dc.DrawLine(primarygrid_pen, point1, point2);
                        continue;
                    }
                    dc.DrawLine(secondgrid_pen, point1, point2);
                }
    
                //竖线与文字
                for (int i = 0; i <= (offset_x + RenderSize.Width); i += X_Sex * 2)
                {
                    if (i < offset_x)
                    {
                        continue;
                    }
                    var point1 = new Point(i, Bottom);
                    var point2 = new Point(i, (Top_Val_Max - Top_Val_Min) * y_scale + Bottom);
    
    
                    //y轴文字
                    if (i % 100 == 0)
                    {
                        var text1 = new FormattedText(i + "", CultureInfo.CurrentCulture, FlowDirection.LeftToRight, new Typeface("Verdana"), 16, Brushes.Black);
                        var mat3 = new Matrix();
                        mat3.ScaleAt(1, -1, i - text1.Width / 2, 8 + text1.Height / 2);
                        dc.PushTransform(new MatrixTransform(mat3));
                        dc.DrawText(text1, new Point(i - text1.Width / 2, 8));
                        dc.Pop();
                    }
    
                    //表格刻度文字
                    if (i % 100 == 0)
                    {
                        for (int y = Top_Val_Min; y <= Top_Val_Max; y += 10)
                        {
                            if (y % Y_Sex == 0)
                            {
                                var text1 = new FormattedText(y + "", CultureInfo.CurrentCulture, FlowDirection.LeftToRight, new Typeface("Verdana"), 12, Brushes.Black);
                                var mat3 = new Matrix();
                                mat3.ScaleAt(1, -1, i + 1, (y - Top_Val_Min) * y_scale + Bottom + text1.Height / 2);
                                dc.PushTransform(new MatrixTransform(mat3));
                                dc.DrawText(text1, new Point(i + 1, (y - Top_Val_Min) * y_scale + Bottom));
                                dc.Pop();
                            }
                        }
                        //深色竖线
                        dc.DrawLine(primarygrid_pen, point1, point2);
                        continue;
                    }
                    //浅色竖线
                    dc.DrawLine(secondgrid_pen, point1, point2);
                }
    
                if (list_points != null)
                {
                    for (int i = (int)offset_x; i < list_points.Count - 1; i++)
                    {
                        if (i > offset_x + RenderSize.Width)
                        {
                            break;
                        }
                        dc.DrawLine(pen, new Point(i, list_points[i] * y_scale + Bottom), new Point(i + 1, list_points[i + 1] * y_scale + Bottom));
                    }
                }
    
                dc.Pop();
                dc.Close();
            }
    
            protected override int VisualChildrenCount => visuals.Count;
            protected override Visual GetVisualChild(int index)
            {
                return visuals[index];
            }
    
            protected override void OnRenderSizeChanged(SizeChangedInfo sizeInfo)
            {
                DrawContent();
                base.OnRenderSizeChanged(sizeInfo);
            }
    
            protected override void OnRender(DrawingContext drawingContext)
            {
                drawingContext.DrawRectangle(Brushes.White, null, new Rect(0, 0, RenderSize.Width, RenderSize.Height));
                base.OnRender(drawingContext);
            }
        }
    }
    
    ```
    
     
2. xaml中显示
    
    ```
    <Window x:Class="DrawingVisual绘制高性能曲线图.MainWindow"
            xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
            xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
            xmlns:local="clr-namespace:DrawingVisual绘制高性能曲线图"
            mc:Ignorable="d"  Loaded="Window_Loaded"
            Title="MainWindow" Height="450" Width="800">
        <Grid>
            <!-- 在这个CruveChartDrawingVisual上绘制图片-->
            <local:CruveChartDrawingVisual x:Name="curve" Margin="0,15,0,20" />
            <!--如下这个是滚动条-->
            <ScrollViewer
            Name="scroll"
            HorizontalScrollBarVisibility="Auto"
            ScrollChanged="ScrollViewer_ScrollChanged"
            VerticalScrollBarVisibility="Disabled">
                <!--这个画布的宽度设置成跟CruveChartDrawingVisual一样的。画布上没有图像，看到的图像是CruveChartDrawingVisual的-->
                <Canvas x:Name="canvas" Height="1" />
            </ScrollViewer>
        </Grid>
    </Window>
    
    ```
    
     
3. 代码后台中生成数据
    
    ```
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Text;
    using System.Threading.Tasks;
    using System.Windows;
    using System.Windows.Controls;
    using System.Windows.Data;
    using System.Windows.Documents;
    using System.Windows.Input;
    using System.Windows.Media;
    using System.Windows.Media.Imaging;
    using System.Windows.Navigation;
    using System.Windows.Shapes;
    
    namespace DrawingVisual绘制高性能曲线图
    {
        /// <summary>
        /// MainWindow.xaml 的交互逻辑
        /// </summary>
        public partial class MainWindow : Window
        {
            public MainWindow()
            {
                InitializeComponent();
            }
    
            private bool isAdd = true;
            private void Window_Loaded(object sender, RoutedEventArgs e)
            {
                // 如下是生成数据
                List<int> lists = new List<int>();
                int temp = 20;
                for (int i = 0; i < 60 * 60; i++)
                {
                    if (isAdd)
                    {
                        lists.Add(temp);
                        temp++;
                    }
                    else
                    {
                        lists.Add(temp);
                        temp--;
                    }
    
                    if (temp == 90) isAdd = false;
                    if (temp == 10) isAdd = true;
                }
    
                // 设置画布的宽度，实际上这个画布上没有图像，纯粹是为了配合滚动条。
                canvas.Width = lists.Count;
                // 填充数据
                curve.SetupData(lists);
            }
    
            /// <summary>
            /// 当滚动条移动的时候，curve也移动。
            /// </summary>
            /// <param name="sender"></param>
            /// <param name="e"></param>
            private void ScrollViewer_ScrollChanged(object sender, ScrollChangedEventArgs e)
            {
                curve.OffsetX(scroll.HorizontalOffset);
            }
        }
    }
    
    ```
    
     

总体上，先写一个控件（主机，容纳Visual)，然后前台xaml，然后后台代码。
