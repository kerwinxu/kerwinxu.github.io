---
layout: post
title: "WinAppDriver操作总结"
date: "2020-11-16"
categories: ["计算机语言", "c"]
---

# 安装

1. [https://github.com/Microsoft/WinAppDriver/releases](https://github.com/Microsoft/WinAppDriver/releases)
2. 需要设置win10系统为开发人员模式。
3. nuget中选择“Appium.WebDriver”，然后会自动安装另外几个东西。

# 先一个小例子

```
using OpenQA.Selenium.Appium;
using OpenQA.Selenium.Appium.Windows;
using OpenQA.Selenium.Interactions;
using OpenQA.Selenium.Remote;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace 用WinAppDriver来自动化GUI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [Obsolete]
        private void button1_Click(object sender, EventArgs e)
        {
            Process.Start(@"d:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe");

            WindowsDriver<WindowsElement> SysInfoApp;

            AppiumOptions appiumOptions = new AppiumOptions();

            

            appiumOptions.AddAdditionalCapability("app", @"C:\Windows\System32\notepad.exe");

            TimeSpan commandTimeout = new TimeSpan(0,0,10);


            SysInfoApp = new WindowsDriver<WindowsElement>(new Uri("http://127.0.0.1:4723"),appiumOptions, commandTimeout);


            SysInfoApp.FindElementByName("文本编辑器").SendKeys("This is some text");



        }

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
            //SysInfoApp.FindElementByName("台账数据").Click(); //这个可以识别

            Actions action = new Actions(SysInfoApp);

            //action.SendKeys("");
            //action.ClickAndHold
        }
    }
}
```

 

解释一下：

- 首先要打开WinAppDriver.exe程序。
- 然后在设置选项参数 AppiumOptions
    - 程序： "app", @"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
    - 程序的参数： "appArguments", @"E:\\onedrive\\outsourcing\\k083\\客户提供的\\超前小导管、管棚检验记录表(1).xlsx"
- 可选的是TimeSpan，这个是延时
- 创建 WindowsDriver对象，
- 这里要特别注意，如果软件启动的时候有闪屏，那么需要先跳转到启动后的窗口 SysInfoApp.SwitchTo().Window(allWindowHandles\[0\]);

# 查找元素

<table style="border-collapse: collapse; width: 100%; height: 192px;"><tbody><tr style="height: 24px;"><td style="width: 25%; height: 24px;">函数名</td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;">字段</td><td style="width: 25%; height: 24px;">例子</td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;">FindElementByXPath</td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;">//Button</td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;">FindElementByName</td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;">Name</td><td style="width: 25%; height: 24px;">Calculator</td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;">FindElementByClassName</td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;">ClassName</td><td style="width: 25%; height: 24px;">TextBlock</td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;">FindElementById</td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;">RuntimeId</td><td style="width: 25%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;">FindElementAccessibilityId</td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;">AutomationId</td><td style="width: 25%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td><td style="width: 25%; height: 24px;"></td></tr></tbody></table>

 

# 按键

- sendKeys
- Keys.chord(Keys.ALT, "G") ,组合键

# 鼠标

- click
- clickHold : 在某个元素上按键，然后按住不放，移动到另一个元素上，这个是拖拽或者选择吧。

# Actions

这个可以组成一系列的操作，然后最后运行的

```
Actions builder = new Actions(buggyFormSession);
builder.sendKeys(Keys.chord(Keys.ALT, "G"));
builder.perform();

Actions mouseOverTextBox3 = new Actions(buggyFormSession);
mouseOverTextBox3.moveToElement(textBox3, 50, 50);
mouseOverTextBox3.perform();
```

 

# 参考：

- [Keyboard and Mouse input with WinAppDriver 这里有更多的参考文章](https://plainswheeler.com/2019/10/16/keyboard-and-mouse-input-with-winappdriver/)
