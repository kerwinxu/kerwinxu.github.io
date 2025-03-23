---
layout: post
title: "【转】Python · numpy · axis"
date: "2020-06-09"
categories: 
  - "python"
---

观众老爷们大家好！最近实在太忙，回首一看上篇专栏文章已经是 4 个月前的事了，所以今天想着写出一篇来撑撑场子（喂

但感觉已经没有当初写专栏的感觉了，所以可能画风会变不少，观众老爷们还望不要介意（逃

这次想和大家分享的是 numpy 中的 axis 这个东西。当初学的时候也没太在意，向来都是感觉差不多就直接过去了，没有去深究背后的一些逻辑。前些天被问起的时候一时懵懂，查了下资料后发现还有点意思，于是就打算写这么一篇专栏来分享一下所得

要想学习 axis，首先要知道的就是 axis 的计数方式。我们在使用 numpy 的各种函数——比如说 np.sum——的时候，有一个参数就叫做 axis。那么这个参数的意思是什么呢？最直白地来说的话，就是“**最外面的括号代表着 axis=0，依次往里的括号对应的 axis 的计数就依次加 1**”

举个例子，现在我们有一个矩阵： $latex x =\\left\[\\begin{array}{c} 0 & 1 \\\\ 2 & 3 \\end{array}\\right\] $；在 Python，或说在 numpy 里面，这个矩阵是这样被表达出来的：_x_ = \[ \[0, 1\], \[2, 3\] \]，然后 axis 的对应方式就是：

[![no img]](http://127.0.0.1/?attachment_id=3738)

所以相应的运算就是：

[![no img]](http://127.0.0.1/?attachment_id=3739)

下面来看一个更“高维”一点的例子：

[![no img]](http://127.0.0.1/?attachment_id=3740)

[![no img]](http://127.0.0.1/?attachment_id=3741)

从这张图可以看出，

- axis=0、axis=index，指的是遍历每个index、行号，即在纵向上遍历每列，所以做sum()、mean()等运算时，是对每列数据做操作，而drop(index, axis=0)，传入的参数指定了某一行号，所以会在纵向上遍历每列，去掉行号对应位置的数据。
- axis=1、axis=columns，指的是遍历每个columns、列名，即在横向上遍历每行，所以做sum()、mean()等运算时，是对每行数据做操作，而drop(col, axis=1)，传入的参数指定了某一列名，所以会在横向上遍历每行，去掉列名对应位置的数据。

作者：行走的程序猿 链接：https://www.jianshu.com/p/4f18e8327872 来源：简书 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

pandas和numpy对于axis参数的使用是一致的，从[numpy官方术语表](https://link.jianshu.com?t=https%3A%2F%2Fdocs.scipy.org%2Fdoc%2Fnumpy%2Fglossary.html)对于axis的释义可知一二。 Axes are defined for arrays with more than one dimension. A 2-dimensional array has two corresponding axes: the first running **vertically downwards across rows (axis 0)**, and the second running **horizontally across columns (axis 1)**.

 

# 引用

 

- [Python · numpy · axis](https://zhuanlan.zhihu.com/p/30960190)
