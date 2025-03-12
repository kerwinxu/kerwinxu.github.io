---
layout: post
title: "tenacity，python通用重试库"
date: "2023-03-01"
categories: 
  - "python"
---

tenacity是一个 Apache 2.0授权的通用重试库，自动化测试或者爬虫中，当网络不稳定导致请求超时或者等待条件满足时操作，我们可以通过tenacity实现代码的重试功能。

[https://github.com/jd/tenacity](https://link.zhihu.com/?target=https%3A//github.com/jd/tenacity)

`pip install tenacity`

用法非常简单，直接加上装饰器使用。

### **重试3次**

```
import tenacity
from tenacity import stop_after_attempt

@tenacity.retry(stop=stop_after_attempt(3))
def retry_test():
    print("重试...")
    raise Exception

retry_test()
```

### **重试10秒**

```
import tenacity
from tenacity import stop_after_delay

@tenacity.retry(stop=stop_after_delay(10))
def retry_test():
    print("重试...")
    raise Exception

retry_test()
```

### **每隔2秒重试**

```
import tenacity
from tenacity import wait_fixed

@tenacity.retry(wait=wait_fixed(2))
def wait_2_s():
    print("Wait 2 second between retries")
    raise Exception

print(wait_2_s)
```
