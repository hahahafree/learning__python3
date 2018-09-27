#tuple一旦初始化就不能修改
t_1 = ('dog','cat','chicken','duck')
print(t_1)
#它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，
# 但不能赋值成另外的元素
#如果要定义一个空的tuple，可以写成()
t_2 = ()
print(t_2)
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t_3 = (1,)
print(t_3)
#最后来看一个“可变的”tuple
t_4 = ('peach','red dates',t_1,t_2)
print(t_4)