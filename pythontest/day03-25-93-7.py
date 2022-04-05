## 有end会只显示在一个位置变化
while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i, end=' ')
## 没有end会全部显示变化
while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i)