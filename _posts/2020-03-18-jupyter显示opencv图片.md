---
layout: post
title: "jupyter显示opencv图片"
date: "2020-03-18"
categories: ["计算机语言", "Python"]
---

```
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna1.png')

show_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

plt.imshow(show_img)
plt.show()

```

 

转载

- [https://juejin.im/post/596b3e50f265da6c2211b609](https://juejin.im/post/596b3e50f265da6c2211b609)
