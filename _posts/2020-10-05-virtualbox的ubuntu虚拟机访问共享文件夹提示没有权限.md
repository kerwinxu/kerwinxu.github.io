---
layout: post
title: "Virtualbox的Ubuntu虚拟机访问共享文件夹提示没有权限"
date: "2020-10-05"
categories: 
  - "linux"
---

sudo usermod -aG vboxsf $(whoami)

将用户加入到（追加到）组中，其中选项\[-aG\]是追加到组的意思。

然后重启动就可以了.
