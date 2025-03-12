---
title: "用powershell将excel存为html格式"
date: "2019-03-20"
categories: 
  - "dos_powdershell"
---

```
$xlHtml = 44
$missing = [type]::Missing
$xl = New-Object -ComObject Excel.Application
$xl.Visible = $true
$wb = $xl.Workbooks.Open('d:\book1.xlsx')
$xl.ActiveWorkbook.SaveAs('d:book1.html',$xlHtml,$missing,$missing,$missing,$missing,$missing,$missing,$missing,$missing,$missing,$missing)
$xl.Quit()


```
