---
layout: post
title: "使用conda管理python环境"
date: "2017-08-26"
categories: ["计算机语言", "Python"]
---

1. 查看有多少个运行环境
    
    ```
    conda info --e
    ```
    
2.  建立一个新的运行环境
    1.  指定版本号
        
        ```text
        conda create -n env_name python=2.7
        ```
        
    2. 同时安装必要的包
        
        ```text
        conda create -n env_name numpy matplotlib python=2.7
        ```
        
    3. 64位下安装32位的运行环境
        
        ```text
        设置32位set CONDA_FORCE_32BIT=1
        ```
        
3. 切换运行环境
    1. 切换进去
        
        ```text
        activate env_name
        ```
        
    2. 退出环境
        
        ```text
        deactivate env_name
        ```
        
4. 移除运行环境
    1. ```text
        conda remove -n env_name --all
        ```
        
5. 安装包
    1. 切换到运行环境的同时安装包
        
        ```text
        activate env_nameconda install pandas
        ```
        
    2. 安装时指定参数n，表明哪个运行环境安装包
        
        ```text
        conda install -n env_name pandas
        ```
        
    3. 安装发行版所有的包
        
        ```text
        conda install anaconda
        ```
        
6. 查看安装了哪些包
    1. 查看当前的运行环境的安装包
        
        ```text
        conda list
        ```
        
    2. 查看指定运行环境的安装包
        
        ```text
        conda list -n env_name
        ```
        
7. 查找包
    1. ```text
        conda search pyqtgraph
        ```
        
8. 更新包
    1. 更新当前运行环境的包
        
        ```text
        conda update numpy
        ```
        
    2. 更新Anaconda
        
        ```text
        conda update anaconda
        ```
        
9.  卸载包
    1. ```text
        conda remove numpy
        ```
