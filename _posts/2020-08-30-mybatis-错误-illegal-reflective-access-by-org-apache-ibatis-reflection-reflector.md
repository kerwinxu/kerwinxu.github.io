---
layout: post
title: "mybatis 错误 : Illegal reflective access by org.apache.ibatis.reflection.Reflector"
date: "2020-08-30"
categories: 
  - "java"
---

详细错误:

WARNING: An illegal reflective access operation has occurred WARNING: Illegal reflective access by org.apache.ibatis.reflection.Reflector (file:/D:/Maven/repository/org/mybatis/mybatis/3.4.5/mybatis-3.4.5.jar) to method java.lang.Object.finalize() WARNING: Please consider reporting this to the maintainers of org.apache.ibatis.reflection.Reflector WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations WARNING: All illegal access operations will be denied in a future release

 

在学习Mybatis框架的时候遇到这些警告,其原因是Mybatis版本与jdk版本的问题；使用jdk9及以上版本会出现以上问题:

解决方式:

```
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>3.5.3</version>
</dependency>
```

用这个高版本的就可以了

 

引用:

[https://www.cnblogs.com/sprite1/p/12790840.html](https://www.cnblogs.com/sprite1/p/12790840.html)
