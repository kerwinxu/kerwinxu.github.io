---
layout: post
title: "Emacs Lisp 速成"
date: "2019-08-25"
categories: 
  - "emacs"
---

你用着 Emacs 却不懂 Lisp 吧？欢迎阅读这篇 Emacs Lisp 入门教程！它应该能够助你搞定 Emacs Lisp，从而更加自如的驾驭 Emacs。

有很多种学习 Lisp 的方式，其中有一些方式要比其他方式更为 Lisp。我喜欢的方式是，基于 C++ 或 Java 的编程经验来学习 Lisp。

本文重点放在 Emacs Lisp 语言本身，因为它才是最难的部分，至于成吨的 Emacs 的 API 的用法，你可以通过阅读 Emacs Lisp 文档来学习。

有些事（例如编写生成代码的代码）是 Lisp 擅长的，而有些事（例如算数表达式）是它不擅长的。我不打算谈论 Lisp 是好还是坏，只关心如何用它编程。Emacs Lisp 跟其他语言差不多，最终你会习惯它的。

许多介绍 Lisp 的文章或书籍尝试给你展现 Lisp 之『道』，饱含着奉承、赞颂以及瑜伽之类的东西。事实上，一开始我真正想要的是一本简单的 cookbook，它讲述的是如何用 Lisp 来做一些我日常生活中的事。本文便立意于此，它讲述的是大致是如何用 Emacs Lisp 来写 C，Java 或 JavaScript 就能写的那些代码。

我们开始吧，看看我能够将这篇文章写的多么短小。我要从挺无聊的词法标记、运算符开始，然后讲述如何实现一些众所周知的语句、声明以及一些程序结构。

# 快速开始

Lisp 代码是像 `(+ 2 3)` 的嵌套的括号表达式。这些表达式有时被称为 form（块）。

也有些不带括号的代码，譬如字符串、数字、符号（必须以单引号为前缀，例如 'foo）、向量等，它们被称为原子（基本上可理解为叶结点）。

注释只能是单行的，分号是注释符。

要将一个名为 `foo` 的变量的值设置为 `"bar"`，只需：

```
(setq foo "bar") ; setq means "set quoted"
```

要以 "flim" 与 "flam" 作为参数值调用一个名为 foo-bar 的函数，只需：

```
(foo-bar "flim" "flam")

```

要进行算 `(0x15 * (8.2 + (7 << 3))) % 2`，只需：

```
(% (* #x15 (+ 8.2 (lsh 7 3))) 2)

```

也就是说，Lisp 的算数运算用的是前缀表达式，与 Lisp 函数调用方式一致。

Lisp 没有静态类型系统；你可以在程序运行时判断数据的类型。在 Emacs Lisp 中，谓词函数通常以 `p` 作为后缀，其含义下文有讲。

**重点**：可以在 Emacs 的 `*scratch*` 缓冲区中对 Emacs Lisp 表达式进行求值试验，有以下几种基本的求值方式：

- 将光标移到表达式最后一个封闭的括号的后面，然后执行 `C-j`（即 Ctrl + j 键）；
- 将光标移到表达式内部，然后执行 `M-C-x`（即 Alt + Ctrl + x 键）；
- 将光标放到表达式最后一个封闭的括号的后面，然后执行 `C-x C-e`。

第一种求值方式会将求值结果显示于 `*scratch*` 缓冲区，其他两种方式会将求值结果显示于 Emacs 的小缓冲区（Minibuffer）。这些求值方式也适用于 Lisp 的原子——数字、字符串、字符以及符号。

# 词法

Lisp 的词法标记（原子级别的程序元素）屈指可数。

## 注释

注释是单行的，由分号领起：

```
(blah blah blah) ; I am a comment

```

## 字符串

带双引号的就是字符串：

```
"He's said: \"Emacs Rules\" one time too many."

```

要让字符串含有换行符，只需：

```
"Oh Argentina!
Your little tin of pink meat
Soars o'er the Pampas"
```

## 字符

