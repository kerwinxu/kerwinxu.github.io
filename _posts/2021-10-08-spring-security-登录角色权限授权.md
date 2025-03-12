---
title: "spring Security  登录角色权限授权"
date: "2021-10-08"
categories: 
  - "java"
---

# 需要

## 数据库设计

用户（user）  、角色 （role） 、  权限（authority ），之间都是多对多的关系

## UserDetails类

用一个类来继承UserDetails类，也或者可以用如上的user来继承

## UserDetailsService 接口

实现  UserDetailsService接口 重写LoadUserUsername方法，参数为用户名，返回的是UserDetails类

## WebSecurityConfigurerAdapter接口自定义Security策略

 

## AuthenticationManagerBuilder：自定义认证策略

 

## @EnableWebSecurity：开启WebSecurity模式
