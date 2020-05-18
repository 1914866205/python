"""
迭代器节省内存的写法
"""
# 求一组数据的累积乘，如[1,2,3,4]
# 累积乘后返回[1,2,6,24]

# 一般的方法
# 这个方法开辟一段新的内存 rtn 空间复杂度为O(n)


def accumulate_div(a):
    if a is None or len(a) == 0:
        return []
    rtn = [a[0]]
    for i in a[1:]:
        rtn.append(i*rtn[-1])
    return rtn


rtn = accumulate_div([1, 2, 3, 4])
print(rtn)

# 更节省内存的写法


def accountlate_div_new(a):
    if a is None or len(a) == 0:
        return []
    it = iter(a)
    total = next(it)
    # //下次进入方法体直接从这里开始
    yield total
    for i in it:
        total = total*1
        yield total
# 调用生成器函数 accimi;ate_dib,结合for，输出结构


acc = accumulate_div([1, 2, 3, 4])
for i in acc:
    print(i, end='')
print()
# 也可以直接转化为list
rtn = list(accountlate_div_new([1, 2, 3, 4]))
print(rtn)
