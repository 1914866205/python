# 爬取二手车网站的数据
from bs4 import BeautifulSoup
# 用于网络请求的库
import urllib.request
# 目标网址
url = 'http://www.che168.com/china/a0_0msdgscncgpi1lto8cspexx0/#pvareaid=106289'
# 发送请求
f = urllib.request.urlopen(url)
resp = f.read()
print(resp)  # 203
# 网页源代码 (文本显示)
# print(resp.text)
# 用BeautifulSoup解析数据  python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
html = BeautifulSoup(resp, 'html.parser')
# 读取title内容
print(html.title)
