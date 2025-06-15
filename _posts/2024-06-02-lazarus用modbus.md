---
layout: post
title: "lazarus用modbus"
date: "2024-06-02"
categories: 
  - "lazarus"
  - "计算机语言"
---

要点；

- pascalSCADA安装：需要先安装如下3个
    - ZeosLib
    - BGRABitmap
    - BGRAControls
- 使用
    - SerialPortDriver ： 串口相关，主要设置串口名称，波特率等。
    - ModBusRTUDriver ：modbus的串口驱动
        - CommunicationPort : 通过哪个串口
    - PLCTagNumber ： modbus的一个数字，通常对应固定数量的寄存器
        - protocolDriver ： 哪个驱动的
        - ScaleProcessor :  转换器的
        - TagType : 设置数据类型，可以设置整数或者浮点数等。
        - MemAddress : 寄存器的地址
        - MemReadFunction : 读的功能号,
        - MemWriteFunction : 写的功能号。
        - PLCStation ： 从机地址。
    - HMILabel ： 这个可以显示只读的数据
        - PLCTag ： 对应上边的PLCTagNumber
        - Prefix ： 前缀

关于功能号的
|类型|读|写|
|--|--|--|
|Digital inputs|2|0|
|Coils (digital outputs)|1|5(TPLCTagNumber)<br>15(TPLCTagNumber，TPLCBlock，TPLCStruct，TPLCString)|
|Registers|3|6(TPLCTagNumber)<br>16(TPLCTagNumber，TPLCBlock，TPLCStruct，TPLCString)|
|Analog registers (analog inputs)|4|0|
|Device status|7|0|


 

发现swap的选项，如果大于一个字节，比如2字节，4字节之类的可以用Swap来交换。 比如默认情况下，如果是2个寄存器，我需要将swapWord设置为真，表示两个字之间交换。
