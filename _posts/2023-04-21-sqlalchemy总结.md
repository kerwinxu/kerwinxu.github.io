---
layout: post
title: "SQLAlchemy总结"
date: "2023-04-21"
categories: 
  - "python"
---

# 重要概念

<table style="border-collapse: collapse; width: 100%;"><tbody><tr><td style="width: 14.5454%;">概念</td><td style="width: 15.5151%;">对应数据库</td><td style="width: 69.9394%;">说明</td></tr><tr><td style="width: 14.5454%;">Engine</td><td style="width: 15.5151%;">连接</td><td style="width: 69.9394%;"></td></tr><tr><td style="width: 14.5454%;">Session</td><td style="width: 15.5151%;">连接池、事务</td><td style="width: 69.9394%;">由此开始查询</td></tr><tr><td style="width: 14.5454%;">Model</td><td style="width: 15.5151%;">表</td><td style="width: 69.9394%;">类定义和表定义类似，类定义本质上是其中一行</td></tr><tr><td style="width: 14.5454%;">Column</td><td style="width: 15.5151%;">列</td><td style="width: 69.9394%;">在各个地方支持运算符运算</td></tr><tr><td style="width: 14.5454%;">Query</td><td style="width: 15.5151%;">若干行</td><td style="width: 69.9394%;">可以链式操作添加条件，1，select，2，delete， 3，update</td></tr></tbody></table>

 

# 模型

```
# coding=utf-8
from __future__ import unicode_literals, absolute_import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
ModelBase = declarative_base() #<-元类

class User(ModelBase):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True)
    date_joined = Column(DateTime)
    username = Column(String(length=30))
    password = Column(String(length=128))
```

创建表

```
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
ModelBase.metadata.create_all(engine)
```

是根据engine创建的

```
如下所有的都要先创建Session
```

```
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
# 实例化
session = Session()

# 真正提交到数据库
session.commit()
```

# 回滚

在调用commit以前，都可以调用rollback进行回滚，本质上只是把某一条数据（也就是映射类的实例）从内存中删除而已，并没有对数据库有任何操作。

# 增加

```
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname') # 在内存中创建了一个对象
session.add(ed_user)  # 添加到会话中，等待添加。
session.commit()      # 提交，这里才是真正的更新。
```

# 查询

通过 **query** 关键字查询。

```
>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flintstone
```

- query.filter() 过滤
- query.filter\_by() 根据关键字过滤
- query.all() 返回列表
- query.first() 返回第一个元素
- query.one() 有且只有一个元素时才正确返回
- query.one\_or\_none()，类似one，但如果没有找到结果，则不会引发错误
- query.scalar()，调用one方法，并在成功时返回行的第一列
- query.count() 计数
- query.order\_by() 排序

**query.join()** 连接查询

```
>>> session.query(User).join(Address).\
...         filter(Address.email_address=='jack@google.com').\
...         all()
[<User(name='jack', fullname='Jack Bean', nickname='gjffdd')>]
```

**query(column.label())** 可以为字段名（列）设置别名：

```
>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
ed
wendy
mary
fred
```

**aliased()**为查询对象设置别名：

```
>>> from sqlalchemy.orm import aliased
>>> user_alias = aliased(User, name='user_alias')

SQL>>> for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
<User(name='ed', fullname='Ed Jones', nickname='eddie')>
<User(name='wendy', fullname='Wendy Williams', nickname='windy')>
<User(name='mary', fullname='Mary Contrary', nickname='mary')>
<User(name='fred', fullname='Fred Flintstone', nickname='freddy')>
```

## 查询常用筛选器运算符

