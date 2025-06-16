---
layout: post
title: "vue用electron生成桌面应用"
date: "2024-08-16"
categories: ["计算机语言", "JavaScript"]
---

最新方法electron已经提供了vue，所以这里用如下的方式来创建：

```
yarn create @quick-start/electron
```

然后如果用到需要编译的，

```
yarn add --dev @electron/rebuild
```

 

引用：

- [https://cn.electron-vite.org/guide/](https://cn.electron-vite.org/guide/)
- [https://classic.yarnpkg.com/en/package/@electron/rebuild](https://classic.yarnpkg.com/en/package/@electron/rebuild)

 

 

 

```
rem 1. 开发环境，我这里vue设置成npm的，而不是yarn的
npm install @vue/cli electron -g
rem 2. 生成项目
vue create electron_demo
rem 3. vue项目中添加 electron 模块
cd electron_demo
vue add electron-builder
rem 4. 运行
npm run electron:serve
rem 5. 打包，需要翻墙
npm run electron:build
```

如下是用yarn来实现的

出现 error @achrinza/node-ipc@9.2.2: The engine "node" is incompatible with this module.

用如下的方式来解决

yarn config set ignore-engines true

```
// 全局安装
npm install -g yarn
// 

// 全局安装vue和electron
yarn global add @vue/cli electron


// 生成vue项目
vue create vue_app_demo
// 添加electron支持
cd vue_app_demo
vue add electron-builder
// 运行
yarn run electron:serve
// 打包
yarn run electron:build
```
