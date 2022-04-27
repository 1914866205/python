fo=open("D:\CompcuteApplication\projectTest\pythonTest\\res\hello.py","r+")
str2=''
for line in fo:
    str=line.split("\"")
    str2 = "\n"+str[0] + "\"" + str[1].upper() + "\"" + str[2]
    print(str2)
    fo.write(str2)
fo.close()