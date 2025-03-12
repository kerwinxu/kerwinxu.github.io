---
title: "jupyter修改kernel"
date: "2022-07-16"
categories: 
  - "python"
---

比如我新建了一个名称为opencv的环境，

```
activate opencv
pip install ipykernel
python -m ipykernel install --name opencv
```

列出所有的环境是

```
jupyter kernelspec list
```

删除某个环境是

```
jupyter kernelspec remove opencv
```
