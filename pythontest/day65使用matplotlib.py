"""
使用matploamlib进行数据绘图
"""
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# matplotlib命令与格式包括：画布和图像  Figure and Axis
# 创建自定义图像
# figure(num=None,figsize=None,dpi=None,facecolor=None,edgecolor=None,edgecolor=None,frameON=tRUE)
# NUM:图像编号或名称，数字为编号，字符串为名称
# figsize:指定figure的宽和高，单位为英寸
# dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
# facecolor 背景颜色
# edgecolor 边框颜色
# frameon 是否显示边框
fig = Figure()
# 获得绘图对象
canvas = FigureCanvas(fig)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
line, = ax.plot([0, 2], [0, 2])
# 图表标题
ax.set_title("a straight line ")
# x和 y 轴的标签
ax.set_xlabel("x label")
ax.set_ylabel("y label")
# 指定位置绘制图片
canvas.print_figure('./res/img/chatpic1.jpg')
