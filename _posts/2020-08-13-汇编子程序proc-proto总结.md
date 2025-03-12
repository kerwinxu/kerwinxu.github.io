---
layout: post
title: "汇编子程序proc/proto总结"
date: "2020-08-13"
categories: 
  - "asm"
---

```
MySub PROTO        ;过程原型
.
INVOKE MySub       ;过程调用
.
MySub PROC          ;过程实现
..
MySub ENDP
```

 

- label PROC \[attributes\] \[USES reglist\], parameter\_list
    - 其中uses的作用相当于push
    - 而后边如果有parameter\_list ，如果是stdcall
        -  则会在过程前面生成 push ebp / mov ebp  , esp
        -  后边生成 mov esp , ebp
