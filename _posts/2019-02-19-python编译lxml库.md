---
layout: post
title: "python编译lxml库"
date: "2019-02-19"
categories: 
  - "构建"
---

最新的，我编译的这个还是不能用，用pip uninstall lxml 然后 pip install lxml 解决了。

因为我用的是python3.7和vc2017，都是最新的版本，所以lxml.etree用不了，需要自己编辑。步骤如下：

- 下载如下软件
    - lxml : git clone https://github.com/lxml/lxml.git lxml
- 先编译如下的：
    - iconv 编译 :  [http://127.0.0.1/?p=2017](http://127.0.0.1/?p=2017)
        - include ： E:\\project\\vc\\libiconv\\libiconv
        - lib : E:\\project\\vc\\libiconv\\x64\\Release
    - libxml2 编译： [http://127.0.0.1/?p=2028](http://127.0.0.1/?p=2028)
        - include : E:\\project\\vc\\libxml2-2.9.9\\win32\\vc2017\\include
        - lib : E:\\project\\vc\\libxml2-2.9.9\\win32\\vc2017\\lib
    - libxslt 编译： [http://127.0.0.1/?p=2030](http://127.0.0.1/?p=2030)
        - include : E:\\project\\vc\\libxslt-1.1.33\\win32\\vc2017\\include
        - lib : E:\\project\\vc\\libxslt-1.1.33\\win32\\vc2017\\lib
    - zlib 编译 ： [http://127.0.0.1/?p=2033](http://127.0.0.1/?p=2033)
        - include ：E:\\project\\vc\\zlib-1.2.11
        - lib : E:\\project\\vc\\zlib-1.2.11\\build\\Release
- 打开sdk，进入vc2017命令行, 输入如下的命令：
    - set INCLUDE= %INCLUDE%;E:\\project\\vc\\libiconv\\libiconv;E:\\project\\vc\\libxml2-2.9.9\\win32\\vc2017\\include\\libxml2;E:\\project\\vc\\libxslt-1.1.33\\win32\\vc2017\\include;E:\\project\\vc\\zlib-1.2.11
    - set LIB=%LIB%;E:\\project\\vc\\libiconv\\x64\\Release;E:\\project\\vc\\libxml2-2.9.9\\win32\\vc2017\\lib;E:\\project\\vc\\libxslt-1.1.33\\win32\\vc2017\\lib;E:\\project\\vc\\zlib-1.2.11\\build\\Release
- 然后 python setup.py install
