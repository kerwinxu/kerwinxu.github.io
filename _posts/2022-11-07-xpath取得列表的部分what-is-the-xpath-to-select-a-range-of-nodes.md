---
layout: post
title: "xpath取得列表的部分What is the XPath to select a range of nodes?"
date: "2022-11-07"
categories: 
  - "数学"
---

## Solution 1

```
/*/bar[position() >= 100 and not(position() > 200)]

```

**Do note**:

1. Exactly the `bar` elements at position 100 to 200 (inclusive) are selected.
2. The evaluation of this XPath expressions can be many times faster than an expression using the `//` abbreviation, because the latter causes a complete scan of the tree whose root is the context node. **Always try to avoid using the `//` abbreviation** in cases when this is possible.

## Solution 2

```
//foo/bar[100 <= position() and position() < 200]

```

## Solution 3

subsequence( /foo/bar, 100, 101 )

 

请注意，这个是一个数组的范围，但不是从结果中去筛选的，比如"//div\[last()\]"是div的最后一个标签，这个其实指的是比如有很多层div，这个得到的结果很可能是这很多层所有的div，因为在各自的某层，他们都是最后一个div。

 

引用

- [What is the XPath to select a range of nodes?](https://9to5answer.com/what-is-the-xpath-to-select-a-range-of-nodes)
