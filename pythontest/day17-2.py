""""
几种方式读文本文件

"""
import time


def main():
    try:
        # 一次性读取整个文件内容
        with open('./res/学习心得.txt', 'r', encoding='gbk') as f:
            print(f.read())
        # 读取文件按行读取到列表中
        with open("./res/学习心得.txt", 'r', encoding='gbk') as f:
            lines = f.readline()
        print(lines)

        # 通过for-in循环逐行读取，加上延时
        with open('./res/学习心得.txt', mode='r', encoding='gbk') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
            print()
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('程序执行结束')


if __name__ == '__main__':
    main()
