---
layout: post
title: "python科学运算之numpy"
date: "2017-06-03"
categories: 
  - "python"
---

 

1. numpy提供了2中简单的对象
    1. ndarray : 存储单一数据类型的多维数组。
    2. ufunc ： 能够对数组进行处理的函数。
2. ndarray  :
    1. 创建数组：
        1. a=np.array(\[1,2,3\]) #创建一维数组。
        2. b=np.array(\[\[1,2,3\],\[4,5,6\]\]) #多层嵌套的序列将创建多维数组。
        3. np.arange(开始值，终值，步长)
        4. np.linspace(开始值，终值，元素个数) ,可以指定endpoint关键字指定是否包含终值，缺省包含终值。
        5. np.logspace(开始值，终值，袁术个数），这个产生的是等比序列，比如np.logspace(0,2,20)，会产生10的0次方到10的2次方，有20个元素的等比序列。
        6. fromstring,frombuffer,fromfile,可以从字节序列创建数组。np.fromstring("abc",dtype=np.int8),也可以np.int16,np.float,
        7. fromfunction,从一个函数创建序列。比如：
            1. def func1(i,j): return (i+1)\*(j+1) a=np.fromfunction(func1,(9,9)) #这里创建的是一个99乘法表。
    2. 数组的属性：
        1.  shape : 数组的大小可以用shape属性获得。
        2. dtype :取得数组的类型。
    3. 存取元素，数组的存储方法与python的标准方法相同。都是用\[\] .
        1. 使用整数序列。组成一个新的数组。比如x\[\[2,3,4\]\],将下标2，3，4的元素重新组成一个数组。
        2. 使用布尔序列。比如，x\[np. array(\[True, False, True, False, False\])\]，True的是0和2下标，将这2个元素重新组成一个数组。比如如下的 x = np. random. rand(10) # 产生一个长度为10，元素值为0-1的随机数的数组 x>0.5 #数组x中的每个元素和0.5进行大小比较，得到一个布尔数组，True表示x中对应的值大于0.5 x\[x>0.5\] # 使用x>0.5返回的布尔数组收集x中的元素，因此得到的结果是x中所有大于0.5的元素的数组
    4. 多维数组。a\[(0,1,2,3,4),(1,2,3,4,5)\] : 用于存取数组的下标和仍然是一个有两个元素的组元，组元中的每个元素都是整数序列，分别对应数组的第0轴和第1轴。从两个序列的对应位置取出两个整数组成下标： a\[0,1\], a\[1,2\], ..., a\[4,5\]。
    5. 结构数组：例子如下： persontype = np. dtype({ ' names' :\[' name' , ' age' , ' weight' \], ' formats' :\[' S32' , ' i' , ' f' \]}) a = np. array(\[("Zhang", 32, 75.5),("Wang", 24, 65.2)\], dtype=persontype)
        1. names指出了字段名
        2. formats指定了格式，S32为字符串，长度为32位，因为每个元素的大小必须固定，所以指定了字符串长度，i为整形，f为浮点数。
    6. 结构数组2，例子如下：dtype(\[('name', '|S32'), ('age', '<i4'), ('weight', '<f4')\])
        1. | : 忽视字节顺序
        2. < : 低位字节在前
        3. \> : 高位字节在前
    7. 结构数组3，np. dtype({' surname' :(' S25' , 0), ' age' :(np. uint8, 25)}) ，用字典来定义字段，因为字典没有顺序，0和那个25表示字段的偏移。
3. ufunc : 能对数组每个元素进行操作的函数。
    1. np.sin : 对每个元素正弦。
    2. np.frompyfunc的调用格式为frompyfunc(func, nin, nout)，其中func是计算单个元素的函数，nin是此 函数的输入参数的个数，nout是此函数的返回值的个数。
    3. ufunc的方法：ufunc函数本身还有些方法，这些方法只对两个输入一个输出的ufunc函数有效，其它的ufunc对象调用这些方法时会抛出ValueError异常。
        1. reduce 方法它沿着axis轴对array进行操作，相当于将<op>运算符插 入到沿axis轴的所有子数组或者元素当中。， np. add. reduce(\[1, 2, 3\]) # 1 + 2 + 3 , np. add. reduce(\[\[1, 2, 3\],\[4, 5, 6\]\], axis=1) # 1,4 + 2,5 + 3,6 如上是得到的是 array(\[ 6, 15\])，原理是，1+2+3=6，4+5+6=15
        2. accumulate 方法和reduce方法类似，只是它返回的数组和输入的数组的shape相同，保存所有的中间计算结果： np. add. accumulate(\[1, 2, 3\])，得到的是array(\[1, 3, 6\])，
        3. reduceat 方法计算多组reduce的结果，通过indices参数指定一系列reduce的起始和终了位置。
4. 方法：
    1. var : 均方差
    2. cov  : 协方差
