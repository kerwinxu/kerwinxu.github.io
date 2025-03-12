---
title: "log4net中引发“System.Transactions.Diagnostics.DiagnosticTrace”的类型初始值设定项引发异常。"
date: "2017-07-05"
categories: 
  - "c"
---

解决方式是，

<configuration> <configSections> <section name="log4net" type="log4net.Config.Log4NetConfigurationSectionHandler, log4net"/> </configSections> <startup><supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0"/></startup>

<log4net> <!--定义输出到文件中--> <appender name="RollingLogFileAppender" type="log4net.Appender.RollingFileAppender">

如下是一堆的定义文件

将这个<configSections>节点放在<configuration>的第一个节点，
