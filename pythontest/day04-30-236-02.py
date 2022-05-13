from math import fabs
from random import random


# 赛事规则：
# 1.1 篮球比赛
# 篮球比赛由两个队参加，每队出场5名队员。每队目标是在对方球篮得分，并阻止对方队在本方球篮得分。
# 篮球比赛由裁判员、记录台人员和技术代表(如到场)管理。
# 1.2 球篮:本方/对方
# 被某队进攻的球篮是对方的球篮，由某队防守的球篮是本方的球篮。
# 1.3 比赛的胜者
# 在比赛时间结束时得分较多的队，将是比赛的胜者。

def printIntro():
    print("模拟篮球比赛的代码分析")
    print("这个程序模拟两支球队A和B的篮球比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
    a = eval(input("请输入A队的能力值（0-1）："))
    b = eval(input("请输入B队的能力值（0-1）："))
    n = eval(input("模拟比赛的场次："))
    return a, b, n


def simNGames(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def simOneGame(probA, proB):
    scoreA = 0
    scoreB = 0
    # 当前发球方
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            # A胜了
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < proB:
                scoreB += 1
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    return a > b or b > a


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("篮球比赛分析开始，共模拟{}场比赛".format(n))
    print("A队获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("B队获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, )


main()
