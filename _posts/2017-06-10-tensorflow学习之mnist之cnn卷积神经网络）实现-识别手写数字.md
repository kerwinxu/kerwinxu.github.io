---
layout: post
title: "tensorflow学习之MNIST之CNN卷积神经网络）实现-识别手写数字"
date: "2017-06-10"
categories: 
  - "python"
---

全部源代码实现：

 

```
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:29:36 2017

@author: kerwin
"""

# -*- coding: utf-8 -*-
"""
# Last Change:  2017-06-10 15:57:42
Created on Fri Jun  2 20:28:53 2017

@author: kerwin
"""
# 识别手写数字，用cnn（卷积神经网络）实现

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 建立抽象模型
#  z = Wx+b ：加权求和加上偏置量
#  a = softmax(z) ： 根据证据求概率
x = tf.placeholder(tf.float32, [None, 784])  # 输入占位符（输入的图片）
y = tf.placeholder(tf.float32, [None, 10])   # 输出占位符（预期输出）

#定义四个函数，分别用于初始化权值W，初始化偏置项b, 构建卷积层和构建池化层
#定义一个函数，用于初始化所有的权值 W
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

#定义一个函数，用于初始化所有的偏置项 b
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)
  
#定义一个函数，用于构建卷积层
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

#定义一个函数，用于构建池化层
def max_pool(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME')


# 构建网络
x_image = tf.reshape(x, [-1,28,28,1])         #转换输入数据shape,以便于用于网络中
W_conv1 = weight_variable([5, 5, 1, 32])      
b_conv1 = bias_variable([32])       
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)     #第一个卷积层
h_pool1 = max_pool(h_conv1)                                  #第一个池化层

W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)      #第二个卷积层
h_pool2 = max_pool(h_conv2)                                   #第二个池化层

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])              #reshape成向量
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)    #第一个全连接层

keep_prob = tf.placeholder("float") 
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)                  #dropout层

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_predict=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)   #softmax层


# 定义损失函数和训练方法
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(y_predict), reduction_indices=[1]))  # 损失函数为交叉熵
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
# 可以看到这样以来，模型中的所有元素(图结构，损失函数，下降方法和训练目标)都已经包括在train里面。
# 我们可以把train叫做训练模型。

correct_prediction = tf.equal(tf.argmax(y_predict, 1), tf.argmax(y, 1))
# ，tf.argmax表示找到最大值的位置(也就是预测的分类和实际的分类)，
# 然后看看他们是否一致，是就返回true,不是就返回false,这样得到一个boolean数组
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# tf.cast将boolean数组转成int数组，最后求平均值，得到分类的准确率(怎么样，是不是很巧妙)

# 如下是建立一个会话训练神经网络
sess = tf.InteractiveSession()               # 建立交互式会话
sess.run(tf.global_variables_initializer())  # 所有变量初始化
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)    # 获得一批100个数据
    train_step.run({x: batch_xs, y: batch_ys, keep_prob: 1.0})               # 给训练模型提供输入和输出

# 测试数据的
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0}))


```

这个代码识别率只有97%，达不到别人说的99%，且运行速度真慢。
