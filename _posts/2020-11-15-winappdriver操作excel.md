---
layout: post
title: "WinAppDriver操作Excel"
date: "2020-11-15"
categories: ["计算机语言", "c"]
---

原文 ： [https://github.com/microsoft/WinAppDriver/issues/392](https://github.com/microsoft/WinAppDriver/issues/392)

里边 ：

Microsoft Outlook application in general displays a splash screen on the startup. As a splash screen is indeed a valid top level application window, Windows Application Driver treats it as the main window that you can indeed automate and test. The failure you saw above is correctly telling you that the splash screen (window) was already closed as the it went away after the actual main window appears.

What you can do at that point is simply switch your session to the main application window. For example:

 

大意是，当outlook打开的时候，前面有一个闪屏，WinAppDriver会根据那个闪屏的窗体操作，但实际上，这个闪屏在打开outlook后关闭了啊。所以要更新窗口

 

```
private void button2_Click(object sender, EventArgs e)
{
    Process.Start(@"d:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe");
    WindowsDriver<WindowsElement> SysInfoApp;
    AppiumOptions appiumOptions = new AppiumOptions();
    appiumOptions.AddAdditionalCapability("app", @"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE");
    appiumOptions.AddAdditionalCapability("appArguments", @"E:\onedrive\outsourcing\k083\客户提供的\超前小导管、管棚检验记录表(1).xlsx");

    TimeSpan commandTimeout = new TimeSpan(0, 0, 30);
    SysInfoApp = new WindowsDriver<WindowsElement>(new Uri("http://127.0.0.1:4723"), appiumOptions, commandTimeout);

    Thread.Sleep(15000);
    // excel
    var allWindowHandles = SysInfoApp.WindowHandles;

    //然后这里
    SysInfoApp.SwitchTo().Window(allWindowHandles[0]);
    //SysInfoApp.FindElementByXPath("//DataItem").Click();
    SysInfoApp.FindElementByXPath("//TabItem").Click();
}
```
