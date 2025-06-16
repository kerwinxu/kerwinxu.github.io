---
layout: post
title: "c#selenium取得request headers"
date: "2020-12-19"
categories: ["计算机语言", "c"]
---

最重要的是：nuget中Selenium.WebDriver的版本要选择4.0.0-alpha05，不是要稳定版。

代码如下：

```
ChromeOptions options = new ChromeOptions();
options.SetLoggingPreference("performance", LogLevel.All); //重要的是这个，这个是打开这个开关的意思。
options.AddArgument("--disable-gpu");
options.AddArgument("no-sandbox");

this.driver = new ChromeDriver(options);

var logs = driver.Manage().Logs.GetLog("performance"); //这个是取得了所有的头部了

for (int i = 0; i < logs.Count; i++)
{
    var log_i = logs[i];
    var str_message = logs[i].Message; //这个是json字符串
    JObject json_root = (JObject)JsonConvert.DeserializeObject(str_message); //解析json的，nuget中Newtonsoft.Json
    var url_tmp = json_root.Value<JObject>("message").Value<JObject>("params").Value<JObject>("response").Value<string>("url"); //取得子元素，一层一层的取得的。
}


```
