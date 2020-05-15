"""
多线程2
"""
import threading
from time import ctime, sleep
# 创建player()函数，用于接收name和time，用于确定要播放的文件及时长


def player(name, sleepTime):
    for i in range(2):
        print('正在播放：', (name, ctime()))
        sleep(sleepTime)


# 字典：播放的文件和播放时长
lists = {"开到土匪.mp3": 1, "好像有人来.mp3": 2, "天呀.mp3": 3}
threads = []
lens = len(lists)
# 遍历歌单，通过字典的items()方法来循环的取name和item，取到的这两个值用于创建线程
for n, t in lists.items():
    t = threading.Thread(target=player, args=(n, t))
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('结束播放', ctime())
