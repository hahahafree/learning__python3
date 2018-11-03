#!/bin/usr/env python 3
# -*- coding: utf-8 -*-

#把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print('list:',L)
print('generator:',g)

#如果要一个一个打印出来，
# 可以通过next()函数获得generator的下一个返回值：
a = next(g)
print('generator值:',a)
a = next(g)
print('generator值:',a)
a = next(g)
print('generator值:',a)
a = next(g)
print('generator值:',a)

#generator也是可迭代对象：
b = (x * x for x in range(10))
for n in g:
    print('迭代对象：',n)

#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
c = fib(10)
print('斐波拉契数列:',c)

#把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def f(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
d = f(20)
print('generator',d)