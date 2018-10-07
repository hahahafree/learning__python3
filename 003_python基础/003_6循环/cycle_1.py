#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names = ['banana','apple','pear']
for name in names:
    print(name)
#for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
#比如我们想计算1-10的整数之和，可以用一个sum变量做累加
sum = 0
sum_1 = [1,2,3,4,5,6,7,8,9,10]
for x_1 in sum_1:
    sum = sum + x_1
print('1-10的整数之和：',sum)
#如果要计算1-100的整数之和，从1写到100有点困难
# 幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数
list_1 = list(range(5))
print(list_1)
#range(101)就可以生成0-100的整数序列
sum_2 = range(101)
sum_3 = 0
for x_2 in sum_2:
    sum_3 = sum_3 + x_2
print(sum_3)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
# 比如我们要计算100以内所有奇数之和，可以用while循环实现
sum_4 = 0
sum_5 = 99
while sum_5 >0:
    sum_4 = sum_4 + sum_5
    sum_5 =sum_5 - 2
print(sum_4)
#在循环中，break语句可以提前退出循环

sum_6 = 1
while sum_6 <= 10:
    if sum_6 > 5:
        break
    print(sum_6)
    sum_6 = sum_6 + 1
print('END')
#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
sum_7 = 0
while sum_7 <= 10:
    sum_7 = sum_7 + 1
    if sum_7 %2 == 0:
        continue
    print(sum_7)