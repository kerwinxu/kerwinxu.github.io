---
layout: post
title: "python模拟modbus传感器从站"
date: "2025-02-09"
categories: 
  - "python"
---

```python
import modbus_tk.defines
import serial
import modbus_tk
from modbus_tk import modbus_rtu
import time
import random
import struct


def floatToUShort(f):
  return struct.unpack(">2H", struct.pack(">f",f))

ser = serial.Serial("com2",9600)
master = modbus_rtu.RtuServer(ser)

# 启动从站
master.start()

slave = master.add_slave(1) # 指定从站地址
slave.add_block('weight', modbus_tk.defines.HOLDING_REGISTERS,0,2)  # 保持寄存器，地址0，2个寄存器，是重量

while True:
  # 设立每个10ms设置一下
  time.sleep(0.01)
  random_number = random.random() * 3 # 0-3kg随机浮点数
  slave.set_values('weight', 0, floatToUShort(random_number))



  


  
  

```
