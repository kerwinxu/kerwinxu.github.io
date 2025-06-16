---
layout: post
title:  Lazarus的实时图表
date:   2025-6-3 15:17:00 +0800
categories: ["计算机语言", "lazarus"]
project: false
excerpt: Lazarus的实时图表
lang: zh
published: true
tag:
- lazarus
- TChart
---

# 步骤
1. 选择控件"TDateTimeIntervalChartSource"，用于将x轴显示成时间
   1. DateTimeFormat 设置成 "hh:mm:ss"，x时间轴的显示文本
1. 选择控件"TChart"，在控件上右键"编辑系列"
1. 这个"TChart"控件的AxisList是坐标轴，这里选择底部坐标轴(x轴)，然后选择Marks属性，
    1. 将Source属性更改为前面的TDateTimeIntervalChartSource
    1. 将Style属性更改为 smsLabel
1. 添加"折线图系列"，

用一个定时器产生随机数，然后显示这个实时曲线，如下是完整的代码
```pascal
unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, StdCtrls,
  TAGraph, TASeries, TAIntervalSources, DateUtils;

type

  { TForm1 }

  TForm1 = class(TForm)
    Chart1: TChart;
    Chart1LineSeries1: TLineSeries;
    Chart1LineSeries2: TLineSeries;
    DateTimeIntervalChartSource1: TDateTimeIntervalChartSource;
    Label1: TLabel;
    Timer1: TTimer;
    Timer2: TTimer;
    procedure FormCreate(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    function RandBetween(a,b:double):Double;
    procedure Timer2Timer(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  startTime: TDateTime;
  pointCount:int64;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Timer1Timer(Sender: TObject);
var
  rand:double;
  seconds:int64;
  i:Double;
begin
  // 产生随机数，然后添加到图表。
  rand := RandBetween(0,100);
  Chart1LineSeries1.AddXY(Now, rand);
  //// 只显示最后的
  if    Chart1LineSeries1.Count > 100 then
  begin
    Chart1LineSeries1.Delete(0);

  end;

  pointCount := pointCount + 1; // 添加一个
  seconds := secondsBetween(now, startTime);
  if seconds > 0 then
  begin
      i :=   pointCount / seconds;
      label1.Caption:= FloatToStr(i);
  end;



//
//  chart1.AxisList[1].Range.Max := now ;
//  chart1.AxisList[1].Range.Min := incsecond(now, -10);


end;

procedure TForm1.FormCreate(Sender: TObject);
begin
   startTime := now;
   pointCount := 0;
end;

function TForm1.RandBetween(a, b: double): Double;
begin
  Result := a + Random * (b - a);
end;

procedure TForm1.Timer2Timer(Sender: TObject);
var
  rand:double;
begin
  // 产生随机数，然后添加到图表。
  rand := RandBetween(0,100);
  Chart1LineSeries2.AddXY(Now, rand);
  //// 只显示最后的
  if    Chart1LineSeries2.Count > 100 then
  begin
    Chart1LineSeries2.Delete(0);
  end;

end;




end.

```

刷新率大概是60Hz，如果客户要求是50Hz以下，可以考虑用这个。


另外Marks.Range应该是坐标轴的显示范围（待验证）