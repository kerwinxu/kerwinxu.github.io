---
layout: post
title: "AttributeError: module 'win32com.gen_py.00062FFF-0000-0000-C000-000000000046x0x9x6' has no attribute 'CLSIDToClassMap'"
date: "2019-05-08"
categories: ["计算机语言", "Python"]
---

发生这个错误的原因并不是很清楚, 大概是升级了一下系统, 但是我并不清楚内部原因.

解决的方法就是, 因为这个缓存的文件有问题, 所以就应该删掉缓存. 所以我先找到这个缓存文件:

<table><tbody><tr><td class="gutter" style="width: 13px;"><pre><span class="line">1</span>
<span class="line">2</span>
<span class="line">3</span>
<span class="line">4</span></pre></td><td class="code" style="width: 453px;"><pre><span class="line"><span class="keyword">from</span> win32com.client.gencache <span class="keyword">import</span> EnsureDispatch</span>
<span class="line"><span class="keyword">import</span> sys</span>
<span class="line">xl = EnsureDispatch(<span class="string">"Word.Application"</span>)</span>
<span class="line">print(sys.modules[xl.__module__].__file__)</span></pre></td></tr></tbody></table>

运行这段代码, 就会找到它的位置. 然后删除`gen_py`文件夹下的所有包含这一堆数字的文件夹`0020905-0000-0000-C000-000000000046x0`.

然后你的程序又能顺利运行了
