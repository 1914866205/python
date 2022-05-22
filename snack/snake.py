import sys
import time
import pygame
from random import *


# Position类，通过其构造函数，设置x和y
class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 生成随机的食物
#食物对象初始化函数，传入形参为贪吃蛇蛇头坐标。
# 当贪吃蛇吃掉食物后，通过该函数生成新的食物。
# 通过传入形参判断新生成的食物坐标是否与蛇头坐标相同，若相同则重新生成新的坐标。
def new_food(head):
    while True:
        new_food = Position(randint(0, 48) * 20, randint(0, 29) * 20)
        # 判断新生成的事物是否和贪吃蛇蛇头重合，重合则不创键
        if new_food.x != head.x and new_food.y != head.y:
            break
        else:
            continue
    return new_food


# 绘制，在窗体中绘制贪吃蛇、食物
# color:颜色，position: 坐标
def rect(color, position):
    pygame.draw.circle(window, color, (position.x, position.y), 10)


# 初始界面和游戏中点退出游戏时
def exit_end():
    pygame.quit()
    quit()


# 游戏结束时，显示得分的窗体的设置
# 游戏结束时，结束界面设置函数。
# 在该函数中进行结束界面窗体的初始化，在窗体中显示玩家的最终得分，
# 并在改函数中调用pygame库quit方法，使该库停止工作。
def show_end():
    # 设计窗口
    # 定义窗口大小
    small_window = pygame.display.set_mode((960, 600))
    init_background = pygame.image.load("D:\\CompcuteApplication\\projectTest\\pythonTest\\snack\\init_bgimg.jpg")
    small_window.blit(init_background, (0, 0))
    # 定义标题
    pygame.display.set_caption("贪吃蛇大冒险")
    # 定义背景图片
    font = pygame.font.SysFont("simHei", 40)
    fontsurf = font.render('游戏结束! 你的得分为: %s' % score, False, black)
    small_window.blit(fontsurf, (250, 200))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()


# 正常模式死亡设置
# 蛇头和蛇身位置重合或者和墙体重合，即死亡

# head: 蛇头， snake_body:蛇身
#正常模式下贪吃蛇死亡判断函数，传入形参为贪吃蛇蛇头和蛇身坐标数据。
# 在该函数中设置布尔型变量die_flag，若死亡设置为Ture并返回，没有死亡为False。
# 通过遍历蛇身存储列表，判断蛇身坐标是否与蛇头坐标相同，若相同则判定贪吃蛇咬到自身，死亡。同时，判断贪吃蛇是否撞墙，及判断蛇头的x和y坐标是否窗体的宽高，若超过则死亡。
def die_snake(head, snake_body):
    # 定义标志物，默认为false，true时判定贪吃蛇碰到自己，死亡
    die_flag = False
    # 遍历存放贪吃蛇位姿的列表，从第1个开始，(第0个位蛇头)
    for body in snake_body[1:]:
        # 如果蛇头的xy和蛇身xy相等，则判定相撞，设置flag为ture
        if head.x == body.x and head.y == body.y:
            die_flag = True
    # 若蛇头的xy在显示窗体外，或flag为true，则显示结束界面，并退出游戏
    if head.x < 0 or head.x > 960 or head.y < 0 or head.y > 600 or die_flag:
        show_end()


