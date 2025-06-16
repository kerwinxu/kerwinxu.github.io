---
layout: post
title: "pillow 出现 invalid face handle"
date: "2021-03-20"
categories: ["计算机语言", "Python"]
---

```
  File "批量添加文字.py", line 108, in draw_content
    draw.text((50,5),str(d['类型']), font=font25bd, fill='#eaca67')
  File "d:\anaconda3\lib\site-packages\PIL\ImageDraw.py", line 379, in text
    draw_text(ink)
  File "d:\anaconda3\lib\site-packages\PIL\ImageDraw.py", line 324, in draw_text
    mask, offset = font.getmask2(
  File "d:\anaconda3\lib\site-packages\PIL\ImageFont.py", line 667, in getmask2
    size, offset = self.font.getsize(
OSError: invalid face handle
```

解决方式

```
fnt = ImageFont.truetype('../fonts/georgiai.ttf', 36, layout_engine=ImageFont.LAYOUT_BASIC)
```

添加了后边的layout\_engine就可以了。
