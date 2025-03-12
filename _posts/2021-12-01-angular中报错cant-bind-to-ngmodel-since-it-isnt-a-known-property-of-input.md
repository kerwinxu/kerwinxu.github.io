---
title: "Angular中报错Can't bind to 'ngModel' since it isn't a known property of 'input'"
date: "2021-12-01"
categories: 
  - "javascript"
---

在Angular项目中使用\[(ngModel)\]双向数据绑定时提示：

Can't bind to 'ngModel' since it isn't a known property of 'input'

解决 这是因为在使用双向数据绑定\[(ngModel)\]时必须引入FormsModule这个模块。

打开app.module.ts

```
import { FormsModule } from '@angular/forms';
```

并添加到声明中

```
imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
```
