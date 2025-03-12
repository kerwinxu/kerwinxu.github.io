---
layout: post
title: "pandasSeries -> DataFrame 转换方法"
date: "2020-11-10"
categories: 
  - "python"
---

### 写在前面

在实际工作中，若遇到以下情况，则必须要进行series和dataframe的转换。 - 使用seaborn进行可视化，输入的数据必须为dataframe

- 在通过pandas读取文件后，然后进行了聚合操作。可以看出聚合后输出为series。

```
df.groupby(
    ['by=None', 'axis=0', 'level=None', 'as_index=True', 'sort=True', 'group_keys=True', 'squeeze=False', 'observed=False', '**kwargs'],
)
#Group series using mapper (dict or key function, apply given function
#to group, return result as series) or by a series of columns.
```

对聚合操作后的数据（此时已经是从dataframe转换至series），那么就需要进行series至dataframe的转换。

```
group.reset_index(level=None, drop=False, name=None, inplace=False)
#Generate a new DataFrame or Series with the index reset.
```
