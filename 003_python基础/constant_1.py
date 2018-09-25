#常量
#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。
# 在Python中，通常用全部大写的变量名表示常量
#但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359
print(PI)
#在Python中，有两种除法，一种除法是/
#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
print(10/3)
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数
print(10//3)
#所以Python还提供一个余数运算，可以得到两个整数相除的余数
print(10%3)