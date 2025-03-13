---
lang: zh
author: Kerwin
layout: post
categories: ["编程", "c#"]
title:  ef6自定义函数解决sqlite的utf8搜索字符串问题
date:   2024-11-23
excerpt: ef6自定义函数解决sqlite的utf8搜索字符串问题
tags: [c#, ef6, sqlite, utf8]
--- 

sqlite只支持utf8字符编码，然后我们插入的数据，很多都是gbk编码，这样会造成搜索字符串的时候，压根不能得到期望的预期，两种解决方式，一种是一开始插入数据的时候，全部转成UTF8编码，而另一种是自定义函数。  
因为我用的是ef6，是orm，然后数据是字符串，背后做了一堆麻烦的东西，然后，sqlite的驱动对于编码是有问题的，反正真正执行搜索的时候，编码不一致，得不到期望的结果。  

首先自定义函数，这个函数的作用是自己做一个包含判断，

```c#
[SQLiteFunction(Name = "ContainsCn", FuncType = FunctionType.Scalar)]
public class FunctionContainsCn:SQLiteFunction
{
    public override object Invoke(object[] args)
    {
        object arg1 = args[0];
        object arg2 = args[1];
        if(arg1 == null || arg2 == null ) { return false; }
        var s1 = arg1.ToString();
        var s2 = arg2.ToString();
        return s1.Contains(s2);
        return base.Invoke(args);
    }

}

```

然后还要注册

```
SQLiteFunction.RegisterFunction(typeof(FunctionContainsCn)); // 注册自定义函数
```

到这里，已经可以在sql语句中使用这个FunctionContainsCn了。但如果想在ef6中操作，那么得添加如下的

```
public class EFDbFunctions
{
    /// <summary>
    /// 解决Sqlite中的CharIndex判断中文的bug，使用此自定义函数替换
    /// </summary>
    /// <param name="find"></param>
    /// <param name="original"></param>
    /// <returns></returns>
    [DbFunctionAttribute("CodeFirstDatabaseSchema", "ContainsCn")]
    public static bool ContainsCn(string original, string find)
    {
        throw new NotSupportedException();


        //throw new NotSupportedException();

    }
}

internal class MyDbContext: DbContext
 {
     public MyDbContext() : base("mydb")
     {

     }

     public DbSet<TableModel> TableModels { get; set; }

     /// <summary>
     /// 在这里边注册自定义函数，
     /// </summary>
     /// <param name="modelBuilder"></param>
     protected override void OnModelCreating(DbModelBuilder modelBuilder)
     {
         base.OnModelCreating(modelBuilder);
         modelBuilder.Conventions.Add(new FunctionsConvention("dbo", typeof(EFDbFunctions)));
     }

 }

```

使用的时候这样子使用,可以看到已经可以在linq中直接用这个函数，且会对应到sql语句，前面的注册，是将这个函数注册到sql。

```
var v1 = dbContext.TableModels.Where(x => EFDbFunctions.ContainsCn(x.Text1, "乐速")).ToArray().Length;
```
