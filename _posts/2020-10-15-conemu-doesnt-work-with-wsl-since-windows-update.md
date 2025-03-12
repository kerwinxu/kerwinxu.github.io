---
layout: post
title: "Conemu doesn't work with wsl since windows update"
date: "2020-10-15"
categories: 
  - "dos_powdershell"
---

这个是因为wsl2更改了,所以会造成如下的错误提示:

```
wslbridge error: failed to start backend process
note: backend error output: -v: -c: line 0: unexpected EOF while looking for matching `''
-v: -c: line 1: syntax error: unexpected end of file

ConEmuC: Root process was alive less than 10 sec, ExitCode=0.
Press Enter or Esc to close console...
```

解决方法是:

[https://github.com/Biswa96/wslbridge2/releases](https://github.com/Biswa96/wslbridge2/releases)

Replacing `{WSL::bash}` task's Command with:

```
set "PATH=%ConEmuBaseDirShort%\wsl;%PATH%" & %ConEmuBaseDirShort%\conemu-cyg-64.exe %ConEmuBaseDirShort%\wsl\wslbridge2.exe -cur_console:pm:/mnt -eConEmuBuild -eConEmuPID -eConEmuServerPID -l

```
