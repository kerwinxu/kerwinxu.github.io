---
layout: post
title: "electron-vite预加载脚本"
date: "2025-02-20"
categories: 
  - "javascript"
---

用于主线程和渲染线程之间的通讯。

1.  预加载线程中将变量或者方法暴露给渲染器
    
    ```js
    import { contextBridge, ipcRenderer } from 'electron'
    
    contextBridge.exposeInMainWorld('electron', {
      ping: () => ipcRenderer.invoke('ping')
    })
    ```
    
2. 将脚本附在渲染进程上，在 **BrowserWindow** 构造器中使用 **webPreferences.preload** 传入脚本的路径。
    
    ```js
    import { app, BrowserWindow } from 'electron'
    import path from 'path'
    
    const createWindow = () => {
      const win = new BrowserWindow({
        webPreferences: {
          preload: path.join(__dirname, 'preload.js'),
        },
      })
    
      ipcMain.handle('ping', () => 'pong')
    
      win.loadFile('index.html')
    }
    
    app.whenReady().then(() => {
      createWindow()
    })
    ```
    
3. 在渲染器进程中使用暴露的函数和变量
    
    ```js
    const func = async () => {
      const response = await window.electron.ping()
      console.log(response) // prints out 'pong'
    }
    
    func()
    ```
