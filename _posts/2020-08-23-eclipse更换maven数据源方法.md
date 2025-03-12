---
layout: post
title: "Eclipse更换Maven数据源方法"
date: "2020-08-23"
categories: 
  - "java"
---

1. 建立一个xml文件
    
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
        <mirrors>
            <mirror>
                <id>nexus</id>
                <name>Tedu Maven</name>
                <mirrorOf>*</mirrorOf>
                <url>http://maven.aliyun.com/nexus/content/groups/public</url>
            </mirror>
        </mirrors>
    </settings>
    ```
    
     
2. Eclipse中Maven更换指定配置文件，具体是window/preference/maven/user setting ，我在global setting导入上边的文件了。
