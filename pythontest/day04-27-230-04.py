import json

fr = open("D:\CompcuteApplication\projectTest\pythonTest\\res\csv\data.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
    print(ls)

fr.close()
fw = open("D:\CompcuteApplication\projectTest\pythonTest\\res\csv\CSV使用中文字符解析data.csv", "w")
for i in range(1, len(ls)):
    # zip()是内置函数，可以将两个长度相同的列表组合成一个关系对，在此生成键值对
    ls[i] = dict(zip(ls[0], ls[i]))
# dump 将python的数据类型转换为JSON  编码 本行代码生成的文件是unicode解码
# json.dump(ls[1:], fw, sort_keys=True, indent=4)
json.dump(ls[1:], fw, sort_keys=True, indent=4,ensure_ascii=False)
fw.close()
