#可变list
t_1 = ['apple','banana']
t_2 = ['pear','mango']
#不可变tuple
t_3 = ('peach','red dates',t_1,t_2)

#长度
print(len(t_3))
#元素
print(t_1)
print(t_2)
#换行输出
print(t_1,"\n",t_2)

print(t_3)
#索引访问list中每一个位置的元素，记得索引是从0开始的(顺序法)
print(t_3[3],t_3[2],t_3[1],t_3[0])
#当索引超出了范围时，Python会报一个IndexError错误
#用-1做索引（倒序法）
print(t_3[-1],t_3[-2],t_3[-3],t_3[-4])
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
t_1.append('cantaloupe')
t_2.append('watermelon')
print(t_1)
print(t_2)
#可以把元素插入到指定的位置，比如索引号为1的位置
t_1.insert(2,'peanut')
t_2.insert(1,'water')
print(t_1)
print(t_2)
#要删除list末尾的元素，用pop()方法
t_4 = t_1.pop()
print(t_4)
print(t_1)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
t_5 = t_2.pop(0)
print(t_5)
print(t_2)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
print(t_1)
t_1[0] = 'rice'
print(t_1)
#list里面的元素的数据类型也可以不同
t_7 = ['food',123,True]
print(t_7)
#list元素也可以是另一个list
t_8 = ['green vegetable','rice',['salad','hot pepper'],'tomatoes']
print(t_8)
#如果拆开写就更容易理解
t_9 = ['salad','hot pepper']
t_10 = ['green vegetable','rice',t_9,'tomatoes']
print(t_10)
