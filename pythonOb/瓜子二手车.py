# 爬取瓜子二手车网站的数据

# 用于网络请求的库
import requests

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
# print(resp.text)

# 网页源代码 (二进制显示)
print(resp.text)
