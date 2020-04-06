# 爬取二手车网站的数据
from bs4 import BeautifulSoup
# 用于网络请求的库
import urllib.request
import csv
# 指定编码
import codecs

# 目标网址
url = 'http://www.che168.com/china/a0_0msdgscncgpi1lto8cspexx0/#pvareaid=106289'
# 发送请求
f = urllib.request.urlopen(url)
resp = f.read()
# print(resp)  # 203
# 网页源代码 (文本显示)
# print(resp.text)
# 用BeautifulSoup解析数据  python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
html = BeautifulSoup(resp, 'html.parser')

# 解析返回的数据
csvfile = open(r'D:\360MoveData\Users\lenovo\Desktop\data.csv',
               'w', newline='')
writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
keys = ['车型', '信息', '价格']
writer.writerow(keys)

i = 1
lis = html.findAll(class_='cards-li list-photo-li')
for li in lis:
    carType = li.h4.text
    carInfo = li.p.text
    carPrice = li.s.text
    print(carType)
    print(carInfo)
    print(carPrice)
    oneCar = [carType, carInfo, carPrice]
    writer.writerow(oneCar)
    i += 1
csvfile.close()
