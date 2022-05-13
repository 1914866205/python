import os

file = input("请输入一个保存路径:")
url = input("请输入一个视频链接:")
os.system("you-get " + '-o ' + file + " " + url)
