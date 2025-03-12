---
layout: post
title: "QQA: Python 中的 str 与 repr"
date: "2019-01-27"
categories: 
  - "python"
---

有时候，你会需要为你的类实现 `__str__` 或 `__repr__` 方法，你知道它们的作用是什么吗？它们有什么区别吗？这个问题的答案一搜就能找到，如果恰巧这是你第一次看到这个问题，不妨看看吧。

 

- `__repr__` 用于生成**正式**的表示。可以认为是将对象序列化的方法，原则上要能反序列化回对象。
- `__str__` 用于生成**非正式**的表示。`format` 或 `print` 会调用它来为用户生成“友好的”显示。
- 如果你需要自己实现，一般实现 `__str__` 即可。

## Python 中一切皆对象

[Python Data Model](https://docs.python.org/3/reference/datamodel.html) 中指出，Python 中的所有数据都是“对象”(Object)。Python 中几乎所有（不确定有没有反例）的操作都可以对应到对象的某个特殊方法。因此可以通过手工实现它们来覆盖默认的逻辑。

比如说迭代器(iterator)取长度操作 `len(iter)` 对应 `obj.__len__`；加法操作 `a + b` 对应`a.__add__(b)`；函数调用 `func(...)` 对应 `func.__cal__(...)`。当然也包括我们要介绍的 `__repr__` 和 `__str__`。

## repr 用于 Debug

Python 中执行 `repr(obj)` 可以获取 `obj` 的字符串表示，而这个操作相当于调用了 [obj.\_\_repr\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__repr__) 。而这个字符串表示“原则上”需要能反序列化回 `obj` 本身。看下面代码：

<table><tbody><tr><td class="code"><pre><span class="line">x = [<span class="number">1</span>,<span class="number">2</span>,<span class="number">3</span>]</span>
<span class="line">repr(x)</span>
<span class="line"><span class="comment">#&gt; '[1, 2, 3]'</span></span>
<span class="line">eval(<span class="string">'[1, 2, 3]'</span>)</span>
<span class="line"><span class="comment">#&gt; [1, 2, 3]</span></span>
<span class="line">eval(repr(x)) == x</span>
<span class="line"><span class="comment">#&gt; True</span></span></pre></td></tr></tbody></table>

我们看到 `'[1, 2, 3]'` (注意到逗号后面带了空格) 是数据 `[1,2,3]` 的字符串表示，用 `eval` 来反序列化可以得到原数据。那么如果变量是自定义的类又如何呢？

<table><tbody><tr><td class="code"><pre><span class="line"><span class="class"><span class="keyword">class</span> <span class="title">MyClass</span>:</span></span>
<span class="line">    <span class="function"><span class="keyword">def</span> <span class="title">__init__</span><span class="params">(self, arg)</span>:</span></span>
<span class="line">        self.arg = arg</span>
<div></div>
<span class="line">x = MyClass(<span class="number">10</span>)</span>
<span class="line">repr(x)</span>
<span class="line"><span class="comment">#&gt; '&lt;__main__.MyClass object at 0x10a40ef98&gt;'</span></span></pre></td></tr></tbody></table>

可以看到，`repr(x)` 给出了对象的类型及对象的 ID (内存地址)。但如果我们用 `eval(repr(x))` 尝试反序列化时，会失败。所以能反序列化其实是一个约定而非强制。我们尝试覆盖默认的实现：

<table><tbody><tr><td class="code"><pre><span class="line"><span class="class"><span class="keyword">class</span> <span class="title">MyClass</span>:</span></span>
<span class="line">    <span class="function"><span class="keyword">def</span> <span class="title">__init__</span><span class="params">(self, arg)</span>:</span></span>
<span class="line">        self.arg = arg</span>
<div></div>
<span class="line">    <span class="function"><span class="keyword">def</span> <span class="title">__repr__</span><span class="params">(self)</span>:</span></span>
<span class="line">        <span class="keyword">return</span> <span class="string">'MyClass({})'</span>.format(self.arg)</span>
<div></div>
<span class="line">x = MyClass(<span class="number">10</span>)</span>
<span class="line">repr(x)</span>
<span class="line"><span class="comment">#&gt; 'MyClass(10)'</span></span>
<span class="line">eval(repr(x))</span>
<span class="line"><span class="comment">#&gt; MyClass(10)</span></span></pre></td></tr></tbody></table>

可以看到对 `__repr__` 的覆盖起了效果，也可以正常反序列化了。

上面这几个例子都是为了说明 `repr` 生成的字符串到底有什么用。

- `repr` 并**不强制**生成的字符串可以反序列化
- `repr` 生成的字符串一般用于 debug，所以一般生成的字符串一般要包含尽可能多的信息，信息要尽可能明确(如默认实现里用 ID 区分开两个不同的对象)。
- 不要使用 `repr` 和 `eval` 来做序列化/反序列化，用 [pickle](https://docs.python.org/3/library/pickle.html) 或 [json](https://docs.python.org/3/library/pickle.html)。

## str 用于显示

[obj.\_\_str\_\_()](https://docs.python.org/3/reference/datamodel.html#object.__str__) 方法会在 `print(obj)` 或 `'{}'.format(obj)` 时被调用，一般是为了给用户提供"友好的"显示，所以 `__str__` 不像 `__repr__` 那样原则上对返回值有约定，想怎么搞都行。

另外，`__str__` 的默认实现是直接调用了 `__repr__` 方法。因此如果覆盖了 `__repr__` 方法，`__str__` 的结果也会随之改变。
