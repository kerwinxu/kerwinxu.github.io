---
layout: post
title: "omniparser v2安装"
date: "2025-03-04"
project: false
categories: ["计算机语言", "Python"]
tag:
- python
---

```
git clone https://github.com/microsoft/OmniParser.git

cd OmniParser

pipenv install --python 3.12

pipenv install huggingface_hub

pipenv shell

huggingface-cli download --resume-download microsoft/OmniParser-v2.0  --local-dir weights

mv weights/icon_caption weights/icon_caption_florence

python gradio_demo.py
```
