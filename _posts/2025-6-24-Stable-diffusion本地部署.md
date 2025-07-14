---
layout: post
title: "Stable-diffusion本地部署"
date: "2025-06-24"
categories: ["构建"]
math: true
---

# 前提
1. 安装python,最好是3.10.6版本，我的是3.9版本，需要修改代码。
1. 安装git

# 下载
```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui --depth=1
```
我只下载最新的

# 安装
运行webui-user.bat,我的只是cpu版本，编辑webui-user.bat，需要修改文件中的内容如下
```
set COMMANDLINE_ARGS=--skip-torch-cuda-test --precision full  --no-half 
```
接下来就是等待，

# 模型安装
我是用 huggingface-cli 进行模型安装的，
```
pip install huggingface_hub
```

然后换成国内源，添加环境变量 HF_ENDPOINT = https://hf-mirror.com  
下载范例，模型安装目录在"models/Stable-diffusion"，每个模型项目一个目录，
```
 huggingface-cli download admruul/anything-v3.0 --local-dir anything-v3.0
```


# 模型



## CheckPoint大模型


## Unet模型


## VAE模型

变分自编码器（VAE）是一种生成模型，其基本思路是通过编码器将真实样本转换为理想的数据分布，然后通过解码器生成样本.


## LoRA 模型
放在"models\Lora"文件夹,应用是 "\<lora:filename:multiplier\>",其中filename是文件名，multiplier是权重，

|名称|说明|
|--|--|
|andrewzhu/MoXinV1|工笔画风格|
|Jovie/Miyazaki|宫崎骏风格|


## ControlNet模型



# 插件

## ControlNet
### 网址 
[https://github.com/Mikubill/sd-webui-controlnet.git](https://github.com/Mikubill/sd-webui-controlnet.git)

### 其他安装
进入"venv\Scripts"文件夹，打开终端，运行activate，然后运行
```
pip install controlnet_aux
```

### 模型
是根据模型来控制的，这里还要下载模型,模型放在 "extensions\sd-webui-controlnet\models"文件夹中。
```
cd extensions\sd-webui-controlnet\models
 huggingface-cli download lllyasviel/ControlNet-v1-1 --local-dir ./
```
这里边有很多v1.5的模型


控制模型
### 控制模型 Openpose

网址 "lllyasviel/ControlNet-v1-1",放在"models\ControlNet”中。
```
cd models\ControlNet
 huggingface-cli download lllyasviel/ControlNet-v1-1 --local-dir ControlNet
```


### 预处理器 Annotator
从图片中提取对 ControlNet 有用的信息，网址"lllyasviel/Annotators",放在"extensions\sd-webui-controlnet\annotator\downloads\openpose"中。

```
cd extensions\sd-webui-controlnet\annotator\downloads
 huggingface-cli download lllyasviel/Annotators --local-dir openpose
```






# 已知问题

## OSError: [WinError 123] 文件名、目录名或卷标语法不正确
解决,这个是因为python3.9，修改"venv\Lib\site-packages\gradio\utils.py"  
```python
def abspath(path: str | Path) -> Path:
    """Returns absolute path of a str or Path path, but does not resolve symlinks."""
    # 添加如下的，只是取得问号前面的
    if isinstance(path, str):
        path=path.split('?')[0]
    
    path = Path(path)

```

# 引用
   - [超全 Stable Diffusion 常用模型推荐（含网盘下载链接）](https://zhuanlan.zhihu.com/p/28932301846)



