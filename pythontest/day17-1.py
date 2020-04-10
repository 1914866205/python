""""
读写二进制文件

"""


def main():
    try:
        # 将图片以二进制只读方式打开，读入data变量
        with open('./res/对AOP的理解.png', 'rb') as fs1:
            data = fs1.read()
        # 将图二进制写的方式打开，写入1.jpg
        with open("./res/1.png", 'rb') as fs2:
            print(data)
            fs2.write(data)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('程序执行结束')


if __name__ == '__main__':
    main()
