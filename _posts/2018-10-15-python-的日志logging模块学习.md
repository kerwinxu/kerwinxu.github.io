---
layout: post
title: "python 的日志logging模块学习"
date: "2018-10-15"
categories: ["计算机语言", "Python"]
---

### 简单的将日志打印到屏幕

 

<table border="1" cellspacing="0" cellpadding="0" bgcolor="#f1f1f1"><tbody><tr><td><code>import&nbsp;logging</code><div></div>logging.debug('This is debug message') logging.info('This is info message') logging.warning('This is warning message')<div></div><wbr><div></div><code><code></code></code><strong>屏幕上打印:</strong><code> WARNING:root:This is warning message</code></td></tr></tbody></table>

默认情况下，logging将日志打印到屏幕，日志级别为WARNING； 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

### 通过logging.basicConfig函数对日志的输出格式及方式做相关配置

<table border="1" cellspacing="0" cellpadding="0" bgcolor="#f1f1f1"><tbody><tr><td><code>import&nbsp;logging</code><div></div>logging.basicConfig(level=logging.DEBUG, <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>datefmt='%a, %d %b %Y %H:%M:%S', <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filename='myapp.log', <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>filemode='w') <wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> logging.debug('This is debug message') logging.info('This is info message') logging.warning('This is warning message')<div></div><wbr><div></div><code><code></code></code><strong>./myapp.log文件中内容为:</strong><code> Sun, 24 May 2009 21:48:54 demo2.py[line:11] DEBUG This is debug message Sun, 24 May 2009 21:48:54 demo2.py[line:12] INFO This is info message Sun, 24 May 2009 21:48:54 demo2.py[line:13] WARNING This is warning message</code></td></tr></tbody></table>

logging.basicConfig函数各参数: filename: 指定日志文件名 filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a' format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示: %(levelno)s: 打印日志级别的数值 %(levelname)s: 打印日志级别名称 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv\[0\] %(filename)s: 打印当前执行程序名 %(funcName)s: 打印日志的当前函数 %(lineno)d: 打印日志的当前行号 %(asctime)s: 打印日志的时间 %(thread)d: 打印线程ID %(threadName)s: 打印线程名称 %(process)d: 打印进程ID %(message)s: 打印日志信息 datefmt: 指定时间格式，同time.strftime() level: 设置日志级别，默认为logging.WARNING stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

### 将日志同时输出到文件和屏幕

```
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
```

 

### logging之日志回滚

<table border="1" cellspacing="0" cellpadding="0" bgcolor="#f1f1f1"><tbody><tr><td><code><code>import&nbsp;logging from&nbsp;logging.handlers&nbsp;import&nbsp;RotatingFileHandler</code></code>################################################################################################# #定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M Rthandler&nbsp;=&nbsp;RotatingFileHandler('myapp.log',&nbsp;maxBytes=10*1024*1024,backupCount=5) Rthandler.setLevel(logging.INFO) formatter&nbsp;=&nbsp;logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s') Rthandler.setFormatter(formatter) logging.getLogger('').addHandler(Rthandler) ################################################################################################</td></tr></tbody></table>

从上例和本例可以看出，logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。 logging的几种handle方式如下：

<table align="center"><tbody><tr><td>logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件 logging.FileHandler: 日志输出到文件日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler<wbr> logging.handlers.BaseRotatingHandler logging.handlers.RotatingFileHandler logging.handlers.TimedRotatingFileHandler<wbr>logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets logging.handlers.DatagramHandler:&nbsp;<wbr>&nbsp;远程输出日志到UDP sockets logging.handlers.SMTPHandler:&nbsp;<wbr>&nbsp;远程输出日志到邮件地址 logging.handlers.SysLogHandler: 日志输出到syslog logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志 logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器</td></tr></tbody></table>

由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中， 上述其它处理方式的使用请参见python2.5手册！

### 通过logging.config模块配置日志

