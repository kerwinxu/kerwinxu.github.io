---
layout: post
title: "tensorflow学习之MNIST-识别手写数字"
date: "2017-06-10"
categories: 
  - "python"
---

这个MNIST相当于tensorflow的hello word了。 首先下载数据集：

```
import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

```

这就下载了数据集了，下载的数据集分成2部分

1. mnist.train，60000行的训练数据集
2. mnist.test，10000行的测试数据集

每个MNIST数据单元由2部分组成，

1. 图片，比如训练数据集的图片是 mnist.train.images，这个图片是28\*28像素的，展开的话相当于784个元素的向量。mnist.train.images 是一个形状为 \[60000, 784\] 的张量，第一个维度数字用来索引图片，第二个维度数字用来索引每张图片中的像素点。
2. 标签，比如训练数据集的标签是 mnist.train.labels，mnist.train.labels 是一个 \[60000, 10\] 的数字矩阵

Softmax回归介绍：softmax用来给不同的对象分配概率。分3步

1. 为了得到一张图片属于某个特定类的证据，我们对图片像素值进行加权求和，如果某个图片的像素具有很强的证据证明不属于该类，那么相应的权值为负数，相反如果某个像素拥有用力的证据证明属于该类，那么相应的权值为正数。红色代表负数权值，蓝色代表正数权值，比如说0，可以看到中间为负数，周围为正数。z\=Wx ![]
2. 我们也需要一个额外的偏置量来过滤无关的干扰量。z\=Wx+b
3. 然后利用softmax来把这些证据转化为概率，比如说这个图片的数字为9个的概率为80%，为8个的概率为50%之类的。a\=softmax(z)

公式总结起来就是

        z\=Wx+b ：加权求和加上偏置量

        a\=softmax(z) ： 根据证据求概率

如上抽象模型的代码为：

```
# 建立抽象模型
x = tf.placeholder(tf.float32, [None, 784]) # 输入占位符，输入的图片。
y = tf.placeholder(tf.float32, [None, 10])  # 输出占位符（预期输出，就是图片的标签）
W = tf.Variable(tf.zeros([784, 10]))        # 加权求和的w
b = tf.Variable(tf.zeros([10]))             # 偏置量
a = tf.nn.softmax(tf.matmul(x, W) + b)      # a表示模型的实际输出
```

然后先小结一下，公式合起来是a\=softmax(Wx+b)，其中x是输入的图片，W是我们要求的变量（加权），b也是我们要求的变量（偏置量），a为实际的输出，a要跟y（预期的输出）比较。

如下是损失函数和训练方法，损失函数为交叉熵，-y\*log(a),值越小，表明这个不同的概率越低，越准确。

如下是交叉熵，主要用于度量两个概率分布间的差异性信息。

1. 交叉熵是表示两个概率分布p,q，其中p表示真实分布，q表示非真实分布，在相同的一组事件中，其中，用非真实分布q来表示某个事件发生所需要的平均比特数。
2. 按照真实分布p来衡量识别一个样本所需要的编码长度的期望为：![]
3. 但是，如果采用错误的分布q来表示来自真实分布p的平均编码长度，则应该是：![]
4. 此时就将H(p,q)称之为交叉熵。
5. 套用在上边就是y\*log(1/a)= -y\*log(a)

这个交叉熵就将y（预期输出）和a（实际输出）结合起来了，

```
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(a), reduction_indices=[1])) # 损失函数为交叉熵
```

现在，这个交叉熵只是判断是否要达到目标，还需要一个优化器来通过不断的计算来达到目标，这里用梯度下降法(gradient descent)，是一个最优化算法，通常也称为最速下降法。常用于机器学习和人工智能当中用来递归性地逼近最小偏差模型。

代码如下：

 

```
optimizer = tf.train.GradientDescentOptimizer(0.5) # 梯度下降法，学习速率为0.5
train = optimizer.minimize(cross_entropy)  # 训练目标：最小化损失函数

```

到此，模型就搞定了 代码如下：

