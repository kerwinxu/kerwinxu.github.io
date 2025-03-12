---
title: "python、tkinter中动态显示图片闪烁问题"
date: "2021-10-17"
categories: 
  - "python"
---

用双缓冲，重要的部分如下：

- 全局变量
    
    ```
    screen_width = 800
    screen_height = 600
    imgtmp = Image.new('RGB',(screen_width,screen_height),(255,255,255))
    photo = PhotoImage(imgtmp)
    ```
    
     
- 关于label对象
    
    ```
    lbImage = Label(root, image=photo)
    lbImage.config(image=photo)
    lbImage.image=photo # 要这样设置。
    # lbImage.pack(fill=BOTH, expand=YES) # 填充整个窗口
    lbImage.pack()
    ```
    
     
- 动态更改的时候
    
    ```
    photo.paste(im2) # 新的图片直接粘贴到原先图片上。
    ```
