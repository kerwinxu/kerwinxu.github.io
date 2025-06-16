---
layout: post
title: "OpenCV_Python官方文档7+——按位运算之给图像加logo"
date: "2021-04-08"
categories: ["计算机语言", "Python"]
---

## OpenCV-Python Tutorials

[https://opencv-python-tutroals.readthedocs.io/en/latest/py\_tutorials/py\_tutorials.html](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)

# 按位运算

包括按位与(AND)、按位或(OR)、按位非(NOT)、按位异或(XOR)等运算。

按位运算的用途：比如要得到一个加logo的图像。如果将两幅图片直接相加会改变图片的颜色，如果用图像混合，则会改变图片的透明度，这时候就需要用按位操作，既不改变图像颜色，又不改变图像透明度，类似PS。 这里需要了解一个术语——掩膜（mask）￼是用一副二值化图片对另外一幅图片进行局部的遮挡。

主要函数

- cv2.bitwise\_and()：位与运算，有0则为0, 全为1则为1
- cv2.bitwise\_not()：或运算，有1则为1, 全为0则为0
- cv2.bitwise\_or()：非运算，非0为1, 非1为0
- cv2.bitwise\_xor()：异或运算，不同为1, 相同为0

ret, dst = cv2.threshold(src, thresh, maxval,type)：阈值（二值化操作），阈值又叫临界值，是指一个效应能够产生的的最低值或最高。 dst： 输出图像 src： 输入图像，只能输入单通道图像，一般为灰度图 thresh： 阈值 maxval： 当像素值大于阈值（或者小于阈值，根据type来决定），所赋予的值 type：阈值操作的类型----每种类型图片效果展示点击这里 cv2.THRESH\_BINARY #二元阈值 cv2.THRESH\_BINARY\_INV #逆二元阈值， cv2.THRESH\_TRUNC cv2.THRESH\_TOZERO cv2.THRESH\_TOZERO\_INV 实例：将OpenCV的logo加到图片为沙漠的左上角，要求有颜色的区域为不透明的。

思路就是把原图中要放logo的区域抠出来，再把logo填到空出来的区域上。

# 步骤

## 1\. 读取图片

```
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
os.chdir('C:/Users/lenovo/Pictures/')

img1 = cv2.imread('desert.jpg')　＃沙漠图片
img2 = cv2.imread('opencv_logo.jpg')　#logo图片
#img2 = cv2.imread('opencv_logo.jpg'，0) #也可以读取logo的时候直接灰度化

```

## 2\. 根据logo大小提取感兴趣区域roi

```
# 把logo放在左上角，提取原图中要放置logo的区域roi
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]
```

## 3\. 创建掩膜mask

```
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #将图片灰度化，如果在读取logo时直接灰度化，该步骤可省略

#如果一个像素高于175，则像素值转换为255（白色色素值），否则转换成0（黑色色素值）
#即有内容的地方为黑色0，无内容的地方为白色255.
#白色的地方还是白色，除了白色的地方全变成黑色
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)#阙值操作
mask_inv = cv2.bitwise_not(mask) #与mask颜色相反，白色变成黑色，黑变白

```

## 4\. logo与感兴趣区域roi融合

```
# 保留除logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)
dst = cv2.add(img1_bg, img2_fg)  # logo与感兴趣区域roi进行融合
img1[:rows, :cols] = dst  # 将融合后的区域放进原图
img_new_add = img1.copy() #对处理后的图像进行拷贝

```

## 5\. 显示每步处理后的图片

```
'''
# 显示图片，调用opencv展示
cv2.imshow('logo',img2)
cv2.imshow('logo_gray',img2gray)
cv2.imshow('logo_mask',mask)
cv2.imshow('logo_mask_inv',mask_inv)
cv2.imshow('roi',roi)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# cv2与matplotlib的图像颜色模式转换，cv2是BGR格式，matplotlib是RGB格式
def img_convert(cv2_img):
    # 灰度图片直接返回
    if len(cv2_img.shape) == 2:
        return cv2_img
    # 3通道的BGR图片
    elif len(cv2_img.shape) == 3 and cv2_img.shape[2] == 3:
        b, g, r = cv2.split(cv2_img) #分离原图像通道
        return cv2.merge((r, g, b)) #合并新的图像通道
    # 4通道的BGR图片
    elif len(cv2_img.shape) == 3 and cv2_img.shape[2] == 4:
        b, g, r, a = cv2.split(cv2_img)
        return cv2.merge((r, g, b, a))
    # 未知图片格式
    else:
        return cv2_img

# 显示图片，调用matplotlib展示
titles = ['logo','logo_gray','logo_mask','logo_mask_inv','roi','img1_bg','img2_fg','dst']
imgs = [img2,img2gray,mask,mask_inv,roi,img1_bg,img2_fg,dst]
for i in range(len(imgs)):
    plt.subplot(2,4,i+1),plt.imshow(img_convert(imgs[i]),'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# 显示加logo的图片
cv2.imshow('img_new_add',img_new_add)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

 

# 所有源代码

```
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os 
os.chdir('C:/Users/lenovo/Pictures/')

# 1. 读取图片
img1 = cv2.imread('desert.jpg') #读取沙漠图片
img2 = cv2.imread('opencv_logo.jpg') #读取logo图片
#img2 = cv2.imread('opencv_logo.jpg'，0) #也可以读取logo的时候直接灰度化

# 2. 根据logo大小提取感兴趣区域roi
# 把logo放在左上角，提取原图中要放置logo的区域roi
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]

