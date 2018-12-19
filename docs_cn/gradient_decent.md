提到梯度下降相信大家应该都不会觉得陌生（不陌生你点进来干嘛[捂脸]），本文就梯度下降的基本原理进行讲解，并手把手、肩并肩地带您实现这一算法。

完整实现代码请参考本人的p...哦不是...github：  
[gradient_decent.py](https://github.com/tushushu/pads/blob/master/pads/optimization/gradient_decent.py)  
[gradient_decent_example.py](https://github.com/tushushu/pads/blob/master/examples/gradient_decent_example.py) 

# 1. 原理篇
我们用人话而不是大段的数学公式来讲讲梯度下降归是怎么一回事。

## 1.1 什么是梯度？
多元函数的各个变量的偏导数以向量的形式写出来，就是梯度。比如函数$f(x, y) = x ^ 2 + siny$，那么它的梯度$grad\ f(x, y)$或者$\Delta f(x, y)$就是$(2x, cosy)$

## 1.2 下降了什么？
在机器学习里，我们用梯度下降是用来求解一个损失函数$L(\Theta)$的最小值，所谓下降实际上是这个损失函数的值在下降。

## 1.3 什么是梯度下降？
沿着函数梯度的负方向不断地更新损失函数的变量$\Theta$，来不断地“逼近”最小值。

## 1.4 如何理解方向？
因为函数的梯度是向量，而向量是有方向的，如函数$z = x ^ 2 + y ^ 2$，$(x, y)$是多维向量，可以沿着无数个方向进行更新。

## 1.5 为什么是梯度的负方向？
根据泰勒公式，$f(X + X_0) \approx f(X) + X_0f'(X)$，其中$f(X)$是当前的函数值，$f'(X)$是梯度，$X_0$是$X$的增量。让$f(X + X_0)$最小，也就是让$X_0f'(X)$最小。两个向量做点乘的时候，如果向量模长一定，那么当向量夹角是π的时候结果最小，即向量$X_0$与梯度$f'(X)$相反的时候$f(X + X_0)$最小。

## 1.6 什么是凸函数？
简单说，就是函数图像向下凹的函数。注意，这跟很多数学教材的定义是相反的。严格的定义是函数在区间I上有定义，当且仅当$\forall x_1, x_2 \in I$，有$[f(x_1) + f(x_2)] / 2 \geq f[(x_1 + x_2)/2]$时，$f(x)$是凸函数。证明一个凸函数的方法是它的二阶导数非负，对于多元函数来说就是海瑟矩阵半正定(不了解可以略过)。从导数定义上可以知道，二阶导数非负，说明一阶导数是单调增函数，那么函数的切线斜率越来越大，所以函数的形状向下凸的。

## 1.7 梯度下降与凸函数
在机器学习领域，我们用梯度下降优化损失函数的时候往往希望损失函数是个凸函数，是因为凸函数处处可导，能用梯度下降求解。且有唯一的最小值，确保最后会收敛在全局最优解。



# 2. 实现篇
本人用全宇宙最简单的编程语言——Python实现了梯度下降，没有依赖任何第三方库，便于学习和使用。简单说明一下实现过程，更详细的注释请参考本人github上的代码。

1. 随机生成$\Theta$的初始值  
2. 计算当前的梯度    
3. 更新$\Theta$  
4. 如果函数收敛或者超过最大迭代次数则返回
   
```Python
from random import random


def gradient_decent(fn, partial_derivatives, n_variables, lr=0.1,
                    max_iter=10000, tolerance=1e-5):
    theta = [random() for _ in range(n_variables)]
    y_cur = fn(*theta)
    for i in range(max_iter):
        # Calculate gradient of current theta.
        gradient = [f(*theta) for f in partial_derivatives]
        # Update the theta by the gradient.
        for j in range(n_variables):
            theta[j] -= gradient[j] * lr
        # Check if converged or not.
        y_cur, y_pre = fn(*theta), y_cur
        if abs(y_pre - y_cur) < tolerance:
            break
    return theta, y_cur
```

# 3. 效果评估
## 3.1 定义二元函数及其导数
1. 定义二元函数f(x, y)，显然x = 1, y = 2时，函数可以取最小值2  
2. 对x和y分别求偏导

```Python
def f(x, y):
    return (x + y - 3) ** 2 + (x + 2 * y - 5) ** 2 + 2


def df_dx(x, y):
    return 2 * (x + y - 3) + 2 * (x + 2 * y - 5)


def df_dy(x, y):
    return 2 * (x + y - 3) + 4 * (x + 2 * y - 5)
```

## 3.2 求解函数最小值

```Python
def main():
    print("Solve the minimum value of quadratic function:")
    n_variables = 2
    theta, f_theta = gradient_decent(f, [df_dx, df_dy], n_variables)
    theta = [round(x, 3) for x in theta]
    print("The solution is: theta %s, f(theta) %.2f.\n" % (theta, f_theta))
```

## 3.3 效果展示
梯度下降的求解结果如下，效果还不错。如果希望结果更加精确，可以把tolerance调小一些。  
![gradient_decent.png](https://github.com/tushushu/pads/blob/master/pic/gradient_decent.png)