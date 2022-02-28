money = input("请输入转换金额，美元后加$，人民币后加￥")
if money[-1] == '$':
    ren = eval(money[0:-1]) / 6
    print("%.2f美元转化为%.2f人民币" % (eval(money[0:-1]), ren))
elif money[-1] == '￥':
    mei = eval(money[0: -1]) * 6
    print("%.2f人民币转化为%.2f美元" % (eval(money[0:-1]), mei))
else:
    print("输入格式有误")
# get到python的打印多个变量，需要用%作为占位符，然后用一个大括号包住