# 3. 创建掩膜mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #将图片灰度化，如果在读取logo时直接灰度化，该步骤可省略

#cv2.THRESH_BINARY：如果一个像素值低于200，则像素值转换为255（白色色素值），否则转换成0（黑色色素值）
#即有内容的地方为黑色0，无内容的地方为白色255.
#白色的地方还是白色，除了白色的地方全变成黑色
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)#阙值操作
mask_inv = cv2.bitwise_not(mask) #与mask颜色相反，白色变成黑色，黑变白

# 4. logo与感兴趣区域roi融合
# 保留除logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)
dst = cv2.add(img1_bg, img2_fg)  # logo与感兴趣区域roi进行融合
img1[:rows, :cols] = dst  # 将融合后的区域放进原图
img_new_add = img1.copy() #对处理后的图像进行拷贝

# 5. 显示每步处理后的图片
'''
# 显示图片，调用opencv展示
cv2.imshow('logo',img2)
cv2.imshow('logo_gray',img2gray)
cv2.imshow('logo_mask',mask)
cv2.imshow('logo_mask_inv',mask_inv)
cv2.imshow('roi',roi)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# cv2与matplotlib的图像颜色模式转换，cv2是BGR格式，matplotlib是RGB格式
def img_convert(cv2_img):
    # 灰度图片直接返回
    if len(cv2_img.shape) == 2:
        return cv2_img
    # 3通道的BGR图片
    elif len(cv2_img.shape) == 3 and cv2_img.shape[2] == 3:
        b, g, r = cv2.split(cv2_img) #分离原图像通道
        return cv2.merge((r, g, b)) #合并新的图像通道
    # 4通道的BGR图片
    elif len(cv2_img.shape) == 3 and cv2_img.shape[2] == 4:
        b, g, r, a = cv2.split(cv2_img)
        return cv2.merge((r, g, b, a))
    # 未知图片格式
    else:
        return cv2_img

# 显示图片，调用matplotlib展示
titles = ['logo','logo_gray','logo_mask','logo_mask_inv','roi','img1_bg','img2_fg','dst']
imgs = [img2,img2gray,mask,mask_inv,roi,img1_bg,img2_fg,dst]
for i in range(len(imgs)):
    plt.subplot(2,4,i+1),plt.imshow(img_convert(imgs[i]),'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# 显示并保存加logo的图片
cv2.imshow('img_new_add',img_new_add)
cv2.imwrite('img_new_add.jpg',img_new_add)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

运行结果： 每步处理后的图片

[![no img]](http://127.0.0.1/?attachment_id=3832)

可以看到mask掩码，白色的是可以显示的，黑色的是被屏蔽的。
