---
title: "ConEmu之类的msys2上直接用mingw64编译环境"
date: "2019-03-01"
categories: 
  - "c-计算机"
---

原先配置：

set MSYS2\_PATH\_TYPE=inherit & set CHERE\_INVOKING=1 & set "PATH=%ConEmuDrive%\\msys64\\usr\\bin;%PATH%" & %ConEmuBaseDirShort%\\conemu-msys2-64.exe -new\_console:p %ConEmuDrive%\\msys64\\usr\\bin\\bash.exe --login -i -new\_console:C:"%ConEmuDrive%\\msys64\\msys2.ico"

 

只要加上红色的部分就可以了

set MSYS2\_PATH\_TYPE=inherit & set MSYSTEM=MINGW64 & set CHERE\_INVOKING=1 & set "PATH=%ConEmuDrive%\\msys64\\usr\\bin;%PATH%" & %ConEmuBaseDirShort%\\conemu-msys2-64.exe -new\_console:p %ConEmuDrive%\\msys64\\usr\\bin\\bash.exe --login -i -new\_console:C:"%ConEmuDrive%\\msys64\\msys2.ico"
