---
title: "BIOS添加Grub2引导（Windows下操作）"
date: "2025-02-15"
categories: 
  - "linux"
---

到Grub2官网ftp://ftp.gnu.org/gnu/grub/ 下载文件grub-2.02-for-windows.zip

wmic diskdrive list brief，记录下安装目标磁盘DeviceID

cd /d d:\\grub-2.02-for-windows

grub-install.exe --directory=D:\\grub-2.02-for-windows\\i386-pc --fonts=unicode （为默认项，可不写） --install-modules=all (如果安装全部，参数不能为all，必须删除) --locale-directory=D:\\grub-2.02-for-windows\\locale --locales=zh\_CN (默认为all) --themes=starfield (此项参数为默认，可不写) --boot-directory=c: --force --label-bgcolor=black (默认项，可不写) --label-color=wite (默认项，可不写) --label-font =unicode(默认项，可不写)

\--recheck --target=i386-pc （默认项可不写） \\\\.\\PHYSICALDRIVE0 (安装设备)

 

grub.cfg文件生成

```
#################################################
#设置菜单的超时时间为5秒
set timeout=5
#每一满屏后暂停输出，以免信息太多一闪而过看不清
set pager=1
################################################
#默认启动第一个菜单项
set default=0
#如果第一个菜单项启动失败，转而启动第二个菜单项
set fallback=1
#################################################
#开启密码验证功能，并设置一个名为'admin'的超级用户
# set superusers=admin
#################################################
#设置主题模式，支持的模式可以grub引导界面，输入e，进入命令行，输入videoinfo查看。
set gfxmode=1600x900x32,auto
#设置主题
set theme=$prefix/themes/starfield/theme.txt
#################################################
#指定翻译文件(*.mo)的目录，若未明确设置此目录，则无法显示中文界面。
set locale_dir=$prefix/locale
#将GRUB2设置为简体中文界面
set lang=zh_CN
#################################################
function load_video {
insmod efi_gop
insmod efi_uga
insmod video_bochs
insmod video_cirrus
insmod all_video
}
function load_disk {
insmod part_gpt
insmod part_msdos
}
function load_filesystem {
insmod ext2
insmod ext3
insmod ext4
insmod ntfs
}
load_video
load_disk
load_filesystem
#################################################
#激活图形模式的输出终端
insmod gfxterm
terminal_output  gfxterm

insmod gfxmenu
insmod png

loadfont $prefix/themes/starfield/dejavu_bold_14.pf2
export theme
#################################################
#设置'root'用户的哈希密码[通过"grub-mkpasswd-pbkdf2"工具生成]
password_pbkdf2 admin grub.pbkdf2.sha512.10000.29CFC23F7FC74CA1A2AA0CFFCC3CE9D38EB7D3FCFD7A9BFA172AAC1816D580C3076DFC7DCBB2B6944B86765793F10D5B804760FFBBF012CE4B79A5ACD6DB8298.7A3F7ADB7A50D7B387BCF07E425276C6247039F63A37EEC744E91D0191283C8353167B9D32751E9E27E9E99A9EBB8ABBEB40BE5171098096EA47735A5F8CC418
#################################################
menuentry 'Windows 10' --class class --hotkey "w" --id windows {
search --file --set=root --no-floppy /bootmgr
chainloader +1
}


menuentry 'install ubuntu' -class ubuntu --id ubuntu{



}


menuentry 'install ubuntu' --class fedora --class gnu-linux --class gnu --class os --unrestricted --hotkey "c" --id linux {
insmod exfat
search --file  --no-floppy --set=root /ubuntu-20.04.1-desktop-amd64.iso
loopback loop ($root)/ubuntu-20.04.1-desktop-amd64.iso
linux (loop)/casper/vmlinuz boot=casper iso-scan/filename=/ubuntu-20.04.1-desktop-amd64.iso
initrd (loop)/casper/initrd

}


menuentry 'win pe' --class windows --id winpe{
insmod exfat
search --file  --no-floppy --set=root /iso/winpe.iso
set iso_path="/iso/winpe.iso"    
loopback loop ($root)$iso_path     
linux16 ($root)/grub/memdisk iso
initrd16 ($root)/iso/winpe.iso
}

```
