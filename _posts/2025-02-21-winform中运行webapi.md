---
layout: post
title: "winform中运行webapi"
date: "2025-02-21"
categories: ["计算机语言", "c#"]
---

# 安装

从nuget安装 Microsoft.AspNet.WebApi.OwinSelfHost

# 代码编写

Servers/Startup.cs

```c#
using System.Web.Http;
using Owin;

namespace WindowsFormsWebApi.Servers
{
    public class Startup
    {
        public void Configuration(IAppBuilder appBuilder)
        {
            HttpConfiguration config = new HttpConfiguration();
            config.Routes.MapHttpRoute(
                name: "DefaultApi",
                routeTemplate: "api/{controller}/{id}",
                defaults: new {id = RouteParameter.Optional});

            appBuilder.UseWebApi(config);
        }
    }
}
```

Controllers/HomeController

```
using System.Web.Http;

namespace WindowsFormsWebApi.Controllers
{
    public class HomeController: ApiController
    {
        [HttpGet]
        public IHttpActionResult ReadKeepReg(int address)
        {
            string str = "123466";
            return Json(str);
        }
    }
}
```

窗体代码

```
using System;
using System.Windows.Forms;
using WindowsFormsWebApi.Servers;
using Microsoft.Owin.Hosting;

namespace WindowsFormsWebApi
{
    public partial class Form1 : Form
    {
        private IDisposable _disposable;
        public Form1()
        {
            InitializeComponent();
        }

        private void InitializeWebApi(string ip, int port)
        {
            if (_disposable == null)
            {
                string baseAddress = $"http://{ip}:{port}/";
                _disposable = WebApp.Start<Startup>(url: baseAddress);
            }
        }

        private void ShutDownWebApi()
        {
            if (_disposable != null)
            {
                _disposable.Dispose();
                _disposable = null;
            }
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            var ip = tbIP.Text;
            var port = (int) numericPort.Value;
            InitializeWebApi(ip, port);
        }

        private void btnStop_Click(object sender, EventArgs e)
        {
            ShutDownWebApi();
        }
    }
}
```

# 测试

启动后访问

http://localhost:2000/api/home/ReadKeepReg?address=0

其中

- http://localhost:2000 地址端口
- api/home/ReadKeepReg 路径
- address=0 参数

 

# 引用

- [C#使用OWIN在WinForm应用程序中托管WebApi](https://zhuanlan.zhihu.com/p/517975190)
