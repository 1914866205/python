# 展示数据并绘制专业图表的库
import matplotlib.pyplot as plt
# 数组操作，用于组织和绘制运算的库
import numpy as np

# 创建一个由x到y，等分成n个元素的数组
x = np.linspace(0, 10, 100)
y = 0
for k in range(1, 10, 1):
    y = y + 4 * np.sin((2 * k - 1) * x) / ((2 * k - 1) * np.pi)
# 根据x，y的数值绘制直、曲线
plt.plot(x, y, 'k', color='r', label="w=1", linewidth=3)
# 获取设置轴属性的快捷方法
# x∈[0,10]  y∈[-1.5,1.5]
plt.axis([0, 10, -1.5, 1.5])
# 在绘图区域中防止绘图标签（图注）
plt.legend()
# 显示创建的绘图对象
plt.show()
