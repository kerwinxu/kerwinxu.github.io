---
title: "python yield from 用法"
date: "2020-11-18"
categories: 
  - "python"
---

# 替代内层for循环

```
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

# 替代内层for循环
def chain(*iterables):
    for i in iterables:
        yield from i
```

- yield from 完全代替了内层的 for 循环。
- yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从中获取迭代器。因 此，x 可以是任何可迭代的对象。
- 在这个示例中使用 yield from代码读起来更顺畅，不过感觉更像是语法糖。

 

例子:我们有一个嵌套型的序列，想将它扁平化处理为一列单独的值。

```
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)
# output：
 1 2 3 4 5 6 7 8
-----------------------------------------------
items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)

# output：
Dave
Paula
Thomas
Lewis
```

- collections.Iterable是一个抽象基类，我们用isinstance(x, Iterable)检查某个元素是否是可迭代的.如果是的话,那么就用yield from将这个可迭代对象作为一种子例程进行递归。最终返回结果就是一个没有嵌套的单值序列了。
- 代码中额外的参数ignore types和检测语句isinstance(x, ignore types)用来将字符 串和字节排除在可迭代对象外，防止将它们再展开成单个的字符。
- 如果这里不用yield from的话，那么就需要另外一个for来嵌套，并不是一种优雅的操作

 

例子2,一个利用一个Node类来表示树结构

```
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
```

结果如下

```
Node(0)
Node(1)
Node(3)
Node(4)
Node(2)
Node(5)
```

- \_\_iter\_\_代表一个Pyton的迭代协议，返回一个迭代器对象,就能迭代了
- depth\_frist返回一个生成器，仔细体会其中的yield与 yield from用法

# 主要功能:打开双通道

**yield from 的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接传入异常，而不用在位于中间的协程中添加大量处理异常的样板代码。有了这个结构，协程可以通过以前不可能的方式委托职责。**
