"""
微信好友头像照片墙
"""
# 微信
import itchat
# 随机数
import random
# 数学运算
import math
# 操作系统  取文件
import os
# 图片处理
from PIL import Image


def wechat_friend_avatar():
    # 登录微信
    itchat.login()
    # 获取好友 列表
    friends = itchat.get_friends(update=True)
    for count, f in enumerate(friends):
        # 取得每位好友的头像
        img = itchat.get_head_img(userName=f["Username"])
        # 保存头像
        imgFile = open("./res/avatar/"+str(count)+".jpg", "wb")
        imgFile.write(img)
        imgFile.close()


def picture_wall():
    x = 0
    y = 0
    # 读取目录下所有文件
    imgs = os.listdir('./res/avatar')
    # 将序列的所有元素随机排序
    random.shuffle(imgs)
    # 创建640*640的图片用于填充图片
    newImg = Image.new('RGBA', (640, 640))
    # 以640*640来拼接图片。math.sart()开平方根计算啊每张小图片的宽高
    width = int(math.sqrt(640*640/len(imgs)))
    # 每行图片数
    numLine = int(640/width)
    for imgName in imgs:
        img = Image.open('./res/avatar/'+imgName)
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片。一行排满，换行拼凑
        newImg.paste(img, (x*width, y*width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
            newImg.save('./res/all.png')


if __name__ == '__main__':
    # wechat_friend_avatar()
    picture_wall()
