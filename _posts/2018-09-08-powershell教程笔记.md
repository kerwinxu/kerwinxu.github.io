---
layout: post
title: "powershell教程笔记"
date: "2018-09-08"
categories: 
  - "dos_powdershell"
---

# 常用命令分类

## Get类

Get-Command ：获得所有的命令

Get-Process ： 获得所有的进程

Get-Help ： 获得帮助

Get-History ：获得当前会话中输入的命令列表。

Get-Job : 获得当前会话中运行的后台作业。

Get-FormatData ： 获得当前会话的格式化数据。

Get-Event ： 获得事件队列中的事件。

Get-Alias ：获得当前会话的别名。

Get-Colture ： 读取操作系统中设置的当前区域性

Get-Data ： 获得当前日期和事件。

Get-Host ： 表示当前主机程序的对象。

Get-Member ： 获得对象的属性和方法。

Get-Random ： 从集合中获得随机数或者随机对象。

Get-UIColture ： 获取操作系统中当前用户界面（UI)区域性设置。

Get-Unique ： 从排序列表中返回唯一项目，去重吗？

Get-Variable ： 当前控制台的变量。

Get-EventLog ：

Get-ChildItem ： 获取一个或多个位置的项和子项目

Get-Content ： 获得指定位置的项的内容。

Get-ItemProperty ： 获得指定项的属性。

Get-WmiObject ： : 获取 Windows Management Instrumentation (WMI) 类的实例或可用类的相关信息

Get-Location ： 获得当前工作位置的相关信息。

Get-PSDrive ：  获取当前会话中的 Windows PowerShell 驱动器

Get-Item ： 获得位于指定位置的项

Get-Process ： 进程

Get-Service ： 服务

Get-Transaction ： 当前（活动）事务。

Get-ExecutionPolicy ： 获取当前会话中的执行策略

## Set类

Set-Alias ： 设置别名

Set-PSDebug ： 打开和关闭脚本调试功能。

Set-StrictMode ： 建立和强制执行表达式、脚本和脚本块中的编码规则。

Set-Date ： 设置日期

Set-Variable ： 设置变量

Set-PSBreakpoint ： 在行、命令或者变量上设置断点。

Set-Location ： 将当前位置设置为指定的位置。

Set-Item ： 将项目的值更改为指定的值。

Set-Service ： 启动、停止和挂起服务并更改服务的属性。

Set-Content ： 在项中写入内容或者用新内容替代。

Set-ItemProperty ： 创建或者更改某一项的属性值。

Set-WmiInstance ： :创建或更新现有 Windows Management Instrumentation (WMI) 类的实例

Set-ExecutionPolicy ： 更改 Windows PowerShell 执行策略的用户首选项。

## Write类

Write-Host ： 将子定义输出内容写入到主机，类似net中的write（）或者writeline（）

Write-Process ： 在命令窗体内显示进度条。

Write-Debug ：将调试信息写入控制台。

Write-Verbose ：将文本写入详细消息流。

Write-Warning ： 写入警告信息。

Write-Error ：写入错误信息。

Write-Output ： 将指定对象发送到管道的下一个命令。如果这个是管道最后一个命令，则在控制台显示这些对象。

Write-EventLog ：  将事件写入到事件日志。

## Remove类

这个是删除吧。

## Select类

选择类

### Select-Object

- \-First
- \-Last
- \-property 属性
- \-excludeProperty <string\[\]> 被忽略的属性名称，会从被选择的属性列表中删除。
- \-expandProperty <string> 定一个筛选的属性, 并尝试对该属性信息进行展开(显示更多有用信息). 如果制定了一个数组的属性, 数组的每个值都会被展开.
- \-unique <SwitchParameter> 当指定此参数时, 具有相同属性和值(这些属性被用来进行筛选)的对象将被划分到一个子集中, 最终只会将子集中的一个成员输出.
- \-inputObject <psobject> 指定输入给此命令的对象.

### Select-String

- \-notMatch 不匹配的
- \-pattern 匹配
- \-context 一起查看上下文
- \-caseSensitive 不是忽略大小写的。

## Sort,Sort-Object命令

- \-Property 按照什么属性进行排序
- \-Descending 按照降序，默认是升序

两种排序方式，分主要排序和次要排序。