```
# 建立抽象模型
x = tf.placeholder(tf.float32, [None, 784]) # 输入占位符（输入的图片）
y = tf.placeholder(tf.float32, [None, 10])  # 输出占位符（预期输出）
W = tf.Variable(tf.zeros([784, 10]))        # 加权求和的
b = tf.Variable(tf.zeros([10]))             # 偏置量
a = tf.nn.softmax(tf.matmul(x, W) + b)      # a表示模型的实际输出

# 定义损失函数和训练方法
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(a), reduction_indices=[1])) # 损失函数为交叉熵
optimizer = tf.train.GradientDescentOptimizer(0.5) # 梯度下降法，学习速率为0.5
train = optimizer.minimize(cross_entropy)  # 训练目标：最小化损失函数

```

可以看到这样以来，模型中的所有元素(图结构，损失函数，下降方法和训练目标)都已经包括在train里面。我们可以把train叫做**训练模型**。

如上是全部模型，然后开始训练。建立会话进行训练啦

```
sess = tf.InteractiveSession()      # 建立交互式会话
tf.initialize_all_variables().run() # 所有变量初始化
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)    # 获得一批100个数据
    train.run({x: batch_xs, y: batch_ys})   # 给训练模型提供输入和输出
print(sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels}))

```

测试模型

```
correct_prediction = tf.equal(tf.argmax(a, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

```

tf.argmax表示找到最大值的位置(也就是预测的分类和实际的分类)，然后看看他们是否一致，是就返回true,不是就返回false,这样得到一个boolean数组。 tf.cast将boolean数组转成int数组，最后求平均值，得到分类的准确率(怎么样，是不是很巧妙),

想要查看到实际输出和预期输出的代码如下：

```
# 如下是显示识别的和期望的数字。
x1, y1 = mnist.train.next_batch(20)
a1 = sess.run(a, feed_dict={x: x1})
print(sess.run(tf.argmax(a1, 1)))
print(sess.run(tf.argmax(y1, 1)))
```

全部代码：

 

```
# -*- coding: utf-8 -*-
"""
# Last Change:  2017-06-10 15:45:30
Created on Fri Jun  2 20:28:53 2017

@author: kerwin
"""
# 识别手写数字

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 建立抽象模型
#  z = Wx+b ：加权求和加上偏置量
#  a = softmax(z) ： 根据证据求概率
x = tf.placeholder(tf.float32, [None, 784])  # 输入占位符（输入的图片）
y = tf.placeholder(tf.float32, [None, 10])   # 输出占位符（预期输出）
W = tf.Variable(tf.zeros([784, 10]))         # 加权求和的
b = tf.Variable(tf.zeros([10]))              # 偏置量
a = tf.nn.softmax(tf.matmul(x, W) + b)       # a表示模型的实际输出

# 定义损失函数和训练方法
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(a), reduction_indices=[1]))  # 损失函数为交叉熵
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 梯度下降法，学习速率为0.5
train = optimizer.minimize(cross_entropy)  # 训练目标：最小化损失函数
# 可以看到这样以来，模型中的所有元素(图结构，损失函数，下降方法和训练目标)都已经包括在train里面。
# 我们可以把train叫做训练模型。

correct_prediction = tf.equal(tf.argmax(a, 1), tf.argmax(y, 1))
# ，tf.argmax表示找到最大值的位置(也就是预测的分类和实际的分类)，
# 然后看看他们是否一致，是就返回true,不是就返回false,这样得到一个boolean数组
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# tf.cast将boolean数组转成int数组，最后求平均值，得到分类的准确率(怎么样，是不是很巧妙)

# 如下是建立一个会话训练神经网络
sess = tf.InteractiveSession()               # 建立交互式会话
sess.run(tf.global_variables_initializer())  # 所有变量初始化
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)    # 获得一批100个数据
    train.run({x: batch_xs, y: batch_ys})               # 给训练模型提供输入和输出

# 测试数据的
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))

# 如下是显示识别的和期望的数字。
x1, y1 = mnist.train.next_batch(20)
a1 = sess.run(a, feed_dict={x: x1})
print(sess.run(tf.argmax(a1, 1)))
print(sess.run(tf.argmax(y1, 1)))
```

可以看到训练网络的x和y数据集是mnist.train中的，而测试网路的x和y是mnist.test。
