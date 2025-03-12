---
layout: post
title: "PyTroch常用API总结"
date: "2022-08-20"
categories: 
  - "python"
  - "pytorch"
---

# 张量创建

 

<table style="border-collapse: collapse; width: 100%; height: 240px;"><tbody><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.tensor()</td><td style="width: 68.3636%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.zeros()</td><td style="width: 68.3636%; height: 24px;">&nbsp;数据为0的</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.zeros_like()</td><td style="width: 68.3636%; height: 24px;">大小与inpurt的张量，但数据为0</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.ones()</td><td style="width: 68.3636%; height: 24px;">数据为1</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.ones_like()</td><td style="width: 68.3636%; height: 24px;">大小与inpurt的张量，但数据为1</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.full()</td><td style="width: 68.3636%; height: 24px;">torch.full(size, full_value) #</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.full_like()</td><td style="width: 68.3636%; height: 24px;">torch.full_like(input, full_value)</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.arange()</td><td style="width: 68.3636%; height: 24px;">torch.arange(start=0,end,step=1)</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.linspace()</td><td style="width: 68.3636%; height: 24px;">torch.linspace(start, end, steps=100, out=None) → Tensor ,steps (int) - 在start和end间生成的样本数</td></tr><tr style="height: 24px;"><td style="width: 18.9091%; height: 24px;">torch.eye()</td><td style="width: 68.3636%; height: 24px;">对角线位置全是1</td></tr><tr><td style="width: 18.9091%;">torch.normal()</td><td style="width: 68.3636%;">torch.normal (means, std, out=None)</td></tr><tr><td style="width: 18.9091%;">torch.randn()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.randn_like()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.rand()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.rand_like()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.randint()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.randint_like()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.randperm()</td><td style="width: 68.3636%;"></td></tr><tr><td style="width: 18.9091%;">torch.bernoulli()</td><td style="width: 68.3636%;"></td></tr></tbody></table>

# 张量操作

<table style="border-collapse: collapse; width: 100%; height: 288px;"><tbody><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.topk.html?highlight=torch%20topk#torch.topk">torch.topk(input, k, dim=None, largest=True, sorted=True, *, out=None)</a></td><td style="width: 32.3635%; height: 24px;">取得最大的k个元素</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.cat.html?highlight=torch%20cat#torch.cat">torch.cat(tensors, dim=0, *, out=None) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">拼接多个张量</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.stack.html?highlight=torch%20stack#torch.stack">torch.stack(tensors, dim=0, *, out=None) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">沿着一个新的维度对张量进行连接</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.chunk.html?highlight=torch%20chunk#torch.chunk">torch.chunk(input, chunks, dim=0) → List of Tensors</a></td><td style="width: 32.3635%; height: 24px;">将一个张量分成指定数量的块</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.split.html?highlight=torch%20split#torch.split">torch.split(tensor, split_size_or_sections, dim=0)</a></td><td style="width: 32.3635%; height: 24px;">将张量分成几块。</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.index_select.html?highlight=torch%20index_selec">torch.index_select(input, dim, index, *, out=None) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">使用索引中的维度和张量选择</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.masked_select.html?highlight=torch%20masked_select#torch.masked_select">torch.masked_select(input, mask, *, out=None) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">得到一个布尔张量</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.reshape.html?highlight=torch%20reshape#torch.reshape">torch.reshape(input, shape) → Tensor</a></td><td style="width: 32.3635%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.transpose.html?highlight=torch%20transpose#torch.transpose">torch.transpose(input, dim0, dim1) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">转置版本</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.t.html#torch.t">torch.t(input) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">上边的特殊版本，torch.transpose(input,0,1)</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.squeeze.html?highlight=torch%20squeeze#torch.squeeze">torch.squeeze(input, dim=None, *, out=None) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">去掉所有大小为1的输入维度。</td></tr><tr style="height: 24px;"><td style="width: 58.6667%; height: 24px;"><a href="https://pytorch.org/docs/stable/generated/torch.unsqueeze.html?highlight=torch%20unsqueeze#torch.unsqueeze">torch.unsqueeze(input, dim) → Tensor</a></td><td style="width: 32.3635%; height: 24px;">在指定的维度上插入一个维数为1的维度</td></tr></tbody></table>

 

