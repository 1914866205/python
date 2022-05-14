import requests
import json
import re
import os
import random

folder_path = 'haha'


def getBaiduImage(url):
    rsp = requests.get(url, timeout=10)
    rsp.raise_for_status()
    print(rsp.text)
    data = json.loads(rsp.text)
    downLoadImage(data)


def tryPic(url):
    form = url[-4:]
    pat = '.*/(.*?)' + form
    pattern = re.compile(pat, re.S)
    filename = re.findall(pattern, url)
    return filename[0], form


def downLoadImage(data):
    global folder_path
    os.mkdir(folder_path)
    imgs = data['data']
    count = 0
    for i in imgs:
        try:
            url = i['download_url']
            img = requests.get(url, timeout=10)
            img = img.content
            image, form = tryPic(url)
            FileName = folder_path + '\\' + image + form
            file = open(FileName, 'bw')
            file.write(img)
            print('No.%d success' % count)
        except KeyError:
            print('No.%d failed' % count)
        count += 1


# 用女明星的图片进行测试
##内地
url = 'http://image.baidu.com/channel/listjson?pn=0&rn=30&tag1=%E6%98%8E%E6%98%9F&tag2=%E5%85%A8%E9%83%A8&ftags=%E5%A5%B3%E6%98%8E%E6%98%9F&ie=utf8'+'1'+'&rn=60&ie=utf8&oe=utf8&'+str(random.random())
getBaiduImage(url)
