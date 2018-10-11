#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。
# 在调用该函数时，可以只传入必选参数：
a = person('apple',5)
print(a)

#也可以传入任意个数的关键字参数
b= person('banana',3,city='Hainan')
print(b)
c = person('pear',1,height='10',weight='2')
print(c)

#和可变参数类似，也可以先组装出一个dict，
# 然后，把该dict转换为关键字参数传进去：
extra = {'city':'Beijing','job':'Engineer'}
d=person('Jack',24,city=extra['city'],job=extra['job'])
print(d)

#当然，上面复杂的调用可以用简化的写法：
f = person('Jack',24,**extra)
print(f)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
