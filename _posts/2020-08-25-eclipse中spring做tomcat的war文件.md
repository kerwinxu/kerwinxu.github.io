---
layout: post
title: "eclipse中spring做Tomcat的war文件"
date: "2020-08-25"
categories: 
  - "java"
---

步骤如下：

 

1. 在pom.xml里设置
    
    ```
    packaging>war</packaging>
    ```
    
     
2. 除嵌入式tomcat插件
    
    在pom.xml里找到spring-boot-starter-web依赖节点，注释掉
    
    ```
    <!-- 		<dependency> -->
    <!-- 			<groupId>org.springframework.boot</groupId> -->
    <!-- 			<artifactId>spring-boot-starter-web</artifactId> -->
    <!-- 		</dependency> -->
    <!-- 		<dependency> -->
    <!-- 		    <groupId>com.fasterxml.jackson.core</groupId> -->
    <!-- 		    <artifactId>jackson-annotations</artifactId> -->
    <!-- 		    <version>2.11.2</version> -->
    <!-- 		</dependency> -->
        <dependency>
            <groupId>org.apache.tomcat</groupId>
            <artifactId>tomcat-servlet-api</artifactId>
            <version>9.0.37</version>
            <scope>provided</scope>
        </dependency>
    ```
    
     
3. 然后添加 org.apache.tomcat 依赖，如上。
4. 若想要定义项目打包的名字，加如下配置
    
    ```
    <build>
        <finalName>project name</finalName>
        <plugins>
          <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
          </plugin>
        </plugins>
      </build>
    ```
    
     
5. 修改启动类，修改启动类，并重写初始化方法
    
    我们法需要类似于web.xml的配置方式来启动spring上下文了，在Application类的同级添加一个SpringBootStartApplication类，其代码如下:
    
    ```
    /**
     * 修改启动类，继承 SpringBootServletInitializer 并重写 configure 方法
     */
    
    
    public class SpringBootStartApplication extends SpringBootServletInitializer {
     
          public static void main( String[] args ){
        	SpringApplication.run(SpringBootStartApplication .class, args);
    }
         /**
          *新增此方法
          */
          @Override
        protected SpringApplicationBuilder configure(SpringApplicationBuilder builder) {
            // 注意这里要指向原先用main方法执行的Application启动类
            return builder.sources(SpringBootStartApplication .class);
        }
    }
    ```
    
     
6. 打包，就是点击项目右键—> run as—>maven build：
7. 部署，把target目录下的war包放到tomcat的webapps目录下，启动tomcat，即可自动解压部署：（tomcat/bi目录下，双击startup.bat即可启动tomcat，成功启动，自动解压部署运行）
8. 访问 ： http://localhost:\[端口号\]/\[项目名\]/  ，比如要有这个项目名（war的文件名），因为会生成这个目录。
