---
title: "racket的Foldr/Foldl"
date: "2021-02-09"
categories: 
  - "lisp"
---

`(foldr + 0 (cons 1 (cons 2 (cons 3 empty))))` would become `(+ 1 (+ 2 (+ 3 0)))`

 

<table class="boxed RBoxed" cellspacing="0" cellpadding="0"><tbody><tr><td><blockquote class="SubFlow"><p class="RForeground"><span class="RktPn">(</span><a name="(def._((lib._racket/private/list..rkt)._foldl))"></a><span title="Provided from: racket/base, racket | Package: base"><span class="RktSym"><a class="RktValDef RktValLink" href="https://docs.racket-lang.org/reference/pairs.html#%28def._%28%28lib._racket%2Fprivate%2Flist..rkt%29._foldl%29%29" data-pltdoc="x">foldl</a></span></span><span class="hspace">&nbsp;</span><span class="RktVar">proc</span><span class="hspace">&nbsp;</span><span class="RktVar">init</span><span class="hspace">&nbsp;</span><span class="RktVar">lst</span><span class="hspace">&nbsp;</span><span class="RktMeta">...+</span><span class="RktPn">)</span><span class="hspace">&nbsp;</span>→<span class="hspace">&nbsp;</span><span class="RktSym"><a class="RktValLink" href="https://docs.racket-lang.org/reference/data-structure-contracts.html#%28def._%28%28lib._racket%2Fcontract%2Fprivate%2Fmisc..rkt%29._any%2Fc%29%29" data-pltdoc="x">any/c</a></span></p></blockquote></td></tr><tr><td><span class="hspace">&nbsp;&nbsp;</span><span class="RktVar">proc</span><span class="hspace">&nbsp;</span>:<span class="hspace">&nbsp;</span><span class="RktSym"><a class="RktValLink" href="https://docs.racket-lang.org/reference/procedures.html#%28def._%28%28quote._~23~25kernel%29._procedure~3f%29%29" data-pltdoc="x">procedure?</a></span></td></tr><tr><td><span class="hspace">&nbsp;&nbsp;</span><span class="RktVar">init</span><span class="hspace">&nbsp;</span>:<span class="hspace">&nbsp;</span><span class="RktSym"><a class="RktValLink" href="https://docs.racket-lang.org/reference/data-structure-contracts.html#%28def._%28%28lib._racket%2Fcontract%2Fprivate%2Fmisc..rkt%29._any%2Fc%29%29" data-pltdoc="x">any/c</a></span></td></tr><tr><td><span class="hspace">&nbsp;&nbsp;</span><span class="RktVar">lst</span><span class="hspace">&nbsp;</span>:<span class="hspace">&nbsp;</span><span class="RktSym"><a class="RktValLink" href="https://docs.racket-lang.org/reference/pairs.html#%28def._%28%28quote._~23~25kernel%29._list~3f%29%29" data-pltdoc="x">list?</a></span></td></tr></tbody></table>

 

总结一下

- 共同点：
    - 参数都是
        - 第一个为函数
        - 第二个为初始结果
        - 第三个以上为列表
    - 运算都是，
        - 先取得一个参数，然后跟初始结果相计算，得到一个临时的结果，然后取得第二个参数，然后在跟临时结果相计算，得到一个临时的结果。
- 不同点
    - foldl 是从左边取得第一个参数，
    - foldr 是从右边取得第一个参数

 

(foldl cons  '() '(1 2 3 4))   =》  '(4 3 2 1)  =  (cons 4 ( cons 3 ( cons 2 (cons 1 empty))))

 

(foldr cons  '() '(1 2 3 4))  =》 '(1 2 3 4)   = (cons 1 ( cons 2 ( cons 3 (cons 4 empty))))
