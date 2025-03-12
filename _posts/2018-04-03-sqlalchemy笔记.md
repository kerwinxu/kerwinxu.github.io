---
layout: post
title: "sqlalchemy笔记"
date: "2018-04-03"
categories: 
  - "python"
---

1. 简单介绍。
    1. 一般步骤
        1. 导入
            1. from sqlalchemy import create\_engine from sqlalchemy.orm import sessionmaker from sqlalchemy.ext.declarative import declarative\_base from sqlalchemy import Column, Integer, String
        2. 创建数据库引擎 # 连接字符串 DB\_CONNECT\_STRING = "mysql+pymysql://business:nicaibudaola111@localhost/business\_one" engine = create\_engine(DB\_CONNECT\_STRING, connect\_args={ 'charset': 'utf8'}, echo=True) # 创建数据库引擎
        3. 创建数据库会话类 DB\_Session = sessionmaker(bind=engine) # 数据库会话类
        4. 创建会话类的实例 session = DB\_Session() # 数据库会话类的实例
        5. 创建每个对象 DB\_Base = declarative\_base()
2. 错误：
    1. 中文乱码
        1.  engine = create\_engine(DB\_CONNECT\_STRING, connect\_args={'charset': 'utf8'}, echo=True) #经验证，这种可以。
        2. ```
            class User(Base):
                __tablename__ = 'tb_user’
                    id = Column(Integer,primary_key = True,autoincrement=True)
                name = Column(String(250),nullable=False,unique = True,comment=u"姓名")
                __table_args__ = {
                    "mysql_charset" : "utf8"
            }  <.pre>/li>
            ```
            
    2. 将ORM对象转化成pandas的DataFrame
        1. df = pd.read\_sql(query.statement, query.session.bind)
    3. 批量删除问题
        1. 不能直接用delete
        2. ```
            session.query(User).filter(User.id.in_((1, 2, 3))).delete(synchronize_session=False)
            session.commit() # or session.expire_all()
            ```
            
        3. 搜了下找到[《Sqlalchemy delete subquery》](http://stackoverflow.com/questions/7892618/sqlalchemy-delete-subquery)这个问题，提到了 delete 的一个注意点：删除记录时，默认会尝试删除 session 中符合条件的对象，而 in 操作估计还不支持，于是就出错了。解决办法就是删除时不进行同步，然后再让 session 里的所有实体都过期：
