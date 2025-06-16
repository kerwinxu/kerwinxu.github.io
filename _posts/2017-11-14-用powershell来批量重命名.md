---
layout: post
title: "用powershell来批量重命名"
date: "2017-11-14"
categories: ["计算机语言", "dos_powdershell"]
---

```
dir *.pdf | foreach { Rename-Item $_ -NewName ($_.BaseName + "_123.pdf")  }
Get-ChildItem Default_*.csv  |Rename-Item -NewName {$_.name -replace '^Default','VOD'}

```

$\_.FullName
