#整数
#十进制
print(0)
print(1)
print(-1)
#十六进制
print(0xffff)

#浮点数
print(1.2)
#次方运算
print(1.2*10**9)
#用e代替10
print(1.2e9)
print(1.2e-9)

#字符串
#单引号'
print('ok')
#双引号"
print("ok")
#单引号'本身是一个字符，可以用""括起来
print("ok'ok")
#如果字符串内部既包含'又包含"怎么办？
# 可以用转义字符\来标识
print('你\'好\"吗"？')
#比如\n表示换行
print('哈哈\n哈')
#\t表示制表符
print('哈\t哈')
#字符\本身也要转义，所以\\表示的字符就是\
print('\\哈哈哈\\')
#Python还允许用r''表示''内部的字符串默认不转义
print(r'哈哈\n哈\n哈哈')
print('哈哈\n哈哈\n哈哈')
#如果字符串内部有很多换行，用\n写在一行里不好阅读
# 为了简化，Python允许用'''...'''的格式表示多行内容
print('''哈哈哈
哈哈哈
哈哈哈''')
#多行字符串'''...'''还可以在前面加上r使用
print(r'''哈哈哈,\n
哈哈哈''')

#布尔值
#布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False
# 在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来
print(True)
print(False)
print(10>15)
print(15>10)
#布尔值可以用and、or和not运算
#and运算是与运算，只有所有都为True，and运算结果才是True
print(True and True)
print(True and False)
print(False and False)
print(15>10 and 100>15)
#or运算是或运算，只要其中有一个为True，or运算结果就是True
print(True or True)
print(True or False)
print(False or False)
print(15>10 or 100>15)
#not运算是非运算，它是一个单目运算符，把True变成False，False变成True
print(not True)
print(not False)
print(not 10>15)
#布尔值经常用在条件判断中
height =int(input("请输入你的身高："))
if height >= 150:
    print('长大了')
else:
    print('小屁孩')

#空值是Python里一个特殊的值，用None表示。
# None不能理解为0，因为0是有意义的，而None是一个特殊的空值
