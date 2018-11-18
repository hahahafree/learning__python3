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

#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
# 需要用list()函数获得所有结果并返回list。
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x % n >0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
