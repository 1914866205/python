"""
基础词云
pip3 install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
# 生成本地图片
w.generate('So cute')
w.to_file('./res/img/output1.png')

# 创建词云对象，设置词云图片 宽，高，字体，内聚颜色等参数
# 中文字体需要提前下载
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        font_path='./res/font/SimHei.ttf')
w.generate('我在现实中，自卑懦弱，不敢和任何人发生冲突，也不敢侮辱别人，生怕被人殴打。但是在网络中…本尊！意气风发！睥睨天下！辱骂网友，唯我独尊！天不生我键盘侠，喷道万古长如夜，键来！仙之颠，傲世间！先有键盘后有天！大河之键天上来！一键横天镇世间！破红尘！杀尽仙！一键在手斩九天！倘若世间无真仙？我愿持键化为仙！')
w.to_file('./res/img/output2.png')
