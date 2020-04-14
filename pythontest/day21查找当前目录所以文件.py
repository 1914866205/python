"""
查找当前目录所有文件
"""

import os


def get_all(cwd):
    result = []
    # 遍历当前目录，获取文件列表
    get_dir = os.listdir(cwd)
    # print(get_dir):
    for i in get_dir:
        # 第一步获取的文件加入路径
        print(i)
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)
            result.append(file_name)
    return result


if __name__ == "__main__":
    # 取得当前目录:/home/ntt/python-learning,拼上子目录
    cur_path = os.getcwd()+'/res'
    print(cur_path)
    print("*************************")
    # 调用函数，统计res目录下的文件
    print('当前目录的所有文件', get_all(cur_path))
