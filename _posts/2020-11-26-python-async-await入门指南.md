---
layout: post
title: "Python Async/Await入门指南"
date: "2020-11-26"
categories: ["计算机语言", "Python"]
---

# 常见的几种python函数形式

1. 普通函数
    
    ```
    def function():
        return 1
    ```
    
2. 生成器函数
    
    ```
    def generator():
        yield 1
    ```
    
3. 异步函数（协程）
    
    ```
    async def async_function():
        return 1
    ```
    
4. 异步生成器
    
    ```
    async def async_generator():
        yield 1
    ```
    
     

通过类型判断可以验证函数的类型

```
import types
print(type(function) is types.FunctionType)
print(type(generator()) is types.GeneratorType)
print(type(async_function()) is types.CoroutineType)
print(type(async_generator()) is types.AsyncGeneratorType)
```

 

直接调用异步函数不会返回结果，而是返回一个coroutine对象：

```
print(async_function())
# <coroutine object async_function at 0x102ff67d8>
```

协程需要通过其他方式来驱动，因此可以使用这个协程对象的send方法给协程发送一个值：

```
print(async_function().send(None))

```

不幸的是，如果通过上面的调用会抛出一个异常：

```
StopIteration: 1

```

因为生成器/协程在正常返回退出时会抛出一个StopIteration异常，而原来的返回值会存放在StopIteration对象的value属性中，通过以下捕获可以获取协程真正的返回值：

```
try:
    async_function().send(None)
except StopIteration as e:
    print(e.value)
# 1
```

通过上面的方式来新建一个run函数来驱动协程函数：

```
def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value
```

在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果：

```
async def async_function():
    return 1

async def await_coroutine():
    result = await async_function()
    print(result)
    
run(await_coroutine())
# 1
```

要注意的是，await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误。

# 异步的例子

假如我要到一家超市去购买土豆，而超市货架上的土豆数量是有限的：

```
class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos

all_potatos = Potato.make(5)
```

现在我想要买50个土豆，每次从货架上拿走一个土豆放到篮子：

```
def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            sleep(.1)
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break

def buy_potatos():
    bucket = []
    for p in take_potatos(50):
        bucket.append(p)
```

对应到代码中，就是迭代一个生成器的模型，显然，当货架上的土豆不够的时候，这时只能够死等，而且在上面例子中等多长时间都不会有结果（因为一切都是同步的），也许可以用多进程和多线程解决，而在现实生活中，更应该像是这样的：

```
async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break
```

当货架上的土豆没有了之后，我可以询问超市请求需要更多的土豆，这时候需要等待一段时间直到生产者完成生产的过程：

```
async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))
```

当生产者完成和返回之后，这是便能从await挂起的地方继续往下跑，完成消费的过程。而这整一个过程，就是一个异步生成器迭代的流程：

```
async def buy_potatos():
    bucket = []
    async for p in take_potatos(50):
        bucket.append(p)
        print(f'Got potato {id(p)}...')
```

async for语法表示我们要后面迭代的是一个异步生成器。

```
def main():
    import asyncio
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(buy_potatos())
    loop.close()
```

用asyncio运行这段代码，结果是这样的：

```
Got potato 4338641384...
Got potato 4338641160...
Got potato 4338614736...
Got potato 4338614680...
Got potato 4338614568...
Got potato 4344861864...
Got potato 4344843456...
Got potato 4344843400...
Got potato 4338641384...
Got potato 4338641160...
...
```

既然是异步的，在请求之后不一定要死等，而是可以做其他事情。比如除了土豆，我还想买番茄，这时只需要在事件循环中再添加一个过程：

```
def main():
    import asyncio
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.wait([buy_potatos(), buy_tomatos()]))
    loop.close()
```

再来运行这段代码：

```
Got potato 4423119312...
Got tomato 4423119368...
Got potato 4429291024...
Got potato 4421640768...
Got tomato 4429331704...
Got tomato 4429331760...
Got tomato 4423119368...
Got potato 4429331760...
Got potato 4429331704...
Got potato 4429346688...
Got potato 4429346072...
Got tomato 4429347360...
...
```

 

# **await和yield from**

Python3.3的yield from语法可以把生成器的操作委托给另一个生成器，生成器的调用方可以直接与子生成器进行通信：

```
def sub_gen():
    yield 1
    yield 2
    yield 3

def gen():
    return (yield from sub_gen())

def main():
    for val in gen():
        print(val)
# 1
# 2
# 3
```

 

利用这一特性，使用yield from能够编写出类似协程效果的函数调用，在3.5之前，asyncio正是使用@asyncio.coroutine和yield from语法来创建协程：

```
# https://docs.python.org/3.4/library/asyncio-task.html
import asyncio

@asyncio.coroutine
def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    yield from asyncio.sleep(1.0)
    return x + y

@asyncio.coroutine
def print_sum(x, y):
    result = yield from compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
```

然而，用yield from容易在表示协程和生成器中混淆，没有良好的语义性，所以在Python 3.5推出了更新的async/await表达式来作为协程的语法。

因此类似以下的调用是等价的：

```
async with lock:
    ...
    
with (yield from lock):
    ...
######################
def main():
    return (yield from coro())

def main():
    return (await coro())
```

那么，怎么把生成器包装为一个协程对象呢？这时候可以用到types包中的coroutine装饰器（如果使用asyncio做驱动的话，那么也可以使用asyncio的coroutine装饰器），@types.coroutine装饰器会将一个生成器函数包装为协程对象：

```
import asyncio
import types

@types.coroutine
def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    yield from asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
```

尽管两个函数分别使用了新旧语法，但他们都是协程对象，也分别称作_native coroutine_以及_generator-based coroutine_，因此不用担心语法问题。

下面观察一个asyncio中Future的例子：

```
import asyncio

future = asyncio.Future()

async def coro1():
    await asyncio.sleep(1)
    future.set_result('data')

async def coro2():
    print(await future)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([
    coro1(), 
    coro2()
]))
loop.close()
```

两个协程在在事件循环中，协程coro1在执行第一句后挂起自身切到asyncio.sleep，而协程coro2一直等待future的结果，让出事件循环，计时器结束后coro1执行了第二句设置了future的值，被挂起的coro2恢复执行，打印出future的结果'data'。

 

 

引用

- [Python Async/Await入门指南](https://zhuanlan.zhihu.com/p/27258289)
