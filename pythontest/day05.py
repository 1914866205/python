"""
判断一组文件中图片的个数
"""


import random


def count_image(file_list):
    """
    file_list:文件列表
    """
    count = 0
    for file in file_list:
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('webp') or file.endswith('bmp'):
            count = count + 1
    return count


# 调用函数
img_list = ['image.jpg', 'images.mp3', 'image2.png', 'w1.webp', 'aea.bmp']
result = count_image(img_list)
print('一共有', result, '个图片文件')


"""
设计一个 函数产生指定长度的验证码，验证码由大小写字母的和数字构成
"""


def generater_code(code_len=4):
    all_chars = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


result2 = generater_code(200)
print(result2)
