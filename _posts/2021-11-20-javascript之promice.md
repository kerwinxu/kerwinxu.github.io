---
layout: post
title: "javascript之Promice"
date: "2021-11-20"
categories: 
  - "javascript"
---

如下是我的理解，先来例子

```
let myPromise = new Promise(function(myResolve, myReject) {
  let req = new XMLHttpRequest();
  req.open('GET', "mycar.htm");
  req.onload = function() {
    if (req.status == 200) {
      myResolve(req.response);
    } else {
      myReject("File not Found");
    }
  };
  req.send();
});

myPromise.then(
  function(value) {myDisplayer(value);},
  function(error) {myDisplayer(error);}
);
```

其实这个调用成功和调用失败返回的函数，可以理解成函数指针，调用成功和调用失败以不同的路径去执行。
