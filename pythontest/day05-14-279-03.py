# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

print(['排行', '影片', '篇集', '播放量', '点赞量', '视频链接'])
# 要爬取的网站链接
r = requests.get('https://www.bilibili.com/v/popular/rank/guochan')
html = r.content
# html.parser是解析器
soup = BeautifulSoup(html, 'html.parser')
div_people_list = soup.find('div', attrs={'class': 'rank-list-wrap'})
div_people_list_list = div_people_list.find('ul', attrs={'class': 'rank-list pgc-list'})
a_s = div_people_list.find_all('li', attrs={'class': 'rank-item'})
# a_s_2 = a_s.find_all('div', attrs={'class': 'info'})
# 排名
for a in a_s:
    for b in a.find_all('div', attrs={'class': 'info'}):
        # 名称及链接
        for c in b.find_all('a', attrs={'target': '_blank'}):
            for d in b.find('span', attrs={'class': 'data-box'}):  # 获取视频集
                for e in b.find_all('span', attrs={'class': 'data-box'})[1:][:1]:
                    # 循环播放数
                    for f in b.find_all('span', attrs={'class': 'data-box'})[2:][:2]:
                        # 循环点赞量
                        web = a['data-rank']  # 排名
                        name = c.string  # 名称
                        name_2 = d.string  # 全集
                        name_2_1 = name_2.replace(" ", "").replace("\t", "").strip()  # 去除多余空格
                        name_3 = e.get_text()  # 播放量
                        data_1 = name_3.replace(" ", "").replace("\n", "").replace("\t", "")
                        name_4 = f.get_text()  # 点赞量
                        data_2 = name_4.replace(" ", "").replace("\n", "").replace("\t", "")
                        url = c['href']  # 链接
                        n = name_2.replace(" ", "").replace("\t", "").strip()  # 去除多余空格
                        d = name_3.replace(" ", "").replace("\t", "")
                        g = name_4.replace(" ", "").replace("\t", "")
                        print(web, end=' ')
                        print(name, end=' ')
                        print(n, end=' ')
                        print(url)
