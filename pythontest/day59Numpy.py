"""
Numpy_3
"""
import numpy as np
v1 = np.arange(5)
print('输出v1:')
print(v1)
# 按照元素顺序逐个加2
print('输出v1+2:')
print(v1+2)
# 执行v1 * v1，矩阵的乘法是按照元素逐个相乘
print('输出v1*v1')
print(v1*v1)
# 5行2列矩阵  取值为[1-10]的随机整数
v2 = np.random.randint(1, 10, (5, 2))
print('输出v2:')
print(v2)
# 此时无法直接将两个矩阵相乘， why?
# print(v1*v2)
# 1.使用dot函数实现矩阵乘法
v3 = np.dot(v1, v2)
print('使用dot函数实现矩阵相乘的结果：')
print(v3)
# 输出矩阵的形状，也就是行列维度
print('输出v3的shape')
print(v3.shape)
# 2.转化为matirx对象，再相乘
v3 = np.matrix(v1)*np.matrix(v2)
print('转化为matirx对象，再相乘的结果')
print(v3)
