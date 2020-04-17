import wordcloud
import random

# 读入外部文本文件
f = open('./res/txt/婚誓.txt', encoding='utf-8')
txt = f.read()
# 更换背景颜色和整体风格
# colormap参考 https://matplotlib.org/examples/color/colormaps_reference.html
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        font_path='./res/font/SimHei.ttf')

# 将txt变量传入
w.generate(txt)
w.to_file('./res/img/output5.png')
