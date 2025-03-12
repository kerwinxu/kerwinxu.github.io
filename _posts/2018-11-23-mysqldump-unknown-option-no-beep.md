---
layout: post
title: "mysqldump: unknown option '--no-beep'"
date: "2018-11-23"
categories: 
  - "维护"
---

网上找了一下，说查看 **my.ini** 发现\[clien\]下有 **no-beep** 参数，mysql客户端将会读取此参数(该参数作用暂时不知)。

mysqldump --no-defaults -u\[用户名\] -p\[这里可以输入密码也可不输入，如不输入会再后面提示输入\] 数据库名 > D:test.sql

就多了--no-defaults 这一部分 就成功了 哈哈！！

如：

mysqldump --no-defaults -u root -p wlan> D:\\wlan.sql

或者删除my.ini \[client\]下的 **no-beep** 参数也可以解决。
