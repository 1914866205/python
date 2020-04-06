# 数据分析
# 原始数据
# 数据清洗：填充或删除缺失数据，删除重复值，数据类型转换，字符串处理，删掉异常数据，数据替换
# 数据分析
# 数据结论
# as  别名
import numpy as np
# 处理csv的文件
import pandas as pd
# 数据分析，画图的库
import matplotlib.pyplot as plt
# 可视化工具
import seaborn as sns

# 解决中文问题  matplotlib.pypolt不支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号显示
plt.rcParams['axes.unicode_minus'] = False
# %matplotlb inline #plt.show   直接显示生产的图表 在这个文档写的代码就不用加了

# 原始数据  UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb3 in position 0: invalid start byte
data = pd.read_csv(
    r'D:\360MoveData\Users\lenovo\Desktop\data.csv', encoding='gb18030')
data
# 数据清洗 删除价格为NaN类型的数据
data.drop([8, 48, 54], inplace=True)  # 参数1  删除的行号   参数2  表示在原始数据上删除
data
data.head(10)  # 默认5行，这里显示10行

# 缺失值  检测当前的数据有没有缺失值
data.isnull()
print('当前缺失值为')
(data.isnull()).sum()

# 删除原价为 NaN 缺失值的数据
data.dropna(subset=['价格'], inplace=True)

# 重复值的检测
data.duplicated()
# 重复值的检测
data.duplicated()
# 删除重复值
data.drop_duplicates(inplace=True)

# 查看剩余所有数据的个数
len(data)
# 查看列名为 价格 的列包含 万 的数据的个数
data.价格.str.contains('万').sum()
# 字符串处理
# 把价格 列 的数据封装到map里一次执行这个替换方法 如16.77万转换成16.77 再通过float转换成浮点数据
data['价格'] = data.价格.map(lambda x: float(x.replace('万', '')))
data.head(10)
# 按价格升序
data.sort_values('价格')
# 按价格降序
data.sort_values('价格', ascending=False)

# 描述性分析
data.describe()
# count 总数
# mean  平均值
# std   方差
# min   最低
# max   最高

# 价格的分析

# 定义分类标准   分析各区间的数据
bins = [0, 30, 60, 90, 120, 150, 180]
pd.cut(data.价格, bins).value_counts()

# 画成直方图
pd.cut(data.价格, bins).value_counts().plot.bar()

# 画成直方图   rot 把x轴的数据进行旋转 ，如旋转水平角度为0度
pd.cut(data.价格, bins).value_counts().plot.bar(rot=0)

# 直方图，x轴水平，并加上标题
pd.cut(data.价格, bins).value_counts().plot.bar(rot=0, title='价格分析')

#    品牌的分析
data['车型'] = data.车型.map(lambda x: x.split(' ')[0])
data
data.车型.value_counts()
# 分组   对所以车辆按地点分组 显示该组的平均价格
data.groupby(['车型'])['价格'].mean()
# 类型转换
#data['列名']=data.列名.map(lambda x:目标数据类型(x))
# 重新排列索引，并删除原索引
data = data.reset_index(drop=True)
data
top10 = ['宝马5系', '奔驰C级', '宝马3系', '奥迪A4L',
         '宝来', '高尔夫', '天籁', '轩逸', '宝马X1', '标致307']
top10
data_top10 = data[data['车型'].isin(top10)]
# 形状
data_top10.shape
print('Top10车型占总车型的比例: %.2f%%' % ((data_top10.shape[0]/data.shape[0])*100))
# 画饼图
plt.axes(aspect='equal')  # 将横轴，纵轴坐标标准化处理，保证饼图是一个正圆，否则为椭圆
plt.pie(data_top10['车型'].value_counts(), explode=[0.2, 0.2, 0.2, 0, 0,
                                                  0, 0, 0, 0, 0], startangle=0, labels=top10, autopct='%.2f%%', radius=2)
# radus半径
