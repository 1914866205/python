"""
读写json文件
"""
# JSON模块上的四个重要函数
# dump:将python对象按照JSON格序列化到文件中
# dumps:将python对象处理成JSON格式化的字符串
# load：将文件中的JSON数据反序列化成对象
# loads：将字符串的内容反序列化成python对象
import json


def main():
    # 定义字典对象
    mydict = {
        'name': '胖',
        'age': 20
    }
    try:
        # 将字典对象序列化到文件
        with open('./res/pang.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

    try:
        # 从文件中读入，反序列化成对象
        with open('./res/pang.json', 'r', encoding='utf-8') as fs:
            mydict = json.load(fs)
            print(mydict)
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('保存数据完成')


if __name__ == "__main__":
    main()
