---
layout: post
title: "PySide6中QListWidget自定义列表项目"
date: "2024-09-01"
categories: 
  - "python"
---

```python
# -*- coding: utf-8 -*-
# 这个脚本是用QListWidget的方式构造列表框，用自定义一个布局的方式来做列表框的项目
# 而 QListView中的自定义，好像是要自己绘图的。

import sys
from PySide6.QtWidgets import QApplication,QMainWindow, QWidget,QVBoxLayout,QHBoxLayout,QListWidget ,QLabel,QPushButton,QListWidgetItem


class QCustomQWidget (QWidget):
    """一个顶顶一的列表项目

    Args:
        QWidget (_type_): _description_
    """
       
    def __init__ (self, parent = None):
        # 首先调用父类的构造函数
        super(QCustomQWidget, self).__init__(parent)
        # 构造界面
        self.textQVBoxLayout = QVBoxLayout()                # 竖直的容器
        self.textUpQLabel    = QLabel()                     # 标签
        self.textDownQLabel  = QLabel()                     # 标签
        self.textQVBoxLayout.addWidget(self.textUpQLabel)   # 容器种添加标签
        self.textQVBoxLayout.addWidget(self.textDownQLabel) # 容器种添加标签
        self.allQHBoxLayout  = QHBoxLayout()                # 水平的容器
        self.iconQLabel      = QPushButton()                # 一个按钮
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)   # 水平容器种先添加按钮
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1) # 然后再添加竖直的容器
        self.setLayout(self.allQHBoxLayout)                 # 用水平容器作为总的容器
        # setStyleSheet 设置样式。
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp (self, text):
        # 设置上文本
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        # 设置下文本
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        # 设置图标，这里没有图片，就注释掉。
        pass
        #self.iconQLabel.setPixmap(QPixmap(imagePath))

class exampleQMainWindow (QMainWindow):
    """主界面，可以手动生成界面，也可以导入ui文件，也可以继承别的界面。
    Args:
        QMainWindow (_type_): _description_
    """

    def __init__ (self):
        # 首先调用弗雷的构造函数
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.myQListWidget = QListWidget(self)      # 创建一个列表框
        for index, name, icon in [                  # 遍历列表框的内容
            ('No.1', 'Meyoko',  'icon.png'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()     # 创建一个自定义项目
            myQCustomQWidget.setTextUp(index)       # 设置内容
            myQCustomQWidget.setTextDown(name)      # 
            myQCustomQWidget.setIcon(icon)          # 
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)   # 创建一个列表框
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())# 调整项的大小以适应部件
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)                         # 添加列表框内容
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget) # 列表框内容换成自定义的。
        self.setCentralWidget(self.myQListWidget)

app = QApplication([])        # 创建程序
window = exampleQMainWindow() # 创建窗口
window.show()                 # 显示窗口
sys.exit(app.exec_())         # 打开消息循环。
```
