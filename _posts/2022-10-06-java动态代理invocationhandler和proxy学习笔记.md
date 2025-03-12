---
layout: post
title: "Java动态代理InvocationHandler和Proxy学习笔记"
date: "2022-10-06"
categories: 
  - "java"
---

# Proxy

proxy是一个创建代理对象的类，最常用的是newProxyInstance方法，

 

# InvocationHandler

roxy代理实例的调用处理程序实现的一个接口，每一个proxy代理实例都有一个关联的调用处理程序；在代理实例调用方法时，方法调用被编码分派到调用处理程序的invoke方法

 

# 例子

一个接口

```
package Io.Github.Kerwinxu.LearnProxy;

public interface People {
  
    public	String work();

}
```

 

一个实现

```
package Io.Github.Kerwinxu.LearnProxy;

public class Teacher implements People {

  @Override
  public String work() {
    System.out.println("老师教书育人...");
    return "教书";
  }

}
```

 

代理处理方法

```
package Io.Github.Kerwinxu.LearnProxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;

public class WorkHander implements InvocationHandler {
  
  /**
   * 代理类中的真正的对象
   */
  private Object object;
  
  // 2个构造函数
  
  public WorkHander() {
    
  }
  
  public WorkHander(Object object) {
    this.object = object;
  }

  public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
    // 在真实的对象执行之前，我们可以添加自己的操作
    System.out.println("before invoke ...");
    Object invokeObject = method.invoke(getObject(), args); // 执行getObject对象的method方法，参数是args
    System.out.println("after invoke ...");
    return invokeObject;
  }
  
  public Object getObject()
  {
    return this.object;
  }

}

```

 

主程序

```
package Io.Github.Kerwinxu.LearnProxy;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.util.logging.Handler;

public class Test {

  public static void main(String[] args) {
    // 要代理的真实的对象
    People people = new Teacher();
    // 代理对象的调用处理函数
    InvocationHandler handerHandler = new WorkHander(people);
    //
    People proxy = (People)Proxy.newProxyInstance(
        handerHandler.getClass().getClassLoader(),      // 取得ClassLoader对象
        people.getClass().getInterfaces(),   // 为代理类提供的接口为真实的接口，这样代理对象就可以像真实对象一样调用接口中的所有方法
        handerHandler);                      // 处理方法的
    
    System.out.println(proxy.work());

  }

}
```
