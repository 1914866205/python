"""
写文本文件
"""


def main():
    str = "啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊 阿秋！"
    try:
        #  w写入，如果文件存在，则清空内容写入，不存在则创建
        f = open("./res/阿秋.txt", 'w', encoding='utf-8')
        print(f.write(str))
        f.close

        # a写入，文件存在，则在文件内容后追加写入，不存在则创建
        f = open("./res/阿秋.txt", 'a', encoding='utf-8')
        print(f.write(str))
        f.close

        # with关键字系统会自动关闭文件和处理异常
        with open("./res/阿秋.txt", 'a', encoding='utf-8') as f:
            f.write(str)

    except IOError as e:
        print(e)
    print('写入完毕')


if __name__ == '__main__':
    main()
