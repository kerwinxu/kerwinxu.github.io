---
layout: post
title: "Ubuntu下Vscode调试出现[无法打开\"libc-start.c\"：无法读取文件...错误解决办法"
date: "2019-12-30"
categories:: [计算机", "Linux"]
---

错误描述：无法打开"libc-start.c"：无法读取文件(Error:找不到文件(/build/glibc-LK5gWL/glibc-2.23/csu/libc-start.c))。 解决方案： $cd / $sudo mkdir build $cd build $sudo mkdir glibc-LK5gWL（注意这里文件名对应报错的文件名） $cd glibc-LK5gWL $sudo wget http://ftp.gnu.org/gnu/glibc/glibc-2.23.tar.gz （注意这里包的版本2.23对应报错版本） $sudo tar -zxvf glibc-2.23.tar.gz 其实就是没有找到相关库，需要在对应的地方放进对应的库文件。 (其实版本下错了也没关系，自己重命名为报错的类型也是可以的)。

注意，我发现，因为好像我的vscode是安装到d盘的，所以这个build竟然是在d盘的，我在d盘创建了这个build目录，然后下载解压，
