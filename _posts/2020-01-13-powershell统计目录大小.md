---
layout: post
title: "powershell统计目录大小"
date: "2020-01-13"
categories: ["计算机语言", "dos_powdershell"]
---

```
$directories=Get-ChildItem e:\
foreach ($directory in $directories){       
$size = Get-ChildItem $directorie.FullName -Recurse –File -ErrorAction SilentlyContinue  | Measure-Object -Property length -sum
write-host "the size of $directory is : "  ,("{0:N2}" -f ($size.sum / 1MB)),"MB】----"
}

```

如上这个已经失效

```
function filesize ([string]$filepath)
{
  
  if ($filepath -eq $null)
  {
    throw "路径不能为空"
  }
  dir -Path $filepath |
  ForEach-Object -Process {
    if ($_.psiscontainer -eq $true)
    {
      $length = 0
      dir -Path $_.fullname -Recurse | ForEach-Object{
        $length += $_.Length
      }
      $l = $length/1KB
      $_.name + "文件夹的大小为： {0:n1} KB" -f $l
    }
  }
  
}
filesize -filepath "E:\系统文件转储\桌面\test"
```
