---
layout: post
title: "spring基于注解装配Bean"
date: "2021-10-04"
categories: 
  - "java"
---

# Spring 中常用的注解如下

1）@Component 可以使用此注解描述 Spring 中的 Bean，但它是一个泛化的概念，仅仅表示一个组件（Bean），并且可以作用在任何层次。使用时只需将该注解标注在相应类上即可。 2）@Repository 用于将数据访问层（DAO层）的类标识为 Spring 中的 Bean，其功能与 @Component 相同。 3）@Service 通常作用在业务层（Service 层），用于将业务层的类标识为 Spring 中的 Bean，其功能与 @Component 相同。 4）@Controller 通常作用在控制层（如 Struts2 的 Action、SpringMVC 的 Controller），用于将控制层的类标识为 Spring 中的 Bean，其功能与 @Component 相同。 5）@Autowired 可以应用到 Bean 的属性变量、属性的 setter 方法、非 setter 方法及构造函数等，配合对应的注解处理器完成 Bean 的自动配置工作。默认按照 Bean 的类型进行装配。 6）@Resource 作用与 Autowired 相同，区别在于 @Autowired 默认按照 Bean 类型装配，而 @Resource 默认按照 Bean 实例名称进行装配。

@Resource 中有两个重要属性：name 和 type。

Spring 将 name 属性解析为 Bean 的实例名称，type 属性解析为 Bean 的实例类型。如果指定 name 属性，则按实例名称进行装配；如果指定 type 属性，则按 Bean 类型进行装配。如果都不指定，则先按 Bean 实例名称装配，如果不能匹配，则再按照 Bean 类型进行装配；如果都无法匹配，则抛出 NoSuchBeanDefinitionException 异常。 7）@Qualifier 与 @Autowired 注解配合使用，会将默认的按 Bean 类型装配修改为按 Bean 的实例名称装配，Bean 的实例名称由 @Qualifier 注解的参数指定。

## 总结

@Component、@Repository、@Service、@Controller 是声明这个是一个Bean，之后有一个名字，就是Bean的id。

而@Autowired和@Resource是自动装配，比如@Resource(name\="userDao")是装配id为userDao的对象。

 

# 示例

## 示例1

```
package net.biancheng;

public interface UserDao {
    /**
     * 输出方法
     */
    public void outContent();

}
```

```
package net.biancheng;

import org.springframework.stereotype.Repository;

@Repository("userDao")
public class UserDaoImpl implements UserDao {

    @Override
    public void outContent() {
        System.out.println("编程帮");
    }

}
```

```
package net.biancheng;

public interface UserService {
    /**
     * 输出方法
     */
    public void outContent();
}
```

```
package net.biancheng;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

@Service("userService")
public class UserServiceImpl implements UserService{
   
    @Resource(name="userDao")
    private UserDao userDao;
   

    public UserDao getUserDao() {
        return userDao;
    }


    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }


    @Override
    public void outContent() {
        userDao.outContent();
        System.out.println("一个在线学习编程的网站");
    }

}
```

```
package net.biancheng;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;

@Controller("userController")
public class UserController {
    @Resource(name = "userService")
    private UserService userService;

    public UserService getUserService() {
        return userService;
    }

    public void setUserService(UserService userService) {
        this.userService = userService;
    }

    public void outContent() {
        userService.outContent();
        System.out.println("专注于分享优质编程教程");
    }

}
```

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
    http://www.springframework.org/schema/context
            http://www.springframework.org/schema/context/spring-context.xsd">

    <!--使用context命名空间，通知spring扫描指定目录，进行注解的解析 -->
    <context:component-scan
        base-package="net.biancheng" />

</beans>
```

```
package net.biancheng;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainApp {
    public static void main(String[] args) {

        ApplicationContext ctx = new ClassPathXmlApplicationContext("Beans.xml");
        UserController uc = (UserController) ctx.getBean("userController");
        uc.outContent();
    }
}
```

 

运行结果：

```
编程帮
一个在线学习编程的网站
专注于分享优质编程教程
```
