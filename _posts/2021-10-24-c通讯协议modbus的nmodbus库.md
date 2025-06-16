---
layout: post
title: "通讯协议ModBus的c#NModbus库"
date: "2021-10-24"
categories: ["计算机语言", "c"]
---

官网 ： [https://github.com/NModbus/NModbus](https://github.com/NModbus/NModbus)

# Tcp

封装ModbusTcp类

```
public class ModbusTCP
 {
     private ModbusFactory modbusFactory;
     private IModbusMaster master;
     private TcpClient tcpClient;

     public string IPAdress { get; set; }
     public int Port { get; set; }

     public bool Connected
     {
         get => tcpClient.Connected;
     }

     public ModbusTCP(string ip, int port)
     {
         IPAdress = ip;
         Port = port;

         modbusFactory = new ModbusFactory();
         tcpClient = new TcpClient(IPAdress, Port);
         master = modbusFactory.CreateMaster(tcpClient);
         master.Transport.ReadTimeout = 2000;
         master.Transport.Retries = 10;
     }


     public bool[] ReadCoils(byte slaveAddress, ushort startAddress, ushort num)
     {
         return master.ReadCoils(slaveAddress, startAddress, num);
     }

     public bool[] ReadInputs(byte slaveAddress, ushort startAddress, ushort num)
     {
         return master.ReadInputs(slaveAddress, startAddress, num);
     }

     public ushort[] ReadHoldingRegisters(byte slaveAddress, ushort startAddress, ushort num)
     {
         return master.ReadHoldingRegisters(slaveAddress, startAddress, num);
     }

     public ushort[] ReadInputRegisters(byte slaveAddress, ushort startAddress, ushort num)
     {
         return master.ReadInputRegisters(slaveAddress, startAddress, num);
     }

     public void WriteSingleCoil(byte slaveAddress, ushort startAddress, bool value)
     {
         master.WriteSingleCoil(slaveAddress, startAddress, value);
     }

     public void WriteSingleRegister(byte slaveAddress, ushort startAddress, ushort value)
     {
         master.WriteSingleRegister(slaveAddress, startAddress, value);
     }

     public void WriteMultipleCoils(byte slaveAddress, ushort startAddress, bool[] value)
     {
         master.WriteMultipleCoils(slaveAddress, startAddress, value);
     }

     public void WriteMultipleRegisters(byte slaveAddress, ushort startAddress, ushort[] value)
     {
         master.WriteMultipleRegisters(slaveAddress, startAddress, value);
     }

 }
```

读取测试

```
private void ReadExecute()
       {
           try
           {
               if (VariableType == "real")
               {
                   ushort[] buff = modbus.ReadHoldingRegisters(SlaveID, ReadAddress, 2);
                   float value = MODBUS.GetReal(buff, 0);
                   ReadValue = value.ToString();
               }
               else if(VariableType == "string")
               {
                   ushort[] buff = modbus.ReadHoldingRegisters(SlaveID, ReadAddress, 10);
                   ReadValue = MODBUS.GetString(buff, 0, 10); 
               }
               else if(VariableType == "Int16")
               {
                   ushort[] buff = modbus.ReadHoldingRegisters(SlaveID, ReadAddress, 1);
                   short value = MODBUS.GetShort(buff, 0);
                   ReadValue = value.ToString();
               }
           }
           catch (Exception ex)
           {
               Msg.Info(ex.Message);
           }
       }
```

写入测试

先转换类型

```
public class MODBUS
   {
       /// <summary>
       /// 赋值string
       /// </summary>
       /// <param name="src"></param>
       /// <param name="start"></param>
       /// <param name="value"></param>
       /// <returns></returns>
       public static void SetString(ushort[] src, int start, string value)
       {
           byte[] bytesTemp = Encoding.UTF8.GetBytes(value);
           ushort[] dest = Bytes2Ushorts(bytesTemp);
           dest.CopyTo(src, start);
       }

       /// <summary>
       /// 获取string
       /// </summary>
       /// <param name="src"></param>
       /// <param name="start"></param>
       /// <param name="len"></param>
       /// <returns></returns>
       public static string GetString(ushort[] src, int start, int len)
       {
           ushort[] temp = new ushort[len];
           for (int i = 0; i < len; i++)
           {
               temp[i] = src[i + start];
           }
           byte[] bytesTemp = Ushorts2Bytes(temp);
           string res = Encoding.UTF8.GetString(bytesTemp).Trim(new char[] { '\0' });
           return res;
       }

       /// <summary>
       /// 赋值Real类型数据
       /// </summary>
       /// <param name="src"></param>
       /// <param name="start"></param>
       /// <param name="value"></param>
       public static void SetReal(ushort[] src, int start, float value)
       {
           byte[] bytes = BitConverter.GetBytes(value);

           ushort[] dest = Bytes2Ushorts(bytes);

           dest.CopyTo(src, start);
       }

       /// <summary>
       /// 获取float类型数据
       /// </summary>
       /// <param name="src"></param>
       /// <param name="start"></param>
       /// <returns></returns>
       public static float GetReal(ushort[] src, int start)
       {
           ushort[] temp = new ushort[2];
           for (int i = 0; i < 2; i++)
           {
               temp[i] = src[i + start];
           }
           byte[] bytesTemp = Ushorts2Bytes(temp);
           float res = BitConverter.ToSingle(bytesTemp, 0);
           return res;
       }

       /// <summary>
       /// 赋值Short类型数据
       /// </summary>
       /// <param name="src"></param>
       /// <param name="start"></param>
       /// <param name="value"></param>
       public static void SetShort(ushort[] src, int start, short value)
       {
           byte[] bytes = BitConverter.GetBytes(value);

           ushort[] dest = Bytes2Ushorts(bytes);

           dest.CopyTo(src, start);
       }

       /// <summary>
       /// 获取short类型数据
       /// </summary>
       /// <param name="src"></param>
       /// <param name="start"></param>
       /// <returns></returns>
       public static short GetShort(ushort[] src, int start)
       {
           ushort[] temp = new ushort[1];
           temp[0] = src[start];
           byte[] bytesTemp = Ushorts2Bytes(temp);
           short res = BitConverter.ToInt16(bytesTemp, 0);
           return res;
       }


       public static bool[] GetBools(ushort[] src, int start, int num)
       {
           ushort[] temp = new ushort[num];
           for (int i = start; i < start + num; i++)
           {
               temp[i] = src[i + start];
           }
           byte[] bytes = Ushorts2Bytes(temp);

           bool[] res = Bytes2Bools(bytes);

           return res;
       }

       private static bool[] Bytes2Bools(byte[] b)
       {
           bool[] array = new bool[8*b.Length];

           for (int i = 0; i < b.Length; i++)
           {
               for (int j = 0; j < 8; j++)
               {
                   array[i * 8 + j] = (b[i] & 1) == 1;//判定byte的最后一位是否为1，若为1，则是true；否则是false
                   b[i] = (byte)(b[i] >> 1);//将byte右移一位
               }
           }
           return array;
       }

       private static byte Bools2Byte(bool[] array)
       {
           if (array != null && array.Length > 0)
           {
               byte b = 0;
               for (int i = 0; i < 8; i++)
               {
                   if (array[i])
                   {
                       byte nn = (byte)(1 << i);//左移一位，相当于×2
                       b += nn;
                   }
               }
               return b;
           }
           return 0;
       }

       private static ushort[] Bytes2Ushorts(byte[] src, bool reverse = false)
       {
           int len = src.Length;

           byte[] srcPlus = new byte[len + 1];
           src.CopyTo(srcPlus, 0);
           int count = len >> 1;

           if (len % 2 != 0)
           {
               count += 1;
           }

           ushort[] dest = new ushort[count];
           if(reverse)
           {
               for (int i = 0; i < count; i++)
               {
                   dest[i] = (ushort)(srcPlus[i * 2] << 8 | srcPlus[2 * i + 1] & 0xff);
               }
           }
           else
           {
               for (int i = 0; i < count; i++)
               {
                   dest[i] = (ushort)(srcPlus[i * 2] & 0xff | srcPlus[2 * i + 1] << 8 );
               }
           }
        
           return dest;
       }

       private static byte[] Ushorts2Bytes(ushort[] src, bool reverse = false)
       {

           int count = src.Length;
           byte[] dest = new byte[count << 1];
           if(reverse)
           {
               for (int i = 0; i < count; i++)
               {
                   dest[i * 2] = (byte)(src[i] >> 8);
                   dest[i * 2 + 1] = (byte)(src[i] >> 0);
               }
           }
           else
           {
               for (int i = 0; i < count; i++)
               {
                   dest[i * 2] = (byte)(src[i] >> 0);
                   dest[i * 2 + 1] = (byte)(src[i] >> 8);
               }
           }
           return dest;
       }
   }
```

写入

```
private void WriteExecute()
        {
            try
            {
                if(VariableType == "real")
                {
                    ushort[] buff = new ushort[2];
                    float value = float.Parse(WriteValue);
                    MODBUS.SetReal(buff, 0, value);
                    modbus.WriteMultipleRegisters(SlaveID, WriteAddress, buff);
                }
                else if(VariableType == "string")
                {
                    ushort[] buff = new ushort[10];
                    MODBUS.SetString(buff, 0, WriteValue);
                    modbus.WriteMultipleRegisters(SlaveID, WriteAddress, buff);
                }
                else if(VariableType == "Int16")
                {
                    ushort[] buff = new ushort[1];
                    short value = short.Parse(WriteValue);
                    MODBUS.SetShort(buff, 0, value);
                    modbus.WriteMultipleRegisters(SlaveID, WriteAddress, buff);
                }
            }
            catch (Exception ex)
            {
                Msg.Info(ex.Message);
            }
        }
```

 

# 示例2

```
private static void Main(string[] args)
        {
            try
            {
                ModbusSerialRtuMasterWriteRegisters();
                ModbusTcpMasterReadInputs();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
 
            Console.WriteLine("Press any key to continue...");
            Console.ReadKey();
        }
 
        /// <summary>
        /// Simple Modbus serial RTU master write holding registers example.
        /// </summary>
        public static void ModbusSerialRtuMasterWriteRegisters()
        {
            using (SerialPort port = new SerialPort("COM3"))
            {
                // configure serial port
                port.BaudRate = 9600;
                port.DataBits = 8;
                port.Parity = Parity.None;
                port.StopBits = StopBits.One;
                port.Open();
 
                var factory = new ModbusFactory();
                IModbusMaster master = factory.CreateRtuMaster(port);
 
                byte slaveId = 1;
                ushort startAddress = 100;
                ushort[] registers = new ushort[] { 1, 2, 3 };
 
                // write three registers
                master.WriteMultipleRegisters(slaveId, startAddress, registers);
            }
        }
 
        /// <summary>
        ///     Simple Modbus TCP master read inputs example.
        /// </summary>
        public static void ModbusTcpMasterReadInputs()
        {
            using (TcpClient client = new TcpClient("127.0.0.1", 502))
            {
                var factory = new ModbusFactory();
                IModbusMaster master = factory.CreateMaster(client);
 
                // read five input values
                ushort startAddress = 100;
                ushort numInputs = 5;
                bool[] inputs = master.ReadInputs(0, startAddress, numInputs);
 
                for (int i = 0; i < numInputs; i++)
                {
                    Console.WriteLine($"Input {(startAddress + i)}={(inputs[i] ? 1 : 0)}");
                }
            }
 
            // output:
            // Input 100=0
            // Input 101=0
            // Input 102=0
            // Input 103=0
            // Input 104=0
        }
```
