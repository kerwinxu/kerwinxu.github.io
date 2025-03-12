---
layout: post
title: "matplotlib-绘制精美的图表"
date: "2017-06-17"
categories: 
  - "python"
---

 

1. 快速绘图：matplotlib的pyplot子库提供了快速绘制2D图表
    1. 载入用：  import matplotlib.pyplot as plt
    2. 创建绘制屏幕：  plt. figure(figsize=(8, 4)) ， figsize参数可以指定绘图对象的宽度和高度，单位为英寸；
    3. 绘制：
        1. plt. plot(x,y,label="$sin(x)$",color="red",linewidth=2) ，绘制线
        2. plt. xlabel("Time(s)") ，设置X轴文字
        3. plt. ylabel("Volt") ， 设置Y轴文字
        4. plt. title("PyPlot First Example") ，设置图表的标题
        5. plt. ylim(-1.2, 1.2) ， 设置Y轴的范围
        6. plt. legend() ， 显示图示，必须得加上这个，才会显示图示。
    4. 显示， plt.show()显示出我们创建的所有绘图对象。
2. matplotlib所绘制的图的每个组成部分都对应有一个对象，
    1. line, = plt. plot(x, x\*x) # plot返回一个列表，通过line,获取其第一个元素， line. set\_antialiased(False) #调用Line2D对象的set\_\*方法设置属性值
    2. 同样我们可以通过调用Line2D对象的get\_\*方法，或者plt.getp函数获取对象的属性值
    3. lines = plt. plot(x, np. sin(x), x, np. cos(x))  # 同时绘制sin和cos两条曲线，lines是一个有两个Line2D对象的列表 plt. setp(lines, color="r", linewidth=2.0)  # 调用setp函数同时配置多个Line2D对象的多个属性值
    4. matplotlib的整个图表为一个Figure对象 ， 此对象在调用plt.figure函数时返回，我们也可以通过 plt.gcf函数获取当前的绘图对象
3. 绘制多轴图，
    1. subplot(numRows, numCols, plotNum) ， 域等分为numRows行 \* numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号，左上的子区域的编号为1。
    2. 在这个子图下的绘图，就会显示在这个子图中。
4. Artists分为简单类型和容器类型两种
    1. 类型的Artists为标准的绘图元件，例如Line2D、 Rectangle、 Text、AxesImage 等等。
    2. 而容器类型则可以包含许多简单类型的Artists，使它们组织成一个整体，例如Axis、 Axes、Figure等。
    3. 直接使用Artists创建图表的标准流程如下
        1. 创建Figure对象
        2. 用Figure对象创建一个或者多个Axes或者Subplot，Subplot返回的就是Axes对象，不同的子图
        3. 调用Axies等对象的方法创建各种简单类型的Artists
5. Artist对象
    1. 分为简单类型和容器类型2种。
        1. 简单类型的Artists为标准的绘图元件，例如Line2D、 Rectangle、 Text、AxesImage 等等
        2. 容器类型则可以包含许多简单类型的Artists，使它们组织成一个整体，例如Axis、 Axes、Figure等。
    2. Artist对象的属性：Artist对象的所有属性都通过相应的 get\_\* 和 set\_\* 函数进行读写
        1. alpha : 透明度，值在0到1之间，0为完全透明，1为完全不透明
        2. animated : 布尔值，在绘制动画效果时使用
        3. axes : 此Artist对象所在的Axes对象，可能为None
        4. clip\_box : 对象的裁剪框
        5. clip\_on : 是否裁剪
        6. clip\_path : 裁剪的路径
        7. contains : 判断指定点是否在对象上的函数
        8. figure : 所在的Figure对象，可能为None
        9. label : 文本标签
        10. picker : 控制Artist对象选取
        11. transform : 控制偏移旋转
        12. visible : 是否可见
        13. zorder : 控制绘图顺序
    3. Figure容器 ，这个相当于是画布了吧。
        1. axes : Axes对象列表,add\_subplot或者add\_axes方法 添加子图。delaxes 删除子图。
        2. patch : 作为背景的Rectangle对象
        3. images : FigureImage对象列表，用来显示图片
        4. legends : Legend对象列表
        5. lines : Line2D对象列表
        6. patches : patch对象列表
        7. texts : Text对象列表，用来显示文字
    4. Axes容器 :它包含了组成图表的众多Artist对象
        1. 属性：
            1. artists : Artist对象列表
            2. patch : 作为Axes背景的Patch对象，可以是Rectangle或者Circle
            3. collections : Collection对象列表
            4. images : AxesImage对象列表
            5. legends : Legend对象列表
            6. lines : Line2D对象列表
            7. patches : Patch对象列表
            8. texts : Text对象列表
            9. xaxis : XAxis对象
            10. yaxis : YAxis对象
        2. 方法：
            1. <table class="docutils" border="1"><colgroup><col width="30%"> <col width="39%"> <col width="32%"></colgroup><tbody valign="top"><tr><td style="width: 147px;">Axes的方法</td><td style="width: 191px;">所创建的对象</td><td style="width: 153px;">添加进的列表</td></tr><tr><td style="width: 147px;">annotate （标注）</td><td style="width: 191px;">Annotate</td><td style="width: 153px;">texts</td></tr><tr><td style="width: 147px;">bars</td><td style="width: 191px;">Rectangle</td><td style="width: 153px;">patches</td></tr><tr><td style="width: 147px;">errorbar</td><td style="width: 191px;">Line2D, Rectangle</td><td style="width: 153px;">lines,patches</td></tr><tr><td style="width: 147px;">fill</td><td style="width: 191px;">Polygon</td><td style="width: 153px;">patches</td></tr><tr><td style="width: 147px;">hist （条状图）</td><td style="width: 191px;">Rectangle</td><td style="width: 153px;">patches</td></tr><tr><td style="width: 147px;">imshow</td><td style="width: 191px;">AxesImage</td><td style="width: 153px;">images</td></tr><tr><td style="width: 147px;">legend</td><td style="width: 191px;">Legend</td><td style="width: 153px;">legends</td></tr><tr><td style="width: 147px;">plot</td><td style="width: 191px;">Line2D</td><td style="width: 153px;">lines</td></tr><tr><td style="width: 147px;">scatter</td><td style="width: 191px;">PolygonCollection</td><td style="width: 153px;">Collections</td></tr><tr><td style="width: 147px;">text</td><td style="width: 191px;">Text</td><td style="width: 153px;">texts</td></tr></tbody></table>
                
            2. 方法：
    5. Axis容器
        1. Axis容器包括坐标轴上的刻度线、刻度文本、坐标网格以及坐标轴标题等内容。
