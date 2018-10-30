#!/bin/usr/env python3
# -*- coding:utf-8 -*-

#由于非字符串类型没有lower()方法，所以列表生成式会报错：
#L = ['Hello', 'World', 18, 'Apple', None]
# [s.lower() for s in L]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 1, in <listcomp>
#AttributeError: 'int' object has no attribute 'lower'

#使用内建的isinstance函数可以判断一个变量是不是字符串：

x = 'abc'
y = 123
a = isinstance(x,str)
b = isinstance(y,str)
print('x是字符串？',a,'\ny是字符串？',b)
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [h.lower() for h  in L1 if isinstance(h,str) is True]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')