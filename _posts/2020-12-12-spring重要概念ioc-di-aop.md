---
title: "spring重要概念IoC/DI/AOP"
date: "2020-12-12"
categories: 
  - "java"
---

# IoC：Inverse of Control（控制反转）

- 读作**“反转控制”**，更好理解，不是什么技术，而是一种**设计思想**，就是**将原本在程序中手动创建对象的控制权，交由Spring框架来管理。**
- **正控：**若要使用某个对象，需要**自己去负责对象的创建**
- **反控：**若要使用某个对象，只需要**从 Spring 容器中获取需要使用的对象，不关心对象的创建过程**，也就是把**创建对象的控制权反转给了Spring框架**
- **好莱坞法则：**Don’t call me ,I’ll call you

例子：

一个类

```
package pojo;

public class Source {  
    private String fruit;   // 类型
    private String sugar;   // 糖分描述
    private String size;    // 大小杯    
    /* setter and getter */
}

```

xml文件

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean name="source" class="pojo.Source">
        <property name="fruit" value="橙子"/>
        <property name="sugar" value="多糖"/>
        <property name="size" value="超大杯"/>
    </bean>
</beans>
```

调用main吧。

```
package test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import pojo.Source;

public class TestSpring {

    @Test
    public void test(){
        ApplicationContext context = new ClassPathXmlApplicationContext(
                new String[]{"applicationContext.xml"}
        );

        Source source = (Source) context.getBean("source");
        System.out.println(source.getFruit());
        System.out.println(source.getSugar());
        System.out.println(source.getSize());
    }
}
```

 

# DI：Dependency Injection（依赖注入）

- 指 Spring 创建对象的过程中，**将对象依赖属性（简单值，集合，对象）通过配置设值给该对象**

继续上边的例子

```
package pojo;

public class JuiceMaker {

    // 唯一关联了一个 Source 对象
    private Source source = null;

    /* setter and getter */

    public String makeJuice(){
        String juice = "xxx用户点了一杯" + source.getFruit() + source.getSugar() + source.getSize();
        return juice;
    }
}

```

 

然后xml文档中使用 ref 来**注入**另一个对象

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean name="source" class="pojo.Source">
        <property name="fruit" value="橙子"/>
        <property name="sugar" value="多糖"/>
        <property name="size" value="超大杯"/>
    </bean>
    <bean name="juickMaker" class="pojo.JuiceMaker">
        <property name="source" ref="source" />
    </bean>
</beans>
```

main再多些一些代码，juickMaker中的属性是被注入的。

```
package test;

import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import pojo.JuiceMaker;
import pojo.Source;

public class TestSpring {

    @Test
    public void test(){
        ApplicationContext context = new ClassPathXmlApplicationContext(
                new String[]{"applicationContext.xml"}
        );

        Source source = (Source) context.getBean("source");
        System.out.println(source.getFruit());
        System.out.println(source.getSugar());
        System.out.println(source.getSize());

        JuiceMaker juiceMaker = (JuiceMaker) context.getBean("juickMaker"); //这个对象的xml配置中有ref，注入另一个对象。
        System.out.println(juiceMaker.makeJuice());
    }
}
```

 

 

# AOP 即 Aspect Oriented Program 面向切面编程

首先，在面向切面编程的思想里面，把功能分为核心业务功能，和周边功能。

- **所谓的核心业务**，比如登陆，增加数据，删除数据都叫核心业务
- **所谓的周边功能**，比如性能统计，日志，事务管理等等

周边功能在 Spring 的面向切面编程AOP思想里，即被定义为切面

在面向切面编程AOP的思想里面，核心业务功能和切面功能分别独立进行开发，然后把切面功能和核心业务功能 "编织" 在一起，这就叫AOP

#### AOP 的目的

AOP能够将那些与业务无关，**却为业务模块所共同调用的逻辑或责任（例如事务处理、日志管理、权限控制等）封装起来**，便于**减少系统的重复代码**，**降低模块间的耦合度**，并**有利于未来的可拓展性和可维护性**。

#### AOP 当中的概念：

- 切入点（Pointcut） 在哪些类，哪些方法上切入（**where**）
- 通知（Advice） 在方法执行的什么实际（**when:**方法前/方法后/方法前后）做什么（**what:**增强的功能）
- 切面（Aspect） 切面 = 切入点 + 通知，通俗点就是：**在什么时机，什么地方，做什么增强！**
- 织入（Weaving） 把切面加入到对象，并创建出代理对象的过程。（由 Spring 来完成）

例子：

一个类

```
package service;

public class ProductService {
    public void doSomeService(){
        System.out.println("doSomeService");
    }
}
```

xml

```
<bean name="productService" class="service.ProductService" />
```

一个切片类

```
package aspect;

import org.aspectj.lang.ProceedingJoinPoint;

public class LoggerAspect {
    
    public Object log(ProceedingJoinPoint joinPoint) throws Throwable {
        System.out.println("start log:" + joinPoint.getSignature().getName());
        Object object = joinPoint.proceed();
        System.out.println("end log:" + joinPoint.getSignature().getName());
        return object;
    }
}
```

xml配置

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:aop="http://www.springframework.org/schema/aop"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
   http://www.springframework.org/schema/beans
   http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
   http://www.springframework.org/schema/aop
   http://www.springframework.org/schema/aop/spring-aop-3.0.xsd
   http://www.springframework.org/schema/tx
   http://www.springframework.org/schema/tx/spring-tx-3.0.xsd
   http://www.springframework.org/schema/context
   http://www.springframework.org/schema/context/spring-context-3.0.xsd">

    <bean name="productService" class="service.ProductService" /> <!-- 被切入的类 -->
    <bean id="loggerAspect" class="aspect.LoggerAspect"/> <!-- 切入类 -->

    <!-- 配置AOP -->
    <aop:config>
        <!-- where：在哪些地方（包.类.方法）做增加 -->
        <aop:pointcut id="loggerCutpoint"
                      expression="execution(* service.ProductService.*(..)) "/>

        <!-- what:做什么增强 -->
        <aop:aspect id="logAspect" ref="loggerAspect"> <!-- 这个指向的是切入类 -->
            <!-- when:在什么时机（方法前/后/前后） -->
            <aop:around pointcut-ref="loggerCutpoint" method="log"/>  
        </aop:aspect>
    </aop:config>
</beans>
```

最后运行main，

我认为这个AOP可以在不修改代码的基础上更改代码。

 

# 总结

- IOC : 创建对象的控制权交给框架。
- DI ： 把有依赖关系的类的实例注入为指定类的实例。
- AOP ： 将切面交给框架，切面好比把方法切开。

# 引用

- [Spring框架的IOC、DI、AOP应用详解](https://www.jianshu.com/p/9cb11d34f242)
