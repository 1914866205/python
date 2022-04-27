from PIL import Image

ascii_char = list('"$%_&WM#*oahkbdqpwmZ0OQLCJUYXzcvunxr\jft/\()1{}?-/+@<>i:;,\~`.')


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = 256 / len(ascii_char)
    # python中“//”是一个算术运算符，表示整数除法，它可以返回商的整数部分（向下取整）。
    return ascii_char[int(gray // unit)]


def main():
    im = Image.open("D:\CompcuteApplication\projectTest\pythonTest\\res\img\\test.jpg")
    WIDTH, HEIGHT = 100, 60
    # NEAREST 低质量
    # BILINEAR 双线性
    # BICUBIC 三次样条插值
    # ANTIALIAS 高质量
    # 此处第三个参数必须要加上，不然报错
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    # 最終输出的文件
    fo = open("D:\CompcuteApplication\projectTest\pythonTest\\res\img\\中文字符画test.txt", "w")
    fo.write(txt)
    fo.close()


main()
# 生成效果图和想象中的不一致