# 张量运算

 

# 自动求导

## torch.autograd.backward

```
torch.autograd.backward(tensors, grad_tensors=None, retain_graph=None, create_graph=False, grad_variables=None, inputs=None)
```

参数

- tensors ： 用于计算梯度的tensor ，torch.autograd.backward(z) == z.backward()
- grad\_tensors: 在计算矩阵的梯度时会用到。他其实也是一个tensor，shape一般需要和前面的tensor保持一致。
- retain\_graph: 通常在调用一次backward后，pytorch会自动把计算图销毁，所以要想对某个变量重复调用backward，则需要将该参数设置为True
- create\_graph: 当设置为True的时候可以用来计算更高阶的梯度
- grad\_variables: 这个官方说法是grad\_variables' is deprecated. Use 'grad\_tensors' instead.也就是说这个参数后面版本中应该会丢弃，直接使用grad\_tensors就好了

关于参数grad\_tensors:

```
x = torch.ones(2,requires_grad=True)
z = x + 2
z.backward(torch.ones_like(z)) # grad_tensors需要与输入tensor大小一致
print(x.grad)

>>> tensor([1., 1.])
```

 

## torch.autograd.grad

这个是求求导数的

```
torch.autograd.grad(
    outputs, 
    inputs, 
    grad_outputs=None, 
    retain_graph=None, 
    create_graph=False, 
    only_inputs=True, 
    allow_unused=False)
```

- outputs: 求导的因变量
- inputs: 求导的自变量
- grad\_outputs: 类似于backward方法中的grad\_tensors
- retain\_graph: 同上
- create\_graph: 同上
- only\_inputs: 默认为True, 如果为True, 则只会返回指定input的梯度值。 若为False，则会计算所有叶子节点的梯度，并且将计算得到的梯度累加到各自的.grad属性上去。
- allow\_unused: 默认为False, 即必须要指定input,如果没有指定的话则报错。

 

# 数据预处理

transforms.Normalize 裁剪 transforms.CenterCrop transforms.RandomCrop transforms.RandomResizedCrop FiveCrop and TenCrop 旋转和翻转 图像变换 transform的操作

 

# 模型容器

## nn.Sequential

一个有序的容器

```
# 两种方式，
# 一种是作为有序的容器
model = nn.Sequential(
          nn.Conv2d(1,20,5),
          nn.ReLU(),
          nn.Conv2d(20,64,5),
          nn.ReLU()
        )
# 第二种是有序的字典，
model = nn.Sequential(OrderedDict([
         ('conv1', nn.Conv2d(1,20,5)),
         ('relu1', nn.ReLU()),
         ('conv2', nn.Conv2d(20,64,5)),
         ('relu2', nn.ReLU())
       ]))
```

 

## nn.ModuleList

它被设计用来存储任意数量的nn. module。

### 什么时候用？

如果在构造函数\_\_init\_\_中用到list、tuple、dict等对象时，一定要思考是否应该用ModuleList或ParameterList代替。

### 和list的区别？

ModuleList是Module的子类，当在Module中使用它的时候，就能自动识别为子module。

当添加 nn.ModuleList 作为 nn.Module 对象的一个成员时（即当我们添加模块到我们的网络时），所有 nn.ModuleList 内部的 nn.Module 的 parameter 也被添加作为 我们的网络的 parameter。

但ModuleList不自动实现前向传播，nn.Sequential中的是自动有前向传播。

nn.ModuleList，它是一个储存不同 module，并自动将每个 module 的 parameters 添加到网络之中的容器。你可以把任意 nn.Module 的子类 (比如 nn.Conv2d, nn.Linear 之类的) 加到这个 list 里面，方法和 Python 自带的 list 一样，无非是 extend，append 等操作。但不同于一般的 list，加入到 nn.ModuleList 里面的 module 是会自动注册到整个网络上的，同时 module 的 parameters 也会自动添加到整个网络中。

