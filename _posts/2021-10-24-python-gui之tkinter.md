---
layout: post
title: "Python GUI之tkinter"
date: "2021-10-24"
categories: ["计算机语言", "Python"]
---

# 主要模块介绍

<table style="border-collapse: collapse; width: 100%; height: 455px;"><tbody><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">tk类</td><td style="width: 13.3333%; height: 24px;">元素</td><td style="width: 75.5151%; height: 24px;">说明</td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Button</td><td style="width: 13.3333%; height: 24px;">按钮</td><td style="width: 75.5151%; height: 24px;">command参数是点击处理函数。</td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Canves</td><td style="width: 13.3333%; height: 24px;">画布</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Checkbutton</td><td style="width: 13.3333%; height: 24px;">复选框</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr><td style="width: 11.1515%;">Entry</td><td style="width: 13.3333%;">单行文本框</td><td style="width: 75.5151%;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Frame</td><td style="width: 13.3333%; height: 24px;">框架</td><td style="width: 75.5151%; height: 24px;">用来放置其他的gui元素，一个容器</td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">LabelFrame</td><td style="width: 13.3333%; height: 24px;">容器控件</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Listbox</td><td style="width: 13.3333%; height: 24px;">列表框</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Menu</td><td style="width: 13.3333%; height: 24px;">菜单</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">MenuButton</td><td style="width: 13.3333%; height: 24px;">按钮菜单</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Message</td><td style="width: 13.3333%; height: 24px;">消息框</td><td style="width: 75.5151%; height: 24px;">类似标签，但可以显示多行文本。</td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">OptionMenu</td><td style="width: 13.3333%; height: 24px;">选择菜单</td><td style="width: 75.5151%; height: 24px;">下单菜单的改版。</td></tr><tr style="height: 23px;"><td style="width: 11.1515%; height: 23px;">Ratiobutton</td><td style="width: 13.3333%; height: 23px;">单选框</td><td style="width: 75.5151%; height: 23px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Scale</td><td style="width: 13.3333%; height: 24px;">滑动条</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">ScrollBar</td><td style="width: 13.3333%; height: 24px;">滚动条</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Spinbox</td><td style="width: 13.3333%; height: 24px;">输入控件</td><td style="width: 75.5151%; height: 24px;">与Entry类似，但可以指定输入范围</td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Text</td><td style="width: 13.3333%; height: 24px;">多行文本框</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">Toplevel</td><td style="width: 13.3333%; height: 24px;">顶层</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;">messageBox</td><td style="width: 13.3333%; height: 24px;">消息框</td><td style="width: 75.5151%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 11.1515%; height: 24px;"></td><td style="width: 13.3333%; height: 24px;"></td><td style="width: 75.5151%; height: 24px;"></td></tr></tbody></table>

from tkinter import  ttk

<table style="border-collapse: collapse; width: 100%;"><tbody><tr><td style="width: 14.303%;">ttk类</td><td style="width: 20.7272%;">简介</td><td style="width: 64.9697%;">说明</td></tr><tr><td style="width: 14.303%;"><div><div>Combobox</div></div></td><td style="width: 20.7272%;">组合框</td><td style="width: 64.9697%;">文本框跟下拉框的组合，values中一定要是元组或者数组，</td></tr><tr><td style="width: 14.303%;"></td><td style="width: 20.7272%;"></td><td style="width: 64.9697%;"></td></tr><tr><td style="width: 14.303%;"></td><td style="width: 20.7272%;"></td><td style="width: 64.9697%;"></td></tr></tbody></table>

# 布局

窗口部件三种放置方式pack/grid/place

## 绝对布局

.place(x=10, y=10)

 

## 相对布局

.pack(fill=？, side=？)

side:停靠在哪个方向

- left: 左
- top: 上
- right: 右
- botton: 下

fill:填充

- x:水平方向填充
- y:竖直方向填充
- both:水平和竖直方向填充
- none:不填充

expand:

- True:随主窗体的大小变化
- False:不随主窗体的大小变化

anchor:

- N:北 下
- E:东 右
- S:南 下
- W:西 左
- CENTER:中间

padx:x方向的外边距

pady:y方向的外边距

ipadx:x方向的内边距

ipady：y方向的内边距

## 表格布局

.grid(row=？,column=？）

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫
 
import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，grid 放置方法
for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
 
# 第5步，主窗口循环显示
window.mainloop()
```

 

# 变量

```
var = StringVar()
var.trace("w", callback)
entry = Entry(root, textvariable=var)
```

```
x = StringVar() # 保存一个 string 类型变量, 默认值为""
x = IntVar() # 保存一个整型变量, 默认值为0
x = DoubleVar() # 保存一个浮点型变量, 默认值为0.0
x = BooleanVar() # 保存一个布尔型变量, 返回值为 0 (代表 False) 或 1 (代表 True)
```

要得到其保存的变量值, 使用它的 get() 方法即可. 要设置其保存的变量值, 使用它的 set() 方法即可

 

 

# 简单步骤

```
import tkinter as tk  # 使用Tkinter前需要先导入
 
# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('My Window')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
# 第4步，在图形界面上设定标签
l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
 
# 第5步，放置标签
l.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();
 
# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
```

 

# 模块详解

## 关于OptionMenu的例子

```
import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")

labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="The selected item is {}".format(variable.get()))

variable.trace("w", callback)

app.mainloop()
```

 

## 文件对话框

需要 import tkinter.filedialog

- tkinter.filedialog.asksaveasfilename():选择以什么文件名保存，返回文件名
- tkinter.filedialog.asksaveasfile():选择以什么文件保存，创建文件并返回文件流对象
- tkinter.filedialog.askopenfilename():选择打开什么文件，返回文件名
- tkinter.filedialog.askopenfile():选择打开什么文件，返回IO流对象
- tkinter.filedialog.askdirectory():选择目录，返回目录名
- tkinter.filedialog.askopenfilenames():选择打开多个文件，以元组形式返回多个文件名
- tkinter.filedialog.askopenfiles():选择打开多个文件，以列表形式返回多个IO流对象

 

# MessageBox消息框

```
tkinter.messagebox.showinfo(title='Hi', message='你好！')            # 提示信息对话窗
tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'
```

 

# 引用

- [Python GUI之tkinter窗口视窗教程大集合（看这篇就够了）](https://www.cnblogs.com/shwee/p/9427975.html#C1)
