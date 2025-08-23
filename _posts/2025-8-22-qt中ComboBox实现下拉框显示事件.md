---
layout: post
title: "qt中ComboBox实现下拉框显示事件"
date: "2025-08-22"
categories: ["计算机语言", "c"]
---

继承一个QCombobox类
MyComboBox.h
```c
#ifndef MYCOMBOBOX_H
#define MYCOMBOBOX_H


#include <QComboBox>
#include <QObject>

class MyComboBox : public QComboBox
{
    Q_OBJECT

public:
    explicit MyComboBox(QWidget *parent = nullptr);

signals:
    void menuPopup();  // 自定义信号，当下拉菜单弹出时触发

protected:
    void showPopup() override;
};


#endif // MYCOMBOBOX_H


```

MyComboBox.cpp
```c
// MyComboBox.cpp
#include "MyComboBox.h"


MyComboBox::MyComboBox(QWidget *parent)
{

}

void MyComboBox::showPopup()
{
    QComboBox::showPopup();  // 保持原有行为
    emit menuPopup();        // 触发自定义信号
}

```
