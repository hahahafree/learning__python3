#Python的字符串支持多语言
print('你好string')
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
print(ord('S'))
print(ord('你'))
# chr()函数把编码转换为对应的字符
print(chr(66))
print(chr(25991))
#如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587')
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
x_1 = b'String'
print(x_1)
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('String_1'.encode('ascii'))
print('你好'.encode('utf-8'))
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
#在bytes中，无法显示为ASCII字符的字节，用\x##显示
#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法
#如果bytes中包含无法解码的字节，decode()方法会报错
print(b'String'.decode('ascii'))
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
#要计算str包含多少个字符，可以用len()函数
print(len('String'))
print(len('你好'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print(len(b'Stirng'))
print(len(b'\xe4\xbd\xa0\xe5\xa5\xbd'))
print(len('你好'.encode('utf-8')))
#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
#如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文
#在Python中，采用的格式化方式和C语言是一致的，用%实现
#整数用%d
print('%d'%300)
#浮点数用%f
print('%f'%3.00)
#浮点数用%.nf,n表示小数点后多少位
print('%.3f'%3.1415926)
#字符串用%s
print('%s'%'你好')
#十六进制整数用%x
print('%x'%0xffff)
#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('name: %s \n height: %s' %('freedom',180))
#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('width: %d %%' %10)
#另一种格式化字符串的方法是使用字符串的format()方法
# 它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hi,{0},好久不见{1:.1f}%'.format('小何',10.12))
#小明的成绩从去年的72分提升到了今年的85分
# 请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位
percent_1 = (85-72)/72*100
print("小明同学成绩提升了：%.1f%%"%percent_1)
