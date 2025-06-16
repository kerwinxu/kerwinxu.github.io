---
layout: post
title: "vs2019中使用Entity FrameWork错误总结"
date: "2020-11-26"
categories: ["计算机语言", "c"]
---

有两种闪退：

解决方式1、

将D:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\PrivateAssemblies目录下的Mysql.Data.dll的版本（也就是mysql for visual studio）跟mysql for net的版本一致。

解决方式2、

这个会在mysql的log上显示如下的内容

```
C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqld.exe: ready for connections. Version: '8.0.21'  socket: ''  port: 3306  MySQL Community Server - GPL.
03:43:55 UTC - mysqld got exception 0xc0000005 ;
Most likely, you have hit a bug, but this error can also be caused by malfunctioning hardware.
Thread pointer: 0x2df95c45180
Attempting backtrace. You can use the following information to find out
where mysqld died. If you see no messages after this, something went
terribly wrong...
7ff6970af74b    mysqld.exe!?get_full_info@Item_aggregate_type@@IEAAXPEAVItem@@@Z()
7ff6970a28d6    mysqld.exe!??0Item_aggregate_type@@QEAA@PEAVTHD@@PEAVItem@@@Z()
7ff69732b288    mysqld.exe!?prepare@SELECT_LEX_UNIT@@QEAA_NPEAVTHD@@PEAVQuery_result@@_K2@Z()
7ff69739dd0e    mysqld.exe!?resolve_derived@TABLE_LIST@@QEAA_NPEAVTHD@@_N@Z()
7ff6973540d6    mysqld.exe!?resolve_placeholder_tables@SELECT_LEX@@QEAA_NPEAVTHD@@_N@Z()
7ff6973525aa    mysqld.exe!?prepare@SELECT_LEX@@QEAA_NPEAVTHD@@@Z()
7ff69732b191    mysqld.exe!?prepare@SELECT_LEX_UNIT@@QEAA_NPEAVTHD@@PEAVQuery_result@@_K2@Z()
7ff69739dd0e    mysqld.exe!?resolve_derived@TABLE_LIST@@QEAA_NPEAVTHD@@_N@Z()
7ff6973540d6    mysqld.exe!?resolve_placeholder_tables@SELECT_LEX@@QEAA_NPEAVTHD@@_N@Z()
7ff6973525aa    mysqld.exe!?prepare@SELECT_LEX@@QEAA_NPEAVTHD@@@Z()
7ff69732b191    mysqld.exe!?prepare@SELECT_LEX_UNIT@@QEAA_NPEAVTHD@@PEAVQuery_result@@_K2@Z()
7ff69739dd0e    mysqld.exe!?resolve_derived@TABLE_LIST@@QEAA_NPEAVTHD@@_N@Z()
7ff6973540d6    mysqld.exe!?resolve_placeholder_tables@SELECT_LEX@@QEAA_NPEAVTHD@@_N@Z()
7ff6973525aa    mysqld.exe!?prepare@SELECT_LEX@@QEAA_NPEAVTHD@@@Z()
7ff6972a980c    mysqld.exe!?prepare_inner@Sql_cmd_select@@MEAA_NPEAVTHD@@@Z()
7ff6972a942c    mysqld.exe!?prepare@Sql_cmd_dml@@UEAA_NPEAVTHD@@@Z()
7ff6972a5ef5    mysqld.exe!?execute@Sql_cmd_dml@@UEAA_NPEAVTHD@@@Z()
7ff6971ad36d    mysqld.exe!?mysql_execute_command@@YAHPEAVTHD@@_N@Z()
7ff6971adfc9    mysqld.exe!?mysql_parse@@YAXPEAVTHD@@PEAVParser_state@@@Z()
7ff6971a6eb2    mysqld.exe!?dispatch_command@@YA_NPEAVTHD@@PEBTCOM_DATA@@W4enum_server_command@@@Z()
7ff6971a7e6e    mysqld.exe!?do_command@@YA_NPEAVTHD@@@Z()
7ff696ff26c8    mysqld.exe!?modify_thread_cache_size@Per_thread_connection_handler@@SAXK@Z()
7ff6982b22a1    mysqld.exe!?set_compression_level@Zstd_comp@compression@transaction@binary_log@@UEAAXI@Z()
7ff697eb739c    mysqld.exe!?my_thread_join@@YAHPEAUmy_thread_handle@@PEAPEAX@Z()
7ff947cd14c2    ucrtbase.dll!_configthreadlocale()
7ff949a57034    KERNEL32.DLL!BaseThreadInitThunk()
7ff949f9cec1    ntdll.dll!RtlUserThreadStart()
Trying to get some variables.
Some pointers may be invalid and cause the dump to abort.
Query (2df977d1768): SELECT
`Project7`.`C12` AS `C1`,
`Project7`.`C1` AS `C2`,
`Project7`.`C2` AS `C3`,
`Project7`.`C3` AS `C4`,
`Project7`.`C4` AS `C5`,
`Project7`.`C5` AS `C6`,
`Project7`.`C6` AS `C7`,
`Project7`.`C7` AS `C8`,
`Project7`.`C8` AS `C9`,
`Project7`.`C9` AS `C10`,
`Project7`.`C10` AS `C11`
FROM (SELECT
`UnionAll3`.`SchemaName` AS `C1`,
`UnionAll3`.`Name` AS `C2`,
`UnionAll3`.`ReturnTypeName` AS `C3`,
`UnionAll3`.`IsAggregate` AS `C4`,
`UnionAll3`.`C1` AS `C5`,
`UnionAll3`.`IsBuiltIn` AS `C6`,
`UnionAll3`.`IsNiladic` AS `C7`,
`UnionAll3`.`C2` AS `C8`,
`UnionAll3`.`C3` AS `C9`,
`UnionAll3`.`C4` AS `C10`,
`UnionAll3`.`C5` AS `C11`,
1 AS `C12`
FROM ((SELECT
`Extent1`.`SchemaName`,
`Extent1`.`Name`,
`Extent1`.`ReturnTypeName`,
`Extent1`.`IsAggregate`,
1 AS `C1`,
`Extent1`.`IsBuiltIn`,
`Extent1`.`IsNiladic`,
`UnionAll1`.`Name` AS `C2`,
`UnionAll1`.`TypeName` AS `C3`,
`UnionAll1`.`Mode` AS `C4`,
`UnionAll1`.`Ordinal` AS `C5`
FROM (
SELECT /* Funct
Connection ID (thread ID): 12
Status: NOT_KILLED
The manual page at http://dev.mysql.com/doc/mysql/en/crashing.html contains
information that should help you find out what is causing the crash.
```

解决方式为：

This proved to be a bug in the new query optimizations, but I was able to find a workaround by disabling some of the optimizations on the server.

Here is the command I used:

```
use mysql;
Set global optimizer_switch='derived_merge=off,subquery_to_derived=off,prefer_ordering_index=off,semijoin=off';
```

引用 ：

- [MySQL crash while generating entity data model in Visual Studio 2019](https://stackoverflow.com/questions/63362585/mysql-crash-while-generating-entity-data-model-in-visual-studio-2019)
