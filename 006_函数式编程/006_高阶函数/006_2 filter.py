#!/bin/usr/env python3
# -*- coding:utf-8 -*-

#在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1
a1 = list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
print('list仅保留奇数：',a1)

def not_empty(s):
    return s and s.strip()
a2 = list(filter(not_empty,['A','','B',None,'C','']))
print('去掉空字符串：',a2)

