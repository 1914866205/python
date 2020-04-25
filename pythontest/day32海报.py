"""
使用Pillpw生成海报
"""
from PIL import Image, ImageDraw, ImageFont
import time

header = "001"
title = "鹊桥仙.纤云弄巧"
books = ['秦观诗传']
writes = ['秦观', '宋']
summary = ['''纤云弄巧，飞星传恨，银汉迢迢暗度。

金风玉露一相逢，便胜却、人间无数。

柔情似水，佳期如梦，忍顾鹊桥归路。

两情若是久长时，又岂在、朝朝暮暮。''']
n = 18
summary_list = [summary[i:i+n]for i in range(0, len(summary), n)]

# 背景图
img = './res/img/首页.png'
# 生成图片
new_img = './res/img/result.png'
# 压缩后的图片
compress_img = './res/compress.png'

# 设置字体样式
font_type = './res/font/SimHei.ttf'
font_medium_type = './res/font/SimHei.ttf'
header_font = ImageFont.truetype('./res/font/SimHei.ttf', 40, encoding='utf-8')
title_font = ImageFont.truetype('./res/font/SimHei.ttf', 30, encoding='utf-8')
font = ImageFont.truetype(font_type, 24)
color = "#000000"
# 打开图片
image = Image.open(img)
draw = ImageDraw.Draw(image)
width, height = image.size
# header头
header_x = 130
header_y = 690
draw.text((header_x, height-header_y), u'%s' % header, color, header_font)

# 标题
title_x = header_x
title_y = header_y-80
draw.text((title_x, height-title_y), u'%s' % title, color, title_font)
# 当前时间
cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
cur_time_x = 590
cur_time_y = title_y-25
cur_time_font = ImageFont.truetype(font_type, 25)
draw.text((cur_time_x, height-cur_time_y), u'%s' %
          cur_time, color, cur_time_font)
# 阅读
book_x = title_x+5
book_start_y = title_y-190
book_y = 0
book_line = 50
for num, book in enumerate(books):
    y = book_start_y-num*book_line
    book_num = num+1
    draw.text((book_x, height-y), u'%s. %s' % (book_line, book), color, font)
# 写作
write_x = book_x
write_y = title_y-450
write_line = 40
for num, write in enumerate(writes):
    write_num = num+1
    y = write_y-num*write_line
    draw.text((write_x, height-y), u'%s. %s' %
              (write_num, write), color, font)
# 哲思
summary_x = book_x+460
summary_y = book_start_y
summary_line = 35
for num, summary in enumerate(summary_list):
    y = summary_y-num*summary_line
    draw.text((summary_x, height-y), u'%s' % summary, color, font)

# 生成图片
image.save(new_img, 'png')
# 压缩图片
sImg = Image.open(new_img)
w, h = sImg.size
width = int(w/2)
height = int(h/2)
dImg = sImg.resize((width, height), Image.ANTIALIAS)
dImg.save(compress_img)
