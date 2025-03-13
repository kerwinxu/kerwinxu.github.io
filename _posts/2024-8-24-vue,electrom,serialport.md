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

```
yarn create @quick-start/electron
...
cd ...
yarn add --dev @electron/rebuild
yarn add serialport

```

Main Thread : src/main
```js
// 我在主线程中操作窗口，这里这仅仅是作为一个演示,返回串口的。
ipcMain.handle('listSerialportNames', async () => await SerialPort.list())

createWindow()

```
Preload Thread : src/preload
```
// Use `contextBridge` APIs to expose Electron APIs to
// renderer only if context isolation is enabled, otherwise
// just add to the DOM global.
if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld('electron', electronAPI)
    contextBridge.exposeInMainWorld('api', api)
    contextBridge.exposeInMainWorld('serialport', {            // 我将串口的操作都放在这里边。
      list: () => ipcRenderer.invoke('listSerialportNames')    // 显示有几个端口的，发送消息的，主进程中处理，渲染进程中调用。
    })
  } catch (error) {
    console.error(error)
  }
} else {
  window.electron = electronAPI
  window.api = api
//   window.serialport = SerialPort.SerialPort
}
```
Renderer Thread : 
```
<script setup>
import Versions from './components/Versions.vue'

const ipcHandle = () => window.electron.ipcRenderer.send('ping')
window.serialport.list().then((ports)=>console.log(ports))


</script>
```




