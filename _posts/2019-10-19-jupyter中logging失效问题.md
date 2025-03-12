---
layout: post
title: "jupyter中logging失效问题"
date: "2019-10-19"
categories: 
  - "python"
---

```
使用当前的ipython / Jupyter版本(例如6.2.1),logging.getLogger().处理程序列表在启动后为空,并且logging.getLogger().setLevel(logging.DEBUG)无效,即没有信息/调试消息打印.
在ipython中,您还必须更改ipython配置设置(并且可能解决ipython错误).例如,要降低日志记录阈值以调试消息：

# workaround via specifying an invalid value first
# %config Application.log_level='WORKAROUND' # 经过验证，这一条错误
# => fails, necessary on Fedora 27, ipython3 6.2.1
%config Application.log_level='DEBUG'
import logging
logging.getLogger().setLevel(logging.DEBUG)
log = logging.getLogger()
log.debug('Test debug')
要获取一个模块的调试消息(参见该模块中的__name__值),您可以使用更具体的一个替换上面的setLevel()调用：

logging.getLogger('some.module').setLevel(logging.DEBUG)
```
