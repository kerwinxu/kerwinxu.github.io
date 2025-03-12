---
layout: post
title: "eclipse maven jar中没有主清单属性"
date: "2021-03-28"
categories: 
  - "java"
---

打开pom.xml，添加如下内容

1.  添加打包的依赖，这里用shade
    
    ```
    <dependency>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.2.1</version>
    </dependency>
    ```
    
2. 添加build ，里边需要修改 <mainClass>com.xuhengxiao.shirosample.App</mainClass> ，起始的Main类。
    
    ```
    <build>
        <plugins>
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>3.2.1</version>
            <executions>
              <execution>
                <phase>package</phase>
                <goals>
                  <goal>shade</goal>
                </goals>
                <configuration>
                  <transformers>
                    <transformer
                      implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                      <mainClass>com.xuhengxiao.shirosample.App</mainClass>
                    </transformer>
                  </transformers>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    ```
