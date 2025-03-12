---
layout: post
title: "modbus的crc校验之python版本"
date: "2024-06-14"
categories: 
  - "python"
---

```
def calc_crc(string):
    data = bytearray.fromhex(string)
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for i in range(8):
            if ((crc & 1) != 0):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return hex(((crc & 0xff) << 8) + (crc >> 8))


crc = calc_crc('02 04 13 88 00 14')
print(crc)
```
