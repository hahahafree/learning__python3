#!/bin/usr/env python3
# -*- coding:utf-8 -*-

#通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#不返回求和的结果,返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
            return ax
        return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1,5,6,7)
b = f()

print(f())





