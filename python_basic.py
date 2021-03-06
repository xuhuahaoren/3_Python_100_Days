'''
Python语言基础
'''

#----------1 Python数据类型
#----------1.1 字符串
# 在Python中用引号引起来的字符集称之为字符串，比如：'hello'、"my Python"、"2+3"等都是字符串
# Python中字符串中使用的引号可以是单引号、双引号跟三引号
print('hello, world!')

c = 'It is a "dog"!'
print(c)

c1 = "It's a dog!"
print(c1)

c2 = """hello
world
!"""
print(c2)

# 转义字符'\'可以转义很多字符，比如\n表示换行，\t表示制表符 (Tab)，字符\本身也要转义，所以\表示的字符就是\
print('It\'s a dog!')
print("hello world!\nhello Python!")
print('\\\t\\')

# 原样输出引号内字符串可以使用在引号前加r
print(r'\\\t\\')

# 子字符串及运算
s = 'Python'
print('Py' in s)
print('py' in s)

# 取子字符串有两种方法，使用[]索引或者切片运算法[:]，这两个方法使用面非常广
print(s[2])
print(s[1:4])

# 字符串连接与格式化输出
word1 = '"hello"'
word2 = '"world"'
sentence = word1.strip('"') + ' ' + word2.strip('"') + '!'  # strip()函数会根据函数体内的字符来扫描字符串从左到右
                                                            # 删除前导和尾随的函数体内相应字符得到字符串的相应副本。
print('The first word is %s, and the second word is %s' %(word1, word2))
print(sentence)

#----------1.2 整数与浮点数
# 整数
# Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样
i = 7
print(i)

print(7 + 3)
print(7 - 3)
print(7*3)
print(7**3)
print(7/3)  # Python3之后，整数除法和浮点数除法已经没有差异
print(7%3)  # 余数
print(7//3)  # 商

# 浮点数
print(7.0/3)
print(3.14*10**2)

# 其他表示方法
print(0b1111)
print(0xff)
print(1.2e-5)

# 更多运算
import math
print(math.log(math.e))

#----------1.3 布尔值
print(True)
print(False)
print(True and False)
print(True or False)
print(not True)
print(18 >= 6*3 or 'py' in 'Python')
print(18 >= 6*3 and 'py' in 'Python')
print(18 >= 6*3 and 'Py' in 'Python')

#----------1.4 日期时间
import time
now = time.strptime('2016-07-20', '%Y-%m-%d')  # 根据指定的格式把一个时间字符串解析为时间元组
print(now)

print(time.strftime('%Y-%m-%d', now))  # 用于格式化时间，返回以可读字符串表示的当地时间，格式由参数 format 决定。

import datetime
someDay = datetime.date(1999, 2, 10)
anotherDay = datetime.date(1999, 2, 15)
deltaDay = anotherDay - someDay
print(deltaDay.days)

# 查看变量类型
print(type(None))
print(type(1.0))
print(type(True))
s = 'NoneType'
print(type(s))

# 类型转换
print(str(10086))
print(float(10086))
print(int('10086'))
print(complex(10086))

#----------2 Python数据类型----------------------------------------------------------------------------------------------
# 列表（list），元组（tuple），集合（set），字典（dict）
#----------2.1 列表（list）
# 用来存储一连串元素的容器，列表用[]来表示，其中元素的类型可不相同。
mylist = [0, 1, 2, 3, 4, 5]
print(mylist)

# 列表索引和切片
# 索引从0开始，含左不含右
print('[4]=', mylist[4])  # 4
print('[-4]=', mylist[-4])  # 2
print('[0:4]=', mylist[0:4])  # [0, 1, 2, 3]
print('[:4]=', mylist[:4])  # [0, 1, 2, 3]
print('[4:]=', mylist[4:])  # [4, 5]
print('[0:4:2]=', mylist[0:4:2])  # [0, 2]
print('[-5:-1:]=', mylist[-5:-1:])  # [1, 2, 3, 4]
print('[-2::-1]=', mylist[-2::-1])  # [4, 3, 2, 1, 1]

# 修改列表
mylist[3] = "小月"
print(mylist[3])
mylist[5] = "晓楠"
print(mylist[5])
mylist[5] = 19787
print(mylist[5])
print(mylist)

# 插入元素
mylist.append('han')
mylist.extend(['long', 'wan'])  # 用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(mylist)

scores = [90, 80, 75, 66]
mylist.insert(1, scores)  # 添加到指定位置
print(mylist)

# 删除元素
print(mylist.pop(1))  # 该函数返回被弹出的元素，不传入参数则删除最后一个元素
print(mylist)

# 判断元素是否在列表中
print('wan' in mylist)
print('han' not in mylist)

print(mylist.count('wan'))
print(mylist.index('wan'))

# range函数生成整数列表
print(range(10))
print(range(-5, 5))
print(range(-10, 10, 2))
print(range(16, 10, -1))


#----------2.2 元组（tuple）
# 元组类似列表，元组里面的元素也是进行索引计算。列表里面的元素的值可以修改，而元组里面的元素的值不能修改，只能读取。
# 元组的符号是()。
studentsTuple = ("ming", "jun", "qiang", "wu", scores)
print(studentsTuple)

try:
    studentsTuple[1] = 'fu'
except TypeError:
    print('TypeError')

scores[1] = 100  # 元组内的列表可以更改元素数值
print(studentsTuple)

print('ming' in studentsTuple)  # 元组支持判断元组内元素是否存在
print(studentsTuple[:4])
print(studentsTuple.count('ming'))
print(studentsTuple.index('jun'))
print(len(studentsTuple))
