---
title: "Python ctypes 中的指针和数组"
date: "2018-04-19"
categories: 
  - "python"
---

ctypes是Python提供的调用C库的模块，C/C++语言的函数中常常会使用数组和指针作为参数或返回值，Python在处理这类库的时候有一些麻烦，但是是可以实现的。

**函数中的数组**

这里以整形数组为例，代码如下：

int\_array \= ctypes.c\_int \* 10

a \= char\_p\_array(1,2,3)

第一句为定义整形数组类型，第二句将a实例化为一个c整形数组，参数为初始化的值，示例没有全部初始化。

**多级指针的处理**

这里以二级指针为例，代码如下：

x \= ctypes.c\_char\_p() y \= ctypes.pointer(x)

第一句定义个char型指针为第一级指针，第二句定义第二级指针。

以此类推可以第一多级指针。

内容的读取：

f \= y.contents.value
