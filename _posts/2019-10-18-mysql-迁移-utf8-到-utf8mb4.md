---
layout: post
title: "MySQL 迁移 utf8 到 utf8mb4"
date: "2019-10-18"
categories: ["数据库", "mysql"]
---

首先用如下的sql

```
use information_schema;
SELECT
  CONCAT(
    'ALTER TABLE `',
    TABLE_NAME,
    '` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;'
  ) AS mySQL
FROM
  INFORMATION_SCHEMA. TABLES
WHERE
  TABLE_SCHEMA = 'your_schema'


```

这个就会成成这个数据库每个表的更改编码的语句，然后复制这个语句，打开新的窗口，先use 这个库 ，然后粘贴过去，执行就可以了。

 

修改这个库的字符集

```
use information_schema;
ALTER DATABASE `your_schema` CHARACTER
SET = utf8mb4 COLLATE = utf8mb4_general_ci;
```
