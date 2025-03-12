---
title: "python和C的交互"
date: "2018-09-24"
categories: 
  - "python"
---

# 用Ctypes来调用c写的dll

## 用python调用c写的dll文件

- 导入动态链接库
    - 代码 ：
        
        ```
        from ctypes import windll # 首先导入 ctypes 模块的 windll 子模块
        somelibc = windll.LoadLibrary(some.dll) # 使用 windll 模块的 LoadLibrary 导入动态链接库
        ```
        
- 访问动态链接库中的函数
    - 代码
        
        ```
        somelibc. helloworld() # 这样就可以得到 some.dll 的 helloworld 的返回值
        
        
        ```
        

## 数据类型对照

### ctypes，c 语言和 Python 语言变量类型关系

| ctypes type | c type | Python type |
| --- | --- | --- |
| c\_char | char | 1-character string |
| c\_wchar | wchar\_t | 1-character unicode string |
| c\_byte | char | int/long |
| c\_ubyte | unsigned char | int/long |
| c\_short | short | int/long |
| c\_ushort | unsigned short | int/long |
| c\_int | int | int/long |
| c\_uint | unsigned int | int/long |
| c\_long | long | int/long |
| c\_ulong | unsigned long | int/long |
| c\_longlong | \_\_int64 or long long | int/long |
| c\_ulonglong | unsigned \_\_int64 or unsigned long long | int/long |
| c\_float | float | float |
| c\_double | double | float |
| c\_char\_p | char \* (NUL terminated) | string or None |
| c\_wchar\_p | wchar\_t \* (NUL terminated) | unicode or None |
| c\_void\_p | void \* | int/long or None |

### c其他类型

- - 指针类型代码
        - ```
            i = c_int(999) # 定义 int 类型变量 i，值为 999 
            pi = pointer(i)    # 定义指针，指向变量 i 
            pi.contents    # 打印指针所指的内容
            ```
            
    - 数组类型代码
        - ```
            class POINT(Structure):  # 定义一个结构，内含两个成员变量 x，y，均为 int 型
                _fields_ = [("x", c_int),
                    ("y", c_int)]
            
            ```
            
    - 结构体类型代码
        - ```
            pa = POINT_ARRAY(POINT(7, 7), POINT(8, 8), POINT(9, 9))
            ```
            

# 使用c写python的模块

## 步骤

1. 引入 Python.h 头文件。
2. 编写包装函数。
3. 函数中处理从python传入的参数
4. 实现逻辑功能
5. 处理c中的返回值，包装成python对象
6. 在一个 PyMethodDef 结构体中注册需要的函数。
7.  在一个初始化方法中注册模块名。
8.  把这个 C 源文件编译成链接库。

## 代码示例1

```
int add(int x, int y){
      return x + y;
  }
  
  //int main(void){
  //    printf("%d", add(1, 2));
  //    return 0;
  //}
  
  #include <Python.h>
  
  static PyObject* W_add(PyObject* self, PyObject* args){
      int x;
      int y;
      if(!PyArg_ParseTuple(args, "i|i", &x, &y)){
          return NULL;
      } else {
          return Py_BuildValue("i", add(x, y));
      }
  }
  
  static PyMethodDef ExtendMethods[] = {
      {"add", W_add, METH_VARARGS, "a function from C"},
      {NULL, NULL, 0, NULL},
  };
  
  PyMODINIT_FUNC initdemo(){
      Py_InitModule("demo", ExtendMethods);
  }


```