```
get-service |
sort-object -property @{Expression="Status";Descending=$true}, @{Expression="Name";Descending=$false} |
format-table name, status –autosize
```

## Format类

### Format-List 

- 将对象输出格式化为属性列表

### Format-Wide

- 每个对象仅有一个属性值被显示

### Format-Table

- 将输出格式化为一张表格。这是默认的输出格式，也就是说即使不指定Format-Table，powershell对对象的输出也为表格形式，此输出格式有一个缺点，就是当列宽不够时，文字会被截断（truncated）
- \-AutoSize 
- \-GroupBy指定的属性即为分组依据

### Format-Custom

- 用预定义的可选视图格式化输出。可以在Windows Powershell目录下查看\*format.PS1XML文件来决定可以选用的视图。也可以创建自己的.PS1XML视图文件。

## Group类

- ```
    ls | Group-Object Extension 根据扩展名分组
    ```
    
- 用自定义表达式分组
    - ls | Group-Object {$\_.Length -gt 1kb} 文件是否大于1kb
    - Get-Process | Group-Object Company -NoElement ，根据当前应用程序的发布者。

# 运算符

## 算术运算符

\+ - \* / %

## 赋值运算符

## 逻辑运算符

！ ： 不等于

not  ： 非

and ：

or ：

## 比较运算符

\-eq ：  等于

\-ceq ：  区分大小写的等于

\-ne ： 不等于

\-gt ： 大于

\-ge ： 大于等于

\-lt ： 小于

\-le ： 小于等于

\-contains ：  包含 ，

用法：

此数组中是否包含3:           1,2,3,5,3,2 –contains 3

返回所有等于3的元素:        1,2,3,5,3,2 –eq 3

返回所有小于3的元素:         1,2,3,5,3,2 –lt 3

测试 2 是否存在于集合中:   if (1, 3, 5 –contains 2)

## 调用运算符

## 字符串运算符

\+ ： 连接2个字符串

\*：按照指定次数重复字符串

\-f： 设置字符串格式。

\-replace ： 替换字符串，

\-match ： 正则表达式匹配

\-like ： 通配符匹配

## 其他运算符

, 数组构造

...  范围运算符

\-is 类型鉴别器

\-as 类型转换器

\-band  ：二进制与

\-bor ： 二进制或

\-bnot ：二进制非

# 条件控制语法

## 循环类

### foreach

-  foreach($i in $var)
- "a","b","c","d" | foreach ： 直接获得管道数据。

### while

- while($n -le 5)    #当$n小于等于5时进行下面操作

### do...while

### do...until

## 分支类

### if ... elseif ... else

### switch

$a = 3  
switch($a)  
{  
1  
{"It's one";break}   #break:表示若匹配跳出swith语句  
2  
{"It's two";break}  
3  
{"It's three";break}  
4  
{"It's four";break}  
5  
{"It's five";break}  
default  
{"It's unknown";break}  
}

用法二如下:switch -casesensitive (表达式)表示区分大小写

用法三如下:switch -regex(表达式)表示正则表达式匹配

$day = "day5"  
switch -regex ($day)  
{  
^\[a-z\]+$  
{"字母,匹配为:" +$\_ ;break}  
^\[/d\]+$  
{"数字,匹配为:" +$\_ ;break}  
^/w+$  
{"字母+数字,匹配为:" +$\_ ;break}  
default  
{"什么都不是" +$\_;break}  
}

用法四如下:switch -regex(表达式)表示正则表达式匹配 表达式可为数组

$day = "day5","day6"  
switch -regex ($day)  
{  
^\[a-z\]+$  
{"字母,匹配为:" +$\_ ;}  
^\[/d\]+$  
{"数字,匹配为:" +$\_ ;}  
^/w+$  
{"字母+数字,匹配为:" +$\_ ;}  
default  
{"什么都不是" +$\_;}  
}

用法五如下:switch -wildcard (表达式)表示通配符匹配

$day = "day2"  
switch -wildcard ($day)  
{  
day2  
{"day2,匹配为:" + $\_;break}  
day3  
{"day3,匹配为:" + $\_;break}  
day\*  
{"通配符,匹配为:" + $\_;break}  
default  
{"什么都不是:" +$\_;break}  
}

## 跳转类

### break

### continue

### Throw

Throw  字符串|异常|ErrorRecord
