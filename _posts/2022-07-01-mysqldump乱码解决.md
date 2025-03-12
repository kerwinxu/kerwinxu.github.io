---
layout: post
title: "mysqldump乱码解决"
date: "2022-07-01"
categories: 
  - "mysql"
---

mysqldump.exe -udrug -pdrug -P3307 --default-character-set=utf8 --hex-blob check\_drug\_machine > E:\\onedrive\\outsourcing\\k356\\demo安装包\\data.sql

 

注意两点

- \--default-character-set=utf8 可以指定编码
- \--hex-blob ，因为有很多二进制类型，比如binary,varbinary之类的，
