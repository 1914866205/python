start_11 = 1 #初始能力
able = 1  # 增长系数
i = 0
while (i <= 365):
    i = i + 1
    # 整体周期为11天    3天无增长   4天增长1%  3天无增长  1天休息
    if (i % 11) == 0:
        # 1天休息
        able = 1
    elif (i % 11) >= 8:
        # 周期刚开始前三天无增长
        continue
    elif (i % 11) >= 4:
        able = (1 + 0.01)
        start_11 = start_11 * able
    else:
        # 周期刚开始前三天无增长
        continue
print("11天为一个周期，365天后能力值为：{}".format(start_11))

able = 1  # 增长系数
start_15 = 1
i = 0
while (i <= 365):
    i = i + 1
    # 整体周期为15天    3天无增长   4天增长1%  3天无增长  4天增长1% 1天休息
    if (i % 15) == 0:
        # 1天休息
        able = 1
    elif (i % 15) >= 11:
        able = (1 + 0.01)
        start_15 = start_15 * able
    elif (i % 15) >= 8:
        # 周期刚开始前三天无增长
        continue
    elif (i % 15) >= 4:
        able =(1 + 0.01)
        start_15 = start_15 * able
    else:
        # 周期刚开始前三天无增长
        continue
print("15天为一个周期，365天后能力值为：{}".format(start_15))
