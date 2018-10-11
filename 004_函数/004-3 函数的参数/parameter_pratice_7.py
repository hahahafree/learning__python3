#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#以下函数允许计算两个数的乘积
def product_1(x, y):
    return x * y

# 请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*args):
    total = 1
    if 0 == len(args):
        raise TypeError('error args')
    for item in args:
        total  = total * item
    return total

args = (1, 2, 3, 4)
a = product(*args)
print(a)
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
