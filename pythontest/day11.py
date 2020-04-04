"""
requests请求api,用字典和列表保存为json
"""

import json
import requests
resp = requests.get(
    # json地址
    'http://api.tianapi.com/allnews/index?key=28873d5ac82af9c4a6357f0d6b4f59ce&num=10&col=7'
)
newslist = json.loads(resp.text)['newslist']
result = []
data = './res/data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['ctime'] = news['ctime']
    temp_dict['title'] = news['title']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f)
print
