---
title: "python当shell"
date: "2019-02-18"
categories: 
  - "python"
---

我想用python当shell用，这里记录相关的操作

# python文件夹操作

## 取得当前目录

os.getcwd()

## 更改当前目录

os.chdir( "C:\\\\123")

## 将一个路径名分解为目录名和文件名两部分

fpath , fname = os.path.split( "你要分解的路径")

例如：

a, b = os.path.split( "c:\\\\123\\\\456\\\\test.txt" )

print a

print b

显示：

c:\\123\\456

test.txt

## 分解文件名的扩展名

pathandname , fext = os.path.splitext( "你要分解的路径")

例如：

a, b = os.path.splitext( "c:\\\\123\\\\456\\\\test.txt" )

print a

print b

显示：

c:\\123\\456\\test

.txt

## 判断一个路径（ 目录或文件）是否存在

b = os.path.exists( "你要判断的路径")

返回值b： True 或 False

## 判断一个路径是否文件

b = os.path.isfile( "你要判断的路径")

返回值b： True 或 False

## 判断一个路径是否目录

b = os.path.isdir( "你要判断的路径")

返回值b： True 或 False

## 获取某目录中的文件及子目录的列表

L = os.listdir( "你要判断的路径")

例如：

L = os.listdir( "c:/" )

print L

显示 :

\['1.avi', '1.jpg', '1.txt', 'CONFIG.SYS', 'Inetpub', 'IO.SYS', 'KCBJGDJC', 'KCBJGDYB', 'KF\_GSSY\_JC', 'MSDOS.SYS', 'MSOCache', 'NTDETECT.COM', 'ntldr', 'pagefile.sys', 'PDOXUSRS.NET', 'Program Files', 'Python24', 'Python31', 'QQVideo.Cache', 'RECYCLER', 'System Volume Information', 'TDDOWNLOAD', 'test.txt', 'WINDOWS'\]

这里面既有文件也有子目录

## 创建子目录

os.makedirs( path ) # path 是"要创建的子目录"

例如:

os.makedirs( "C:\\\\123\\\\456\\\\789")

调用有可能失败，可能的原因是：

(1) path 已存在时(不管是文件还是文件夹)

(2) 驱动器不存在

(3) 磁盘已满

(4)磁盘是只读的或没有写权限

## 删除子目录

os.rmdir( path ) # path: "要删除的子目录"

产生异常的可能原因:

(1) path 不存在

(2) path 子目录中有文件或下级子目录

(3) 没有操作权限或只读

测试该函数时，请自已先建立子目录。

## 删除文件

os.remove( filename ) # filename: "要删除的文件名"

产生异常的可能原因:

(1) filename 不存在

(2) 对filename文件， 没有操作权限或只读。

## 文件改名

os.name( oldfileName, newFilename)

产生异常的原因：

(1) oldfilename 旧文件名不存在

(2) newFilename 新文件已经存在时，此时，您需要先删除 newFilename 文件。

 

# subprocess

## subprocess.call()

 

父进程等待子进程完成 返回退出信息(returncode，相当于Linux exit code)

## **subprocess.check\_call()**

父进程等待子进程完成 返回0 检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性，可用try…except…来检查

## **subprocess.check\_output()**

父进程等待子进程完成 返回子进程向标准输出的输出结果 检查退出信息，如果returncode不为0，则举出错误subprocess.CalledProcessError，该对象包含有returncode属性和output属性，output属性为标准输出的输出结果，可用try…except…来检查。

## **subprocess.Popen()**

subprocess模块定义了一个类： Popen

 

```
class subprocess.Popen( args, 
      bufsize=0, 
      executable=None,
      stdin=None,
      stdout=None, 
      stderr=None, 
      preexec_fn=None, 
      close_fds=False, 
      shell=False, 
      cwd=None, 
      env=None, 
      universal_newlines=False, 
      startupinfo=None, 
      creationflags=0)

```

