---
layout: post
title: "Emacs的lisp基础"
date: "2018-09-17"
categories: 
  - "emacs"
---

lisp是基于s表达式的语言，代码和数据是用同一种方式来表达的，S表达式，直观上就是括号括起来的一串列表。

在lisp中，默认是对s表达式求值的，

- 如果是数字，就对数字求值，
- 如果是字符串也是如此，
- 如果是一个表，则将第一个原子当函数名，对其进行求值。

# 定义变量

## 定义普通变量

(set 'three (+ 1 2))

## 定义带文档的变量

我们可以通过defvar特殊表来实现。 defvar特殊表不同于setq的是，它只针对未赋过初值的新变量有效，如果已经有值了，它就不起任何作用。所以我们在第一次定义变量的时候使用defvar特殊表吧，文档还是很重要的。

## 定义局部变量

(let ((变量名 绑定值)(变量名 绑定值)) 语句)

(let ((a 1)(b 2)) (+ a b))

在let中，如果未指明绑定值，则自动绑定到nil上。

## 定义全局变量

在 Common Lisp 中，全局变量的命名约定是名字前后各加一个星号 \* ，这样的形式：

```
*书籍数据库*
```

全局变量可以使用宏 defvar 来定义，初值为 nil，如下：

```
(defvar *书籍数据库* nil)
```

# 注释

# 表处理

## car和cdr：取表头和其余部分

- car函数：取一个表的第一个元素
- cdr函数：取一个表的除了car取到部分的其它部分

## nthcdr函数：多次cdr

(cdr (cdr '(1 2 3 4 5)))

(nthcdr 2 '(1 2 3 4 5))

nthcdr的第一个参数，如果是0，则直接返回原表。如果是1，则退化成cdr。

## cons函数：将car和cdr拼接起来

- (cons '1 '(2 3 4))
    - 将得到 (1 2 3 4).
- (cons '(1 2 3) '(4 5 6))
    - 得到的结果不是(1 2 3 4 5 6)而是((1 2 3) 4 5 6)

## append函数：将两个表合成一个表

- (append '(1 2 3) '(4 5 6))

## 获取表中最后一个元素：last函数

 

## 构造一个新表: list函数

- (list 1 2 3 4)

## 求表长度：length函数

- (length '(1 2 4 5))

## 给表换car和cdr：setcar和setcdr函数

(setq list1 '(1 2 3 4)) (setcar list1 5)

此时再通过C-h v去查list1的值，已经变为(5 2 3 4).

我们再将其后部也换掉：

(setcdr list1 '(6))

list1此时的值已经变成(5 6)

## 将表逆序排列：reverse函数

(reverse '(1 2 3 4))

## 像命令语言一样顺序编程

(defun func1 (x) (+ x 1)) (defun func2 (x) (\* x 2)) (defun func3(x) (\* x x)) (func3 (func2 (func1 0)))

先执行的，要写在最里面

Lisp善解人意地提供了progn特殊表，可以像C一样顺序执行。 我们可以这么写：

(progn (setq a (func1 0)) (setq b (func2 a)) (setq c (func3 b)))

## 针对整个表的进行操作 - mapcar函数

(defun sqr2 (x) (\* x x))

然后，我们就可以调用mapcar函数，对整个表都应用sqr2函数：

(mapcar 'sqr2 '(1 2 3 4))

针对这样只用一次的函数，我们可以使用lambda表达式来实现：

(mapcar (lambda (x) (\* x x)) '(5 6 7 8))

## 增加表项目push

 

## apply函数

(apply '+ '(5 6 7 8))

就相当于：

(+ 5 6 7 8)
