---
title: "DbNavigator中的添加不识别sqlite的自增主键 autoincroment"
date: "2024-11-19"
categories: 
  - "lazarus"
---

我是手动设置这个主键，table1MaxId 是前面取得这个表id的最大值。

```
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
