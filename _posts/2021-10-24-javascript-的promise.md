---
layout: post
title: "JavaScript 的promise"
date: "2021-10-24"
categories: 
  - "javascript"
---

```
const fs = require('fs')

const getFile = (fileName) => {
  return new Promise((resolve, reject) => {
    fs.readFile(fileName, (err, data) => {
      if (err) {
        reject(err)  // 调用 `reject` 会导致 promise 失败，无论是否传入错误作为参数，
        return        // 且不再进行下去。
      }
      resolve(data)
    })
  })
}

getFile('/etc/passwd')
.then(data => console.log(data))
.catch(err => console.error(err))
```

我的解读，fs.readFile(fileName, (err, data)是一个异步读取，下边是如果出现错误，就执行reject(err) ，并且以err为参数传递出去，如果成功那么就以data为参数传递出去。

最终下标的调用，成功的话会调用then，而失败的话会调用catch。

 

关于promise链式例子如下：

```
new Promise(function(resolve, reject) {

  setTimeout(() => resolve(1), 1000); // (*)

}).then(function(result) { // (**)

  alert(result); // 1
  return result * 2;

}).then(function(result) { // (***)

  alert(result); // 2
  return result * 2;

}).then(function(result) {

  alert(result); // 4
  return result * 2;

});
```

- setTimeout(() => resolve(1), 1000); // (\*) ，这个定时器在1秒后返回1，是成功返回。
- 返回的1被下边的then当作函数参数接收，不断的返回。。。
