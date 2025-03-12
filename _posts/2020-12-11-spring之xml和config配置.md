---
title: "spring之xml和config配置"
date: "2020-12-11"
categories: 
  - "java"
---

# 前言

为了送耦合

# xml配置

比如如下的一个简单的bean

```
package com.yiibai.core;

/**
 * Spring bean
 * 
 */
public class HelloWorld {
  private String name;

  public void setName(String name) {
    this.name = name;
  }

  public void printHello() {
    System.out.println("Spring 3 : Hello ! " + name);
  }
} 

```

如下是xml的配置文件

```
<beans xmlns="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
  http://www.springframework.org/schema/beans/spring-beans-3.0.xsd">

  <bean id="helloBean" class="com.yiibai.core.HelloWorld">
    <property name="name" value="Yiibai" />
  </bean>

</beans>

```

然后执行代码

```
package com.yiibai.core;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
  public static void main(String[] args) {
    ApplicationContext context = new ClassPathXmlApplicationContext(
        "applicationContext.xml"); HelloWorld obj = (HelloWorld) context.getBean("helloBean");
    obj.printHello();
  }
} 

```

简单点，如果要修改成其他的类或者属性，只要再xml配置中修改一下就可以了，松耦合。

 

# config配置方式

跟xml最大的区别是，有一个config的类来做这类事情。

比如如下的

```
package com.yiibai.hello;
 
public interface HelloWorld {
  
  void printHelloWorld(String msg);
 
}
```

```
package com.yiibai.hello.impl;

import com.yiibai.hello.HelloWorld;

public class HelloWorldImpl implements HelloWorld {

  @Override
  public void printHelloWorld(String msg) {

    System.out.println("Hello : " + msg);
  }

}
```

使用 @Configuration 注释告诉 Spring，这是核心的 Spring 配置文件，并通过 @Bean 定义 bean。

```
package com.yiibai.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import com.yiibai.hello.HelloWorld;
import com.yiibai.hello.impl.HelloWorldImpl;

@Configuration
public class AppConfig {
  
    @Bean(name="helloBean")
    public HelloWorld helloWorld() {
        return new HelloWorldImpl();
    }
  
}
```

执行结果

```
package com.yiibai.core;
 
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import com.yiibai.config.AppConfig;
import com.yiibai.hello.HelloWorld;
 
public class App {
  public static void main(String[] args) {
      
            ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
      HelloWorld obj = (HelloWorld) context.getBean("helloBean");
      
      obj.printHelloWorld("Spring Java Config");

  }
}
```
