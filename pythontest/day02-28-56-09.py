# 区别于实例2的python蟒蛇

import turtle

turtle.setup(650, 360, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("yellow")
turtle.seth(-40)
color = ["black", "pink"]
turtle.circle(80, 80)  # 画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆
turtle.circle(80)
for i in range(2):
    turtle.pencolor(color[i])
    turtle.penup()
    turtle.circle(-80, 80)  # 画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆
    turtle.pendown()
    turtle.circle(80)
    turtle.penup()
    turtle.circle(80, 80)  # 画圆，半径为正(负)，表示圆心在画笔的左边(右边)画圆

