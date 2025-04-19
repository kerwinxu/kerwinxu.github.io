---
layout: post
title:  TorchSocket的记录
date:   2025-4-19 13:35:00 +0800
categories: ["c#", "网络"]
project: false
excerpt: TorchSocket的记录
lang: zh
published: true
tag:
- c#
- 网络
---

用TorchSocket可以将数据收取，数据解析分离

# 服务器  
```c#
var service = new TcpService();
service.Connecting = (client, e) => { return EasyTask.CompletedTask; };//有客户端正在连接
service.Connected = (client, e) => { return EasyTask.CompletedTask; };//有客户端成功连接
service.Closing = (client, e) => { return EasyTask.CompletedTask; };//有客户端正在断开连接，只有当主动断开时才有效。
service.Closed = (client, e) => { return EasyTask.CompletedTask; };//有客户端断开连接
service.Received = async (client, e) =>
{
    //从客户端收到信息
    var mes = e.ByteBlock.Span.ToString(Encoding.UTF8);
    client.Logger.Info($"已从{client.Id}接收到信息：{mes}");
};

await service.SetupAsync(new TouchSocketConfig()//载入配置
     .SetListenIPHosts("tcp://127.0.0.1:7789", 7790)//可以同时监听两个地址
     .ConfigureContainer(a =>//容器的配置顺序应该在最前面
     {
         a.AddConsoleLogger();//添加一个控制台日志注入（注意：在maui中控制台日志不可用）
     })
     .ConfigurePlugins(a =>
     {
         //a.Add();//此处可以添加插件
     }));

await service.StartAsync();//启动
```

# 客户端
```c#
var tcpClient = new TcpClient();
tcpClient.Connecting = (client, e) => { return EasyTask.CompletedTask; };//即将连接到服务器，此时已经创建socket，但是还未建立tcp
tcpClient.Connected = (client, e) => { return EasyTask.CompletedTask; };//成功连接到服务器
tcpClient.Closing = (client, e) => { return EasyTask.CompletedTask; };//即将从服务器断开连接。此处仅主动断开才有效。
tcpClient.Closed = (client, e) => { return EasyTask.CompletedTask; };//从服务器断开连接，当连接不成功时不会触发。
tcpClient.Received = (client, e) =>
{
    //从服务器收到信息。但是一般byteBlock和requestInfo会根据适配器呈现不同的值。
    var mes = e.ByteBlock.Span.ToString(Encoding.UTF8);
    tcpClient.Logger.Info($"客户端接收到信息：{mes}");
    return EasyTask.CompletedTask;
};

//载入配置
await tcpClient.SetupAsync(new TouchSocketConfig()
      .SetRemoteIPHost("127.0.0.1:7789")
      .ConfigureContainer(a =>
      {
          a.AddConsoleLogger();//添加一个日志注入
      }));

await tcpClient.ConnectAsync();//调用连接，当连接不成功时，会抛出异常。

Result result = await tcpClient.TryConnectAsync();//或者可以调用TryConnectAsync
if (result.IsSuccess())
{

}

tcpClient.Logger.Info("客户端成功连接");


```

# 适配器

可选2个参数，ByteBlock(字节数组)和IRequestInfo(解析到的对象)，例如：FixedHeaderPackageAdapter，仅投递ByteBlock数据，届时IRequestInfo将为null。而如果是继承的CustomDataHandlingAdapter，则仅投递IRequestInfo，ByteBlock将为null。
内置适配器
    - FixedHeaderPackageAdapter ： 固定包头数据
	- FixedSizePackageAdapter ： 固定长度
	- TerminatorPackageAdapter : 终止因子，比如 new TerminatorPackageAdapter("\r\n")
	- PeriodPackageAdapter ： 周期数据
	- JsonPackageAdapter ： json格式

