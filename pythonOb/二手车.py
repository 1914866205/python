# 爬取二手车网站的数据

# 用于网络请求的库
import requests
# 用于xpath的包 pip install lxml
# from lxml import html
# 目标网址
url = 'http://www.che168.com/china/a0_0msdgscncgpi1lto8cspexx0/#pvareaid=106289'
# 添加请求头  伪装
header = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
# 发送请求
resp = requests.get(url)
print(resp)  # 203
# 网页源代码 (文本显示)
print(resp.text)

# 网页源代码 (二进制显示)
# print(resp.text)
# text = resp.text  # 网页内容
# 提取数据      re 正则    bs Jsoup语法      xpath
# 解析
# text = etree.HTML(text)
# xpath语法
#   //不是转义字符 在xpath语法中，一个/表示下一级  类似子选择器
#   //表示不管任何位置，所有的ul  类似后代选择器
# ul = html.xpath('//ul[@class="viewlist_ul"]')[0]
# print(ul)
# 获取当前结点下所有的li标签.
# lis=ul.xpath('./li')
# print(lis)
# for li in lis:
