---
layout: post
title: "numpy中dot和multiply的区别"
date: "2018-02-18"
categories: 
  - "python"
---

两个都是乘法，不过：

```
import numpy as np

X = np.array([[1,2],[3,4]])
Y = np.array([[5,6],[7,8]])

```

# dot 就是线性代数中的矩阵乘积

In \[2\]:

```
np.dot(X,Y)

```

Out\[2\]:

```
array([[19, 22],
       [43, 50]])
```

# multiply 是数量积,对应元素相乘

In \[3\]:

```
np.multiply(X,Y)

```

Out\[3\]:

```
array([[ 5, 12],
       [21, 32]])
```

In \[5\]:

```
X*Y

```

Out\[5\]:

```
array([[ 5, 12],
       [21, 32]])
```
