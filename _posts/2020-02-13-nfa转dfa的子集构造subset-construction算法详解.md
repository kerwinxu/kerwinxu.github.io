---
layout: post
title: "NFA转DFA的子集构造(Subset Construction)算法详解"
date: "2020-02-13"
categories: 
  - "设计模式"
---

# 概念

如下是我转载别人的，文中说的是来自虎书，

首先我们形式化 $latex \\epsilon $ 闭包如下：

- $latex edge(s,c)$ : 状态s沿着标有c的边可到达的所有 **NFA** 状态的集合。
- $latex closure(S) $ : 对于状态集合S，从S出发，只通过 $latex \\epsilon$边可以到达的状态集合
    - 这种经过 $latex \\epsilon$边的概念可以用数学方法表述，即  $latex closure(S)$ 是满足如下条件的最小集合**T** $latex T = S \\cup ( U\_{s \\in  T} edge(s, \\epsilon ))$
    - 我们可以用迭代法算出 **T：**
        - $latex T \\leftarrow S$ $latex repeat \\ \\ T' \\leftarrow T$ $latex \\ \\ \\ \\ \\ \\ \\ \\ \\  T \\leftarrow T' \\cup (U\_{s\\in T'} \\ \\ edge(s,\\epsilon))$ $latex until \\ \\  T = T'$
        - 解析：当我们位于一个状态集合S，S里任意状态经过若干 $latex \\epsilon$ 能够到达的状态，都包含在$latex closure(S)$里。

现在我们假设我们位于**NFA**状态$latex s\_i, s\_j,s\_k$组成的集合 $latex d = \\{s\_i,s\_j,s\_k\\}$,从d中状态出发，输入字符c将到达**NFA**新的状态集，我们称这个状态集合为  $latex DFA \\ \\ \\ edge(d,c)$

$latex FA \\ \\ \\ edge(d,c) = closure (U\_{s\\in d } \\ \\ edge(s,c))$

利用$latex DFA \\ \\ edge$ 能更形式化的写出**NFA**模拟算法，如果初态为$latex s\_1$ ,输入的字符串是 $latex c\_1,\\cdots, c\_k$ ,则算法为：

$latex d = closure(\\{s\_1\\})$ $latex for i \\leftarrow 1 to k$ $latex \\ \\ \\ \\ d \\leftarrow DFA \\ \\ edge(d,c\_i)$

有了closure和DFA edge 算法，就能构造出DFA,DFA的状态$latex d\_1$就是 $latex closure (s\_1)$,如果$latex  d\_j=DFAedge(d\_i,c) $ 则存在一条从 $latex d\_i$到$latex d\_j$的标记为c的边，令$latex \\Sigma $ 是字母表

$latex states\[0\] \\leftarrow \\lbrace \\rbrace; \\qquad states\[1\] \\leftarrow closure(\\lbrace s\_1 \\rbrace) \\\\ p\\leftarrow 1; \\qquad j \\leftarrow 0 \\\\ while \\ j \\leq p \\\\ \\ \\ \\ foreach \\ c \\in \\Sigma \\\\ \\qquad e \\leftarrow DFAedge(states\[j\],c) \\\\ \\qquad if \\ e =states\[i\] \\ for \\ some \\ i \\leq p \\\\ \\qquad \\quad \\ then \\ trans\[j,c\] \\leftarrow i \\\\ \\qquad \\quad \\ else \\ p \\leftarrow p+1 \\\\ \\qquad \\qquad \\quad \\, states\[p\] \\leftarrow e \\\\ \\qquad \\qquad \\quad \\, trans\[j,c\] \\leftarrow p \\\\ \\; \\; j \\leftarrow j+1 $

龙书中讲的是，首先是概念

- 子集构造法的基本思想是让构造得到的DFA的每个状态对应于NFA的一个状态的集合，DFA在读入 $latex a\_1a\_2\\cdots a\_n$之后到达的状态对应于相应的NFA从开始状态出发，沿着$latex a\_1a\_2\\cdots a\_n$为边的路径能到达的状态的集合。

算法

- - 输入： 一个NFA N
    - 输出： 一个接受同样语言的DFA D
    - 方法：我们为算法D构造一个转换表 Dtran , D的每个状态是一个NFA集合，构造Dtran，使得D并行的模拟N在遇到一个给定输入串可能执行的所有动作，下面是一些函数的定义
        
        <table style="border-collapse: collapse; width: 100%;"><tbody><tr><td style="width: 32.8025%;">操作</td><td style="width: 67.1975%;">描述</td></tr><tr><td style="width: 32.8025%;">$latex \epsilon - closure(s) $</td><td style="width: 67.1975%;">能够从NFA状态s开始只通过 $latex \epsilon$转换到达的NFA状态的集合。</td></tr><tr><td style="width: 32.8025%;">$latex \epsilon - closure(T) $</td><td style="width: 67.1975%;">能够从T中的某个NFA状态s开始只通过 $latex \epsilon $ 转换到达的NFA状态集合，即，$latex \bigcup_{s \in T} \epsilon -closure(s)$</td></tr><tr><td style="width: 32.8025%;">$latex move(T,a) $</td><td style="width: 67.1975%;">能够从T中某个状态s出发通过标号a的转换到达的NFA状态的集合。</td></tr></tbody></table>
        
    - 在读入第一个符号之前，N可以位于集合 $latex \\epsilon-closure(s\_0)$中的任何状态上，其中， $lates s\_0$是N的起始状态
    - 下面进行归纳：假定N在读入串x之后可以位于集合T的任何集合上，如果下一个输入为a，那么N可以立即移动到集合 $latex move(T,a)$中的任何状态，然而，N可以读取a之后再执行几个 $latex \\epsilon$转换，因此N在读入$latex xa$之后可以位于 $latex \\epsilon-closure(move(T,a))$中的任意状态上，接着我们可以构造出转换函数 Dtran :
        - 一开始 ，$latex \\epsilon-clusure(s\_0)$ 是$latex Dstates$ 的唯一状态，且它未标记。
        - $latex while(在Dstates中有一个未标记的状态T) \\lbrace \\\\ \\quad \\quad \\ 给T加上标记; \\\\ \\quad \\quad \\ for(每个输入符号a) \\lbrace \\\\ \\qquad \\qquad \\quad U=\\epsilon-clusure\\left(move(T,a) \\right) \\\\ \\qquad \\qquad \\quad if(U不在Dstates中) \\\\ \\qquad \\qquad \\qquad \\qquad \\, 将U加入Dstates中，且不加标记; \\\\ \\qquad \\qquad \\quad Dtran\[T,a\]=U \\\\ \\quad \\quad \\ \\rbrace \\\\ \\rbrace$

# 一个例子

给定一个正则表达式 $latex (a|b)^\* abb $的**NFA**，我们使用子集构造法构造**DFA**。

[![](/assets/image/default/20190329030919691.png)](http://127.0.0.1/?attachment_id=2982)

解法：首先，我们分析得出，NFA的初始状态为0，因而初始状态集

$latex A= \\epsilon - closure(0) = \\{0,1,2,4,7\\}$

如下是循环：

1. A被加上标记，对于输入符号a，b，分别求出 $latex a:B=\\epsilon-closure(move(A,a))=\\lbrace1,2,3,4,6,7,8 \\rbrace \\\\b:C=\\epsilon-closure(move(A,b))=\\lbrace1,2,4,5,6,7 \\rbrace $
2. B,C 都没有被标记，因而将B,C依次加上标记，对于输入符号a,b，分别求出: $latex a:B=\\epsilon-closure(move(B,a))=\\lbrace1,2,3,4,6,7,8 \\rbrace  求出来的\\lbrace1,2,3,4,6,7,8 \\rbrace在 Dstates中，不新建一个，\\\\b:D=\\epsilon-closure(move(B,b))=\\lbrace1,2,4,5,6,7,9 \\rbrace  ，求出来的不在Dstates中，新建一个D$ $latex a:B=\\epsilon-closure(move(C,a))=\\lbrace1,2,3,4,6,7,8 \\rbrace \\\\b:C=\\epsilon-closure(move(C,b))=\\lbrace1,2,4,5,6,7 \\rbrace$
3. 现在只剩D没有加标记，因而给D加上标记，对于输入符号a,b，分别求出: $latex a:B=\\epsilon-closure(move(D,a))=\\lbrace1,2,3,4,6,7,8 \\rbrace \\\\b:E=\\epsilon-closure(move(D,b))=\\lbrace1,2,4,5,6,7,10 \\rbrace$
4. 还剩一个E没有标记，因而给E加上标记，对于输入符号a,b，分别求出: $latex a:B=\\epsilon-closure(move(E,a))=\\lbrace1,2,3,4,6,7,8 \\rbrace \\\\b:C=\\epsilon-closure(move(E,b))=\\lbrace1,2,4,5,6,7 \\rbrace$
5. 所有构造出来的集合都已经被标记，构造完成！A,B,C,D,E为五个不同状态： $latex A=\\lbrace0,1,2,4,7 \\rbrace \\\\ B=\\lbrace1,2,3,4,6,7,8 \\rbrace \\\\ C=\\lbrace1,2,4,5,6,7 \\rbrace \\\\ D=\\lbrace1,2,4,5,6,7,9 \\rbrace \\\\ E=\\lbrace1,2,4,5,6,7,10 \\rbrace$
6. 接着就是根据状态来画图了，最好先画好状态表： [![](/assets/image/default/17004872-d0b1564e61d7a25e.jpg)](http://127.0.0.1/?attachment_id=2985) 由此可知，A通过a，连到B，以此类推。就可以做出DFA图了^

[![](/assets/image/default/20190329034629249.png)](http://127.0.0.1/?attachment_id=2986)

# 如何最小化DFA的状态数量

很简单，如果开始于s1的机器接收字符串σ，始于s2的和始于与s1接收的串相同，并到达相同状态，且两个状态集同为终态或者非终态，那么s1,s2是等价的。我们可以把指向s2的连线全部指向s1，并删除s2，反之亦然。

- 举个书上的例子： [![](/assets/image/default/20190329034218208.png)](http://127.0.0.1/?attachment_id=2987)
    - 图中的{5,6,8,15},{6,7,8}是等价的，还有{10,11,13,15},{11,12,13}也是等价的。
        - 在判断是否等价前，我们要先判断是否为死状态哦(1.不能到达终态 2.从开始没有路径指向这个状态)。

# 引用

- [https://www.cnblogs.com/Zzzcode/p/10843983.html](https://www.cnblogs.com/Zzzcode/p/10843983.html)
