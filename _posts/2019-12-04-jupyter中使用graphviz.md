---
layout: post
title: "jupyter中使用graphviz"
date: "2019-12-04"
categories: 
  - "python"
---

首先安装 graphviz 这个软件，官网是 [http://graphviz.org/download/](http://graphviz.org/download/)

然后运行 pip install graphviz

 

在jupyter中，需要这样做，如下是一个例子，是二叉树的

```
%matplotlib inline
# 这里是一个函数来显示一个二叉树。
from graphviz import Digraph
def show_BinTree(root_node):
    """显示一颗二叉树"""
    def recurve_tree(tree, g):
        """这个是递归树实现的添加结点到图形中"""
        # 如果有左子树，就添加左子树，并且递归
        if tree.left is not None:
            g.node(name=tree.left.data, )
            g.edge(tree.data, tree.left.data)
            recurve_tree(tree.left, g)
        # 右子树同理
        if tree.right is not None:
            g.node(name=tree.right.data, )
            g.edge(tree.data, tree.right.data)
            recurve_tree(tree.right, g)
        
    # 首先初始化这个吧。
    g = Digraph('二叉树')
    recurve_tree(root_node, g)
    return g
    # 我用先根序的堆栈来实现这个

show_BinTree(tree_A)
```

注意最后一句，在jupyter中，如果某一行是一个变量，那么就会打印这个变量，我是根据这个特性来的。
