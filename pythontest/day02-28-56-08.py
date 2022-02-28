# 正方形螺旋线

import turtle  # https://zhuanlan.zhihu.com/p/90712358

# 绘图软件。在python文档中介绍了Turtle本身是一款简单、易上手的绘图软件

turtle.setup(800, 800)
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
turtle.pensize(1)  # 画笔的宽度
length = 100
turtle.pendown()
for i in range(10):
    turtle.fd(length)
    turtle.seth(90)
    length -= 5
    turtle.fd(length)
    turtle.seth(-180)
    turtle.fd(length)
    length -= 5
    turtle.seth(-90)
    turtle.fd(length)
    turtle.seth(0)
