"""
多线程售票
"""
import os
import threading

# 声明一个全局变量(全局需要共享数据) 存储一两列出的总票数
tickis = 1000

# 因为数据存在安全性问题，为了保证卖票线程不会抢买同一个票
# 而导致售票系统异常，需要给数据上锁，从而保证在该票卖了之后再卖其他的
# threading 提供了锁工具，类似java的线程同步，同样要声明为全局变量
lock = threading.Lock()
# 定义一个卖票的函数


def sale_tickis(thread_name):
    # 函数里共享全局变量需要用到关键字 global 声明，否则访问不到
    global tickis
    global lock
    # 卖票
    while 1:
        # 操作数据之前需要给数据上锁
        lock.acquire()
        if tickis != 0:
            tickis -= 1
            print(thread_name, "余票为：", tickis)
        else:
            print(thread_name, "票卖完了")
            os.exit(0)
        # 操作完数据后要释放所，这样后面才能继续卖票
        # 否则数据锁定无法卖票
        lock.release()


class my_thread(threading.Thread):
    def __init__(self, name=""):
        # super(threading.Thread,self).__init__()
        threading.Thread.__init__(self)
        self.name = name
        # 重写Thread类的run()方法创建线程

    def run(self):
        # 调用卖票方法
        sale_tickis(self.name)


# 初始化类创建线程
if __name__ == "__main__":
    for i in range(1, 21):
        thread = my_thread("线程"+str(i))
        # 开启线程
        thread.start()
