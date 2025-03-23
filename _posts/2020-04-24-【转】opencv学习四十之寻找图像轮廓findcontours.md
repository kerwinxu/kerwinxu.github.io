---
layout: post
title: "【转】opencv学习(四十)之寻找图像轮廓findContours()"
date: "2020-04-24"
categories: 
  - "c-计算机"
  - "图像处理"
---

1.概述 在这篇文章中介绍如何使用findContours()函数寻找图像中物体的轮廓，在OpenCV中没有给出findCountours()函数的原理，如果想了解查找轮廓原理，可以翻\*\*墙出去Google”Topological structural analysis of digitized binary images by border following”,这里就不一一翻译了.

2.API opencv中提供findContours()函数来寻找图像中物体的轮廓，并结合drawContours()函数将找到的轮廓绘制出。首先看一下findContours(),opencv中提供了两种定义形式

```
void cv::findContours   (   InputOutputArray    image,
                            OutputArrayOfArrays     contours,
                            OutputArray     hierarchy,
                            int     mode,
                            int     method,
                            Point   offset = Point() 
                        )   

```

 

参数解释 image:输入图像，图像必须为8-bit单通道图像，图像中的非零像素将被视为1，0像素保留其像素值，故加载图像后会自动转换为二值图像。我们同样可以使用cv::compare,cv::inRange,cv::threshold,cv::adaptiveThreshold,cv::Canny等函数来创建二值图像，，如果第四个参数为cv::RETR\_CCOMP或cv::RETR\_FLOODFILL，输入图像可以是32-bit整型图像(CV\_32SC1) contours:检测到的轮廓，每个轮廓都是以点向量的形式进行存储即使用point类型的vector表示 hierarchy:可选的输出向量(std::vector)，包含了图像的拓扑信息，作为轮廓数量的表示hierarchy包含了很多元素，每个轮廓contours\[i\]对应hierarchy中hierarchy\[i\]\[0\]~hierarchy\[i\]\[3\],分别表示后一个轮廓，前一个轮廓，父轮廓，内嵌轮廓的索引，如果没有对应项，则相应的hierarchy\[i\]设置为负数。 mode轮廓检索模式，可以通过cv::RetrievalModes()查看详细信息，如下

其中 RETR\_EXTERNAL:表示只检测最外层轮廓，对所有轮廓设置hierarchy\[i\]\[2\]=hierarchy\[i\]\[3\]=-1 RETR\_LIST:提取所有轮廓，并放置在list中，检测的轮廓不建立等级关系 RETR\_CCOMP:提取所有轮廓，并将轮廓组织成双层结构(two-level hierarchy),顶层为连通域的外围边界，次层位内层边界 RETR\_TREE:提取所有轮廓并重新建立网状轮廓结构 RETR\_FLOODFILL：官网没有介绍，应该是洪水填充法 method:轮廓近似方法可以通过cv::ContourApproximationModes()查看详细信息

CHAIN\_APPROX\_NONE：获取每个轮廓的每个像素，相邻的两个点的像素位置差不超过1 CHAIN\_APPROX\_SIMPLE：压缩水平方向，垂直方向，对角线方向的元素，值保留该方向的重点坐标，如果一个矩形轮廓只需4个点来保存轮廓信息 CHAIN\_APPROX\_TC89\_L1和CHAIN\_APPROX\_TC89\_KCOS使用Teh-Chinl链逼近算法中的一种 offset:轮廓点可选偏移量，有默认值Point()，对ROI图像中找出的轮廓并要在整个图像中进行分析时，使用

opencv中提供的另一种定义形式如下：

```
void cv::findContours   (   InputOutputArray    image,
                            OutputArrayOfArrays     contours,
                            int     mode,
                            int     method,
                            Point   offset = Point() 
                        )   

```

 

drawContours()

```
void cv::drawContours   (   InputOutputArray    image,
                            InputArrayOfArrays  contours,
                            int     contourIdx,
                            const Scalar &  color,
                            int     thickness = 1,
                            int     lineType = LINE_8,
                            InputArray  hierarchy = noArray(),
                            int     maxLevel = INT_MAX,
                            Point   offset = Point() 
                        )

```

 

参数解释 image:输入输出图像，Mat类型即可 contours:使用findContours检测到的轮廓数据，每个轮廓以点向量的形式存储，point类型的vector contourIdx:绘制轮廓的只是变量，如果为负值则绘制所有输入轮廓 color:轮廓颜色 thickness:绘制轮廓所用线条粗细度，如果值为负值，则在轮廓内部绘制 lineTpye:线条类型，有默认值LINE\_8，有如下可选类型

[![]](http://127.0.0.1/?attachment_id=3376)

hierarchy:可选层次结构信息 maxLevel:用于绘制轮廓的最大等级 offset:可选轮廓便宜参数，用制定偏移量offset=(dx, dy)给出绘制轮廓的偏移量

示例代码

```
#include <iostream>
#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>
#include <stdlib.h>

using namespace std;
using namespace cv;

int main()
{
    Mat srcImage, grayImage, dstImage;
    srcImage = imread("HappyFish.jpg");

    //判断图像是否加载成功
    if (srcImage.empty())
    {
        cout << "图像加载失败" << endl;
        return -1;
    }
    else
    {
        cout << "图像加载成功!" << endl << endl;
    }

    namedWindow("原图像", WINDOW_AUTOSIZE);
    imshow("原图像", srcImage);

    //转换为灰度图并平滑滤波
    cvtColor(srcImage, grayImage, COLOR_BGR2GRAY);

    //定义变量
    vector<vector<Point>>contours;
    vector<Vec4i>hierarchy;

    grayImage = grayImage > 100;
    findContours(grayImage, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE);

    //绘制轮廓图
    dstImage = Mat::zeros(grayImage.size(), CV_8UC3);
    for (int i = 0; i < hierarchy.size(); i++)
    {
        Scalar color = Scalar(rand() % 255, rand() % 255, rand() % 255);
        drawContours(dstImage, contours, i, color, CV_FILLED, 8, hierarchy);
    }
    imshow("轮廓图", dstImage);
    waitKey(0);

    return 0;
}

```
