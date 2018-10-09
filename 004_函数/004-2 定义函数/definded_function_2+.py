#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0
#的两个解。
#提示：计算平方根可以调用math.sqrt()函数：
import math


def quadratic(a_1,b_1,c_1):

    a = int(a_1)
    b = int(b_1)
    c = int(c_1)

    data_1 = b ** 2 - 4 * a * c
    data_2 = math.sqrt(data_1)
    if a == 0:
        print('输入错误！',a,'x^2+bx=c不是一元二次方程！')
    elif data_1 < 0:
        print('原方程无实根！')
    elif data_1 == 0:
        x = -(b/(2*a))
        x1 = x
        x2 = x

    elif data_1 >0:
        x1 = (-b+data_2)/(2*a)
        x2 = (-b-data_2)/(2*a)
        return x1, x2



print(quadratic(2,3,1))
