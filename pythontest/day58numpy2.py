"""
Numpy2
"""
import numpy as np

# 组合 ndarray对象
a = np.arange(10).reshape(2, -1)
print(a)
# 找出a中大于3的元素索引
# 返回一个元组，带有2个ndarray对象
# 分别表示大于3的元素第一位，第二维度中的位置
b = np.array(np.where(a > 3))
print(b)
# 使用np.transpose方法转置后，结果就能看懂了
print(np.transpose(b))
# 创建一个[3,5] 所有元素为True的数组
a = np.ones((3, 5), dtype=bool)
# 一维转二维
a = np.linspace(1, 5, 10)
print(a.reshape(5, 2))
# 提取出数组中的奇数
m = np.arange(10).reshape(2, 5)
print(m[m % 2 == 1])
