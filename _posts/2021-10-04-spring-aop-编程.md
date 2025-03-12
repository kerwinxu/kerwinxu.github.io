---
title: "Spring AOP 编程"
date: "2021-10-04"
categories: 
  - "数学"
---

# 通用AOP术语

如下这个是通用的，但或许在不同的实现中名称稍有不同。

| 名称 | 说明 |
| --- | --- |
| Joinpoint（连接点） | 指那些被拦截到的点，在 Spring 中，指可以被动态代理拦截目标类的方法。 |
| Pointcut（切入点） | 指要对哪些 Joinpoint 进行拦截，即被拦截的连接点。 |
| Advice（通知） | 指拦截到 Joinpoint 之后要做的事情，即对切入点增强的内容。 |
| Target（目标） | 指代理的目标对象。 |
| Weaving（植入） | 指把增强代码应用到目标上，生成代理对象的过程。 |
| Proxy（代理） | 指生成的代理对象。 |
| Aspect（切面） | 切入点和通知的结合。 |

Advice 直译为通知，也有的资料翻译为“增强处理”，共有 5 种类型，如下表所示。

| 通知 | 说明 |
| --- | --- |
| before（前置通知） | 通知方法在目标方法调用之前执行 |
| after（后置通知） | 通知方法在目标方法返回或异常后调用 |
| after-returning（返回后通知） | 通知方法会在目标方法返回后调用 |
| after-throwing（抛出异常通知） | 通知方法会在目标方法抛出异常后调用 |
| around（环绕通知） | 通知方法会将目标方法封装起来 |

# Spring 的AOP

 

# 示例

## 示例1

没有AOP的情况

这个例子是基于gradle创建的，首先 build.gradle 文件添加依赖：

```
dependencies {
    compile 'org.springframework:spring-context:5.0.6.RELEASE'
}
```

首先接口

```
package com.sharpcj.aopdemo.test1;

public interface IBuy {
    String buy();
}
```

然后是两个实现

```
package com.sharpcj.aopdemo.test1;

import org.springframework.stereotype.Component;

@Component
public class Boy implements IBuy {
    @Override
    public String buy() {
        System.out.println("男孩买了一个游戏机");
        return "游戏机";
    }
}
```

```
package com.sharpcj.aopdemo.test1;

import org.springframework.stereotype.Component;

@Component
public class Girl implements IBuy {
    @Override
    public String buy() {
        System.out.println("女孩买了一件漂亮的衣服");
        return "衣服";
    }
}
```

spring的配置文件

```
package com.sharpcj.aopdemo;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackageClasses = {com.sharpcj.aopdemo.test1.IBuy.class})
public class AppConfig {
}
```

测试类

```
package com.sharpcj.aopdemo;

import com.sharpcj.aopdemo.test1.Boy;
import com.sharpcj.aopdemo.test1.Girl;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class AppTest {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        Boy boy = context.getBean("boy",Boy.class);
        Girl girl = (Girl) context.getBean("girl");
        boy.buy();
        girl.buy();
    }
}
```

运行结果

```
男孩买了一个游戏机
女孩买了一件漂亮的衣服
```

这里运用SpringIOC里的自动部署。现在需求改变了，我们需要在男孩和女孩的 buy 方法之前，需要打印出“男孩女孩都买了自己喜欢的东西”。用 Spring AOP 来实现这个需求只需下面几个步骤：

1、 既然用到 Spring AOP, 首先在 build.gralde 文件中引入相关依赖：

```
dependencies {
    compile 'org.springframework:spring-context:5.0.6.RELEASE'
    compile 'org.springframework:spring-aspects:5.0.6.RELEASE'
}
```

 

2、 定义一个切面类，BuyAspectJ.java

```
package com.sharpcj.aopdemo.test1;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class BuyAspectJ {
    @Before("execution(* com.sharpcj.aopdemo.test1.IBuy.buy(..))")
    public void haha(){
        System.out.println("男孩女孩都买自己喜欢的东西");
    }
}
```

 

这个类，我们使用了注解 @Component 表明它将作为一个Spring Bean 被装配，使用注解 @Aspect 表示它是一个切面。 类中只有一个方法 haha 我们使用 @Before 这个注解，表示他将在方法执行之前执行。关于这个注解后文再作解释。 参数("execution(\* com.sharpcj.aopdemo.test1.IBuy.buy(..))") 声明了切点，表明在该切面的切点是com.sharpcj.aopdemo.test1.Ibuy这个接口中的buy方法。

3、 在配置文件中启用AOP切面功能

```
package com.sharpcj.aopdemo;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration
@ComponentScan(basePackageClasses = {com.sharpcj.aopdemo.test1.IBuy.class})
@EnableAspectJAutoProxy(proxyTargetClass = true)
public class AppConfig {
}
```

我们在配置文件类增加了`@EnableAspectJAutoProxy`注解，启用了 AOP 功能，参数`proxyTargetClass`的值设为了 true 。默认值是 false

测试结果如下

```
男孩女孩都买了自己喜欢的东西
男孩买了一台游戏机
男孩女孩都买了自己喜欢的东西
女孩买了一件漂亮的衣服
```

可以看到我们并没有修改Boy 和 Girl 类的 Buy 方法，也没有修改测试类的代码，几乎是完全无侵入式地实现了需求。这就是 AOP 的“神奇”之处。

 

 

 

 

 

# 参考

- [https://www.cnblogs.com/joy99/p/10941543.html](https://www.cnblogs.com/joy99/p/10941543.html)
