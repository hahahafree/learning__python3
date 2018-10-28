#!/bin/usr/env python3
# -*- coding:utf-8 -*-

#dict就可以迭代：
#dict迭代的是key
d = {'a':1,'b':2,'c':4,'d':5}
for i in d:
    print('dict迭代key:',i)

#迭代value
for value in d.values():
    print('迭代value:',value)

#同时迭代key和value
for k, v in d.items():
    print('同时迭代key和value:',k,v)

#字符串也是可迭代对象，因此，也可以作用于for循环
for ch in 'ABCDEFG':
    print('字符串也是可迭代对象:',ch)

#方法是通过collections模块的Iterable类型判断：
from collections.abc import Iterable
n=isinstance('abc',Iterable)
print('str是否可迭代',n)
# list是否可迭代
m=isinstance([1,2,3],Iterable)
print('list是否可迭代',m)
# 整数是否可迭代
k=isinstance(123,Iterable)
print('整数是否可迭代',k)

#Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
for i ,value in enumerate(['A','B','C','D']):
    print(i,value)

#同时引用了两个变量
for x,y in [(1,1),(2,2),(3,3)]:
    print(x,y)
