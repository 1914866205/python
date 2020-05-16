"""
使用ThreadPoolExecutor向线程池进行任务提交者，更方便的从被调用函数中获取返回值
"""

from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)
# 提交到线程池
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')
# 获得的handle对象会处理所有的阻塞与写作，然后从工作线程中返回数据
x = a.result()
y = b.result()
