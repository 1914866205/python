from  random import randint
num = int(input("请输入一个1-99数字"))
n = 1
guess=randint(1,99)
print(guess)
while (num != guess):
    if num > guess:
        print("遗憾，太大了")
    elif num < guess:
        print("遗憾，太小了")
    n = n + 1
    num = int(input("请输入一个0-99数字"))
print("预测了{}次".format(n))
