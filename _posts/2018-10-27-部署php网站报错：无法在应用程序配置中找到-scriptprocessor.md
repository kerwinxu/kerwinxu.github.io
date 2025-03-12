---
layout: post
title: "部署PHP网站报错：无法在<fastCGI>应用程序配置中找到<handler> scriptProcessor"
date: "2018-10-27"
categories: 
  - "wordpress相关"
---

出现这个问题的原因是设置程序映射出错了。

我的问题是，请求路径，正确的是“\*.php”，而我的是“.php”

有些人的问题是可执行文件路径写错了。
