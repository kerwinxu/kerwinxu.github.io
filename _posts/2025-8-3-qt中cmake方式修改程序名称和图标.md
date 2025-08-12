---
layout: post
title: "qt中cmake方式修改程序名称和图标"
date: "2025-07-30"
categories: ["计算机语言", "c"]
math: true
---

# 修改程序名称
```
set_target_properties(RadiationMonitoringSystemByMultiUsbHub PROPERTIES
    ${BUNDLE_ID_OPTION}
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
    OUTPUT_NAME "程序名称"
)

```

# 修改程序运行时候的图标
建立一个qrc，导入ioc文件，然后在程序中
```c
#include "mainwindow.h"

#include <QApplication>
#include <QIcon>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setWindowIcon(QIcon(":/resources/logo.ico"));
    w.show();
    return a.exec();
}
```

# 修改win系统的程序图标
这个是建立一个rc文件（win系统独有），内容是
```
IDI_ICON1 ICON "logo.ico"
```
