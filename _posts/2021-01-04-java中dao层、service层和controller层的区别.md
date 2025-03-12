---
layout: post
title: "Java中DAO层、Service层和Controller层的区别"
date: "2021-01-04"
categories: 
  - "java"
---

**DAO层：** DAO层叫数据访问层，全称为data access object，属于一种比较底层，比较基础的操作，具体到对于某个表的增删改查，也就是说某个DAO一定是和数据库的某一张表一一对应的，其中封装了增删改查基本操作，建议DAO只做原子操作，增删改查。

**Service层：** Service层叫服务层，被称为服务，粗略的理解就是对一个或多个DAO进行的再次封装，封装成一个服务，所以这里也就不会是一个原子操作了，需要事物控制。

**Controler层：** Controler负责请求转发，接受页面过来的参数，传给Service处理，接到返回值，再传给页面。

**总结：** 个人理解DAO面向表，Service面向业务。后端开发时先数据库设计出所有表，然后对每一张表设计出DAO层，然后根据具体的业务逻辑进一步封装DAO层成一个Service层，对外提供成一个服务

 

**引用**

- [Java中DAO层、Service层和Controller层的区别](https://blog.csdn.net/qq_22771739/article/details/82344336)
