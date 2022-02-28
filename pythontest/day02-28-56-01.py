
def tempCovert():
    val = input("请输入带温度表示符号的温度值（例如：32C）：")  # python默认输入是字符串
    while val[-1] not in ['N', 'n']:  # 如果不是N或n
        if val[-1] in ['C', 'c']:  # -1是倒数第一位
            f = 1.8 * eval(val[0:-1]) + 32  # 左闭右开
            print("转换后的温度为： %.2fF" % f)
        elif val[-1] in ['F', 'f']:
            c = (eval(val[0:-1]) - 32) / 1.8
            print("转换后的温度为: %.2fC" % c)
        else:
            print("输入有误")
        val = input("再玩一次？（输入N或n结束）")

tempCovert()
