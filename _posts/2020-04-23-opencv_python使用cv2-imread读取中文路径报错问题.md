---
layout: post
title: "opencv_python使用cv2.imread()读取中文路径报错问题"
date: "2020-04-23"
categories: 
  - "python"
---

```
# -*- coding: utf-8 -*-
import cv2
import numpy as np
 
## 读取图像，解决imread不能读取中文路径的问题
def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img
if __name__=='__main__':
    path='E:/images/百合/百合1.jpg'
    img=cv_imread(path)
    cv2.namedWindow('lena',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('lena',img)
    k=cv2.waitKey(0)
    ##这样是保存到了和当前运行目录下
    cv2.imencode('.jpg', img)[1].tofile('百合.jpg')

```

另外，下边评论说

imdecode读取的是BGR顺序，亲测！跟imread顺序一致