```
class net_modlist(nn.Module):
    def __init__(self):
        super(net_modlist, self).__init__()
        self.modlist = nn.ModuleList([
                       nn.Conv2d(1, 20, 5),
                       nn.ReLU(),
                        nn.Conv2d(20, 64, 5),
                        nn.ReLU()
                        ])

    def forward(self, x):
        for m in self.modlist:
            x = m(x)
        return x

net_modlist = net_modlist()
print(net_modlist)
#net_modlist(
#  (modlist): ModuleList(
#    (0): Conv2d(1, 20, kernel_size=(5, 5), stride=(1, 1))
#    (1): ReLU()
#    (2): Conv2d(20, 64, kernel_size=(5, 5), stride=(1, 1))
#    (3): ReLU()
#  )
#)

for param in net_modlist.parameters():
    print(type(param.data), param.size())
#<class 'torch.Tensor'> torch.Size([20, 1, 5, 5])
#<class 'torch.Tensor'> torch.Size([20])
#<class 'torch.Tensor'> torch.Size([64, 20, 5, 5])
#<class 'torch.Tensor'> torch.Size([64])
```

## nn.ModuleDict

ModuleDict 可以像常规的Python字典一样对ModuleDict进行索引，但是其中包含的模块已正确注册，并且对所有 Module 方法都是可见的。

```
class MyModule(nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.choices = nn.ModuleDict({
                'conv': nn.Conv2d(10, 10, 3),
                'pool': nn.MaxPool2d(3)
        })
        self.activations = nn.ModuleDict([
                ['lrelu', nn.LeakyReLU()],
                ['prelu', nn.PReLU()]
        ])

    def forward(self, x, choice, act):
        x = self.choices[choice](x)
        x = self.activations[act](x)
        return x
```

 

# 模型构建

## nn.Conv2d

```
CLASStorch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)
```

- in\_channels (int) – Number of channels in the input image
- out\_channels (int) – Number of channels produced by the convolution
- kernel\_size (int or tuple) – Size of the convolving kernel
- stride (int or tuple, optional) – Stride of the convolution. Default: 1
- padding (int, tuple or str, optional) – Padding added to all four sides of the input. Default: 0
- padding\_mode (string, optional) – 'zeros', 'reflect', 'replicate' or 'circular'. Default: 'zeros'
- dilation (int or tuple, optional) – Spacing between kernel elements. Default: 1
- groups (int, optional) – Number of blocked connections from input channels to output channels. Default: 1
- bias (bool, optional) – If True, adds a learnable bias to the output. Default: True

 

## nn.Conv3d

```
class torch.nn.Conv3d(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True)
```

**Parameters：**

- in\_channels(`int`) – 输入信号的通道
- out\_channels(`int`) – 卷积产生的通道
- kernel\_size(`int` or `tuple`) - 卷积核的尺寸
- stride(`int` or `tuple`, `optional`) - 卷积步长
- padding(`int` or `tuple`, `optional`) - 输入的每一条边补充0的层数
- dilation(`int` or `tuple`, `optional`) – 卷积核元素之间的间距
- groups(`int`, `optional`) – 从输入通道到输出通道的阻塞连接数
- bias(`bool`, `optional`) - 如果`bias=True`，添加偏置

三维卷积层, 输入的尺度是(N, C\_in,D,H,W)，输出尺度（N,C\_out,D\_out,H\_out,W\_out）

**shape:**  
`input`: (N,C\_in,D\_in,H\_in,W\_in)  
`output`: (N,C\_out,D\_out,H\_out,W\_out)

注意：3D卷积的输入是**5维的tensor**

nn.ConvTranspose2d

## nn.MaxPool2d

最大池化层

```
torch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
```

 

## nn.AvgPool2d

平均池化层

 

## nn.MaxUnpool2d

## nn.Linear

全连接层

```
CLASStorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)
```

