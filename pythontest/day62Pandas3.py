"""
Pandas_3
"""
import pandas as pd
import numpy as np
# Series 是pandas两大数据结构中（DataFrame,Series)的一种
# 每个Series对象都是由两个数组成
# index:它是从NumPy 数组继承的Index对象，保存标签信息
# values:保存值为NumPy

# 1. 创建一个series
# Series的标准构造函数：Series(data=None,index=None,dtype=None,name=None)
ps = pd.Series(data=[-3, 2, 1], index=['a', 'f', 'b'], dtype=np.float32)
print(ps)
print('----------------------')
# 2.Series增强元素（Pandas运行包含重复的标签）
ps = ps.append(pd.Series(data=[-8.0], index=['f']))
print(ps)
print('-------------------')
# 3.Series访问元素，有两种方式
# 通过索引访问
print(ps[2])
# 通过标签访问
print(ps['f'])
# 4.Series之删除元素，append操作和drop操作都是发生在原数据的副本上，不是原书记
ps = ps.drop('f')
print(ps)
print('------------------')
# 5.Series 之修改元素
ps['b'] = 10.0
print(ps)
