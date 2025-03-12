---
layout: post
title: "jupyter中显示opencv图像"
date: "2021-04-13"
categories: 
  - "python"
---

```
import cv2
import numpy as np
import pytesseract as tess
from PIL import Image
from matplotlib import pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = (30.0, 24.0)   # 单位是inches


def imshow(im):
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
    h,w = im.shape[:2]
    print(im.shape)
    plt.imshow(im,cmap='gray')
```
