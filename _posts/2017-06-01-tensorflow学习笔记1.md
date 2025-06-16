---
layout: post
title: "tensorflow学习笔记1"
date: "2017-06-01"
categories: ["计算机语言", "Python"]
---

1. tensorflow运行流程：主要分2步，构造模型和训练。构造模型，需要构造一个图来描述我们的模型，所谓图，就好比流程图，就是将数据的输入->中间处理->输出的过程表示出来。构造模型不会发生实际的运算，到训练阶段，才会有实际的数据输入，运算等。
    1. 概念描述。
        1. Tensor，张量，tensorflow用Tensor数据结构来保存所有的数据。
            1. 、生成张量方式1： a = tf.zeros(shape=\[1,2\]) ， shape为张量的维度和大小。
            2. 生成蟑螂方式2：
            3. 生成张量的时候，没有实际赋值，训练的时候，才有实际的值。
        2. Variable，变量，一般用来表示图种的各个计算参数。
            1. 生成变量方式1：W = tf.Variable(tf.zeros(shape=\[1,2\]))，只用一个Tensor也是可以的。
            2. 注意 ： 生成变量后，还有初始化才能有具体的值，tf.global\_variables\_initializer() ，现在这个版本得用这个了。而不是initialize\_all\_variables
            3. 通常会将统计模型中的参数作为变量，例如, 你可以将一个神经网络的权重作为某个变量存储在一个 tensor 中. 在训练过程中, 通过重复运行训练图, 更新这个 tensor.
        3. Feed ，Tensor以变量或者常量的形式存储，Tensorflow提供了Feed机制，可以临时替换途中的任意操作中Tensor，可以对图中的任意操作提交补丁，直接插入Tensor。
        4. placeholder ，占位符，抽象的概念，用于表示输入输出数据的格式。只是告诉系统，这里有一个值/向量/矩阵，没有具体的值，运行的时候会补上。
            1. x = tf.placeholder(tf.float32,\[1, 5\],name='input') #类型是float，1表示1维，5表示5个数据，也就是一个向量。
            2. y = tf.placeholder(tf.float32,\[None, 5\],name='input') ，None表示维数未知，tensorflow会自动处理。
        5. Session，会话。抽象模型的实现者。
    2. 模型构建：
        1. 我觉得吧，这个就是先表示各种Tensor，placeholder，然后用各种运算，比如乘法用tf.matmul，加法用tf.add等等。
    3. 综述：
        1. 使用图（graph）来表示计算任务。
        2. 在会话（session）中执行图。
        3. 使用张量（tensor）表示数据。
        4. 使用变量（variable）表示状态。
        5. fetch从中获取数据。可以在使用 Session 对象的 run() 调用 执行图时, 传入一些 tensor, 这些 tensor 会帮助你取回结果
        6. 使用feed可以为任意操作赋值。可以临时替代图中的任意操作中的 tensor 可以对图中任何操作提交补丁, 直接插入一个 tensor.
