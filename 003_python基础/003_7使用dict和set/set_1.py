#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
set_1 = set([1,2,3])
print(set_1)
#重复元素在set中自动被过滤
set_2 = set([1,2,3,3,2,1])
print(set_2)
#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
set_1.add(4)
print(set_1)
set_1.add(4)
print(set_1)
#通过remove(key)方法可以删除元素
set_1.remove(1)
print(set_1)
#set可以看成数学意义上的无序和无重复元素的集合
# 因此，两个set可以做数学意义上的交集、并集等操作
print(set_1)
print(set_2)
#交集
set_3 = set_1 & set_2
print('交集',set_3)
#并集
set_4 = set_1 | set_2
print('并集',set_4)
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a = ['c','b','d']
a.sort()
print(a)
#而对于不可变对象，比如str，对str进行操作呢
a_1 = 'dfg'
print(a_1)
b = a_1.replace('d','h')
print(b)