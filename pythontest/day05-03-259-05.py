import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# 创建一个坐标系风格子绘图区域
ax = plt.axes(polar=True)
## 创建一个由x到y，等分成n个元素的数组
theta = np.linspace(0, 2 * np.pi, 4, endpoint=False)
radius = 0.25 + 0.75 * np.random.random(size=len(theta))
points = np.vstack((theta, radius)).transpose()
plt.gca().add_patch(patches.Polygon(points, color='c'))
angles = [a if a <= 360. else a - 360. for a in np.arange(90, 90 + 360, 360.0 / 4)]
titles = ['敏捷', '速度', '耐性', '智力']
ax.set_thetagrids(angles, labels=titles, weight="bold", color="black")
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.show()
