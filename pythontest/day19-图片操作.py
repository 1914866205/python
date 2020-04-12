"""
使用Pillow来处理图像：pip3 install Pillow
图片翻转、学习遍历目录和文件、处理网络图片、处理网络图片
"""
# 图片相关
from io import BytesIO
from PIL import Image
import requests as req
from PIL import Image, ImageFilter
# 系统相关
import os
# 打开图片，打印其格式，大小，图片类型
img = Image.open('./res/img/table-test.png')
print(img.format, img.size, img.mode)

# 直接可以复制
Image.open('./res/img/table-test.png').save('./res/img/table-test-copy.png')

# 用thumbnail()方法为其生成原尺寸1/3大小的缩略图
w, h = img.size
img.thumbnail((w//3, h//3))
img.save('./res/img/缩略.png', 'png')

# 使用filter()滤镜，此处使用模糊效果
img = Image.open('./res/img/table-test.png')
img1 = img.filter(ImageFilter.BLUR)
img1.save('./res/img/模糊.png', 'png')

# 翻转
img = Image.open('./res/img/table-test.png')
img1 = img.transpose(Image.FLIP_LEFT_RIGHT)
img1.save('./res/img/左右翻转.png', "PNG")
img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
img1.save('./res/img/上下翻转.png', "PNG")
img1 = img.transpose(Image.ROTATE_90)
img1.save('./res/img/旋转90度.png', 'PNG')
img1 = img.transpose(Image.ROTATE_180)
img1.save('./res/img/旋转180度.png', 'PNG')

# 学习遍历目录和文件
list = os.listdir('./res/img')
# 此处仅遍历img根目录，遍历其子目录可以自行学习
# 使用os.path.splitext(file)[0] 可获得主文件名
# 使用 os.path.splitext(file)[-1] 可获得以.开头的文件后提名
for file in list:
    if os.path.splitext(file)[-1] == '.png':
        print(os.path.splitext(file)[0])

# 处理网络图片
resp = req.get(
    'http://pic1.zhimg.com/100/***.jpg')
image = Image.open(BytesIO(resp.content))
# 在此之前可以做相关处理
image.save('./res/img/test.png')
