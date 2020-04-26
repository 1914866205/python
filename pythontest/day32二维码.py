"""
二维码
pip3 install qrcode
pip3 install myqr
"""
import qrcode
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=8, border=4)
qr.add_data('''
如果有一天，你不再寻找爱情，只是去爱；你不再渴望成功，只是去工作；你不再追求成长，只是去修。那么，一切才真正开始。
''')
img = qr.make_image()
img.save('./res/img/code.png')
qr.add_data('https://www.baidu.com')
img1 = qr.make_image(fill_color='#D32F2F',
                     back_color='#607D8B')
img1.save('./res/img/code1.png')
