#用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。
print('hello word')
#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出
print('dog','monkey','tiger','duck')
#print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
#print()也可以打印整数，或者计算结果
print(300)
print(100+200)
#对于100 + 200，Python解释器自动计算出结果300，但是，'100 + 200 ='是字符串而非数学公式，Python把它视为字符串
print('100+200=',100+200)
#Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里
name = input('please enter your name:')
print('hello',name)