- args: args参数。可以是一个字符串，可以是一个包含程序参数的列表。要执行的程序一般就是这个列表的第一项，或者是字符串本身。 subprocess.Popen(\["cat","test.txt"\]) subprocess.Popen("cat test.txt") 这两个之中，后者将不会工作。因为如果是一个字符串的话，必须是程序的路径才可以。(考虑unix的api函数exec，接受的是字符串 列表) 但是下面的可以工作 subprocess.Popen("cat test.txt", shell=True) 这是因为它相当于 subprocess.Popen(\["/bin/sh", "-c", "cat test.txt"\]) 在\*nix下，当shell=False（默认）时，Popen使用os.execvp()来执行子程序。args一般要是一个【列表】。如果args是个字符串的 话，会被当做是可执行文件的路径，这样就不能传入任何参数了。注意： shlex.split()可以被用于序列化复杂的命令参数，比如： >>> shlex.split('ls ps top grep pkill') \['ls', 'ps', 'top', 'grep', 'pkill'\] >>>import shlex, subprocess >>>command\_line = raw\_input() /bin/cat -input test.txt -output "diege.txt" -cmd "echo '$MONEY'" >>>args = shlex.split(command\_line) >>> print args \['/bin/cat', '-input', 'test.txt', '-output', 'diege.txt', '-cmd', "echo '$MONEY'"\] >>>p=subprocess.Popen(args) 可以看到，空格分隔的选项（如-input）和参数（如test.txt）会被分割为列表里独立的项，但引号里的或者转义过的空格不在此列 。这也有点像大多数shell的行为。在\*nix下，当shell=True时，如果arg是个字符串，就使用shell来解释执行这个字符串。如果args是个列表，则第一项被视为命令， 其余的都视为是给shell本身的参数。也就是说，等效于： subprocess.Popen(\['/bin/sh', '-c', args\[0\], args\[1\], ...\])在Windows下，下面的却又是可以工作的 subprocess.Popen(\["notepad.exe", "test.txt"\]) subprocess.Popen("notepad.exe test.txt") 这是由于windows下的api函数CreateProcess接受的是一个字符串。即使是列表形式的参数，也需要先合并成字符串再传递给api函数 subprocess.Popen("notepad.exe test.txt" shell=True) 等同于 subprocess.Popen("cmd.exe /C "+"notepad.exe test.txt" shell=True）
- bufsize参数: 如果指定了bufsize参数作用就和内建函数open()一样：0表示不缓冲，1表示行缓冲，其他正数表示近似的缓冲区字节数，负数表 示使用系统默认值。默认是0。
- executable参数: 指定要执行的程序。它很少会被用到：一般程序可以由args 参数指定。如果shell=True ，executable 可以用于指定用哪个shell来执行（比如bash、csh、zsh等）。\*nix下，默认是 /bin/sh ，windows下，就是环境变量 COMSPEC 的值。windows下，只有当你要执行的命令确实是shell内建命令（比如dir ，copy 等）时，你才需要指定shell=True ，而当你要执行一个基于命令行的批处理脚本的时候，不需要指定此项。
- stdin stdout和stderr： stdin stdout和stderr，分别表示子程序的标准输入、标准输出和标准错误。可选的值有PIPE或者一个有效的文件描述符（其实是个正 整数）或者一个文件对象，还有None。如果是PIPE，则表示需要创建一个新的管道，如果是None ，不会做任何重定向工作，子进程的文件描述符会继承父进程的。另外，stderr的值还可以是STDOUT ，表示子进程的标准错误也输出到标准输出。
- preexec\_fn参数： 如果把preexec\_fn设置为一个可调用的对象（比如函数），就会在子进程被执行前被调用。（仅限\*nix）
- close\_fds参数： 如果把close\_fds设置成True，\*nix下会在开子进程前把除了0、1、2以外的文件描述符都先关闭。在 Windows下也不会继承其他文件描述符。
- shell参数： 如果把shell设置成True，指定的命令会在shell里解释执行。
- cwd参数： 如果cwd不是None，则会把cwd做为子程序的当前目录。注意，并不会把该目录做为可执行文件的搜索目录，所以不要把程序文件所在 目录设置为cwd 。
- env参数： 如果env不是None，则子程序的环境变量由env的值来设置，而不是默认那样继承父进程的环境变量。注意，即使你只在env里定义了 某一个环境变量的值，也会阻止子程序得到其 他的父进程的环境变量（也就是说，如果env里只有1项，那么子进程的环境变量就只有1个了）。例如：>>> subprocess.Popen('env', env={'test':'123', 'testtext':'zzz'}) test=123 <subprocess.Popen object at 0x2870ad2c> testtext=zzz
- universal\_newlines参数: 如果把universal\_newlines 设置成True，则子进程的stdout和stderr被视为文本对象，并且不管是\*nix的行结束符（'/n' ），还是老mac格式的行结束符（'/r' ），还是windows 格式的行结束符（'/r/n' ）都将被视为 '/n' 。startupinfo和creationflags参数： 如果指定了startupinfo和creationflags，将会被传递给后面的CreateProcess()函数，用于指定子程序的各种其他属性，比如主窗口样式或者是 子进程的优先级等。（仅限Windows）

## 子进程的文本流控制

子进程的标准输入、标准输出和标准错误如下属性分别表示:

- child.stdin
- child.stdout
- child.stderr

可以在Popen()建立子进程的时候改变标准输入、标准输出和标准错误，并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe)，如下2个例子：

```
>>> import subprocess
>>> child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
>>> print child1.stdout.read(),
#或者child1.communicate()
>>> import subprocess
>>> child1 = subprocess.Popen(["cat","/etc/passwd"], stdout=subprocess.PIPE)
>>> child2 = subprocess.Popen(["grep","0:0"],stdin=child1.stdout, stdout=subprocess.PIPE)
>>> out = child2.communicate()

```

subprocess.PIPE实际上为文本流提供一个缓存区。child1的stdout将文本输出到缓存区，随后child2的stdin从该PIPE中将文本读取走。child2的输出文本也被存放在PIPE中，直到communicate()方法从PIPE中读取出PIPE中的文本。 注意：communicate()是Popen对象的一个方法，该方法会阻塞父进程，直到子进程完成.
