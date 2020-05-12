"""
列表生成高效案例-2
"""
# 7.文件列表
import os
list = [d for d in os.listdir('./res/img')]
print(list)

# 8.转为小写
list = ['Hello', 'World', '2019Python']
print([str(w).lower() for w in list])

# 9.保留唯一值


def filter_non_unique(lst):
    return [item for item in lst if lst.count(item) == 1]


list = filter_non_unique([1, 2, 2, 3, 4, 4, 5])
print(list)

# 10.筛选分组


def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]
    ]


print(bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]))

# 11


def bifurcate_by(lst, fn):
    return[
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)],
    ]


print(bifurcate_by(['Python3', 'up', 'users',
                    'people'], lambda x: x[0] == 'u'))

# 12 差集


def difference(a, b):
    _a, _b = set(a), set(b)
    return [item for item in _a if item not in _b]


print(difference([1, 1, 2, 3, 3], [1, 2, 4]))
