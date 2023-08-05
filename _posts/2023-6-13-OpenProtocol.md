---
lang: zh
author: Kerwin
layout: post
categories: ["编程", "c#"]
title:  OpenProtocol
project: true
image: "/assets/image/openprotocol/openprotocol.png"
date:   2023-6-13
excerpt: 协议数据跟对象之间转换的
tags: [c#]
---
﻿# 摘要
我这个程序是类似ORM，ORM是面向对象与关系数据库之间的匹配的，而这个OpenProtocol是面向对象与通讯的字节流之间的匹配的，是一种序列化技术。  
# Summary 
My program is similar to ORM, ORM is object-oriented and relational database matching, and OpenProtocol is object-oriented matching between communicating byte streams, which is a serialization technology.  

# Demo

```
using Io.Github.KerwinXu.OpenProtocol;
using Io.Github.KerwinXu.OpenProtocol.Attributes;
using Io.Github.KerwinXu.OpenProtocol.Attributes.Checks;
using Io.Github.KerwinXu.OpenProtocol.Attributes.Size;

namespace Demo
{
    class TestClass
    {
        
        // DataItem表示数据项目，0表示这个是字节流的第一项。
        // DataItem represents the data item, and 0 indicates that this is the first item in the byte stream.
        [DataItem(0)]  
        public readonly byte Start = 0xff;

        [DataItem(1)]
        public byte FunCode { get; set; }

        // DefaultSize(大小,是否按照字节计数) ， 这里的0表示没有数据。
        // DefaultSize (size, whether bytes counted) , 0 here means no data.
        // [StaticSizeByOther("FunCode", 1, 1)] :  如果"FunCode"属性的值是1，那么这个数据的大小是1.
        // [StaticSizeByOther("FunCode", 1, 1)]: If the value of the "FunCode" attribute is 1, then the size of the data is 1
        [DefaultSize(0,true)]
        [StaticSizeByOther("FunCode", 1, 1)]
        [DataItem(2)]
        public byte DataLength { get; set; }

        // [VarSizeByOther("FunCode",1, "DataLength",IsByteCount =false)] : 如果属性"FunCode"的值是1，那么属性Data的长度是属性"DataLength"的值，是按照Data的ushort数据类型计数。
        // [VarSizeByOther("FunCode",1, "DataLength",IsByteCount =false)] : If the value of the property "FunCode" is 1, then the length of the property Data is the value of the property "DataLength", which is counted according to the ushort data type of Data.
        [VarSizeByOther("FunCode",1, "DataLength",IsByteCount =false)]
        [DataItem(3)]
        public ushort[]? Data { get; set; }

        // [CheckSum(1,3)] 这个是校验和，1表示从“[DataItem(1)]”开始，3表示到“[DataItem(3)]”结束。
        // [CheckSum(1,3)] This is the checksum, 1 means starting with "[DataItem(1)]" and 3 means ending with "[DataItem(3)]".
        [DataItem(4,true)]
        [CheckSum(1,3)]
        public byte CheckSum { get; set; }

        // 请注意，所有固定的数据都是字段，并且数据类型只支持byte或者byte[]
        //  Note that all fixed data is a field, and the data type only supports byte or byte[]
        [DataItem(5)]
        public readonly byte [] End = { 0x0f, 0xff };

    }

    class Program
    {
        static void Main(string[] args)
        {
            // 
            byte[] datas = { 0xff,0x01, 0x01, 0x01, 0x02, 0xfb, 0x0f, 0xff };
            TestClass testClass = (new BytesSerializer<TestClass>()).Deserialize(datas);
            Console.WriteLine($"funcode:{testClass.FunCode}, DataLength:{testClass.DataLength}, CheckSum:{testClass.CheckSum}");
            //
            var datas2 = (new BytesSerializer<TestClass>()).Serialize(testClass);
            Console.WriteLine($"{Enumerable.SequenceEqual(datas, datas2)}");

        }
    }
}
```

# 下载

[https://www.nuget.org/packages/Io.Github.KerwinXu.OpenProtocol](https://www.nuget.org/packages/Io.Github.KerwinXu.OpenProtocol)  

[https://github.com/kerwinxu/OpenProtocol.git](https://github.com/kerwinxu/OpenProtocol.git)