# 正常模式主体设置
#正常模式的主循环函数，通过该函数进行正常模式下贪吃蛇和食物的初始化、
# 玩家控制贪吃蛇运动、蛇头和蛇身的判断更新和得分统计实现。
def start_game():
    # 定义存分数的全局变量
    # 分数
    global score
    # 随机颜色
    global color
    color = (randint(10, 255), randint(10, 255), randint(10, 255))
    # 定义存放玩家键盘输入运动方向的变量，初始为向右
    run_direction = "right"
    # 定义贪吃蛇运动方向的变量，初始为玩家键入方向
    run = run_direction
    # 实例化蛇头、蛇身、食物对象
    head = Position(160, 160)
    # 初始化蛇身长度为3个单位  动态数组 蛇身对象
    snake_body = [Position(head.x, head.y + 20), Position(head.x, head.y + 40), Position(head.x, head.y + 60)]
    # 初始化食物位置
    food = Position(300, 300)
    # 死循环
    while True:
        # 获取此表面(背景)并将其绘制到窗口上.为此,我们将调用screen.blit(background,(x,y)),
        # 其中(x,y)是我们希望表面左上角在窗口内的位置.该函数表示将背景表面拖到屏幕上并将其放置在(x,y)处.
        window.blit(background, (0,0))
        # 监听玩家键盘输入的运动方向值，并根据输入转为up、down、right或left，方便程序中调用
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_end()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    run_direction = "up"
                elif event.key == pygame.K_RIGHT:
                    run_direction = "right"
                elif event.key == pygame.K_LEFT:
                    run_direction = "left"
                elif event.key == pygame.K_DOWN:
                    run_direction = "down"
        # 绘制食物
        rect(color, food)
        # 绘制蛇头
        rect(black, head)
        # 绘制蛇身，因为蛇身是动态的
        for pos in snake_body:
            rect(white, pos)
        # 判断贪吃蛇原运动方向与玩家键盘输入的运动方向是否违反正常运动情况
        if run == "up" and not run_direction == "down":
            run = run_direction
        elif run == "down" and not run_direction == "up":
            run = run_direction
        elif run == "left" and not run_direction == "right":
            run = run_direction
        elif run == "right" and not run_direction == "left":
            run = run_direction

        # 插入蛇头位置到蛇身列表中
        snake_body.insert(0, Position(head.x, head.y))
        #下面再删除蛇尾

        # 根据玩家键入方向进行蛇头xy的更新
        if run == "up":
            head.y -= 20
        elif run == "down":
            head.y += 20
        elif run == "left":
            head.x -= 20
        elif run == "right":
            head.x += 20
        # 正常模式下死亡判定。头的位置和身体重合、或者超出边界、则死亡
        die_snake(head, snake_body)
        # 判断蛇头和食物坐标，若相等，则加分，并生成新的食物
        if head.x == food.x and head.y == food.y:
            score += 1
            food = new_food(head)
            color = (randint(10, 255), randint(10, 255), randint(10, 255))
        else:
            #pop()
            #函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
            snake_body.pop()
        font = pygame.font.SysFont("simHei", 25)
        mode_title = font.render('正常模式', False, grey)
        socre_title = font.render('得分: %s' % score, False, grey)
        window.blit(mode_title, (50, 30))
        window.blit(socre_title, (50, 65))
        # 绘制更新
        pygame.display.update()
        # 通过帧率设置贪吃蛇速度
        clock.tick(8)


# 可穿墙模式死亡设置
# head:蛇头，snake_body:蛇身
# 可穿墙模式下贪吃蛇死亡判断函数，传入形参为贪吃蛇蛇头和蛇身坐标数据。
# 在该函数中设置布尔型变量die_flag，若死亡设置为Ture并返回，没有死亡为False。
# 通过遍历蛇身存储列表，判断蛇身坐标是否与蛇头坐标相同，若相同则判定贪吃蛇咬到自身，死亡。
def through_snake(head, snake_body):
    # 定义标志位
    die_flag = False
    # 遍历，蛇头碰到蛇身时，flag为true退出游戏
    for body in snake_body[1:]:
        if head.x == body.x and head.y == body.y:
            die_flag = True
    if die_flag:
        show_end()
    else:  # 当蛇头的xy出窗体时
        # 四种穿墙情况，分别设置
        # 就是 相当于循环队列的位置，重置位置
        if head.x < 0:
            head.x = 960
        if head.x > 960:
            head.x = 0
        if head.y < 0:
            head.y = 600
        if head.y > 600:
            head.y = 0


# 穿墙模式主体设置
#可穿墙模式的主循环函数，通过该函数进行可穿墙模式下贪吃蛇和食物的初始化、
# 玩家控制贪吃蛇运动、蛇头和蛇身的判断更新和得分统计实现。
def start_kgame():
    global score
    global color
    color = (randint(10, 255), randint(10, 255), randint(10, 255))
    # 定义蛇初始方向
    run_direction = "up"
    run = run_direction
    # 实例化蛇头、蛇身、食物对象
    head = Position(160, 160)
    # 三格
    snake_body = [Position(head.x, head.y + 20), Position(head.x, head.y + 40), Position(head.x, head.y + 60)]
    # 初始化食物位置
    food = Position(300, 300)
    # 死循环，监听键盘键值
    while True:
        window.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_end()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    run_direction = "up"
                elif event.key == pygame.K_RIGHT:
                    run_direction = "right"
                elif event.key == pygame.K_LEFT:
                    run_direction = "left"
                elif event.key == pygame.K_DOWN:
                    run_direction = "down"
        # 食物
        rect(color, food)
        # 蛇头
        rect(black, head)
        # 蛇身
        for pos in snake_body:
            rect(white, pos)
        # 判断贪吃蛇原运动方向与玩家键盘输入的运动方向是否违反正常运动情况
        if run == "up" and not run_direction == "down":  # 若运动方向为向上，玩家输入运动方向向下，则违背贪吃蛇正常运动情况
            run = run_direction
        elif run == "down" and not run_direction == "up":
            run = run_direction
        elif run == "left" and not run_direction == "right":
            run = run_direction
        elif run == "right" and not run_direction == "left":
            run = run_direction
        # 插入蛇头位置到蛇身列表中
        snake_body.insert(0, Position(head.x, head.y))
        # 根据玩家键入方向进行蛇头xy的更新
        if run == "up":
            head.y -= 20
        elif run == "down":
            head.y += 20
        elif run == "left":
            head.x -= 20
        elif run == "right":
            head.x += 20
        # 穿墙实现
        # 穿墙模式下的死亡判定  头位置和身体位置重合
        through_snake(head, snake_body)
        # 判断是否加分和随机生成新的食物
        if head.x == food.x and head.y == food.y:
            score += 1
            food = new_food(head)
            color = (randint(10, 255), randint(10, 255), randint(10, 255))
        else:
            snake_body.pop()
        font = pygame.font.SysFont("simHei", 25)
        mode_title = font.render('穿墙模式', False, grey)
        socre_title = font.render('得分: %s' % score, False, grey)

        #绘制文本
        window.blit(mode_title, (50, 30))
        window.blit(socre_title, (50, 65))
        # 绘制更新
        pygame.display.update()
        # 通过帧率设置贪吃蛇速度
        clock.tick(8)


