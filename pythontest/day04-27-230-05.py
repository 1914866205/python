import json

file = open("D:\CompcuteApplication\projectTest\pythonTest\\res\\txt\English.txt", "r+")
dic=json.loads(file.read())
while True:
    choice = int(input("请输入操作： 0 添加    1 查询    2 退出"))
    if choice == 0:
        eng = input("请输入英文单词：")
        for key, value in dic.items():
            if eng == key:
                print("该单词已添加到字典库")
                file.close()
                exit(1)
        chi = input("请输入中文单词：")
        dic[eng] = chi
        file.write(str(dic))
        print("添加成功")
    elif choice == 1:
        eng = input("请输入要查询的英文单词：")
        try:
            print(dic.get(eng))
        except:
            print("字典库中未找到这个单词")
    elif choice == 2:
        file.close()
        exit(1)
    else:
        print("输入有误")
