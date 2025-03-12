---
layout: post
title: "chez scheme 和 racket 的效率比较"
date: "2020-08-13"
categories: 
  - "lisp"
---

```
(define fib-1 (lambda (n)
  (let ((i 1) (v0 1) (v1 0))
    (define func (lambda ()
      (let ((t 0))
        (cond ((= n 0) 0)
          ((= n 1) 1)
          (else
            (if (< i n)
              (begin
                (set! t (+ v1 v0))
                (set! v1 v0)
                (set! v0 t)
                (set! i (+ i 1))
                (func))
              v0))))))
    (func))))

(time (begin(fib-1 1000000) (cons 'a 'b)))
```

结果：

chez scheme :

(time (begin (fib-1 1000000) ...)) 1749 collections 27.125000000s elapsed cpu time, including 0.281250000s collecting 28.175881200s elapsed real time, including 0.254562900s collecting 43423135824 bytes allocated, including 43382648112 bytes reclaimed (a . b)

 

racket:

cpu time: 55563 real time: 60633 gc time: 21331 '(a . b)

 

看起来效率并不是很大，差别一倍吧。
