---
layout: post
title: "python-docx删除某一个段落或者run"
date: "2021-04-27"
categories: 
  - "python"
---

```
def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None
```
