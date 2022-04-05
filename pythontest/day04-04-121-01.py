num = int(input("请输入一个0-9数字"))
n = 1
while (num != 7):
    if num > 7:
        print("遗憾，太大了")
    elif num < 7:
        print("遗憾，太小了")
    n = n + 1
    num = int(input("请输入一个0-9数字"))
print("预测了{}次".format(n))
