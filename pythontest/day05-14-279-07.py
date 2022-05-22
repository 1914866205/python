import requests
import time


def showBaidu():
    url = 'https://www.baidu.com/'
    count = 0
    fail = 0
    start = time.time()
    while True:
        if int(time.time() - start) == 30:
            break
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            count += 1
        except:
            fail += 1
            continue
    print('30 秒内，访问百度{}次成功 {}次失败'.format(count, fail))


showBaidu()
