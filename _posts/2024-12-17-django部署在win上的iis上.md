---
title: "django部署在win上的iis上"
date: "2024-12-17"
categories: 
  - "python"
---

步骤

1. 安装 pip install wfastcgi
2. 在管理员权限cmd下启动wfastcgi-enable，得到类似这样的信息 c:\\Users\\ss\\AppData\\Local\\Programs\\Python\\Python37\\python.exe|c:\\Users\\ss\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\wfastcgi.py"
3. 新建一个网站，添加网站名称，路径以及端口。
4. 网站里选择应用程序设置
    1. DJANGO\_SETTINGS\_MODULE : FileShareSystem.settings , FileShareSystem是项目，settings的文件
    2. PYTHONPATH：E:\\onedrive\\outsourcing\\k505\\FileShareSystem ，项目的跟文件
    3. WSGI\_HANDLER ： django.core.wsgi.get\_wsgi\_application()
5. 网站里选择处理程序映射，找到“Python FastCgi”，重要的是打开之后确定，相当于启动。
6. 修改进程标识，应用程序池/网站/进程模型/标识中，改为LocalSystem
7. static文件设置
    1. 将setting.py中修改
        
        ```
        STATIC_URL = '/static/'
        STATIC_ROOT= os.path.join(BASE_DIR, 'static')
        ```
        
    2. 在static目录下添加web.config
        
        ```
        <?xml version="1.0" encoding="UTF-8"?>
            <configuration>
              <system.webServer>
              <!-- this configuration overrides the FastCGI handler to let IIS serve the static files -->
              <handlers>
                <clear/>
           <add name="StaticFile" path="*" verb="*" modules="StaticFileModule" resourceType="File" requireAccess="Read" />
             </handlers>
           </system.webServer>
        </configuration>
        ```
