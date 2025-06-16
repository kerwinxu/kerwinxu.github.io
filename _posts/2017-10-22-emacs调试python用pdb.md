---
layout: post
title: "emacs调试python用pdb"
date: "2017-10-22"
categories: ["构建"]
---

#### pdb调试

在Emacs中，通过M-x pdb可调出pdb对python代码进行调试。但是发现在Windows系统中，总进入不了调试模式。主要原因有：

 

新的解决方法：  (setq gud-pdb-command-name (concat "python -i -m pdb " (file-name-nondirectory buffer-file-name)))

只要设置这一个就可以了。

1\. windows中，找不到pdb.py位置。需自己制定pdb的路径。可以通过下面的方法设置pdb的路径：

![复制代码]

;; pdb setup, note the python version (setq pdb-path 'c:/python25/Lib/pdb.py gud-pdb-command-name (symbol-name pdb-path)) (defadvice pdb (before gud-query-cmdline activate) "Provide a better default command line when called interactively." (interactive (list (gud-query-cmdline pdb-path (file-name-nondirectory buffer-file-name)))))

![复制代码]

2\. windows中，调用pdb时，未使用python -i 参数。

针对上面两个问题，我的解决办法是，不设置pdb具体路径，M-x pdb 回车后，出现下面命令:

Run pdb (like this): pdb

然后手动修改一下：

Run pdb (like this): python -i -m pdb test.py

这样就搞定了。
