#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

#比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现
age = 18
if age >= 18:
    print('你的年龄是：',age)
    print('长大了！')

#给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了
if age >= 20:
    print('你的年龄是：',age)
    print('长大了！')
else:
    print('你的年龄是：',age)
    print('teenager')

#当然上面的判断是很粗略的，完全可以用elif做更细致的判断
if age >= 20:
    print('你的年龄是：',age)
    print('长大了！')
elif age >= 10:
    print('adult')
else:
    print('你的年龄是：',age)
    print('teenager')
#elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是
#if <条件判断1>:
#    <执行1>
#elif <条件判断2>:
#    <执行2>
#elif <条件判断3>:
#    <执行3>
#else:
#   <执行4>
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
if age >= 20:
    print('你的年龄是：',age)
elif age >= 10:
    print('adult')
else:
    print('teenager')
#if判断条件还可以简写，比如写
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = 10
if x:
    print('True')
#input()读取用户的输入，这样可以自己输入
birth_1 = input('birth:')
birth = int(birth_1 )
if birth <2000:
    print('90后？')
else:
    print('00后')
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果
height =input('请输入你的身高：')
weight = input('请输入你的体重：')
height_1 = int(height)
weight_1 = int(weight)

bmi = (height_1 / weight_1)**2
if bmi < 18.5:
    print('你的体重过轻')
elif 18.5 <= bmi <25 :
    print('你的体重正常！')
elif 25 <= bmi < 28 :
    print('你的体重过重！')
elif 28 <= bmi < 32 :
    print('你的体重肥胖！')
else:
    print('你的体重严重肥胖！')