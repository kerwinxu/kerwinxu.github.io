---
title: "Normal Equation推导"
date: "2018-02-23"
categories: 
  - "数学"
---

Normal Equation说是一种最小二乘法。

- 首先定义一堆符号 $$ X=\\left\[\\begin{array}{c}(x^{(1)})^T\\\\ (x^{(2)})^T\\\\\\vdots\\\\(x^{(m)})^T\\end{array}\\right\] ,\\overrightarrow{y}=\\left\[\\begin{array}{c}y^{(1)}\\\\y^{(2)}\\\\\\vdots\\\\y^{(m)}\\end{array}\\right\]$$
    - 注意这个X矩阵的最后一列全是1，即将每个点的x坐标扩展成齐次坐标形式。
- 误差是 $$ X\\theta-\\overrightarrow{y}=\\left\[\\begin{array}{c}(x^{(1)})^T\\theta\\\\ (x^{(2)})^T\\theta\\\\\\vdots\\\\(x^{(m)})^T\\theta\\end{array}\\right\]-\\left\[\\begin{array}{c}y^{(1)}\\\\y^{(2)}\\\\\\vdots\\\\y^{(m)}\\end{array}\\right\] = \\left\[\\begin{array}{c}h\_{\\theta}(x^{(1)})-y^{(1)}\\\\h\_{\\theta}(x^{(2)})-y^{(2)}\\\\\\vdots\\\\h\_{\\theta}(x^{(m)})-y^{(m)}\\end{array}\\right\]$$
- 我们定义的损失函数为误差的平方和的最小 $$Cost=J(\\theta)=\\frac{1}{2}(X\\theta-\\overrightarrow{y})^T(X\\theta-\\overrightarrow{y})=\\frac{1}{2}\\sum\_{i=1}^{m}(h\_\\theta(x^{(i)})-y^{(i)})^2$$
    - 矩阵乘以这个矩阵的转置矩阵，得到的就是损失函数的平方和。
    - 这个损失函数可以展开  \\\[\\begin{aligned} J(\\theta)&= \\frac{1}{2m}(X\\theta-\\overrightarrow{y})^T(X\\theta-\\overrightarrow{y})\\\\ &= \\frac{1}{2m}((X\\Theta)^T-(\\overrightarrow{y})^T)(X\\theta-\\overrightarrow{y})\\\\ &= \\frac{1}{2m}((X\\theta)^T X\\theta-(X\\theta)^T\\overrightarrow{y}-(\\overrightarrow{y})^T X\\theta+(\\overrightarrow{y})^T \\overrightarrow{y}) \\\\ &=\\frac{1}{2m}(\\theta^TX^T X\\theta-\\theta^TX^T\\overrightarrow{y}-(\\overrightarrow{y})^T X\\theta+(\\overrightarrow{y})^T \\overrightarrow{y}) \\\\ &=\\frac{1}{2m}(\\theta^TX^T X\\theta-2\\theta^TX^T\\overrightarrow{y}+(\\overrightarrow{y})^T \\overrightarrow{y}) \\\\ \\end{aligned}\\\]
        - 要点：
            - 矩阵转置运算法则中有
                - (A+B)’=A’+B’
                - (AB)’=B’A’ : 注意位置颠倒了
                    - $latex (X\\Theta)^T$ 展开，用了这个。
                - $latex \\theta^TX^T\\overrightarrow{y}$ 是标量，与它的转置是相等的。
- 求这个损失函数的导数 $$ \\frac{\\partial J(\\theta)}{\\partial}=\\frac{1}{2m}(2X^TX\\theta-2X^Ty)
- 设导数为0，我们很容易得到 \\\[2X^TX\\theta=2X^Ty\\\\\\theta=(X^TX)^{-1}X^Ty\\\]
