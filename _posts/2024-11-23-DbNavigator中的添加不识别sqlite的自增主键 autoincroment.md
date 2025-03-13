---
lang: zh
author: Kerwin
layout: post
categories: ["编程", "lazarus"]
title:  DbNavigator中的添加不识别sqlite的自增主键 autoincroment
date:   2024-11-23
excerpt: DbNavigator中的添加不识别sqlite的自增主键 autoincroment
tags: [lazarus, delphi7,DBNavigator,autoincroment]
---  

现在用delphi的很少了，用lazarus的就更少了，我现在用的是codetyphon，更更少了，这个问题，我找了很久，最后用自己的方式暂时解决，我的方式是，我自己控制这个自增的主键，程序启动的时候，我先取得了表id的最大值，然后程序中手动添加。
```delphi
procedure TForm1.DBNavigator1Click(Sender: TObject; Button: TDBNavButtonType);
begin
  // 这里手动取得主键，然后设置
  if Button = nbInsert then
  begin
    // 我要取得最新的
    datasource1.dataset.FieldByName('id').Value:= table1MaxId;
    table1MaxId := table1MaxId + 1;
  end;
end;

```