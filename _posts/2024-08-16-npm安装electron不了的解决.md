---
layout: post
title: "npm安装electron不了的解决"
date: "2024-08-16"
categories: 
  - "javascript"
---

在.npmrc文件中的最后添加

```
ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron
```

生成.npmrc文件是

```
npm config ls
```
