---
lang: zh
author: Kerwin
layout: post
categories: ["js"]
title:  vue3和electron中使用类似serialport的node原生模块
date:   2024-8-24 11:51:00 +0800
excerpt: vue3和electron中使用类似serialport的node原生模块
tag: [JS,vue3,electron,serialport]
---

我看了很多资料，但没有一篇是让我这个新手看懂的，我这里的步骤很简洁，  

1. 生成vue项目
```
vue create demo
```
2. 添加electron支持,这里用 "electron-builder",这个会选择electron的版本，选择最大的那个。
```
cd demo
vue add electron-builder
```
3. 修改 vue.config.js
```
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
	transpileDependencies: false,
	pluginOptions: {
		electronBuilder: {
			nodeIntegration: true,
			externals: ['serialport'], 
		}
	}
})
```
4. 添加serialport，运行完如果是有错误的，不管它。
```
yarn add serialport
```
5. 我这里仅仅显示是否能够调用"serialport",在App.vue中添加
```
import {SerialPort} from 'serialport'

SerialPort.list().then(
	(ports)=>{console.log(ports);}
)
```
6. 测试效果
```
yarn run electron:serve
```
可以在控制台看到输出了相关的端口信息。

请注意，这个serialport是node原生模块，这个serialport可以被electron打包成本地的，但却不能"yarn run serve"运行,可能原因是electron做了很多配置，但我没找对方法,如果有人知道方法，麻烦告诉我。



