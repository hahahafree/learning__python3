#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。
#可以直接从Python的官方网站查看文档：http://docs.python.org/3/library/functions.html#abs
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息
#调用abs函数:
print('abs(-10)=',abs(-10))
print('abs(10)=',abs(10))

x = -100
y = 100
print('x = -100,y = 100的绝对值:',abs(x),abs(y))
#调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
#Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个
#abs(1, 2)
#Traceback (most recent call last):
 # File "<stdin>", line 1, in <module>
#TypeError: abs() takes exactly one argument (2 given)

#如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
#并且给出错误信息：str是错误的参数类型
#abs('a')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: bad operand type for abs(): 'str'

#max函数max()可以接收任意多个参数，并返回最大的那个：
print('max(1,2,3,4,5)=',max(1,2,3,4,5))
print('max(-1,2,3,4,-5)=',max(-1,2,3,4,-5))

#min()
print('min(1,2,3)=',min(1,2,3))

#sum()
print('sum(1,2,3)=',sum([1,2,3]))

#数据类型转换
#Python内置的常用函数还包括数据类型转换函数
# 比如int()函数可以把其他数据类型转换为整数：
print('int("123")=',int('123'))
print('float("12.3")=',float('12.3'))
print('str(1.2)=',str(1.2))
print('bool(1)=',bool(1))
print('bool('')=',bool(''))

#函数名其实就是指向一个函数对象的引用
# 完全可以把函数名赋给一个变量
# 相当于给这个函数起了一个“别名”：
a = abs # 变量a指向abs函数
print('a=abs(-1)=',a(-1)) # 所以也可以通过a调用abs函数

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print('255的16进制：',str(hex(n1)))
print('1000的16进制：',str(hex(n2)))