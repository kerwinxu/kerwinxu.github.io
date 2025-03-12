---
layout: post
title: "net中Obfuscar进行代码混淆"
date: "2022-12-23"
categories: 
  - "c"
---

# 安装

在nuget中安装

 

# 配置

```
<?xml version='1.0'?>
<Obfuscator>
  <!-- 输入的工作路径，采用如约定的 Windows 下的路径表示法，如以下表示当前工作路径 -->
  <!-- 推荐使用当前工作路径，因为 DLL 的混淆过程，需要找到 DLL 的所有依赖。刚好当前工作路径下，基本都能满足条件 -->
  <Var name="InPath" value="." />
  <!-- 混淆之后的输出路径，如下面代码，设置为当前工作路径下的 Obfuscar 文件夹 -->
  <!-- 混淆完成之后的新 DLL 将会存放在此文件夹里 -->
  <Var name="OutPath" value=".\Obfuscar" />
  <!-- 以下的都是细节的配置，配置如何进行混淆 -->

  <!-- 使用 KeepPublicApi 配置是否保持公开的 API 不进行混淆签名，如公开的类型公开的方法等等，就不进行混淆签名了 -->
  <!-- 语法的写法就是 name 表示某个开关，而 value 表示值 -->
  <!-- 对于大部分的库来说，设置公开的 API 不进行混淆是符合预期的 -->
  <Var name="KeepPublicApi" value="false" />
  <!-- 设置 HidePrivateApi 为 true 表示，对于私有的 API 进行隐藏，隐藏也就是混淆的意思 -->
  <!-- 可以通过后续的配置，设置混淆的方式，例如使用 ABC 字符替换，或者使用不可见的 Unicode 代替 -->
  <Var name="HidePrivateApi" value="true" />
  <!-- 设置 HideStrings 为 true 可以设置是否将使用的字符串进行二次编码 -->
  <!-- 由于进行二次编码，将会稍微伤一点点性能，二次编码需要在运行的时候，调用 Encoding 进行转换为字符串 -->
  <Var name="HideStrings" value="true" />
  <!-- 设置 UseUnicodeNames 为 true 表示使用不可见的 Unicode 字符代替原有的命名，通过此配置，可以让反编译看到的类和命名空间和成员等内容都是不可见的字符 -->
  <Var name="UseUnicodeNames" value="true" />
  <!-- 是否复用命名，设置为 true 的时候，将会复用命名，如在不同的类型里面，对字段进行混淆，那么不同的类型的字段可以是重名的 -->
  <!-- 设置为 false 的时候，全局将不会有重复的命名 -->
  <Var name="ReuseNames" value="true" />
  <!-- 配置是否需要重命名字段，默认配置了 HidePrivateApi 为 true 将都会打开重命名字段，因此这个配置的存在只是用来配置为 false 表示不要重命名字段 -->
  <Var name="RenameFields" value="true" />
  <!-- 是否需要重新生成调试信息，生成 PDB 符号文件 -->
  <Var name="RegenerateDebugInfo" value="true" />

  <!-- 需要进行混淆的程序集，可以传入很多个，如传入一排排 -->
  <!-- <Module file="$(InPath)\Lib1.dll" /> -->
  <!-- <Module file="$(InPath)\Lib2.dll" /> -->
  <Module file="$(InPath)\HeenerholiCeleehano.dll" />

  <!-- 程序集的引用加载路径，对于 dotnet 6 应用，特别是 WPF 或 WinForms 项目，是需要特别指定引用加载路径的 -->
  <!-- 这里有一个小的需要敲黑板的知识点，应该让 Microsoft.WindowsDesktop.App 放在 Microsoft.NETCore.App 之前 -->
  <!-- 对于部分项目，如果没有找到如下顺序，将会在混淆过程中，将某些程序集解析为旧版本，从而失败 -->
  <AssemblySearchPath path="C:\Program Files\dotnet\shared\Microsoft.WindowsDesktop.App\6.0.1\" />
  <AssemblySearchPath path="C:\Program Files\dotnet\shared\Microsoft.NETCore.App\6.0.1\" />
</Obfuscator>
```

| Name | Description |
| --- | --- |
| InPath | Directory containing the input assemblies, such as `c:\\in`. |
| OutPath | Directory to contain the obfuscated assemblies, such as `c:\\out`. |
| LogFile | Obfuscation log file path (mapping.txt). |
| XmlMapping | Whether the log file should be of XML format. |
| KeyFile | Key file path, such as `c:\folder\key.pfx`. |
| KeyContainer | Key container name. |
| RegenerateDebugInfo | Whether to generate debug symbols for obfuscated assemblies. |
| MarkedOnly | Whether to only obfuscate marked items. All items are obfuscated when set to `false`. |
| RenameProperties | Whether to rename properties. |
| RenameEvents | Whether to rename events. |
| RenameFields | Whether to rename fields. |
| KeepPublicApi | Whether to exclude public types and type members from obfuscation. |
| HidePrivateApi | Whether to include private types and type members from obfuscation. |
| ReuseNames | Whether to reuse obfuscated names. |
| UseUnicodeNames | Whether to use Unicode characters as obfuscated names. |
| UseKoreanNames | Whether to use Korean characters as obfuscated names. |
| HideStrings | Whether to hide strings. |
| OptimizeMethods | Whether to optimize methods. |
| SuppressIldasm | Whether to include an attribute for ILDASM to indicate that assemblies are obfuscated. |
| AnalyzeXaml | Whether to analyze XAML related metadata for obfuscation. |

## 如下是我的配置

```
<?xml version='1.0'?>
<Obfuscator>
  <Var name="InPath" value="." />
  <Var name="OutPath" value=".\Obfuscar" />
  <Var name="KeepPublicApi" value="false" />
  <Var name="HidePrivateApi" value="true" />
  <Var name="HideStrings" value="true" />
  <Var name="UseUnicodeNames" value="true" />
  <Var name="RenameProperties" value="true"/>
  <Var name="RenameEvents" value="true" />
  <Var name="ReuseNames" value="true" />
  <Var name="RenameFields" value="true" />
  <Var name="ReuseNames" value="true" />
  <Var name="OptimizeMethods" value="true"/>
  <Var name="RegenerateDebugInfo" value="false" />
  <Module file="$(InPath)\HeenerholiCeleehano.dll" />

</Obfuscator>
```

 

# 运行

在项目文件夹中添加配置文件，然后设置成永远拷贝文件夹。

在编译后事件中设置这个。

```
cd $(OutDir)
"$(Obfuscar)" obfuscar.xml
```
