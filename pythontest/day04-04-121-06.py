import random as random
total=1000000
win1=0 #换
win2=0 #不换
for i in range(total):
    #模拟选择过程
    man=random.randint(1,3)
    car=random.randint(1,3)
    #结果： 一开门为车门，不换+1
    #       一开始为羊门，换+1
    if man==car:
        win1+=1
    else:
        win2+=1
print("在{}次实验中：".format(total))
print("若不更改门，获胜的概率为{:.3}%.".format(win1/total*100))
print("若更改门，获胜的概率为{:.3}%.".format(win2/total*100))

