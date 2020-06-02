"""
数据分析案例————猫眼电影
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.用pandas导入数据集
# read_csv 使用说明
# 第一个参数表示文件的相对路径
# 第二个关键字参数：delimiter='::',表示文件分隔符使用 ::
# 后面几个关键字参数分别代码使用的引擎，文件没有表头，所有header为None
# 导入后 DataFrame 的别名，使用 names关键字设置
path = './res/csv/maoyan.csv'
df = pd.read_csv(path, sep=',', encoding='utf=8', index_col=False)
# drop函数用法：DataFrame.drop(labels=None,axis=0,index=None,columns=None,inplace=False)
# 参数说明:
# labels 就是要删除的行列的名字，用列表给定
# axis 默认为0，指删除行，因此删除columns是要知道axis=1
# index直接指定要删除的行
# columns 直接指定要删除的列
# inplace=False,默认该删除操作不改变原数据，而是返回一个执行删除操作之后的新的dataFrame
# inplace=True,则会直接在原数据上进行删除，删除后无法返回

# 从数据中删除第一列  电影编号
df.drop(df.columns[0], axis=1, inplace=True)
# 滤掉缺失数据
df.dropna(inplace=True)
# 删除重复数据
df.drop_duplicates(inplace=True)
# 查看数据
df.head(10)
print(df)

# 查看数据的结构
df.info()
print(df.columns)
print(df.shape)

# 数据可视化，不加以下设置，图表标题等会中文乱码
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # mac系统中文显示
plt.rcParams['font.sans-serif'] = ['./res/font/SimHei.ttf']  # Ubuntu做法
# 年份&上映电影的数目，剔除2018年的数据
fig, ax = plt.subplots(figsize=(9, 6), dpi=70)
df[df[u'上映时间'] < 2018][u'上映时间'].value_counts(
).sort_index().plot(kind='line', ax=ax)
ax.set_xlabel(u'时间（年）')
ax.set_ylabel(u'上映数量')
ax.set_title(u'上映时间&上映的电影数目')
plt.savefig('./res/img/mapyan1.png')
plt.show()

# 上映时间&上映数量&评分的关系图
x = df[df[u'上映时间'] < 2018][u'上映时间'].value_counts().sort_index().index
y = df[df[u'上映时间'] < 2018][u'上映时间'].value_counts().sort_index().values
y2 = df[df[u'上映时间'] < 2018].sort_values(
    by=u'上映时间').groupby(u'上映时间').mean()[u'评分'].values
fig, ax = plt.subplots(figsize=(10, 5), dpi=70)
ax.plot(x, y, label=u'上映数量')
ax.set_xlim(1980, 2017)
ax.set_xlabel(u'上映时间')
ax.set_ylabel(u'上映数量')
ax.set_title(u'时间&上映数量&评分均值')
ax2 = ax.twinx()
ax2.plot(x, y2, c='y', ls='--', label=u'评分')
ax.legend(loc=1)
ax2.legend(loc=2)
plt.savefig('./res/img/maoyan2.png')
plt.show()

# 世界&上映时间&均值评分
fig, ax = plt.subplots(figsize=(10, 7), dpi=60)
df[df[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].plot(kind='line', ax=ax)
ax.set_ylabel(u'评分')
ax.set_title(u'世界&上映时间&均值评分')
plt.savefig('./res/img/maoyan3.png')
plt.show()
