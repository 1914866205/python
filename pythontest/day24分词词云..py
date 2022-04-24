# 导入词云制作库wordcloud这中文分词库jieba
import jieba
import wordcloud
# 构建并配置词云对象w
w = wordcloud.WordCloud(
    width=1000,
    height=400,
    background_color='#6c909e',
    colormap='GnBu',
    font_path='D:\CompcuteApplication\projectTest\pythonTest\\res\\font\SimHei.ttf'
)

# 调用jieba的Lcut()方法对原始文本进行中文分词，得到string
txt = '''
从此天涯奔走 穷尽一生探寻挚友 
从此放下离愁 生生世世酒敬自由
从此泼墨煮茶 闭口不谈世间繁华
从此安分守己 也在不说浪迹天涯
从此闭心锁魂 闭口不谈一往情深
从此一人流浪 再也没有我的码头
从此青灯常守 闭口不谈往事情愁
从此江水东流 再也不说玉簪红袖
从此人海逐流 闭口不谈相依为命
从此孑然一身 再也没有十里春风
从此养花遛狗 闭口不说天长地久 
从此白日寻酒 再也不说爱恨情仇
从此莫念莫愁 闭口不言长相厮守
从此清风配酒 路长水远我一人走
从此心随风动 闭口不谈你情我浓
从此宰鸡杀狗 再也不想为你停留
从此花天酒地 闭口不说真心真意
从此洒脱不羁 再也不想这世唯一
从此只为父母 闭口不谈为谁付出
从此负山而走 只为遇见那片海阔天空
'''
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file('D:\CompcuteApplication\projectTest\pythonTest\\res\\img\\output4.png')
