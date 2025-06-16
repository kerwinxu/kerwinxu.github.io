---
layout: post
title: "plotformio使用stm32cubemx的配置"
date: "2025-01-24"
categories: ["计算机语言", "单片机编程"]
---

```
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter
;   Upload options: custom upload port, speed and extra flags
;   Library options: dependencies, extra library storages
;   Advanced options: extra scripting
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[platformio]
src_dir = ./     
; include_dir = ./Core/Inc   ; 一定要添加这个，否则会找不到头文件。

[env:genericSTM32F103C8]
platform = ststm32
board = genericSTM32F103C8
board_build.mcu = stm32f103c8t6
board_build.f_cpu = 8000000L
; framework = stm32cube
; upload_port=COM4
; 如下的两个，一个是用来上传，一个是用来调试，测试可以用
upload_protocol=cmsis-dap 
debug_tool=cmsis-dap

; -Idir是include文件目录, 这里随了GCC的语法
; build_flag本质上就是给arm-noeabi-gcc加上了编译参数，直接添加的，所以直接随的是GCC的语法
; framework = stm32cube（不用framework了）
; 编译配置-D是宏定义，-Idir是include文件目录,读者可按自己项目结构更改
; 这里笔者锐评一下: 这种方式就是会十分繁琐！必须依次指定所有的包含目录!
; 在已经存在支持的框架下，请优先使用platformIO已经支持的框架！
build_flags =      
    -DUSE_HAL_DRIVER   
  -DSTM32F103xB  ; 预定义宏, 看官可以理解为在一切源文件的开头加上了#define STM32F103xE
  -I./Core/Inc    ; 包含了源文件的路径
    -I./Drivers/STM32F1xx_HAL_Driver/Inc
    -I./Drivers/STM32F1xx_HAL_Driver/Inc/Legacy
    -I./Drivers/CMSIS/Device/ST/STM32F1xx/Include
    -I./Drivers/CMSIS/Include

;选择编译文件的所在路径，这里包含了源文件路径，启动文件，驱动库和rtos路径。如果+<*>便是路径下的所以文件，-<.git/>便是忽略.git路径下的文件
build_src_filter = +<Core/Src> +<startup_stm32f103xb.s> +<Drivers/STM32F1xx_HAL_Driver/Src> +<Middlewares/>


; src_dir就是告知我们的项目的大源文件地址在何处，它隶属于platformio模块的匹配
; https://docs.platformio.org/en/latest/projectconf/sections/platformio/options/directory/src_dir.html

;选择链接文件，我们的STM32上电后要执行一段启动脚本
board_build.ldscript = ./STM32F103C8Tx_FLASH.ld

extra_scripts = export_hex.py

```
