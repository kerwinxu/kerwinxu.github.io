---
layout: post
title: "PANDAS 数据合并与重塑（join/merge篇）"
date: "2018-02-27"
categories: 
  - "python"
---

在[上一篇](http://blog.csdn.net/stevenkwong/article/details/52528616)文章中，我整理了pandas在数据合并和重塑中常用到的concat方法的使用说明。在这里，将接着介绍pandas中也常常用到的join 和merge方法

# merge

pandas的merge方法提供了一种类似于SQL的内存链接操作，官网文档提到它的性能会比其他开源语言的数据操作（例如R）要高效。

和SQL语句的对比可以看[这里](http://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#compare-with-sql-join)

**merge的参数**

on：列名，join用来对齐的那一列的名字，用到这个参数的时候一定要保证左表和右表用来对齐的那一列都有相同的列名。

left\_on：左表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。

right\_on：右表对齐的列，可以是列名，也可以是和dataframe同样长度的arrays。

left\_index/ right\_index: 如果是True的haunted以index作为对齐的key

how：数据融合的方法。

sort：根据dataframe合并的keys按字典顺序排序，默认是，如果置false可以提高表现。

```
merge的默认合并方法：
    merge用于表内部基于 index-on-index 和 index-on-column(s) 的合并，但默认是基于index来合并。
```

- 1
- 2
- 3

## 1.1 复合key的合并方法

```
使用merge的时候可以选择多个key作为复合可以来对齐合并。
```

- 1
- 2

### 1.1.1 通过on指定数据合并对齐的列

```
In [41]: left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
   ....:                      'key2': ['K0', 'K1', 'K0', 'K1'],
   ....:                      'A': ['A0', 'A1', 'A2', 'A3'],
   ....:                      'B': ['B0', 'B1', 'B2', 'B3']})
   ....: 

In [42]: right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
   ....:                       'key2': ['K0', 'K0', 'K0', 'K0'],
   ....:                       'C': ['C0', 'C1', 'C2', 'C3'],
   ....:                       'D': ['D0', 'D1', 'D2', 'D3']})
   ....: 

In [43]: result = pd.merge(left, right, on=['key1', 'key2'])
```

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11
- 12
- 13

![这里写图片描述](http://img.blog.csdn.net/20160918152218387) 没有指定how的话默认使用inner方法。

how的方法有：

#### left

只保留左表的所有数据

```
In [44]: result = pd.merge(left, right, how='left', on=['key1', 'key2'])
```

- 1

![这里写图片描述](http://img.blog.csdn.net/20160918152652584)

#### right

只保留右表的所有数据

```
In [45]: result = pd.merge(left, right, how='right', on=['key1', 'key2'])
```

- 1

![这里写图片描述](http://img.blog.csdn.net/20160918152838290)

#### outer

保留两个表的所有信息

```
In [46]: result = pd.merge(left, right, how='outer', on=['key1', 'key2'])
```

- 1

![这里写图片描述](http://img.blog.csdn.net/20160918153031886)

#### inner

只保留两个表中公共部分的信息

```
In [47]: result = pd.merge(left, right, how='inner', on=['key1', 'key2'])
```

- 1

![这里写图片描述](http://img.blog.csdn.net/20160918153214049)

## 1.2 indicator

v0.17.0 版本的pandas开始还支持一个indicator的参数，如果置True的时候，输出结果会增加一列 ’ \_merge’。\_merge列可以取三个值

1. left\_only 只在左表中
2. right\_only 只在右表中
3. both 两个表中都有

## 1.3 join方法

dataframe内置的join方法是一种快速合并的方法。它默认以index作为对齐的列。

### 1.3.1 how 参数

join中的how参数和merge中的how参数一样，用来指定表合并保留数据的规则。

具体可见前面的 how 说明。

### 1.3.2 on 参数

在实际应用中如果右表的索引值正是左表的某一列的值，这时可以通过将 右表的索引 和 左表的列 对齐合并这样灵活的方式进行合并。

ex 1

```
In [59]: left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
   ....:                      'B': ['B0', 'B1', 'B2', 'B3'],
   ....:                      'key': ['K0', 'K1', 'K0', 'K1']})
   ....: 

In [60]: right = pd.DataFrame({'C': ['C0', 'C1'],
   ....:                       'D': ['D0', 'D1']},
   ....:                       index=['K0', 'K1'])
   ....: 

In [61]: result = left.join(right, on='key')
```

- 1
- 2
- 3
- 4
- 5
- 6
- 7
- 8
- 9
- 10
- 11

![这里写图片描述](http://img.blog.csdn.net/20160918154752800)

### 1.3.3 suffix后缀参数

如果和表合并的过程中遇到有一列两个表都同名，但是值不同，合并的时候又都想保留下来，就可以用suffixes给每个表的重复列名增加后缀。

```
In [79]: result = pd.merge(left, right, on='k', suffixes=['_l', '_r'])
```

- 1
- 2

![这里写图片描述](http://img.blog.csdn.net/20160918160131490)

\*　另外还有lsuffix 和 rsuffix分别指定左表的后缀和右表的后缀。

## 1.4 组合多个dataframe

一次组合多个dataframe的时候可以传入元素为dataframe的列表或者tuple。一次join多个，一次解决多次烦恼~

```
In [83]: right2 = pd.DataFrame({'v': [7, 8, 9]}, index=['K1', 'K1', 'K2'])

In [84]: result = left.join([right, right2])
```

- 1
- 2
- 3

![这里写图片描述](http://img.blog.csdn.net/20160918160941503)

## 1.5 更新表的nan值

### 1.5.1 combine\_first

如果一个表的nan值，在另一个表相同位置（相同索引和相同列）可以找到，则可以通过combine\_first来更新数据

### 1.5.2 update

如果要用一张表中的数据来更新另一张表的数据则可以用update来实现

### 1.5.3 combine\_first 和 update 的区别

使用combine\_first会只更新左表的nan值。而update则会更新左表的所有能在右表中找到的值（两表位置相对应）。

示例代码参考来源——[官网](http://pandas.pydata.org/pandas-docs/stable/merging.html)
