from PIL import Image

im = Image.open("D:\CompcuteApplication\projectTest\pythonTest\\res\img\\test.jpg")
# NEAREST 低质量
# BILINEAR 双线性
# BICUBIC 三次样条插值
# ANTIALIAS 高质量
im.resize((10, 10), Image.NEAREST)  # 宽，高  
im.save("D:\CompcuteApplication\projectTest\pythonTest\\res\img\\压缩test.jpg")
