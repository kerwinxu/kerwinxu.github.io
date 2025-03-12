---
title: "WPF/WinForm 如何生成单文件的EXE"
date: "2024-11-03"
categories: 
  - "c"
---

# 调试信息的嵌入

pdb文件的嵌入

项目属性/生成/高级/调试信息，完全改成嵌入。

 

# exe.config 文件的嵌入

只需要将解决方案下的App.config文件属性中，生成操作设置成【嵌入的资源】，就可以了

 

# dll的嵌入

过Costura.Fody这个Dll去帮助实现，这个可以nuget安装。

 

# 第三方xml的隐藏

XML文件的隐藏，需要在项目的 .csproj文件中加入元素节点AllowedReferenceRelatedFileExtensions。具体如下：

```
<AllowedReferenceRelatedFileExtensions>.allowedextension</AllowedReferenceRelatedFileExtensions>
```

比如我这里将debug改成隐藏的

```
<PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|AnyCPU' ">
    <PlatformTarget>AnyCPU</PlatformTarget>
    <DebugSymbols>true</DebugSymbols>
    <DebugType>full</DebugType>
    <Optimize>false</Optimize>
    <OutputPath>bin\Debug\</OutputPath>
    <DefineConstants>DEBUG;TRACE</DefineConstants>
    <ErrorReport>prompt</ErrorReport>
    <WarningLevel>4</WarningLevel>
  <AllowedReferenceRelatedFileExtensions>.allowedextension</AllowedReferenceRelatedFileExtensions> 
  </PropertyGroup>
```
