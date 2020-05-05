"""
字典基本操作
"""
# 创建
d = {'a': 1, 'b': 2, 'c': 3}
# 遍历
for key, val in d.items():
    print(key, val)
#  li两种方法获取所有键集合
set(d)
set(d.keys())
# 获取所有值集合
set(d.values())
# 判断键是否在字典中
if 'c' in d:
    print('键c在字典d中')
# 获取某键对应的值
d.get('c')
# 添加或修改一个键值对
d['d'] = 4
print(d)
# 两种方法删除一个键值对
del d['d']
print(d)
d.pop('c')
print(d)
# 字典的三个视图
d = {'a': 1, 'b': 2, 'c': 3}
d.keys()
d.values()
d.items()
