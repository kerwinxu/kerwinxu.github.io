---
layout: post
title: "python3 序列化模块（json、pickle、shelve）"
date: "2018-01-15"
categories: ["计算机语言", "Python"]
---

# 序列化模块

**序列化的目的**

1、以某种存储形式使自定义对象持久化；

2、将对象从一个地方传递到另一个地方。

3、使程序更具维护性。

![no img]

## 1.json

Json模块提供了四个功能：dumps、dump、loads、load

 

![复制代码]

```
import json
#(1)dumps
dic = {'k1':'值1','k2':'值2','k3':'值3'}
str_dic = json.dumps(dic)   #将字典转换成一个字符串
print(type(str_dic),str_dic)
'''结果：
<class 'str'> {"k3": "\u503c3", "k1": "\u503c1", "k2": "\u503c2"}
'''

#（2）loads
dic2 = json.loads(str_dic)  #将一个序列化转换成字典
print(type(dic2),dic2)
'''结果：
<class 'dict'> {'k3': '值3', 'k1': '值1', 'k2': '值2'}
'''

#（3）dump
f1 = open('json_file','w')  #默认编码方式是GBK
dic = {'k1':'值1','k2':'值2','k3':'值3'}
json.dump(dic,f1)   #dump方法将dic字典信息，转换成json字符串写入文件
f1.close()

#（4）load
f = open('json_file')   #默认编码方式是GBK
dic2 = json.load(f) #load方法将文件中的内容转换成数据类型返回
f.close()
print(type(dic2),dic2)
'''结果：
<class 'dict'> {'k3': '值3', 'k1': '值1', 'k2': '值2'}
'''

#（5）ensure_ascii
import json
f = open('file','w')    #以写的方式打开一个文件    #默认编码方式是GBK
json.dump({'国籍':'中国'},f)    #将{'国籍':'中国'}转换成json字符串写入文件中
ret = json.dumps({'国籍':'中国'})   #将{'国籍':'中国'}转换成json字符串赋给变量ret
f.write(ret+'\n')   #将ret的json字符串内容写入文件
json.dump({'国籍':'美国'},f,ensure_ascii=False) #dump对于中文默认以ASCII码存储，如果不使用需指定ensure_ascii=False
ret = json.dumps({'国籍':'美国'},ensure_ascii=False)    #dumps对于中文默认以ASCII码存储，如果不使用需指定ensure_ascii=False
f.write(ret+'\n')
f.close()

#（6）其它参数说明
r'''
Serialize obj to a JSON formatted str.(字符串表示的json对象) 
Skipkeys：默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。
此时设置成True，则会跳过这类key 
ensure_ascii:，当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示。) 
If check_circular is false, then the circular reference check for container types will be skipped and a circular reference will result in 
an OverflowError (or worse). 
If allow_nan is false, then it will be a ValueError to serialize out of range float values (nan, inf, -inf) in strict compliance of the 
JSON specification, instead of using the JavaScript equivalents (NaN, Infinity, -Infinity). 
indent：应该是一个非负的整型，如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫
pretty-printed json 
separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：
”隔开。 
default(obj) is a function that should return a serializable version of obj or raise TypeError. The default simply raises TypeError. 
sort_keys：将数据根据keys的值进行排序。 
To use a custom JSONEncoder subclass (e.g. one that overrides the .default() method to serialize additional types), specify it with the
 cls kwarg; otherwise JSONEncoder is used.
'''

#（7）格式化输出
import json
data = {'username':['李华','二愣子'],'sex':'male','age':16}
json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
print(json_dic2)
'''结果：
{
  "age":16,
  "sex":"male",
  "username":[
    "李华",
    "二愣子"
  ]
}'''
```

![复制代码]

## 2.pickle

![复制代码]

```
json和pickle的区别
用于序列化的两个模块

　　json，用于字符串 和 python数据类型间进行转换
　　pickle，用于python特有的类型 和 python的数据类型间进行转换

pickle模块提供了四个功能：dumps、dump(序列化，存）、loads（反序列化，读）、load  （不仅可以序列化字典，列表...可以把python中任意的数据类型序列化）
```

![复制代码]

![复制代码]

```
import pickle
#（1）dumps
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic) # dumps 方法将字典转换成字节
print(str_dic)
'''结果：
b'\x80\x03}q\x00(X\x02\x00\x00\x00k2q\x01X\x02\x00\x00\x00v2q\x02X\x02\x00\x00\x00k1q\x03X\x02\x00\x00\x00v1q\x04X\x02\x00\x00\x00k3q\x05X\x02\x00\x00\x00v3q\x06u.'
'''

#（2）loads
dic2 = pickle.loads(str_dic)    # loads反序列化方法，将dumps生成的字节转换成数据类型
print(dic2)    #字典
'''结果：
{'k2': 'v2', 'k1': 'v1', 'k3': 'v3'}
'''


#（3）dump
import time
struct_time  = time.localtime(1000000000)
print(struct_time)
f = open('pickle_file','wb')
pickle.dump(struct_time,f)  #dump序列化方法，将内容转换成序列化数据存到文件汇总
f.close()

#（4）load
f = open('pickle_file','rb')
struct_time2 = pickle.load(f)   #load反序列化方法，将文件中的序列化数据读取出来
print(struct_time2.tm_year)
```

![复制代码]

## 3.shelve

![复制代码]

```
# shelve也是python提供给我们的序列化工具，比pickle用起来更简单一些。
# shelve只提供给我们一个open方法，是用key来访问的，使用起来和字典类似。
#（1）shelve存入数据
import shelve
f = shelve.open('shelve_file')
f['key'] = {'int':10, 'float':9.5, 'string':'Sample data'}  #直接对文件句柄操作，就可以存入数据
f.close()

#（2）shelve读出数据
import shelve
f1 = shelve.open('shelve_file')
existing = f1['key']  #取出数据的时候也只需要直接用key获取即可，但是如果key不存在会报错
f1.close()
print(existing)
```

![复制代码]
