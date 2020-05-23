"""
NumPy数值计算练习起步
"""
import numpy as np

# 通过构造函数array 创建一维 array
v = np.array([1, 2, 3, 4])
print(v)
# 创建二维 array
m = np.array([[1, 2], [3, 4]])
print(m)
# v 和 m的类型都是 ndarray.NumPy 中最主要的数据结构
print(type(v), type(m))
# 指定范围内的数组
ara = np.arange(1, 10)
print(ara)

# 在指定的间隔内返回num均匀分布的样本
print(np.linspace(1, 10, 15))
