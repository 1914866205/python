import turtle, datetime,random


def drawGap():
    # 绘制数码管间隔,为5像素
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):
    # 绘制单段数码管,移动40像素
    # colors=["#FF5252","#FF5252","#B2EBF2","#9E9E9E","#689F38","#536DFE"]
    # i=random.randint(0,5)
    # turtle.pencolor(colors[i])
    turtle.pencolor("red")
    drawGap()
    # turtle.pendown() if draw else turtle.penup()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
        turtle.pencolor("#CFD8DC")
        turtle.pendown()
    turtle.fd(40)
    drawGap()
    # 向右旋转90度
    turtle.right(90)


def drawDigit(d):
    # 根据数字绘制七段数码管
    #
    #               **6**
    #             *       *
    #             5       7
    #             *       *
    #               **1**
    #             *       *
    #             4       2
    #             *       *
    #               **3**

    #   1
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    #   2
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    #   3
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    #   4
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    # 此处需要重新调整角度，因为上个函数已经把角度右转90度了
    turtle.left(90)
    #   5
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    #   6
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    #   7
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)

    # 此时角度指向正左方，但一个数字已刻画完，需要向右移动到一个新位置，重新刻画
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年', font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))

main()

