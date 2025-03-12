---
title: "pipenv，pip的版本管理系统"
date: "2023-03-01"
categories: 
  - "python"
---

pipenv命令具有以下选项

```
$ pipenv
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --update         更新Pipenv & pip
  --where          显示项目文件所在路径
  --venv           显示虚拟环境实际文件所在路径
  --py             显示虚拟环境Python解释器所在路径
  --envs           显示虚拟环境的选项变量
  --rm             删除虚拟环境
  --bare           最小化输出
  --completion     完整输出
  --man            显示帮助页面
  --three / --two  使用Python 3/2创建虚拟环境（注意本机已安装的Python版本）
  --python TEXT    指定某个Python版本作为虚拟环境的安装源
  --site-packages  附带安装原Python解释器中的第三方库
  --jumbotron      不知道啥玩意....
  --version        版本信息
  -h, --help       帮助信息
```

可使用的命令参数：

```
Commands:
  check      检查安全漏洞
  graph      显示当前依赖关系图信息
  install    安装虚拟环境或者第三方库
  lock       锁定并生成Pipfile.lock文件
  open       在编辑器中查看一个库
  run        在虚拟环境中运行命令
  shell      进入虚拟环境
  uninstall  卸载一个
  update     卸载当前所有的包，并安装它们的最新版本
```

常用命令如下：

- pipenv --python 3.7 创建3.7版本Python环境
- pipenv install package\_name 安装包
- pipenv graph 查看包与包之间依赖关系
- pipenv --venv 查看虚拟环境保存路径
- pipenv --py 查看python解释器路径
- pipenv install package\_name --skip-lock 跳过lock，可以等项目开发好后，再更新所有报的hash值
- pipenv install --dev package\_name 在开发环境安装测试包(可以加–skip-lock参数)
- pipenv uninstall package\_name 卸载包
- 你也可以指定 $ pipenv install -r path/to/requirements.txt 导入某个requirements文件
