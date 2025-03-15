---
layout: post
title: "django部署在win上的iis上"
date: "2024-12-17"
categories: ["python", "Django"]
---

步骤

1. 安装 pip install wfastcgi  
2. 在管理员权限cmd下启动wfastcgi-enable，得到类似这样的信息
3. 新建一个网站，添加网站名称，路径以及端口。
4. 网站里选择应用程序设置
    1. DJANGO\_SETTINGS\_MODULE : FileShareSystem.settings , FileShareSystem是项目，settings的文件
    2. PYTHONPATH：E:\onedrive\outsourcing\k505\FileShareSystem ，项目的根文件
    3. WSGI\_HANDLER ： django.core.wsgi.get\_wsgi\_application()
5. 网站里选择处理程序映射，找到“Python FastCgi”，重要的是打开之后确定，相当于启动。
6. 修改进程标识，应用程序池/网站/进程模型/标识中，改为LocalSystem
7. static文件设置,
    1. 将setting.py中修改
        ```python
		STATIC_URL = '/static/'   # 每个app下的资源文件夹都是这个名称  
		STATIC_ROOT= os.path.join(BASE_DIR, 'static') # 会将所有的app下的目录都汇总到这个文件夹下
		# 如下的是要追加 
		TEMPLATES = [
			{
				"BACKEND": "django.template.backends.django.DjangoTemplates",
				"DIRS": [],
				"APP_DIRS": True,
				"OPTIONS": {
					"context_processors": [
						"django.template.context_processors.debug",
						"django.template.context_processors.request",
						'django.template.context_processors.static',    # 追加这一行
						"django.contrib.auth.context_processors.auth",
						"django.contrib.messages.context_processors.messages",
					],
				},
			},
		]

        ```

	2. 在url.py中追加如下的代码
	    ```python
		from django.conf.urls.static import static
		from django.conf import settings
		urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)  # 添加根目录。
		```
	3. 在项目的根目录执行，会将所有app下的静态资源统一目录，
	    ```
		python manage.py collectstatic
		```

