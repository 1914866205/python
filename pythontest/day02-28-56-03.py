# 彩色蟒蛇

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
turtle.penup()  # 提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.fd(-250)  # 指沿着海龟的前方向运行
#  turtle.bk(d):指沿着海龟的反方向运行
turtle.pendown()  # turtle.pendown() 别名turtle.pd() 画笔落下，留下痕迹
turtle.pensize(25)  # 画笔的宽度
turtle.pencolor("purple")  # 设置颜色
color = ["black", "pink", "brown"]
turtle.seth(-40) # turtle.setheading(angle) 别名turtle.seth(angle) 改变行进方向
for i in range(3):
    turtle.circle(80, 80)  # 画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆
    turtle.circle(-40, 80)
    turtle.pencolor(color[i])
turtle.circle(40, 80 / 2)
##
# 根据半径r，绘制一个extent角度的弧度
# 　　　　　　r：默认圆心在海龟左侧r距离的位置#
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
