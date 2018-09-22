#可变list
t_1 = ['apple','banana']
t_2 = ['pear','mango']
#不可变tuple
t_3 = ('peach','red dates',t_1,t_2)
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
t_1.append('cantaloupe')
t_2.append('watermelon')
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
