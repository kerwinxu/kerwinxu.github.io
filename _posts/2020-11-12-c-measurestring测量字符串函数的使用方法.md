---
layout: post
title: "C# MeasureString测量字符串函数的使用方法"
date: "2020-11-12"
categories: ["计算机语言", "c"]
---

（1）在窗体中测量字符串

使用`System.Drawing.Graphics`的`MeasureString`函数 主要用它的2个重载函数

（1）`Graphics.MeasureString` 方法 `(String, Font)` ，测量用指定的 `Font` 对象绘制的指定字符串，返回 `SizeF` 结构。返回的`SizeF`就是测量字符串的打印在屏幕上的宽度和高度，默认以像素为单位，与`Form`中控件`Size`的单位一致。该函数重载中还含有一个 `StringFormat`参数，如果未指定这个参数，那么将使用`StringFormat.GenericDefault`返回的`StringFormat`进行测量，这个测量结果比较大。如果使用`StringFormat.GenericTypographic`参数测量，结果比较小。

（2）`public SizeF MeasureString(string text,Font font,SizeF layoutArea,StringFormat stringFormat, out int charactersFitted, out int linesFilled);` 这个函数能测量使用指定字体和指定矩形区域中能容纳字符串的长度和行数，其中，`layoutArea`为一个容纳字符串的矩形区域； `stringFormat`为字符串的对齐方式，字符间距，是否保持词组在同一行等属性（这个参数很重要）；`charactersFitted`返回能容纳的字符的数目；`linesFilled`返回能容纳字符的行数。 重点：默认的情况下`Graphics`返回的结果是用像素作为单位，设置`PageUnit`属性可以改变这种状态。窗体中创建`Graphics`实例直接可以使用`Control.CreateGraphics` 方法。

(2)在打印时测量字符串(`ActiveReport`)

两点注意：

(1) `Graphics`对象由打印机创建`pDoc.PrinterSettings.CreateMeasurementGraphics();` (2) 由于帐票的控件`Size`均以`inch`(英寸)或者厘米为单位，所以获得`Graphics`实例后把`PageUnit`属性设置为`GraphicsUnit.Inch;`

 

可以使用`TextRenderer.MeasureText`以更精确的测量,代码参考如下: 代码如下

```
protected override void OnPaint(PaintEventArgs e)
{
base.OnPaint(e);
string str = "测试用的字符串";
StringFormat format = new StringFormat();
format.Alignment = StringAlignment.Center;
format.LineAlignment = StringAlignment.Center;
Size size = TextRenderer.MeasureText(str, this.Font);
Rectangle rect = new Rectangle(20, 20, size.Width, size.Height);
TextRenderer.DrawText(e.Graphics, str, this.Font, rect, Color.Blue, Color.Yellow);
e.Graphics.DrawRectangle(SystemPens.ControlDarkDark, rect);
}
```

引用：

- [C# MeasureString测量字符串函数的使用方法](https://blog.csdn.net/WuLex/article/details/89951151)
