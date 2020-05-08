"""
批量压缩文件
"""
# 导入 zipfile,用来做压缩文件，操作
import zipfile
import os
import time


def batch_zip(start_dir):
    # 要压缩的文件路径
    start_dir = start_dir
    # 压缩文件夹的名字
    file_news = start_dir+'.zip'

    z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
    for dir_path, dir_name, file_names in os.walk(start_dir):
        # 不replace的话，就从根路径开始复制
        f_path = dir_path.replace(start_dir, '')
        # 实现当前文件夹以及包含的所有文件的压缩
        f_path = f_path and f_path + os.sep
        for filename in file_names:
            z.write(os.path.join(dir_path, filename), f_path+filename)
        z.close
        return file_news


if __name__ == '__main__':
    batch_zip('./res/img')
