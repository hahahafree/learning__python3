#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
#举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list
names = ['banana','apple','fish','tortoise']
scores = [90,80,70,60]
print('banana的成绩：',str(scores[0]))
#如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
# 用Python写一个dict如下
d_1 = {'banana':90,'apple':80,'fish':70,'tortoise':60}
print('apple的成绩：',d_1['apple'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d_1['peach'] = 50
print(d_1)
#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d_1['peach'] = 40
print(d_1)
d_1['peach'] = 30
print(d_1)
#如果key不存在，dict就会报错
#d['Thomas']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'Thomas'
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
if 'girl' in d_1:
    print('True')
else:
    print('False')
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print('fis存在？',d_1.get('fis',0))
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d_1)
d_1.pop('fish')
print(d_1)
#和list比较，dict有以下几个特点：

    #查找和插入的速度极快，不会随着key的增加而变慢；
    #需要占用大量的内存，内存浪费多。
#而list相反：

    #查找和插入的时间随着元素的增加而增加；
    #占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。
