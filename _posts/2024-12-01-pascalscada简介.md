---
title: "pascalSCADA简介"
date: "2024-12-01"
categories: 
  - "lazarus"
---

- HMI： 一堆控件
    - 常用控件，文本框，编辑框之类的
    - 绘图的
        - HMIBasicEletricMotor ： 基本电机样式
        - HMIPolyline ：多边形
        - HMIBasicValve ：
        - HMIBasicVectorControl : svg图形的
        - HMIFitaBasica ： 基本磁带的
        - HMIRoscaBasica ： 基本螺纹的
        - HMIRedlerBasico ： 砌砖的样子
    - Flow ： 跟随的，
        - Conditions ： 一堆条件
        -  AffectedObjects ： 影响的控件
        - 包括控件
            - HMIControlDislocatorAnimation ： 更改某个控件的坐标（locator是坐标）
            - HMIBooleanPropertyConnector ： 更改某个控件中某个布尔值属性的
            - HMIColorPropertyConnector ：更改某个控件中某个颜色值属性的
    - link ：
