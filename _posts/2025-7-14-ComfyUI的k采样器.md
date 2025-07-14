---
layout: post
title: "ComfyUI的k采样器"
date: "2025-07-14"
categories: ["计算机语言", "ComfyUI"]
math: true
---

常用采样器名称
1. Euler
    1. euler ： 基础采样器，生成速度快但可能缺乏细节
    1. euler_ancestral : 在基础euler的基础上添加随机噪声
1. DPM 
    1. dpmpp_2m : 集合预测其和矫正器，平衡速度与质量，推荐用于高精度图像生成。
    1. dpmpp_2m_sde : 在DMP++基础上引入随机噪声，
1. Heum
    1. heun :比Euler更精确，通过二阶计算提升细节，但耗时增加。
    1. heunpp2 : Heun的优化版本，进一步优化计算效率。
1. Uni
    1. uni_pc : 可在10布左右生成高质量的结果
    1. uni_pic_ph2 : Uni-PC的升级版本，细节处理更精细。

采样器选择建议
1. 图像质量优先 ： 推荐dpmpp_2m,heun, ddim
1. 快速生成 ： euler , uni_pic
1. 创意多样性 ： euler_ancestral, dpmpp_2m_sde