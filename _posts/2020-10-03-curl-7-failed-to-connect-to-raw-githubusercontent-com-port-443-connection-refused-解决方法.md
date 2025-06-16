---
layout: post
title: "curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused 解决方法"
date: "2020-10-03"
categories:: [计算机", "Linux"]
---

原因  
由于某些你懂的因素，导致GitHub的raw.githubusercontent.com域名解析被污染了。

解决方法  
通过修改hosts解决此问题。

查询真实IP

在https://www.ipaddress.com/查询raw.githubusercontent.com的真实IP

修改hosts

`sudo vim /etc/hosts`

添加如下内容：

`199.232.68.133 raw.githubusercontent.com`

重新执行命令即可，但是下载会比较慢。
