---
layout: post
title: "electron-quick-start 打包windows,Linux,MacOS"
date: "2022-12-21"
categories: ["计算机语言", "JavaScript"]
---

这个是打包成exe文件，刚下载下来的Readme中，只有如下的：

```
# Clone this repository
git clone https://github.com/electron/electron-quick-start
# Go into the repository
cd electron-quick-start
# Install dependencies
npm install
# Run the app
npm start
```

但上边的只是运行了一个临时的可执行文件，但并没有打包，如下的是打包的方式

1. npm install --save-dev @electron-forge/cli
2. npx electron-forge import
3. npm run make
4. 完成后会生成out文件包，在里边有可执行文件。只是打包的exe文件实在是太大了。

 

# 引用

- [electron-quick-start 打包windows,Linux,MacOS](https://blog.csdn.net/weixin_39248539/article/details/115321532)
