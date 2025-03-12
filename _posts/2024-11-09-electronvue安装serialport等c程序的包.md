---
layout: post
title: "electron,vue,安装serialport等c++程序的包"
date: "2024-11-09"
categories: 
  - "javascript"
---

# 步骤

请注意，因为我的是python3.7,而最新的node-gyp需要python的版本是>=3.12，所以我是在pipenv中构造了3.13的环境。

1. 生成项目
    
    ```
    yarn create @quick-start/electron
    ```
    
2. 进入项目文件夹
3. 安装构造本地代码的
    
    ```
    yarn add --dev @electron/rebuild
    ```
    
4. 安装SerialPort
    
    ```
    yarn add serialport
    ```
    
    ，
5. 我是用进程间通讯的方式来处理串口等c++库的，原因是vue不允许native库,需要在3个地方添加，主进程、预加载进程和渲染进程。
    1.  主进程，主进程中是真正执行的，src/main目录
        
        ```
        // 我在主线程中操作窗口，这里这仅仅是作为一个演示,返回串口的。
        ipcMain.handle('listSerialportNames', async () => await SerialPort.list())
        
        createWindow()
        ```
        
    2. 预加载进程，src/preload目录，这个是暴露给渲染进程，并且做了隔离
        
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
        
    3.  渲染进程中,src/renderer，是调用预加载中的，
        
        ```
        <script setup>
        import Versions from './components/Versions.vue'
        
        const ipcHandle = () => window.electron.ipcRenderer.send('ping')
        window.serialport.list().then((ports)=>console.log(ports))
        
        
        </script>
        ```
        
         
6. 可以看到成功的输出了现有串口列表。

 

 

单独测试是否安装库成功

node test\_serialport.cjs是成功运行的，可以说，应该是本地化方面出了问题？

```
// 这里看看串口是否可以正常调用
const SerialPort = require('serialport');
  // 这里显示有几个串口
  console.log('查看有几个串口')
  SerialPort.SerialPort.list().then((ports) => {
  console.log(ports)
  })
```

 

# 主线程跟渲染进程通讯

 

## 渲染器到主进程（单向）

要从渲染进程向主进程发送单向 IPC 消息，您可以使用 ipcRenderer.send API 发送消息，然后由 ipcMain.on API 接收。

 

## 渲染器到主进程（双向）

双向 IPC 的一个常见应用是从渲染进程代码调用主进程模块并等待结果。这可以通过使用 ipcRenderer.invoke 与 ipcMain.handle 配合来完成。

 

## 区别

单向的不用返回值，双向的会返回值。

 

## 主进程到渲染进程

以后再看。 [https://www.electron.js.cn/docs/latest/tutorial/ipc#pattern-3-main-to-renderer](https://www.electron.js.cn/docs/latest/tutorial/ipc#pattern-3-main-to-renderer)

 

 

# 错误解决

cannot execute cause=fork/exec C:\\Users\\kerwin\\.yarn\\releases\\yarn-1.22.19.cjs: %1 is not a valid Win32 application

修改“C:\\Users\\kerwin\\.yarn\\releases\\yarn-1.22.19.cjs”文件，

源文件第一行是 #!/usr/bin/env node

修改成 !node

原因是这个是win10系统，而程序执行的时候是当作unix系统了，当然是错误的。

 

# 引用

- [⨯ cannot execute cause=fork/exec...pnpm\\bin\\pnpm.cjs: %1 is not a valid Win32 application.](https://developer.aliyun.com/article/1430368)
- [进程间通信 \_ Electron 中文](https://www.electron.js.cn/docs/latest/tutorial/ipc)
