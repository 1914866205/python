"""
生成式用法
生成式（推导式）可以用来生产列表，集合和字典
"""

import os
# 列表生成式生成自然数序列
list1 = list(range(1, 11))
print(list1)

# 列表生成式生成自然数平方序列
list2 = [x * x for x in range(1, 11)]
print(list2)

# 可以带条件
list3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list3)
# 列出指定目录下的所有文件和目录名
list4 = [d for d in os.listdir('./res')]
print(list4)

# 结合两个列表的不相等元素
list5 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list5)
# 字典生成式
prices = {
    'AAPL': 191.88,
    'GPPG': 1186.96,
    'INM': 143.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# ‘用股票价格大于100元的股票构成一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)
