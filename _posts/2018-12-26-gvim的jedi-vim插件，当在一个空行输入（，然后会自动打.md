---
title: "gvim的jedi-vim插件，当在一个空行输入（，然后会自动打开一个窗口的问题"
date: "2018-12-26"
categories: 
  - "python"
  - "vim"
---

解决方法：

在vimrc中添加

py3 import os;import sys;sys.executable=os.path.join(sys.prefix,'python.exe')

覆盖掉sys.executable

 

重现问题

- 在空行输入（后
- :JediDebugInof 命令后

问题原因：

 

this happens because sys.executable inside vim returns the path to the vim executable on windows so , instead of starting a python environment , jedi is starting a new instance of vim on that \_\_main\_\_.py file , a solution would be overwrite sys.executable with the right path on windows .
