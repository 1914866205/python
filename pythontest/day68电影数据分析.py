"""
使用Pandas做数据清洗和特征工程；
1.如何进行数据探索性分析 (EDA)
2.学会数据分析的基本思维、基本技能和工具
包括：使用数据分析常用工具 numpy 和 pandas，绘图工具 matplotlib 和 pyecharts
@Date 2020.06.03
"""
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyecharts.charts import Bar, Grid, Line, Pie
import pyecharts.options as opts
from pyecharts.globals import ThemeType


# read_csv 使用说明
# 第一个参数表示文件的相对路径
# 第二个关键字参数表示文件分隔符
# 后面几个关键字参数分别代表使用的引擎，文件没有表头，所以 header 为None
# 导入后 DataFrame 的列名，使用 names 关键字设置，这个参数比较有用


# 1.导入电影数据文件 movies.dat，包括3个字段：Movie ID, Movie Title, Genre
# 分别表示电影 ID、电影名称、题材（可能属于多个题材，中间用 | 分割）
movies = pd.read_csv('./res/csv/movies.dat', delimiter='::',
                     engine='python', header=None, names=['Movie ID', 'Movie Title', 'Genre'], encoding='utf-8')
movies.head()  # 定位到起始行，34436行


# 2.导入用户相关的数据文件 users.dat，包括两个字段：用户ID, Twitter ID
users = pd.read_csv('./res/csv/users.dat', delimiter='::',
                    engine='python', header=None, names=['User ID', 'Twitter ID'], encoding='utf-8')
users.head()  # [60283 rows x 2 columns]


# 3.导入评分记录 rating.data，包括四个字段：用户ID，电影ID，评分，评分时间
ratings = pd.read_csv('./res/csv/ratings.dat', delimiter='::',
                      engine='python', header=None, names=['User ID', 'Movie ID', 'Rating', 'Rating Timestamp'], encoding='utf-8')
ratings.head()  # [814505 rows x 4 columns]


# 4.数据预览：Pandas 提供 2 个很好用的方法：info、describe
# info 统计出数据的每一列类型，是否为 null 和个数；
# describe 描述出数据每一列的统计学属性信息，包括常见的平均值、方差、中位数、分位数等。
movies.info()  # 打印结果分析：共34437行数据，前两列没有空值，只有Genre列（34159）存在空值，占807.2+KB
users.info()
ratings.info()


ratings.describe()  # 电影评论的平均得分为 7.30, 方差大约 1.86
# 电影评论得分是一个重要特征列，可以绘制频率分布直方图和箱型图，直观感受评论得分的分布情况
# 25 % 的电影得分在 0~6 分，6~7 分的电影又有 25 %， 7~9 分的电影又有 25 %，9 分以上的电影占有 25%


plt.figure(figsize=[8, 8])
plt.hist(x=ratings['Rating'], color=['orange'])
plt.savefig('./res/img/movie1.png')
# plt.show()
plt.figure(figsize=[8, 8])
plt.boxplot(x=ratings['Rating'], showmeans=True, meanline=True)
plt.grid()
plt.savefig('./res/img/movie2.png')
plt.show()


# 使用 value_counts 方法统计电影种类的取值数
# 结果显示有 2693 种，超乎想象，原因一部电影可能属于多种类型，中间用 | 分割
genre_count = movies['Genre'].value_counts()
print(genre_count)
# 根据分隔符 | 解析字符串，然后统计每个子串出现次数
# 填充 Genre 列的空值，填充为 others 类型
movies['Genre'].isnull().sum() / len(movies['Genre'])  # 打印下空值比例
movies['Genre'].fillna('others', inplace=True)
# 根据分割符 | 解析此列，并将此列转换为 NumPy 对象
genres = movies['Genre'].str.split('|').to_numpy()
# 使用 defaultdict 统计出电影种类和对应电影数
counter = defaultdict(int)
for genre in genres:
    for e in genre:
        counter[e] += 1
print(counter)
# 一共有 29 种电影,对上面字典按种类数排序
counter_sorted = sorted(counter.items(), key=lambda x: x[1])
print(counter_sorted)
# 取电影种类数最多的前 10 进行分析
top10 = counter_sorted[-10:]
# 绘制前 10 最多种类数的柱状图，使用 pyecharts 绘制
x = [x for x, y in top10]
y = [y for x, y in top10]
bar = (
    Bar(init_opts=opts.InitOpts(height='1200px'))
    .add_xaxis(x)
    .add_yaxis('电影种类名', y, category_gap='50%')
    .reversal_axis()
    .set_global_opts(title_opts=opts.TitleOpts(title="电影种类及影片数"),
                     toolbox_opts=opts.ToolboxOpts())
)
grid = (
    Grid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(bar, grid_opts=opts.GridOpts(pos_left="30%"))
)
grid.render(path='./res/html/movie1.html')

# 对于上面的top 10 数据使用 pyecharts 绘制饼状图
c = (Pie().add(
    "", [list(z) for z in top10],
    radius=["40%", "55%"],
    label_opts=opts.LabelOpts(
        position="outside",
        formatter="{a|{a}}{adg|}\n{b|{b}: }{c} {per|{d}%}",
        background_color="#eee",
        border_color="#eee",
        border_width=1,
        border_radius=4,
        rich={
            "a": {"color": "#999", "LineHeight": 22, "align": "center"},
            "abg": {
                "backgroundColor": "#e3e3e3",
                "width": "100 %",
                "align": "right",
                "height": 22,
                "borderRedisu": [4, 4, 0, 0]
            },
            "hr": {
                "borderColor": "#aaa",
                "width": "100 %",
                "borderWidth": 0.5,
                "height": 0
            },
            "b": {"fontSize": 16, "lineHeight": 33},
            "per": {"color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2}})

)
)
c.render(path='./res/html/movies.html')
# 可以看到前三类已经4占到50%，最多的Drame占比27%
