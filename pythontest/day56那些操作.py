"""
那些操作
"""
# 字符串处理成字典
s = 'k0:10|k1:2|k2:11|k3:5'
m = map(lambda x: x.split(':'), s.split('|'))
print({mi[0]: int(mi[1])for mi in m})

# 使用filter()求出列表中大于10的元素
a = [15, 2, 7, 56, 3, 45, 6, 4, 62, -51]
b = list(filter(lambda x: x > 10, a))

print(b)

# 列表内元素可重复出现，如何删除列表中的某个元素


def del_item(lst, e):
    for i in lst:
        if i == e:
            lst.remove(i)
    return list


s = del_item([1, 3, 5, 3, 6, 4, 3], 3)
print(s)
# 上述代码好像成功的删除了元素3
# 可是看下面的代码
s = del_item([1, 3, 5, 3, 12, 3, 4, 6], 3)
print(s)

# 这是为什么呢？
# 因为变量 lst，remove，一次，移掉#位置i后的所有元素索引都要减一
# 所以一旦删除的元素重复出现在列表中，总会漏掉一个该删除的元素
# 正确做法，找到被删除元素后，删除，同时下次遍历索引不加一，若未找到，遍历索引加一


def del_item2(lst, e):
    i = 0
    while i < len(lst):
        if lst[i] == e:
            lst.remove(lst[i])
        else:
            i += 1
    return lst


# 再次调用看结果
s = del_item2([1, 23, 2, 3, 4, 3, 5], 3)
print(s)