- in\_features – size of each input sample
- out\_features – size of each output sample
- bias – If set to False, the layer will not learn an additive bias. Default: True

 

## nn.Sigmoid

[![](/assets/image/default/Sigmoid.png)](http://127.0.0.1/?attachment_id=4707)

- Input: (\*)(∗), where \*∗ means any number of dimensions.
- Output: (\*)(∗), same shape as the input.

```
m = nn.Sigmoid()
input = torch.randn(2)
output = m(input)
```

## nn.ReLU

 

[![](/assets/image/default/ReLU.png)](http://127.0.0.1/?attachment_id=4706)

## nn.tanh

[![](/assets/image/default/Tanh.png)](http://127.0.0.1/?attachment_id=4708)

## nn.Sigmoid nn.tanh 区别

[![](/assets/image/default/v2-f190fdedc174f080f2e4bdd56ed504a1_720w.jpg)](http://127.0.0.1/?attachment_id=4709)

 

从数学上看，这两个函数可以通过线性变化等价，唯一的区别在于值域是 (0,1) 和 (-1, 1)。作为激活函数，都存在两端梯度弥散、计算量大的问题，sigmoid函数因为和生物上的神经元信号刺激的 firing rate 长得像，一度比较流行。。。但是，作为非中心对称的激活函数，sigmoid有个问题：输出总是正数！！！

 

# 损失函数

<table style="border-collapse: collapse; width: 100%; height: 536px;"><tbody><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.CrossEntropyLoss()</td><td style="width: 76.0607%; height: 24px;">交叉熵损失函数</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.NLLLoss</td><td style="width: 76.0607%; height: 24px;">softmax(x)+log(x)+nn.NLLLoss====&gt;nn.CrossEntropyLoss</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 80px;"><td style="width: 23.9393%; height: 80px;">nn.BCELoss</td><td style="width: 76.0607%; height: 80px;">用于计算预测值和真实值之间的二元交叉熵损失(Binary Cross Entropy) 主要用于多标记任务（一个样本对应多个类别）</td><td style="width: 0.848485%; height: 80px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.BCEWithLogitsLoss</td><td style="width: 76.0607%; height: 24px;">只是在BCELoss上加了个logits函数(也就是sigmoid函数)</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.L1Loss</td><td style="width: 76.0607%; height: 24px;">计算网络输出与标签之差的绝对值</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.MSELoss</td><td style="width: 76.0607%; height: 24px;">均方误差</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.SmoothL1Loss</td><td style="width: 76.0607%; height: 24px;">如果绝对元素误差低于 beta，则创建使用平方项的标准，否则使用 L1 项</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 48px;"><td style="width: 23.9393%; height: 48px;">nn.PoissonNLLLoss</td><td style="width: 76.0607%; height: 48px;">真实标签服从泊松分布的负对数似然损失，神经网络的输出作为泊松分布的参数$latex \lambda $</td><td style="width: 0.848485%; height: 48px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.KLDivLoss</td><td style="width: 76.0607%; height: 24px;">用于连续分布的距离度量；并且对离散采用的连续输出空间分布进行回归通常很有用</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.MarginRankingLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.MultiLabelMarginLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.SoftMarginLoss</td><td style="width: 76.0607%; height: 24px;">针对二分类问题</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.MultiLabelSoftMarginLoss</td><td style="width: 76.0607%; height: 24px;">多标签交叉熵损失函数</td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.MultiMarginLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.TripletMarginLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.HingeEmbeddingLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.CosineEmbeddingLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;">nn.CTCLoss</td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr><tr style="height: 24px;"><td style="width: 23.9393%; height: 24px;"></td><td style="width: 76.0607%; height: 24px;"></td><td style="width: 0.848485%; height: 24px;"></td></tr></tbody></table>

 

# 优化器

Optimizer .zero\_grad() .step() .add\_param\_group() .state\_dick() or .load\_state\_dick optim.SGD

 

# 模型加载和保存

torch.save torch.load

 

# 引用

- [torch.stack()函数](https://blog.csdn.net/weixin_39504171/article/details/106074550)
