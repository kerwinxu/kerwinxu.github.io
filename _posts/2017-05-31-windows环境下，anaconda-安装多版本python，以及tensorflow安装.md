---
title: "Windows环境下，Anaconda 安装多版本python，以及TensorFlow安装"
date: "2017-05-31"
categories: 
  - "python"
---

Anaconda只支持python3.5，而最新版的anaconda是python3.6，所以要做如下操作

1. conda create -n tensorflow python=3.5 ，创建一个python3.5环境。
2. activate tensorflow ，将这个环境生效。
3. pip install tensorflow-gpu ，安装gpu版本的 ，pip install tensorflow  ，是安装cpu版本的
4. 想要长期有效的话，path路径添加这个 “D:\\Anaconda3\\envs\\tensorflow”，和“D:\\Anaconda3\\envs\\tensorflow\\Scripts”
5. 要安装前面所有的包，首先pip list显示所有包，当然，这个pip是Anaconda3/script目录的那个，这个以后补充，

另外Anaconda的环境管理如下：

1. 创建环境 ，conda create -n tensorflow python=3.5
2. 激活环境，activate tensorflow
3. 列出所有环境，conda info -envis ，当前环境会显示在括号内。
4. 复制一个环境 conda create -n flowers --clone snowflakes
5. 删除一个环境 conda remove -n flowers --all
6. 注销当前环境 deactivate
7. 安装包，conda install --name bunnies beautifulsoup4 ，得指明为哪个环境安装包。
8. 移除包 conda remove -n bunnies iopro
9. 移除环境 conda remove -n snakes --all
