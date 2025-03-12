---
layout: post
title: "git status 显示中文乱码"
date: "2019-10-22"
categories: 
  - "git"
---

# 场景

在使用git命令行查看当前 状态时,

git status 显示中文文件乱码: [![](/assets/image/default/L3Byb3h5L2h0dHBzL2ltZzIwMTguY25ibG9ncy5jb20vYmxvZy8xNDU3ODU5LzIwMTkwNC8xNDU3ODU5LTIwMTkwNDA3MTM1MjU5NjMyLTkwMzQ2NDM0Ni5wbmc.png)](http://127.0.0.1/?attachment_id=2755)

# 解决

修改git配置,

1. git config \--global core.quotepath false