<table border="1" cellspacing="0" cellpadding="0" bgcolor="#f1f1f1"><tbody><tr><td><code>#logger.conf </code><code>###############################################</code><code>[loggers] keys=root,example01,example02</code><div></div><code>[logger_root] level=DEBUG handlers=hand01,hand02</code><div></div><code>[logger_example01] handlers=hand01,hand02 qualname=example01 propagate=0</code><div></div><code>[logger_example02] handlers=hand01,hand03 qualname=example02 propagate=0</code><div></div><code>###############################################</code><div></div><code>[handlers] keys=hand01,hand02,hand03</code><div></div><code>[handler_hand01] class=StreamHandler level=INFO formatter=form02 args=(sys.stderr,)</code><div></div><code>[handler_hand02] class=FileHandler level=DEBUG formatter=form01 args=('myapp.log', 'a')</code><div></div><code>[handler_hand03] class=handlers.RotatingFileHandler level=INFO formatter=form02 args=('myapp.log', 'a', 10*1024*1024, 5)</code><div></div><code>###############################################</code><div></div><code>[formatters] keys=form01,form02</code><div></div><code>[formatter_form01] format=%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s datefmt=%a, %d %b %Y %H:%M:%S</code><div></div><code>[formatter_form02] format=%(name)-12s: %(levelname)-8s %(message)s datefmt=</code></td></tr></tbody></table>

上例3：

<table border="1" cellspacing="0" cellpadding="0" bgcolor="#f1f1f1"><tbody><tr><td><code><code>import&nbsp;logging import&nbsp;logging.config</code></code>logging.config.fileConfig("logger.conf") logger&nbsp;=&nbsp;logging.getLogger("example01")<code><code></code></code>logger.debug('This is debug message') logger.info('This is info message') logger.warning('This is warning message')</td></tr></tbody></table>

上例4：

<table border="1" cellspacing="0" cellpadding="0" bgcolor="#f1f1f1"><tbody><tr><td><code><code>import&nbsp;logging import&nbsp;logging.config</code></code>logging.config.fileConfig("logger.conf") logger&nbsp;=&nbsp;logging.getLogger("example02")<code><code></code></code>logger.debug('This is debug message') logger.info('This is info message') logger.warning('This is warning message')</td></tr></tbody></table>

### logging是线程安全的

 

### 多模块使用logging

主模块mainModule.py

```
import logging
import subModule
logger = logging.getLogger("mainModule")
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)


logger.info("creating an instance of subModule.subModuleClass")
a = subModule.SubModuleClass()
logger.info("calling subModule.subModuleClass.doSomething")
a.doSomething()
logger.info("done with  subModule.subModuleClass.doSomething")
logger.info("calling subModule.some_function")
subModule.som_function()
logger.info("done with subModule.some_function")
```

 

子模块subModule.py，

```
import logging

module_logger = logging.getLogger("mainModule.sub")
class SubModuleClass(object):
    def __init__(self):
        self.logger = logging.getLogger("mainModule.sub.module")
        self.logger.info("creating an instance in SubModuleClass")
    def doSomething(self):
        self.logger.info("do something in SubModule")
        a = []
        a.append(1)
        self.logger.debug("list a = " + str(a))
        self.logger.info("finish something in SubModuleClass")

def som_function():
    module_logger.info("call function some_function")
```

执行之后，在控制和日志文件log.txt中输出，

2016-10-09 20:25:42,276 - mainModule - INFO - creating an instance of subModule.subModuleClass 2016-10-09 20:25:42,279 - mainModule.sub.module - INFO - creating an instance in SubModuleClass 2016-10-09 20:25:42,279 - mainModule - INFO - calling subModule.subModuleClass.doSomething 2016-10-09 20:25:42,279 - mainModule.sub.module - INFO - do something in SubModule 2016-10-09 20:25:42,279 - mainModule.sub.module - INFO - finish something in SubModuleClass 2016-10-09 20:25:42,279 - mainModule - INFO - done with subModule.subModuleClass.doSomething 2016-10-09 20:25:42,279 - mainModule - INFO - calling subModule.some\_function 2016-10-09 20:25:42,279 - mainModule.sub - INFO - call function some\_function 2016-10-09 20:25:42,279 - mainModule - INFO - done with subModule.some\_function

首先在主模块定义了logger'mainModule'，并对它进行了配置，就可以在解释器进程里面的其他地方通过getLogger('mainModule')得到的对象都是一样的，不需要重新配置，可以直接使用。定义的该logger的子logger，都可以共享父logger的定义和配置，所谓的父子logger是通过命名来识别，任意以'mainModule'开头的logger都是它的子logger，例如'mainModule.sub'。
