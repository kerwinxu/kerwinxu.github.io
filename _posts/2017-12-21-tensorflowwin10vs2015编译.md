---
layout: post
title: "tensorflow,win10,vs2015编译"
date: "2017-12-21"
categories: ["构建"]
---

# 在 Windows 环境中从源代码构建

我们将从源代码构建 TensorFlow pip 软件包并将其安装在 Windows 设备上。

**注意**：我们已经针对 Windows 系统提供了经过精密测试的预构建 [TensorFlow 软件包](https://tensorflow.google.cn/install/pip)。

## Windows 设置

安装以下构建工具以配置 Windows 开发环境。

### 安装 Python 和 TensorFlow 软件包依赖项

安装[适用于 Windows 的 Python 3.5.x 或 Python 3.6.x 64 位版本](https://www.python.org/downloads/windows/)。选择 pip 作为可选功能，并将其添加到 `%PATH%` 环境变量中。

安装 TensorFlow pip 软件包依赖项：

```
pip3 install six numpy wheel
```

这些依赖项列在 `REQUIRED_PACKAGES` 下的 [`setup.py`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/pip_package/setup.py) 文件中。

### 安装 Bazel

[安装 Bazel](https://docs.bazel.build/versions/master/install-windows.html)，它是用于编译 TensorFlow 的构建工具。

将 Bazel 可执行文件的位置添加到 `%PATH%` 环境变量中。

### 安装 MSYS2

为构建 TensorFlow 所需的 bin 工具[安装 MSYS2](https://www.msys2.org/)。如果 MSYS2 已安装到 `C:\msys64` 下，请将 `C:\msys64\usr\bin` 添加到 `%PATH%` 环境变量中。然后，使用 `cmd.exe` 运行以下命令：

```
pacman -S git patch unzip

```

### 安装 Visual C++ 生成工具 2015

因为兼容性问题，vc2017跟cuda不怎么兼容，所以这里最好是用vc2015

安装 Visual C++ 生成工具 2015。此软件包随附在 Visual Studio 2015 中，但可以单独安装：

1. 转到 [Visual Studio 下载页面](https://visualstudio.microsoft.com/vs/older-downloads/)，
2. 选择“可再发行组件和生成工具”，
3. 下载并安装：
    - _Microsoft Visual C++ 2015 Redistributable 更新 3_
    - _Microsoft 生成工具 2015 更新 3_

**注意**：TensorFlow 针对 Visual Studio 2015 更新 3 进行了测试。

### 安装 GPU 支持（可选）

要安装在 GPU 上运行 TensorFlow 所需的驱动程序和其他软件，请参阅 Windows [GPU 支持](https://tensorflow.google.cn/install/gpu)指南。

### 下载 TensorFlow 源代码

使用 [Git](https://git-scm.com/) 克隆 [TensorFlow 代码库](https://github.com/tensorflow/tensorflow)（`git` 随 MSYS2 一起安装）：

```
git clone https://github.com/tensorflow/tensorflow.git
```

代码库默认为 `master` 开发分支。您也可以检出要构建的[版本分支](https://github.com/tensorflow/tensorflow/releases)：

```
git checkout branch_name# r1.9, r1.10, etc.

```

**要点**：如果您在使用最新的开发分支时遇到构建问题，请尝试已知可用的版本分支。

## 配置构建

通过在 TensorFlow 源代码树的根目录下运行以下命令来配置系统构建：

```
python ./configure.py

```

此脚本会提示您指定 TensorFlow 依赖项的位置，并要求指定其他构建配置选项（例如，编译器标记）。以下代码展示了 `python ./configure.py` 的示例运行会话（您的会话可能会有所不同）：

#### 查看示例配置会话

```
python ./configure.py
Starting local Bazel server and connecting to it...
................
You have bazel 0.15.0 installed.
Please specify the location of python. [Default is C:\python36\python.exe]:

Found possible Python library paths:
  C:\python36\lib\site-packages
Please input the desired Python library path to use.  Default is [C:\python36\lib\site-packages]

Do you wish to build TensorFlow with CUDA support? [y/N]: Y
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use. [Leave empty to default to CUDA 9.0]:

Please specify the location where CUDA 9.0 toolkit is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]:

Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 7.0]: 7.0

Please specify the location where cuDNN 7 library is installed. Refer to README.md for more details. [Default is C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0]: C:\tools\cuda

Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size. [Default is: 3.5,7.0]: 3.7

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is /arch:AVX]:

Would you like to override eigen strong inline for some C++ compilation to reduce the compilation time? [Y/n]:
Eigen strong inline overridden.

Configuration finished

```

## 需要更改的

问题：

- socket问题，解决方式：
    - 修改 tensorflow\\core\\platform\\cloud\\gcs\_dns\_cache.cc 文件，修改成如下的，winsock2在上边。 #include <winsock2.h> #include <Windows.h>

### 配置选项

对于 [GPU 支持](https://tensorflow.google.cn/install/gpu)，请指定 CUDA 和 cuDNN 的版本。如果您的系统安装了多个 CUDA 或 cuDNN 版本，请明确设置版本而不是依赖于默认版本。`./configure.py` 会创建指向系统 CUDA 库的符号链接，因此，如果您更新 CUDA 库路径，则必须在构建之前再次运行此配置步骤。

**注意**：从 TensorFlow 1.6 开始，二进制文件使用 AVX 指令，这些指令可能无法在旧版 CPU 上运行。

## 构建 pip 软件包

### Bazel 构建

请注意，编译的时候，电脑不要做其他事情，因为内存不够啊，如果做其他的事情，会出现莫名其妙的问题。

#### 仅支持 CPU

使用 `bazel` 构建仅支持 CPU 的 TensorFlow 软件包构建器：

```
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package

```

#### GPU 支持

要构建支持 GPU 的 TensorFlow 软件包构建器，请运行以下命令：

```
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package

```

#### Bazel 构建选项

注意要加上 /arch:AVX2 ， 不加上的话，编译出来的不支持AVX2，我试过在配置中加上这个也没用，只能在bazel中加。

从源代码构建 TensorFlow 可能会消耗大量内存。如果系统内存有限，请使用以下命令限制 Bazel 的内存消耗量：`--local_resources 2048,.5,1.0`。

如果构建支持 GPU 的 TensorFlow，请添加 `--copt=-nvcc_options=disable-warnings` 以禁止显示 nvcc 警告消息。

### 构建软件包

`bazel build` 命令会创建一个名为 `build_pip_package` 的可执行文件，此文件是用于构建 `pip` 软件包的程序。例如，以下命令会在 `C:/tmp/tensorflow_pkg` 目录中构建 `.whl` 软件包：

```
bazel-bin\tensorflow\tools\pip_package\build_pip_package C:/tmp/tensorflow_pkg

```

尽管可以在同一个源代码树下构建 CUDA 和非 CUDA 配置，但建议您在同一个源代码树中的这两种配置之间切换时运行 `bazel clean`。

### 安装软件包

生成的 `.whl` 文件的文件名取决于 TensorFlow 版本和您的平台。例如，使用 `pip3 install` 安装软件包：

```
pip3 install C:/tmp/tensorflow_pkg/tensorflow-version-cp36-cp36m-win_amd64.whl

```

**成功**：TensorFlow 现已安装完毕。

## 使用 MSYS shell 构建

也可以使用 MSYS shell 构建 TensorFlow。做出下面列出的更改，然后按照之前的 Windows 原生命令行 (`cmd.exe`) 说明进行操作。

### 停用 MSYS 路径转换

MSYS 会自动将类似 Unix 路径的参数转换为 Windows 路径，此转换不适用于 `bazel`。（标签 `//foo/bar:bin`被视为 Unix 绝对路径，因为它以斜杠开头。）

```
export MSYS_NO_PATHCONV=1
```

### 设置 PATH

将 Bazel 和 Python 安装目录添加到 `$PATH` 环境变量中。如果 Bazel 安装到了 `C:\tools\bazel.exe`，并且 Python 安装到了 `C:\Python36\python.exe`，请使用以下命令设置 `PATH`：

\# Use Unix-style with ':' as separator
`export PATH="/c/tools:$PATH"` `export PATH="/c/Python36:$PATH"`

要启用 GPU 支持，请将 CUDA 和 cuDNN bin 目录添加到 `$PATH` 中：

```
export PATH="/c/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v9.0/bin:$PATH"
```

 

 

下边的可以不看，是以前的记录。

1.  需要软件：
    1. git
    2. anaconda 64
    3. cuda9
    4. cudnn 7
    5. cmake
    6. swig
    7. vc 2015
2. 官网步骤 [https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/cmake/README.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/cmake/README.md)
3. 我的步骤
    1. 到cmake生成vc项目的时候，基本一样，如下是要设置的。
    2. 先修改vc 2015成增量编译，因为要编译多遍的。
    3. 编辑以"\_"下划线开头的5个项目，配置属性==>连接器==>常规==>附加库目录==>添加：$(SolutionDir)$(Configuration); ，不然的话会出现 LINK : fatal error LNK1181: 无法打开输入文件“\\pywrap\_tensorflow\_internal.lib”错误。
4.  关于grpc项目，先编译第一遍，不成功，修改如下后再单独编译，就成功了，因为防火墙，https://storage.googleapis.com/libpng-public-archive/libpng-1.2.53.tar.gz ，可能访问不了。但是这个是可以下载的。我直接下载到： E:\\project\\pythonlib\\tensorflow\\tensorflow\\contrib\\cmake\\build\\downloads文件夹中。
    1. 进入tensorflow\\tensorflow\\contrib\\cmake\\external修改boringssl的url，将其URL由原来指向https://boringssl.googlesource.com/boringssl 改为 https://github.com/google/boringssl
    2. 修改tensorflow\\tensorflow\\contrib\\cmake\\build\\grpc\\src\\grpc\\.gitmodules，将third\_party/boringssl-with-bazel的url为 https://github.com/kerwinxu/boringssl-with-bazel
    3. 修改C:\\TF\\tensorflow\\tensorflow\\contrib\\cmake\\build\\grpc\\src\\grpc\\.git\\config中的third\_party/boringssl-with-bazel的url为https://github.com/google/boringsslc
    4. 为了防止重新下载grpc及其submudule，我们需要修改相应的cmake文件C:\\TF\\tensorflow\\tensorflow\\contrib\\cmake\\build\\grpc\\tmp\\grpc-gitclone.cmake，主要是不让他存在删除或重新下载grpc的命令，我们将如下命令注释掉： #execute\_process( # COMMAND ${CMAKE\_COMMAND} -E remove\_directory "C:/TF/tensorflow/tensorflow/contrib/cmake/build/grpc/src/grpc" # RESULT\_VARIABLE error\_code # ) #if(error\_code) # message(FATAL\_ERROR "Failed to remove directory: 'C:/TF/tensorflow/tensorflow/contrib/cmake/build/grpc/src/grpc'") #endif() 同时不让它retry git clone 3 times，主要是在while(error\_code AND number\_of\_tries LESS 3)之前set(error\_code 0)
    5. 还有下载的 https://github.com/kerwinxu/libFuzzer.git ，https://github.com/kerwinxu/boringssl-with-bazel.git ，我是从这里下载的。
5. 编辑 tf\_python\_copy\_scripts\_to\_destination 项目，将里边的
    1. "D:\\Program Files\\CMake\\bin\\cmake.exe" -E touch E:/project/pythonlib/tensorflow/tensorflow/contrib/cmake/build/tf\_python/tensorflow/contrib/lite/python/lite.py
    2. 前面加上，创建这个目录，可能是因为没有目录，所以touch创建文件不成功。
    3. md E:/project/pythonlib/tensorflow/tensorflow/contrib/cmake/build/tf\_python/tensorflow/contrib/lite/python
    4. 或者也可以用
    5. cmake -E make\_directory E:/project/pythonlib/tensorflow/tensorflow/contrib/cmake/build/tf\_python/tensorflow/contrib/lite/python
6. 我的步骤：
    1. 首先All\_BUILD，肯定是错误的啦
    2. 像如上修改grpc，重新编译
    3. 一般情况下，只有一个项目出现问题，tf\_core\_kernels ，堆空间不够的，对这个项目单独编译。
    4. 然后单独编译，tf\_python\_build\_pip\_package，如果出现错误。就修改这个项目的“生成事件”，一个“预先生成事件”，一个是“后期生成事件”，这个是命令行，我将这个做成批处理运行，然后看看哪里错误就修改哪里。
