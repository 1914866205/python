import jieba
import wordcloud
from PIL import Image
import numpy as np
import imageio
import os
import matplotlib.pyplot as plt
import re

f = open("D:\CompcuteApplication\projectTest\pythonTest\\res\\txt\《三国演义》.txt", "r", encoding="gb18030")
t = f.read()
f.close()
mask = imageio.imread("D:\CompcuteApplication\projectTest\pythonTest\\res\img\关羽.png")
excludes = {"将军", "却说", "二人", "不可", "荆州", "不能", "如此"}
words = jieba.lcut(t)

counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孔明" or word == "孔明曰":
        rword = "诸葛亮"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "都督":
        rword = "周瑜"
    elif word == "翼德":
        rword = "张飞"
    elif word == "孟德":
        rword = "曹操"
    elif word == "后主":
        rword = "刘禅"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for w in excludes:
    del counts[w]
items = list(counts.items())
items.sort(key=lambda item: item[1], reverse=True)
# 生成词云函数所需要的文本段
txt = "".join(t)
# 调用wordcloud生成词云
w = wordcloud.WordCloud(
    font_path="D:\CompcuteApplication\projectTest\pythonTest\\res\\font\SimHei.ttf",
    width=500, height=400,
    mask=mask,
    max_words=200,
    max_font_size=100,
    background_color="white",
    font_step=3,
    color_func=wordcloud.ImageColorGenerator(mask),
    prefer_horizontal=0.9)
w = w.generate(t)
plt.imshow(w)  # 显示词云
plt.axis("off")  # 关闭坐标轴
plt.show()  # 显示图像
outputFileFolder = r'D:\\360MoveData\Users\lenovo\Desktop\三国演义.png'
if os.path.exists(outputFileFolder) == False:
    w.to_file(outputFileFolder)
