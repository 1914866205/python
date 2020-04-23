from time import time
from threading import Thread

import requests

# 继承Thread类创建自定义的线程类


class DownLoadHanlder(Thread):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def run(self):
        # filename = self.url[self.url.rfind('/')+1:]
        # resp = requests.get(self.url)
        with open('./res/元曲.txt', 'wb') as f:
            # f.write(resp.content)
            f.write(bytes(self.content, 'utf-8'))


def main():
    # 使用了天行数据接口提供的网络API，用自己的Key替换掉下面代码中心的APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/txapi/yuanqu/index?key=cd3ffda4506c231ff8c9bde908dc7d81&word=折桂令')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        # url = mm_dict['picUrl']
        content = mm_dict['content']
        # 通过多线程的方式实现下载
        DownLoadHanlder(content).start()


if __name__ == '__main__':
    main()
