"""
传递当前目录，批量修改文件后缀名
"""
import argparse
import os


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        # 获取得到文件后缀名
        split_file = os.path.splitext(filename)
        file_ext = split_file[1]
        # 定位后缀名为old_ext的文件
        if old_ext == file_ext:
            # 修改后文件的完整名字
            newfile = split_file[0]+new_ext
            # 实现重命名操作
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
    print("完成重名名")
    print(os.listdir(work_dir))


if __name__ == '__main__':
    batch_rename('./res/img', '.png', '.jpg')
