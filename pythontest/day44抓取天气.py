"""
抓取天气
"""
from lxml import etree
import requests


def request_temperature():
    # 中国天气网
    url = 'http://www.weather.com.cn/weather1d/101190101.shtml#input'
    # request发起请求
    with requests.get(url) as res:
        content = res.content
        # 使用lxml的etree解析页面
        html = etree.HTML(content)
    # 通过 xpath定位周边城市和景区，返回list
    location = html.xpath('//*[@id="around"]//a[@target="_blank"]/span/text()')
    # 温度list
    temerature = html.xpath('//*[@id="around"]/div/ul/li/a/i/text()')
    # 简化上述两个list作为key和value合成字典
    dictionary = dict(zip(location, temerature))
    return dictionary


if __name__ == '__main__':
    print(request_temperature())
