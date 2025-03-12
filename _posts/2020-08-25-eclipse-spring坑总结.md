---
title: "eclipse/spring坑总结"
date: "2020-08-25"
categories: 
  - "java"
---

1. 这个是打包过程中的坑，JpaRepositoriesRegistrar.EnableJpaRepositoriesConfiguration: Cannot resolve reference to bean 'jpaMappingContext' while setting bean property 'mappingContext'; nested exception is org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'jpaMappingContext': Invocation of init method failed; nested exception is org.hibernate.service.spi.ServiceException: Unable to create requested service \[org.hibernate.engine.jdbc.env.spi.JdbcEnvironment\]
    - 解决方式：
        - 在启动类上添加@EnableJpaRepositories
            - ```
                @SpringBootApplication
                @EnableJpaRepositories
                public class SpringdemoApplication {
                
                  public static void main(String[] args) {
                    SpringApplication.run(SpringdemoApplication.class, args);
                  }
                
                }
                
                ```
