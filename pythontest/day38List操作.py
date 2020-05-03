"""
List操作
"""

# 创建
empty = []
lst = [1, 'xiaopang', 20, '18851855106']
lst2 = ['001', '2020-05-03', ['三文鱼', '电烤箱']]
# 长度
print(len(lst2))
# 遍历
for _ in lst:
    print(f'{_}的类型为{type(_)}')
# 插入删除等操作
sku = lst2[2]
# oppend追加到list尾部
sku.append('烤鸭')
# insert到指定索引处
sku.insert(1, '牛腱子')
# pop移除尾部元素
item = sku.pop()
# remove移除,或者sku.remove(sku[0])
sku.remove('三文鱼')
print(sku)

# 生成1到20的序列，步长为3，放入list
a = list(range(1, 20, 3))
print(a)
# 各种切片操作
print(a[-1], a[:-1], a[1:5], a[1:5:2], a[::3], a[::-3])
