---
layout: post
title: "js中serialport本地化编译"
date: "2024-08-20"
categories: 
  - "javascript"
---

项目文件夹下创建binding.gyp文件 内容

```json
{
  "targets": [
    {
      "target_name": "serialport",
      "sources": [  ]
    }
  ]
}
```

运行代码

```
node-gyp configure --dist-url=https://registry.npmmirror.com/serialport
node-gyp rebuild
```
