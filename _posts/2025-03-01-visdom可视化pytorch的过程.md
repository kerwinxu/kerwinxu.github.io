---
layout: post
title: "visdom可视化pytorch的过程"
date: "2025-03-01"
categories: ["python", "pytorch"]
tags:
- python
- pytorch
- visdom
---

# 安装和启动

```
# visdom 安装指令
pip install visdom
# 启动 visdom web服务器
python -m visdom.server
```

# 监听数据

## 监听单一数据

```
from visdom import Visdom
import numpy as np
import time

# 将窗口类实例化
viz = Visdom() 

# 创建窗口并初始化
viz.line([0.], [0], win='train_loss', opts=dict(title='train_loss'))

for global_steps in range(10):
    # 随机获取loss值
    loss = 0.2 * np.random.randn() + 1
    # 更新窗口图像
    viz.line([loss], [global_steps], win='train_loss', update='append')
    time.sleep(0.5)
```

## 监听多个数据

```
from visdom import Visdom
import numpy as np
import time

# 将窗口类实例化
viz = Visdom() 

# 创建窗口并初始化
viz.line([[0.,0.]], [0], win='train', opts=dict(title='loss&acc', legend=['loss', 'acc']))
for global_steps in range(10):
    # 随机获取loss和acc
    loss = 0.1 * np.random.randn() + 1
    acc = 0.1 * np.random.randn() + 0.5
    # 更新窗口图像
    viz.line([[loss, acc]], [global_steps], win='train', update='append')
    # 延时0.5s
    time.sleep(0.5)
```

## 可视化图像

```
from visdom import Visdom
import numpy as np
import cv2
import torch

# 使用opencv读取数据
img = cv2.imread('pkq.jpg')
# opencv按照BGR读取，而visdom默认按照RGB显示,因此要进行通道转换
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# visdom类似于pytorch中的卷积模型，接收的数据都要求通道数在前
img = np.transpose(img, (2, 0, 1))
img = torch.from_numpy(img)
# 可视化图像
viz.image(img, win='pkq')
```
