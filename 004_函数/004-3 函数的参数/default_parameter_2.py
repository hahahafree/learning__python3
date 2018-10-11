#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#默认参数
#由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power_3(x_3,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x_3
    return s
#当我们调用power(5)时，相当于调用power(5, 2)：
print("5的平方=",power_3(5))
print("5的平方=",power_3(5,2))

#默认参数有个最大的坑，演示如下：
def add_end(L=[]):
    L.append('END')
    return L
#当你正常调用时，结果似乎不错：
f = add_end([1,2,3])
print(f)
#多次调用默认参数时：
g = add_end()
print(g)
g = add_end()
print(g)
g = add_end()
print(g)

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end_1(h=None):
    if h is None:
        h = []
    h.append('END')
    return h
#现在，无论调用多少次，都不会有问题：
j = add_end_1()
print(j)
j = add_end_1()
print(j)
j = add_end_1()
print(j)