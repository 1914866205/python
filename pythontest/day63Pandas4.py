"""
Pandas_4
"""
import pandas as pd
import numpy as np
# 创建DataFrame的常用方法
df1 = pd.DataFrame([['Tom', 74.0, '2020-05-01'], ['Jerry', '91.5',
                                                  '2020-06-01']], index=['a', 'b'], columns=['name', 'score', 'date'])

print(df1)
# 也可以通过字典
df2 = pd.DataFrame({'name': ['zhang', 'wang'], 'score': [87, 98],
                    'date': ['2020-05-01', '2020-06-01']}, index=['x', 'y'])
print(df2)
# DataFrame增加数据
df2 = df2.append(pd.Series(
    data=['zhao', 93, '2020-02-01'], index=['name', 'score', 'date'], name='z'
))
print(df2)
# DataFrame删除数据，使用drop删除指定索引或标签，删除副本
df2 = df2.drop('z')
print(df2)
# DataFrame修改数据，先根据索引或标签定位到行列再修改
df1.loc['a', 'name'] = 'new name'
print(df1)
# Pandas推荐使用访问接口 iloc(索引访问),loc(标签访问) 访问数据
print(df1.iloc[1:])
print(df1.loc['b', 'name'])
