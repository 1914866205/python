"""
列表生成高效案例
"""

# 1.对每个元素的乘方操作后，利用列表生成式返回一个新的列表
from random import random
a = range(0, 11)
b = [x**2 for x in a]
print(b)

# 2.数值型的元素列表，转换为字符串类型的列表
a = range(0, 10)
b = [str(i) for i in a]
print(b)

# 3.生成 10 个 0到 1的随机浮点数，保留小数点后两位
a = [round(random(), 2)for _ in range(10)]
print(a)

# 4. 对一个列表里面的数据筛选，值计算 [0,11)中的偶数平方
a = range(11)
b = [x**2 for x in a if x % 2 == 0]
print(b)

# 5.zip和列表
a = range(5)
b = ['a', 'b', 'c', 'd', 'e']
c = [str(y)+str(x) for x, y in zip(a, b)]
print(c)

# 6.打印键值对
a = {'a': 1, 'b': 2, 'c': 3}
b = [k+'='+str(v) for k, v in a.items()]
print(b)
