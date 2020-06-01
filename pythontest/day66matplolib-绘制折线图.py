"""
matplolib 2 绘制折线图
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.linspace(0, 5, 10)
y = x**2
# 绘制折线图
plt.plot(x, y)
plt.show()
# 调整线条颜色
plt.plot(x, y, 'r')
plt.show()
# 修改线型
plt.plot(x, y, 'r--')
plt.show()
plt.plot(x, y, 'g-*')
plt.show()
plt.plot(x, y, 'r-*')
plt.title('title')
plt.show()
# 添加 x,y轴label和title
plt.plot(x, y, 'r-*')
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# 添加 text文本
plt.plot(x, y, 'r--')
plt.text(1.5, 10, 'y=x*x')
