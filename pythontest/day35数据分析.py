"""
使用Pandas做数据分析
pip3 install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pandas
四月，再见
五月，你好
"""

import pandas as pd
# 导入数据集
path = "./res/csv/data.csv"
# 数据集存入一个名为chipo的数据集
chipo = pd.read_csv(path, sep='\t')
# 查看前十行
print(chipo.head(10))
# 数据集中有多少列
print(chipo.shape[1])
# 打印出全部的列名
print(chipo.columns)
# 数据集的索引
print(chipo.index)
# 在name这一列中，一共有多少种
print(chipo['name'].nunique())
