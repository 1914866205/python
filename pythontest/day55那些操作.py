"""
那些操作
"""
# 字典按value排序并返回新字典
d = {'a': 12, 'b': 50, 'c': 1, 'd': 20}
# 使用Python 内置函数sorted排序
d = dict(sorted(d.items(), key=lambda item: item[1]))
print(d)

# 删除list 里重复元素，并保证元素顺序不变


def del_duplicated(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b


a = [3, 5, 4, 2, 2, 4]
print(del_duplicated(a))

# 找出两个列表的相同元素和不同元素


def ana(a, b):
    aset, bset = set(a), set(b)
    same = aset.intersection(bset)
    differ = aset.difference(bset).union(bset.difference(aset))
    return same, differ


a = [3, 2, 5, 4, 2, 4, 2]
b = [2, 2, 56, 6, 1, 3, 1, 3, 5, 2]
print(ana(a, b))
