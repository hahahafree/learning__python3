#!/bin/usr/env python3
# -*- coding:utf-8 -*-

#例子1
def fab_1(x):
    n,a,b = 0,0,1
    while n < x:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'

a_1 = fab_1(5)
print('斐波那契數列x=5:',a_1)

#例子2
def fab_2(x):
    n,a,b = 0,0,1
    L = []
    while n < x:
        L.append(b)
        a,b = b,a+b
        n = n+1
    return L

b_1 = fab_2(6)
print('斐波那契數列x=6:',b_1)

#例子3
class Fab(object):
    def __init__(self,max):
        self.max = max
        self.n ,self.a,self.b = 0,0,1
    def __iter__(self):
        return self
    def __next__(self):#在新的迭代器规则中，迭代器对象应该实现__next__方法，而不是next(python2.0)
        if self.n < self.max:
            r = self.b
            self.a,self.b = self.b,self.a + self.b
            self.n = self.n +1
            return r
        raise StopIteration

c_1 =  Fab(7)
for i in c_1:
        print('斐波那契數列x=7:',i)

#例子4
def fab(x):
    n,a,b = 0,0,1
    while n < x:
        yield b
        a,b = b,a+b
        n = n+1
d_1 = fab(8)
for i in d_1:
    print('斐波那契數列x=8:',i)