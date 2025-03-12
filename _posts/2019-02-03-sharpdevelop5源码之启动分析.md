---
title: "SharpDevelop5源码之启动分析"
date: "2019-02-03"
categories: 
  - "c"
---

# 启动函数

启动函数都是从 public static void Main(string\[\] args) 开始的，找到 src\\Main\\SharpDevelop\\Startup\\SharpDevelopMain.cs ，里边有启动函数

## 启动函数Main功能

这个启动函数只是做了2个功能

1. commandLineArgs = args; // Needed by UseExceptionBox ，保存命令行参数。
2. 调用Run（）函数，调用前会判断UseExceptionBox，是否显示异常窗体的，如果是，当有异常的时候就显示异常窗体。

## Run() 函数

功能

1. 将命令行参数给SplashScreenForm。SplashScreenForm.SetCommandLineArgs(commandLineArgs);
2. SplashScreenForm，判断这个参数里是否有不显示nologo参数，如果有，就不显示SplashScreenForm
3. 调用检查环境变量CheckEnvironment函数
    1. 检查是否是net4.5版本的
    2. Work around a WPF issue when %WINDIR% is set to an incorrect path
4. 调用RunApplication 函数
    1. 不管是否出现异常，且有SplashScreenForm情况下，都销毁SplashScreenForm窗体。

## RunApplication 函数

功能

1. StartupSettings startup = new StartupSettings(); 字面意思是启动设置。这里我忽略调试模式啦
    1. 设置如下信息
        1. startup.ApplicationRootPath = Path.Combine(Path.GetDirectoryName(exe.Location), ".."); 程序根目录
        2. startup.AllowUserAddIns = true;允许使用用户插件
        3. startup.ConfigDirectory ，config目录
        4. startup.DomPersistencePath
        5. startup.AddAddInsFromDirectory(Path.Combine(startup.ApplicationRootPath, "AddIns"));添加插件目录，这里表示程序运行目录下的AddIns目录。
        6. SplashScreenForm.GetParameterList，这里边的参数如果有addindir开头的，那么也当作是插件目录吧。
2. SharpDevelopHost host = new SharpDevelopHost(AppDomain.CurrentDomain, startup);，根据启动设置和当前程序为参数，构造一个host。
    1. host.BeforeRunWorkbench += delegate 运行工作台前的事件。
    2. host.RunWorkbench(workbenchSettings);，在设置工作台相关参数后，启动工作台。
3. string\[\] fileList = SplashScreenForm.GetRequestedFileList();，要打开的文件列表。
4. WorkbenchSettings workbenchSettings = new WorkbenchSettings(); 工作台设置。
    1. 功能
        1. workbenchSettings.InitialFileList.Add(fileList\[i\]); ，工作台要添加要打开的文件。

# 各种类

## SharpDevelopHost类

### 属性

- internal static Assembly SdaAssembly
- public ReadOnlyCollection<Document> OpenDocuments
- public bool WorkbenchVisible
- public AppDomain AppDomain
- public System.ComponentModel.ISynchronizeInvoke InvokeTarget

### 方法

- 构造函数
    - - public SharpDevelopHost(StartupSettings startup)
            - Create a new AppDomain to host SharpDevelop.
        - public SharpDevelopHost(AppDomain appDomain, StartupSettings startup)
            - Host SharpDevelop in the existing AppDomain.
    - 功能
        - 都是设置如下2个参数的
            - AppDomain appDomain; 程序域
            - CallHelper helper;
- public void RunWorkbench(WorkbenchSettings settings) ，根据工作台设置启动工作台。
- public bool CloseWorkbench(bool force)
- public Document OpenDocument(string fileName)
- public void OpenProject(string fileName)
- public bool IsSolutionOrProject(string fileName)
- public void UnloadDomain()
- public T CreateInstanceInTargetDomain<T>(params object\[\] arguments) where T : MarshalByRefObject
- public object CreateInstanceInTargetDomain(Type type, params object\[\] arguments)
