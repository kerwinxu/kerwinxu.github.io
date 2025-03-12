---
title: "Windows 10家庭版如何添加Hyper-V虚拟机？"
date: "2019-06-21"
categories: 
  - "linux"
---

虚拟机算是很多企业用户的必备工具软件了，它能通过软件模拟具有完整硬件系统功能的、运行在一个完全隔离环境中的完整计算机操作系统，企业常用的虚拟机软件有VMware ESXi、Xenserver、Hyper-V等。随着计算机硬件的日新月异，虚拟机也从企业飞入了寻常百姓家了，个人用户也能安装使用虚拟机了。在个人电脑上常见的虚拟机有VMware Workstation、Virtual Box、Parallels Desktop、Hyper-V等。

![](https://img.ithome.com/newsuploadfiles/2018/8/20180805_203625_160.jpeg@wm_1,k_aW1nL3FkLnBuZw==,y_20,o_100,x_20,g_7 "IT之家学院：Windows 10家庭版如何添加Hyper-V虚拟机？只需一个脚本")

本文是是关于Hyper-V的，所以这里简单介绍一下。Hyper-V是微软的一款虚拟化产品，算是之前Virtual PC和Virtual Server的继承者吧。微软在2003年收购了推出了Virtual PC软件的Connectix公司，并在其后推出了服务器使用的虚拟化软件Virtual Server和个人用户使用的虚拟化软件Virtual PC。Hyper-V在2008年随着Windows Server 2008推出，Virtual Server与Virtual PC也就逐渐淡出了人们视野。

Hyper-V跟微软自家之前的虚拟化产品Virtual PC、Virtual Server等产品相比，有着很显著的区别。Hyper-V的本质是一个虚拟化管理程序，和微软之前的Virtual Server系列产品，处在的层次不同，它更接近于硬件，这一点比较像VMware的ESX Server系列，实际上Hyper-V属于微软的第一个裸金属虚拟化产品。Hyper-V由hypervisor层直接运行于物理服务器硬件之上。所有的虚拟分区都通过hypervisor硬件通信，其中的hypervisor是一个很小、效率很高的代码集，负责协调这些调用。

正因为以上原因，Hyper-V对硬件还是有些要求的，针对服务器，只要满足以下四个条件就可以使用Hyper-v角色：

1.CPU支持数据执行保护（DEP）。

2.CPU支持硬件虚拟化技术。

3.CPU64位处理器。

4.内存最低限度为2GB。

针对个人电脑，除了以上几个要求外，CPU还必须支持二级地址转换，否则，是无法添加Hyper-V的。

可以使用Coreinfo工具软件 ([下载地址](https://download.sysinternals.com/files/Coreinfo.zip)）来查看电脑是否支持Hyper-V，这是微软SysinternalsSuite工具软件套件中的一个，很实用。具体使用方法，把下载好的Coreinfo解压到桌面上，用管理员模式打开PowerShell，输入：.\\ Coreinfo.exe -v，将显示你电脑虚拟化的相关信息，当然你已经添加了Hyper-V了，就无需使用这个软件了。下图所示的内容表明笔者电脑的CPU是完全支持Hyper-V的。

![](https://img.ithome.com/newsuploadfiles/2018/8/20180805_203625_289.png@wm_1,k_aW1nL3F3LnBuZw==,y_20,o_100,x_20,g_9 "IT之家学院：Windows 10家庭版如何添加Hyper-V虚拟机？只需一个脚本")

Hyper-V之前一直专属Windows Server平台，从Windows 8系统开始，个人用户才能使用Hyper-V，不过令人遗憾的是，只有Windows专业版及以上的系统才能使用Hyper-V，Windows家庭版是不能使用的，这个政策一直延续到现在的Windows 10。很多有Hyper-V需求的用户因此而升级为Windows 10专业版。如果仅仅想用Hyper-V而升级为专业版完全没有必要，因为家庭版其实是能添加Hyper-V的。

添加方法非常简单，把以下内容保存为.cmd文件，然后以管理员身份打开这个文件。提示重启时保存好文件重启吧，重启完成就能使用功能完整的Hyper-V了。

> pushd "%~dp0"
> 
> dir /b %SystemRoot%\\servicing\\Packages\\\*Hyper-V\*.mum >hyper-v.txt
> 
> for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\\servicing\\Packages\\%%i"
> 
> del hyper-v.txt
> 
> Dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL

![](https://img.ithome.com/newsuploadfiles/2018/8/20180805_203625_407.png@wm_1,k_aW1nL3F3LnBuZw==,y_20,o_100,x_20,g_9 "IT之家学院：Windows 10家庭版如何添加Hyper-V虚拟机？只需一个脚本")

脚本执行过程如上图所示，按Y重启之后，就可以在开始菜单-所有应用-Windows管理工具中找到“Hyper-V管理器”了，打开它就能使用Hyper-V。
