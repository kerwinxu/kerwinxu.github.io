---
layout: post
title: "powershell中的Cmdlet的参数输入输出"
date: "2019-08-30"
categories: 
  - "dos_powdershell"
---

我看到简单的代码，我原先以为Cmdlet的输入是一个函数，参数是函数的输入呢，但现在看到他是另一种实现，比如这个参数要如下声明

```
[Cmdlet(VerbsCommon.Get, "proc")]
public class GetProcCommand: Cmdlet
{
    /// <summary>
    /// Specify the cmdlet Name parameter.
    /// </summary>
    [Parameter(Position = 0)]
    [ValidateNotNullOrEmpty]
    public string[] Name
    {
        get { return processNames; }
        set { processNames = value; }
    }
    private string[] processNames;
    #endregion Parameters
}
```

外部来的参数全部保留到这里了。

然后有个重写输入的处理方法

```
protected override void ProcessRecord()
{
  // If no process names are passed to the cmdlet, get all processes.
  if (processNames == null)
  {
    // Write the processes to the pipeline making them available
    // to the next cmdlet. The second argument of this call tells
    // PowerShell to enumerate the array, and send one process at a
    // time to the pipeline.
    WriteObject(Process.GetProcesses(), true);
  }
  else
  {
    // If process names are passed to the cmdlet, get and write
    // the associated processes.
    foreach (string name in processNames)
    {
      WriteObject(Process.GetProcessesByName(name), true);
    }
  }
}
```

这李会看到，他调用保存属性值的私有变量来判断输入的。