```
# 等于
query.filter(User.name == 'ed')

# 不等于
query.filter(User.name != 'ed')

# like和ilike
query.filter(User.name.like('%ed%'))
query.filter(User.name.ilike('%ed%')) # 不区分大小写

# in
query.filter(User.name.in_(['ed', 'wendy', 'jack']))
query.filter(User.name.in_(
    session.query(User.name).filter(User.name.like('%ed%'))
))
# not in
query.filter(~User.name.in_(['ed', 'wendy', 'jack'])) 

# is
query.filter(User.name == None)
query.filter(User.name.is_(None))

# is not
query.filter(User.name != None)
query.filter(User.name.is_not(None))

# and
from sqlalchemy import and_
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')

# or
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))

# match
query.filter(User.name.match('wendy'))
```

## 使用文本SQL

```
>>> from sqlalchemy import text
SQL>>> for user in session.query(User).\
...             filter(text("id<224")).\
...             order_by(text("id")).all():
...     print(user.name)
ed
wendy
mary
fred
```

# 删除数据

```
# ORM 删除一条多条数据
# 导入 ORM 创建会话
from my_create_table import User,engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# DELETE FROM `user` WHERE id=20
res = db_session.query(User).filter(User.id==20).delete()
print(res)
db_session.commit()

db_session.close()
#关闭会话
```

 

# 增改删查

```
增：session.add(User(name='jack', age=3))
删：session.query(User).filter(User.name == 'jack').delete()
改：session.query(User).filter(User.name == 'tom').update({"age": 2})
查：u = session.query(User).filter(User.name == 'tom')

```

 

 

# 关联关系

## 一对多

```
>>> from sqlalchemy import ForeignKey
>>> from sqlalchemy.orm import relationship

>>> class Address(Base):
...     __tablename__ = 'addresses'
...     id = Column(Integer, primary_key=True)
...     email_address = Column(String, nullable=False)
...     user_id = Column(Integer, ForeignKey('users.id'))
...
...     user = relationship("User", back_populates="addresses")
...
...     def __repr__(self):
...         return "<Address(email_address='%s')>" % self.email_address

>>> User.addresses = relationship(
...     "Address", order_by=Address.id, back_populates="user")
```

`ForeignKey`定义两列之间依赖关系，表示关联了用户表的用户ID

**relationship** 告诉ORM`Address`类本身应链接到`User`类，**back\_populates** 表示引用的互补属性名，也就是本身的表名。

## 多对多

创建一个关联表

```
>>> from sqlalchemy import Table, Text
>>> # association table
>>> post_keywords = Table('post_keywords', Base.metadata,
...     Column('post_id', ForeignKey('posts.id'), primary_key=True),
...     Column('keyword_id', ForeignKey('keywords.id'), primary_key=True)
... )
```

下一步我们定义`BlogPost`和`Keyword`，使用互补 **relationship** 构造，每个引用`post_keywords`表作为关联表：

```
>>> class BlogPost(Base):
...     __tablename__ = 'posts'
...
...     id = Column(Integer, primary_key=True)
...     user_id = Column(Integer, ForeignKey('users.id'))
...     headline = Column(String(255), nullable=False)
...     body = Column(Text)
...
...     # many to many BlogPost<->Keyword
...     keywords = relationship('Keyword',
...                             secondary=post_keywords,
...                             back_populates='posts')
...
...     def __init__(self, headline, body, author):
...         self.author = author
...         self.headline = headline
...         self.body = body
...
...     def __repr__(self):
...         return "BlogPost(%r, %r, %r)" % (self.headline, self.body, self.author)


>>> class Keyword(Base):
...     __tablename__ = 'keywords'
...
...     id = Column(Integer, primary_key=True)
...     keyword = Column(String(50), nullable=False, unique=True)
...     posts = relationship('BlogPost',
...                          secondary=post_keywords,
...                          back_populates='keywords')
...
...     def __init__(self, keyword):
...         self.keyword = keyword
```

 

# flush和commit的区别

flush() 会将session中的数据刷到数据库中，使数据库主键自增；但不会写到磁盘里。当别的session查询时并不会查到flush的数据；插入数据时，session1 flush()一条, session2 commit()一条，session2插入的主键会跳过session1 flush()产生的主键；

而commit在执行前会调用flush，并且写到磁盘中。
