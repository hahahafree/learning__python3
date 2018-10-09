#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#我们以自定义一个求绝对值的my_abs函数为例：
x = int(input('请输入整数：'))
def my_abs(x):
    if x >=0:
        return x

    else:
        return -x
print(x,'的绝对值：',my_abs(x))

#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，
# 让代码能运行起来pass语句什么都不做，那有什么用？
# 实际上pass可以用来作为占位符

#pass还可以用在其他语句里，比如：
age_1 = 10
if age_1 >=18:
    pass

#缺少了pass，代码运行就会有语法错误。

#参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
#my_abs(1, 2)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: my_abs() takes 1 positional argument but 2 were given

#数据类型检查可以用内置函数isinstance()实现：
y = int(input('请输入整数：'))
if not isinstance(y,(int,float)):
    raise TypeError('bad operand type')
def my_abs(y):
    if y >=0:
        return y

    else:
        return -y
print(y,'的绝对值：',my_abs(y))

#返回多个值
#比如在游戏中经常需要从一个点移动到另一个点，
# 给出坐标、位移和角度，就可以计算出新的新的坐标：

import math

def move(x_1,y_1,step,angle=0):
    nx_1 = x_1 + step * math.cos(angle)
    ny_1 = y_1 - step * math.sin(angle)
    return nx_1,ny_1
r = move(100,100,60,math.pi / 6)
print('坐标：',r)


