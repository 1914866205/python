"""
使用Pandas做数据清洗和特征工程
1.如何进行数据探索性分析（EDA）
2.学会数据分析的基本思维，基本技能和工具
包括：使用数据分析常用的工具numpy和pandas，绘图工具matplotlib和pyecharts
"""
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Bar, Grid, Line, Pie
import pyecharts.options as opts
from pyecharts.globals import ThemeType
# resd_csv使用说明
# 第一个参数表示文件的相对路径
# 第二个关键字参数表示文件分隔符
# 后面的关键字参数分别代表使用的引擎，文件没有表头，所以header为None
# 导入后DataFrame的列名，使用names关键字设置

# 1.导入电影数据文件 movies.dat  包括三个字段，Movie ID,Movie Title,Genre
# 分别别说电影 ID，名称，题材，多个中间用 | 分割
movies = pd.read_csv('./res/csv/movies.dat', delimiter='::', engine='python',
                     header=None, names=['Movie Id', 'Movie Title', 'Genre'], encoding='utf-8')

movies.head()  # 定位到起始行 34436行

# 2. 导入用户相关的数据文件,  users.dat
# 包括两个字段 用户ID  Twitter Id
users = pd.read_csv('./res/csv/users.dat', delimiter='::',
                    engine='python', header=None, names=['User ID', 'Twitter ID'], encoding='utf-8')
users.head()  # 60283       rows*2  columns

# 3.导入评分数据  rating.data 包括四个字段
# 用户ID  电影ID 评分  评分时间
ratings = pd.read_csv('./res/csv/ratings.dat', delimiter='::', engine='python', header=None,
                      names=['User  ID', 'Movie  ID', 'Rating', 'Rating Timestamp'], encoding='utf-8')


ratings.head()    # 814505  *   4  columns

# 数据预览 Pandas提供2个很好的方法  info  describe
#  info  统计出数据的每一列的类型，是否为null和个数
# describe 描述出数据的每一列的统计学属性元素，包括常见的平均值，方差，中位数，分位数等
movies.info()  # 打印结果分析 共 34437行数据，前两行没有空值，只有Genere列  34159存在空值，  807.2KB
users.info()
ratings.info()

ratings.describe()  # 电影评论的平均得分  7.30  方差大于 1.86
# 电影评论的得分是一个重要的特征列，可以绘制频率分布直方图和箱型图，直观的感受评分的分布、
# 25%的电影得分在0-6分，6-7分的电影有25%  7-9和9分以上的也是25%
plt.figure(figsize=[8, 8])
plt.savefig('./res/img/moviel.png')
# plt.show()
plt.figure(figsize=[8, 8])
plt.boxplot(x=ratings['Rating'], showmeans=True, meanline=True)
plt.grid()
plt.savefig('./res/img/movie2.png')

#
# 使用value_counts方法统计电影种类的取值数

# 结果显示有2693种，因为一个电影可能有多种类型，中间用 |  分割
genre_count = movies['Genre'].value_counts()
print(genre_count)
# 根据分隔符 |  解析字符串，然后统计每个子串出现的次数
# 填充 Gnres 列的空值，填充为 others 类型
movies['Genre'].isnull().sum()/len(movies['Genre'])  # 打印下空值比例
movies['Genre'].fillna('others', inplace=True)
# 根据分隔符  |  解析此列 并将此列转为Numpy对象
genres = movies['Genre'].str.split('|').to_numpy()
# 使用 defaultdict统计出电影种类和对应电影数
counter = defaultdict(int)
for genre in genres:
    for e in genre:
        counter[e] += 1
print(counter)
# 一共 29/ 种电影，按照上面字典按种类排序
counter_sorted = sorted(counter.items(), key=lambda x: x[1])
print(counter_sorted)
# 取电影种类最多的前10进行分析
top10 = counter_sorted[-10:]
# 绘制前10最多种类数的柱状图，使用pyecharts绘制
x = [x for x, y in top10]
y = [y for x, y in top10]
bar = (
    Bar(init_opts=opts.InitOpts(height='1200px'))
    .add_xaxis(x)
    .add_yaxis('电影种类名', y, category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title='电影种类及影片数'),
                     toolbox_opts=opts.ToolboxOpts())
)
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
)

grid.render(path='./res/html/moviel.html')
