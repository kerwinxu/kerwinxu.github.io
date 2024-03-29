---
layout: post
title: 条形码管理专家
author: kerwin xu
date: 2021-10-28 14:38:52 +0800
categories: 软件
project: true
excerpt: 支持自定义模板和批量打印
image: "/assets/image/barcodemanager/img1.png"
lang: zh
tag:
- 条形码打印
- 批量打印
---

# 简介

方便的打印条形码的，支持自定义模板，支持批量打印。  
   - 模板编辑编辑模板。
   - 支持excel导入数据。
     - 支持冗余打印
     
# 下载

[最新下载](https://github.com/kerwinxu/barcodeManager/releases)


# 简单步骤
## 模板编辑
### 页面设置
打开软件后首先应该"页面设置"，也就是设置纸张  

![页面设置](/assets/image/barcodemanager/1.png)
不同的打印机有不同的纸张尺寸，请选择相关的打印机和相关的纸张尺寸，这里清注意，比如有一些A4纸大小的条形码纸张，还分成很多行列的，在这里，需要选择A4纸大小，然后行列数，请在“布局”中设置，对打印机而言，这个纸张尺寸就是A4大小，但对于我们想分隔成很多行列的，我们可以自己在这里设置  
![设置纸张](/assets/image/barcodemanager/2.png)  
### 编辑
这里可以做图形的编辑，重点的是条形码,右边可以设置相关的属性。  
![编辑](/assets/image/barcodemanager/3.png)  
条形码支持从excel导入输入，excel文件的格式如下，其中第一行为这一列的标题

|款号 |   品名  |  数量  |  条形码 |
| :--- | :---    | :---    | :---     |
|1 |   男装T恤  |  342 |   123456789012|
|2 |   女装T恤   | 42342 |   123456789013|
|3 |   男装休闲长裤  |  4242 |   123456789014 |
|4 |   女装休闲长裤  |  42  |  123456789015|
|5  |  男装牛仔长裤   | 4242 |   123456789016|
|6  |  女装牛仔长裤   | 42  |  123456789017 |
|7 |   男装长袖衬衫  |  452 |   123456789018|
|8 |   女装长袖衬衫  |  5432 |   123456789019|

这个标题就是变量，打印的时候，会按照excel的行读取，然后按照列名填充相关的内容。    

![变量](/assets/image/barcodemanager/4.png) 

## 条形码管理专家

这个重点是两个  
   - 模板 ： 可以导入用模板编辑的模板。
   - 数据 ： 通过excel导入

![条形码管理专家](/assets/image/barcodemanager/5.png) 




