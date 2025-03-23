---
layout: post
title: "Django4管理admin"
date: "2022-12-16"
categories: 
  - "python"
---

# 前言

这个管理真的太好用了，这里单独用一个文章。

 

# 打开步骤

## 创建一个超级用户

```
python3 manage.py createsuperuser
```

会要求输入用户和密码

## 将模型注册

### 通用的

这个是用Django的默认页面来操作

```
admin.site.register(Book)
```

### 定制的注册 一个 ModelAdmin 类

两种方式吧

```python
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
```

 

注册器的方式

```python
# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
```

 

# 高级配置

## 配置列表视图

```python
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
```

注意：这个不能指定ManyToManyField 的字段，可以定义一个函数来获取。

```python
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') # 这个display_genre是用函数来获取的。

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
```

 

## 基本设置

```python
from django.contrib import admin
from blog.models import Blog
  
#Blog模型的管理器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'caption', 'author', 'publish_time')
    
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-publish_time',)
  
    #list_editable 设置默认可编辑字段
    list_editable = ['machine_room_id', 'temperature']
  
    #fk_fields 设置显示外键字段
     fk_fields = ('machine_room_id',)
```

我们可以设置其他字段也可以点击链接进入编辑界面

```python
from django.contrib import admin
from blog.models import Blog
  
#Blog模型的管理器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):   
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'caption')
```

 

 

## 创建列表过滤器

列表视图现在将在右侧包含一个过滤器框

```python
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
```

```python
from django.contrib import admin
from blog.models import Blog
  
#Blog模型的管理器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'author', 'publish_time')
     
    #筛选器
    list_filter =('trouble', 'go_time', 'act_man__user_name', 'machine_room_id__machine_room_name') #过滤器
    search_fields =('server', 'net', 'mark') #搜索字段
    date_hierarchy = 'go_time'    # 详细时间分层筛选
```

 

## 颜色显示

```python
from django.db import models
from django.contrib import admin
from django.utils.html import format_html
 
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=6)
 
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            self.color_code,
            self.first_name,
            self.last_name,
        )
 
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'colored_name')
```

是在模型中写的，而不是在AdminModel中写的。

## 调整页面头部显示内容和页面标题

```python
class MyAdminSite(admin.AdminSite):
    site_header = '好医生运维资源管理系统'  # 此处设置页面显示标题
    site_title = '好医生运维'  # 此处设置页面头部标题
 
admin_site = MyAdminSite(name='management')
```

 

需要注意的是： admin\_site = MyAdminSite(name='management') 此处括号内name值必须设置，否则将无法使用admin设置权限，至于设置什么值，经本人测试，没有影响。

注册的时候使用admin\_site.register，而不是默认的admin.site.register。

[![]](http://127.0.0.1/?attachment_id=4896)

后经网友提示发现也可以这样：

```python
from django.contrib import admin
from hys_operation.models import *
 
 
# class MyAdminSite(admin.AdminSite):
#     site_header = '好医生运维资源管理系统'  # 此处设置页面显示标题
#     site_title = '好医生运维'
#
# # admin_site = MyAdminSite(name='management')
# admin_site = MyAdminSite(name='adsff')
admin.site.site_header = '修改后'
admin.site.site_title = '哈哈'
```

## 通过当前登录的用户过滤显示的数据

[![]](http://127.0.0.1/?attachment_id=4897)

 

## 细节布局

### 控制哪些字段被显示和布局

```python
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
```

如上2个的区别

- list\_display 是显示多个模型的数据，以列表的形式展示的。
- fields ： 是打开某个具体的模型，显示哪些？

fields默认是垂直展示的，而('date\_of\_birth', 'date\_of\_death')表示分组到一个元组中。

### 剖切细节视图

```python
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
```

fieldsets ，每个部分都有自己的标题，

## 关联记录的内联编辑

```python
class BooksInstanceInline(admin.TabularInline):
    # 内联模型
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
```
