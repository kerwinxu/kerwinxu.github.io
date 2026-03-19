---
layout: post
title: "Django迁移数据库从mysql到Postgresql"
date: "2026-03-19"
categories: ["数据库", "PostgreSQL"]
math: true
---

1. 安装Postgresql的驱动，我安装的是psycopg2，好像别人安装的是psycopg2-binary。
1. 在PostgreSQL中创建数据库，主要是为了在settings中设置。
1. 用Django从mysql中导出数据
   1. ```python manage.py dumpdata  > datadump.json ```
1. 将“datadump.json”的编码改成utf8，原因是我创建的数据库中是这个编码。
1. 修改Django中settings.py的配置
1. 加载数据
   1. ```python manage.py migrate --run-syncdb```
   1. ```python manage.py loaddata datadump.json```



```python
# settings文件数据库的配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '新数据库名',
        'USER': '用户名',
        'PASSWORD': '密码',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
