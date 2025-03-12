---
title: "使用MyBatis Generator逆向工程报错：元素类型为 \"context\" 的内容必须匹配"
date: "2020-08-27"
categories: 
  - "java"
---

配置文件 generatorConfig.xml 里面的context的子元素必须按照它给出的顺序，如下是我找的一个正确的顺序

 

```
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE generatorConfiguration PUBLIC
        "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd" >
<generatorConfiguration>
    <!-- 本地数据库驱动程序jar包的全路径  使用时改称自己的本地路径-->
    <classPathEntry location="D:/software/Mavenrepo/mysql/mysql-connector-java/5.1.44/mysql-connector-java-5.1.44.jar"/>
    <context id="context" targetRuntime="MyBatis3">
    <!--定义生成的java类的编码格式-->
        <property name="javaFileEncoding" value="UTF-8"/>
        
        <!--suppressAllComments 设置为true 则不再生成注释-->
        <commentGenerator>
            <property name="suppressAllComments" value="true" />
        </commentGenerator>

        <!-- 数据库的相关配置 -->
        <jdbcConnection
                driverClass="com.mysql.cj.jdbc.Driver"
                connectionURL="jdbc:mysql://localhost:3306/ssm_crud"
                userId="root"
                password="123"/>

        <javaTypeResolver>
            <property name="forceBigDecimals" value="false"/>
        </javaTypeResolver>

        <!-- 实体类生成的位置 -->
        <javaModelGenerator targetPackage="com.ltq.model" targetProject="src/main/java">
            <property name="trimStrings" value="true"/>
        </javaModelGenerator>

        <!-- Mapper.xml 文件的位置 -->
        <sqlMapGenerator targetPackage="mapper" targetProject="src/main/resources">
        </sqlMapGenerator>

        <!-- Mapper 接口文件的位置 -->
        <javaClientGenerator targetPackage="com.ltq.mapper" targetProject="src/main/java" type="XMLMAPPER">
        </javaClientGenerator>

        <!-- table指定每个生成表的生成策略  表名 和 model实体类名-->
        <table tableName="tbl_emp" domainObjectName="Employee" enableSelectByExample="true"
               enableDeleteByExample="true" enableCountByExample="true"
               enableUpdateByExample="true" selectByExampleQueryId="true">
            <property name="ignoreQualifiersAtRuntime" value="false"/>
            <property name="useActualColumnNames" value="false"/>
        </table>
        <table tableName="tbl_dept" domainObjectName="Department" enableSelectByExample="true"
               enableDeleteByExample="true" enableCountByExample="true"
               enableUpdateByExample="true" selectByExampleQueryId="true">
            <property name="ignoreQualifiersAtRuntime" value="false"/>
            <property name="useActualColumnNames" value="false"/>
        </table>
    </context>
</generatorConfiguration>
```

若想要生成全部表 使用 tableName="%" 即可
