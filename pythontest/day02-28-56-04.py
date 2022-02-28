# 等边三角形

import turtle  # https://zhuanlan.zhihu.com/p/90712358

# 绘图软件。在python文档中介绍了Turtle本身是一款简单、易上手的绘图软件

turtle.setup(650, 350, 200, 200)
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
turtle.pensize(25)  # 画笔的宽度

# turtle.fd(150)  # 指沿着海龟的前方向运行
# turtle.right(120) # 右边夹角度转向
# turtle.fd(150)  # 指沿着海龟的前方向运行
# turtle.right(120)
# turtle.fd(150)  # 指沿着海龟的前方向运行
turtle.fd(150)  # 指沿着海龟的前方向运行
turtle.seth(120)  # 右边夹角度转向
turtle.fd(150)  # 指沿着海龟的前方向运行
turtle.seth(-120)  # 左边夹角度转向
turtle.fd(150)  # 指沿着海龟的前方向运行

# turtle.penup()  # 提起笔移动，不绘制图形，用于另起一个地方绘制
# turtle.pendown()  # turtle.pendown() 别名turtle.pd() 画笔落下，留下痕迹
# #  turtle.bk(d):指沿着海龟的反方向运行
# turtle.angle
