# 展示数据并绘制专业图表的库
import matplotlib.pyplot as plt
# 数组操作，用于组织和绘制运算的库
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 定义参数方程
def X(a, t):
    return a * (2 * np.sin(t) - np.sin(2 * t))
def Y(a, t):
    return a * (2 * np.cos(t) - np.cos(2 * t))
# 绘制左半边
t1 = [i for i in np.arange(-np.pi, 0, 0.01)]
x1 = [X(80, i) for i in t1]
y1 = [Y(80, i) for i in t1]
plt.title("爬山吗？")
plt.plot(x1, y1, color='r')
plt.text(-150, -50, '涛涛', color='r')
# 绘制右半边
t2 = [i for i in np.arange(0, np.pi,0.01)]
x2 = [X(80, i) for i in t2]
y2 = [Y(80, i) for i in t2]
plt.plot(x2, y2, color='b')
plt.text(150, -50, '瓶子', color='b')
# 显示创建的绘图对象
plt.show()
