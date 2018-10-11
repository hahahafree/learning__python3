#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#位置参数
#我们先写一个计算x2的函数：
def power(x):
    return x*x
#对于power(x)函数，参数x就是一个位置参数。
#当我们调用power函数时，必须传入有且仅有的一个参数x：
a_1 = power(5)
print("5的平方=",a_1)
#现在，如果我们要计算x3怎么办？可以再定义一个power3函数，
# 但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
#你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
def power_1(x_1,n):
    s = 1
    while n > 0:
        n = n - 1
        s  = s * x_1
    return s
#对于这个修改后的power(x, n)函数，可以计算任意n次方：
c = power_1(5,3)
d = power_1(5,4)
print("5的3次方=",c)
print("5的4次方=",d)