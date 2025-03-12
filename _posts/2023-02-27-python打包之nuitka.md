---
layout: post
title: "python打包之Nuitka"
date: "2023-02-27"
categories: 
  - "python"
---

核心是两种，一种是需要编译成c代码的，而另一种是用python.dll调用就可以了，我估计他们是自建了一个python。

以下是Nuitka的关键命令段

- **\--nofollow-imports #所有的import全部不使用，交给python3x.dll执行**
- **\--follow-import-to=need #need为你需要编译成C/C++的py文件夹命名**

比如numpy，不需要重新编译，用原先的就最好，这个就可以用**\--nofollow-imports**，而我们自己写的代码，需要保密的，可以添加**\--follow-import-to**，文章中说可以将我们自己写的部分添加到一个包中，比如need包，然后运行的参数

```
nuitka --standalone --windows-disable-console --mingw64 --nofollow-imports --show-memory --show-progress --plugin-enable=qt-plugins --include-qt-plugins=sensible,styles --follow-import-to=need --output-dir=o 你的.py

```

 

我用的是PySide6，所以这里--plugin-enable=qt-plugins，我的是--plugin-enable=pyside6

我用msvc ,所以这里--mingw64改成--msvc=14.3

如果需要一个文件就是 --onefile ，并且取消--nofollow-imports

常用命令

**部分常用命令**

**\--mingw64 #默认为已经安装的vs2017去编译，否则就按指定的比如mingw(官方建议)**

**\--standalone 独立环境，这是必须的(否则拷给别人无法使用)**

**\--windows-disable-console 没有CMD控制窗口**

**\--output-dir=out 生成exe到out文件夹下面去**

**\--show-progress 显示编译的进度，很直观**

**\--show-memory 显示内存的占用**

> **\--include-qt-plugins=sensible,styles 打包后PyQt的样式就不会变了**

**\--plugin-enable=qt-plugins 需要加载的PyQt插件**

**\--plugin-enable=tk-inter 打包tkinter模块的刚需**

**\--plugin-enable=numpy 打包numpy,pandas,matplotlib模块的刚需**

**\--plugin-enable=torch 打包pytorch的刚需**

**\--plugin-enable=tensorflow 打包tensorflow的刚需**

**\--windows-icon-from-ico=你的.ico 软件的图标**

**\--windows-company-name=Windows下软件公司信息**

**\--windows-product-name=Windows下软件名称**

**\--windows-file-version=Windows下软件的信息**

**\--windows-product-version=Windows下软件的产品信息**

**\--windows-file-description=Windows下软件的作用描述**

**\--windows-uac-admin=Windows下用户可以使用管理员权限来安装**

**\--linux-onefile-icon=Linux下的图标位置**

**\--onefile 像pyinstaller一样打包成单个exe文件**

**\--include-package=复制比如numpy,PyQt5 这些带文件夹的叫包或者轮子**

**\--include-module=复制比如when.py 这些以.py结尾的叫模块**

**\--recurse-all 递归所有**

 

 

# 引用

- [Nuitka之乾坤大挪移-让天下的Python都可以打包](https://zhuanlan.zhihu.com/p/137785388)
- [Nuitka 所有命令解释](https://blog.csdn.net/qq_38830593/article/details/123092470)
- [python 打包模块:nuitka](https://www.cnblogs.com/leoych/p/14446354.html)
