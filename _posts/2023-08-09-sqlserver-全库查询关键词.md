---
layout: post
title: "sqlserver 全库查询关键词"
date: "2023-08-09"
categories: 
  - "数学"
---

```
DECLARE @what varchar(800)
SET @what='电气设备及线路维护费' --要搜索的字符串

DECLARE @sql varchar(8000)             -- 临时拼接的sql 
-- 游标拼接出查询字符串。
DECLARE TableCursor CURSOR LOCAL FOR   -- 定义游标，local表示本地的，不是全局的。
-- 如下的sql是一个临时变量，后边的字符串会进行运算。
SELECT sql='IF EXISTS ( SELECT 1 FROM ['+o.name+'] WHERE ['+c.name+'] LIKE ''%'+@what+'%'' ) PRINT ''所在的表及字段：['+o.name+'].['+c.name+']'''
FROM syscolumns c JOIN sysobjects o ON c.id=o.id   -- 连接表

-- 175=char 56=int 可以查 select * from sys.types
WHERE o.xtype='U' AND c.status>=0 AND c.xusertype IN (175, 239, 231, 167 )

-- 打开游标
OPEN TableCursor  
-- 查询游标数据
FETCH NEXT FROM TableCursor INTO @sql -- 将结果放在“@sql”中
WHILE @@FETCH_STATUS=0 -- 只要还有数据
BEGIN                  -- pascal类似的语法吧
    EXEC( @sql )       -- 执行这个Z“@sql”，这个应该就是上边“sql”的值。
    FETCH NEXT FROM TableCursor INTO @sql  -- 继续循环
END

CLOSE TableCursor -- 关闭游标

-- 删除游标引用
DEALLOCATE TableCursor
```