# 自定义适配器
```c#
internal class MyCustomDataHandlingAdapter : CustomDataHandlingAdapter<MyRequestInfo>
{
    /// <summary>
    /// 筛选解析数据。实例化的TRequest会一直保存，直至解析成功，或手动清除。
    /// <para>当不满足解析条件时，请返回<see cref="FilterResult.Cache"/>，此时会保存<see cref="ByteBlock.CanReadLen"/>的数据</para>
    /// <para>当数据部分异常时，请移动<see cref="ByteBlock.Pos"/>到指定位置，然后返回<see cref="FilterResult.GoOn"/></para>
    /// <para>当完全满足解析条件时，请返回<see cref="FilterResult.Success"/>最后将<see cref="ByteBlock.Pos"/>移至指定位置。</para>
    /// </summary>
    /// <param name="byteBlock">字节块</param>
    /// <param name="beCached">是否为上次遗留对象，当该参数为True时，request也将是上次实例化的对象。</param>
    /// <param name="request">对象。</param>
    /// <param name="tempCapacity">缓存容量指导，指示当需要缓存时，应该申请多大的内存。</param>
    /// <returns></returns>
    protected override FilterResult Filter<TByteBlock>(ref TByteBlock byteBlock, bool beCached, ref MyRequestInfo request, ref int tempCapacity)
    {
        //以下解析思路为一次性解析，不考虑缓存的临时对象。

        if (byteBlock.CanReadLength < 3)
        {
            return FilterResult.Cache;//当头部都无法解析时，直接缓存
        }

        var pos = byteBlock.Position;//记录初始游标位置，防止本次无法解析时，回退游标。

        var myRequestInfo = new MyRequestInfo();

        //此操作实际上有两个作用，
        //1.填充header
        //2.将byteBlock.Pos递增3的长度。
        var header = byteBlock.ReadToSpan(3);//填充header

        //因为第一个字节表示所有长度，而DataType、OrderType已经包含在了header里面。
        //所有只需呀再读取header[0]-2个长度即可。
        var bodyLength = (byte)(header[0] - 2);

        if (bodyLength > byteBlock.CanReadLength)
        {
            //body数据不足。
            byteBlock.Position = pos;//回退游标
            return FilterResult.Cache;
        }
        else
        {
            //此操作实际上有两个作用，
            //1.填充body
            //2.将byteBlock.Pos递增bodyLength的长度。
            var body = byteBlock.ReadToSpan(bodyLength);

            myRequestInfo.DataType = header[1];
            myRequestInfo.OrderType = header[2];
            myRequestInfo.Body = body.ToArray();
            request = myRequestInfo;//赋值ref
            return FilterResult.Success;//返回成功
        }
    }
}

internal class MyRequestInfo : IRequestInfo
{
    /// <summary>
    /// 自定义属性,Body
    /// </summary>
    public byte[] Body { get; internal set; }

    /// <summary>
    /// 自定义属性,DataType
    /// </summary>
    public byte DataType { get; internal set; }

    /// <summary>
    /// 自定义属性,OrderType
    /// </summary>
    public byte OrderType { get; internal set; }
}

```

使用
```c#
private static async Task<TcpClient> CreateClient()
{
    var client = new TcpClient();
    //载入配置
    await client.SetupAsync(new TouchSocketConfig()
         .SetRemoteIPHost("127.0.0.1:7789")
         .SetTcpDataHandlingAdapter(() => new MyCustomDataHandlingAdapter())
         .ConfigureContainer(a =>
         {
             a.AddConsoleLogger();//添加一个日志注入
         }));

    await client.ConnectAsync();//调用连接，当连接不成功时，会抛出异常。
    client.Logger.Info("客户端成功连接");
    return client;
}

private static async Task<TcpService> CreateService()
{
    var service = new TcpService();
    service.Received = (client, e) =>
    {
        //从客户端收到信息

        if (e.RequestInfo is MyRequestInfo myRequest)
        {
            client.Logger.Info($"已从{client.Id}接收到：DataType={myRequest.DataType},OrderType={myRequest.OrderType},消息={Encoding.UTF8.GetString(myRequest.Body)}");
        }
        return Task.CompletedTask;
    };

    await service.SetupAsync(new TouchSocketConfig()//载入配置
         .SetListenIPHosts("tcp://127.0.0.1:7789", 7790)//同时监听两个地址
         .SetTcpDataHandlingAdapter(() => new MyCustomDataHandlingAdapter())
         .ConfigureContainer(a =>
         {
             a.AddConsoleLogger();//添加一个控制台日志注入（注意：在maui中控制台日志不可用）
         })
         .ConfigurePlugins(a =>
         {
             //a.Add();//此处可以添加插件
         }));
    await service.StartAsync();//启动
    service.Logger.Info("服务器已启动");
    return service;
}
```

原理，收到数据后会在缓冲中判断是否需要的对象，然后投递，最后Received接收。
![自定义适配器逻辑](/assets/image/default/customdatahandlingadapter.png)





# 引用
    - [TorchSocket官网](https://touchsocket.net)