- `?`x 可以获得字符 x 的 ASCII 码，这里的 x 可以是任意 ASCII 编码的字符。例如 `?a` 的求值结果是 ASCII 码 `97`，而 `?` （问号后面是一个空格）的求知结果是 32。
- `?` 后面尾随的字符，有些需要逃逸，例如 `?\(`，`?\)` 以及 `?\\`。
- Emacs 22+ 支持 Unicode，这超出了本文范围。

字符本质上只是整型数值，因此你可以对它们做算术运算（例如，从 `?a` 迭代到 `?z`）。

## 数字

- 整型数的位数是 29 位（并非大家习惯的 32 位）；
- 二进制数，前缀是 `#b`，例如 `#b10010110`；
- 八进制数：`#o[0-7]+`，例如 `#o377`；
- 十六进制数，前缀是 `#x`，例如 `#xabcd`，`xDEADBEE`；
- 浮点数：位数是 64；
- 科学计数，例如 `5e-10`，`6.02e23`。

在不支持大整数的 Emacs Lisp 中，变量 `most-positive-fixnum` 与 `most-negative-fixnum` 分别是最大的与最小的整型数。Emacs 22+ 提供了一个叫做 `calc` 的大整数/数学库，以备不时之需。也就是说，Emas Lisp 的算数运算会发生上溢和下溢，如同你在 C 或 Java 中遇到的情况相似。

## 布尔值

符号 `t` 是 `true`，符号 `nil` 是 `false`（与 `null` 同义）。

在 Emacs Lisp 中，`nil` 是唯一的『假』值，其他非 `nil` 值皆为『真』值，也就是说像空字串、0、`'false` 符号以及空向量之类，都是真值。不过，空的列表 `'()` 与 `nil` 等价。

## 数组

Emacs Lisp 有定长数组，名曰『向量』(Vector)。可使用方括号来构建预先初始化的字面向量，例如：

```
[-2 0 2 4 6 8 10]
["No" "Sir" "I" "am" "a" "real" "horse"]
["hi" 22 120 89.6 2748 [3 "a"]]
```

 

注意，要使用空白字符来隔离数组中的元素，不要使用逗号。

向量中存储的数据可以是混合类型，也能够对向量进行嵌套。通常是使用 `make-vector` 来构建向量，因为字面向量是单例，对此不要惊讶。

## 列表

Lisp 重度依赖链表，因此专门为它提供了词法标记。圆括号里的任何东西都是列表，除非你引用了它，否则 Lisp 解释器就会像函数调用那样对其进行求值。在 Lisp 中有以下几种列表引用形式：

```
(quote (1 2 3)) ;  产生列表 (1 2 3)，并且不会对列表元素进行求值

'(1 2 3)  ; 单引号是 (quote (...)) 形式的简写，注意它在左括号之外

(list 1 (+ 1 1) 3) ; 也可以产生列表 (1 2 3)，因为 Lisp 解释器会首先对列表元素进行求值

`(1 ,(+ 1 1) 3)  ; 也可以产生列表 (1 2 3)，这是经过『反引号』模板系统产生的
```

## 序对

你可以直接设定 Lisp 列表的首部与尾部，将其作为 2 个元素的无类型结构来使用。语法是 `(head-val . tail-value)`，不过必须是引用的形式（见上文）。

对于较小的数据集，检索表的数据结构通常设计为关联列表（即所谓的 `alist`），这只不过是带点的序对所构成的列表而已，例如：

```
'( (apple . "red")
   (banana . "yellow")
   (orange . "orange") )
