---
title: "zeos中ZTable筛选"
date: "2024-11-19"
categories: 
  - "lazarus"
---

```
procedure TForm1.Button1Click(Sender: TObject);
begin
  // 我搜索
  ZTable1.Filtered:=false;
  ZTable1.Filter:= 'text1 like ' + QuotedStr('*乐*');    // 是*号，不是%。    QuotedStr是双引号
  ZTable1.Filtered:=true;
end;
```
