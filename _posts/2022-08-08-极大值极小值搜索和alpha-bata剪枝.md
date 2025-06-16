---
layout: post
title: "极大值极小值搜索和alpha Bata剪枝"
date: "2022-08-08"
categories: ["计算机", "算法"] 
---

# 极大值极小值

简单讲就是我取评分最高的，而对方取评分最低的，这样我就少得分。

例子：

假设一个二层博弈树，

- 最上边一层是树的根节点，这里MAX表示会选取下一层子节点中评分最高的，
- 第二层的MIN表示会选取下一层子节点中评分最低的。
- 第三层是叶子节点，只需要计算评分。

注意：只有在叶子节点才会计算评分，在树的中间层，对AI来说暂时不知道哪个节点是最有利的。

[![no img]](http://127.0.0.1/?attachment_id=4658)

极大值极小值策略

- AI下棋的层是MAX层，这一层AI会选取子节点中评分最高的。
- 玩家下棋的层是MIN层，这一层玩家会选取子节点中评分最低的。

# alpha beta剪枝策略

- 当一个MIN层的$latex \\alpha \\le \\beta $ ,剪掉该节点的所有未搜索子节点。
- 当一个MAX层的$latex \\alpha \\ge \\beta$ 剪掉该节点的所有未搜索子节点。
- 其中$latex \\alpha $ 是该层最有利的评分，$latex \\beta $ 是父节点的当前$latex \\alpha $ 值。

初始化节点的$latex \\alpha $ 值，

- 如果是在MAX层，初始化$latex \\alpha $ 的值是负无穷大，这样子节点的值肯定比这个值大。
- 如果是在MIN层，初始化$latex \\alpha $ 的值是正无穷大，这样子节点的值肯定比这个值小。

## MIN层剪枝

 

- B节点在MIN层，子节点是5和3，所以$latex \\alpha $取值3,[![no img]](http://127.0.0.1/?attachment_id=4659)
    - 节点A的$latex \\alpha $更新为当前最有利的分值为3
- 开始搜索节点C，C的$latex \\alpha=2 , \\beta=+\\infty $  [![no img]](http://127.0.0.1/?attachment_id=4660)
    - 节点C的$latex \\alpha = 6$,同时节点A的$latex \\alpha = 6$
- 开始搜索节点D，搜索节点D的第一个子节点为5，这时候节点D符合MIN剪枝 $latex \\alpha \\le \\beta $ ，所以节点D的第二个节点就被裁掉了。[![no img]](http://127.0.0.1/?attachment_id=4661)

 

这个剪枝算法，是深度优先策略，需要剪枝的部分是不想让对方高分，比如MIN层剪枝，是越小越好，如果分数大，是给对方机会。

 

# 引用

- [Python 五子棋AI实现(3):极大极小值搜索和alpha beta剪枝](https://blog.csdn.net/marble_xu/article/details/90647361)
