---
layout: post
title: "tensorflow维度变换"
date: "2021-01-31"
categories: 
  - "python"
---

# 增加维度

tensorflow2的卷积神经网络需要的输入数据是4维的，这里更改维度的方法是

```
x=np.expand_dims(x,axis=3)
```

- tf.expand\_dims(x, axis)可在指定的axis 轴前可以插入一个新的维度
    - tf.expand\_dims 的axis 为正时，表示在当前维度之前插入一个新维度；为负时，表示当前维度之后插入一个新的维度
    - logits and labels must have the same first dimension，如果其他维度会出现这个错误。

# 删除维度

是增加维度的逆操作，与增加维度一样，删除维度只能删除长度为1 的维度，也不会改变张量的存储。

可以通过tf.squeeze(x, axis)函数，axis 参数为待删除的维度的索引号.

如果不指定维度参数 axis，即 tf.squeeze(x)，那么他会默认删除所有长度为1的维度

# 交换维度

在实现算法逻辑时，在保持维度顺序不变的条件下，仅仅改变张量的理解方式是不够的，有时需要直接调整的存储顺序，即交换维度(Transpose)。通过交换维度，改变了张量的存储顺序，同时也改变了张量的视图

我们以\[𝑏, ℎ, w, 𝑐\]转换到\[𝑏, 𝑐, ℎ, w\]为例，介绍如何使用tf.transpose(x, perm)函数完成维度交换操作，其中 perm 表示新维度的顺序 List。

tf.transpose(x, perm=\[0,3,1,2\])

通过tf.transpose完成维度交换后，张量的存储顺序已经改变，视图也随之改变，后续的所有操作必须基于新的存续顺序进行

# 数据复制

tf.tile(x, multiples)函数完成数据在指定维度上的复制操作，multiples 分别指定了每个维度上面的复制倍数，对应位置为1 表明不复制，为2 表明新长度为原来的长度的2 倍，即数据复制一份，以此类推。

```
tf.tile(x, multiples=[2,1])
```
