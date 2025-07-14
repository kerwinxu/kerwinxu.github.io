---
layout: post
title: "手写c#的modbus-rtu查询"
date: "2025-07-08"
categories: ["计算机语言", "c#"]
math: true
---

先精简的版本，以后再复杂吧。

```csharp

  /// <summary>
  /// CRC校验，参数data为byte数组
  /// </summary>
  /// <param name="data">校验数据，字节数组</param>
  /// <returns>字节0是高8位，字节1是低8位</returns>
  private byte[] CRCCalc(byte[] data)
  {
      int crc = 0xffff;
      for (int i = 0; i < data.Length; i++)
      {
          crc ^= data[i];
          for (int j = 0; j < 8; j++)
          {
              int temp = crc & 1;
              crc >>= 1;
              if (temp == 1)
              {
                  crc ^= 0xa001;
              }
          }
      }
      byte[] crc16 = new byte[2];
      crc16[1] = (byte)((crc >> 8) & 0xff);
      crc16[0] = (byte)(crc & 0xff);
      return crc16;
  }


  private ushort[] ReadInputRegisters(SerialPort serialPort,  byte slaveId, ushort address, ushort length, int time_out)
  {
      // 发送的字节
      List<byte> send_buf = new List<byte>();
      send_buf.Add(slaveId); // 先添加
      send_buf.Add(4);       // 输入寄存器
      send_buf.AddRange(modbus_short_to_bytes(address));
      send_buf.AddRange(modbus_short_to_bytes(length));
      var _crc = CRCCalc(send_buf.ToArray()); 
      send_buf.AddRange(_crc);
      // 这里进行发送
      serialPort.Write(send_buf.ToArray(), 0, send_buf.Count);
      // 然后等待接收
      ushort[] result = new ushort[length];   // 准备接收这么多
      DateTime now = DateTime.Now;
      int expect_count = 5 + length * 2;
      List<byte>recv_buf = new List<byte>();
      while (expect_count > recv_buf.Count && (DateTime.Now - now).TotalMilliseconds < time_out) {
          // 这里进行读取
          if (serialPort.BytesToRead > 0) { 
              byte[] tmp =new byte[serialPort.BytesToRead];
              serialPort.Read(tmp, 0, tmp.Length);
              recv_buf.AddRange(tmp);
          }
          Thread.Sleep(1);
      }
      if (expect_count == recv_buf.Count)
      {
          // 每一个都是从高位读取的
          int _start = 3; // 从序号3开始读取
          for (global::System.Int32 i = 0; i < length; i++)
          {
              var data2 = recv_buf.Skip(_start + i * 2).Take(2).ToArray();
              if(BitConverter.IsLittleEndian) Array.Reverse(data2);
              result[i] = BitConverter.ToUInt16(data2, 0);
          }

      }
      
      return result;

  }


```