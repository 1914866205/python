"""
多线程
"""
import threading
import time
# 创建一个线程
my_thread = threading.Thread()
# 创建一个名称为my_thread的线程
my_thread = threading.Thread(name='my_thread')


def print_i(i):
    print('打印i:%d' % (i,))


# 通过参数 target 传入，参数类型为callable
my_thread = threading.Thread(target=print_i, args=(1,))
# 启动线程
my_thread.start()


def print_time():
    # 在每个线程中打印5次
    for _ in range(5):
        # 模拟打印前的相关处理逻辑耗时
        time.sleep(0.1)
        print('当前线程%s,打印结束时间为：%s' %
              (threading.current_thread().getName(), time.time()))


# 开辟 3 个线程，装载到threads中
threads = [threading.Thread(name='t%d' % (
    i,), target=print_time)for i in range(3)]
# 启动3个线程
[t.start()for t in threads]
