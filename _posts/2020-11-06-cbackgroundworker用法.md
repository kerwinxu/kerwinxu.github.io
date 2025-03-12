---
layout: post
title: "C#backgroundWorker用法"
date: "2020-11-06"
categories: 
  - "c"
---

# BackgroundWorker类介绍

## 常用属性

- public bool IsBusy { get; } //只读属性，用来判断当前线程是否正在工作中
- public bool WorkerReportsProgress { get; set; } //决定当前线程是否能报告进度
- public bool WorkerSupportsCancellation { get; set; } //决定当前线程能否取消
- public bool CancellationPending { get; } //只读属性，用来判断是否发送了取消线程的消息（当调用CancelAsync()方法时，被设置为true）

## 常用事件

- public event DoWorkEventHandler DoWork; //开始 必须，线程的主要逻辑，调用RunWorkerAsync()时触发该事件
- public event ProgressChangedEventHandler ProgressChanged; //报告 可选，报告进度事件，调用ReportProgress()时触发该事件
- public event RunWorkerCompletedEventHandler RunWorkerCompleted; //结束 可选，当线程运行完毕、发生异常和调用CancelAsync()方法这三种方式都会触发该事件

## 常用方法

- public void RunWorkerAsync(); //启动线程，触发DoWork事件
- public void RunWorkerAsync(object argument);
- public void ReportProgress(int percentProgress); //报告进度，触发ProgressChanged事件,请注意,这个percentProgress是百分数
- public void ReportProgress(int percentProgress, object userState);
- public void CancelAsync(); //取消线程，将CancellationPending设置为true

# 注意事项

- DoWork事件中不能与UI控件进行交流 如果需要在线程处理过程中与UI控件进行交流，请在ProgressChanged和RunWorkerCompleted中进行，否则会出现以下错误
