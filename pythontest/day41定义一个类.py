"""
定义一个类
"""


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repf__(self):
        return 'id = '+self.id+',name='+self.name


xiaoming = Student('001', 'xiaoming')
# 返回对象的哈希值
print(hash(xiaoming))
# 返回对象的内存地址
print(id(xiaoming))
# 如果迭代器的所有元素都为真，返回True，否则返回False
print(any([0, 0, 1]))
# 分别将十进制转成二进制，八进制，十六进制
print(bin(10))
print(oct(9))
print(hex(15))
