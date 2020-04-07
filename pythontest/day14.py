"""
元组类型练习
"""

# 定义元组

import hashlib
t = ('倪涛涛', 20, True, '江苏徐州')
print(t)
# 获取元组中发元素
print(t[0])
print(t[1])
# 遍历元组中的值
for member in t:
    print(member)

# 重新给元组赋值
# t[0]='ntt' # TypeError
# 变量t重新引用了新的元组，原来的元组被垃圾回收器回收
t = ('ntt', 22, True, '江苏徐州')
print(t)
# 将元组数据转成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '小胖'
person[1] = 10
print(person)
# 将列表转成元组
fruits_list = ['apple', 'banana', 'pear']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


"""
对字符串进行32位加密
"""


def hash_cry32(s):
    m = hashlib.md5()
    m.update((str(s).encode('utf*8')))
    return m.hexdigest()


print(hash_cry32(27))
print(hash_cry32('ntt'))
