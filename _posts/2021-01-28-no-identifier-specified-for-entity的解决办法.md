---
layout: post
title: "No Identifier specified for entity的解决办法"
date: "2021-01-28"
categories: 
  - "java"
---

检查注解：

1. 检查是否有@Entity注解
2. 检查是否有@Id注解，并且是 import javax.persistence.\*;中的。
