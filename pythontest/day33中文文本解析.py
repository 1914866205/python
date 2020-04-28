"""
中文文本的情歌分析
"""
from snownlp import SnowNLP

# text='来到杨过曾经生活过的地方，小龙女动情的说：我也想过过过儿过过的生活。'
text='人要是行，干一行行一行，一行行行行行; 要是不行,干一行不行一行，一行不行行行不行'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags=[x for x in s.tags]
print(tags)
#断句
print(s.sentences)
# 拼音
print(s.pinyin)

#情绪判断，返回值为证明情绪的概率，越接近1表示证明情绪，越接近0表示负面情绪
text1='呵呵'
text2='呵'
text3='嘿嘿'
s1=SnowNLP(text1)
s2=SnowNLP(text2)
s3=SnowNLP(text3)
print(text1,s1.sentiments)
print(text2,s2.sentiments)
print(text3,s3.sentiments)
# 呵呵 0.6755407653910152
# 呵 0.5262327818078083
# 嘿嘿 0.6440677966101697


#关键字抽取
text4='从别后，忆相逢，几回魂梦与君同'
s4=SnowNLP(text4)
print(s4.keywords(limit=5))
#概况总结文章
print(s4.summary(limit=4))