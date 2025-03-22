---
layout: post
title:  Django转成mysql数据库
date:   2025-3-22 20:12:00 +0800
categories: ["python", "django"]
project: false
excerpt: Django转成mysql数据库
lang: zh
published: true
tag:
- python
- django
- mysql
---

Django默认是sqlite数据库，我这里转成mysql数据库，原先的sqlite已经有大量的数据。  

# 安装依赖
```
pip install pymysql
```
修改settings.py的同级目录下的__init__.py,追加
```python
import pymysql
pymysql.install_as_MySQLdb()
```
# 导出数据
```
python -Xutf8 manage.py dumpdata --exclude auth.permission --exclude contenttypes -o db.json
```
# 修改数据库
修改settings.py文件
```python
DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
	'default': {
		'ENGINE': 'django.db.backends.mysql', # 或 'django.db.backends.postgresql'
		'NAME': 'shop_contact',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': 'localhost',
		'PORT': '3306', # 对于 PostgreSQL，端口通常是 5432
	}
}

```

# 建立数据库
在新的数据库中建立表结构
```
python manage.py migrate
```
# 迁移数据
```
python -Xutf8 manage.py loaddata db.json
```