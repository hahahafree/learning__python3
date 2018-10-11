#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#可变参数
#我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#但是调用的时候，需要先组装出一个list或tuple：
k = calc([1,2,3])
print(k)

#把函数的参数改为可变参数：
def calc_1(*number_1):
    sum = 0
    for n in number_1:
        sum = sum + n*n
    return sum
#利用可变参数，调用函数的方式可以简化成这样：
l_1 = calc_1(1,2,3)
print(l_1)

#*nums表示把nums这个list的所有元素作为可变参数传进去。
# 这种写法相当有用，而且很常见。
nums = [2,3,4]
l_2 = calc_1(*nums)
print("2^2+3^2+4^2=",l_2)