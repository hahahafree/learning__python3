#!/bin/usr/env python3
# -*- coding: utf-8 -*-

#我们已经知道，可以直接作用于for循环的数据类型有以下几种：

#一类是集合数据类型，如list、tuple、dict、set、str等；

#一类是generator，包括生成器和带yield的generator function。

#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

#可以使用isinstance()判断一个对象是否是Iterable对象：

from collections.abc import Iterable
a = isinstance([],Iterable)#列表
b = isinstance({},Iterable)#元组
c = isinstance('zb',Iterable)
d = isinstance((x for x in range(10)),Iterable)
f = isinstance(100,Iterable)
print('列表为可迭代对象？',a)
print('元组为可迭代对象？',b)
print('字符串为可迭代对象？',c)
print('可迭代对象？',d)
print('可迭代对象？',f)

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
aa = isinstance(iter([]),Iterable)
print(aa)
bb = isinstance(iter('abc'),Iterable)
print(bb)

#凡是可作用于for循环的对象都是Iterable类型；

#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

#集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

#Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1,2,3,4]:
    pass
it = iter([1,2,3,4])
while True:
    try:
        x = next(it)
    except StopIteration:
        break