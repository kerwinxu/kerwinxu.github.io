---
layout: post
title: "python-snap7库模拟西门子s7plc"
date: "2026-05-15"
categories: ["计算机语言", "python"]
---

```python
from snap7 import Client, Server, SrvArea, type, util
from ctypes import c_char

# --- Server setup ---
server = Server()
# db_size = 100
# db_data = bytearray(db_size)
# db_array = (c_char * db_size).from_buffer(db_data)
# # server.register_area(SrvArea.DB, 1, db_array)

# 这里启用一些寄存器
server.register_area(SrvArea.DB, 1, (c_char * 2048).from_buffer(bytearray(2048))) # Db区域的2048字节
server.register_area(SrvArea.PE, 0, (c_char * 300).from_buffer(bytearray(300))) # 输入区的300字节
server.register_area(SrvArea.PA, 0, (c_char * 300).from_buffer(bytearray(300))) # 输出区的300字节
server.register_area(SrvArea.MK, 0, (c_char * 1024).from_buffer(bytearray(1024))) # M区的300字节


# 启动服务器
server.start(tcp_port=102)

# --- Client connection ---
client = Client()
client.connect("127.0.0.1", 0, 1, tcp_port=102)

# Write data
# client.db_write(1, 0, bytearray([0x01, 0x02, 0x03, 0x04]))
# 这里写入一些初始的数据
# 充气时间检测区域
vw62 = bytearray(2)
util.set_int(vw62, 0, 100)
client.write_area(area=type.Areas.DB, db_number=1, start=62, data=vw62)
VD60 = bytearray(2)
util.set_int(VD60, 0, 99)
client.write_area(area=type.Areas.DB, db_number=1, start=60, data=VD60)

# M区的M0
M0 = bytearray(1) #
util.set_bool(M0, 0, 0, False) # 复位状态
util.set_bool(M0, 0, 1, True)  # 运行状态
# util.set_bool(M0, 0, 2, True) # 清零的
util.set_bool(M0, 0, 3, False) # 通道1禁用
util.set_bool(M0, 0, 4, False) # 通道2禁用
util.set_bool(M0, 0, 5, True) # 通道3禁用
util.set_bool(M0, 0, 6, True) # 通道4禁用
util.set_bool(M0, 0, 7, True) # 调试模式

client.mb_write(0, 1, M0)




# 输入区
I0 = bytearray(1)
util.set_bool(I0, 0, 3, True) # 当前模式
client.eb_write(0,1, I0)

I1 = bytearray(1)
util.set_bool(I1, 0, 1, True) # 通道1气压
client.eb_write(1, 1, I1)



def db_write_int(start_byte_addr, bytes, value):
    util.set_int(bytes, 0, value)
    client.db_write(1, start_byte_addr, bytes)

def db_write_dint(start_byte_addr, bytes, value):
    util.set_dint(bytes, 0, value)
    client.db_write(1, start_byte_addr, bytes)


def db_write_real(start_byte_addr, bytes, value):
    util.set_real(bytes, 0, value)
    client.db_write(1, start_byte_addr, bytes)

# 用户区
VD0 = bytearray(2) # 生产数量
db_write_dint(0, VD0, 10)
VD4 = bytearray(2) # 良品数
db_write_dint(4, VD4, 4)
VD8 = bytearray(2) # 不良数
db_write_dint(8, VD8, 6)

# 泄露值
VD12 = bytearray(4) # 通道1结束泄漏值
db_write_real(12, VD12, 1.2)

VD28 = bytearray(4) # 通道1实时泄漏值
db_write_real(28, VD28, 3.4)

# 通道结果
VB50 = bytearray([1])
client.db_write(1, 50, VB50)

# 红箱子投入
VB54 = bytearray([1])
client.db_write(1, 54, VB54)

# 数据库存储
VW102 = bytearray(2)
db_write_int(102, VW102, 1)

# 产品名称
VB120 = bytearray('hello', encoding='utf8')
client.db_write(1, 120, VB120)

# 模拟一个数据
VD130 = bytearray(4) # 泄露值
db_write_real(130, VD130, 123.456)
VW146 = bytearray(b'OK') # 判断结果
client.db_write(1, 146, VW146)
VW148 = bytearray([1]) # 通道号
client.db_write(1, 148, VW148)


# 报警查看M20开始的
M20 = bytearray(3) # 3个字节
util.set_bool(M20, 0, 0, True) # 急停按下
client.mb_write(20, len(M20), M20)

# 气密参数
VW900 = bytearray(50) # 气密1的所有参数都在这里边
util.set_int(VW900, 0, 10) # 充气时间
util.set_int(VW900, 2, 20) # 保压时间
util.set_int(VW900, 4, 40) # 检测时间
util.set_int(VW900, 8, 80) # 测后排气
util.set_real(VW900, 10, 100.0) # 设定压力
util.set_real(VW900, 14, 140.0)
util.set_real(VW900, 18, 180.0)
util.set_real(VW900, 22, 220.0)
util.set_real(VW900, 26, 260.0)
util.set_real(VW900, 30, 300.0)
util.set_real(VW900, 34, 340.0)
util.set_real(VW900, 38, 380.0)
client.db_write(1, 900, VW900)


def event_do(event):
    print(event)


server.set_events_callback(event_do) # 这个没有生效

# Read it back
# data = client.db_read(1, 0, 4)
# print(f"Read back: {list(data)}")  # [1, 2, 3, 4]
print('启动')
# 等待输入
while True:
    cmd=input()
    if cmd == 'q':
        break

# Clean up
client.disconnect()
server.stop()

```