```

Emacs Lisp 有内建的哈希表，位向量等数据结构，但是它们并没有语法，你只能通过函数来创建它们。

# 运算符

有些运算，在其他语言中体现为运算符的形式，而在 Emacs Lisp 中体现为函数的调用。

## 等号

数值相等判断：`(= 2 (+ 1 1))`，单个等号，求值结果为 `t` 或 `nil`，也能用于浮点数比较。

数值不相等判断：`(/= 2 3)`，看上去像相除后赋值，但并不是。

值相等判断：`(eq 'foo 2)`，类似于 Java 的 `==`，适用于整型、符号、限定字串（Interned String）以及对象引用的相等比较。对于浮点数，可使用 `eql`（或者 `=`）。

结构的深度相等比较：使用 `equal`，例如：

```
(equal '(1 2 (3 4)) (list 1 2 (list 3 (* 2 2)))) ; 求值结果为 t

```

`equal` 函数类似于 Java 的 `Object.equals()`，适用于列表、向量、字符串等类型。

## 字符串

字符串没有任何运算符，只是有很多字符串操作函数，下面是几个常用的函数：

```
(concat "foo" "bar" "baz")  ; 求值结果为 "foobarbaz"

(string= "foo" "baz")  ; 求值结果为 nil (false)，也可以用 equal

(substring "foobar" 0 3) ; 求值结果为 "foo"

(upcase "foobar")  ; 求值结果为 "FOOBAR"
```

 

使用 `M-x apropos RET \bstring\b RET` 可查看所有与字符串操作相关的函数说明。

## 算术

还是画个表容易看……

[![]](http://127.0.0.1/?attachment_id=2620)

# 语句

这一节会给出一些类似 Java 语句的代码片段。它不复杂，仅仅是让你能够上手的方子。

## if/else

情况 1：无 `else` 从句（`(if test-expr expr)`）

示例：

```
(if (>= 3 2)
  (message "hello there"))
```

情况 2：`else` 从句（`(if test-expr then-expr else-expr)`）

```
(if (today-is-friday)         ; test-expr
    (message "yay, friday")   ; then-expr
  (message "boo, other day")) ; else-expr
```

如果你需要在 `then-expr` 中存在多条表达式，可使用 `progn`——类似于 C 或 Java 的花括号，对这些表达式进行封装：

```
(if (zerop 0)
    (progn
      (do-something)
      (do-something-else)
      (etc-etc-etc)))
```

在 else-expr 中没必要使用 progn，因为 then-expr 之后的所有东西都被视为 else-expr 的一部分，例如：

```
(if (today-is-friday)
    (message "yay, friday")
  (message "not friday!")
  (non-friday-stuff)
  (more-non-friday-stuff))
```

情况 3： 通过 `if` 语句的嵌套可实现 `else-if` 从句，也可以用 `cond`（下文有讲）：

```
(if 'sunday
    (message "sunday!")      ; then-expr
  (if 'saturday              ; else-if
      (message "saturday!")  ; next then-expr
    (message ("weekday!")))) ; final else
```

情况 4：无 `else-if` 的多分支表达式——使用 `when`：

如果没有 `else` 从句，可以使用 `when`，这是一个宏，它提供了隐式的 `progn`：

```
(when (> 5 1)
  (blah)
  (blah-blah)
  (blah blah blah))
```

也可以用 `unless`，它的测试表达式与 `when` 反义：

```
(unless (weekend-p)
  (message "another day at work")
  (get-back-to-work))
```

## switch

经典的 `switch` 语句，Emacs Lisp 有两个版本：`cond` 与 `case`。

Emacs Lisp 的 `cond` 与 `case` 不具备 `switch` 的查表优化功能，它们本质上是嵌套的 `if-then-else` 从句。不过，如果你有多重嵌套，用 `cond` 或 `case` 要比 `if` 表达式更美观一些。`cond` 的语法如下：

```
(cond
  (test-1
    do-stuff-1)
  (test-2
    do-stuff-2)
  ...
  (t
    do-default-stuff))
```

`do-stuff` 部分可以是任意数量的语句，无需用 `progn` 封装。

与经典的 `switch` 不同，`cond` 可以处理任何测试表达式（它只是依序检验这些表达式），并非仅限于数字。这样所带来的负面影响是，`cond` 对数字不进行任何特定的转换，因此你不得不将它们与某种东西进行比较。下面是字符串比较的示例：

```
(cond
 ((equal value "foo")  ; case #1 – notice it's a function call to `equal' so it's in parens
  (message "got foo")  ; action 1
  (+ 2 2))             ; return value for case 1
 ((equal value "bar")  ; case #2 – also a function call (to `+')
  nil)                 ; return value for case 2
 (t                    ; default case – not a function call, just literal true
  'hello))             ; return symbol 'hello
```

末尾的 `t` 从句是可选的。若某个从句匹配成功，那么这个从句的求值结果便是整个 `cond` 表达式的求值结果。

Emacs `'cl`（Common Lisp）包（译注：Emacs Lisp 手册推荐使用 `'cl-lib` ，因为 `'cl` 过时了），提供了 `case`，它能够进行数值或符号比较，因此它看上去比较像标准的 `switch`：

```
(case 12
  (5 "five")
  (1 "one")
  (12 "twelve")
  (otherwise
   "I only know five, one and twelve."))  ; result:  "twelve"
```

使用 `case`，默认从句可以用 `t`，也可以用 `otherwise`，但它必须最后出现。

使用 `case` 更干净一些，但是 `cond` 更通用。

## while

Emacs Lisp 的 `while` 函数相对正常一些，其语法为 `(while test body-forms)`。

例如，可在 `*scratch*` 缓冲区中执行以下代码：

```
(setq x 10
      total 0)
(while (plusp x)  ; 只要 x 是正数
  (incf total x)  ; total += x
  (decf x))       ; x -= 1
```

在上述代码中，我们首先设置了两个全局变量 `x=10` 与 `total=0`，然后执行循环。循环结束后，可对 `total` 进行求值，结果为 55（从 1 到 10 求和结果）。

## break/continue

Lisp 的 `cache/throw` 能够实现控制流的向上级转移，它与 Java 或 C++ 的异常处理相似，尽管功能上要弱一些。

在 Emacs Lisp 中要 `break` 一个循环，可以将 `(cache 'break ...)` 置于循环外部，然后在循环内部需要中断的地方放置 `(throw 'break value)`，例如：

[![]](http://127.0.0.1/?attachment_id=2621)

符号 `'break` 不是 Lisp 语法，而是自己取的名字——要取容易理解的名字，譬如对于多重循环，可在 `cache` 表达式中用 `'break-outer` 与 `'break-inner` 之类的名字。

如果你不关心 `while` 循环的『返回值』，可以 `(throw 'break nil)`。

要实现循环中的 `continue`，可将 `cache` 置入循环内部之首。例如，对从 1 到 99 的整数求和，并且在该过程中避开能被 5 整除的数（这是个蹩脚的例子，只是为了演示 `continue` 的用法）:

[![]](http://127.0.0.1/?attachment_id=2622)

可将这些示例组合起来，在同一个循环内实现 `break` 与 `continue`：

[![]](http://127.0.0.1/?attachment_id=2623)

上面的循环的计算结果为 4000，即 `total` 的值。要得到这个结果，还有更好的计算方式，不过我需要足够简单的东西来讲述如何在 Lisp 中实现 `break` 与 `continue`。

`catch/throw` 机制能够像异常那样跨函数使用。不过，它的设计并非真的是面向异常或错误处理——Emacs Lisp 另外有一套机制来做这些事，也就是后文的 `try/catch` 这一节所讨论东西。你应该习惯在 Emacs Lisp 代码中使用 `catch/throw` 进行控制流转移。

## o/while

Emacs Lisp 中最容易使用的循环机制是 Common Lisp 包提供的 `loop` 宏。要使用这个宏，需要加载 `cl-lib` 包：

```
(require 'cl-lib) ; 获取大量的 Common Lisp 里的好东西

```

`loop` 宏是带有大量特征的微语言，值得好好观摩一番。我主要用它来演示如何构造一些基本的循环。

基于 `loop` 所实现的 `do/while` 机制如下：

```
(loop do
  (setq x (1+ x))
  while
  (< x 10))
```

在 `do` 与 `while` 之间可以有任意数量的 Lisp 表达式。

## for

C 风格的 `for` 循环由四种成分构成：变量初始化，循环体，条件测试以及自增。用 `loop` 宏也能模拟出这种循环结构。例如，像下面的 JavaScript 的循环结构：

```
var result = [];
for (var i = 10, j = 0; j <= 10; i--, j += 2) {
  result.push(i+j);
}
```

对于这样的循环结构，基于 Emacs Lisp 的 `loop` 可将其模拟为：

```
(loop with result = '()         ; 初始化：只被执行一次
      for i downfrom 10         ; i 从 10 递减
      for j from 0 by 2         ; j 从 0 开始自增 2
      while (< j 10)            ; j >= 10 时循环终止
      do
      (push (+ i j) result)     ; 将 i + j 的求值结果入栈
      finally
      return (nreverse result)) ; 将 result 中存储的数据次序逆转，然后作为求值结果
```

由于 `loop` 表达式有很多选项，这样写虽然繁琐，但是容易理解。

注意，上述代码中，`loop` 声明了一个数组 result，然后将它作为『返回』值。事实上，`loop`　也能处理循环之外的变量，这种情况下就不需要　`finally return`　从句了。

`loop`　宏出人意料的灵活。有关它的全面介绍超出了本文范畴，但是如果你想驾驭　Emacs Lisp，那么你有必要花一些时间揣摩一下它。

## for .. in

如果你迭代访问一个集合，Java　提供了『智能』的　`for`　循环，JavaScript　提供了　`for .. in` 与　`for each .. in`。这些，在 Lisp 里也能做到，但是你可能需要对 `loop` 宏有很好的理解，它可以为迭代过程提供一站式服务。

最基本的方式是 `loop for var in sequence`，然后针对特定结果做一些处理。例如，你可以将 `sequence` 中的东西收集起来（或者将一个函数作用与它们）：

```
(loop for i in '(1 2 3 4 5 6)
    collect (* i i))            ;  结果为 (1 4 9 16 25 36)
```

`loop` 宏能够迭代列表元素、列表单元、向量、哈希键序列、哈希值序列、缓冲区、窗口、窗框、符号以及你想遍历的任何东西。请参阅 Emacs 手册获得更多信息。

## 函数

用 `defun`（**de**fine **fun**ction）定义函数。

语法：`(defun 函数名 参数列表 [可选的文档化注释] 函数体)`

```
(defun square (x)
  "Return X squared."
  (* x x))
```

对于无参函数，只需让参数列表为空即可：

```
(defun hello ()
  "Print the string `hello' to the minibuffer."
  (message "hello!"))
```

函数体可由任意数量的表达式构成，函数的返回值是最后那个表达式的求值结果。由于函数的返回类型没有声明，因此有必要在文档化注释中注明函数的返回类型。对函数进行求值之后，其文档化注释可通过 `M-x describe-function` 查看。

Emacs Lisp 不支持函数/方法的重载，但是它支持 Python 和 Ruby 所提供的那种可选参数与 rest 参数。你可以使用 Common Lisp 化的参数列表，在使用 `defun*` 宏代替 `defun` 时，可支持关键字参数（keyword arguments，见后文的 `defstruct` 一节）。`defun*` 宏也允许使用 `(return "foo")` 这种控制流转移方式来代替 `catch/throw` 机制。

如果你像让自己定义的函数能够作为 `M-x` 命令来执行，只需将 `(interactive)` 作为函数体内的第一个表达式，亦即位于文档化注释字串之后。

## 局部变量

在函数中要声明局部变量，可使用 `let` 表达式。基本语法是 `(let var-decl var-decl)`：

```
(let ((name1 value1)
      (name2 value2)
      name3
      name4
      (name5 value5)
      name6
      ...))
```

每个 `var-decl` 要么仅仅是变量名，要么就是 `(变量名 初始值)` 形式。初始化的变量与未初始化的变量出现的次序是任意的。未初始化的变量，其值为 `nil`。

在一个函数中可以有多条 `let` 表达式，但是为了性能起见，通常是将变量声明都放到开始的 `let` 表达式中，这样会快一点。不过，你应该写清晰的代码。

## 引用参数

C++ 有引用参数，函数可以修改调用者堆栈中的变量。Java 没有这个功能，因此有时你不得不迂回的向函数传递单元素数组，或一个对象，或别的什么东西来模拟这个功能。

Emacs Lisp 也没有真正的向函数传递引用的机制，但是它有动态域（Dynamic Scope），这意味着你可以用任何方式修改位于调用者堆栈中的变量。看下面这两个函数：

```
(defun foo ()
  (let ((x 6))  ; 定义了一个（栈中的）局部变量 x，将其初始化为 6
    (bar)       ; 调用 bar 函数
    x))         ; 返回 x

(defun bar ()
  (setq x 7))   ; 在调用者的栈中搜索 x 并修改它的值
```

如果你调用了 `(foo)`，返回值为 7。

动态域通常被认为是近乎邪恶的坏设计，但是它有时也能派上用场。即使它真的很糟糕，通过它也能了解一些 Emacs 的内幕。

## return

Lisp 函数默认是返回最后一个被求值的表达式的结果。通过一些构造技巧，也可以让每个可能的返回结果安排在函数的尾部位置。例如：

[![]](http://127.0.0.1/?attachment_id=2624)

上述 Lisp 函数 `day-name` 的返回值是最后一个表达式的求值结果，因此无论我们怎么嵌套 `if`，都能自动产生一个结果返回，因此这里不需要显式的 `return` 语句。

不过，有时用 `if` 嵌套的方式来重构函数的返回形式会不太方便，它较适合一些小的函数。对于一些规模较大并且嵌套较深的函数，你可能希望函数能够在较早的时机返回。在 Emacs Lisp 中，这一需求可基于 `break` 与 `continue` 来实现。上文中的 `day-name` 可重构为：

```
(defun day-name ()
  (let ((date (calendar-day-of-week
               (calendar-current-date))))  ; 0-6
    (catch 'return
      (case date
        (0
         (throw 'return "Sunday"))
        (6
         (throw 'return "Saturday"))
        (t
         (throw 'return "weekday"))))))
```

显然，使用 `catch/throw` 会降低程序性能，但是有时你会需要用它来消除太深的嵌套结构。

## try/catch

前文已经讲了 `catch/throw`，它类似于异常，可用于控制流转移。

Emacs 真正的错误处理机制叫做『条件』系统，本文不打算对此予以全面介绍，仅涉及如何捕捉异常以及如何忽略它们。

下面是一个一般化的 `condition-case` 结构，而且我也给出了 Java 的等价描述。

[![]](http://127.0.0.1/?attachment_id=2625)

如果你想让 `cache` 块为空，可使用 `ignore-errorse`：

```
(ignore-errors
  (do-something)
  (do-something-else))
```

有时你的启动文件（译注：可能是 .emacs 或init.el文件）可能不是总是正确工作。可以使用 `ignore-errors` 来封装 Emacs Lisp 代码，这样即使被封装的代码出错，也不会导致 Emacs 启动失败。

`condition-case nil` 的意思是『错误信息不赋给已命名的变量』。Emacs Lisp 允许你捕获不同的错误类别并对错误信息进行排查。这方面的知识请从 Emacs Lisp 手册获取。

在 `condition-case` 块内如果存在多条表达式需要求值，必须用 `progn` 将它们封装起来。

`condition-case` 不会捕捉 `throw` 扔出来的值——这两个系统是彼此独立的。

## try/finally

Emacs Lisp 提供了类似 finally 的功能 `unwind-protect`：

[![]](http://127.0.0.1/?attachment_id=2626)

与 `condition-case` 相似，`unwind-protect` 接受单个体块（body-form，译注：try 部分），后面跟随着一条或多条善后的表达式，因此你需要用 `progn` 将体块内的表达式封装起来。

## try/catch/finally

如果让 `condition-case`（等价于 `try/catch`）成为 `unwind-protect`（等价于 `try/finally`）的体块，那么就可以得到 `try/catch/finally` 的效果：

```
(unwind-protect                 ; finally
    (condition-case nil         ; try
        (progn                  ; {
          (do-something)        ;   body-1
          (do-something-else))  ;   body-2 }
      (error                    ; catch
       (message "oh no!")       ; { catch 1
       (poop-pants)))           ;   catch 2 }
  (first-finally-expr)          ; { finally 1
  (second-finally-expr))        ;   finally 2 }
```

# 类

Emacs Lisp 不是标准意义上的面向对象编程语言，它没有类、继承以及多态等语法。Emacs 的 Common Lisp 包（现在的 `cl-lib`）提供了一个有用的特性 `defstruct`，通过它可以实现简单的 OOP 支持。下面我会给出一个简单的示例。

下面的 Emacs Lisp 代码与 Java 代码本质上是等价的：

[![]](http://127.0.0.1/?attachment_id=2627)

`defstruct` 宏提供了一个灵活的默认构造器，但是你也可以根据自己的需要来定义相适的构造器。

`defstruct` 宏在创建对象实例时，也创建了一组判定函数，它们的用法如下：

```
(person-p (make-person))
t
(employee-p (make-person))
nil
(employee-p (make-employee))
t
(person-p (make-employee))  ; yes, it inherits from person
t
```

Java 在对象构造器方面可能挺糟糕，不过 Emacs 在域（类成员）的设置方面挺糟糕。要设置类（结构体）的域，必须使用 `setf` 函数，然后将类名作为域名的前缀：

[![]](http://127.0.0.1/?attachment_id=2628)

这样看上去，Lisp 并不是太糟糕，但是在实践中（因为 Emacs Lisp 不支持命名空间，并且也没有 `with-slots` 宏），你会被卷入很长的类名与域名中的，例如：

```
(setf (js2-compiler-data-current-script-or-function compiler-data) current-script
      (js2-compiler-data-line-number compiler-data) current-line
      (js2-compiler-data-allow-member-expr-as-function-name compiler-data) allow
      (js2-compiler-data-language-version compiler-data) language-version)
```

要获取域的值，需要将类名与域名连接起来，然后作为函数来用：

```
(person-name steve) ; yields "Steve"

```

`defstruct` 还能做很多事——它的功能非常得体，该考虑的事都考虑了，尽管它没能形成一个完善的面向对象系统。

## 缓冲区即类

在 Emacs Lisp 编程中，将缓冲区视为类的实例往往很有用。因为 Emacs 支持缓冲区级别的局部变量的概念——无论变量以那种方式设置（译注，例如通过 `setq` 设置的变量），它们都会自动变成缓冲区内部的局部变量。因此，这些变量的行为就像是被封装在实例中的变量。

可以用 `make-variable-buffer-local` 函数将一个变量声明为缓冲区级别的局部变量，通常这个函数会在 `devar` 或 `defconst` 之后出现（见下文）。

# 变量

在 Emacs Lisp 中，可以用 `defvar` 或 `defconst` 声明变量，也可以为变量提供文档化注释：

```
(defconst pi 3.14159 "A gross approximation of pi.")

```

语法为 `(defvar 变量名 值 [文档化注释])`。

不过，会让你大跌眼镜的是，`defconst` 定义的是变量，而 `defvar` 定义的是常量，至少在重新求值时是这样。要改变 `defvar` 变量的值，需要使用 `makeunbound` 来解除变量的绑定。不过，总是可以使用 `setq` 来修改 `defvar` 或 `defconst`变量的值。这两种变量形式，仅有的区别是，`defconst` 可以表达一种意图：你定义的是一个常量。

可以使用 `setq` 来创建全新的变量，但是如果用 `defvar`，Emacs Lisp 的字节码编译器能捕捉到一些错误信息。

# 总结

Emacs Lisp 是一种真正的编程语言。它有编译器、调试器、性能分析器、效果显示器、运行时文档、库、输入/输出、网络、进程控制等。它有很多东西值得学习，但是我希望这篇小文章能够让你向它迈出第一步。

无论 Emacs Lisp 有多么古怪和烦人，只要你上手了，它就能让你体验到编程的快乐。作为一种编程语言，它并不伟大，而且每个人都期望它是 Common Lisp 或 Scheme 或其他某种更好的 Lisp 方言。有些人甚至认为它根本不是 Lisp。

但是，要定制你的 Emacs，或者修复你从他人那里得到的 Emacs Lisp 代码，那么 Emacs Lisp 就会非常非常有用。四两 Emacs Lisp 可拨千钧之物。

正在学习 Emacs Lisp 的你，如果觉得这份文档是有用的，请告诉我。如果你打算写一些 Emacs 扩展，可以告诉我你希望我的下一篇文档要写什么。有兴趣的化，我会再继续这个 Emergency Elisp 系列。

Good Luck！
