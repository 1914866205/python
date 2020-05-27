"""
Pandas_1
"""
import pandas as pd
# Padnas读取 URL 路径的文件，得到（149 rows * 5 columns）的数据集
result = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

print(result)
# 创建比保存数据
d = {'id': [1, 2], 'name': ['gz', 'lh'], 'age': [10, 12]}

df = pd.DataFrame(d)
# test.csv 文件分隔符为 \t ，如果使用 sep 默认的逗号分隔符，读入后的数据混为一体
df.to_csv('test.csv', sep='\t')
# 读取数据，查看结果
df = pd.read_csv('test.csv')
print(df)
# set 必须设置为 '\t'，数据分割才会正常
df = pd.read_csv('test.csv', sep='\t')
print(df)

# 读取之列选择属性
# 参数用于选择数据文件的哪些列到 DataFrame 中
# 只想使用源数据文件的id和age两列,那么可以为usecols参数赋值为['id','name']
df = pd.read_csv('test.csv', delim_whitespace=True, usecols=['id', 'name'])
print(df)
