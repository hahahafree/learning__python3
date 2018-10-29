#!/bin/usr/env python3
# -*- coding:utf-8 -*-

#例子1
a = list(range(1,11))
print('1-10:',a)

#例子2 1*1
b=[]
for x in range(1,11):
    b.append(x*x)
print('1*1:',b)

#例子3
c=[x*x for x in range(1,11)]
print('列表生产式：x*x',c)

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
d = [x * x for x in range(1,11) if x % 2 == 0]
print('1-11偶数的平方：',d)

#还可以使用两层循环，可以生成全排列：
f = [m + n for m in 'ABC' for n in 'XYZ']
print('全排列：',f)

#列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
g = [d for d in os.listdir('.')]
print(g)

#for循环其实可以同时使用两个甚至多个变量
# 比如dict的items()可以同时迭代key和value：
h = {'x':'A','y':'B','z':'C'}
for k,v in h.items():
    print('同时迭代key和value:',k,'=',v)

#列表生成式也可以使用两个变量来生成list：
j = {'x':'A','y':'B','z':'C'}
j1=[k + '=' + v for k ,v in j.items()]
print('两个变量来生成list：',j1)

#把一个list中所有的字符串变成小写：
k = ['A','B','C','Dog']
k1 = [s.lower() for s in k]
print('把一个list中所有的字符串变成小写：',k)