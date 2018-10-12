#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：

#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

#所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(100))

#要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
def fact_iter(num,product):
    if num ==1:
        return product
    return fact_iter(num - 1 , num * product)
print(fact_iter(5,1))
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
#汉诺塔的移动可以用递归函数非常简单地实现。

#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法，例如：
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
#move(3, 'A', 'B', 'C')
def move (n,a,b,c):
    if n ==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(3,'A','B','C')