# 监听函数，监听键盘输入
# msg: 按钮信息，x: 按钮的x轴，y: 按钮的y轴，w: 按钮的宽，h: 按钮的高，ic: 按钮初始颜色，ac: 按钮按下颜色，action: 按钮按下的动作
# 游戏初始界面按钮监听函数，在该函数中实现对玩家鼠标点击事件和键盘输入事件的监听。
# 并根据玩家选择，运行按钮对应的触发函数。即点击“正常模式”按钮，运行正常模式的主循环函数，以此类推。
def button(msg, x, y, w, h, ic, ac, action=None):
    # 获取鼠标位置
    mouse = pygame.mouse.get_pos()
    # 获取键盘输入
    click = pygame.mouse.get_pressed()
    # 点击鼠标位置的按钮
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # 绘制一个方块
        pygame.draw.rect(window, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))
    # 设置按钮中的文字样式和居中对齐
    font = pygame.font.SysFont('simHei', 20)
    smallfont = font.render(msg, True, white)
    smallrect = smallfont.get_rect()
    # 计算中心位置
    smallrect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(smallfont, smallrect)


# 游戏初始界面，选择模式
# 游戏初始界面实现函数，在该函数中进行游戏初始界面窗体的初始化。
# 在该界面窗体中设置文本为“正常模式”、“可穿墙模式”和“退出”的三个点击按钮，
# 通过设置循环，调用button函数监听玩家的点击。
def into_game():
    into = True
    while into:
        window.blit(init_background, (0, 0))
        #监听用户事件，如果退出，则游戏结束
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_end()
        # 设置字体
        font = pygame.font.SysFont("simHei", 50)
        # 初始界面显示文字
        fontsurf = font.render('欢迎来到贪吃蛇大冒险!', True, black)  # 文字
        fontrect = fontsurf.get_rect()
        fontrect.center = ((width / 2), 200)
        window.blit(fontsurf, fontrect)
        #三个按钮对象
        # 触发方法 start_game
        button("正常模式", 370, 370, 200, 40, blue, brightred, start_game)
        # 触发方法 start_kgame
        button("可穿墙模式", 370, 420, 200, 40, violte, brightred, start_kgame)
        # 触发方法 exit_end
        button("退出", 370, 470, 200, 40, red,brightred, exit_end)
        pygame.display.update()
        # 每秒调用n次tick函数，一般设置在循环中，限制循环每秒的循环次数。从而达到设置页面刷新率的效果。
        clock.tick(15)

# 在运行模块，进行pygame库的初始化、设置游戏背景音乐、
# 显示窗口各个参数的设置以及游戏初始界面的显示设置
if __name__ == '__main__':
    # 定义画布颜色
    white = (255, 255, 255)
    red = (200, 0, 0)
    green = (0, 128, 0)
    blue = (0, 202, 254)
    violte = (194, 8, 234)
    brightred = (255, 0, 0)
    brightgreen = (0, 255, 0)
    black = (0, 0, 0)
    grey = (129, 131, 129)
    score = 0
    # 设计窗口
    # 定义窗口大小
    width = 960
    height = 600
    #初始化一个窗口
    window = pygame.display.set_mode((width, height))
    #设置当前窗口标题
    pygame.display.set_caption("贪吃蛇大冒险")
    # 定义背景图片
    init_background = pygame.image.load("D:\\CompcuteApplication\\projectTest\\pythonTest\\snack\\init_bgimg.jpg")
    background = pygame.image.load("D:\\CompcuteApplication\\projectTest\\pythonTest\\snack\\bgimg.jpg")
    # 创建时钟对象 (可以控制游戏循环频率)
    clock = pygame.time.Clock()
    # 初始化 其实就是检查，电脑上一些需要的硬件调用接口、基础功能是否有问题。如果有，他会在程序运行之前就反馈给你，方便你进行排查和规避。
    pygame.init()
    # 初始界面
    into_game()


