---
title: "vscode  Using git on msys2"
date: "2019-10-11"
categories: 
  - "git"
---

As I filed issue ago, vscode can't work with msys2's git. Because git provided on msys2 return `/c/` prefixed-path for rev-parse command.

[#387](https://github.com/microsoft/vscode/issues/387)

If you really want to use msys2's git, try following.

1. Write git-wrap.bat for git.exe
    
    ```
    @echo off
    setlocal
    
    rem If you don't add path for msys2 into %PATH%, enable following line.
    rem set PATH=c:\msys64\usr\bin;%PATH%
    
    if "%1" equ "rev-parse" goto rev_parse
    git %*
    goto :eof
    :rev_parse
    for /f %%1 in ('git %*') do cygpath -w %%1
    ```
    
    Put this git-wrap.bat into somewhere.
2. Set `git.path` for git-wrap.bat open `File` -> `Preferences` -> `User Settings`, And add `git.path` pointed `git-wrap.bat` on your configuration file like below.
    
    ```
      "git.path": "c:/users/mattn/bin/git-wrap.bat",
    ```
    
3. Restart vscode

Have fun!
