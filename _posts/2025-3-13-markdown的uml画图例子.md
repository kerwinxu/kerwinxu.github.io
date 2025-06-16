---
layout: post
title:  markdown的uml画图例子
date:   2025-3-13 13:49:00 +0800
categories: ["计算机语言", markdown]
project: false
excerpt: markdown的uml画图例子
lang: zh
published: true
tag:
- markdown
- uml
- 时序图
---


   

# 时序图

- mermaid : 一个图标工具
   - sequenceDiagram : 时序图

   - 冒号 ： 内容
   - participant xx as xx : 别称，昵称，
   - 线
      - -> 无箭头的实线
	  - --> 无箭头的虚线
	  - ->> ：有箭头的实线（主动发送消息）
      - --> ：有箭头的虚线（响应）
	  - -x ： 末尾带x的实体箭头
	  - --x ： 末尾带x的虚线箭头
	  - -) : 实体末端带有一个空心箭头（异步）
	  - --) ： 虚线末端带有一个空心箭头（异步）
   - 激活
      - 直接激活
	     - activate 对象 ： 开始
		 - deactivate 对象 ： 结束
      - 符号激活
	     - + 对象
		 - - 对象
   - 注释 : note [位置] [对象] ： 注释内容
   - 循环 loop

## 不带昵称的画法
用markdown的时序图  
```mermaid
    sequenceDiagram
	Client->>Gateway : 发送Json RPC请求
	Gateway-->>Client : 把Json RPC响应发送到客户端
```

## 带昵称的画法
```mermaid
    sequenceDiagram
	participant C as Client
	participant G as Gateway
	C->>G : 发送Json RPC请求
	G-->>C : 把Json RPC响应发送到客户端

```

## 激活框
消息接收方的时间上标记一小段时间，表示对消息进行处理的时间间隔。有两种激活方式  
   - 通过语法实现，会在指定对象的消息中添加。
   - 直接在对象前面增加加减号（开始时用加号+，结束时用减号-）

```mermaid
    sequenceDiagram
	participant L as 老板
	participant A as 员工
	L ->> + A : 不仅要996，还要669
	activate L
	A -->> - L : 故障
	L ->> + A : 悔创公司
	A -->> L :...
	deactivate L
``` 
## 注释
语法 ：note [位置] [对象] ： 注释内容

```mermaid
   sequenceDiagram
   note left of 老板 : 我是个脸盲
   note right of 员工 : 我对钱不感兴趣
   note over 老板,员工 : 对996感兴趣
```

## 循环
loop 消息说明  
[消息流]  
end

```mermaid
    sequenceDiagram
	网友 ->> 某宝 : 网购
	某宝 -->> 网友 : 下单成功

	loop 一天7次
		网友 ->> + 某宝 : 查看配送进度
		某宝 -->> - 网友 : 配送中
	end
```
## 选择 alt

```mermaid
    sequenceDiagram
	   土豪 ->> + 取款机 : 查询余额
	   取款机 -->> - 土豪 : 余额

	    alt 余额 > 5000
	        土豪 ->> 取款机 : 取上限5000
	    else 100 < 余额 < 5000
		    土豪 ->> 取款机 : 有多少取多少
		else 余额 < 100
		    土豪 ->> 取款机 : 退卡
		end
```

## 可选 opt
相当于单个分支的if语句
```mermaid
    sequenceDiagram
	    老板 ->> 员工 : 开始996

		opt 薪资加倍
		    员工 -->> 老板 : no way
		end
```

## 并行 par
将消息序列分成多个片段，并列执行

```mermaid
    sequenceDiagram
		老板 ->> 员工 : 开始996

		par 上班时间
			员工 ->> 员工  : 工作
		and 
			员工 ->> 员工  : 刷微博
		and 
			员工 ->> 员工  : 刷朋友圈
		end

		员工 -->> 老板 : 下班

```

## 背景颜色
```mermaid
    sequenceDiagram
	client ->> server : 发送请求
	rect rgb(191,223,255)
	server ->> server : 处理请求
	server -->> client : 发送响应
	end
```


# 饼图
```mermaid
    pie showData
	title 饼图名称
	"item1" : 50
	"item2" : 50
```


# 引用
   - [Markdown如何画时序图，一篇就够了](https://blog.csdn.net/zhw21w/article/details/125749449)
