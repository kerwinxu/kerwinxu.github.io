---
layout: post
title: "Scrapy ImportError: DLL load failed: 操作系统无法运行1%"
date: "2018-09-27"
categories: 
  - "python"
---

from cryptography.hazmat.bindings.\_openssl import ffi, lib

ImportError: DLL load failed: 操作系统无法运行1%

解决:

`pip install -I cryptography`

然后还有个问题就是要编译openssl，并加入到环境变量中。
