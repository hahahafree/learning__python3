#!/bin/usr/env python3
# -*- coding:utf-8 -*-

a = sorted([1,2,22,3,33,5855,555,45])
print("[1,2,22,3,33,5855,555,45],小到大排序：",a)

#接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
b = sorted([36,1,2,2],key=abs)
print("[36,1,2,2],按绝对值大小排序：",b)
#字符串排序的例子：
c= sorted(['apple','banana','boy','time'])
print("['apple','banana','boy','time'],字符串排序:",c)
#给sorted传入key函数，即可实现忽略大小写的排序：
d = sorted(['apple','banana','boy','time'],key=str.lower)
print("['apple','banana','Boy','Time'],忽略大小写的排序：",d)
#反向排序，不必改动key函数，可以传入第三个参数reverse=True：
f = sorted(['Apple','Banana','boy','time'],key=str.lower,reverse = True)
print("['apple','banana','boy','time']反向排序",f)
#用一组tuple表示学生名字和成绩：
#用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Dart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print("按名字排序：",L2)

def by_score(t):
    return -t[1]
L3 = sorted(L, key=by_score)
print("按成绩从高到低排序：",L3)