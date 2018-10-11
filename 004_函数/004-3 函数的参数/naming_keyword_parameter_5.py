#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查。
#仍以person()函数为例，我们希望检查是否有city和job参数：
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

#但是调用者仍可以传入不受限制的关键字参数：
a =  person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
print(a)

#只接收city和job作为关键字参数。这种方式定义的函数如下：
def person_1(name,age,*,city,job):
    print(name,age,city,job)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
#*后面的参数被视为命名关键字参数。
b = person('Jack', 24, city='Beijing', job='Engineer')
print(b)

#果函数定义中已经有了一个可变参数，
# 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person_3(name, age, *args, city, job):
    print(name, age, args, city, job)

#命名关键字参数可以有缺省值，从而简化调用：
def person_4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数：
c =  person('Jack', 24, job='Engineer')
print(c)
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
# 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person_5(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass