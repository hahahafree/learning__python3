#!/bin/usr/env python3
# -*- coding:utf-8 -*-

def f(x):
    return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
r1=list(r)
print('1-9的平方：',r1)


q = list(map(str,[1,2,3,4,5,6,7,8]))
print('字符串：',q)

#reduce的用法
from functools import reduce
def add(x,y):
    return x + y
w = reduce(add,[1,3,5,7,9])
print('1-9奇数和：',w)

#[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x * 10 + y
a = reduce(fn,[1,3,5,7,9])
print('13579:',a)

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
s1 = reduce(fn,map(char2num,'13579'))
print('字符串转整数',s1)

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    name = name.lower()
    return name[0].upper() + name[1:]

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x,y : x * y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]

    n = len(s)
    for i in range(n):
        if s[i] == ".":
            break

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456')- 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

