---
layout: post
title: "win10-vscode之gcc编写gdb调试"
date: "2019-12-31"
categories: 
  - "c-计算机"
---

# 需要安装

- c/c++ ，微软出的，
- remote wsl ，这个是远程wsl的，其实可以不用。
- glibc-2.27.tar ，或者其他版本，下载解压，放在D:\\build\\glibc-OTsEL5目录，你放在相应的目录吧
    - 如果没有这个，单步调试的时候会出现can't open file  \\build\\glibc-OTsEL5... 之类的，你看看这个是在哪个目录，就解压在哪个目录吧。
        - 这个就是类似printf 函数的目录，

# vscode项目配置

## tasks.json 是用在launch前执行的任务

```
// tasks.json
{
    // https://code.visualstudio.com/docs/editor/tasks
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build",  // 任务的名字叫Build，注意是大小写区分的，等会在launch中调用这个名字
            "type": "shell",  // 任务执行的是shell命令，也可以是
            "command": "g++", // 命令是g++，这里也可以用make命令。
            "args": [
                "'-Wall'",
                "'-std=c++17'",  //使用c++17标准编译
                "'${file}'", //当前文件名
                "-o", //对象名，不进行编译优化
                "'${fileBasenameNoExtension}.exe'",  //当前文件名（去掉扩展名）
            ],
          // 所以以上部分，就是在shell中执行（假设文件名为filename.cpp）
          // g++ filename.cpp -o filename.exe
            "group": { 
                "kind": "build",
                "isDefault": true   
                // 任务分组，因为是tasks而不是task，意味着可以连着执行很多任务
                // 在build组的任务们，可以通过在Command Palette(F1) 输入run build task来运行
                // 当然，如果任务分组是test，你就可以用run test task来运行 
            },
            "problemMatcher": [
                "$gcc" // 使用gcc捕获错误
            ],
        }
    ]
}
```

另外wsl中的可以这样用，如下是例子参考。

```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build",
            "type": "shell",
            "command": "wsl gcc -g /mnt/c/works/clearn/test.c -o /mnt/c/works/clearn/test.o",
            "problemMatcher": [],
        }
    ]
}
```

注意这了label的名字应该和preLaunchTask所对应，这个配置文件的意义就是在调试前运行一条命令编译文件。这得益于WSL和windows命令行的互通，你完全可以在Powershell中执行绝大多数linux命令，只需在这之前加上wsl即可，而且这与你子系统的发行版无关。

## launch.json 是读取执行文件

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "C++ Launch",      //这个应该是F1中出现的名字
            "preLaunchTask": "Build",  //在launch之前运行的任务名，这个名字一定要跟tasks.json中的任务名字大小写一致
            "type": "cppdbg",
            "request": "launch",
            "program": "/mnt/c/works/clearn/test.o",//编译完成的文件
            "args": ["-fThreading"],
            "stopAtEntry": false,        //打开后停滞
            "cwd": "/mnt/c/works/clearn",//项目所在目录
            "environment": [],
            "externalConsole": true,     //是否选用外部控制台。
            "internalConsoleOptions": "openOnSessionStart",//调试时跳转到内部调试台
            "preLaunchTask": "build",//编译任务
            "windows": {
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ]
            },
            "pipeTransport": {
                "pipeCwd": "",
                "pipeProgram": "c:\\windows\\sysnative\\bash.exe",//通常不需要修改
                "pipeArgs": ["-c"],
                "debuggerPath": "/usr/bin/gdb"
            },
            "sourceFileMap": {
                "/mnt/c": "C:\\"//地址转换
            }
        }
    ]
}
```

# 单步调试提示找不到文件

在使用单步调试时提示“无法打开...：找不到文件(file:///build/glibc-OTsEL5/glibc-2.27/...”这类提示时，你要做的就是补全glibc-2.27目录下的文件，没有这些文件就VSCode的C/C++插件就无法正常单步调试。你可以直接[下载](http://ftp.gnu.org/gnu/glibc/glibc-2.27.tar.xz)文件并解压到指定的目录，像我的就是在C:/build/glibc-OTsEL5目录。如果版本不对请到[这里](http://ftp.gnu.org/gnu/glibc/)寻找对应版本。

这就是我在d盘建立了一个build目录的原因。

# 一些常用的配置变量

## Predefined variables

The following predefined variables are supported:

- **${workspaceFolder}** - the path of the folder opened in VS Code
- **${workspaceFolderBasename}** - the name of the folder opened in VS Code without any slashes (/)
- **${file}** - the current opened file
- **${relativeFile}** - the current opened file relative to `workspaceFolder`
- **${relativeFileDirname}** - the current opened file's dirname relative to `workspaceFolder`
- **${fileBasename}** - the current opened file's basename
- **${fileBasenameNoExtension}** - the current opened file's basename with no file extension
- **${fileDirname}** - the current opened file's dirname
- **${fileExtname}** - the current opened file's extension
- **${cwd}** - the task runner's current working directory on startup
- **${lineNumber}** - the current selected line number in the active file
- **${selectedText}** - the current selected text in the active file
- **${execPath}** - the path to the running VS Code executable
- **${defaultBuildTask}** - the name of the default build task
