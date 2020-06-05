"""
Matplotlib绘图
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
midwest = pd.read_csv('res/csv/midwest_filter.csv')
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1))
          for i in range(len(categories))]
plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal',
                data=midwest.loc[midwest.category == category, :], s=20, c=colors[i], label=str(category))
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000), xlabel='Area', ylabel='Population')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("测试", fontsize=22)
plt.legend(fontsize=12)
plt.show()
plt.savefig('./res/img/散点图.png')
