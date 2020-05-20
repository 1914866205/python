"""
那些操作
"""
from functools import reduce
import random

# 一行代码生成[1.3.5.7...]
# 使用列表生成式，创建列表，观察元素出现规律
a = [2*i+1 for i in (range(10))]
print(a)

# 写一个等差数列，产生一个首项为10，公差为12，末项不大于100的列表
# 使用生成式创建
a = list(range(10, 100, 12))
print(a)

# 一行代码求1到1000内整数的和
# 方法1：使用python内置函数sum求和
s = sum(range(1000))
print(s)
# 方法2：使用 functools模块中的reduce求和
s = reduce(lambda x, y: x+y, range(1000))
print(s)
# 打乱一个列表
# 还有random模块，shuffle函数打乱原来的列表
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)
print(a)
