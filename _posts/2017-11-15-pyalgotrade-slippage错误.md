---
title: "pyalgotrade在python3上安装"
date: "2017-11-15"
categories: 
  - "python"
  - "回测交易"
---

[https://github.com/jingzhaoyang/pyalgotrade](https://github.com/jingzhaoyang/pyalgotrade)

 

PyAlgoTrade是一个开源回测平台，不过它本身支持Python2版本的，而在PyAlgoTrade的一个交流群里，经常有人问它是否支持Python3，于是我就想把它作个Python3版本适配。背景交代完了，我们就来看看怎么来让其支持Python3版本。

# `iteritems()`与`items()`

在python2中字典的`iteritems`是返回一个迭代对象，而`items`是返回一个列表。他们最主要的区别就是迭代对象占用的内存更小，因为它不需要想列表一样一次分配整个列表的所有内存，只需要分配列表中一个元素的内存空间。然而，在python3版本中，`items`就返回迭代对象，并且去除了`iteritems`。下面是具体的文件修改：

```
--- a/pyalgotrade/barfeed/csvfeed.py
+++ b/pyalgotrade/barfeed/csvfeed.py
@@ -178,7 +178,7 @@ class GenericRowParser(RowParser):

         # Process extra columns.
         extra = {}
- for k, v in csvRowDict.iteritems():
+        for k, v in csvRowDict.items():
             if k not in self.__columnNames:
                 extra[k] = csvutils.float_or_string(v)
```

# `sort()`的`cmp`参数

在python2中如果想对字典列表中的某个字段进行对比排序，就需要用到`sort()`的cmp参数，如：

```
#python2以age排序
persons=[{'name':'zhang3','age':15},{'name':'li4','age':12}]
#升序
persons.sort(lambda a,b:cmp(a['age'],b['age']))
#降序
persons.sort(lambda a,b:cmp(b['age'],a['age']))
```

然而在python3.x中取消了cmp参数，也不支持直接往sort()里面传函数了。可以构造排序函数传递给key来实现。

```
#python3以age排序
persons=[{'name':'zhang3','age':15},{'name':'li4','age':12}]
#升序
persons.sort(key = lambda a:a['age'])
#降序需要传参reverse的值为True
persons.sort(key = lambda a:a['age'],reverse=True)
```

具体到PyAlgoTrade代码里，修改如下：

```
--- a/pyalgotrade/barfeed/membf.py
+++ b/pyalgotrade/barfeed/membf.py
@@ -68,15 +68,15 @@ class BarFeed(barfeed.BaseBarFeed):

         # Add and sort the bars
         self.__bars[instrument].extend(bars)
- barCmp = lambda x, y: cmp(x.getDateTime(), y.getDateTime())
- self.__bars[instrument].sort(barCmp)
+        barCmp = lambda x : x.getDateTime()
+        self.__bars[instrument].sort(key=barCmp)

         self.registerInstrument(instrument)
```

# `xrange()`与`range()`

在python2中xrange是返回迭代对象，而range是返回列表。而在python3中range返回迭代对象，而xrange被移除。这部分就不上代码了，只需要修改`xrange`为`range`就行。

# `csv`库里面的`next()`方法变更为`__next__()`

`csv`库在原python2中的`next()`方法被重命名为`__next__()`所以这里修改下名字就行了，具体修改代码如下：

```
--- a/pyalgotrade/utils/csvutils.py
+++ b/pyalgotrade/utils/csvutils.py
@@ -31,23 +31,23 @@ class FastDictReader(object):
         self.__fieldNames = fieldnames
         self.reader = csv.reader(f, dialect, *args, **kwargs)
         if self.__fieldNames is None:
- self.__fieldNames = self.reader.next()
+            self.__fieldNames = self.reader.__next__()
         self.__dict = {}

     def __iter__(self):
         return self

- def next(self):
+    def __next__(self):
         # Skip empty rows.
- row = self.reader.next()
+        row = self.reader.__next__()
         while row == []:
- row = self.reader.next()
+            row = self.reader.__next__()

         # Check that the row has the right number of columns.
         assert(len(self.__fieldNames) == len(row))

         # Copy the row values into the dict.
- for i in xrange(len(self.__fieldNames)):
+        for i in range(len(self.__fieldNames)):
             self.__dict[self.__fieldNames[i]] = row[i]

         return self.__dict
```

附上用python3跑官方文档单均线的示例：

![](http://upload-images.jianshu.io/upload_images/1924769-630e249d245790b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

SMA

# 备注

- 修改好的代码放在我的github上，点这里[传送门](https://github.com/jingzhaoyang/pyalgotrade)
- 为何不提交给上级源？PyAlgoTrade的作者在项目的issue里面回答过，他自己精力有限，没法同时做到两个版本的适配。如果想做两个版本的适配，需要对python版本进行判断，然后调用对应的代码，这个工作量要比只修改为python3版本工作量大许多。同时，还要维护PyAlgoTrade的更新，所以目前官方只支持Python2版本。

```
作者：ymengyue
链接：http://www.jianshu.com/p/8b46954b0227
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
