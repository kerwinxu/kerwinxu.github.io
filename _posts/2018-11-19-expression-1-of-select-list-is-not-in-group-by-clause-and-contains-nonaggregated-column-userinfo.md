---
layout: post
title: "Expression #1 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'userinfo."
date: "2018-11-19"
categories: ["数据库", "mysql"]
---

安装了mysql5.7，用group by 查询时抛出如下异常：

Expression #3 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'userinfo.t\_long.user\_name' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql\_mode=only\_full\_group\_by 1 原因： MySQL 5.7.5和up实现了对功能依赖的检测。如果启用了only\_full\_group\_by SQL模式(在默认情况下是这样)，那么MySQL就会拒绝选择列表、条件或顺序列表引用的查询，这些查询将引用组中未命名的非聚合列，而不是在功能上依赖于它们。(在5.7.5之前，MySQL没有检测到功能依赖项，only\_full\_group\_by在默认情况下是不启用的。关于前5.7.5行为的描述，请参阅MySQL 5.6参考手册。)

执行以下个命令，可以查看 sql\_mode 的内容。

mysql> SHOW SESSION VARIABLES; 1 mysql> SHOW GLOBAL VARIABLES; 1 mysql> select @@sql\_mode; 1 可见session和global 的sql\_mode的值都为： ONLY\_FULL\_GROUP\_BY,STRICT\_TRANS\_TABLES,NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ERROR\_FOR\_DIVISION\_BY\_ZERO,NO\_AUTO\_CREATE\_USER,NO\_ENGINE\_SUBSTITUTION

only\_full\_group\_by说明： only\_full\_group\_by ：使用这个就是使用和oracle一样的group 规则, select的列都要在group中,或者本身是聚合列(SUM,AVG,MAX,MIN) 才行，其实这个配置目前个人感觉和distinct差不多的，所以去掉就好 官网摘抄： 官网：ONLY\_FULL\_GROUP\_BY Reject queries for which the select list, HAVING condition, or ORDER BY list refer to nonaggregated columns that are neither named in the GROUP BY clause nor are functionally dependent on (uniquely determined by) GROUP BY columns.

As of MySQL 5.7.5, the default SQL mode includes ONLY\_FULL\_GROUP\_BY. (Before 5.7.5, MySQL does not detect functional dependency and ONLY\_FULL\_GROUP\_BY is not enabled by default. For a description of pre-5.7.5 behavior, see the MySQL 5.6 Reference Manual.)

A MySQL extension to standard SQL permits references in the HAVING clause to aliased expressions in the select list. Before MySQL 5.7.5, enabling ONLY\_FULL\_GROUP\_BY disables this extension, thus requiring the HAVING clause to be written using unaliased expressions. As of MySQL 5.7.5, this restriction is lifted so that the HAVING clause can refer to aliases regardless of whether ONLY\_FULL\_GROUP\_BY is enabled.

解决： 执行以下两个命令：

mysql> set global sql\_mode='STRICT\_TRANS\_TABLES,NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ERROR\_FOR\_DIVISION\_BY\_ZERO,NO\_AUTO\_CREATE\_USER,NO\_ENGINE\_SUBSTITUTION'; 1 mysql> set session sql\_mode='STRICT\_TRANS\_TABLES,NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ERROR\_FOR\_DIVISION\_BY\_ZERO,NO\_AUTO\_CREATE\_USER,NO\_ENGINE\_SUBSTITUTION'; 1 这两个命令，去掉 sql\_mode 的 ONLY\_FULL\_GROUP\_BY

见其他文章有说： 直接修改mysql配置文件（我的系统是Ubuntu16.04的，在/etc/mysql/mysql.conf.d/mysqld.cnf 中并没有sql\_mode这个配置，所以直接加上就好，如果是其他系统有得修改就不用添加了） 这个方法暂时没有式。

mysql 配置信息读取顺序。

①ps aux|grep mysql|grep ‘my.cnf’

②mysql –help|grep ‘my.cnf’

/etc/my.cnf, /etc/mysql/my.cnf, /usr/local/etc/my.cnf, ~/.my.cnf 这些就是mysql默认会搜寻my.cnf的目录，顺序排前的优先。mysql按照上面的顺序加载配置文件，后面的配置项会覆盖前面的。

如果没有该文件可以自定义一个文件。然后回默认读取配置中的内容） 查看你需要修改的是哪个配置文件。我只有/etc/my.cnf 只修改这个文件即可

配置文件my.cnf通常会分成好几部分，如\[client\]，\[mysqld\], \[mysql\]等等。MySQL程序通常是读取与它同名的分段部分，例如服务器mysqld通常读取\[mysqld\]分段下的相关配置项。如果配置项位置不正确，该配置是不会生效的

参考：https://stackoverflow.com/questions/37951742/1055-expression-of-select-list-is-not-in-group-by-clause-and-contains-nonaggr

这个语句没试过，先记录：

set @@sql\_mode='STRICT\_TRANS\_TABLES,NO\_ZERO\_IN\_DATE,NO\_ZERO\_DATE,ERROR\_FOR\_DIVISION\_BY\_ZERO,NO\_AUTO\_CREATE\_USER,NO\_ENGINE\_SUBSTITUTION'; 1 去掉ONLY\_FULL\_GROUP\_BY即可正常执行sql. --------------------- 作者：fansili 来源：CSDN 原文：https://blog.csdn.net/fansili/article/details/78664267 版权声明：本文为博主原创文章，转载请附上博文链接！

 

在sql8.0上，要用如下的语句

```
set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
set session sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


```

没有这个 NO\_AUTO\_CREATE\_USER

 

我的方法是在my.ini上添加这个设置了，但是在mysqld上节点上的了
