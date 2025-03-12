---
layout: post
title: "spring/mybatis的分页之用pageHelper实现"
date: "2020-08-30"
categories: 
  - "java"
---

两种方式吧

# 原版pageHelper实现

# pagehelper-spring-boot实现

在 pom.xml 中添加如下依赖：

```
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-starter</artifactId>
    <version>1.3.0</version>
</dependency>
```

设置application.yaml文件

```
#pagehelper分页配置 第二种和第三种不需要 重点讲的第一种需要
pagehelper:
    helperDialect: mysql
    reasonable: true
    supportMethodsArguments: true
    params: count=countSql
```

然后用如下代码转换

```
@RequestMapping("/getStockDetails")
public PageInfo<StockDetail> getStockDetails(Integer pageNum, Integer pageSize)
{
  Logger logger=Logger.getLogger(StockDetailController.class);
  logger.info(String.format("pageNum:%d,pageSize:%d", pageNum,pageSize));
  
  PageHelper.startPage(pageNum,pageSize);
  List<StockDetail> stockDetails=stockDetailsMapper.getStockDetails();
  return new PageInfo<StockDetail>(stockDetails);
}
```

原先返回是List,现在改成PageInfo就可以了.
