import re
import requests
import os
num = 0
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Cookie': '',
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
    }
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%A4%B4%E5%83%8F'
html = requests.get(url, headers=header)
html.encoding = 'utf8'
print(html.text)
html = html.text
pachong_picture_path = 'D:\\'
if not os.path.exists(pachong_picture_path):
    os.mkdir(pachong_picture_path)
res = re.findall('"objURL":"(.*?)"', html)
for i in res:
    num = num + 1
    picture = requests.get(i)
    file_name = 'D:\\images' + str(num) + ".jpg"
    f = open(file_name, "wb")
    f.write(picture.content)
    print(i)
f.close()