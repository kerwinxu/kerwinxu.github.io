---
layout: post
title: "文本压力测试工具lucust"
date: "2026-02-02"
categories: ["计算机语言", "python"]
math: true
---

我这里用的压力测试工具是lucust，是python写的，安装
```
pip install locust
```

简单脚本
```python
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
  host = "http://localhost:8888"
  wait_time = between(1, 2)

  @task
  def index_page(self):
    self.client.get("/hello")
    self.client.get("/world")

  @task(3)
  def view_item(self):
    for item_id in range(10):
      self.client.get(f"/item?id={item_id}", name="/item")
      time.sleep(1)

  def on_start(self):
    self.client.post("/login", json={"username": "foo", "password": "bar"})
```

运行
```
lucust -f a.py -P 8089
```

我这里自定义了端口，和我原先的有冲突。然后在浏览器中访问http://localhost:8089/，设置模拟用户数和每秒产生用户数，开始测试。
