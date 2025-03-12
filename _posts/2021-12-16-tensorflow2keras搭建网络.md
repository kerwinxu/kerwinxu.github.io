---
layout: post
title: "tensorflow2keras搭建网络"
date: "2021-12-16"
categories: 
  - "python"
---

六步：

1. import
2. train, test : 训练集，测试集
3. model = tf.keras.models.Sequential :  相当于走了一遍前向传播
    - 拉直层 ： tf.keras.layers.Flatten
    - 全连接层 ： tf.keras.layers.Dense(神经元个数, activation=激活函数, kerenl\_regularizer=正则化)
        - activation : relu , softmax , sigmod, tanh
        - kernel\_regularizer : tf.keras.regualrizer.l1(), tf.keras.regualrizer.l2()
    - 卷积层 ： tf.keras.layers.Conv2D(filters=卷积核个数,kernel\_size=卷积核尺寸,strides=卷积步长, padding="valid"or"same")
    - LSTM层 ： tf.keras,layers.LSTM
4. model.compile(optimizer=优化器， loss=损失函数,metries=评测指标)
    - 优化器
        - 'sgd' or tf.keras.optimizers.SGD(lr=学习率, momentum=动量参数)
        - 'adagrad' or tf.keras.optimizers.Adagrad(lr=学习率)
        - 'adadelta' or tf.keras.optimizers.Adadelta(lr=学习率)
        - 'adam' or tf.keras.optimizers.Adam(lr=学习率, beta\_1=0.9, beta\_2=0.999)
    - 损失函数
        - 'mse'
        - 'square\_categorical\_crossentropy
    - 评测指标
        - 'accuracy' : 数值的情况
        - 'categorical\_accuracy' : 都是独热码的情况
        - 'spuare\_categorical\_accuracy' : 结果y是数值，但实际y\_是独热码。
5. model.fit (训练集的输入特征，训练集的标签 batch\_size=每次喂入神经网络的样本数 , epochs=要迭代多少次数据集, validation\_data=(输入集的输入特征，测试集的标签) validation\_split=从训练集划分多少比例给测试集 validation\_freq= 多少次epochs测试一次)
6. model.summary : 打印网络结构和参数统计。
