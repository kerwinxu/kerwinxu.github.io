---
lang: zh
author: Kerwin
layout: post
categorie["ORM"]
title:  typeorm会根据实体类修改数据库
date:   2024-9-06 15:43:00 +0800
excerpt: 模typeorm会根据实体类修改数据库
tag:
- JS
---

我开发的过程中数据库中已经有数据，我做了一个实体类，运行测试，发现typeorm会根据实体类中的选项更改数据库，导致数据库中列的属性更改了不少，数据也丢失了很多，我恢复数据库才找回来。

!注意，已经要先在演示环境中开发。