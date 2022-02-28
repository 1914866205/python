# 等边三角形进阶

import turtle  # https://zhuanlan.zhihu.com/p/90712358

# 绘图软件。在python文档中介绍了Turtle本身是一款简单、易上手的绘图软件

turtle.setup(800, 800, 400, 400)
##
#  turtle.setup(width=0.5, height=0.75, startx=None, starty=None)，
#  参数：width, height: 输入宽和高为整数时, 表示像素;
#  为小数时, 表示占据电脑屏幕的比例，
#  (startx, starty): 这一坐标表示矩形窗口左上角顶点的位置,
#  如果为空,则窗口位于屏幕中心。
# #
# https://blog.csdn.net/zengxiantao1994/article/details/76588580
# 画笔的状态
turtle.pencolor("black")  # 设置颜色
turtle.pensize(10)  # 画笔的宽度

turtle.fd(150)  # 指沿着海龟的前方向运行
turtle.seth(-120)  # 右边夹角度转向
turtle.fd(150)  # 指沿着海龟的前方向运行
turtle.seth(120)  # 左边夹角度转向
turtle.fd(150)
# 指沿着海龟的前方向运行
turtle.seth(60)
turtle.fd(150)
turtle.seth(-60)
turtle.fd(300)
turtle.seth(-180)
turtle.fd(300)
turtle.seth(60)
turtle.fd(150)

