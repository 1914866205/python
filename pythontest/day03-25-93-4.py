num=input("请输入一个5位数字")
flag=True
for i in range(2):
    if num[i]==num[4-i]:
        continue
    else:
        flag=False
        print("{}不是回文字符".format(num))
        break
if(flag):
    print("{}是回文字符".format(num))
