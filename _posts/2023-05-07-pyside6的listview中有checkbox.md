---
layout: post
title: "PySide6的ListView中有checkbox"
date: "2023-05-07"
categories: ["计算机语言", "Python"]
---

```python
slm = QStandardItemModel()              # 增强的项目模型
for i in self.all_labels:      
  item = QStandardItem(i.label_text)  # 增强的项目
  item.setCheckable(True)             # 支持复选框
  slm.appendRow(item)                 # 添加到模型中，这个是添加到行，也有添加到列
self.ui.listView_search_labels.setModel(slm) # 设置模型
```

代码
